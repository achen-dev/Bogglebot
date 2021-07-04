INDEX_A = 0
INDEX_B = 25393
INDEX_C = 43787
INDEX_D = 75875
INDEX_E = 94588
INDEX_F = 108765
INDEX_G = 120639
INDEX_H = 131579
INDEX_I = 145305
INDEX_J = 158485
INDEX_K = 161319
INDEX_L = 165257
INDEX_M = 175240
INDEX_N = 195024
INDEX_O = 208467
INDEX_P = 221128
INDEX_Q = 255971
INDEX_R = 257754
INDEX_S = 274526
INDEX_T = 313265
INDEX_U = 332065
INDEX_V = 354819
INDEX_W = 360138
INDEX_X = 366683
INDEX_Y = 367183
INDEX_Z = 368317

words_file = open('words_alpha.txt', 'r')
word_lines = words_file.readlines()
cleaned_lines = []
for item in word_lines:
    cleaned_lines.append(item[:-1])
cleaned_lines.sort()
for item in cleaned_lines:
    if len(item) < 3:
        cleaned_lines.remove(item)
for i in range(1, len(cleaned_lines)):
    if cleaned_lines[i][0] != cleaned_lines[i-1][0]:
        print(cleaned_lines[i][0], i)
print(cleaned_lines[:30])

