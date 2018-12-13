from appium import webdriver


def get_appdriver():
    URL = 'http://10.8.1.79:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Redmi',
        'app': 'C:\\Projects\\com.ownmettro.androidecommerce.apk',
        'apkPackage': 'com.ownmettro.androidecommerce',
        'autoGrantPermissions': 'true'
    }
    driver = webdriver.Remote(URL, desired_caps)
    return driver
