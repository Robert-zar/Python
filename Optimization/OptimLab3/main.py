import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import optimization_view
from main_function_optimize import *
import random

class OptViewApp(QtWidgets.QMainWindow, optimization_view.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_lab_1.clicked.connect(self.lab1)
        self.pushButton_lab_2.clicked.connect(self.lab2)
        self.pushButton_lab_3.clicked.connect(self.lab3)
        self.pushButton_lab_4.clicked.connect(self.lab4)
        self.pushButton_lab_5.clicked.connect(self.lab5)
        self.pushButton_lab_6.clicked.connect(self.lab6)
        self.pushButton_lab_7.clicked.connect(self.lab7)
        self.pushButton_lab_8.clicked.connect(self.lab8)
    def lab1(self):
        point = main_function_optimize(1,"C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [-0,0,100, 0.001, 0.001], [[-10,10],[-10,10]])
        self.textEdit_lab_1.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab2(self):
        point = main_function_optimize(2, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [], [[-4, 4], [-4, 4]])
        self.textEdit_lab_2.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab3(self):
        point = main_function_optimize(3, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [100, -2, 2, -2, 2, 0, 0, 0, 0.1, 0.1, 10],[[-2, 2], [-2, 2]])
        self.textEdit_lab_3.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab4(self):
        point = main_function_optimize(4, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [100,50,0], [[-4,4],[-4,4]])
        self.textEdit_lab_4.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab5(self):
        point = main_function_optimize(5, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [3, 300, 10, 30, 15, 5, 1, 500, 10], [[-4, 4], [-4, 4]])
        self.textEdit_lab_5.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab6(self):
        point = main_function_optimize(6, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [-2, 2, -2,2,50,50,10,5, 7,0.2,100,0.2,0.2],[[-2,2],[-2,2]])
        self.textEdit_lab_6.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab7(self):
        point = main_function_optimize(7, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [-3, 3, -3, 3, 10, 250, 0.1, 5, 0.1], [[-1,1],[-1,1]])
        self.textEdit_lab_7.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))
    def lab8(self):
        point = main_function_optimize(8, "C:\\Users\\rzarg\\OneDrive\\Рабочий стол\\pythonProject_optimization\\pictires", [100, -5,5,-5,5,0,0,0,0.05,0.1,5,   100, 0.01, 0.01],[[-5,5],[-5,5]])
        self.textEdit_lab_8.setText("x = "+str(round(point[0],2))+" y = "+str(round(point[1],2))+" z = "+str(round(point[2],2)))

# оптимизируемая функция
def function(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


# Генерация начальной популяции
def generate_population(num_persons, min_x, max_x, min_y, max_y):
    population = []
    for i in range(num_persons):
        population.append([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
    return population


# селекция усечением
def truncation_selection(num_persons, population):
    new_population = []
    for i in population:
        new_population.append([function(i[0], i[1]), i[0], i[1]])
    new_population.sort()
    result = []
    for i in range(num_persons):
        percent = random.uniform(0, 1)
        person = random.randint(0, int(len(new_population) * percent))
        result.append([new_population[person][1], new_population[person][2]])
    return result


# элитарная селекция
def elite_selection(num_persons, population):
    new_population = []
    for i in population:
        new_population.append([function(i[0], i[1]), i[0], i[1]])
    new_population.sort()
    result = []
    elite = int(num_persons * 0.1)
    for i in range(elite):
        result.append([new_population[elite][1], new_population[elite][2]])
    n_pop = truncation_selection(num_persons - elite, population[elite:])
    result += n_pop
    return result


# панмиксия
def panmixy(population):
    parents_pairs = []
    num_persons = len(population)
    for i in range(num_persons):
        second_parent = random.randint(0, num_persons - 1)
        parents_pairs.append([population[i], population[second_parent]])
    return parents_pairs


def get_distance(parent_1, parent_2):
    return (parent_1[0] - parent_2[0]) ** 2 + (parent_1[1] - parent_2[1])


# промежуточная рекомбинация
def intermediate_recombination(parent_pairs):
    new_population = []
    for i in range(len(parent_pairs)):
        alpha_1 = random.uniform(-0.25, 1.25)
        parent_1 = parent_pairs[i][0]
        parent_2 = parent_pairs[i][1]
        new_population.append(
            [parent_1[0] + alpha_1 * (parent_2[0] - parent_1[0]), parent_1[1] + alpha_1 * (parent_2[1] - parent_1[1])])
    return new_population


# мутация
def mutation(population, chance, step):
    for i in range(len(population)):
        for j in range(2):
            val = random.uniform(0, 1)
            # мутация
            if val < chance:
                population[i][j] += step if val < chance / 2 else -step
    return population


'''Генетический алгоритм
Параметры: 
1. Число особей
2-5. Минимальные и максимальные значения переменных
6. Селекция особей
    0 - Отсечением
    1 - Элитарная
7. Вероятность мутации
8. Шаг мутации
9. Число поколений'''

population_for_improving = [[]]


def genetic_algorithm(num_persons, min_x, max_x, min_y, max_y, parent_choice, method, selection, mutation_chance,
                      mutation_step, num_generations):
    list_points = list()
    population = generate_population(num_persons, min_x, max_x, min_y, max_y)
    for gen in range(num_generations):
        # Выбор родителей
        if parent_choice == 0:
            parents = panmixy(population)
        # Скрещивание и мутация
        children = intermediate_recombination(parents)
        children = mutation(children, mutation_chance, mutation_step)

        # Выбор особей следующего поколения
        population += children
        if selection == 0:
            population = truncation_selection(num_persons, population)
        elif selection == 1:
            population = elite_selection(num_persons, population)
        list_points.append([population[0][0], population[0][1], function(population[0][0], population[0][1])])

    # Выбор самой прспособленной особи
    mn = function(population[0][0], population[0][1])
    p = population[0]
    for person in population:
        if function(person[0], person[1]) < mn:
            p = person
            mn = function(person[0], person[1])
    return [p, mn, list_points]

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = OptViewApp()  # Создаём объект класса OptViewApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
# старт программы
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()