import pdfrw

def merge_pdfs(input_files, output_file):
    output = pdfrw.PdfWriter()

    for file in input_files:
        input_pdf = pdfrw.PdfReader(file)
        output.addpages(input_pdf.pages)

    with open(output_file, 'wb') as f:
        output.write(f)

if __name__ == '__main__':
    input_files = ['file1.pdf', 'file2.pdf']  # 替换为您要合并的 PDF 文件名
    output_file = 'merged.pdf'  # 合并后的文件名
    merge_pdfs(input_files, output_file)
