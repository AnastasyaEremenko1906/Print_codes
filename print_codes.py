import qrcode
import os

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)

number = 0
number_of_mku = int(input("Введите трехзначный номер МКУ\n"))
name_of_folder = 'Codes_for_{}_MKU'.format(number_of_mku)
way_to_folder = os.path.expanduser("~\\Desktop\\{}\\".format(name_of_folder))
os.mkdir(way_to_folder)

list_of_info = [f"Перевод кнопок аварийной остановки МКУ (1)    {number_of_mku}",
                f"Перевод кнопок аварийной остановки МКУ (2)    {number_of_mku}",
                f"Перевод кнопок аварийной остановки МКУ (3)    {number_of_mku}",
                f"Перевод кнопок аварийной остановки МКУ (4)    {number_of_mku}",
                f"Перевод кнопок аварийной остановки МКУ (5)    {number_of_mku}",
                f"Перевод кнопок аварийной остановки МКУ (6)    {number_of_mku}",
                f"Проверка уровня масла смазки цилиндров компрессора    {number_of_mku}",
                f"Проверка уровня масла в компрессоре    {number_of_mku}",
                f"Проверка наличия конденсата в глушителе двигателя    {number_of_mku}",
                f"Сброс конденсата    {number_of_mku}",
                f"Проверка и очистка от снега и льда    {number_of_mku}",
                f"Проверка уровня антифриза    {number_of_mku}",
                f"Проверка состояния фильтров:- (1) воздуха двигателя    {number_of_mku}",
                f"Проверка уровня антифриза (долить антифриз)    {number_of_mku}",
                f"Проверка уровня гидравлической жидкости    {number_of_mku}",
                f"При необходимости долить антифриз    {number_of_mku}",
                f"Перевод свечных трубопроводов    {number_of_mku}",
                f"Подключение заземления МКУ    {number_of_mku}",
                f"Снятие защитного кожуха с вентилятора системы охлаждения    {number_of_mku}",
                f"Проверка уровня антифриза (3,сист охл)    {number_of_mku}",
                f"Проверка и очистка от снега и льда всасов воздуха двигателя    {number_of_mku}",
                f"Проверка уровня масла    {number_of_mku}",
                f"Проверка масляного фильтра    {number_of_mku}",
                f"Подключение пульта управления    {number_of_mku}",
                f"Подключение счетчика перекачиваемого газа    {number_of_mku}",
                f"Проверка подключения воздуха от тягача к МКУ    {number_of_mku}",
                f"Включить массу установки    {number_of_mku}",
                f"Проверка состояния АКБ (напряжение)    {number_of_mku}",
                f"Подключить клапан системы пожаротушения    {number_of_mku}",
                f"Проверка уровня топлива предпусковых подогревателей    {number_of_mku}",
                "Контроль объема 1 МКС",
                "Контроль объема 2 МКС",
                "Общий объем",
                "Проверка фланцев"]

list_of_names = ['левый_1',
                 'левый_2',
                 'левый_3',
                 'левый_4',
                 'левый_5',
                 'левый_6',
                 'левый_7',
                 'левый_18',
                 'левый_8',
                 'левый_9',
                 'левый_10',
                 'левый_11',
                 'левый_12',
                 'левый_13',
                 'левый_14',
                 'левый_15',
                 'левый_16',
                 'правый_1',
                 'правый_2',
                 'правый_3',
                 'правый_4',
                 'правый_5',
                 'правый_6',
                 'передний_1',
                 'передний_2',
                 'передний_3',
                 'передний_4',
                 'передний_5',
                 'передний_6',
                 'передний_7',
                 'обход-МКУ1',
                 'обход-МКУ2',
                 'обход-общий',
                 'обход-проверка']

for data in list_of_info:
    try:
        current_text = list_of_info[number]
        current_name = list_of_names[number]
        qr.add_data(current_text)
        qr.make(fit=True)
        img = qr.make_image()
        path = os.path.join(way_to_folder, '{}.jpg'.format(current_name))
        img.save(path)
        number += 1
    except qrcode.exceptions.DataOverflowError:
        pass
    except ValueError:
        pass

