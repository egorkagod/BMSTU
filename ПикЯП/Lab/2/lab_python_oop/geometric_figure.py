from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod
    def figure_name(cls):
        return cls.__name__
