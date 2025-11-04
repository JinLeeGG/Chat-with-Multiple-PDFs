# MultiPDF Chat App

A powerful chatbot application that allows users to upload multiple PDF documents and interact with their content through natural language queries. Built with OpenAI API, LangChain, and Streamlit for an intuitive user experience.

## Features

- 📄 **Multiple PDF Support**: Upload and process multiple PDF documents simultaneously
- 💬 **Interactive Chat Interface**: Ask questions about your documents in natural language
- 🔍 **Intelligent Search**: Uses vector embeddings for accurate content retrieval
- 🤖 **OpenAI Integration**: Powered by OpenAI's language models for contextual responses
- 📊 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
 
## Technology Stack

- **LangChain**: Framework for building LLM applications
- **Streamlit**: Web application framework for the user interface
- **OpenAI**: Language model for generating responses
- **PyPDF2**: PDF processing and text extraction
- **FAISS**: Vector database for efficient similarity search
- **Tiktoken**: Token counting for OpenAI models

## Requirements

- Python 3.10.11
- OpenAI API key

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd multipdf-chat-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install langchain PyPDF2 python-dotenv streamlit openai faiss-cpu altair tiktoken langchain-community
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   Open your browser and navigate to `http://localhost:8501`

3. **Upload PDF documents**
   - Use the file uploader to select one or multiple PDF files
   - Wait for the documents to be processed

4. **Start chatting**
   - Type your questions about the uploaded documents
   - Get intelligent responses based on the document content

## How It Works

1. **Document Processing**: PDFs are uploaded and text is extracted using PyPDF2
2. **Text Chunking**: Large documents are split into manageable chunks
3. **Embeddings**: Text chunks are converted to vector embeddings
4. **Vector Storage**: Embeddings are stored in FAISS for efficient retrieval
5. **Query Processing**: User questions are embedded and matched against document vectors
6. **Response Generation**: Relevant document sections are sent to OpenAI for contextual answers

## Demo

![Demo GIF](demo/chatwithpdf_demo.gif)

*Add your demo GIF file to showcase the application in action*

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your OpenAI API key is correctly set in the `.env` file
   - Verify the key has sufficient credits

2. **PDF Processing Issues**
   - Check that PDF files are not password-protected
   - Ensure PDFs contain extractable text (not just images)

3. **Memory Issues**
   - For large PDFs, consider reducing chunk size
   - Monitor system memory usage

4. **Dependency Conflicts**
   - Use a virtual environment to avoid package conflicts
   - Ensure Python version 3.10.11 is being used

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the language model API
- LangChain community for the excellent framework
- Streamlit team for the user-friendly web framework

## Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Note**: Remember to keep your OpenAI API key secure and never commit it to version control.
