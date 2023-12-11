from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("name", String(50))
    age = Column("age", Integer)
    sex = Column("sex", Integer)
    cp = Column("cp", Integer)
    trestbps = Column("trestbps", Float)
    chol = Column("chol", Float)
    fbs = Column("fbs", Integer)
    restecg = Column("restecg", Integer)
    thalach = Column("thalach", Float)
    exang = Column("exang", Integer)
    oldpeak = Column("oldpeak", Float)
    slope = Column("slope", Float)
    ca = Column("ca", Float)
    thal = Column("thal", Integer)
    num = Column("num", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, age:int, sex:int, cp:int, 
                trestbps:float, chol:float, fbs:int, 
                restecg:int, thalach:float, exang:int, 
                oldpeak:float, slope:float, ca:float, 
                thal:int, num:int,
                data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
            name: nome do paciente
            age : idade em anos
            sex : sexo do paciente(0: mulher 1: homem)
            cp : tipo da dor torácica(1: angina típica, 2: angina atípica, 3: dor não cardíaca, 4: assintomática)
            trestbps : pressão arterial em repouso
            chol: colesterol sérico (mg/dl)
            fbs : açucar no sangue em jejum > 120mg/dl (0: False, 1: True)

            restecg : (resultado do eletrocardiografia de repouso
            0: normal
            1: anormalidades de ST-T (inversão da onda T e elevação ou depressão de > 0.05mV)
            2: hipertrofia ventricular esquerda provável ou definitiva (pelos critérios de Romhilt-Estes))

            thalach :frequência cardíaca máxima atingida
            exang : angina induzida pelo exercício (0: não, 1: sim)
            oldpeak :depessão do segmento ST induzida pelo exercício em relação ao repouso
            slope : inclinação do segmento ST no pico do exercício
            ca : número de vasos principais colorido por fluoroscopia

            thal :thallium stress test é um exame de imagem nuclear que mostra como o sangue flui para o coração enquanto você se exercita ou em repouso. O Thalium é um elemento químico radioativo.
            3: normal
            6: defeito fixo
            7: defeito reversível

            num :diagnóstico de doença cardíaca (diagnóstico angiográfico)
            0: não há doença cardíaca ( < 50% de estreitamento do diâmetro)
            1,2,3,4: há doença cardíaca ( > 50% de estreitamento do diâmetro)

            data_insercao: data de quando o paciente foi inserido à base
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.num = num

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao