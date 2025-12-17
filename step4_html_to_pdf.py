from weasyprint import HTML
from io import BytesIO


def html_to_pdf(html):
    pdf_io = BytesIO()
    HTML(string=html).write_pdf(pdf_io)
    pdf_io.seek(0)
    return pdf_io.read()
