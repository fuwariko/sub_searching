def find_substring(string, substring):
    st_len = len(string)
    sub_len = len(substring)
    i = 0
    while i <= st_len - sub_len:
        if string[i] == substring[0]:
            if string[i: i + sub_len] == substring:  # сравниваем выбранную подстроке в строке с искомой подстрокой
                # обрезаем с i символа
                return True
        i = i + 1
    return False
