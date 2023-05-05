from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def storeData(dataType, value):
    if(dataType == 'byKeyWord'):
        file = open('keywords.txt', 'a')
        file.write(str(value) + ';')
        file.close()
    elif(dataType == 'byMessage'):
        file = open('message.txt', 'a')
        file.write(str(value) + ';')
        file.close()
    elif(dataType == 'byEmail'):
        file = open('emails.txt', 'a')
        file.write(str(value) + ';')
        file.close()
    elif(dataType == 'bySubject'):
        file = open('subject.txt', 'a')
        file.write(str(value) + ';')
        file.close()

def searchByKeyWord(keyWord, driver):
    
    driver.get("https://registro.br/tecnologia/ferramentas/whois")

    search_bar = driver.find_element(By.NAME, "whois-field")
    search_bar.clear()

    search_bar.send_keys(keyWord)
    search_bar.send_keys(Keys.ENTER)
    

    time.sleep(4)
    
    emails = driver.find_element(By.CLASS_NAME, "cell-emails")
    email = emails.text

    storeData('byEmail', email)
    return (email)
    #site = "https://" + keyWord
    # key Word = dominio do site

def sendMail(driver):
    user = "scrapingemailucs@gmail.com"
    password = "qwe321##"

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
    to_field.send_keys('diogograebin@gmail.com')#email

    subject_field = driver.find_element(By.NAME, "subjectbox")
    subject_field.send_keys('teste assunto') #subject

    text_field = driver.find_element(By.ID, ":9c")
    text_field.send_keys("Testando encvio do email") #message

    btn_send = driver.find_element(By.CLASS_NAME, "dC")
    btn_send.click()

   


print("Scraping mail")
print("Para prosseguir, digite uma palavra chave")

keyWord = input()
storeData('byKeyWord', keyWord)

print("Digite o assunto do email")
subject = input()
storeData('bySubject', subject)


print("Digite a mensagem que deseja encaminhar via email")
message = input()
storeData('byMessage', message)



driver = webdriver.Chrome()
sendMail(driver)

#email = searchByKeyWord(keyWord, driver)


#driver.close()
