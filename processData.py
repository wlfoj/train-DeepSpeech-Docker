import sys
import csv

class ProcessPhrases():
    '''Classe para realizar o processamento dos textos'''

    @classmethod
    def cleanText(self, pathTest: str, pathTrain: str, pathDev: str):
        '''Método para realizar uma limpeza básica nos carcteres lixos'''
        # 0-> path test    1-> path train   2-> path dev
        arquivos = [pathTest, pathTrain, pathDev]
        for i in range(3):
            # Entra em cada arquivo
            with open(arquivos[i]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                texto = []
                # Passando por cada linha
                for linha in csv_reader:
                    # Fazendo as verificações e substituições de strings
                    # a coluna 2 é a das falas
                    if("ü" in linha[2]):
                        linha[2] = linha[2].replace("ü", "u")
                    if("´" in linha[2]):
                        linha[2] = linha[2].replace("´", "")
                    if("»" in linha[2]):
                        linha[2] = linha[2].replace("»", "")
                    if("'" in linha[2]):
                        linha[2] = linha[2].replace("'", "")
                    if("“" in linha[2]):
                        linha[2] = linha[2].replace("“", "")
                    if("”" in linha[2]):
                        linha[2] = linha[2].replace("”", "")
                    if("«" in linha[2]):
                        linha[2] = linha[2].replace("«", "")
                    if("è" in linha[2]):
                        linha[2] = linha[2].replace("è", "é")
                    # Adicionando o novo conteudo na lista
                    texto.append([linha[0],linha[1],linha[2]])
            # Atualizando os arquivos
            with open(arquivos[i], 'w') as arquivo_csv:
                escrever = csv.writer(arquivo_csv, delimiter=',', lineterminator='\n')
                for j in range(len(texto)):
                    escrever.writerow(texto[j])


    @classmethod
    def cleanTotalText(self, pathTest: str, pathTrain: str, pathDev: str):
        '''Método para realizar uma limpeza completa nos carcteres lixos'''
        # 0-> path test    1-> path train   2-> path dev
        arquivos = [pathTest, pathTrain, pathDev]
        for i in range(3):
            # Entra em cada arquivo
            with open(arquivos[i]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                texto = []
                # Passando por cada linha
                for linha in csv_reader:
                    # Fazendo as verificações e substituições de strings
                    # a coluna 2 é a das falas
                    if("ü" in linha[2]):
                        linha[2] = linha[2].replace("ü", "u")
                    if("´" in linha[2]):
                        linha[2] = linha[2].replace("´", "")
                    if("»" in linha[2]):
                        linha[2] = linha[2].replace("»", "")
                    if("'" in linha[2]):
                        linha[2] = linha[2].replace("'", "")
                    if("“" in linha[2]):
                        linha[2] = linha[2].replace("“", "")
                    if("”" in linha[2]):
                        linha[2] = linha[2].replace("”", "")
                    if("«" in linha[2]):
                        linha[2] = linha[2].replace("«", "")
                    if("é" in linha[2]):
                        linha[2] = linha[2].replace("é", "e")
                    if("ñ" in linha[2]):
                        linha[2] = linha[2].replace("ñ", "n")
                    if("ú" in linha[2]):
                        linha[2] = linha[2].replace("ú", "u")
                    if("è" in linha[2]):
                        linha[2] = linha[2].replace("è", "e")
                    if("í" in linha[2]):
                        linha[2] = linha[2].replace("í", "i")
                    if("ã" in linha[2]):
                        linha[2] = linha[2].replace("ã", "a")
                    if("ó" in linha[2]):
                        linha[2] = linha[2].replace("ó", "o")
                    if("á" in linha[2]):
                        linha[2] = linha[2].replace("á", "a")
                    if("ô" in linha[2]):
                        linha[2] = linha[2].replace("ô", "o")
                    if("â" in linha[2]):
                        linha[2] = linha[2].replace("â", "a")
                    if("õ" in linha[2]):
                        linha[2] = linha[2].replace("õ", "o")
                    if("à" in linha[2]):
                        linha[2] = linha[2].replace("à", "a")
                    if("ê" in linha[2]):
                        linha[2] = linha[2].replace("ê", "e")
                    # Adicionando o novo conteudo na lista
                    texto.append([linha[0],linha[1],linha[2]])
            # Atualizando os arquivos
            with open(arquivos[i], 'w') as arquivo_csv:
                escrever = csv.writer(arquivo_csv, delimiter=',', lineterminator='\n')
                for j in range(len(texto)):
                    escrever.writerow(texto[j])


def main():
    '''Procedimento para chamar e tratar os possíveis erros do processamento das falas'''

    try:
        ProcessPhrases.cleanText(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print("ERRO\nA chamada do arquivo deve ter 3 parametros")
        print("1 -> o caminho para a tabela de teste")
        print("2 -> o caminho para a tabela de treinamento")
        print("3 -> o caminho para a tabela de desenvolvimento")
    except FileNotFoundError:
        print("Arquivo não encontrado")
        print("Algum dos caminhos está incorreto")
    except:
        print("Error\nNão sei qual é")


if __name__ == "__main__":
    main()
