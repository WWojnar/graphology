from slantAnalyser import SlantAnalyser


class TestSlantAnalyser:
    def test_slant_extremely_reclined(self):
        assert SlantAnalyser.analyzeSlant([135])[0]["slantType"] == "extremely reclined"
        assert SlantAnalyser.analyzeSlant([129])[0]["slantType"] == "extremely reclined"
        assert SlantAnalyser.analyzeSlant([180])[0]["slantType"] == "extremely reclined"

    def test_slant_very_reclined(self):
        assert SlantAnalyser.analyzeSlant([120])[0]["slantType"] == "very reclined"
        assert SlantAnalyser.analyzeSlant([113])[0]["slantType"] == "very reclined"
        assert SlantAnalyser.analyzeSlant([128])[0]["slantType"] == "very reclined"

    def test_slant_reclined(self):
        assert SlantAnalyser.analyzeSlant([105])[0]["slantType"] == "reclined"
        assert SlantAnalyser.analyzeSlant([98])[0]["slantType"] == "reclined"
        assert SlantAnalyser.analyzeSlant([112])[0]["slantType"] == "reclined"

    def test_slant_vertical(self):
        assert SlantAnalyser.analyzeSlant([90])[0]["slantType"] == "vertical"
        assert SlantAnalyser.analyzeSlant([83])[0]["slantType"] == "vertical"
        assert SlantAnalyser.analyzeSlant([97])[0]["slantType"] == "vertical"

    def test_slant_inclined(self):
        assert SlantAnalyser.analyzeSlant([75])[0]["slantType"] == "inclined"
        assert SlantAnalyser.analyzeSlant([68])[0]["slantType"] == "inclined"
        assert SlantAnalyser.analyzeSlant([82])[0]["slantType"] == "inclined"

    def test_slant_very_inclined(self):
        assert SlantAnalyser.analyzeSlant([60])[0]["slantType"] == "very inclined"
        assert SlantAnalyser.analyzeSlant([53])[0]["slantType"] == "very inclined"
        assert SlantAnalyser.analyzeSlant([67])[0]["slantType"] == "very inclined"

    def test_slant_extremely_inclined(self):
        assert SlantAnalyser.analyzeSlant([45])[0]["slantType"] == "extremely inclined"
        assert SlantAnalyser.analyzeSlant([52])[0]["slantType"] == "extremely inclined"
        assert SlantAnalyser.analyzeSlant([0])[0]["slantType"] == "extremely inclined"
