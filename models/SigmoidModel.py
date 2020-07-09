from .BaseModel import BaseModel
from .Function import Function
from .utils import *
import numpy as np
import math

from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

class SigmoidModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Sigmoid"

    def get_function_by_order(self):
        def sigmoid(x, L, k, x0, b):
            y = L / (1 + np.exp(k*(x-x0))) + b
            return y
        return sigmoid

    def get_equation_string(self, coef):
        # \frac{L}{1 + e^{-k(x-x_0)}}
        return "\\frac{" + str(round(coef[0],2)) + "}{" + "1 + e^{" + "{} \\cdot (x {:+g})".format(round_sig(coef[1]), round(coef[2], 2)) + "}" + "}" + " {:+g}".format(round(coef[3], 2))
    
    def get_best_fit(self, complexity_level, x0, y0):

        x0 = np.array(x0)
        y0 = np.array(y0)
        func = self.get_function_by_order()

        # Initial guesses
        p0 = [max(y0), 1, np.median(x0), min(y0)]

        try:
            coef, _ = curve_fit(func, x0, y0, p0, method='dogbox', maxfev=2000)
        except RuntimeError:
            return None

        y1 = func(x0, *coef.tolist()).tolist()

        mse = mean_squared_error(y0, y1)

        equation_string = self.get_equation_string(coef)

        return Function(self.get_model_name(), complexity_level, f"y = {equation_string}", (x0, y1), round_sig(mse))