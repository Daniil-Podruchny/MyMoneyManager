from PyQt5.QtWidgets import QMessageBox


def isEmpty(obj, name, sum, date):
    if name == "" or sum == "" or date == "":
        QMessageBox.about(obj, "Ошибка добавления", "Все поля должны быть заполнены!")
        return True

def isCorrectSum(obj, sum):
    if sum.isdigit():
        return True
    else:
        QMessageBox.about(obj, "Ошибка добавления", "Введите корректное значение для поля 'сумма'!")