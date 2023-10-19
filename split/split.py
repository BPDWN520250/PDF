import PyPDF2
import os

'''
PyPDF2==3.0.1
pycryptodome==3.19.0
'''


# 按照特定的页码对pdf进行切分 start_page表示pdf开始的页码 end_page表示切分位置页码
def spilt_pdf(input_data_path, end_page):
    data = PyPDF2.PdfReader(input_data_path)
    if end_page > len(data.pages):
        print('切分页码超过pdf总页码')
    else:
        writer = PyPDF2.PdfWriter()
        for page in range(0, end_page):
            writer.add_page(data.pages[page])
            with open('first_out.pdf', "wb") as output_stream:
                writer.write(output_stream)
        writer = PyPDF2.PdfWriter()
        for page in range(end_page, len(data.pages)):
            writer.add_page(data.pages[page])
            with open('second_out.pdf', "wb") as output_stream:
                writer.write(output_stream)


def input_path():
    # path = os.path.dirname(__file__)
    # print(path)
    ls = os.listdir()
    data_list = []
    for data in ls:
        if data.endswith('pdf'):
            data_list.append(data)
    if not data_list:
        raise FileNotFoundError("No PDF files found in the directory.")
    input_data_path = data_list[0]
    return input_data_path


if __name__ == '__main__':
    input_data_path = input_path()
    print('将要切分的文件',input_data_path)
    end_page = int(input('请输入切分的位置:'))
    spilt_pdf(input_data_path,end_page)

