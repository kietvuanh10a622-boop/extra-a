def validate_score(score):
    try:
        s = float(score)
        return 0 <= s <= 10
    except:
        return False

def validate_credits(c):
    try:
        c = int(c)
        return c > 0
    except:
        return False
