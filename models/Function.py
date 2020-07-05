class Function:
    def __init__(self, model_name, complexity_level, equation_string, input_y_values, output_y_values, mse):
        self.model_name = model_name
        self.complexity_level = complexity_level
        self.equation_string = equation_string
        self.input_y_values = input_y_values
        self.output_y_values = output_y_values
        self.mse = mse

    def __str__(self):
        '''
        For example: "y = 2x + 5" 
        '''
        return self.equation_string