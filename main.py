from  PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import sys
import os
from probablity import Probability

def electicScheme4var(elementProbabilityList):
    act_1 = elementProbabilityList[1] + Probability.negativeProbability(elementProbabilityList[1]) * elementProbabilityList[2] * elementProbabilityList[3]
    act_2 = elementProbabilityList[4] + Probability.negativeProbability(elementProbabilityList[4]) * elementProbabilityList[5]
    return elementProbabilityList[0] + Probability.negativeProbability(elementProbabilityList[0]) *(act_1 * act_2)


'''for element in input().split():
    float_list.append(float(element))
print(electicScheme4var(float_list))'''

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class mywindow(QtWidgets.QMainWindow):
    '''Конструктор гловного окна'''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Установить изображение с формулой в главном окне
        pixmap = QPixmap(resource_path("img/formula.jpg"))
        pixmap_2 = QPixmap(resource_path("img/schema.jpg"))
        self.ui.formulaLabel.setPixmap(pixmap)
        self.ui.schemaLabel.setPixmap(pixmap_2)

        # Подвязка кнопки "Вычислить" к методам класса главного окна
        self.ui.calcButton.clicked.connect(self.solve)

    '''Произвести рассчёт по формуле у данной задачи'''
    def solve(self):
        #Считать введённые пользователем данные
        float_list = []
        for i in range(0, 6):
            element = self.ui.probabilityTable.item(0,i).text()
            # Проверить введенные данные
            if (float(element) - 1.00 > 0.00) or (float(element) + 1.00 < 1.00):
                QtWidgets.QMessageBox.information(self, "Ошибка", "Вероятность должна быть в промежутке [0.00; 1.00]")
                return
            float_list.append(float(element))
        #n = self.ui.n_spinBox.value()

        # Произвести вычисления по формуле
        result = electicScheme4var(float_list)

        # Вывести результат в поле для ответа
        str_result = "{:01.12f}".format(result)
        self.ui.resultTextEdit.setText(str_result)

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    sys.exit(app.exec())