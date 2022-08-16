import os
from pdf2image import convert_from_path
import glob
from pathlib import Path

path1 = '/home/vdungx/Desktop/pdf2img/'
path = os.path.join(path1, 'Văn bản mẫu')


path_file = glob.glob(path + '/*/*.pdf')

for i in path_file:
    # print(i)
    folder = str(i).split('/')[-2]
    file_name = str(i).split('/')[-1]
    file_name = file_name.split('.')[0]

    if Path(path1 + 'output/' + folder).exists() == False:
        os.mkdir(path1 + 'output/' + folder)
    if Path(path1 + 'output/' + folder + '/' + file_name).exists() == False:
        os.mkdir(path1 + 'output/' + folder + '/' + file_name)

    images = convert_from_path(i, 300)
    for j in range(len(images)):
        images[j].save(('./output/{}/{}/page_{}.png').format(folder, file_name, (str(j+1)), 'PNG'))
        print(('./output/{}/{}/page_{}.png').format(folder, file_name, (str(j+1)), 'PNG'))