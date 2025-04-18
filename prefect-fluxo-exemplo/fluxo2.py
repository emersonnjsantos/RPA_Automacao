from prefect import flow, task
from graphviz import Digraph

@task
def carregar_dados():
    print("📦 Dados carregados")
    return [10, 20, 30]

@task
def validar_dados(dados):
    print("✅ Dados validados")
    return all(isinstance(x, int) for x in dados)

@task
def transformar_dados(dados):
    print("🔄 Dados transformados")
    return [x * 2 for x in dados]

@task
def salvar_dados(dados):
    print("💾 Dados salvos:", dados)

@task
def notificar_erro():
    print("🚨 Erro na validação dos dados!")

@flow(name="Fluxo-Orquestrado-Completo")
def fluxo_principal():
    dados = carregar_dados()
    valido = validar_dados(dados)

    if valido:
        transformado = transformar_dados(dados)
        salvar_dados(transformado)
    else:
        notificar_erro()

    # Geração do fluxograma
    dot = Digraph(comment="Fluxograma Completo")
    dot.node("A", "Carregar Dados")
    dot.node("B", "Validar Dados")
    dot.node("C1", "Transformar Dados")
    dot.node("C2", "Notificar Erro")
    dot.node("D", "Salvar Dados")

    dot.edge("A", "B")
    dot.edge("B", "C1", label="Se válido")
    dot.edge("B", "C2", label="Se inválido")
    dot.edge("C1", "D")

    dot.render("fluxograma_complexo", format="pdf", cleanup=True)
    print("📄 Fluxograma gerado: fluxograma_complexo.pdf")

if __name__ == "__main__":
    fluxo_principal()
