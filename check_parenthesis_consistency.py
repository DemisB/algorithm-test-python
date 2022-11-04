def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for c in string:
        if c not in ("(", "[", "{", "}", "]", ")"):
            continue

        if c in ("(", "[", "{"):
            stack.append(c)

        if c in ("}", "]", ")"):
            try:
                if stack.pop() != pairs[c]:
                    return False
            except IndexError:
                return False

    if len(stack):
        return False

    return True
