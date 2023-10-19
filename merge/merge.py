import PyPDF2
import os

'''
PyPDF2==3.0.1
pycryptodome==3.19.0
'''



# 合并两个pdf
def meger_pdf(input_data_path):
    data1 = PyPDF2.PdfReader(input_data_path[0])
    data2 = PyPDF2.PdfReader(input_data_path[1])
    writer = PyPDF2.PdfWriter()
    writer.append(fileobj=data1)  # 将data1中的第一页到第五页取出来  pages=(1, 10)
    writer.append(fileobj=data2)
    output = open("merge-output.pdf", "wb")
    writer.write(output)
    writer.close()
    output.close()


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
    input_data_path = data_list[:2]
    return input_data_path

if __name__ == '__main__':
    input_data_path = input_path()
    print('将在下面两个文件中操作')
    print(input_data_path)
    meger_pdf(input_data_path)