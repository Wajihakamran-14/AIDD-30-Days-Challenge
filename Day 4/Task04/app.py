import streamlit as st
from main import extract_text_from_pdf, summarize_text, generate_quiz
import os

st.set_page_config(layout="wide")
st.title("📑 PDF Summarizer and Quiz Generator")
st.write("Upload a PDF to get a summary and generate a quiz.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Display file details
    st.write("🎉File uploaded successfully!")
    st.write(f"File name: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size / 1024:.2f} KB")

    try:
        # Extract text
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
        
        if text:
            st.success("✅ Text extracted successfully!")
            
            # Summarize text
            with st.spinner("Generating summary..."):
                summary = summarize_text(text)
            
            if summary:
                st.subheader("Summary")
                
                # Allow user to choose display style
                display_style = st.radio(
                    "Choose summary display style:",
                    ('Card', 'Block', 'Expander'),
                    index=0
                )
                
                if display_style == 'Card':
                    st.info(summary)
                elif display_style == 'Block':
                    st.markdown(f"```\n{summary}\n```")
                elif display_style == 'Expander':
                    with st.expander("Click to view summary"):
                        st.write(summary)

                st.session_state['summary'] = summary
                st.session_state['original_text'] = text

            else:
                st.error("Could not generate summary.")
        else:
            st.error("Could not extract text from PDF. The file might be empty or unreadable.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Quiz Generation
if 'original_text' in st.session_state and st.session_state['original_text']:
    if st.button("Create Quiz"):
        try:
            with st.spinner("Generating quiz... This might take a while."):
                quiz = generate_quiz(st.session_state['original_text'])
            
            if quiz:
                st.subheader("Generated Quiz")
                st.write(quiz)
            else:
                st.error("Could not generate quiz.")
        except Exception as e:
            st.error(f"An error occurred during quiz generation: {e}")
else:
    st.info("Upload a PDF and get a summary first to enable quiz generation.")
    
