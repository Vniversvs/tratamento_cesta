import pandas as pd
import xlwt
import time



##### TODO
##### criar memória pra não ter que ler as mesmas planilhas de novo
##### criar janela
##### fazer o programa emitir planilhas





# class Venda:
#     def __init__(self, dia, quantidade):
#         self.dia = dia
#         # self.produto = produto
#         self.quantidade = quantidade


class Produto:
    def __init__(self, nome,  Und, preco_compra, preco_venda, vendas, produtor):
        self.nome = nome
        self.Und = Und
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.vendas = vendas
        self.produtor = produtor
        # self.Uniformizar_Unidade()

    def add_venda(self, venda):
        self.vendas.append(venda)

    def Total_Vendas(self):
        return sum(self.vendas)

    def Comparar_Produtos(self, produto):
        if self.nome == produto.nome and self.Und == produto.Und and self.produtor == produto.produtor:
            return True
        return False

    def Uniformizar_Unidade(self):
        if "Metade" in self.nome:
            return [500, "ml"]
        self.Und = self.Und.replace(" ", "")
        self.Und = self.Und.replace("1litro", "1000ml")
        self.Und = self.Und.replace("1Litro", "1000ml")
        self.Und = self.Und.replace("1Kg", "1000g")
        self.Und = self.Und.replace("1kg", "1000g")
        self.Und = self.Und.replace("kg", "1000g")
        self.Und = self.Und.replace("mls", "ml")
        self.Und = self.Und.replace("Dz", "dz")
        self.Und = self.Und.replace("pé", "Molho")
        self.Und = self.Und.replace("Unidade", "und")
        self.Und = self.Und.replace("gr", "g")
        qtd = ""
        UND = ""
        for character in self.Und:
            if character in "1234567890":
                qtd += character
            else:
                UND += character
        if qtd == "":
            qtd = "1"
        retu = [int(qtd), UND]
        return retu


#### DADOS GLOBAIS
lista_de_produtores=[ "Agricultores MPA RJ", "Arroz Velho Chico (MPA Sergipe)", "Cervejas Artesanais ", "COOPERNATURAL", "Copirecê", "EcoBio", "Fazenda Vale da Lua", "Grupo Semear",
                      "Mel Teresópolis", "Monte Veneto", "MPA-ES", "MPA-RJ", "MST/RS", "Nanna Natus", "Natucoa", "Naturalmente", "Severino (Bio)", "Sitio do Hudson", "Sítio Santo Antônio",
                     "Somma Kombucha", "Sustenta Chips Banana e Aipim", "Thiago", "Troço Bom", "UPC Luciano"]















# Datas_de_Entrega0 = ["28-02", "20-03", "04-04", "08-04", "11-04", "15-04", "18-04", "22-04", "25-04"]
# Planilhas = []

# for x in Datas_de_Entrega0:
#     Datas_de_Entrega.append("Entrega " + x + "-2020.xlsx")

# file = pd.ExcelFile("Entrega 20-03-2020 teste.xlsx")



# Planilha = pd.read_excel("Entrega 28-02-2020.xlsx", sheet_name="Sheet1")
# Planilha2 = pd.read_excel("Entrega 20-03-2020.xlsx", sheet_name="Sheet1")
# Planilha3 = pd.read_excel("Entrega 04-04-2020.xlsx", sheet_name="Sheet1")
# Planilha4 = pd.read_excel("Entrega 08-04-2020.xlsx", sheet_name="Sheet1")
# Planilha4_2 = pd.read_excel("Entrega 08-04-2020 2.xlsx", sheet_name="Sheet1")
# Planilha5 = pd.read_excel("Entrega 11-04-2020.xlsx", sheet_name="Sheet1")
# Planilha6 = pd.read_excel("Entrega 15-04-2020.xlsx", sheet_name="Sheet1")
# Planilha7 = pd.read_excel("Entrega 18-04-2020.xlsx", sheet_name="Sheet1")
# Planilha8 = pd.read_excel("Entrega 22-04-2020.xlsx", sheet_name="Sheet1")
# Planilha9 = pd.read_excel("Entrega 25-04-2020.xlsx", sheet_name="Sheet1")
# Planilha9_2 = pd.read_excel("Entrega 25-04-2020 2.xlsx", sheet_name="Sheet1")
# Planilha10 = pd.read_excel("Entrega 29-04-2020.xlsx", sheet_name="Sheet1")
# Planilha11 = pd.read_excel("Entrega 02-05-2020 1.xlsx", sheet_name="Sheet1")
# Planilha12 = pd.read_excel("Entrega 02-05-2020 2.xlsx", sheet_name="Sheet1")
# Planilha13 = pd.read_excel("Entrega 06-05-2020 1.xlsx", sheet_name="Sheet1")
# Planilha14 = pd.read_excel("Entrega 06-05-2020 2.xlsx", sheet_name="Sheet1")
# Planilha15 = pd.read_excel("Entrega 14-03-2020.xlsx", sheet_name="Sheet1")
# Planilha16 = pd.read_excel("Entrega 18-03-2020.xlsx", sheet_name="Sheet1")
# Planilha17 = pd.read_excel("Entrega 21-03-2020.xlsx", sheet_name="Sheet1")
# Planilha18 = pd.read_excel("Entrega 25-03-2020.xlsx", sheet_name="Sheet1")
# Planilha19 = pd.read_excel("Entrega 28-03-2020.xlsx", sheet_name="Sheet1")

