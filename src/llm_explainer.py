def explain_errors(entry, errors):
    explanation = f"Entry {entry.get('id')} could not be processed due to the following issues:\n\n"

    for err in errors:
        explanation += f"• {err}\n"

    explanation += "\nPlease review the journal entry and ensure it follows accounting rules (balanced debits/credits and valid accounts)."

    return explanation