tasks = {
    "easy": {
        "cases": [
            {"symptoms": ["fever"], "severity": "low"},
            {"symptoms": ["cold"], "severity": "low"}
        ],
        "expected": "home_care"
    },

    "medium": {
        "cases": [
            {"symptoms": ["fever", "fatigue"], "severity": "medium"},
            {"symptoms": ["headache", "weakness"], "severity": "medium"}
        ],
        "expected": "visit_doctor"
    },

    "hard": {
        "cases": [
            {"symptoms": ["chest pain"], "severity": "high"},
            {"symptoms": ["breathing problems"], "severity": "high"}
        ],
        "expected": "emergency"
    }
}
