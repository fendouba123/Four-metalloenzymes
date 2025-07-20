from Bio.PDB import PDBParser
import requests

def download_pdb_file(protein_id):
    # 构造PDB文件的URL
    pdb_url = f"https://files.rcsb.org/download/{protein_id}.pdb"

    try:
        # 使用requests库下载文件
        response = requests.get(pdb_url, stream=True)

        # 检查请求是否成功
        if response.status_code == 200:
            # 打开一个文件并写入下载的内容
            with open(f"{protein_id}.pdb", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"PDB file for {protein_id} downloaded successfully!")
        else:
            print(f"Failed to download PDB file for {protein_id}. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred while downloading the PDB file for {protein_id}. Error: {e}")

# # 示例：下载ID为"1crn"的蛋白质PDB文件
# download_pdb_file("1crn")

with open('example_zn.txt', 'r') as fileinput:
    for line in fileinput:
        pdb_id = line.strip()  # 去掉行尾的换行符
        download_pdb_file(pdb_id)


import os

# 定义文件夹路径
folder_path = 'D:/APP/PyCharm Community Edition 2022.1.4/pycharm程序文件/生物数学-python程序/YYQ(3D)/test(ID+CA+B)'
target_extension = '.pdb'

# 遍历文件夹
for filename in os.listdir(folder_path):
    # 构建完整的文件路径
    file_path = os.path.join(folder_path, filename)
    #name, ext = os.path.splitext(filename)
    if filename.endswith(target_extension):
        name = os.path.splitext(filename)[0]
    # 判断是否是文件
    if os.path.isfile(file_path):
        # 打开文件
        with open(file_path, 'r') as file:
            # 处理文件内容
            # content = file.read()
            # print(content)
            # 打开文件
            file_CA_1 = open(name+'_Atom'+'.pdb', 'w')
            #file_CA_B_1 = open(name+'_Atom'+'_B'+'.txt', 'w')
            # 指定要检查的列号（从0开始计数）和要检查的值
            column_to_check = 0  # 假设我们要检查第二列
            value_to_find = 'ATOM'

            # 逐行读取
            for line in file:
                # 分割行并检查指定列的值
                if line.split()[column_to_check] == value_to_find:
                    # 如果匹配，输出整行
                    file_CA_1.write(line.strip() + "\n")

        file_CA_1.close()

        with open(name+'_Atom'+'.pdb', 'r') as file_ATOM:
            # 处理文件内容
            # content = file.read()
            # print(content)
            # 打开文件
            #seq_B= "name+'_CA'+'_B'+'.txt'"
            #file_path_B='D:/APP/PyCharm Community Edition 2022.1.4/pycharm程序文件/生物数学-python程序/YYQ(3D)/test(B)'
            #full_path=file_path_B+seq_B
            file_CA_2 = open(name + '_CA' + '.pdb', 'w')
            file_CA_B_1 = open(name+'_CA'+'_B'+'.txt', 'w')
            #file_CA_B_1 = open(full_path, 'w')
            # 指定要检查的列号（从0开始计数）和要检查的值
            column_to_check_CA = 2  # 假设我们要检查第二列
            value_to_find_CA = 'CA'

            # 逐行读取
            for line_ATOM in file_ATOM:
                # 分割行并检查指定列的值
                if line_ATOM.split()[column_to_check_CA] == value_to_find_CA:
                    # 如果匹配，输出整行
                    file_CA_2.write(line_ATOM.strip() + "\n")

        file_CA_2.close()

        # 打开文件并读取所有行
        with open(name + '_CA' + '.pdb', 'r') as file_CA:
            line_Bs = file_CA.readlines()

        # 初始化列表来存储第二列的值
        column_values = []

        # 遍历每一行，并分割每行的值
        for line_B in line_Bs:
            values = line_B.split()  # 默认按空格分割
            if len(values) > 1:  # 确保至少有两个值
                column_values.append(values[10])  # 添加第二列的值

        # 将第二列的值输出到一行
        file_CA_B_1.write(' '.join(column_values))
        # print(' '.join(column_values))
