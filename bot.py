import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#srh
UrlZeceLaInfo = "https://www.zecelainfo.com/3627-fab/"

def LogIn(driver, username, pasword) :
    driver.find_element_by_id("user").send_keys(username)
    driver.find_element_by_id("parola").send_keys(pasword)
    driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(3)

def isproblem(driver) :
    if driver.title == "www.pbinfo.ro":
        return 0
    else :
        return 1

def GetPbId(driver) :
    CurString = str(driverChrome.title)
    NumberOfProblem = 0
    for i in range (0, len(CurString)) :
        if CurString[i].isdigit() == False :
            break
        else :
            NumberOfProblem = NumberOfProblem * 10 + int(CurString[i])
    return NumberOfProblem


    # Firefox - pbinfo 500_IQ
    # Chrome  - zecelainfo.com

driverFirefox = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.28.0-win64.zip\geckodriver.exe")
driverFirefox.get("https://www.pbinfo.ro/")
LogIn(driverFirefox, "IQ", "IQ")

driverChrome = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.28.0-win64.zip\geckodriver.exe")
driverChrome.get(UrlZeceLaInfo)

for NrOfProblem in range (1, 4001) :

    CurrUrl = driverChrome.current_url

    if "vignette" in CurrUrl: #pt reclama
        CurrUrl = CurrUrl[:-16]
        driverChrome.get(CurrUrl)


    PbId = GetPbId(driverChrome) #am aflat id pb

    UrlSolOf = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id=" + str(PbId)
    driverFirefox.get(UrlSolOf) #intru cont 300 iq

    if "numai de utilizatorii" in driverFirefox.page_source: #daca nu am pb
        copiedText = driverChrome.find_element_by_css_selector(".wp-block-preformatted").text
        driverFirefox.get("https://www.pbinfo.ro/probleme/" + str(PbId))
        message = driverFirefox.find_element_by_css_selector(".CodeMirror > div:nth-child(1) > textarea:nth-child(1)")
        message.send_keys(copiedText)
        driverFirefox.find_element_by_xpath("//*[@id=\"btn-submit\"]").click()
        time.sleep(13)
        #f = open("out1.txt")
        #r = f.read()

        #f = open('out1.txt', 'r+')
        #f.truncate(0)
        #f.close()
        #writeProblem(driverFirefox)


    driverChrome.find_element_by_css_selector(".nav-arrow").click()

    time.sleep(1)
