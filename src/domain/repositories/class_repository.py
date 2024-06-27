import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from abc import ABC, abstractmethod
from domain.models.class_model import ClassModel

class ClassRepository(ABC):
    @abstractmethod
    def create_class(self, clas: ClassModel) -> ClassModel:
        pass

    @abstractmethod
    def update_status(self, class_id, new_status) -> ClassModel:
        pass

    @abstractmethod
    def update_number_of_students(self, class_id) -> ClassModel:
        pass

# TODO: Implement the methods, add stidents, add transcripyion, list transcription