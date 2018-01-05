from zonesAnalyzer import ZonesAnalyzer

class TestZonesAnalyzer:

    def test_ZonesEqual(self):
        assert ZonesAnalyzer.analyze([1, 2, 3, 4])["zoneDominance"] == "balanced"

    def test_UpperZoneDominant(self):
        assert ZonesAnalyzer.analyze([20, 60, 80, 110])["zoneDominance"] == "upper zone dominant"

    def test_MiddleZoneDominant(self):
        assert ZonesAnalyzer.analyze([10, 20, 40, 55])["zoneDominance"] == "middle zone dominant"

    def test_LowerZoneDominant(self):
        assert ZonesAnalyzer.analyze([10, 20, 35, 55])["zoneDominance"] == "lower zone dominant"

    def test_BalancedZones(self):
        assert ZonesAnalyzer.analyze([10, 20, 31, 38])["zoneDominance"] == "balanced"
