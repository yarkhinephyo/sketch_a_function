from models.BaseModel import BaseModel
from models.Function import Function
import numpy as np
import math

from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

class ExponentialModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Exponential"

    def get_function_by_order(self):

        return lambda x, a, b1, c: a * np.exp(b1*x) + c

    def get_best_fit(self, complexity_level, x0, y0):

        if complexity_level == 0:
            return None
        
        x0 = np.array(x0)
        y0 = np.array(y0)
        func = self.get_function_by_order()

        try:
            coef, _ = curve_fit(func, x0, y0, maxfev=2000)
        except RuntimeError:
            return None

        y1 = func(x0, *coef.tolist()).tolist()

        mse = mean_squared_error(y0, y1)

        equation_string = " + ".join([f"({round(coef[i], 1)})(x)^{i}" for i in range(1, len(coef) - 1)])

        return Function("Exponential", complexity_level, f"y = ({round(coef[0], 1)}) e^({equation_string}) + {round(coef[-1], 1)}", (x0, y1), mse)