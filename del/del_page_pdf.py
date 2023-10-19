import PyPDF2
import os
'''
PyPDF2==3.0.1
pycryptodome==3.19.0
'''


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


# 删除pdf中指定的页码：
def del_page_pdf(input_data_path, page_num):
    data = PyPDF2.PdfReader(input_data_path)
    writer = PyPDF2.PdfWriter()
    for page_index in range(len(data.pages)):
        if page_index != page_num:
            page = data.pages[page_index]
            writer.add_page(page)
        else:
            pass
    with open('del_output.pdf', 'wb') as file:
        writer.write(file)


if __name__ == '__main__':
    # input_data_path = 'input.pdf'
    # output_data_path = 'output.pdf'
    start_page = 0
    end_page = 3
    # spilt_pdf(input_data_path, output_data_path, start_page, end_page)
    # insert_pdf('input.pdf', 'second_output.pdf')
    input_data_path = input_path()
    print(input_data_path)
    del_page = int(input('请输入需要删除的页码:'))
    # del_page = 0
    del_page_pdf(input_data_path, del_page)
