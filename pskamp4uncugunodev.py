"""Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

Test Caseler;

Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır."""




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class test_sauce_odev:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    

    def test_empty_login(self):
        """
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        """
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUsername=self.driver.find_element(By.ID,"user-name")
        #inputUsername.send_keys("")   bu satırı actions ta yaptığım için kapattım
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPassword=self.driver.find_element(By.ID,"password")
        #inputPassword.send_keys("")  bu satırı actions ta yaptığım için kapattım
        loginButton=self.driver.find_element(By.ID,"login-button")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(inputUsername,"")
        actions.send_keys_to_element(inputPassword,"")
        actions.perform()
        loginButton.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        testResult=errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU:{testResult}")
    def test_empty_password(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUsername=self.driver.find_element(By.ID,"user-name")
        #inputUsername.send_keys("1")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPassword=self.driver.find_element(By.ID,"password")
        #inputPassword.send_keys("")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(inputUsername,"1")
        actions.send_keys_to_element(inputPassword,"")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        # print(errorMessage)
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"TEST SONUCU:{testResult}")
    def test_locked_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUsername=self.driver.find_element(By.ID,"user-name")
        #inputUsername.send_keys("locked_out_user")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPassword=self.driver.find_element(By.ID,"password")
        #inputPassword.send_keys("secret_sauce")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(inputUsername,"locked_out_user")
        actions.send_keys_to_element(inputPassword,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMessage)
        testResult=errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU:{testResult}")
    def test_X_icon_clean(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUsername=self.driver.find_element(By.ID,"user-name")
        #inputUsername.send_keys("")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPassword=self.driver.find_element(By.ID,"password")
        #inputPassword.send_keys("")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(inputUsername,"")
        actions.send_keys_to_element(inputPassword,"")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        #errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        x_icon_username=self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg > path")
        try:
            x_icon_username.is_displayed()
            print("X İKONU ÇIKIYOR")
        except:
            print("x ikonu çıkmadı")
        
        x_icon_password=self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg > path")
        
        x_icon=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
        try:
            x_icon_username.is_displayed()
            x_icon_password.is_displayed()
            print("ikonlar duruyor")
        except:
            print("ikonlar tekrar gitti her şey yolunda")
        
        #print(x_icon_username.is_displayed())
        

        while True:
            continue
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        inputUsername=self.driver.find_element(By.ID,"user-name")
        #inputUsername.send_keys("standard_user")
        
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        inputPassword=self.driver.find_element(By.ID,"password")
        #inputPassword.send_keys("secret_sauce")
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(inputUsername,"standard_user")
        actions.send_keys_to_element(inputPassword,"secret_sauce")
        actions.perform()
        loginButton=self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        urunSayisi=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
       
        testResult=len(urunSayisi)==6
        print(f"TEST SONUCU:{testResult}")
        
        
        while True:
           
           continue


        

        
        


testclass=test_sauce_odev()
#testclass.test_empty_login()
#testclass.test_empty_password()
#testclass.test_locked_login()
#testclass.test_X_icon_clean()
testclass.test_valid_login()



