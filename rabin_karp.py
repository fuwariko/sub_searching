def find_substring(string, substring):
    st_len = len(string)
    sub_len = len(substring)
    sub_hash = 0
    st_hash = 0
    h = 1
    p = 256
    q = 3

    for i in range(sub_len - 1):
        h = (h * p) % q

    for i in range(sub_len):
        sub_hash = (p * sub_hash + ord(substring[i])) % q  # хэш значение для подстроки
        st_hash = (p * st_hash + ord(string[i])) % q  # хэш значение для первого окна

    for i in range(st_len - sub_len + 1):
        if sub_hash == st_hash:  # если хэши равны, то еще не значит, что символы одинаковые, поэтому проверяем это
            for j in range(sub_len):
                if string[i + j] != substring[j]:
                    break
                else:
                    return True

        if i < (st_len - sub_len):  # удаляем хэш первого символа и добавляем хэш последнего
            st_hash = (st_hash - ord(string[i]) * h % q + q) % q
            st_hash = (st_hash * p + ord(string[i + sub_len])) % q

    return False
