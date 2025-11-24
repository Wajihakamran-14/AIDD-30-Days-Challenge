**Role** Senior Python AI Engineer. Your task is to build a PDF Summarizer and Quiz Generator Agent using Agentic AI.  

Instructions:

1️⃣ **Project Structure**
- **main.py** → contains all agent logic using OpenAgents SDK.  
- **app.py** → contains the front-end UI (Streamlit, HTML/CSS optional).  
- **.env** → stores the Gemini API key.  
- **requirements.txt** → lists all dependencies.

2️⃣ **Agent Tools & SDK**
- Use **PyPDF** for PDF text extraction.
- Use these tools from Mcp for **OpenAgents SDK**:
    - get-library-docs
    - resolve-library-id
- Use **OpenAgents SDK** for agent creation, including classes and functions such as:
    - Runner
    - OpenAI Chat Completion
    - Function Tools
    - Agents
    - AsyncIO
- All syntax and documentation must be taken **exactly from MCP**. No guessing or hallucination.

3️⃣ **Agent Functionality**
- **PDF Summarizer**
    - User uploads a PDF (handled in `app.py`).
    - Extract text using PyPDF (in `main.py`).
    - Generate a concise and meaningful summary using Gemini 2.5-flash model.
    - Summary should be displayable in multiple UI styles (card, block, container, expander, etc.) chosen by the user.
- **Quiz Generator**
    - After summarization, user can click “Create Quiz”.
    - Generate quiz using **original PDF text**, not the summary.
    - Include:
        - 10+ MCQs with 4 options (A, B, C, D) with hidden correct answers
        - Mixed question types (True/False, Fill-in-the-Blank)
    - Quiz output must be clear and user-friendly.

4️⃣ **Execution & Environment**
- The agent must be runnable in Python.
- Handle errors gracefully (file upload errors, text extraction issues, API errors).
- Ensure multi-page PDFs and large files are supported.
- All dependencies should be listed in **requirements.txt**.
- Gemini API key must be loaded from `.env`.

5️⃣ **Critical Instructions**
- Use exact syntax from **OpenAgents SDK documentation** in MCP.  
- **Do not add extra functionality** outside the requirements above.  
- Generate fully modular Python code:
    - `main.py` → agent logic (summarization + quiz generation)
    - `app.py` → front-end UI
    - `.env` → API key
    - `requirements.txt` → all packages


all this implemtation in UV Project Task04 folder 