# Planilha20 = pd.read_excel("Entrega 09-05-2020 1.xlsx", sheet_name="Sheet1")

# produtos = []


def Procurar_ColunaTotal(Planilha):
    i = 0
    while Planilha.columns[i] != "Total Pedido":
        i += 1
    return i

def Procurar_Total(Planilha):
    i = 0
    while Planilha.columns[i] != "Total Pedido":
        i += 1
    return Planilha.columns[i]


def info_produto(linha, Planilha, produtor_da_vez):
    nome = Planilha.iloc[linha][0]
    Und = Planilha.iloc[linha][1]
    valor_compra = Planilha.iloc[linha][2]
    valor_venda = Planilha.iloc[linha][3]
    vendas = []
    produtor = produtor_da_vez
    return [nome, Und, valor_compra, valor_venda, vendas, produtor]

# produtor_da_vez = "Arroz Velho Chico (MPA Sergipe)"
def Primeiro_Produtor(Planilha):
    return list(Planilha.columns.values)[0]


def get_Tamanho(Planilha):
    return len(Planilha.index)



# print(Procurar_ColunaTotal(Planilha20))
# print(info_produto(2, Planilha20, Primeiro_Produtor(Planilha20)))
# print(get_Tamanho(Planilha20))


def check_produto(nome, Und, produtor, produtos):
    for produto in produtos:
        if nome == produto.nome and Und == produto.Und and produtor == produto.produtor:
            return True
    return False

def add_Produto_Linha(Produtor_da_Vez, Planilha, Produtos, linha):
    produto = Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Planilha.iloc[linha][2], Planilha.iloc[linha][3], [], Produtor_da_Vez)
    if produto not in Produtos:
        Produtos.append(produto)

# def add_Produtos_Planilha_Produtor(Planilha, Produtor, produtos):
#     linha = 0
#     produtor_da_vez = Primeiro_Produtor(Planilha)
#     while linha < get_Tamanho(Planilha)-2:
#         if "TOTAL" in Planilha.iloc[linha][0]:
#             linha += 2
#             produtor_da_vez = Planilha.iloc[linha][0]
#             linha += 1
#         else:


def add_Produtos_Planilha(Planilha, produtos):
    produtor_da_vez = Primeiro_Produtor(Planilha)
    linha = 0
    while linha < get_Tamanho(Planilha)-2:
        if "TOTAL" in Planilha.iloc[linha][0]:
            linha += 2
            produtor_da_vez = Planilha.iloc[linha][0]
            linha += 1
        else:
            dados_do_produto = info_produto(linha, Planilha, produtor_da_vez)
            if check_produto(dados_do_produto[0], dados_do_produto[1], produtor_da_vez, produtos) == False:
                produtos.append(Produto(dados_do_produto[0], dados_do_produto[1], dados_do_produto[2],
                                  dados_do_produto[3], dados_do_produto[4], dados_do_produto[5]))
            linha += 1
    return produtos

def Procurar_Produto(nome, Und, produtor, produtos):
    i = 0
    while i < len(produtos):
        if nome == produtos[i].nome and Und == produtos[i].Und and produtor == produtos[i].produtor:
            return produtos[i]
        i += 1


# def add_Vendas_Planilha(Planilha):
#     linha = 0
#     while linha < get_Tamanho(Planilha):
#         if Planilha.iloc[linha][0] in infos_dos_produtos:
#             Procurar_Produto(Planilha.iloc[linha][0]).add_venda(Planilha.iloc[linha][Procurar_Total(Planilha)])
#         linha += 1

