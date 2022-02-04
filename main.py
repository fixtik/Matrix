from typing import Optional
from random import randint

class Matrix:

    def __init__(self, row: int = 2, col: int = 2):

        self.col = col
        self.row = row

        self.data_arr = [[randint(0, 20)] * self.col for _ in range(self.row)]

    @staticmethod
    def __check_type_value(value):
        if not isinstance(value, int):
            raise TypeError("введены некорректные данные")
        if value <= 0:
            raise ValueError("введены некорректные значения")


    @property
    def row(self) -> int:
        return self.__j_row

    @row.setter
    def row(self, j: int):
        self.__check_type_value(j)
        self.__j_row = j

    @property
    def col(self) -> int:
        return self.__i_col

    @col.setter
    def col(self, i: int):
        self.__check_type_value(i)
        self.__i_col = i

    def set_matrix_value(self):

        for row in range(self.row):
            for col in range(self.col):
                inp = input(f'Введите число [{row, col}]: ')
                if not inp.isdigit():
                    raise TypeError
                self.data_arr[row][col] = int(inp)

    @staticmethod
    def __res_init(col: int, row: int):
        return [[0] * col for _ in range(row)]

    def add_matrix(self, other_matrix: Optional['Matrix']) -> list:
        """
        Сложение двук объектов типа Matrix
        :param other_matrix: матрица для сложения
        :return: массив типа list
        """
        if not isinstance(other_matrix, type(self)):
            raise TypeError(f"Ожидаю Matrix, получаю {type(other_matrix)}")

        if self.row != other_matrix.row and self.col != other_matrix.col:
            raise IndexError("Матрицы не годятся для сложения - они разной размерности!")
        result = self.__res_init(self.col, self.row)
        for col in range(self.row):
            for row in range(self.col):
                result[row][col] = self.data_arr[row][col] + other_matrix.data_arr[row][col]
        return result

    def mul_int(self, value: int) -> list:
        """
        результат умножения матрицы на число
        :param value: целочисленное число
        :return: массив
        """
        if not isinstance(value, int):
            raise ValueError
        result = self.__res_init(self.col, self.row)
        for row in range(self.row):
            for col in range(self.col):
                result[row][col] = self.data_arr[row][col] * value
        return result

    def print_matrix(self):
        """
        вывод матрицы на экран
        """
        for row in range(self.row):
            for col in range(self.col):
                print(f'{self.data_arr[row][col]:>5}', end =' ')
            print()


    def mul_matrix(self, other: Optional['Matrix']) -> list:
        """
        перемножение двух объектов типа Matrix
        :param other: матрица-множитель
        :return: матрица типа list
        """
        if not (self.col == other.row):
            raise IndexError("Матрицы не годятся для перемножения - число строк и столбцов не сопадает!")
        result = self.__res_init(other.col, self.row)
        for row in range(self.row):
            for col in range(other.col):
                for k in range(self.row):
                    result[row][col] += self.data_arr[row][k] * other.data_arr[k][col]
        return result


if __name__ == '__main__':

    m1 = Matrix(2,2)
    m1.set_matrix_value()


    print(m1.data_arr)

    m2 = Matrix(2,2)
    m2.set_matrix_value()
    print(m2.data_arr)

    print(m1.mul_matrix(m2))

