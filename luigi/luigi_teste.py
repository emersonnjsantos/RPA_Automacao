import luigi

class MathematicalOperations(luigi.Task):
    intNum_1 = luigi.IntParameter()
    intNum_2 = luigi.IntParameter()

    def Add(self, intNum_1, intNum_2):
        return intNum_1 + intNum_2

    def Double(self, intNum):
        return 2 * intNum

    def run(self):
        soma = self.Add(self.intNum_1, self.intNum_2)
        doubled_sum = self.Double(soma)
        print(f'Resultado final: {doubled_sum}')


if __name__ == '__main__':
    luigi.build([MathematicalOperations(intNum_1=5, intNum_2=10)], local_scheduler=True)

