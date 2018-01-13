from tDataExtractor import TDataExtractor
import cv2



class Test_tDataExtractor:

    def test_image1(self):
        analysis = self.getAnalysis('tImages/t1.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'short'


    def test_image2(self):
        analysis = self.getAnalysis('tImages/t2.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image3(self):
        analysis = self.getAnalysis('tImages/t3.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'


    def test_image4(self):
        analysis = self.getAnalysis('tImages/t4.png')
        assert analysis['labelTrend'] == 'falling'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image5(self):
        analysis = self.getAnalysis('tImages/t5.png')
        assert analysis['labelTrend'] == 'rising'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image6(self):
        analysis = self.getAnalysis('tImages/t6.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image7(self):
        analysis = self.getAnalysis('tImages/t7.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image8(self):
        analysis = self.getAnalysis('tImages/t8.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image9(self):
        analysis = self.getAnalysis('tImages/t9.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image10(self):
        analysis = self.getAnalysis('tImages/t10.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image11(self):
        analysis = self.getAnalysis('tImages/t11.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image12(self):
        analysis = self.getAnalysis('tImages/t12.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'falling'
        assert analysis['crossingLength'] == 'normal'

    def test_image13(self):
        analysis = self.getAnalysis('tImages/t13.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image14(self):
        analysis = self.getAnalysis('tImages/t14.png')
        assert analysis['labelTrend'] == 'rising'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'normal'

    def test_image15(self):
        analysis = self.getAnalysis('tImages/t15.png')
        assert analysis['labelTrend'] == 'falling'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image16(self):
        analysis = self.getAnalysis('tImages/t16.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image17(self):
        analysis = self.getAnalysis('tImages/t17.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'constant'
        assert analysis['crossingLength'] == 'long'

    def test_image18(self):
        analysis = self.getAnalysis('tImages/t18.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'rising'
        assert analysis['crossingLength'] == 'long'

    def test_image19(self):
        analysis = self.getAnalysis('tImages/t19.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'falling'
        assert analysis['crossingLength'] == 'long'

    def test_image20(self):
        analysis = self.getAnalysis('tImages/t20.png')
        assert analysis['labelTrend'] == 'vertical'
        assert analysis['labelThickness'] == 'falling'
        assert analysis['crossingLength'] == 'long'

    def getAnalysis(self, imageFile):
        img = cv2.imread(imageFile)
        extractor = TDataExtractor(img)
        extractor.analyze()
        analysis = extractor.getAnalysis()
        return analysis
