import csv 
from pillow import Image as im

file_name = 'dateset_labels.csv'



with open(file_name) as dataset_labels:
    csv_reader = csv.DictReader(dataset_labels, delimiter=',')
    for row in csv_reader:






# read labels from csv into array of dicts 
# work with jpg images:

img = im.open(path)

width, height = im.size
img = img.crop( left, upper, right, lower )  
img = img.resize( width, height )
# depending on class choise a dir where image should be saved then 
# get image size and cut sign bits to another jpg with number  
# in another csv get base with sheet number, size of image


def CropSignFromImage( file_name, x_from, y_from, width,
                       height, sign_class, sign_id , image_number)
    image = im.open( file_name )
    weight, height = image.size()
    image = image.crop( x_from, y_from, x_from + width, y_from + height )
    image = image.resize( width, height )
    # проверка на наличие верхней директории директории
    # проверка на наличие нижней директории 
    # если есть то сохраняем в ней картинку, если нет то делаем и сохраняем

    pass