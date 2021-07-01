# prediction file 
with open("jianti-final/test_predictions.txt") as f:
    pred = f.readlines()

# gold file
with open("data/jianti.test") as f:
    gold = f.readlines()

rets = []
for p, g in zip(pred, gold):
    word_pred = p.strip().split()
    gold = g.strip().split()
    ret = []
    for wg in gold:
        wgg = wg.replace("\ufeff", "")
        found = False
        for w in word_pred:
            word = w.split("/")[0]
            if wgg == word:
                ret.append(wgg+"/"+w.split("/")[1])
                found = True
            elif word.startswith(wgg):
                ret.append(wgg+"/"+w.split("/")[1])
                found = True
            elif wgg.startswith(word):
                ret.append(wgg+"/"+w.split("/")[1])
                found = True

            if found:
                break
        if not found:
            ret.append(wgg + "/" + "Sy")
    rets.append("  ".join(ret))



print(rets[:10])
with open("result.txt", 'w') as f:
    for ins in rets:
        f.write(ins + '\n')