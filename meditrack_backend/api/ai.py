"""
AI-powered symptom analyzer for MediTrack.

Provides symptom analysis and recommendations based on
keyword matching and severity assessment.
"""

from typing import Dict, List, Tuple


class SymptomAnalyzer:
    """
    Analyzes user symptoms and provides recommendations.
    
    Uses keyword matching to identify potential conditions
    and severity assessment to suggest appropriate actions.
    """

    # Condition database with symptoms
    CONDITIONS = {
        'common_cold': {
            'symptoms': ['cold', 'cough', 'runny nose', 'sneezing', 'sore throat'],
            'description': 'Common Cold',
            'severity': 'Low',
            'care': 'Rest, hydration, and over-the-counter medications'
        },
        'flu': {
            'symptoms': ['flu', 'fever', 'body aches', 'fatigue', 'cough', 'chills'],
            'description': 'Influenza (Flu)',
            'severity': 'Moderate',
            'care': 'Rest, fluids, and antiviral medications if available'
        },
        'headache': {
            'symptoms': ['headache', 'migraine', 'head pain', 'throbbing'],
            'description': 'Headache',
            'severity': 'Low',
            'care': 'Rest in quiet area, over-the-counter pain relievers, hydration'
        },
        'allergies': {
            'symptoms': ['allergies', 'sneezing', 'itchy eyes', 'runny nose', 'rash'],
            'description': 'Allergic Reaction',
            'severity': 'Low-Moderate',
            'care': 'Identify and avoid triggers, antihistamines'
        },
        'anxiety': {
            'symptoms': ['anxiety', 'panic', 'stress', 'nervous', 'worry', 'heart palpitations'],
            'description': 'Anxiety',
            'severity': 'Low-Moderate',
            'care': 'Deep breathing, meditation, relaxation techniques'
        },
        'gastroenteritis': {
            'symptoms': ['nausea', 'vomiting', 'diarrhea', 'stomach pain', 'abdominal cramps'],
            'description': 'Gastroenteritis (Stomach Bug)',
            'severity': 'Moderate',
            'care': 'Rest, clear liquids, electrolyte replacement'
        },
        'fever': {
            'symptoms': ['fever', 'high temperature', 'chills', 'sweating'],
            'description': 'Fever',
            'severity': 'Low-Moderate',
            'care': 'Stay hydrated, rest, fever-reducing medications'
        },
    }

    def analyze(self, symptoms: str, severity: int = 5) -> Dict[str, str]:
        """
        Analyze user symptoms and provide recommendations.
        
        Args:
            symptoms: User's symptom description
            severity: Severity level (1-10)
            
        Returns:
            Dictionary with analysis and suggested action
        """
        symptoms_lower = symptoms.lower()
        matched_conditions = self._match_conditions(symptoms_lower)
        
        analysis = self._generate_analysis(matched_conditions, symptoms_lower)
        action = self._recommend_action(matched_conditions, severity)
        
        return {
            'analysis': analysis,
            'action': action
        }

    def _match_conditions(self, symptoms: str) -> List[Tuple[str, int]]:
        """
        Match symptoms to known conditions.
        
        Returns:
            List of tuples (condition_key, match_count)
        """
        matches = []
        
        for condition_key, condition_data in self.CONDITIONS.items():
            match_count = 0
            for symptom in condition_data['symptoms']:
                if symptom.lower() in symptoms:
                    match_count += 1
            
            if match_count > 0:
                matches.append((condition_key, match_count))
        
        # Sort by match count (descending)
        return sorted(matches, key=lambda x: x[1], reverse=True)

    def _generate_analysis(self, matched_conditions: List[Tuple[str, int]], 
                          symptoms: str) -> str:
        """
        Generate analysis based on matched conditions.
        
        Args:
            matched_conditions: List of matched conditions
            symptoms: Original symptom description
            
        Returns:
            Analysis text
        """
        if not matched_conditions:
            return (
                "Based on your symptoms, we recommend consulting with a healthcare "
                "professional for a proper diagnosis. Keep track of your symptoms and "
                "seek medical attention if they worsen."
            )
        
        primary_condition_key = matched_conditions[0][0]
        primary_condition = self.CONDITIONS[primary_condition_key]
        
        analysis = f"""Based on your symptoms, we identify the following:

**Potential Condition:** {primary_condition['description']}
**Severity Level:** {primary_condition['severity']}
**Recommended Care:** {primary_condition['care']}

**Your Symptoms:** {symptoms[:100]}...

Please note this is not a medical diagnosis. Always consult with a healthcare professional 
for accurate diagnosis and treatment."""
        
        return analysis

    def _recommend_action(self, matched_conditions: List[Tuple[str, int]], 
                         severity: int) -> str:
        """
        Recommend action based on conditions and severity.
        
        Args:
            matched_conditions: List of matched conditions
            severity: Severity level (1-10)
            
        Returns:
            Recommended action
        """
        if not matched_conditions:
            if severity > 7:
                return 'emergency'
            elif severity > 4:
                return 'visit_clinic'
            return 'self_care'
        
        # High severity and matched conditions
        if severity > 7:
            return 'emergency'
        elif severity > 5 or matched_conditions[0][1] > 4:
            return 'visit_clinic'
        
        return 'self_care'
