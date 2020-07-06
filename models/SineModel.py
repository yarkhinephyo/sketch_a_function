from .BaseModel import BaseModel
from .Function import Function
import numpy as np
import math

from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

class SineModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Sine"

    def get_function_by_order(self):
        return lambda x, a, b, c, d: a * np.sin(b*x + c) + d

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

        equation_string = f"({round(coef[0], 1)}) sin({round(coef[1], 1)} * x + {round(coef[2], 1)}) + {round(coef[3],1)}"

        return Function("Sine", complexity_level, f"y = {equation_string}", (x0, y1), mse)