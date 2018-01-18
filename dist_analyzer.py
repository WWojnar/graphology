

#TODO: add more advanced analysis (submisive zones)

class DistAnalyzer:

    @staticmethod
    def analyze(ratio):
    
	if ratio<0.1:
		return {
			"spacing": "verry narrow",
			"analysis": "someone who will crowd others for attention, craving constant contact and closeness"
			}
        
	if ratio>1.9:
		return {
			"spacing": "verry wide",
			"analysis": "someone who need maintain his distance from social contact, either due to an inner need for privacy."
			}

        
	if ratio>0.1 and ratio<0.7:
		return {
			"spacing": "narrow letters with cramped spacing",
			"analysis": "someone who is fearful and dependent, who cannot give himself (or others) enough space in life"
			}
        
	if ratio>1.4 and ratio<1.9:
        	return {
			"spacing": "wide letters with wide spaces",
			"analysis": "someone who demands attention in an extravagant or exaggerated manner, stemming from a need to be noticed"
			}
	if ratio>0.9 and ratio<1.4:
		return {
			"spacing": "well-balanced",
			"analysis": "someone who is social maturity, intelligence and inner organization"
			}
