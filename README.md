# 📚 AI PDF Topic Summarizer

This project is an AI-powered web application that summarizes specific topics from uploaded PDF documents. The application allows users to upload a PDF (such as lecture notes or textbooks), enter a topic name, and receive a concise summary generated using a pretrained Hugging Face Transformer model.

The system uses **facebook/bart-large-cnn**, a powerful text summarization model, to generate summaries from relevant sections of the PDF.

---

## 🚀 Features

* Upload any PDF document
* Enter a specific topic to search within the PDF
* Extract relevant paragraphs containing the topic
* Generate an AI-powered summary using Hugging Face Transformers
* Interactive web interface built with **Streamlit**

---

## 🧠 Model Used

The summarization is performed using the pretrained model:

facebook/bart-large-cnn

This model is designed for high-quality text summarization and is widely used for summarizing articles and documents.

---

## 🛠 Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* PyPDF2

---

## 📂 Project Structure

```
ai-pdf-summarizer
│
├── summerizer.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/ai-pdf-summarizer.git
```

Navigate to the project folder:

```
cd ai-pdf-summarizer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app:

```
streamlit run summerizer.py
```

The application will open in your browser.

---

## 💻 How It Works

1. Upload a PDF document.
2. Enter the topic you want summarized.
3. The system scans the PDF for paragraphs containing the topic.
4. Relevant text is extracted and passed to the Hugging Face summarization model.
5. The model generates a concise summary of the topic.

---

## 🌐 Deployment

The application can be deployed easily using:

* Streamlit Community Cloud
* Hugging Face Spaces
* Render

---



* Summarizing lecture notes
* Extracting explanations of specific concepts from textbooks
* Quickly reviewing large study materials
* Research paper topic summarization

---

##License

This project is for educational and research purposes.
