def get_full_name(user):
    """Return 'first last' from a user dict. Return 'Unknown' if name keys are missing."""
    first = user["first_name"]  # BUG: should use user.get("first_name", "Unknown")
    last = user["last_name"]    # BUG: should use user.get("last_name", "")
    return f"{first} {last}".strip()
