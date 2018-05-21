import urllib.request
cont = 0
texto = ''
listasrh = ['http://acheivagas.blogspot.com.br/p/e-mail-lista-rh.html?m=1','https://www.scribd.com/document/160245411/Lista-de-Emails-Do-RH-Das-Grandes-Empresas-No-Brasil','http://valeempregar.com.br/lista-de-emails-rh/','http://www.empregosadmitindo.com.br/2015/04/lista-de-emails-do-rh-das-grandes.html?m=1']#lista de urls com emails de rh
while cont <=3:
    listadavez = listasrh[cont]#pega uma url da lista

    content = urllib.request.urlopen(listadavez).read()#acessa a url e lê a pagina html
    content = str(content)#tranforma o html em str
    while ('<' in content): # laço para substituir caractere
        content = content.replace('<', ' ')

    while ('>' in content):# laço para substituir caractere
        content = content.replace('>', ' ')
        
    while ('/' in content):# laço para substituir caractere
        content = content.replace('/', ' ')

    while ('\n' in content):# laço para substituir caractere
        content = content.replace('\n', ' ')

    while ('\n\n' in content):# laço para substituir caractere
        content = content.replace('\n\n', ' ')

    while (':' in content):# laço para substituir caractere
        content = content.replace(':', ' ')

    while ('"' in content):# laço para substituir caractere
        content = content.replace('"', ' ')
        
    texto = content.split(' ')#cortando espaços e tranformando str em lista
    cont +=1
    
    x = len(texto)#contar elementos da lista
    for i in range (1,x):
        while '@' in texto[i] and '.' in texto[i]:#verificando se é um email
            print (texto[i])
            i+=1
