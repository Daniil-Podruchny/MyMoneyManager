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

def isSelected(obj, selectedItems):
    if not selectedItems:
        QMessageBox.about(obj, "Ошибка выбора", "Выберете элемент из списка, который хотите удалить!")

def tupleArr_ArrArr(tupleArray):
    result_array = []
    for tuple in tupleArray:
        result_array.append(list(tuple))
    return result_array

def getMonthName(num):
    month = {
        1: "январь",
        2: "февраль",
        3: "март",
        4: "апрель",
        5: "май",
        6: "июнь",
        7: "июль",
        8: "август",
        9: "сентябрь",
        10: "октябрь",
        11: "ноябрь",
        12: "декабрь"
    }

    return month[num]