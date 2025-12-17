from pdf2image import convert_from_bytes
from docx import Document
from docx.shared import Cm
from io import BytesIO


def pdf_to_images_docx(pdf_bytes):
    images = convert_from_bytes(pdf_bytes)
    doc = Document()

    for img in images:
        bio = BytesIO()
        img.save(bio, format="JPEG", quality=90)
        bio.seek(0)

        doc.add_picture(bio, width=Cm(18))
        doc.add_page_break()

    output = BytesIO()
    doc.save(output)
    output.seek(0)
    return output
