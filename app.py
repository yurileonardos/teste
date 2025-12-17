from step1_pdf_to_docx import pdf_to_docx
from step2_docx_to_html import docx_to_html
from step3_html_edit_tables import remove_price_columns
from step4_html_to_pdf import html_to_pdf
from step5_pdf_to_images_docx import pdf_to_images_docx

if tr_file:
    docx_raw = pdf_to_docx(tr_file.read())
    html_raw = docx_to_html(docx_raw)
    html_clean = remove_price_columns(html_raw)
    pdf_clean = html_to_pdf(html_clean)
    docx_final = pdf_to_images_docx(pdf_clean)

    st.download_button(
        "📥 Baixar TR (Word – sem preços)",
        docx_final,
        file_name="TR_SEM_PRECOS.docx"
    )
