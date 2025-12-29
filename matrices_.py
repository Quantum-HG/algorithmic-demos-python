import copy
from tkinter import *

root = Tk()
root.geometry("500x500")


# but = Button(root, text=0, font=("Freesans", 20), padx=10, bg="yellow", bd=5)
# but.place(x=200, y=200)

# MATRIX = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.order = [self.rows, self.columns]
        self.matrix = []
        for i in range(rows):
            lis = []
            for j in range(columns):
                lis.append(0)
            self.matrix.append(lis)

    def show(self):
        for row in self.matrix:
            print(row)
        print("-" * 20)

    def get(self, row, column):
        return self.matrix[row - 1][column - 1]

    def set(self, row, column, value):
        self.matrix[row - 1][column - 1] = value

    def add(self, other):
        assert (self.order == other.order)
        for row in range(self.rows):
            for column in range(self.columns):
                self.set(row, column, other.get(row, column) + self.get(row, column))

    def subtract(self, other):
        other_copy = copy.copy(other)
        other_copy.scalar_multiplication(-1)
        self.add(other_copy)

    def scalar_multiplication(self, scalar):
        for row in range(self.rows):
            for column in range(self.columns):
                self.matrix[row - 1][column - 1] *= scalar

    def scalar_division(self, scalar):
        self.scalar_multiplication(1 / scalar)


m1 = Matrix(3, 3)
m2 = Matrix(3, 3)
m1.set(1, 1, 5)
m1.set(1, 2, 50)
m2.set(1, 1, 57)
m2.set(3, 3, 587)
m1.show()
m2.show()
m1.scalar_division(0.65)
m1.show()

# root.mainloop()
