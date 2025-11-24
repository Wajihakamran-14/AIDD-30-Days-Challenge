# PDF Summarizer and Quiz Generator

This project is an AI-powered agent that summarizes PDF documents and generates quizzes from their content. It's built using Python, the OpenAgents SDK, and Google's Gemini model. The user interface is created with Streamlit.

## Features

-   Upload a PDF file.
-   Generate a concise summary of the PDF content.
-   Create a quiz with multiple-choice, true/false, and fill-in-the-blank questions based on the original PDF text.

## Project Structure

-   `main.py`: Contains the agent logic for summarization and quiz generation.
-   `app.py`: The Streamlit-based web interface.
-   `.env`: Stores the Gemini API key.
-   `requirements.txt`: Lists all project dependencies.

## Setup and Usage

1.  **Clone the repository.**
2.  **Create a virtual environment.**
3.  **Install dependencies:** 
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up your API Key:** Create a `.env` file in the project root and add your Gemini API key:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```
5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```
