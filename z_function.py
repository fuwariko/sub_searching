def z_function(string):
    st_len = len(string)
    z_func = [0] * st_len
    left = 0
    right = 0  # границы самой правой подстроки = префиксу, которую уже нашли
    for i in range(1, st_len):
        if i <= right:  # если символ лежит внутри границ, то значение ф-ии будет от i-left,
            # если = правой границе, то обрезаем до нее
            z_func[i] = min(right - i + 1, z_func[i - left])
        while i + z_func[i] < st_len and string[z_func[i]] == string[i + z_func[i]]:
            # обновляем значение зет функции, пока не встретились неравные символы с префиксом
            # и пока не вышли за границы
            z_func[i] += 1
        # проверяем, правее ли мы, обновляем границы
        if i + z_func[i] - 1 > right:
            right = i + z_func[i] - 1
            left = i
    return z_func


def find_substring(string, substring):
    z_func = z_function(substring + "#" + string)
    sub_len = len(substring)
    for i in range(1, len(z_func)):
        if z_func[i] == sub_len:  # если длина подстроки совпадает со значением зет функции то подстрока найдена
            return True
    return False