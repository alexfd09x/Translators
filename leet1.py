import appendix

leet = ['4', '8', '<', '|)', '3', '|=', '6', '|-|', '1', '_/', '|<', '|_', '|\/|',
        'И', '0', '|°', '0,', '|2', '5', '7', '|_|', '\/', '\/\/', '><', 'Ч', '7_', ' ', 'I', 'Z', 'E', 'A',
        'S', 'G', 'T', 'B', 'g', '.', '!', '?', '/', '\\', ')', '(', '-', ':', ';', '_', '+', '=', '*',
        ')|(', 'E', 'N', '/|', '||', '(|)', '||_', 'Y', '|||_', '6|', '6', '`6', '-)', '|О', '9|']


def coder(a):
    b = len(a)
    a = appendix.lister(a)
    for i in range(0, 1):
        for i in range(0, b):
            if a[i] == 'a' or a[i] == 'A' or a[i] == 'а' or a[i] == 'А':
                a[i] = leet[0]
            elif a[i] == 'b' or a[i] == 'B' or a[i] == 'в' or a[i] == 'В':
                a[i] = leet[1]
            elif a[i] == 'c' or a[i] == 'C' or a[i] == 'с' or a[i] == 'С':
                a[i] = leet[2]
            elif a[i] == 'd' or a[i] == 'D' or a[i] == 'д' or a[i] == 'Д':
                a[i] = leet[3]
            elif a[i] == 'e' or a[i] == 'E' or a[i] == 'е' or a[i] == 'Е' or a[i] == 'ё' or a[i] == 'Ё':
                a[i] = leet[4]
            elif a[i] == 'f' or a[i] == 'F':
                a[i] = leet[5]
            elif a[i] == 'g' or a[i] == 'G' or a[i] == 'б' or a[i] == 'Б':
                a[i] = leet[6]
            elif a[i] == 'h' or a[i] == 'H' or a[i] == 'н' or a[i] == 'Н':
                a[i] = leet[7]
            elif a[i] == 'i' or a[i] == 'I':
                a[i] = leet[8]
            elif a[i] == 'j' or a[i] == 'J':
                a[i] = leet[9]
            elif a[i] == 'k' or a[i] == 'K' or a[i] == 'к' or a[i] == 'К':
                a[i] = leet[10]
            elif a[i] == 'l' or a[i] == 'L':
                a[i] = leet[11]
            elif a[i] == 'm' or a[i] == 'M' or a[i] == 'м' or a[i] == 'М':
                a[i] = leet[12]
            elif a[i] == 'n' or a[i] == 'N':
                a[i] = leet[13]
            elif a[i] == 'o' or a[i] == 'O' or a[i] == 'о' or a[i] == 'О':
                a[i] = leet[14]
            elif a[i] == 'p' or a[i] == 'P' or a[i] == 'р' or a[i] == 'Р':
                a[i] = leet[15]
            elif a[i] == 'q' or a[i] == 'Q':
                a[i] = leet[16]
            elif a[i] == 'r' or a[i] == 'R':
                a[i] = leet[17]
            elif a[i] == 's' or a[i] == 'S':
                a[i] = leet[18]
            elif a[i] == 't' or a[i] == 'T' or a[i] == 'т' or a[i] == 'Т':
                a[i] = leet[19]
            elif a[i] == 'u' or a[i] == 'U':
                a[i] = leet[20]
            elif a[i] == 'v' or a[i] == 'V':
                a[i] = leet[21]
            elif a[i] == 'w' or a[i] == 'W' or a[i] == 'ш' or a[i] == 'Ш':
                a[i] = leet[22]
            elif a[i] == 'x' or a[i] == 'X' or a[i] == 'х' or a[i] == 'Х':
                a[i] = leet[23]
            elif a[i] == 'y' or a[i] == 'Y' or a[i] == 'у' or a[i] == 'У':
                a[i] = leet[24]
            elif a[i] == 'z' or a[i] == 'Z':
                a[i] = leet[25]
            elif a[i] == ' ':
                a[i] = leet[26]
            elif a[i] == '1':
                a[i] = leet[27]
            elif a[i] == '2':
                a[i] = leet[28]
            elif a[i] == '3':
                a[i] = leet[29]
            elif a[i] == '4':
                a[i] = leet[30]
            elif a[i] == '5':
                a[i] = leet[31]
            elif a[i] == '6':
                a[i] = leet[32]
            elif a[i] == '7':
                a[i] = leet[33]
            elif a[i] == '8':
                a[i] = leet[34]
            elif a[i] == '9':
                a[i] = leet[35]
            elif a[i] == '.':
                a[i] = leet[36]
            elif a[i] == '!':
                a[i] = leet[37]
            elif a[i] == '?':
                a[i] = leet[38]
            elif a[i] == '/':
                a[i] = leet[39]
            elif a[i] == '\\':
                a[i] = leet[40]
            elif a[i] == ')':
                a[i] = leet[41]
            elif a[i] == '(':
                a[i] = leet[42]
            elif a[i] == '-':
                a[i] = leet[43]
            elif a[i] == ':':
                a[i] = leet[44]
            elif a[i] == ';':
                a[i] = leet[45]
            elif a[i] == '_':
                a[i] = leet[46]
            elif a[i] == '+':
                a[i] = leet[47]
            elif a[i] == '=':
                a[i] = leet[48]
            elif a[i] == '*':
                a[i] = leet[49]
            elif a[i] == 'ж' or a[i] == 'Ж':
                a[i] = leet[50]
            elif a[i] == 'з' or a[i] == 'З':
                a[i] = leet[51]
            elif a[i] == 'и' or a[i] == 'И':
                a[i] = leet[52]
            elif a[i] == 'л' or a[i] == 'Л':
                a[i] = leet[53]
            elif a[i] == 'п' or a[i] == 'П':
                a[i] = leet[54]
            elif a[i] == 'ф' or a[i] == 'Ф':
                a[i] = leet[55]
            elif a[i] == 'ц' or a[i] == 'Ц':
                a[i] = leet[56]
            elif a[i] == 'ч' or a[i] == 'Ч':
                a[i] = leet[57]
            elif a[i] == 'щ' or a[i] == 'Щ':
                a[i] = leet[58]
            elif a[i] == 'ы' or a[i] == 'Ы':
                a[i] = leet[59]
            elif a[i] == 'ь' or a[i] == 'Ь':
                a[i] = leet[60]
            elif a[i] == 'ъ' or a[i] == 'Ъ':
                a[i] = leet[61]
            elif a[i] == 'э' or a[i] == 'Э':
                a[i] = leet[62]
            elif a[i] == 'ю' or a[i] == 'Ю':
                a[i] = leet[63]
            elif a[i] == 'я' or a[i] == 'Я':
                a[i] = leet[64]
    c = ''
    for i in range(0, b):
        c += a[i]
    return c

# Input:
# This verion of the project actually translates everything you type,
# but results of this kind of translations are... not that readable.

# Output:
# 7|-|15 \/3|210И 0|= 7|-|3 |°|20_/3<7 4<7|_|4|_|_Ч 7|24И5|_4735 3\/3|2Ч7|-|1И6 Ч0|_| 7Ч|°3,
# 8|_|7 |235|_||_75 0|= 7|-|15 |<1И|) 0|= 7|24И5|_4710И5 4|23... И07 7|-|47 |234|)48|_3.
