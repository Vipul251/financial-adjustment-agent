def validate_entry(entry, coa_accounts):
    errors = []
    warnings = []

    debit = 0
    credit = 0

    for line in entry["lines"]:
        acc = str(line["account"]).strip()
        d = float(line.get("debit", 0))
        c = float(line.get("credit", 0))

        debit += d
        credit += c

        # Missing account
        if acc not in coa_accounts:
            errors.append(f"Account '{acc}' not found in COA")

        # Suspicious zero line
        if d == 0 and c == 0:
            warnings.append(f"Zero value line for account {acc}")

    # Balance check
    if round(debit, 2) != round(credit, 2):
        errors.append(f"Unbalanced entry: Debit={debit}, Credit={credit}")

    return errors, warnings