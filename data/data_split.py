import math

all_data = []
with open('jianti', encoding='utf-16-le') as f:
    for line in f:
        if line == '\n':
            continue
        all_data.append(line)

total = len(all_data)
train_num = math.ceil(total*0.7)
dev_num = total - train_num
print(train_num, dev_num)

with open('jianti.train', 'w') as f:
    for line in all_data[:train_num]:
        f.write(line)
with open('jianti.dev', 'w') as f:
    for line in all_data[train_num:]:
        f.write(line)