"""
    1678. Goal Parser Interpretation
    You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
    Given the string command, return the Goal Parser's interpretation of command.

    :type command: str
    :rtype: str

    This following codes are modified for use in local editor. It may be slighly different from submission code.
"""
def interpret(command):
    n = len(command)
    temp = []
    for i in range(n):
        if command[i].isalpha():
            temp.append(command[i])
        if command[i] == "(" and command[i+1] == ")":
            temp.append("o")

    return "".join(temp)

print(interpret("(al)G(al)()()G"))