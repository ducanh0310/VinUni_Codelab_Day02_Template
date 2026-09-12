# Deep Dive Report

# Vinhomes AI Resident Feedback Intelligence System


# Phase 3 — Problem Statement


## 1. Who

Vinhomes operation teams responsible for handling resident requests.


## 2. What

Thousands of daily resident feedback messages need classification and routing.


## 3. Where

Smart urban areas operated by Vinhomes.


## 4. When

During daily operation and peak complaint periods.


## 5. Why

Manual processing reduces operation efficiency and resident experience.


## 6. Success Metric

Business:

- Faster response time
- Higher resident satisfaction


AI:

- Classification accuracy
- Routing accuracy



---

# Future-State Workflow


Resident Feedback

↓

AI Understanding Layer

↓

Information Extraction

↓

Issue Classification

↓

Priority Detection

↓

Department Recommendation

↓

Human Approval

↓

Ticket Creation


---

# AI Fit Analysis


## Rule-based AI

Used for:

- Emergency keywords
- Safety warnings


Example:

"cháy", "rò điện", "ngập nước"

→ High priority


---

## LLM


Used for:

- Understanding Vietnamese complaints
- Summarization
- Reasoning


Example:


Input:

"Nhà tôi tầng 12 bị nước nhỏ xuống từ trần phòng ngủ"


Output:

Category:
Water Leakage

Priority:
High



---

# Human-in-the-loop


AI does NOT replace operation managers.


AI:

✓ Analyze

✓ Recommend

✓ Prioritize


Human:

✓ Approve

✓ Take action

✓ Make final decision



---

# Operational Boundary


## AI Can

- Classify complaints
- Summarize issues
- Recommend department
- Generate reports


## AI Cannot

- Approve compensation
- Make legal decisions
- Close complaints automatically



---

# Fallback Strategy


If AI confidence < 80%:


↓

Send to human operator


If safety issue detected:


↓

Immediate escalation



---

# Evaluation Checklist


| Criteria | Result |
|-|-|
| Clear business problem | YES |
| Data availability | YES |
| AI suitability | YES |
| Safety risk controlled | YES |
| Human approval available | YES |


# Decision

## GO

Reason:

The solution creates operational value with controlled AI risk.