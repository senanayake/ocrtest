import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import sys

def extract_text_from_pdf(pdf_path, output_text_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Open the output text file
    with open(output_text_path, 'w') as output_file:
        # Loop through each page
        for page_num in range(pdf_document.page_count):
            # Get the page
            page = pdf_document.load_page(page_num)
            
            # Render page to an image
            pix = page.get_pixmap()
            img_data = pix.pil_tobytes(format="png")
            img = Image.open(io.BytesIO(img_data))
            
            # Use OCR to extract text from the image
            text = pytesseract.image_to_string(img)
            
            # Write the extracted text to the output file
            output_file.write(f"--- Page {page_num + 1} ---\n")
            output_file.write(text)
            output_file.write("\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_path> <output_text_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_text_path = sys.argv[2]
    
    extract_text_from_pdf(pdf_path, output_text_path)