def add_Vendas_Planilha(Planilha, produtos):
    produtor_da_vez = Primeiro_Produtor(Planilha)
    infos = []
    linha = 0
    for produto in produtos:
        infos.append([produto.nome, produto.Und, produto.produtor])
    while linha < get_Tamanho(Planilha)-2:
        if [Planilha.iloc[linha][0], Planilha.iloc[linha][1], produtor_da_vez] in infos:
            Procurar_Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], produtor_da_vez, produtos).add_venda(Planilha.iloc[linha][Procurar_Total(Planilha)])
            linha += 1
        if "TOTAL" in Planilha.iloc[linha][0]:
            linha += 2
            produtor_da_vez = Planilha.iloc[linha][0]
            linha += 1




# add_Produtos_Planilha(Planilha)

# add_Produtos_Planilha(Planilha2)
# add_Produtos_Planilha(Planilha3)
# add_Produtos_Planilha(Planilha4)
# add_Produtos_Planilha(Planilha4_2)
# add_Produtos_Planilha(Planilha5)
# add_Produtos_Planilha(Planilha6)
# add_Produtos_Planilha(Planilha7)
# add_Produtos_Planilha(Planilha8)
# add_Produtos_Planilha(Planilha9)
# add_Produtos_Planilha(Planilha9_2)
# add_Produtos_Planilha(Planilha10)
# add_Produtos_Planilha(Planilha11)
# add_Produtos_Planilha(Planilha12)
# add_Produtos_Planilha(Planilha13)
# add_Produtos_Planilha(Planilha14)
# add_Produtos_Planilha(Planilha15)
# add_Produtos_Planilha(Planilha16)
# add_Produtos_Planilha(Planilha17)
# add_Produtos_Planilha(Planilha18)
# add_Produtos_Planilha(Planilha19)

# add_Produtos_Planilha(Planilha20)
#




# add_Vendas_Planilha(Planilha)

# add_Vendas_Planilha(Planilha2)
# add_Vendas_Planilha(Planilha3)
# add_Vendas_Planilha(Planilha4)
# add_Vendas_Planilha(Planilha4_2)
# add_Vendas_Planilha(Planilha5)
# add_Vendas_Planilha(Planilha6)
# add_Vendas_Planilha(Planilha7)
# add_Vendas_Planilha(Planilha8)
# add_Vendas_Planilha(Planilha9)
# add_Vendas_Planilha(Planilha9_2)
# add_Vendas_Planilha(Planilha10)
# add_Vendas_Planilha(Planilha11)
# add_Vendas_Planilha(Planilha12)
# add_Vendas_Planilha(Planilha13)
# add_Vendas_Planilha(Planilha14)
# add_Vendas_Planilha(Planilha15)
# add_Vendas_Planilha(Planilha16)
# add_Vendas_Planilha(Planilha17)
# add_Vendas_Planilha(Planilha18)
# add_Vendas_Planilha(Planilha19)

# add_Vendas_Planilha(Planilha20)




# for produto in produtos:
#     print([produto.nome, produto.Und, sum(produto.vendas), produto.produtor])



def Fazer_Total(produtos):
    Planilha_Totais = xlwt.Workbook()
    sheet = Planilha_Totais.add_sheet("Sheet1")
    sheet.write(0, 0, "Nome do Produto")
    sheet.write(0, 1, "Unidade")
    sheet.write(0, 2, "Preço de Compra")
    sheet.write(0, 3, "Preço de Venda")
    sheet.write(0, 4, "Total de pedidos")
    sheet.write(0, 5, "Produtor")
    for i in range(1, len(produtos)):
        sheet.write(i, 0, produtos[i].nome)
        sheet.write(i, 1, produtos[i].Und)
        sheet.write(i, 2, produtos[i].preco_compra)
        sheet.write(i, 3, produtos[i].preco_venda)
        sheet.write(i, 4, sum(produtos[i].vendas))
        sheet.write(i, 5, produtos[i].produtor)
    Planilha_Totais.save('Planilha de Totais.xlsx')


