import numpy as np

class MatrixCalculator:
    def add(self, matrix1, matrix2):
        try:
            result = np.add(matrix1, matrix2)
            return result.tolist()
        except Exception as e:
            return f"Ошибка: {e}"

    def subtract(self, matrix1, matrix2):
        try:
            result = np.subtract(matrix1, matrix2)
            return result.tolist()
        except Exception as e:
            return f"Ошибка: {e}"

    def multiply(self, matrix1, matrix2):
        try:
            result = np.dot(matrix1, matrix2)
            return result.tolist()
        except Exception as e:
            return f"Ошибка: {e}"

    def transpose(self, matrix):
        try:
            result = np.transpose(matrix)
            return result.tolist()
        except Exception as e:
            return f"Ошибка: {e}"

    def determinant(self, matrix):
        try:
            result = np.linalg.det(matrix)
            return [[round(result, 2)]]  # Возвращаем детерминант в виде матрицы 1x1
        except Exception as e:
            return f"Ошибка: {e}"

    def inverse(self, matrix):
        try:
            result = np.linalg.inv(matrix)
            return result.tolist()
        except np.linalg.LinAlgError:
            return "Ошибка: Матрица не обратима"
        except Exception as e:
            return f"Ошибка: {e}"

    def is_square(self, matrix):
        return len(matrix) == len(matrix[0])

    def is_valid_matrix(self, matrix):
        try:
            np_matrix = np.array(matrix)
            if len(np_matrix.shape) != 2:
                return False
            return True
        except Exception as e:
            return False