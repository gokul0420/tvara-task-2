from pypdf import PdfReader

def load_pdf(path: str)->str:
    try:
        reader=PdfReader(path)
    except Exception:
        raise ValueError("Cant read pdf")
    
    text=""
    page_text=""
    for i in reader.pages:
        page_text+=i.extract_text()
        if page_text:
            text+=page_text+"\n"
    if not text.strip():
        raise ValueError("PDF is empty")
    return text