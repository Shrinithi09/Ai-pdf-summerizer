import streamlit as st
from transformers import pipeline
import PyPDF2

st.title("📚 AI PDF Topic Summarizer")

# Load summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

pipe = load_model()

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
topic = st.text_input("Enter topic to summarize")

if uploaded_file and topic:

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    # Extract text from PDF
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Split text into paragraphs
    paragraphs = text.split("\n")

    relevant_paragraphs = []

    # Find paragraphs related to topic
    for para in paragraphs:
        if topic.lower() in para.lower():
            relevant_paragraphs.append(para)

    if len(relevant_paragraphs) == 0:
        st.error("Topic not found in the PDF")

    else:

        topic_text = " ".join(relevant_paragraphs)

        # Handle long text
        chunk_size = 1000
        chunks = []

        for i in range(0, len(topic_text), chunk_size):
            chunks.append(topic_text[i:i+chunk_size])

        summaries = []

        with st.spinner("Generating summary..."):

            for chunk in chunks:
                result = pipe(
                    chunk,
                    max_length=200,
                    min_length=80,
                    do_sample=False
                )
                summaries.append(result[0]["summary_text"])

        final_summary = " ".join(summaries)

        st.subheader("Summary")
        st.write(final_summary)