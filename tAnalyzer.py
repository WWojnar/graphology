class TAnalyzer:
    @staticmethod
    def analyze(data):
        result = []
        if 'labelTrend' in data:
            result.append(TAnalyzer.getLabelTrendAnalysis(data))

        if 'crossingPosition' in data:
            result.append(TAnalyzer.getPositionCrossingAnalysis(data))

        if 'labelThicknessTrend' in data:
            result.append(TAnalyzer.getLabelThicknessTrendAnalysis(data))

        if 'crossingLength' in data:
            result.append(TAnalyzer.getCrossingLengthAnalysis(data))

        if 'labelThickness' in data:
            result.append(TAnalyzer.getLabelThicknessAnalysis(data))

        return result

    @staticmethod
    def getLabelThicknessAnalysis(data):
        analysis = {'labelThickness': data['labelThickness'], "analysis": ""}
        if data['labelThickness'] == 'thick':
            analysis['analysis'] = 'domineering will and great energy, but ' \
                                   'capable of insensitivity and selfishness in pursuing goals. '
        if data['labelThickness'] == 'thin':
            analysis['analysis'] = 'resignation. . . extreme sensitivity. . . timidity .'
        return analysis

    @staticmethod
    def getCrossingLengthAnalysis(data):
        analysis = {'crossingLength': data['crossingLength'], "analysis": ""}
        if data['crossingLength'] == 'short':
            analysis['analysis'] = 'lack of drive and will power. . . in superior scripts, reserve ' \
                                   'and restraint of natural instincts, in inferior script,' \
                                   ' lack of confidence timidity.'
        if data['crossingLength'] == 'normal':
            analysis['analysis'] = 'healthy balance, calmness, self-control in thought and action.'
        if data['crossingLength'] == 'long':
            analysis['analysis'] = 'energy, vigor, resolution, boldness . . . an overly-long ' \
                                   'crossing not only implies the same confidence, persistence and enthusiasm,' \
                                   'but also a person consumed with ambition who cannot be stopped'
        return analysis

    @staticmethod
    def getLabelThicknessTrendAnalysis(data):
        analysis = {'labelThicknessTrend': data['labelThicknessTrend'], "analysis": ""}
        if data['labelThicknessTrend'] == 'rising':
            analysis['analysis'] = 'the club shape that means cruelty and possible brutality. '
        if data['labelThicknessTrend'] == 'falling':
            analysis['analysis'] = 'quick-witted and sarcastic.'
        return analysis

    @staticmethod
    def getPositionCrossingAnalysis(data):
        analysis = {'crossingPosition': data['crossingPosition'], "analysis": ""}
        if data['crossingPosition'] == 'low':
            analysis['analysis'] = 'individual goals will be of low importance to him'
        if data['crossingPosition'] == 'medium':
            analysis['analysis'] = 'individual goals will be of medium importance to him'
        if data['crossingPosition'] == 'high':
            analysis['analysis'] = 'individual goals will be of high importance to him'
        return analysis

    @staticmethod
    def getLabelTrendAnalysis(data):
        analysis = {'labelTrend': data['labelTrend'], "analysis": ""}
        if data['labelTrend'] == 'rising':
            analysis["analysis"] = "optimism, ardor, enthusiasm, ambition"
        if data['labelTrend'] == 'falling':
            if 'labelThickness' in data and data['labelThickness'] == 'thick':
                analysis["analysis"] = "stubborness and an argumentative nature" \
                                       ". . . very heavy pressure leads " \
                                       "to despotism, aggressiveness, destructiveness, and cruelty."
                analysis['labelTrend'] += ' heavy pressure'
            else:
                analysis['analysis'] = "like x-ing, dependency, fear, and hopeless resignation."
                analysis['labelTrend'] += ' light pressure'
        return analysis
