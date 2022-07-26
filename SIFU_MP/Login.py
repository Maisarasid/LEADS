import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    #button_mp_xpath = "/html/body/section[1]/div/div[1]/div[1]/div[1]/div[1]/a"
    textbox_username_id = "username"
    textbox_password_id = "password"
    #button_login_xpath = "/html/body/div/div[2]/div/div/div/div/form/div[4]/input[2]"

    def __init__(self, driver):
        self.driver = driver

#Click button Market Profiling
    def clickMP(self):
        mp = self.driver.find_element(By.XPATH, "/html/body/section[1]/div/div[1]/div[1]/div[1]/div[1]/a")
        mp.click()
        time.sleep(2)

#set the username
    def setUsername(self, user_id):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(user_id)
        time.sleep(2)

#set the Password
    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        time.sleep(2)

#click login button
    def clickLogin(self):
        login = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/form/div[4]/input[2]")
        login.click()
        time.sleep(2)

#click segment
    def choose_Segment(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[1]/nb-select/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

#click product
    def choose_Product(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[2]/nb-select/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)
        #select = Select(self.driver.find_element(By.XPATH, "//button[contains(.,'ALL')]"))
        #select.select_by_visible_text("CONSUMER")

    def choose_Region(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[3]/nb-select/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def choose_State(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[4]/nb-select/button").click()
        time.sleep(2)

    def State_KL(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def choose_BusZone(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[5]/nb-select/button").click()
        time.sleep(2)

    def Busi_Bangsar(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Busi_Anggerik(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Busi_JalanTuankuAbdulRahman(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Busi_Maluri(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[5]").click()
        time.sleep(2)

    def choose_MarkCent(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[2]/div/div[6]/nb-select/button").click()
        time.sleep(2)

    def Mark_Bangsar(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_TunRazak(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_BktAnggerik(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_TAR(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Bintang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Maluri(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def State_MSC(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Busi_Cyberjaya(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Busi_Serdang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Busi_Kinrara(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Busi_Puchong(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[5]").click()
        time.sleep(2)

    def Mark_Cyberjaya(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Serdang1(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Serdang2(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_BJL(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Kinrara(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_PCG(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_USJ(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def State_PetalingJaya(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Busi_Kajang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Busi_LapanganTerbangSubang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Busi_TamanPetaling(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Busi_TunDrIsmail(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[5]").click()
        time.sleep(2)

    def Mark_Bangi(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_Kajang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_Semenyih(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Mark_LapanganTerbangSubang(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_SubangJaya(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_KualaPauh(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_SgBesi(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_TamanPetaling(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Mark_KelanaJaya(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[2]").click()
        time.sleep(2)

    def Mark_PJCentral(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[3]").click()
        time.sleep(2)

    def Mark_SgWay(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[4]").click()
        time.sleep(2)

    def Mark_TunDrIsmail(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[5]").click()
        time.sleep(2)

    def State_Selangor(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[2]/div/div/nb-option-list/ul/nb-option[5]").click()
        time.sleep(2)


    def click_submitFilter(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[3]/button[1]").click()
        time.sleep(3)

    def click_resetFilter(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/nav/div/div/form/div[3]/button[2]").click()
        time.sleep(3)