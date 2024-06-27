import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from domain.models.class_model import ClassModel
from domain.repositories.class_repository import ClassRepository
from infrastructure.adapters.data_sources.entities.class_entity import ClassEntity
from infrastructure.adapters.data_sources.db_config import db
from flask import jsonify

class ClassRepositoryAdapter(ClassRepository):
    def create_class(self, ClassModel):
        new_class = ClassEntity(name = ClassModel.name, number_of_students = ClassModel.number_of_students, teacher = ClassModel.teacher, status = ClassModel.status, group = ClassModel.group, grade = ClassModel.grade)
        db.add(new_class)
        db.commit()
        return jsonify(new_class.to_dict())
    
    def update_status(self, class_id, new_status):
        class_info = db.query(ClassEntity).filter(ClassEntity.id == class_id).first()
        class_info.status = new_status
        db.commit()
        return jsonify(class_info.to_dict())
    
    def update_number_of_students(self, class_id):
        class_info = db.query(ClassEntity).filter(ClassEntity.id == class_id).first()
        class_info.number_of_students = str(int(class_info.number_of_students) + 1)
        db.commit()
        return jsonify(class_info.to_dict())