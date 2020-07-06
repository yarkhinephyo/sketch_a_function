import sys
sys.path.append(".")

from abc import ABC, abstractmethod
from models.Function import Function
import numpy as np

class BaseModel(ABC):
    
    @abstractmethod
    def get_model_name(self):
        return "Base Model"

    @abstractmethod
    def get_best_fit(complexity_level, x0, y0):
        """
        example input:
            x0 = [-0.5, -0.4, -0.3, ... , 0.5, 0.6]
            y0 = [-0.7, -0.5, -0.2, ... , 0.4, 0.6]

        return: Function Object or None <if there is an error>
        """

        return Function("Base Model", 2, "y = 2x + 5", ([], []), 3.33)