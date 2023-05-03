#from selenium import webdriver

#driver = webdriver.Chrome("Bibliotecas\Documentos")

#driver.get("https://google.com")


#driver.close()

def storeData(dataType, value):
    if(dataType == 'byKeyWord'):
        file = open('keywords.txt', 'a')
        file.write(str(value) + ';')
        file.close()
    elif(dataType == 'byMessage'):
        file = open('message.txt', 'a')
        file.write(str(value) + ';')
        file.close()

print("Scraping mail")
print("Para prosseguir, digite uma palavra chave")

keyWord = input()
storeData('byKeyWord', keyWord)

#busca de emails

print("Digite a mensagem que deseja encaminhar via email")
message = input()
storeData('byMessage', message)






