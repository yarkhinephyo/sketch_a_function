from models.BaseModel import BaseModel
from models.Function import Function
import numpy as np
import math

from numpy.polynomial.polynomial import polyfit
from sklearn.metrics import mean_squared_error

class LogarithmicModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Logarithmic"

    def get_best_fit(self, complexity_level, x0, y0):

        if (np.array(x0) < 0).any():
            return None

        log_x0 = np.log(x0)
        coef = polyfit(log_x0, y0, complexity_level)
        y1 = np.polyval(coef[::-1], log_x0).tolist()

        mse = mean_squared_error(y0, y1)

        equation_string = " + ".join([f"({round(coef[i], 1)})(log x)^{i}" for i in range(len(coef))])

        return Function("Logarithmic", complexity_level, f"y = {equation_string}", (x0, y1), round(mse, 2))