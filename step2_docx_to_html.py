import mammoth
from io import BytesIO


def docx_to_html(docx_bytes):
    with BytesIO(docx_bytes) as f:
        result = mammoth.convert_to_html(f)
        return result.value
