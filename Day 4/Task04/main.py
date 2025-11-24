import os
import io
import asyncio
from dotenv import load_dotenv
from pypdf import PdfReader
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI


# Load environment variables
load_dotenv()

# Read API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in environment. Add it to your .env file.")

# --- Gemini API client (OpenAI-compatible wrapper) ---
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",   # Correct endpoint
)

# --- Correct model wrapper for Agent SDK ---
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",         # Model name
    openai_client=external_client     # Gemini client passed here
)


# ---------------------------------------------------
# PDF TEXT EXTRACTION
# ---------------------------------------------------
def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF using PyPDF.
    """
    if pdf_file is None:
        return None

    try:
        pdf_bytes = pdf_file.read()
        pdf_reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text

    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"


# ---------------------------------------------------
# SUMMARY GENERATION
# ---------------------------------------------------
async def summarize_text_async(text: str) -> str:
    """
    Summarize the extracted text using Gemini 2.5 Flash.
    """
    summarizer_agent = Agent(
        name="PDF Summarizer Agent",
        instructions=(
            "You are an expert summarizer. Produce a clean, meaningful summary "
            "containing the core ideas, important concepts, and main arguments. "
            "Keep the wording simple and coherent."
        ),
        model=model
    )

    result = await Runner.run(
        summarizer_agent,
        input=f"Summarize this document:\n\n{text}"
    )

    return result.final_output


def summarize_text(text: str) -> str:
    return asyncio.run(summarize_text_async(text))


# ---------------------------------------------------
# QUIZ GENERATION
# ---------------------------------------------------
async def generate_quiz_async(text: str) -> str:
    """
    Generate MCQs 
    """
    quiz_agent = Agent(
        name="Quiz Generator",
        instructions="""You are an expert academic quiz generator. You MUST follow these formatting rules exactly:

        === QUIZ FORMAT RULES (STRICT) ===
1. Each question MUST appear on its own new line.
2. Each option (A, B, C, D) MUST appear on its own new line.
3. Leave exactly ONE blank line between each question block.
4. reveal correct answers in last section only, do NOT mix with questions.
5. Keep questions clear, simple, and readable.
6. questions should directly reference the original text.
7. question should be bolded.
8. Use this MCQ structure exactly:
9. heading should be bolded and ### Section 1 — Multiple Choice Questions
Q1. Your question text?

A) Option A

B) Option B

C) Option C

D) Option D

Q2. Next question...
A) ...
B) ...
C) ...
D) ...

=== REQUIRED OUTPUT SECTIONS ===

Section 1 — Multiple Choice Questions
- At least 10 MCQs
- Format exactly as shown above

=== IMPORTANT ===
- Use ONLY the original PDF text as reference.
- NEVER mix paragraphs together.
- NEVER collapse questions into a single paragraph.
""",
        model=model
    )

    result = await Runner.run(
        quiz_agent,
        input=f"Create a quiz from this document:\n\n{text}"
    )

    return result.final_output


def generate_quiz(text: str) -> str:
    return asyncio.run(generate_quiz_async(text))
