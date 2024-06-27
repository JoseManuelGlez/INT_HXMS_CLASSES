import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

sys.path.insert(0, r'C:\Users\12345\Desktop\ms-users')

from flask import Flask, request, jsonify
from infrastructure.adapters.class_repository_adapter import ClassRepositoryAdapter
from domain.models.class_model import ClassModel
from domain.uses_cases.class_use_case import ClassUseCase

app = Flask(__name__)

class_repository = ClassRepositoryAdapter()
class_use_case = ClassUseCase(class_repository)

class ApiRest:
    @app.route('/class', methods=['POST'])
    def create_class():
        clas = request.get_json()
        new_class = ClassModel(name = clas['name'], number_of_students = clas['number_of_students'], teacher = clas['teacher'], status = clas['status'], group = clas['group'], grade = clas['grade'])
        return class_use_case.create_class(new_class)
        
    
    @app.route('/class/status/<class_id>', methods=['PUT'])
    def update_status(class_id):
        data = request.get_json()
        new_status = data['status']
        return class_use_case.update_status(class_id, new_status)
    
    @app.route('/class/add-number-student/<class_id>', methods=['PUT'])
    def update_number_of_students(class_id):
        return class_use_case.update_number_of_students(class_id)

def start_api():
    app.run(host='0.0.0.0', port=3002, debug=True)
