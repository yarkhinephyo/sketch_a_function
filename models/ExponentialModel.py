from .BaseModel import BaseModel
from .Function import Function
from .utils import *
import numpy as np
import math

from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

class ExponentialModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Exponential"

    def get_function_positive(self):
        return lambda x, a, b1, c: a * np.exp(b1*x) + c

    def get_function_negative(self):
        return lambda x, a, b1, c: a * np.exp(-b1 * x) + c

    def get_equation_string_positive(self, coef):
        return f"{round(coef[0], 1)} \\cdot e^" + "{" + f"{round_sig(coef[1], 1)} \\cdot x" + "}" + " {:+g}".format(round(coef[2],1))

    def get_equation_string_negative(self, coef):
        return f"{round(coef[0], 1)} \\cdot e^" + "{-" + f"{round_sig(coef[1], 1)} \\cdot x" + "}" + " {:+g}".format(round(coef[2],1))

    def get_best_fit(self, complexity_level, x0, y0):
        
        x0 = np.array(x0)
        y0 = np.array(y0)

        func_pos = self.get_function_positive()
        func_neg = self.get_function_negative()

        try:
            coef_pos, _ = curve_fit(func_pos, x0, y0, maxfev=2000)
            y1_pos = func_pos(x0, *coef_pos.tolist())
            mse_pos = mean_squared_error(y0, y1_pos)
        except RuntimeError:
            return None
            
        try:
            coef_neg, _ = curve_fit(func_neg, x0, y0, maxfev=2000)
            y1_neg = func_neg(x0, *coef_neg.tolist())
            mse_neg = mean_squared_error(y0, y1_neg)
        except RuntimeError:
            return None

        if mse_pos < mse_neg:
            y1, mse = y1_pos, mse_pos
            equation_string = self.get_equation_string_positive(coef_pos)
        else:
            y1, mse = y1_neg, mse_neg
            equation_string = self.get_equation_string_negative(coef_neg)

        return Function("Exponential", complexity_level, f"y = {equation_string}", (x0, y1), round_sig(mse))

# class NegativeExponentialModel(ExponentialModel):

#     def get_function_by_order(self):
#         return lambda x, a, b1, c: a * np.exp(-b1 * x) + c
    
#     def get_equation_string(self, coef):
#         return f"({round(coef[0], 1)}) e^(-{round_sig(coef[1])} * x) + {round(coef[2], 1)}"
