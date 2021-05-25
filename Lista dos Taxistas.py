import pyautogui as pyg
import time
import os
import numpy as np
import pandas as pd


#os.remove(pathtofile)

path = "/home/vni/Documents/"



# file1 = open("Sistema de Pedidos da Cesta Camponesa.html", "r")








def abrir_relatorio():
    pyg.press("tab", presses = 2)
    time.sleep(2)
    pyg.hotkey("ctrl", "enter")
    time.sleep(2)
    pyg.hotkey("ctrl", "pagedown")
    time.sleep(2)
    pyg.hotkey("ctrl", "s")
    time.sleep(2)
    pyg.press("enter")
    time.sleep(2)
    pyg.hotkey("ctrl", "w")

def abrir_lista_vendas(nome):
    pyg.press("tab", presses = 3)
    time.sleep(2)
    pyg.hotkey("ctrl", "enter")
    time.sleep(2)
    pyg.hotkey("ctrl", "pagedown")
    time.sleep(30)
    pyg.press("tab", presses = 3)
    time.sleep(2)
    pyg.press("tab", presses = 3)
    time.sleep(2)
    pyg.press("tab")
    time.sleep(2)
    pyg.press("enter")
    time.sleep(1)
    pyg.hotkey("ctrl", "c")
    time.sleep(1)
    pyg.hotkey("alt", "tab")
    time.sleep(5)
    pyg.hotkey("ctrl", "n")
    time.sleep(3)
    pyg.hotkey("ctrl", "v")
    time.sleep(2)
    pyg.press("enter")
    time.sleep(1)
    salvar_cestas(nome)
    pyg.hotkey("alt", "f4")
    time.sleep(4)
    pyg.hotkey("alt", "tab")
    time.sleep(3)
    pyg.hotkey("ctrl", "w")
    time.sleep(5)



    # pyg.hotkey("ctrl", "s")
    # time.sleep(2)
    # pyg.press("enter")
    # time.sleep(2)
    # pyg.hotkey("ctrl", "w")


def dividir(lista, str):
    corte = str
    if "Diferen" in corte:
        lista.append(corte[:corte.index("Diferen")+30])
        corte = corte[corte.index("Diferen")+30:]
        dividir(lista, corte)
    else:
        pass
    return lista



def get_cestante(str):
    if "Tel." not in str:
        return ""
    corte = str[str.index("style"):]
    corte = corte[corte.index(">")+1:]
    nome = corte[:corte.index("Tel.") - 2]
    # nome = nome.replace(" ", "")
    corte = corte[corte.index("Tel.")+5:]
    tel = corte[:corte.index("End.")- 2]
    # tel = tel.replace(" ", "")
    corte = corte[corte.index("End.")+6:]
    end = corte[:corte.index("</th")]
    corte = corte[corte.index("Diferen")+14:]
    total = corte[:corte.index("</fo")]
    return [nome.replace("\n", ""), tel.replace("\n", ""), end.replace("\n", ""), total.replace("\n", "")]



lista_final = []


def addto_listafinal():
    time.sleep(5)
    abrir_relatorio()
    time.sleep(5)

    file0 = open(path+"Sistema de Pedidos da Cesta Camponesa.html", "r")
    file =file0.read()
    file = file[file.index("Responsável"):]

    nucleo = file[file.index("Núcleo")+7:]
    nucleo = nucleo[:nucleo.index("-")]

    file = file[file.index("Pedido"):]

    lista_de_cestantes = dividir([], file)
    if len(lista_de_cestantes) > 0:
        lista_de_cestantes.pop(-1)
        for str in lista_de_cestantes:
            lista_final.append([nucleo] + get_cestante(str))

    os.remove(path+"Sistema de Pedidos da Cesta Camponesa.html")


##deu certo
# def seila(i):
#     print(i)
#     if i>0:
#         print(i)
#         i-=1
#         seila(i)
# seila(3)


def rotation(n):
    i=0
    while i < n:
        pyg.write("xdytew")
        i+=1

def gerar_planilha(n):
    i=0
    while i<n:
        addto_listafinal()
        i+=1
    df = pd.DataFrame(np.array(lista_final), columns=["Núcleo", "Nome", "Telefone", "Endereço", "Total"])
    df.to_excel(dia + " Lista de informacoes de cestantes.xlsx", sheet_name="1")

dia = "Rio 09-01-2021"
time.sleep(3)
gerar_planilha(1)


