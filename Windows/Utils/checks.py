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

def tupleArr_ArrArr(tupleArray):
    result_array = []
    for tuple in tupleArray:
        result_array.append(list(tuple))
    return result_array