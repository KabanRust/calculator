from PySide6.QtWidgets import QMessageBox

class Programmable_func:
    def define_new_function(self):
        name = self.func_name_input.text().strip()
        params = self.func_params_input.text().strip().split()
        expression = self.func_expression_input.text().strip()
        
        success, message = self.programmable_calculator.define_function(name, params, expression)
        if success:
            self.update_function_lists()
            QMessageBox.information(self, "Успех", message)
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def call_existing_function(self):
        name = self.call_name_input.text().strip()
        args = [float(arg) for arg in self.call_args_input.text().strip().split()]
        
        success, result = self.programmable_calculator.call_function(name, args)
        if success:
            self.call_result.setText(str(result))
        else:
            self.call_result.setText(str(result))
            QMessageBox.warning(self, "Ошибка", str(result))

    def set_variable(self):
        name = self.var_name_input.text().strip()
        value = self.var_value_input.text().strip()
        
        success, message = self.programmable_calculator.set_variable(name, value)
        if success:
            self.update_function_lists()
            QMessageBox.information(self, "Успех", message)
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def update_function_lists(self):
        functions = self.programmable_calculator.list_functions()
        variables = self.programmable_calculator.list_variables()
        
        text = "Определённые функции:\n"
        text += "\n".join(functions)
        text += "\n\nПеременные:\n"
        text += "\n".join(variables)
        
        self.functions_list.setText(text)