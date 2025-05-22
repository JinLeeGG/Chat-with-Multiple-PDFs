import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = "" # storing all texts from pdfs
    for pdf in pdf_docs: # looping all pdfs
        pdf_reader = PdfReader(pdf) # read pdf
        for page in pdf_reader.pages: # loop each pages of pdfs
            text += page.extract_text() # append it to text 
    
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon = ":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your document") # lable on top of user input

    # Sidebar
    with st.sidebar:  
        st.subheader("your document")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True) # this enables to upload multiple files
        if st.button("Process"):
            with st.spinner("Processing"): # while the spinning wheel is spinning (processing)
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chucks = get_text_chunks(raw_text)
                st.write(text_chucks)

                
                # create vector store

if __name__ == '__main__':
    main()