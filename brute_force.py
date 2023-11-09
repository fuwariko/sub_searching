def find_substring(string, substring):
    st_len = len(string)
    sub_len = len(substring)
    for i in range(st_len - sub_len + 1):
        for j in range(sub_len):
            if string[i + j] != substring[j]:
                break
            else:
                j = j + 1
        if j == sub_len:
            return True
    return False