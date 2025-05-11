def parse_cell(value):
    """Extract base and tier change values"""
    if not value:
        return "", 0

    if value.startswith("+"):
        tier_change = 1
        base = value[1:]
    elif value.startswith("-"):
        tier_change = -1
        base = value[1:]
    else:
        tier_change = 0
        base = value

    return base, tier_change
