from abc import ABC, abstractmethod
import Function
import numpy as np

class BaseModel(ABC):
    
    @abstractmethod
    def get_model_name(self):
        return "Base Model"

    @abstractmethod
    def get_best_fit(complexity_level):
        return Function("Base Model", 2, "y = 2x + 5", np.random.rand((300, 300, 4)), np.random.rand((300, 300, 4)), 3.33)