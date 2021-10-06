import qrcode
import os
from helpers import make_list_of_info, list_of_names


qr = qrcode.QRCode(version=1, box_size=10, border=4,)
number_of_mku = int(input("Введите трехзначный номер МКУ\n"))
name_of_folder = 'Codes_for_{}_MKU'.format(number_of_mku)
way_to_folder = os.path.expanduser("~\\Desktop\\{}\\".format(name_of_folder))
os.mkdir(way_to_folder)

for text, code_name in zip(make_list_of_info(number_of_mku), list_of_names):
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'{way_to_folder}' + f'{code_name}'+'.jpg')
    qr.clear()
