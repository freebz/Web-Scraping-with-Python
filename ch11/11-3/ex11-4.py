# 11.3 CAPTCHA 읽기와 테서랙트 훈련

# $ tesseract captchaExample.tiff output

# 92353


# 11.3.1 테서랙트 훈련

def main(self):
    languageName = "eng"
    fontName = "captchaFont"
    directory = "<path to images>"
def runAll(self):
    self.createFontFile()
    self.cleanImages()
    self.renameFiles()
    self.extractUnicode()
    self.runShapeClustering()
    self.runMfTraining()
    self.runCnTraining()
    self.createTessData()
    
