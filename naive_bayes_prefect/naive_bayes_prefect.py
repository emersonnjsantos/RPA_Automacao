from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

from prefect import flow, task

# Tarefa 1: Carregar o dataset
@task
def load_iris_data():
    iris = load_iris()
    X = iris.data
    Y = iris.target
    return X, Y

# Tarefa 2: Dividir os dados em treino e teste
@task
def split_data(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
    return X_train, X_test, Y_train, Y_test

# Tarefa 3: Executar o Naive Bayes
@task
def execute_naive_bayes(X_train, X_test, Y_train, Y_test):
    model = GaussianNB()
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test, y_pred)
    print(f"🔍 Precisão do modelo: {acc:.2%}")
    return acc

# Fluxo principal
@flow(name="Execute-Naive-Bayes")
def run_pipeline():
    X, Y = load_iris_data()
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    accuracy = execute_naive_bayes(X_train, X_test, Y_train, Y_test)
    return accuracy

if __name__ == "__main__":
    run_pipeline()
