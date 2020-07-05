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
        return Function("Base Model", 2, "y = 2x + 5", ([], []), 3.33)