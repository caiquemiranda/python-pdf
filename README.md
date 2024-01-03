## Python PDF Manipulation

Este repositório contém um código simples em Python para manipulação de arquivos PDF. O objetivo principal é oferecer uma ferramenta leve e fácil de entender para realizar tarefas comuns relacionadas a PDFs, como mesclar, dividir e extrair páginas.

### Funcionalidades

**Mesclagem de PDFs:**
Combinação de vários arquivos PDF em um único documento.

**Divisão de PDFs:**
Separação de um documento PDF em arquivos menores com base em intervalos de páginas.

**Extração de Páginas:**
Criação de um novo PDF contendo páginas específicas extraídas de um documento existente.

#### Requisitos

Certifique-se de ter o Python instalado em seu ambiente. Além disso, você precisará instalar a biblioteca PyPDF2, que é utilizada para manipulação de PDFs. Você pode instalá-la usando o seguinte comando:

```bash
pip install PyPDF2
```


**Mesclagem de PDFs:**
```python
from pdf_manipulator import merge_pdfs

pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
output_file = 'merged.pdf'

merge_pdfs(pdf_files, output_file)

```

**Divisão de PDFs:**

```python
from pdf_manipulator import split_pdf

input_file = 'original.pdf'
output_files_prefix = 'split'
page_ranges = [(1, 3), (4, 6), (7, 10)]

split_pdf(input_file, output_files_prefix, page_ranges)
```

**Extração de Páginas:**

```python
from pdf_manipulator import extract_pages

input_file = 'original.pdf'
output_file = 'extracted_pages.pdf'
pages_to_extract = [2, 4, 6]

extract_pages(input_file, output_file, pages_to_extract)
```
