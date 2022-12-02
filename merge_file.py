import os
import os.path

# 目标文件夹的路径
filedir = 'E:/PythonProject/CommunityDetection/merge_file_data'
# 获取当前文件夹中的文件名称列表
filelist = os.listdir(filedir)


# 合并文件，并将结果存储在 JoinData.TXT 文件中
with open('merge_file_data/JoinData.txt', 'w', encoding='utf-8') as f:
    # 遍历文件名,构建文件路径
    for filename in filelist:
        filepath = filedir + '/' + filename
        # 遍历文件,按行写入
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')


