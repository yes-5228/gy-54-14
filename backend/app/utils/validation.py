def require_fields(payload, fields):
    return [field for field in fields if payload.get(field) in (None, "")]


def validate_score(score):
    try:
        value = float(score)
    except (TypeError, ValueError):
        return "成绩必须是数字"
    if value < 0 or value > 100:
        return "成绩必须在 0 到 100 之间"
    return None


def validate_credit(credit):
    try:
        value = float(credit)
    except (TypeError, ValueError):
        return "学分必须是数字"
    if value < 0:
        return "学分不能为负数"
    return None
