from prefect import flow, task
from graphviz import Digraph

@task
def Add(intNum_1, intNum_2):
    return intNum_1 + intNum_2

@task
def Double(intNum):
    return 2 * intNum

@task
def Print_Value(strValue):
    print(f"Resultado final: {strValue}")

@flow(name="Operações-Matemáticas")
def run_operations():
    intNum_1 = 5
    intNum_2 = 10

    soma = Add(intNum_1, intNum_2)
    dobrado = Double(soma)
    Print_Value(dobrado)

    # Corrigido: gerar fluxograma com tuplas
    dot = Digraph(comment="Fluxograma das Operações")
    dot.node("Start", "Start")
    dot.node("A", "Add(5, 10)")
    dot.node("B", "Double(soma)")
    dot.node("C", "Print_Value(dobrado)")
    dot.node("End", "End")

    # Agora com tuplas corretamente
    dot.edges([("Start", "A"), ("A", "B"), ("B", "C"), ("C", "End")])

    dot.render("fluxograma_operacoes_matematicas", format="pdf", cleanup=True)
    print("Fluxograma gerado como PDF.")

if __name__ == "__main__":
    run_operations()
