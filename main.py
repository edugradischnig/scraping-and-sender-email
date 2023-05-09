"""
Sugerimos que, antes de iniciar a execução, os seguintes fatores sejam levados em consideração:
- Software foi feito para ser executado em ambiente configurado conforme especificações
- Credencial do gmail remetente foi disponibilizada para testes
- Recomendável antes de executar a primeira vez, efetuar o login no gmail disponibilizado
abaixo, a fim de pular pop us de segurança que podem aparecer no primeiro login no dispositivo.
scrapingemailucs@gmail.com
qwe321##
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def storeData(dataType, value):
    file = open(dataType + '.txt', 'a')
    file.write(str(value) + ';')
    file.close()

def searchByKeyWord(keyWord, driver):
    driver.get("https://registro.br/tecnologia/ferramentas/whois")
    time.sleep(1)

    try:
        search_bar = driver.find_element(By.NAME, "whois-field")
        search_bar.clear()

        search_bar.send_keys(keyWord)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(4)
        
        emails = driver.find_element(By.CLASS_NAME, "cell-emails")
        email = emails.text

        if(email):
            storeData('byEmail', email)
            return (email)
        else:
            return ""
        
    except:
        print("Não foi possível encontrar email responsável no Registro BR!")

def sendMail(driver, destinatary, subject, message):
    user = "scrapingemailucs@gmail.com" # user de exemplo criado
    password = "qwe321##" # user de exemplo criado

    driver.get("https://mail.google.com")
    user_field = driver.find_element(By.NAME, "identifier")

    user_field.clear()
    user_field.send_keys(user)

    btn_next = driver.find_element(By.ID, "identifierNext")
    btn_next.click()

    time.sleep(5)
    password_field = driver.find_element(By.NAME, "Passwd")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    time.sleep(5)
    btn_compose = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div")
    btn_compose.click()

    time.sleep(2)
    
    to_field = driver.find_element(By.ID, ":c0")
    to_field.send_keys(destinatary)#email desinatário

    subject_field = driver.find_element(By.NAME, "subjectbox")
    subject_field.send_keys(subject) #subject

    text_field = driver.find_element(By.ID, ":9c")
    text_field.send_keys(message) #message

    btn_send = driver.find_element(By.CLASS_NAME, "dC")
    btn_send.click()


print("Scraping mail")
print("Para prosseguir, digite um domínio. Ex.:(ucsvirtual.ucs.br)")

keyWord = input()
storeData('byKeyWord', keyWord)

print("Digite o assunto do email")
subject = input()
storeData('bySubject', subject)


print("Digite a mensagem que deseja encaminhar via email")
message = input()
storeData('byMessage', message)


#pathChromeDriver = "C:/Users/Eduardo/Documents"
driver = webdriver.Chrome()

destinatary = searchByKeyWord(keyWord, driver)

sendMail(driver, destinatary, subject, message)


