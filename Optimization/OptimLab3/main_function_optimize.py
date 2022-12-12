#/use/bin/env python3
#coding: UTF-8
from bacteria_algorithm import bacteria_algorithm
from Genetic_algorithm import genetic_algorithm
from imm_algorithm import immun_algorithm
from beetest import bee_algorithm
from swarm_algorithm import main_swarm_function
from Simplex import start_count
from quickest_descent import quickest_descent
from hybrid_algorithm import hybrid_algorithm

from opt_graphics import draw_function

'''
Главная функция.
Параметры:
1. Алгоритм оптимизации (он же номер лабы)
   1 - Наискорейший спуск
   2 - Симплекс-метод
   3 - Генетичнский алгоритм
   4 - Роевый алгоритм
2. Путь к папке с картинками (для отрисовки функции)
3. Параметры алгоритма оптимизации (для каждого свой набор)
4. Ограничения на обрасть отрисовки в формате:
    [[min_x, max_x],[min_y, max_y]]
'''

def main_function_optimize(algorithm, path, p, bounds):
	if algorithm==1:
		point=quickest_descent(p[0],p[1],p[2], p[3], p[4])
		num_function=5
	elif algorithm == 2:
		point=start_count()
		num_function=1
	elif algorithm== 3:
		point=genetic_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10])
		num_function=0
	elif algorithm==4:
		point=main_swarm_function(p[0],p[1],p[2])
		num_function=3
	elif algorithm == 5:
		point=bee_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8])
		if p[0]==0:
			num_function=2
		elif p[0]==2:
			num_function=6
		elif p[0]==3:
			num_function=0
	elif algorithm==6:
		point=immun_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
		num_function=0
	elif algorithm==7:
		point=bacteria_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7], p[8])
		num_function=2
	elif algorithm==8:
		point=hybrid_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13])
		num_function=5



	draw_function(num_function, point, bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1], path)
	return [point[0][0], point[0][1], point[1]]
  