# Totais = xlwt.Workbook()
# sheet = Totais.add_sheet('test')
# sheet.write(0, 0, "Nome do Produto")
# sheet.write(0, 1, "Unidade")
# sheet.write(0, 2, "Preço de Compra")
# sheet.write(0, 3, "Preço de Venda")
# sheet.write(0, 4, "Total de pedidos")
# sheet.write(0, 5, "Produtor")
# for i in range(1, len(produtos)):
#     sheet.write(i, 0, produtos[i].nome)
#     sheet.write(i, 1, produtos[i].Und)
#     sheet.write(i, 2, produtos[i].preco_compra)
#     sheet.write(i, 3, produtos[i].preco_venda)
#     sheet.write(i, 4, sum(produtos[i].vendas))
#     sheet.write(i, 5, produtos[i].produtor)
# Totais.save('Totais3.xlsx')





############################################### segunda parte



# Planilha_Totais = pd.read_excel("Totais3.xlsx", sheet_name="test")






def uniformizar_unidade(linha, Planilha):
    if "Metade" in Planilha.iloc[linha]["Nome do Produto"]:
        return [500, "ml"]
    unidade = Planilha.iloc[linha]["Unidade"].replace(" ", "")
    unidade = unidade.replace("1litro", "1000ml")
    unidade = unidade.replace("1Litro", "1000ml")
    unidade = unidade.replace("1Kg", "1000g")
    unidade = unidade.replace("1kg", "1000g")
    unidade = unidade.replace("kg", "1000g")
    unidade = unidade.replace("mls", "ml")
    unidade = unidade.replace("Dz", "dz")
    unidade = unidade.replace("pé", "Molho")
    unidade = unidade.replace("Unidade", "und")
    unidade = unidade.replace("gr", "g")
    qtd = ""
    UND = ""
    for character in unidade:
        if character in "1234567890":
            qtd += character
        else: UND += character
    if qtd == "":
        qtd = "1"

    retu = [int(qtd), UND]

    return retu



def get_produtores(Planilha):
    produtores = []
    linha = 0
    while linha < get_Tamanho(Planilha):
        if Planilha.iloc[linha][5].replace("/", "") not in produtores:
            produtores.append(Planilha.iloc[linha][5].replace("/", ""))
        linha += 1
    return produtores

# produtores = get_produtores(Planilha_Totais)




def Somar_Planilha(Planilha):
    linha = 0
    soma = [[0, "g"], [0, "ml"], [0, "Molho"], [0, "und"], [0, "dz"]]
    while linha < get_Tamanho(Planilha):
        quantidade_da_linha = uniformizar_unidade(linha, Planilha)
        for coisa in soma:
            if quantidade_da_linha[1] == coisa[1]:
                coisa[0]+=quantidade_da_linha[0]*Planilha.iloc[linha][4]
        linha+=1
    soma[0][0] = soma[0][0]/1000
    soma[0][1] = "Kg"
    soma[1][0] = soma[1][0]/1000
    soma[1][1] = "L"
    return soma




def Converter_Molhos(soma):
    soma[0][0] += soma[2][0]*0.3
    soma.pop(2)
    return soma

# soma = Somar_Planilha(Planilha_Totais)




def Analisar_xlsx(arquivo):
    Planilha = pd.read_excel(arquivo, sheet_name="Sheet1")
    produtos = add_Produtos_Planilha(Planilha, [])
    add_Vendas_Planilha(Planilha, produtos)
    Fazer_Total(produtos)
    time.sleep(2)
    Planilha_Totais = pd.read_excel("Planilha de Totais.xlsx", sheet_name="Sheet1")
    return Somar_Planilha(Planilha_Totais)

def somar_somas(soma1, soma2):
    return [[soma1[0][0]+soma2[0][0], "Kg"], [soma1[1][0]+soma2[1][0], "L"], [soma1[2][0]+soma2[2][0], "Molho"], [soma1[3][0]+soma2[3][0], "und"], [soma1[4][0]+soma2[4][0], "dz"]]


def printbonito(soma):
    return "vendemos " + str(soma[0][0])+soma[0][1] + ", " + str(soma[1][0])+soma[1][1] + ", " + str(soma[2][0])+soma[2][1] + ", " + str(soma[3][0])+soma[3][1] + ", " + str(soma[4][0])+soma[4][1]

# print(somar_somas(Analisar_xlsx("Entrega 02-05-2020 1.xlsx"), Analisar_xlsx("Entrega 02-05-2020 2.xlsx")))
# print(somar_somas(Analisar_xlsx("Entrega 06-05-2020 1.xlsx"), Analisar_xlsx("Entrega 06-05-2020 2.xlsx")))
# print(Analisar_xlsx("Entrega 09-05-2020 1.xlsx"))
# print(somar_somas(Analisar_xlsx("Entrega 13-05-2020 1.xlsx"), Analisar_xlsx("Entrega 13-05-2020 2.xlsx")))
# print(somar_somas(Analisar_xlsx("Entrega 16-05-2020 1.xlsx"), Analisar_xlsx("Entrega 16-05-2020 2.xlsx")))
# print(somar_somas(Analisar_xlsx("Entrega 20-05-2020 1.xlsx"), Analisar_xlsx("Entrega 20-05-2020 2.xlsx")))
# print(somar_somas(Analisar_xlsx("Entrega 23-05-2020 1.xlsx"), Analisar_xlsx("Entrega 23-05-2020 2.xlsx")))


