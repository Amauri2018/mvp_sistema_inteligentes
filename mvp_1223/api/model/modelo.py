import numpy as np
import pickle
import joblib

class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([form.age, 
                            form.sex, 
                            form.cp, 
                            form.trestbps, 
                            form.chol, 
                            form.fbs, 
                            form.restecg, 
                            form.thalach,
                            form.exang,
                            form.oldpeak,
                            form.slope,
                            form.ca,
                            form.thal
                        ])
        #if X_input.shape[0] != 12:
            #raise ValueError(f'O modelo espera 12 características, mas foram fornecidas {X_input.shape[0]} características.')
        
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])