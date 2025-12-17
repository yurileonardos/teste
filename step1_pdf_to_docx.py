from pdf2docx import Converter
from io import BytesIO
import tempfile


def pdf_to_docx(pdf_bytes):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as pdf_tmp:
        pdf_tmp.write(pdf_bytes)
        pdf_tmp.flush()

        docx_tmp = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)

        cv = Converter(pdf_tmp.name)
        cv.convert(docx_tmp.name)
        cv.close()

        with open(docx_tmp.name, "rb") as f:
            return f.read()
