
sen_num = 0
token_num = 0
with open('fanti.dev') as f: # , encoding='utf-16-le'
    for line in f:
        line = line.rstrip().split('  ')
        sen_num += 1
        for l in line:
            l = l.split('/')[0]
            token_num += len(l)
print(sen_num, token_num)