# print(printbonito(somar_somas(Analisar_xlsx("Entrega 20-05-2020 1.xlsx"), Analisar_xlsx("Entrega 20-05-2020 2.xlsx"))))
# print(printbonito(somar_somas(Analisar_xlsx("Entrega 23-05-2020 1.xlsx"), Analisar_xlsx("Entrega 23-05-2020 2.xlsx"))))




def Addxlsx_Produtos_Produtor(arquivo, Produtor, produtos):
    Planilha = pd.read_excel(arquivo, sheet_name="Sheet1")
    if Get_Linhas_Produtor(Planilha, Produtor) ==False:
        return produtos
    elif Get_Linhas_Produtor(Planilha, Produtor)!=False:
        linhas = Get_Linhas_Produtor(Planilha, Produtor)
        Planilha=Planilha.filter(linhas, axis=0)
        linha = 1
        while linha < get_Tamanho(Planilha):
            if check_produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Produtor, produtos) == False:
                produtos.append(Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Planilha.iloc[linha][2], Planilha.iloc[linha][3], [Planilha.iloc[linha][Procurar_Total(Planilha)]], Produtor))
            else: Procurar_Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Produtor, produtos).add_venda(Planilha.iloc[linha][Procurar_Total(Planilha)])
            linha += 1
    return produtos

def Analisar_Produtor(arquivos, Produtor, produtos):
    while len(arquivos) > 0:
        produtos=Addxlsx_Produtos_Produtor(arquivos[0],Produtor,produtos)
        arquivos.remove(arquivos[0])
    return produtos



def Analisar_Produtor_xlsx(arquivos, Produtor):
    produtos = []
    for arquivo in arquivos:
        Addxlsx_Produtos_Produtor(arquivo, Produtor, produtos)
    for arquivo in arquivos:
        Planilha = pd.read_excel(arquivo, sheet_name="Sheet1")
        linhas = Get_Linhas_Produtor(Planilha, Produtor)
        Planilha=Planilha.filter(linhas, axis=0)
        add_Vendas_Planilha(Planilha, produtos)
    Fazer_Total(produtos)
    time.sleep(2)
    Planilha_Totais = pd.read_excel("Planilha de Totais.xlsx", sheet_name="Sheet1")
    return Somar_Planilha(Planilha_Totais)
    # return produtos




    # Planilha = pd.read_excel(arquivo, sheet_name="Sheet1")
    # Planilha=Planilha.filter(Get_Linhas_Produtor(Planilha, Produtor))
    # linha = 1
    # produtos=[]
    # while linha < get_Tamanho(Planilha):
    #     produtos.append(Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Planilha.iloc[linha][2], Planilha.iloc[linha][3], [], Produtor))
    #     linha+=1

    ###
    # for linha in range(linhas[0], linhas[1]):
    #     add_Produto_Linha(Produtor, Planilha, produtos, linha)
    # produtos = add_Produtos_Planilha(Planilha, [])
    # for produto in produtos:
    #     if produto.produtor != Produtor:
    #         produtos.remove(produto)
    ###







# print(Analisar_Produtor_xlsx("Entrega 16-05-2020 2.xlsx", Produtor1))
# print(Analisar_xlsx("Entrega 16-05-2020 2.xlsx"))

def Get_Linhas_Produtor(Planilha, Produtor):
    lista = []
    linha = 0
    totais = []
    if Planilha.columns[0] == Produtor:
        lista.append(0)
    while linha < get_Tamanho(Planilha)-2:
        if Planilha.iloc[linha][0] == Produtor:
            lista.append(linha)
            linha+=1
        elif "TOTAL" in Planilha.iloc[linha][0]:
            totais.append(linha)
            linha+=1
        else: linha+=1
    if lista == []:
        return False
    while totais[0]<lista[0]:
        totais.remove(totais[0])
    return [i for i in range(lista[0], totais[0])]
    # return [n for n in range(0, lista[0])]+[n for n in range(totais[0], get_Tamanho(Planilha))]



