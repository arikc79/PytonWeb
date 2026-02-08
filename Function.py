# 1
def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


# 2
def revers(s, i=0):
    if len(s) <= 1:
        return s

    if i >= len(s):
        return ""
    return revers(s, i + 1) + s[i]


if __name__ == "__main__":
    print(revers("ТІВИРП, World!"))
