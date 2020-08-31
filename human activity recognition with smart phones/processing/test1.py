b = ['123 abc', '456 jkb']
for a in b:
    for i in a:
        print(i)
        if i == ' ':
            c = a.replace(a[:a.index(i)+1], '')
            c = '"' + c + '"'
            break
    a.replace(a, c)
print(b)
