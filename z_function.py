def z_function(string):
    st_len = len(string)
    z_func = [0] * st_len
    left = 0
    right = 0
    for i in range(1, st_len):
        if i <= right:
            z_func[i] = min(right - i + 1, z_func[i - left])
        while i + z_func[i] < st_len and string[z_func[i]] == string[i + z_func[i]]:
            z_func[i] += 1
        if i + z_func[i] - 1 > right:
            right = i + z_func[i] - 1
            left = i
    return z_func


def find_substring(string, substring):
    z_func = z_function(substring + "#" + string)
    st_len = len(string)
    sub_len = len(substring)
    for i in range(sub_len + 1, st_len + 2):
        if z_func[i] == sub_len:
            return True
    return False