def salvar_cestas(nome):
    pyg.hotkey("ctrl", "s")
    time.sleep(2)
    pyg.write(nome)
    time.sleep(4)
    pyg.press("enter")
    time.sleep(2)



# abrir_lista_vendas('abc.xlsx')
# salvar_cestas('abc.xlsx')




# predatas2 = ['27/06/2020 1', '27/06/2020 2',
#          '24/06/2020 1', '24/06/2020 2', '20/06/2020 1', '20/06/2020 2', '17/06/2020 1', '17/06/2020 2', '13/06/2020 1', '13/06/2020 2',
#          '10/06/2020 1', '10/06/2020 2', '06/06/2020 1', '06/06/2020 2', '03/06/2020 1', '03/06/2020 2', '30/05/2020 1', '30/05/2020 2',
#          '27/05/2020 1', '27/05/2020 2', '23/05/2020 1', '23/05/2020 2', '20/05/2020 1', '20/05/2020 2', '16/05/2020 1', '16/05/2020 2',
#          '13/05/2020 1', '13/05/2020 2', '09/05/2020 1', '09/05/2020 2', '06/05/2020 1', '06/05/2020 2', '02/05/2020 1', '02/05/2020 2',
#          '29/04/2020 1', '29/04/2020 2', '25/04/2020 1', '25/04/2020 2', '22/04/2020 1', '18/04/2020 2', '18/04/2020 1', '15/04/2020 2',
#          '11/04/2020 1', '08/04/2020 2', '08/04/2020 1', '04/04/2020 2', '01/04/2020 1', '28/03/2020 2', '25/03/2020 1', '21/03/2020 2']
#
# feito = ['Entrega 27-06-2020 1.xlsx', 'Entrega 27-06-2020 2.xlsx', 'Entrega 24-06-2020 1.xlsx', 'Entrega 24-06-2020 2.xlsx',
#          'Entrega 20-06-2020 1.xlsx', 'Entrega 20-06-2020 2.xlsx', 'Entrega 17-06-2020 1.xlsx', 'Entrega 17-06-2020 2.xlsx',
#          'Entrega 13-06-2020 1.xlsx', 'Entrega 13-06-2020 2.xlsx', 'Entrega 10-06-2020 1.xlsx', 'Entrega 10-06-2020 2.xlsx',
#          'Entrega 06-06-2020 1.xlsx', 'Entrega 06-06-2020 2.xlsx', 'Entrega 03-06-2020 1.xlsx', 'Entrega 03-06-2020 2.xlsx'
#           'Entrega 18-04-2020 2.xlsx',
#          'Entrega 18-04-2020 1.xlsx', 'Entrega 15-04-2020.xlsx', 'Entrega 11-04-2020.xlsx', 'Entrega 08-04-2020 2.xlsx',
#          'Entrega 08-04-2020 1.xlsx', 'Entrega 04-04-2020.xlsx', 'Entrega 01-04-2020.xlsx', 'Entrega 28-03-2020.xlsx',
#          'Entrega 25-03-2020.xlsx', 'Entrega 21-03-2020.xlsx']
# fazer = []
# falta = []


