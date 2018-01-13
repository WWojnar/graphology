from tDataExtractor import TDataExtractor
import cv2



class Test_tDataExtractor:

    def test_image1(self):
        data = self.extractData('tImages/t1.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'short'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'


    def test_image2(self):
        data = self.extractData('tImages/t2.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image3(self):
        data = self.extractData('tImages/t3.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'thin'


    def test_image4(self):
        data = self.extractData('tImages/t4.png')
        assert data['labelTrend'] == 'falling'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image5(self):
        data = self.extractData('tImages/t5.png')
        assert data['labelTrend'] == 'rising'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image6(self):
        data = self.extractData('tImages/t6.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'normal'

    def test_image7(self):
        data = self.extractData('tImages/t7.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image8(self):
        data = self.extractData('tImages/t8.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image9(self):
        data = self.extractData('tImages/t9.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'normal'

    def test_image10(self):
        data = self.extractData('tImages/t10.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image11(self):
        data = self.extractData('tImages/t11.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image12(self):
        data = self.extractData('tImages/t12.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'falling'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'thick'

    def test_image13(self):
        data = self.extractData('tImages/t13.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image14(self):
        data = self.extractData('tImages/t14.png')
        assert data['labelTrend'] == 'rising'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'normal'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image15(self):
        data = self.extractData('tImages/t15.png')
        assert data['labelTrend'] == 'falling'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'thick'

    def test_image16(self):
        data = self.extractData('tImages/t16.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'normal'

    def test_image17(self):
        data = self.extractData('tImages/t17.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'constant'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image18(self):
        data = self.extractData('tImages/t18.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'rising'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'medium'
        assert data['labelThickness'] == 'normal'

    def test_image19(self):
        data = self.extractData('tImages/t19.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'falling'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'normal'

    def test_image20(self):
        data = self.extractData('tImages/t20.png')
        assert data['labelTrend'] == 'vertical'
        assert data['labelThicknessTrend'] == 'falling'
        assert data['crossingLength'] == 'long'
        assert data['crossingPosition'] == 'high'
        assert data['labelThickness'] == 'thin'

    def extractData(self, imageFile):
        img = cv2.imread(imageFile)
        extractor = TDataExtractor(img)
        extractor.analyze()
        analysis = extractor.getData()
        return analysis
