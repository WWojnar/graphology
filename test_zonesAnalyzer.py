from zonesAnalyzer import ZonesAnalyzer

class TestZonesAnalyzer:

    def test_ZonesEqual(self):
        assert ZonesAnalyzer.analyze([1, 2, 3, 4]) == "balanced"

    def test_UpperZoneDominant(self):
        assert ZonesAnalyzer.analyze([20, 60, 80, 110]) == "upper zone dominant"

    def test_MiddleZoneDominant(self):
        assert ZonesAnalyzer.analyze([10, 20, 40, 55]) == "middle zone dominant"

    def test_LowerZoneDominant(self):
        assert ZonesAnalyzer.analyze([10, 20, 35, 55]) == "lower zone dominant"

    def test_BalancedZones(self):
        assert ZonesAnalyzer.analyze([10, 20, 31, 38]) == "balanced"
