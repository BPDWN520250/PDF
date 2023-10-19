import PyPDF2
import os

'''
PyPDF2==3.0.1
pycryptodome==3.19.0
'''


# 按照特定的页码对pdf进行切分 start_page表示pdf开始的页码 end_page表示切分位置页码
def spilt_pdf(input_data_path, start_page, end_page):
    data = PyPDF2.PdfReader(input_data_path)
    if end_page > len(data.pages):
        print('切分页码超过pdf总页码')
    else:
        writer = PyPDF2.PdfWriter()
        for page in range(start_page, end_page):
            writer.add_page(data.pages[page])
            with open('first_out', "wb") as output_stream:
                writer.write(output_stream)
        writer = PyPDF2.PdfWriter()
        for page in range(end_page, len(data.pages)):
            writer.add_page(data.pages[page])
            with open('second_out', "wb") as output_stream:
                writer.write(output_stream)


# 合并两个pdf
def meger_pdf(input_data_path_1, input_data_path_2):
    data1 = PyPDF2.PdfReader(input_data_path_1)
    data2 = PyPDF2.PdfReader(input_data_path_2)
    writer = PyPDF2.PdfWriter()
    writer.append(fileobj=data1, pages=(1, 10))  # 将data1中的第一页到第五页取出来
    writer.append(fileobj=data2)
    output = open("merge-output.pdf", "wb")
    writer.write(output)
    writer.close()
    output.close()


# 在pdf中指定位置插入另外一个pdf
def insert_pdf(input_data_path_1, input_data_path_2):
    data1 = PyPDF2.PdfReader(input_data_path_1)
    data2 = PyPDF2.PdfReader(input_data_path_2)
    writer = PyPDF2.PdfWriter()
    writer.append(fileobj=data1, pages=(1, 10))  # 将data1中的第一页到第五页取出来
    writer.merge(position=7, fileobj=data2, pages=(1, 3))
    output = open("insert-output.pdf", "wb")
    writer.write(output)
    writer.close()
    output.close()


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

    # input_data_path = 'input.pdf'
    # output_data_path = 'output.pdf'
    start_page = 0
    end_page = 3
    # spilt_pdf(input_data_path, output_data_path, start_page, end_page)
    # insert_pdf('input.pdf', 'second_output.pdf')
    input_data_path = input_path()
    print(input_data_path)
    # del_page = input('请输入需要删除的页码')
    del_page = 1
    del_page_pdf(input_data_path, del_page)
