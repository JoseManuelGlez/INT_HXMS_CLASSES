import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from domain.models.class_model import ClassModel
from domain.repositories.class_repository import ClassRepository

class ClassUseCase:
    def __init__(self, class_repository: ClassRepository):
        self.class_repository = class_repository

    def create_class(self, clas: ClassModel) -> ClassModel:
        return self.class_repository.create_class(clas)
    
    def update_status(self, class_id, new_status) -> ClassModel:
        return self.class_repository.update_status(class_id, new_status)
    
    def update_number_of_students(self, class_id) -> ClassModel:
        return self.class_repository.update_number_of_students(class_id)
    
