import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from sqlalchemy import Column, String
from infrastructure.adapters.data_sources.db_config import Base, db

class ClassEntity(Base):
    __tablename__ = 'classes'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String(100))
    number_of_students = Column(String(100))
    teacher = Column(String(100))
    status = Column(String(100))
    group = Column(String(100))
    grade = Column(String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'number_of_students': self.number_of_students,
            'teacher': self.teacher,
            'status': self.status,
            'group': self.group,
            'grade': self.grade
        }

Base.metadata.create_all(bind=db.get_bind())
