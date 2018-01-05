

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
            return "upper zone dominant"

        if middleZoneSize > dominanceMinimum*(lowerZoneSize + upperZoneSize):
            return "middle zone dominant"

        if lowerZoneSize > dominanceMinimum*(upperZoneSize+middleZoneSize):
            return "lower zone dominant"

        return "balanced"