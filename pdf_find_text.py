# Py PDF Find Extract
# v1.0
# created by: Earl L
# python forum
# MAC

import pdfplumber

pdf_file = '/Users/name/python/scripts/document.pdf' 
search_word = 'Page (1)'

with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for page_nr, pg in enumerate(pages, 1):
        content = pg.extract_text()
        if search_word in content:
            print(f'<{search_word}> found at page number <{page_nr}> '\
                f'at index <{content.index(search_word)}>')
