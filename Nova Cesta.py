import pandas as pd

bairros=["Botafogo", "Catete/Laranjeira", "Copacabana/Leme", "Estácio", "Flamengo", "Glória", "Grajaú",
         "Humaitá", "Lapa/Bairro de Fátima", "Leblon/Ipanema/Lagoa", "Méier 1", "Méier 2", "Paquetá", "Santa Tereza",
         "Tijuca 1", "Tijuca 2", "Tijuca 3", "Vila Isabel", "Vila Valqueire", "Zona Norte"]



def find_Format(column):
    if "R$" in file.columns[column]:
        price_part=file.columns[column][file.columns[column].find("R$")+2:]
        if "/" in price_part:
            return 1
        else:
            return 2
    else:
        return 3

def getPrice(column):
    n=find_Format(column)
    try:
        if n == 1:
            price_part=file.columns[column][file.columns[column].find("R$")+2:]
            b=price_part.find("/")
            return float(price_part[:b].replace(",", "."))
            # return float(file.columns[column][a+3:b].replace(",", "."))
        elif n==2:
            a=file.columns[column].find("R$")
            return float(file.columns[column][a + 2:-1].replace(",", "."))
            # return float(file.columns[column][a+3:-1].replace(",", "."))
        else:
            return 0
    except ValueError:
        print("oops, column " + str(column))

def get_pedido(row):
    data1=file.iloc[row]
    col=6
    rows=[]
    while col < len(file.columns):
        if data1[col]>0:
            # cols.append(col)
            rows.append([file.columns[col], getPrice(col), data1[col], data1[col]*getPrice(col)])
        col+=1
    return rows

def sum_total3(rows):
    sum=0
    for row in rows:
        sum+=row[-1]
    return sum

def get_rows(bairro):
    rows=[]
    row=0
    # print(bairro==file.iloc[row][1])
    while row<len(file):
        if file.iloc[row][1]==bairro:
            rows.append(row)
        row+=1
    return rows

def bairro_list(bairro):
    bairro_list=[]
    rows=get_rows(bairro)
    for row in rows:
        bairro_list.append(get_pedido(row))
    return bairro_list

def lista_taxistas(file):
    file2 = file.sort_values(by=['NÚCLEO'])
    file3 = file2[['NÚCLEO','NOME COMPLETO', "ENDEREÇO", "Endereço de e-mail", "TELEFONE"]]
    file3.to_excel("lista taxistas.xlsx")
    return file3

def get_infocestante(row):
    info=[]
    for col in [4,3,2,5]:
        info.append(file.iloc[row][col])
    return info

def make_pedidoscestante(row):
    info=get_infocestante(row)
    pedidos=get_pedido(row)
    return [info,pedidos]

def make_lista(row):
    lista1=[get_infocestante(row)]
    for pedido in get_pedido(row):
        lista1.append(pedido)
    total = 0
    for row1 in range(1, len(lista1)):
        total+=lista1[row1][3]
    # print(total)
    lista1.append(["Total", "", "", total])
    lista1.append(["", "", "", "", "", ""])
    return lista1

def make_final(rows):
    listafinal=[]
    for row in rows:
        listafinal+=make_lista(row)
    df=pd.DataFrame(listafinal)
    df.to_excel("Lista de Pedidos " + dia + ".xlsx")
    return df

# listanums=[]
# for num in range(11, len(file)):
#     listanums.append(num)
# print(listanums)

# make_final(listanums)

# lista_taxistas(file)

def place_rs(file):
    file=file.rename(columns={"Doação MPA":"Doação MPA R$1,00"})
    return file

dia="16_01"
filename="Cesta Camponesa "+ dia + " (respostas).xlsx"
path = "/home/vni/Labora/Trabalho/Projetos/Coding - Raizes/"
file = pd.read_excel(path + filename).rename(columns={"Doação MPA":"Doação MPA R$1,00"})


# print(file.columns[6])
# print(place_rs(file).columns[6])

rows = [i for i in range(0, len(file))]
rowstest=rows[0:30]
teste1=make_final(rowstest)






## Teste MAKE DF ENTRY
# print(make_lista(15))
# print(make_lista(16))
# print(make_lista(17))
# print(make_final([15,16,17]))


# print(make_df(15))
# print(make_df(16))

## TESTE MAKE PEDIDO
# for row in range (20, 90):
#     print(row)
#     print(make_pedidoscestante(row)[0])

## TESTE GET PEDIDO
# for row in range(4,20):
    # print(row)
#     for thing in get_pedido(row):
#         print(thing)
#     print(get_infocestante(row))



# lista_taxistas(file)
# filea=lista_taxistas(file)
# print(filea)

# for row in range(len(file2)):
#     print(file2.iloc[row][1])

## TESTE BAIRRO LIST
# bairro="Lapa/Bairro de Fátima"
# lista2=bairro_list(bairro)
# for thing in lista2:
#     for thing2 in thing:
#         print(thing2)


## TESTE GET BAIRROS ROWS
# bairro="Lapa/Bairro de Fátima"
# bairro2="Vila Isabel"
# print(get_rows(bairro))
# print(get_rows(bairro2))
# for i in range(0, 7):
#     print(file.iloc[i][1]==bairro)

## TESTE GET PURCHASE
# row=7
# for thing in get_pedido(row):
#     print(thing)
#
# print(sum_total3(get_pedido(row)))

# for thing in get_purchasedcols(row):
#     print(thing)
# print(sum_total2(row))

## TESTE TABELAR_PEDIDO
# row=6
# print(tabelar_pedido(row))


# print(file.columns[0])
# print(file.columns[1])
# print(file.columns[2])
# print(file.columns[3])
# print(file.columns[4])
# print(file.columns[5])


## TESTE SUM_TOTAL
# row=6
# col=0
# while col<20:
#     print(file.iloc[row][col], file.columns[col])
#     col+=1

# sum_total(row)



#TESTE LEITURA DE PREÇO DE PRODUTO
# for column in range(98, 102):
    # print(file.columns[column])
    # print(getPrice(column), file.columns[column])
    # print(find_Format(column))




###########################
#LIXO

# def tabelar_pedido(row):
#     data1=file.iloc[row]
#     col=6
#     ret=[]
#     while col<40:
#         if type(data1[col]) != type("a"):
#             if data1[col]>0:
#                 ret.append([data1[col], file.columns[col]])
#         col+=1
#     return ret


# def sum_total2(row):
#     sum = 0
#     # col = 6
#     cols = get_purchasedcols(row)
#     for col in cols:
#         data1=file.iloc[row]
#         if data1[col]>0:
#             print(getPrice(col), file.columns[col])
#             sum+=getPrice(col)*data1[col]
#     return sum
# def sum_total(row):
#     sum=0
#     col=6
#     while col < len(file.columns)-1:
#         data1=file.iloc[row][col]
#         if type(data1) != type("a"):
#             if data1 > 0:
#                 try:
#                     sum+=data1*getPrice(col)
#                     print(sum, data1, file.columns[col])
#                     col+=1
#                 except:
#                     print(sum, data1, file.columns[col])
#                     col+=1
#             col+=1
#     return sum


# def get_purchasedcols(row):
#     data1=file.iloc[row]
#     col=6
#     cols=[]
#     while col < len(file.columns):
#         if data1[col]>0:
#             # cols.append(col)
#             cols.append([col, file.columns[col], getPrice(col), data1[col], data1[col]*getPrice(col)])
#         col+=1
#     return cols