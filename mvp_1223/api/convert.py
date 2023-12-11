import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pickle import dump
from pickle import load

# Carrega arquivo csv usando Pandas usando uma URL

# Informa a URL de importação do dataset
url = "https://raw.githubusercontent.com/Amauri2018/datasets/main/doenca_cardiaca.csv"

# Informa o cabeçalho das colunas
colunas = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']

# Lê o arquivo utilizando as colunas informadas
dataset = pd.read_csv(url, names=colunas, skiprows=0, delimiter=',')
dataset = dataset.iloc[1:]

# Pega apenas os dados do dataset e guardando em um array
array = dataset.values

# Separa o array em variáveis preditoras (X) e variável target (Y)
X = array[:,0:13]
Y = array[:,13]


# Divide os dados em treino e teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)

# Cria o modelo
modelo = LogisticRegression(solver='liblinear')

# Treina o modelo
modelo.fit(X_train, Y_train)

# Salva o modelo no disco
filename = 'doenca_cardiaca.pkl'
dump(modelo, open(filename, 'wb'))

# Salvar em formato .joblib
joblib_file = "doenca_cardiaca.joblib"
dump(modelo, open(joblib_file, 'wb'))


# Algum tempo depois...
# Carrega o modelo do disco
loaded_model = load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)