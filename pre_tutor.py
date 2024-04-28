import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text




# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_text = extract_text_from_pdf(r"pdf_data/Lecture 9_Times Series Forecasting (Stationary Data)(3).pdf")
print(pdf_text)
