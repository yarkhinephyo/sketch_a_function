from models.BaseModel import BaseModel
from sklearn.linear_model import LinearRegression
from models.Function import Function
import numpy as np

class PolynomialModel(BaseModel):

    def __init__(self):
        self.reg = LinearRegression()

    def get_model_name(self):
        return "Linear Model"

    def get_best_fit(self, complexity_level, x0, y0):
        
        X = np.transpose(np.array([x0]))
        reg = self.reg.fit(X, y0)
        y1 = reg.predict(X).tolist()

        gradient = reg.coef_[0]
        intercept = reg.intercept_

        return Function("Linear Model", 1, f"Y = {gradient}X + {intercept}", (x0, y1), 5)