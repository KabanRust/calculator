from PySide6.QtWidgets import QLineEdit

class Matrix_perform:
    def perform_add(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.add(matrix1, matrix2)
        self.display_result(result)

    def perform_subtract(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.subtract(matrix1, matrix2)
        self.display_result(result)

    def perform_multiply(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        matrix2 = self.get_matrix(self.matrix_layouts[1])
        result = self.matrix_calculator.multiply(matrix1, matrix2)
        self.display_result(result)

    def perform_transpose(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.transpose(matrix1)
        self.display_result(result)

    def perform_determinant(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.determinant(matrix1)
        self.display_result(result)

    def perform_inverse(self):
        matrix1 = self.get_matrix(self.matrix_layouts[0])
        result = self.matrix_calculator.inverse(matrix1)
        self.display_result(result)


class Matrix_size:
    def local_matrix_size(self):
        rows = self.rows_spinbox.value()
        cols = self.cols_spinbox.value()
        matrices_count = self.matrices_count_spinbox.value()

        # Очистка макетов матриц
        for matrix_layout in self.matrix_layouts:
            for i in reversed(range(matrix_layout.count())):
                widget = matrix_layout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

        self.matrices = [[[QLineEdit() for _ in range(cols)] for _ in range(rows)] for _ in range(matrices_count)]

        for k, matrix in enumerate(self.matrices):
            for i in range(rows):
                for j in range(cols):
                    self.matrix_layouts[k].addWidget(matrix[i][j], i, j)

    def local_get_matrix(self, matrix_layout):
        rows = self.rows_spinbox.value()
        cols = self.cols_spinbox.value()
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                cell_value = matrix_layout.itemAtPosition(i, j).widget().text()
                try:
                    row.append(float(cell_value))
                except ValueError:
                    row.append(0)
            matrix.append(row)
        return matrix