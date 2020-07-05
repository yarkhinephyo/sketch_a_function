from abc import ABC, abstractmethod
import Function
import numpy as np

class BaseModel(ABC):
    
    @abstractmethod
    def get_model_name(self):
        return "Base Model"

    @abstractmethod
    def get_best_fit(complexity_level, y_values):
        return Function("Base Model", 2, "y = 2x + 5", y_values, y_values, 3.33)