from .BaseModel import BaseModel
from .Function import Function
from .utils import *
import numpy as np

from numpy.polynomial.polynomial import polyfit
from sklearn.metrics import mean_squared_error

class PolynomialModel(BaseModel):

    def __init__(self):
        pass

    def get_model_name(self):
        return "Polynomial"

    def get_equation_string(self, coef):
        degrees = []

        for i in range(len(coef)):
            if i == 0:
                degrees.append('{:g}'.format(round_sig(coef[i], 2)) )
            elif i == 1:
                degrees.append('{:+g}x'.format(round_sig(coef[i], 2)) )
            else:
                degrees.append('{:+g}x^{}'.format(round_sig(coef[i], 2), i) )

        return " ".join(degrees)


    def get_best_fit(self, complexity_level, x0, y0):
        
        coef = polyfit(x0, y0, complexity_level)
        y1 = np.polyval(coef[::-1], x0).tolist()

        mse = mean_squared_error(y0, y1)

        equation_string = self.get_equation_string(coef)

        return Function("Polynomial", complexity_level, f"y = {equation_string}", (x0, y1), round_sig(mse))