# datas = ['Entrega 27/06/2020 1.xlsx', 'Entrega 27/06/2020 2.xlsx', 'Entrega 24/06/2020 1.xlsx', 'Entrega 24/06/2020 2.xlsx',
#          'Entrega 20/06/2020 1.xlsx', 'Entrega 20/06/2020 2.xlsx', 'Entrega 17/06/2020 1.xlsx', 'Entrega 17/06/2020 2.xlsx',
#          'Entrega 13/06/2020 1.xlsx', 'Entrega 13/06/2020 2.xlsx', 'Entrega 10/06/2020 1.xlsx', 'Entrega 10/06/2020 2.xlsx',
#          'Entrega 06/06/2020 1.xlsx', 'Entrega 06/06/2020 2.xlsx', 'Entrega 03/06/2020 1.xlsx', 'Entrega 03/06/2020 2.xlsx',
#          'Entrega 30/05/2020 1.xlsx', 'Entrega 30/05/2020 2.xlsx', 'Entrega 27/05/2020 1.xlsx', 'Entrega 27/05/2020 2.xlsx',
#          'Entrega 23/05/2020 1.xlsx', 'Entrega 23/05/2020 2.xlsx', 'Entrega 20/05/2020 1.xlsx', 'Entrega 20/05/2020 2.xlsx',
#          'Entrega 16/05/2020 1.xlsx', 'Entrega 16/05/2020 2.xlsx', 'Entrega 13/05/2020 1.xlsx', 'Entrega 13/05/2020 2.xlsx',
#          'Entrega 09/05/2020 1.xlsx', 'Entrega 09/05/2020 2.xlsx', 'Entrega 06/05/2020 1.xlsx', 'Entrega 06/05/2020 2.xlsx',
#          'Entrega 02/05/2020 1.xlsx', 'Entrega 02/05/2020 2.xlsx', 'Entrega 29/04/2020 1.xlsx', 'Entrega 29/04/2020 2.xlsx',
#          'Entrega 25/04/2020 1.xlsx', 'Entrega 25/04/2020 2.xlsx', 'Entrega 22/04/2020 1.xlsx', 'Entrega 18/04/2020 2.xlsx',
#          'Entrega 18/04/2020 1.xlsx', 'Entrega 15/04/2020 2.xlsx', 'Entrega 11/04/2020 1.xlsx', 'Entrega 08/04/2020 2.xlsx',
#          'Entrega 08/04/2020 1.xlsx', 'Entrega 04/04/2020 2.xlsx', 'Entrega 01/04/2020 1.xlsx', 'Entrega 28/03/2020 2.xlsx',
#          'Entrega 25/03/2020 1.xlsx', 'Entrega 21/03/2020 2.xlsx']
# marco = [ 'Entrega 28/03/2020.xlsx', 'Entrega 25/03/2020.xlsx', 'Entrega 21/03/2020.xlsx']
# abril = ['Entrega 29/04/2020 1.xlsx', 'Entrega 29/04/2020 2.xlsx',
#          'Entrega 25/04/2020 1.xlsx', 'Entrega 25/04/2020 2.xlsx', 'Entrega 22/04/2020.xlsx', 'Entrega 18/04/2020 2.xlsx',
#          'Entrega 18/04/2020 1.xlsx', 'Entrega 15/04/2020.xlsx', 'Entrega 11/04/2020.xlsx', 'Entrega 08/04/2020 2.xlsx',
#          'Entrega 08/04/2020 1.xlsx', 'Entrega 04/04/2020.xlsx', 'Entrega 01/04/2020.xlsx']
# maio = ['Entrega 30/05/2020 1.xlsx', 'Entrega 30/05/2020 2.xlsx', 'Entrega 27/05/2020 1.xlsx', 'Entrega 27/05/2020 2.xlsx',
#          'Entrega 23/05/2020 1.xlsx', 'Entrega 23/05/2020 2.xlsx', 'Entrega 20/05/2020 1.xlsx', 'Entrega 20/05/2020 2.xlsx',
#          'Entrega 16/05/2020 1.xlsx', 'Entrega 16/05/2020 2.xlsx', 'Entrega 13/05/2020 1.xlsx', 'Entrega 13/05/2020 2.xlsx',
#          'Entrega 09/05/2020 1.xlsx', 'Entrega 09/05/2020 2.xlsx', 'Entrega 06/05/2020 1.xlsx', 'Entrega 06/05/2020 2.xlsx',
#          'Entrega 02/05/2020 1.xlsx', 'Entrega 02/05/2020 2.xlsx']
# junho = ['Entrega 27/06/2020 1.xlsx', 'Entrega 27/06/2020 2.xlsx', 'Entrega 24/06/2020 1.xlsx', 'Entrega 24/06/2020 2.xlsx',
#          'Entrega 20/06/2020 1.xlsx', 'Entrega 20/06/2020 2.xlsx', 'Entrega 17/06/2020 1.xlsx', 'Entrega 17/06/2020 2.xlsx',
#          'Entrega 13/06/2020 1.xlsx', 'Entrega 13/06/2020 2.xlsx', 'Entrega 10/06/2020 1.xlsx', 'Entrega 10/06/2020 2.xlsx',
#          'Entrega 06/06/2020 1.xlsx', 'Entrega 06/06/2020 2.xlsx', 'Entrega 03/06/2020 1.xlsx', 'Entrega 03/06/2020 2.xlsx']

# time.sleep(12)
# for dia in fazer:
#     abrir_lista_vendas(dia)

# datas=[]
# for dia in predatas2:
#     datas.append("Entrega " + dia + ".xlsx")
# print(datas)