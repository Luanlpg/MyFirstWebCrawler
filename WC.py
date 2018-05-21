import urllib.request
cont = 0
texto = ''
listasrh = ['http://acheivagas.blogspot.com.br/p/e-mail-lista-rh.html?m=1','https://www.scribd.com/document/160245411/Lista-de-Emails-Do-RH-Das-Grandes-Empresas-No-Brasil','http://valeempregar.com.br/lista-de-emails-rh/','http://www.empregosadmitindo.com.br/2015/04/lista-de-emails-do-rh-das-grandes.html?m=1']#lista de urls com emails de rh
while cont <=3:
    listadavez = listasrh[cont]#pega uma url da lista

    content = urllib.request.urlopen(listadavez).read()#acessa a url e lê a pagina html
    content = str(content)#tranforma o html em str
    while ('<' in content):
        content = content.replace('<', ' ')

    while ('>' in content):
        content = content.replace('>', ' ')
        
    while ('/' in content):
        content = content.replace('/', ' ')

    while ('\n' in content):
        content = content.replace('\n', ' ')

    while ('\n\n' in content):
        content = content.replace('\n\n', ' ')

    while (':' in content):
        content = content.replace(':', ' ')

    while ('"' in content):
        content = content.replace('"', ' ')
        
    texto = content.split(' ')
    cont +=1
    
    for i in range (1,x):
        while '@' in texto[i] and '.' in texto[i]:
            print (texto[i])
            i+=1
def remove_repetidos(list = texto):
    l = []
    for i in texto:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

lista = remove_repetidos(lista)
print (lista)        
           
