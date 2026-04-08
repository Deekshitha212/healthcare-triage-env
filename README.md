Markdown
# Healthcare Triage AI Environment

## Overview

This project simulates a real-world healthcare triage system where an AI agent must decide the appropriate level of care for a patient.

The agent evaluates patient symptoms and determines whether the patient requires:
- Home care 
- Doctor consultation 
- Emergency care 
This environment follows the OpenEnv specification with step(), reset(), and state() APIs.
---

## Motivation

Healthcare triage is a critical real-world problem. Incorrect decisions can lead to severe consequences.

This environment allows evaluation of AI agents in making safe and effective healthcare decisions, especially in:
- Early diagnosis
- Emergency detection
- Resource prioritization

---

## Environment Design

### Observations (State)

The agent receives patient data:

- Symptoms (list of strings)
- Severity (low / medium / high)
- Age
- Duration of symptoms

Example:
{ "symptoms": ["fever", "fatigue"], "severity": "medium", "age": 40, "duration": 3 }

---

### Actions

The agent can choose one of:

- home_care
- visit_doctor
- emergency

---

###  Reward Function

- Correct decision → +1.0  
- Partially correct → +0.5  
- Wrong decision → -0.5  
- Missing emergency → -1.0  

---

## Tasks
Each task is evaluated using a deterministic grader with scores from 0.0 to 1.0.
### Easy
- Simple symptoms (fever, cold)

### Medium
- Moderate conditions (fatigue, weakness)

### Hard
- Critical symptoms (chest pain, breathing problems)

---

## How to Run

pip install pydantic openai

python test_env.py

python test_tasks.py

python baseline.py

python patient_test.py

---

## Baseline Performance

A simple rule-based agent selects actions based on symptom severity and critical conditions.

---
## Patient Interaction

The system also includes a simple interactive mode where users can input their symptoms and receive AI-based triage decisions.

Run:

python patient_test.py

___

## Author

Deekshitha Thammi

---

## Conclusion

This environment demonstrates how AI can assist in healthcare decision-making and provides a structured way to evaluate agent performance.