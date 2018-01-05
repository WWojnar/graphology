

#TODO: add more advanced analysis (submisive zones)

class ZonesAnalyzer:

    @staticmethod
    def analyze(separators):
        separators.sort()

        assert len(separators) == 4, "there must be exactly 4 separators"

        upperZoneSize = separators[1]-separators[0]
        middleZoneSize = separators[2] - separators[1]
        lowerZoneSize = separators[3] - separators[2]

        dominanceMinimum = 0.7

        if upperZoneSize > dominanceMinimum*(middleZoneSize+lowerZoneSize):
            return {
                "zoneDominance": "upper zone dominant",
                "analysis" : "intelligence and ambition, idealism, disorientation"
            }

        if middleZoneSize > dominanceMinimum*(lowerZoneSize + upperZoneSize):
            return {
                "zoneDominance": "middle zone dominant",
                "analysis": "overly concerned for himself, sensitivity to feeling and experience"
                            "low super-ego, leader type, strong willed, practical"
            }

        if lowerZoneSize > dominanceMinimum*(upperZoneSize+middleZoneSize):
            return {
                "zoneDominance": "lower zone dominant",
                "analysis": "Driven excessively by instinctual wants, needs constant variety and change "
            }

        return {
            "zoneDominance": "balanced",
            "analysis": "stability, involvement, initiative, balance"
        }