# for produto in produtos:
#     print([produto.nome, produto.Und,produto.vendas, produto.Total_Vendas()])





def Total_Produtos(produtos):
    total=[[0, "g"], [0, "ml"], [0, "Molhos"], [0, "und"], [0, "dz"] ]
    for produto in produtos:
        quantidade=produto.Uniformizar_Unidade()
    for produto in produtos:
        for coisa in total:
            if coisa[1] in produto.Und:
                coisa[0]+=produto.Total_Vendas()*quantidade[0]
    total[0][1]="kg"
    total[0][0]=total[0][0]/1000
    total[1][0]=total[1][0]/1000
    total[1][1]="L"
    return total


def Total_Produtos_Produtor(produtos, produtor):
    total=[[0, "g"], [0, "ml"], [0, "Molhos"], [0, "und"], [0, "dz"] ]
    for produto in produtos:
        quantidade=produto.Uniformizar_Unidade()
    for produto in produtos:
        if produto.produtor == produtor:
            for coisa in total:
                if coisa[1] in produto.Und:
                    coisa[0]+=produto.Total_Vendas()*quantidade[0]
    total[0][1]="kg"
    total[0][0]=total[0][0]/1000
    total[1][0]=total[1][0]/1000
    total[1][1]="L"
    return total

    pass



arqs1 = ["Entrega 02-05-2020 1.xlsx", "Entrega 02-05-2020 2.xlsx", "Entrega 06-05-2020 1.xlsx", "Entrega 06-05-2020 2.xlsx",
         "Entrega 09-05-2020 1.xlsx", "Entrega 09-05-2020 2.xlsx", "Entrega 13-05-2020 1.xlsx", "Entrega 13-05-2020 2.xlsx",
         "Entrega 16-05-2020 1.xlsx", "Entrega 16-05-2020 2.xlsx", "Entrega 20-05-2020 1.xlsx", "Entrega 20-05-2020 2.xlsx",
         "Entrega 23-05-2020 1.xlsx", "Entrega 23-05-2020 2.xlsx", "Entrega 27-05-2020 1.xlsx", "Entrega 27-05-2020 2.xlsx",
         "Entrega 30-05-2020 1.xlsx", "Entrega 30-05-2020 2.xlsx"]

marco = [ 'Entrega 28-03-2020.xlsx', 'Entrega 25-03-2020.xlsx', 'Entrega 21-03-2020.xlsx']
abril = ['Entrega 29-04-2020.xlsx',
         'Entrega 25-04-2020 1.xlsx', 'Entrega 25-04-2020 2.xlsx', 'Entrega 22-04-2020.xlsx', 'Entrega 18-04-2020 2.xlsx',
         'Entrega 18-04-2020 1.xlsx', 'Entrega 15-04-2020.xlsx', 'Entrega 11-04-2020.xlsx', 'Entrega 08-04-2020 2.xlsx',
         'Entrega 08-04-2020 1.xlsx', 'Entrega 04-04-2020.xlsx', 'Entrega 01-04-2020.xlsx']
maio = ['Entrega 30-05-2020 1.xlsx', 'Entrega 30-05-2020 2.xlsx', 'Entrega 27-05-2020 1.xlsx', 'Entrega 27-05-2020 2.xlsx',
         'Entrega 23-05-2020 1.xlsx', 'Entrega 23-05-2020 2.xlsx', 'Entrega 20-05-2020 1.xlsx', 'Entrega 20-05-2020 2.xlsx',
         'Entrega 16-05-2020 1.xlsx', 'Entrega 16-05-2020 2.xlsx', 'Entrega 13-05-2020 1.xlsx', 'Entrega 13-05-2020 2.xlsx',
         'Entrega 09-05-2020 1.xlsx', 'Entrega 09-05-2020 2.xlsx', 'Entrega 06-05-2020 1.xlsx', 'Entrega 06-05-2020 2.xlsx',
         'Entrega 02-05-2020 1.xlsx', 'Entrega 02-05-2020 2.xlsx']
