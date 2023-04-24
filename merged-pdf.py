import pdfrw

def merge_pdfs(input_files, output_file):
    output = pdfrw.PdfWriter()

    for file in input_files:
        input_pdf = pdfrw.PdfReader(file)
        output.addpages(input_pdf.pages)

    with open(output_file, 'wb') as f:
        output.write(f)

if __name__ == '__main__':
    input_files = ['第7期決算報告書.pdf', '令和3年分法定調書.pdf', '履歴事項全部証明書　7月24日まで.pdf', '住民票.pdf', '在籍証明書.pdf', '签证更新(个人部).pdf', 'ビザ更新申請書　会社記入部分.pdf']  # 替换为您要合并的 PDF 文件名
    output_file = 'merged.pdf'  # 合并后的文件名
    merge_pdfs(input_files, output_file)
