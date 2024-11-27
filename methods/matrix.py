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
