import luigi

# 1️⃣ Tarefa inicial: Buscar os produtos disponíveis
class BuscarProdutos(luigi.Task):
    def run(self):
        # Simulando que João viu 3 produtos no app
        produtos = ["Camisa", "Tênis", "Calça"]
        print(f"João visualizou os produtos: {produtos}")

        # Salvando os produtos num arquivo de saída simulado
        with self.output().open('w') as f:
            f.write(','.join(produtos))

    def output(self):
        # Indica onde os dados da tarefa serão salvos
        return luigi.LocalTarget("produtos.txt")

# 2️⃣ Tarefa intermediária: Calcular o total do carrinho
class CalcularTotalCarrinho(luigi.Task):
    def requires(self):
        # Essa tarefa depende da execução da anterior
        return BuscarProdutos()

    def run(self):
        # Lê os produtos do arquivo salvo pela tarefa anterior
        with self.input().open('r') as f:
            produtos = f.read().split(',')

        # Simula valores e calcula total
        precos = {"Camisa": 50, "Tênis": 120, "Calça": 80}
        total = sum(precos[p] for p in produtos)
        print(f"Total do carrinho de João: R${total}")

        # Salvando o total em um arquivo
        with self.output().open('w') as f:
            f.write(str(total))

    def output(self):
        return luigi.LocalTarget("total.txt")

# 3️⃣ Tarefa final: Gerar o recibo da compra
class GerarRecibo(luigi.Task):
    def requires(self):
        # Depende do cálculo total do carrinho
        return CalcularTotalCarrinho()

    def run(self):
        # Lê o total calculado anteriormente
        with self.input().open('r') as f:
            total = f.read()

        # Simula a geração de um recibo
        recibo = f"Recibo de compra - Cliente: João\nTotal pago: R${total}"
        print("\n🧾 Recibo gerado:\n" + recibo)

        with self.output().open('w') as f:
            f.write(recibo)

    def output(self):
        return luigi.LocalTarget("recibo.txt")

# 🚀 Aqui iniciamos o fluxo do Luigi
if __name__ == '__main__':
    luigi.build([GerarRecibo()], local_scheduler=True)
