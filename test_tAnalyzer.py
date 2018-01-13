from tAnalyzer import TAnalyzer

class Test_TAnalyzer:
    def test_shouldReturnAnalysisForProperData(self):
        data = {
            "labelTrend": 'rising',
            "labelThicknessTrend": 'vertical',
            "crossingLength": 'normal',
            "crossingPosition": 'low',
            "labelThickness": 'thin'
        }
        analysis = TAnalyzer.analyze(data)

        assert len(analysis) == 5

        assert analysis[0]["labelTrend"] == "rising"
        assert analysis[0]["analysis"] == "optimism, ardor, enthusiasm, ambition"

        assert analysis[1]["crossingPosition"] == "low"
        assert analysis[1]["analysis"] == "individual goals will be of low importance to him"

        assert analysis[2]["labelThicknessTrend"] == "vertical"
        assert analysis[2]["analysis"] == ""

        assert analysis[3]["crossingLength"] == "normal"
        assert analysis[3]["analysis"] == 'healthy balance, calmness, self-control in thought and action.'

        assert analysis[4]["labelThickness"] == "thin"
        assert analysis[4]["analysis"] == 'resignation. . . extreme sensitivity. . . timidity .'



    def test_shouldReturnOnlyAnalysisForGivenData(self):
        data = {
            "labelTrend": 'rising',
            "labelThicknessTrend": 'vertical',
            "crossingLength": 'normal'
        }
        analysis = TAnalyzer.analyze(data)

        assert len(analysis) == 3

        assert analysis[0]["labelTrend"] == "rising"
        assert analysis[0]["analysis"] == "optimism, ardor, enthusiasm, ambition"


        assert analysis[1]["labelThicknessTrend"] == "vertical"
        assert analysis[1]["analysis"] == ""

        assert analysis[2]["crossingLength"] == "normal"
        assert analysis[2]["analysis"] == 'healthy balance, calmness, self-control in thought and action.'


    def test_shouldReturnOnlyAnalysisForFallingThin(self):
        data = {
            "labelTrend": 'falling'
        }
        analysis = TAnalyzer.analyze(data)

        assert len(analysis) == 1

        assert analysis[0]["labelTrend"] == "falling light pressure"
        assert analysis[0]["analysis"] ==  "like x-ing, dependency, fear, and hopeless resignation."

    def test_shouldReturnOnlyAnalysisForFallingThin(self):
        data = {
            "labelTrend": 'falling',
            'labelThickness': 'thick'
        }
        analysis = TAnalyzer.analyze(data)

        assert len(analysis) == 2

        assert analysis[0]["labelTrend"] == "falling heavy pressure"

        assert analysis[1]["labelThickness"] == "thick"