junho = ['Entrega 27-06-2020 1.xlsx', 'Entrega 27-06-2020 2.xlsx', 'Entrega 24-06-2020 1.xlsx', 'Entrega 24-06-2020 2.xlsx',
         'Entrega 20-06-2020 1.xlsx', 'Entrega 20-06-2020 2.xlsx', 'Entrega 17-06-2020 1.xlsx', 'Entrega 17-06-2020 2.xlsx',
         'Entrega 13-06-2020 1.xlsx', 'Entrega 13-06-2020 2.xlsx', 'Entrega 10-06-2020 1.xlsx', 'Entrega 10-06-2020 2.xlsx',
         'Entrega 06-06-2020 1.xlsx', 'Entrega 06-06-2020 2.xlsx', 'Entrega 03-06-2020 1.xlsx', 'Entrega 03-06-2020 2.xlsx']

# arqs2 = ["Entrega 16-05-2020 2.xlsx"]




def print_produtor(produtor):
    produtos = Analisar_Produtor(arqs1, produtor, [])
    print(Total_Produtos(produtos))

def extrair_numeros(lista):
    return [float(lista[0][0]), float(lista[1][0]), float(lista[2][0]), float(lista[3][0]), float(lista[4][0])]

lista_dos_produtores2=["Cervejas Artesanais ", "COOPERNATURAL", "EcoBio", "Ervas e Afins", "Mel Teresópolis", "MST/RS", "Nanna Natus", "Natucoa", "Naturalmente", "Somma Kombucha",
                       "Troço Bom", "Ubá Chocolates Artesanais"]
# print_produtor(lista_dos_produtores2[11])

# print_produtor(lista_de_produtores[0])
# print_produtor(lista_de_produtores[1])
# print_produtor(lista_de_produtores[2])

# produtos=Analisar_Produtor(arqs1, lista_de_produtores[1], [])
# for produto in produtos:
#     print(produto.Und)
#     print(produto.vendas)
#     quantidade=produto.Uniformizar_Unidade()
#     # print([produto.Und, quantidade])
#     print(Total_Produtos(produtos))



def Totais_do_Mes(arquivos):
    lista=[]
    for arq in arquivos:
        lista.append(extrair_numeros(Analisar_xlsx(arq)))
    df=pd.DataFrame(columns=["Kg", "L", "Molhos", "und", "dz"], data=lista)
    df.to_excel("Totais do Mês.xlsx")

Totais_do_Mes(marco)

# total=[[0, "g"], [0, "ml"], [0, "Molhos"], [0, "Und"], [0, "dz"] ]
# for produto in produtos:
#     print(produto.Und)
#     print(total[0][1])
#     print(total[0][1]==produto.Und)

#     quantidade=produto.Uniformizar_Unidade()
#     print(quantidade)
#     for coisa in total:
#         print(produto.Und==coisa[1])

# print(total)






























# df = pd.DataFrame({"Letters": ["a", "b", "c", "d", "e"], "Numbers": [1, 2, 3, 4, 5]})
# Planilha = pd.read_excel("Entrega 16-05-2020 2.xlsx", sheet_name="Sheet1")
# Planilha=Planilha.filter(Get_Linhas_Produtor(Planilha, "EcoBio"), axis=0)
# print(Analisar_Produtor_xlsx("Entrega 16-05-2020 2.xlsx", "EcoBio"))



# print(Addxlsx_Produtos_Produtor("Entrega 16-05-2020 2.xlsx", "EcoBio", []))

# for produto in Addxlsx_Produtos_Produtor("Entrega 16-05-2020 2.xlsx", "EcoBio", []):
#     print(produto.nome)





# print(Planilha)
# produtos=[]
# for linha in range(1, get_Tamanho(Planilha)):
#     print([Planilha.iloc[linha][0], Planilha.iloc[linha][1], Planilha.iloc[linha][2], Planilha.iloc[linha][3], [], "EcoBio"])
# linha=1
# while linha < get_Tamanho(Planilha):
#     produtos.append(Produto(Planilha.iloc[linha][0], Planilha.iloc[linha][1], Planilha.iloc[linha][2], Planilha.iloc[linha][3], [], "EcoBio"))
#     linha+=1
# for produto in produtos:
#     print(produto.nome)
# print(len(produtos))








# print(Planilha)
# print(Get_Linhas_Produtor(Planilha, "EcoBio"))
# while Planilha.iloc[0][0] != "EcoBio":
#     Planilha=Planilha.drop(0)
# linhas=Get_Linhas_Produtor(Planilha, "EcoBio")
# lista=[]
# for i in range(0, linhas[0]):
#     lista.append(i)

# print(Planilha)
# print(Get_Linhas_Produtor(Planilha, "EcoBio"))

# print(Planilha)

# print(Get_Linhas_Produtor(Planilha, "EcoBio"))












