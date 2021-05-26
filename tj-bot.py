from selenium import webdriver
from time import sleep
import sys
import os
import argparse

class TJbot:
    def __init__(self,fpg, driver_path):
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 1,
                                    'plugins': 2, 'popups': 2, 'geolocation': 2,
                                    'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                    'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                    'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                    'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                    'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                    'durable_storage': 2}}
        options.add_experimental_option('prefs', prefs)
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        self.driver=webdriver.Chrome(options=options, executable_path=driver_path)
        self.driver.maximize_window()
        while fpg > 0:
            try:
                self.driver.get("https://tjournal.ru/special/egypt-6578706c6f7265206974206865726520225c6422")
                sleep(5)
                self.driver.find_element_by_xpath("//*[@id=\"page_wrapper\"]/div/div[4]/div[2]/div[1]/div[4]/div").click()
                sleep(1.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[2]/div/pre[12]").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[9]/div[2]/div[1]/div[7]/input").send_keys(69182)
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[9]/div[2]/div[1]/div[7]/div").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[9]/div[2]/div[2]/div").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[2]/div/pre[13]").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[7]/div[2]/div[1]/div[5]/input").send_keys("pearl")
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[7]/div[2]/div[1]/div[5]/div").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[7]/div[2]/div[2]/div").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[2]/div/pre[1]").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[8]/div[2]/div[1]/div[5]/input").send_keys(30181)
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[8]/div[2]/div[1]/div[5]/div").click()
                sleep(0.5)
                self.driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[4]/div/div[8]/div[2]/div[2]/div").click()
                sleep(0.5)
                fpg-=1
                print ("TJ bot has to perform {} more entries".format (fpg) )
            except Exception:
                print ("TJ bot run into an error {}".format (Exception) )
        self.driver.close();
        
def validate_file(f):
    if not os.path.exists(f):
        raise argparse.ArgumentTypeError("{0} does not exist".format(f))
    return f

def argParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--amount', default=100, type=int)
    parser.add_argument ('-d', '--driver', type=validate_file, default="./chromedriver")
    return parser
    
if __name__ == "__main__":
    parser = argParser()
    namespace = parser.parse_args(sys.argv[1:])
    fpg = namespace.amount
    path = namespace.driver
    print ("TJ bot will solve task {} times".format (fpg) )
    TJbot(fpg, path)
