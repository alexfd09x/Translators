def coder(a, z, y):
    b = len(a)
    d = len(z)
    a = list(a)
    c = []
    for ii in range(b):
        for i in range(d):
            if a[ii] == z[i]:
                c.append(y[i])
    g = ''.join(c)
    return g
