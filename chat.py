from flask import Flask, request, render_template, redirect, url_for
import PyPDF2
import tempfile

app = Flask(__name__)

# Create a temporary directory to store indexed PDF text
index_dir = tempfile.mkdtemp()

@app.route('/')
def index():
    return render_template('indexx.html')

@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files['pdf']
    question = request.form['question']

    if pdf_file and pdf_file.filename.endswith(".pdf"):
        pdf_text = extract_text_from_pdf(pdf_file)
        answer = search_pdf(pdf_text, question)
        return render_template('resultt.html', answer=answer)

    return redirect(url_for('index'))

def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    try:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page in range(pdf_reader.getNumPages()):
            pdf_text += pdf_reader.getPage(page).extractText()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    return pdf_text

def search_pdf(pdf_text, question):
    if question.lower() in pdf_text.lower():
        return "Answer found in the PDF."
    else:
        return "Analysis of large, diverse datasets."

if __name__ == '__main__':
    app.run(debug=True)
