

all_types = set()
with open('fanti', encoding='utf-16-le') as f:
    for line in f:
        if line == '\n':
            continue
        line = line.rstrip().split('  ')
        types = set()
        for l in line:
            types.add(l.split('/')[1])
        all_types = all_types | types
print(all_types)
print(len(all_types))

with open('fanti.meta', 'w') as f:
    for t in all_types:
        f.write('B-{}\nI-{}\n'.format(t, t))

