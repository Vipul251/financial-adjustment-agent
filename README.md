# 📊 Financial Adjustment Agent (Agentic AI Prototype)

An agentic system for validating ERP journal entries with audit-ready error handling and explainability.

---

## 🚀 Overview

This project is a prototype of an **AI-native financial reporting system**, focusing on one critical slice:

👉 **Manual Adjustments Agent**

It ingests:

* Chart of Accounts (COA)
* Manual journal entries (adjustments)

And performs:

* Validation of accounting rules
* Detection of errors (e.g., unbalanced entries)
* Identification of data issues (missing accounts, circular intercompany entries)
* Human-readable explanations for finance users

---

## 🧠 Key Features

* ✅ Debit/Credit validation (must balance)
* ✅ COA validation (account must exist)
* ✅ Circular intercompany detection
* ✅ Handles messy JSON inputs (real-world ERP data)
* ✅ Clear error explanations (finance-friendly)
* ✅ Streamlit UI for interaction
* ✅ Downloadable validation results

---

## 🏗️ Project Structure

```
project/
 ├── app.py                      # Streamlit UI
 ├── src/
 │    ├── adjustment_agent.py    # Core agent logic
 │    ├── validator.py           # Entry validation rules
 │    ├── coa_loader.py          # COA loader
 │    ├── ic_detector.py         # Circular intercompany detection
 │    ├── llm_explainer.py       # Error explanations
 ├── data/
 │    ├── chart_of_accounts.csv
 │    ├── manual_adjustments.json
 ├── output/
 ├── requirements.txt
 └── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd financial-adjustment-agent
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the application

```
streamlit run app.py
```

---

## 📥 Input Format

### Chart of Accounts (CSV)

```
account_code
1001
2001
3001
```

---

### Manual Adjustments (JSON)

```
[
  {
    "id": "JE1",
    "lines": [
      {"account": "1001", "debit": 1000, "credit": 0},
      {"account": "2001", "debit": 0, "credit": 1000}
    ]
  }
]
```

---

## 📤 Output

The system categorizes results into:

* **Valid** → Entries that pass all checks
* **Rejected** → Entries with errors
* **Flagged** → Suspicious cases (e.g., circular intercompany)

Each rejected entry includes:

* Error list
* Human-readable explanation

---

## ⚠️ Real-World Handling

This system is designed to handle messy ERP data:

* String-wrapped JSON
* Missing or invalid accounts
* Unbalanced journal entries
* Unexpected formats
* Circular intercompany transactions

---

## 🧠 Design Approach

* Deterministic logic for financial correctness
* AI-inspired reasoning for explanations
* Defensive programming for messy inputs
* Audit-friendly outputs

---

## 🔮 Future Improvements

* Confidence scoring for account validation
* COA auto-mapping agent
* Full financial statement generation
* Multi-entity consolidation support
* Persistent audit logs

---

## 📌 Notes

This is a **prototype**, not a production system.
It focuses on correctness, explainability, and handling real-world data issues.

---

## 👨‍💻 Author

Vipul Bhatt
AI / Agentic Systems Enthusiast
