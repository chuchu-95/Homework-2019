def huiwen(lst):
    """
    :param lst: input a list to judge if it is palindrome
    :return: return true or false
    """
    if lst[::] == lst[::-1]:
        return True
    else:
        return False


print(huiwen([1, 2, 1]))

