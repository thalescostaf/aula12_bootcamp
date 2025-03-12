import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
            self.df = pd.read_csv(self.file_path)

    def filtrar_por_estado(self, coluna, atributo):
            return self.df[self.df[coluna] == atributo]
        

arquivo_csv = './exemplo.csv'

filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
resultado = arquivo_CSV.filtrar_por_estado(filtro,limite)

print(resultado)


arquivo_csv2 = './exemplo2.csv'

filtro2 = 'estado'
limite2 = 'TO'

arquivo_CSV2 = CsvProcessor(arquivo_csv2)
arquivo_CSV2.carregar_csv()
resultado2 = arquivo_CSV2.filtrar_por_estado(filtro2, limite2)

print("")
print(resultado2)