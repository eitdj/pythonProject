class CaptureScreen:
    @staticmethod
    def capture_screenshot(driver):
        return driver.save_screenshot("C:\\Users\\EIT\\PycharmProjects\\pythonProject\\screenshots\\screenshot.png")