import os
import sys

def try_extract():
    pdf_path = "GUIDEBOOK BPC IFEST 2026.pdf"
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        return

    # Try pypdf
    try:
        import pypdf
        print("Using pypdf...")
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- PAGE {idx+1} ---\n" + page_text
        with open("guidebook_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted guidebook text using pypdf to guidebook_text.txt.")
        return
    except ImportError:
        print("pypdf not available.")

    # Try fitz (PyMuPDF)
    try:
        import fitz
        print("Using PyMuPDF (fitz)...")
        doc = fitz.open(pdf_path)
        text = ""
        for idx, page in enumerate(doc):
            page_text = page.get_text()
            if page_text:
                text += f"\n--- PAGE {idx+1} ---\n" + page_text
        with open("guidebook_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted guidebook text using PyMuPDF to guidebook_text.txt.")
        return
    except ImportError:
        print("fitz not available.")

    # Try pdfplumber
    try:
        import pdfplumber
        print("Using pdfplumber...")
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for idx, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- PAGE {idx+1} ---\n" + page_text
        with open("guidebook_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted guidebook text using pdfplumber to guidebook_text.txt.")
        return
    except ImportError:
        print("pdfplumber not available.")

    print("No pdf extraction library found. Let's try to install pypdf via pip.")
    # Try running pip install pypdf inline if possible
    try:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- PAGE {idx+1} ---\n" + page_text
        with open("guidebook_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully installed and extracted guidebook text using pypdf to guidebook_text.txt.")
    except Exception as e:
        print(f"Failed to install or run pypdf: {e}")

if __name__ == "__main__":
    try_extract()
