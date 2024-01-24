import os
import re

# 获取目录下的所有文件名
img_path = "data/busi/masks/0"
files = os.listdir(img_path)

# 遍历所有文件名
for file in files:
    # 使用正则表达式替换文件名中的"_mask"
    new_file = re.sub('_mask', '', file)
    # 重命名文件
    os.rename(os.path.join(img_path, file), os.path.join(img_path, new_file))