import streamlit as st


def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon = ":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your document") # lable on top of user input

    # Sidebar
    with st.sidebar:  
        st.subheader("your document")
        st.file_uploader("Upload your PDFs here and click on 'Process")
        st.button("Process")

if __name__ == '__main__':
    main()