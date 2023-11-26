import PyPDF2


def separar_paginas_pdf(arquivo_origem, arquivo_destino, pagina_inicio, pagina_fim):
    # Abrir o PDF original
    pdf_original = PyPDF2.PdfReader(arquivo_origem)

    # Criar um novo PDF
    escritor_pdf = PyPDF2.PdfWriter()

    # Adicionar páginas do PDF original ao novo PDF
    for pagina in range(pagina_inicio, pagina_fim + 1):
        escritor_pdf.add_page(pdf_original.pages[pagina])

    # Salvar o novo PDF
    with open(arquivo_destino, 'wb') as pdf_novo:
        escritor_pdf.write(pdf_novo)


# Exemplo de uso
separar_paginas_pdf('pdf/entrada/python_book.pdf',
                    'pdf/saida/paginas_separadas.pdf',
                    0, 55)  # Separa as páginas 1 a 55
