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

    
# augmentation for jianti
all_data = []
cur_num = 0
with open('jianti', encoding='utf-16-le') as f:
    data = []
    for line in f:
        if line == '\n':
            all_data.append(data)
            data = []
        else:
            data.append(line.rstrip())
            cur_num += 1
            if cur_num > train_num:
                break
all_data.append(data)
print(len(all_data), cur_num)

with open('jianti.train.aug', 'w') as f:
    for data in all_data:
        sent_len = []
        for line in data:
            line = line.rstrip().split('  ')
            slen = 0
            for l in line:
                l = l.split('/')[0]
                slen += len(l)
            sent_len.append(slen)
        
        for window in range(1, len(data)+1):
            for i in range(len(data)-window+1):
                cur_len = sum(sent_len[i:i+window])
                if window == 0 or cur_len < 400:
                    cur_data = '  '.join(data[i:i+window])
                    f.write(cur_data+'\n')
