from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Angelica"
    age: int = 35
    sex: int = 0
    cp: int = 2
    trestbps: float = 152.0
    chol: float = 90.0
    fbs: int = 0
    restecg: int = 1
    thalach: float = 120.0
    exang: int = 1
    oldpeak: float = 140.5
    slope: float = 120.3
    ca: float = 153.3
    thal: int = 3
     
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Angelica"
    age: int = 35
    sex: int = 0
    cp: int = 2
    trestbps: float = 152.0
    chol: float = 90.0
    fbs: int = 0
    restecg: int = 1
    thalach: float = 120.0
    exang: int = 1
    oldpeak: float = 140.5
    slope: float = 120.3
    ca: float = 153.3
    thal: int = 3
    num: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Angelica"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Angelica"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trestbps": paciente.trestbps,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalach": paciente.thalach,
        "exang": paciente.exang,
        "oldpeak": paciente.oldpeak,
        "slope": paciente.slope,
        "ca": paciente.ca,
        "thal": paciente.thal,
        "num": paciente.num
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex": paciente.sex,
            "cp": paciente.cp,    
            "trestbps": paciente.trestbps,
            "chol": paciente.chol,
            "fbs": paciente.fbs,
            "restecg": paciente.restecg,
            "thalach": paciente.thalach,
            "exang": paciente.exang,
            "oldpeak": paciente.oldpeak,
            "slope": paciente.slope,
            "ca": paciente.ca,
            "thal": paciente.thal,
            "num": paciente.num
        })

    return {"pacientes": result}

