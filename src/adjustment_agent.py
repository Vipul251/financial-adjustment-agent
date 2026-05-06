import json
from src.coa_loader import load_coa
from src.validator import validate_entry
from src.llm_explainer import explain_errors
from src.ic_detector import detect_circular_ic


class AdjustmentAgent:

    def __init__(self, coa_file):
        self.coa_accounts = load_coa(coa_file)

    # ✅ THIS MUST BE INSIDE CLASS
    def process(self, adjustments_file):

        content = adjustments_file.read()

        try:
            entries = json.loads(content)
        except:
            entries = json.loads(content.decode("utf-8"))

        if isinstance(entries, str):
            entries = json.loads(entries)
        
    # Handle multiple possible formats
        if isinstance(entries, dict):
           if "entries" in entries:
               entries = entries["entries"]
           else:
                raise ValueError("Invalid format: expected key 'entries'")

        if not isinstance(entries, list):
          raise ValueError("Adjustments must be a list")
        # if not isinstance(entries, list):
        #     raise ValueError("Adjustments must be a list")

        # Clean entries
        clean_entries = []
        for e in entries:
            if isinstance(e, dict):
                clean_entries.append(e)
            else:
                try:
                    parsed = json.loads(e)
                    if isinstance(parsed, dict):
                        clean_entries.append(parsed)
                except:
                    continue

        entries = clean_entries

        results = {
            "valid": [],
            "rejected": [],
            "flagged": []
        }

        if detect_circular_ic(entries):
            results["flagged"].append({
                "issue": "Circular intercompany entries detected",
                "action": "manual review required"
            })

        for entry in entries:
            errors, warnings = validate_entry(entry, self.coa_accounts)

            if errors:
                results["rejected"].append({
                    "entry_id": entry.get("id"),
                    "errors": errors,
                    "explanation": explain_errors(entry, errors)
                })
            else:
                results["valid"].append({
                    "entry": entry,
                    "warnings": warnings
                })

        return results
