import numpy as np

#Создайте 3 ваших любимых эррея разными способами
if __name__ == "__main__":
    X = np.array ([3, 1, 4, 1, 5, 9, 2, 6, 5]) 
    Y = np.random.rand(13)
    Z = np.arange (3, 10, 1)

#Создайте функцию matrix_multiplication, которая принимает 2 матрицы, 
#перемножает их по соответствующим правилам и выдаёт получившуюся матрицу. Имеется ввиду матричное перемножение, а НЕ поэлементное
def matrix_multiplication (M1, M2): 
    return np.matmul(M1,M2)

#Создайте функцию multiplication_check, которая принимает список с матрицами, 
#и выдаёт True, если они могут быть перемножены друг на друга в порядке, в котором они находятся в списке, и False, если их нельзя перемножить.
def multiplication_check (*Ms):
    M_product = Ms[0]
    for num in range (len(Ms)-1): 
        if M_product.shape[1] != Ms[num+1].shape[0]: 
            return False
        else:
            M_product = np.matmul(M_product,Ms[num+1])
            return True

#Создайте функцию multiply_matrices, 
#которая принимает список с матрицами, и выдаёт результат перемножения, 
#если его можно получить, или возвращает None, если их нельзя перемножить
def multiply_matrices (*Ms):
    if multiplication_check(*Ms):
        return np.linalg.multi_dot(Ms)
    else:
        return None

#Создайте функцию compute_2d_distance, принимающую 2 одномерных эррея c парой значений 
#(как координаты точки на плоскости) и вычисляющую расстояние между ними
def compute_2d_distance (X, Y):
    answer = np.linalg.norm(X - Y)
    return answer

#Создайте функцию compute_multidimensional_distance, принимающую 2 одномерных эррея с любым количеством значений (но равным) и 
#вычисляющую расстояние между ними
def compute_multidimensional_distance (X, Y): 
    answer = np.linalg.norm(X - Y)
    return answer

#Создайте функцию compute_pair_distances, которая получает 2d эррей, 
#где каждая строка это наблюдение, а каждый столбец - фича. 
#Функция рассчитывает матрицу попарных расстояний и выдаёт её пользователю.

def compute_pair_distances (array): 
    dist_sq = np.sum((array[:, np.newaxis, :] - array[np.newaxis, :, :]) ** 2, axis = -1)
    return np.sqrt(dist_sq)