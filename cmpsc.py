ftravs = [[111, 323, 279],
          [312, 235, 69],
          [411, 141, 131]]

s_Pio = [750, 580, 480]
s_Ajo = [722, 786, 302]

############
s_Pic = []
for item in ftravs:
    s_Pic.append(sum(item))

print("Produced, ", sum(s_Pic))
print(s_Pic)

# transpose and get the attracted travels
ftravs_tt = list(zip(*ftravs))
print("Transpose, ", ftravs_tt)

s_Ajc = []
for item in ftravs_tt:
    s_Ajc.append(sum(item))

print("Attracted, ", sum(s_Ajc))
print(s_Ajc)

ccsi = []
for po, pc in zip(s_Pio, s_Pic):
    ccsi.append(round(po / pc, 3))

print("Coeffs i after first pass, ", ccsi)

for i in range(len(ftravs)):
    ftravs[i] = [ccsi[i]*item for item in ftravs[i]]


print("Matrix after first pass, ", ftravs)



##############
s_Pic = []
for item in ftravs:
    s_Pic.append(sum(item))

print("Produced after first pass, ", sum(s_Pic))
print(s_Pic)

# transpose and get the attracted travels
ftravs_tt = list(zip(*ftravs))
print("Transpose after first pass, ", ftravs_tt)

s_Ajc = []
for item in ftravs_tt:
    s_Ajc.append(sum(item))

print("Attracted after first pass, ", sum(s_Ajc))
print(s_Ajc)

ccsj = []
for ao, ac in zip(s_Ajo, s_Ajc):
    ccsj.append(round(ao / ac, 3))

print("Coeffs j after first pass, ", ccsj)

for i in range(len(ftravs)):
    ftravs_tt[i] = [ccsj[i]*item for item in ftravs_tt[i]]


ftravs = list(zip(*ftravs_tt))
print("Matrix after pass, ", ftravs)



############
s_Pic = []
for item in ftravs:
    s_Pic.append(sum(item))

print("Produced 2, ", sum(s_Pic))
print(s_Pic)

# transpose and get the attracted travels
ftravs_tt = list(zip(*ftravs))
print("Transpose 2, ", ftravs_tt)

s_Ajc = []
for item in ftravs_tt:
    s_Ajc.append(sum(item))

print("Attracted 2, ", sum(s_Ajc))
print(s_Ajc)

ccsi = []
for po, pc in zip(s_Pio, s_Pic):
    ccsi.append(round(po / pc, 3))

print("Coeffs i after first pass, ", ccsi)

for i in range(len(ftravs)):
    ftravs[i] = [ccsi[i]*item for item in ftravs[i]]


print("Matrix after first pass, ", ftravs)



##############
s_Pic = []
for item in ftravs:
    s_Pic.append(sum(item))

print("Produced after first pass, ", sum(s_Pic))
print(s_Pic)

# transpose and get the attracted travels
ftravs_tt = list(zip(*ftravs))
print("Transpose after first pass, ", ftravs_tt)

s_Ajc = []
for item in ftravs_tt:
    s_Ajc.append(sum(item))

print("Attracted after first pass, ", sum(s_Ajc))
print(s_Ajc)

ccsj = []
for ao, ac in zip(s_Ajo, s_Ajc):
    ccsj.append(round(ao / ac, 3))

print("Coeffs j after first pass, ", ccsj)

for i in range(len(ftravs)):
    ftravs_tt[i] = [ccsj[i]*item for item in ftravs_tt[i]]


ftravs = list(zip(*ftravs_tt))
print("Matrix after pass, ", ftravs)

fm = [[125, 420, 205],
      [288, 250, 42],
      [309, 116, 55]]

for item in fm:
    print(sum(item))

fm_tt = list(zip(*fm))

for item in fm_tt:
    print(sum(item))

