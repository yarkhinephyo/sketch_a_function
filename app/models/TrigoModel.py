from .BaseModel import BaseModel
from .Function import Function
from .utils import *
import numpy as np
import math

from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# Base class for all trigo-related models
class TrigoModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return None
    
    def get_best_fit(self, complexity_level, x0, y0):

        x0 = np.array(x0)
        y0 = np.array(y0)
        func = self.get_function_by_order()

        try:
            coef, _ = curve_fit(func, x0, y0, maxfev=2000)
        except RuntimeError:
            return None

        y1 = func(x0, *coef.tolist()).tolist()

        mse = mean_squared_error(y0, y1)

        equation_string = self.get_equation_string(coef)

        return Function(self.get_model_name(), complexity_level, f"y = {equation_string}", (x0, y1), round_sig(mse))


class SineModel(TrigoModel):

    def get_model_name(self):
        return "Sine"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.sin(b*x + c) + d

    def get_equation_string(self, coef):
        return f"({round_sig(coef[0])}) \\cdot \\sin" + f"({round_sig(coef[1])} \\cdot x" + " {:+g})".format(round(coef[2], 2)) + " {:+g}".format(round(coef[3],2))

    

class SinhModel(TrigoModel):

    def get_model_name(self):
        return "Sinh"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.sinh(b*x + c) + d

    def get_equation_string(self, coef):
        return f"({round_sig(coef[0])}) \\cdot \\sinh" + f"({round_sig(coef[1])} \\cdot x" + " {:+g})".format(round(coef[2], 2)) + " {:+g}".format(round(coef[3], 2))


class CoshModel(TrigoModel):

    def get_model_name(self):
        return "Cosh"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.cosh(b*x + c) + d

    def get_equation_string(self, coef):
        return f"({round_sig(coef[0])}) \\cdot \\cosh" + f"({round_sig(coef[1])} \\cdot x" + " {:+g})".format(round(coef[2], 2)) + " {:+g}".format(round(coef[3], 2))


class TanhModel(TrigoModel):

    def get_model_name(self):
        return "Tanh"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.tanh(b*x + c) + d

    def get_equation_string(self, coef):
        return f"({round_sig(coef[0])}) \\cdot \\tanh" + f"({round_sig(coef[1])} \\cdot x" + " {:+g})".format(round(coef[2], 2)) + " {:+g}".format(round(coef[3], 2))


class ArctangentModel(TrigoModel):

    def get_model_name(self):
        return "Arctan"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.arctan(b*x + c) + d

    def get_equation_string(self, coef):
        return f"({round_sig(coef[0])}) \\cdot tan^{{-1}}" + f"({round_sig(coef[1])} \\cdot x" + " {:+g})".format(round(coef[2], 2)) + " {:+g}".format(round(coef[3], 2))