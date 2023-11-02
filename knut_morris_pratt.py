def find_substring(string, substring):
    s = substring + "#" + string
    array = [0] * len(s)

    for i in range(1, len(s)):
        j = array[i - 1]  # значение префикс функции на предыдущем этапе
        while j > 0 and s[i] != s[j]:  # пока j > 0 и j и i символ не равны мы должны смещаться назад и уменьшать j
            j = array[j - 1]
        if j == 0:
            if s[i] == s[0]:  # если они равны, то длина префикс функции = 1
                array[i] = 1
            else:
                array[i] = 0  # если не равны, то 0
        else:
            array[i] = j + 1  # если j > 0  и при этом s[i]  совпадает с s[j]
            # то значит i входит в подстроку и увеличиваем j, тк до этого сравнивали значение на предыдущем этапе

        if array[i] == len(substring):
            return True  # чтобы узнать индекс символа в стринг нужно вычесть длину подстроки + 1,
            # чтобы не оказаться на решетке, а потом вычесть подстроку и решетку

    return False
