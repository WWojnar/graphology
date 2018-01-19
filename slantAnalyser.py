from sets import Set


class SlantAnalyser:
    slantPossibleValues = [
        {
            "angleRange": [129, 180],
            "slantType": "extremely reclined",
            "analysis": "out of touch with his environment and lives in the past, "
                        "can still show the well-developed and charming public personality"
        },
        {
            "angleRange": [113, 128],
            "slantType": "very reclined",
            "analysis": "independent, hard to fathom and difficult to get along with, cold, yet may still seem sociable"
        },
        {
            "angleRange": [98, 112],
            "slantType": "reclined",
            "analysis": "feelings are repressed, out of touch with themselves emotionally"
                        " yet are self-absorbed at the same time, reclined writers resist accepting progress or change."
        },
        {
            "angleRange": [83, 97],
            "slantType": "vertical",
            "analysis": "Open to the experience of the moment, but his responses are cautious and considered"
        },
        {
            "angleRange": [68, 82],
            "slantType": "inclined",
            "analysis": "sensitive and emotionally healthy, with modes responses"
        },
        {
            "angleRange": [53, 67],
            "slantType": "very inclined",
            "analysis": "express their emotional self impulsively, responds with compassion"
        },
        {
            "angleRange": [0, 52],
            "slantType": "extremely inclined",
            "analysis": "volcano of emotional reactions: extremely ardent, passionate, "
                        "jealous, easily offended, very demonstrative with affections, "
                        "susceptible to hurt arid can hate bitterly and with abandon, loves the same way"
        }
    ]

    @staticmethod
    def analyzeSlant(angles):
        results = []
        foundValues = Set()
        for angle in angles:
            for possible in SlantAnalyser.slantPossibleValues:
                if possible["angleRange"][0] <= angle <= possible["angleRange"][1]:
                    results.append(possible)
                    foundValues.add(possible["slantType"])
        return results