# def somar_produtor(produtor):
#     linha = 0
#     soma = [[0, "g"], [0, "ml"], [0, "Molho"], [0, "und"], [0, "dz"]]
#     while Planilha_Totais.iloc[linha][0] != "fim":
#         if Planilha_Totais.iloc[linha][5].replace("/", "") == produtor:
#             for coisa in soma:
#                 if uniformizar_unidade(linha)[1] == coisa[1]:
#                     coisa[0] += uniformizar_unidade(linha)[0]*Planilha_Totais.iloc[linha][4]
#         linha += 1
#     soma[0][0] = soma[0][0]/1000
#     soma[0][1] = "Kg"
#     soma[1][0] = soma[1][0]/1000
#     soma[1][1] = "L"
#     return soma
#
# soma_kg = 0
# soma_L = 0
# soma_molho = 0
# soma_und = 0
#
# for produtor in produtores:
#     soma_kg += somar_produtor(produtor)[0][0]
#     soma_L += somar_produtor(produtor)[1][0]
#     soma_molho += somar_produtor(produtor)[2][0]
#     soma_und += somar_produtor(produtor)[3][0]
#
# print("total de kg = " + str(soma_kg) + " total de litros = " + str(soma_L) + " total de molhos = " + str(soma_molho) + " total de unidades = " + str(soma_und))
#
#
# def fazer_frase(soma):
#     for parte in soma:
#         if parte[0] == 0:
#             soma.remove(parte)
#     return soma
#     # return "Movimentamos " + str()





#################################### Testes

#teste do uniformizador
# while linha < get_Tamanho(Planilha_Totais):
#     print(uniformizar_unidade(linha))
#     linha+=1




#################################### Lixo


# Total_por_Produtor = xlwt.Workbook()
# sheets = []
# for produtor in produtores:
#     Total_por_Produtor.add_sheet(produtor)
# Total_por_Produtor.save("Total Por Produtor.xlsx")

# for produtor in produtores:
#     print(produtor)
    # print("Movimentamos " )
#


#
# linha = 0
# while Planilha_Totais.iloc[linha][0] != "fim":
#     print(uniformizar_unidade(linha))
#     linha += 1



# Totais = xlwt.Workbook()
# sheet = Totais.add_sheet('test')
# for i in range(0, len(produtos)):
#     sheet.write(i, 0, produtos[i].nome)
#     sheet.write(i, 1, produtos[i].Und)
#     sheet.write(i, 2, produtos[i].preco_compra)
#     sheet.write(i, 3, produtos[i].preco_venda)
#     sheet.write(i, 4, sum(produtos[i].vendas))
#     sheet.write(i, 5, produtos[i].produtor)
# Totais.save('Totais.xlsx')


# for
# sheet = Totais.add_sheet('test')


# def print_produtor(produtor):
#     linha = 0
#     linhas_do_produtor = []
#     if Planilha_Totais.iloc[linha][5] == produtor:
#         linhas_do_produtor.append(linha)


# for produto in produtos:
#     print([produto.nome, produto.Und, produto.produtor])

# tentativas = []
# tentativas.append(Produto("a", "a", "a", "a", "a", "a"))
# print(tentativas[0].nome)

# print(lista.index)
# i = 0
# while lista.at()
# df1 = file.parse("Sheet1")
#
# df1 = pd.read_excel()
# for i in range(0, 30):
#     print(df1.at[i, "Unidade"])

# def check_produto(produto):
#     if type(produto) == type("a"):
#         for prod in produtos:
#             if produto == prod.nome:
#                 return True
#     else:
#         for prod in produtos:
#             if produto.nome == prod.nome:
#                 return True
#         return False

#
# def get_Tamanho(Planilha):
#     i = 0
#     while "Geral" not in Planilha.iloc[i][0]:
#         i += 1
#     return i





# def uniformizar_unidades():
#     linha = 0
#     unidades = []
#     while Planilha_Totais.iloc[linha][0] != "fim":
#         unidade = Planilha_Totais.iloc[linha]["Unidade"].replace(" ", "")
#         unidade = unidade.replace("1litro", "1000ml")
#         unidade = unidade.replace("1Litro", "1000ml")
#         unidade = unidade.replace("1kg", "1000g")
#         unidade = unidade.replace("kg", "1000g")
#         unidade = unidade.replace("mls", "ml")
#         unidade = unidade.replace("Dz", "dz")
#         unidade = unidade.replace("Unidade", "und")
#         if unidade not in unidades:
#             unidades.append(unidade)
#         linha += 1
#     return unidades
#