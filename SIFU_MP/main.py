import time
import unittest
from selenium import webdriver
from SIFU_MP.Login import LoginPage
from selenium.webdriver.common.by import By

class test_cases(unittest.TestCase):
    exec_path = "C:\\Users\\Maisara Rasid\\OneDrive - International Islamic University Malaysia\\DOCUMENTS\\ChromeDriver\\chromedriver.exe"
    base_URL = "https://lead-portal-sifu.apps.ocp.tmrnd.com.my/"
    user_id = "sifu001"
    password = "pass1234"

    @classmethod
#pass the service object driver & initiatives webdrive
#open url & maximize the window

    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= cls.exec_path)
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()
        time.sleep(2)

#call each function from the LoginPage class

    def test_cases(self):
        self.lp = LoginPage(self.driver)
        #self.lp.clickMP()
        self.lp.setUsername(self.user_id)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #self.lp.driver.refresh()
        self.lp.choose_Segment()
        self.lp.click_submitFilter()
        self.lp.choose_Product()
        self.lp.click_submitFilter()
        self.lp.choose_Region()
        self.lp.click_submitFilter()
        self.lp.choose_State()
        self.lp.State_KL()
        self.lp.click_submitFilter()
        #self.ls.driver.execute_script("window.history.go(-1)")

        #State: KL | Business Zone: Bangsar and MC: Bangsar
        self.lp.choose_BusZone()
        self.lp.Busi_Bangsar()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_Bangsar()
        self.lp.click_submitFilter()

        #State: KL | Business Zone: Bukit Anggerik | MC: Bandar Tun Razak
        self.lp.choose_BusZone()
        self.lp.Busi_Anggerik()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_TunRazak()
        self.lp.click_submitFilter()

        #State: KL | Business Zone: Bukit Anggerik | MC: Bukit Anggerik
        self.lp.choose_MarkCent()
        self.lp.Mark_BktAnggerik()
        self.lp.click_submitFilter()

        #State: KL | Business Zone: Jalan Tuanku Abdul Rahman | MC: TAR
        self.lp.choose_BusZone()
        self.lp.Busi_JalanTuankuAbdulRahman()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_TAR()
        self.lp.click_submitFilter()

        #State: KL | Business Zone: Maluri | MC: Bintang
        self.lp.choose_BusZone()
        self.lp.Busi_Maluri()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_Bintang()
        self.lp.click_submitFilter()

        #State: KL | Business Zone: Maluri | MC: Maluri
        self.lp.choose_MarkCent()
        self.lp.Mark_Maluri()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Cyberjaya | MC: Cyberjaya
        self.lp.choose_State()
        self.lp.State_MSC()
        self.lp.click_submitFilter()
        self.lp.choose_BusZone()
        self.lp.Busi_Cyberjaya()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_Cyberjaya()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Serdang | MC: Serdang 1
        self.lp.choose_BusZone()
        self.lp.Busi_Serdang()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_Serdang1()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Serdang | MC: Serdang 2
        self.lp.choose_MarkCent()
        self.lp.Mark_Serdang2()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Kinrara | MC: BJL
        self.lp.choose_BusZone()
        self.lp.Busi_Kinrara()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_BJL()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Kinrara | MC: Kinrara
        self.lp.choose_MarkCent()
        self.lp.Mark_Kinrara()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Puchong | MC: PCG
        self.lp.choose_BusZone()
        self.lp.Busi_Puchong()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_PCG()
        self.lp.click_submitFilter()

        #State: MSC | Business Zone: Puchong | MC: USJ
        self.lp.choose_MarkCent()
        self.lp.Mark_USJ()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Kajang | MC: Bangi
        self.lp.choose_State()
        self.lp.State_PetalingJaya()
        self.lp.click_submitFilter()
        self.lp.choose_BusZone()
        self.lp.Busi_Kajang()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_Bangi()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Kajang | MC: Kajang
        self.lp.choose_MarkCent()
        self.lp.Mark_Kajang()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Kajang | MC: Semenyih
        self.lp.choose_MarkCent()
        self.lp.Mark_Semenyih()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Lapangan Terbang Subang | MC: Lapangan Terbang Subang
        self.lp.choose_BusZone()
        self.lp.Busi_LapanganTerbangSubang()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_LapanganTerbangSubang()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Lapangan Terbang Subang | MC: Subang Jaya
        self.lp.choose_MarkCent()
        self.lp.Mark_LapanganTerbangSubang()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Taman Petaling | MC: Kuala Pauh
        self.lp.choose_BusZone()
        self.lp.Busi_TamanPetaling()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_KualaPauh()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Taman Petaling | MC: Sg Besi
        self.lp.choose_MarkCent()
        self.lp.Mark_SgBesi()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Taman Petaling | MC: Taman Petaling
        self.lp.choose_MarkCent()
        self.lp.Mark_TamanPetaling()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Tun Dr Ismail | MC: Kelana Jaya
        self.lp.choose_BusZone()
        self.lp.Busi_TunDrIsmail()
        self.lp.click_submitFilter()
        self.lp.choose_MarkCent()
        self.lp.Mark_KelanaJaya()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Tun Dr Ismail | MC: PJ Central
        self.lp.choose_MarkCent()
        self.lp.Mark_PJCentral()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Tun Dr Ismail | MC: Sg Way
        self.lp.choose_MarkCent()
        self.lp.Mark_SgWay()
        self.lp.click_submitFilter()

        #State: Petaling Jaya | Business Zone: Tun Dr Ismail | MC: Tun Dr Ismail
        self.lp.choose_MarkCent()
        self.lp.Mark_TunDrIsmail()
        self.lp.click_submitFilter()

        #Reset Filter
        self.lp.click_resetFilter()

