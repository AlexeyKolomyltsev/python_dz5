# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


x = "haaabccctt"
xc = x[0]
x_rle = ""
count = 1
for i in range(1, len(x)):
    if x[i] == xc[-1]:
        count += 1
    else:
        x_rle += str(count) + xc[-1]
        xc += x[i]
        count = 1
x_rle += str(count) + xc[-1]
print(x_rle)

x_rle = '1h3a1b3c1t'
x =''
count = ''
for i in range(len(x_rle)):
    if x_rle[i].isdigit(): count += x_rle[i]
    else:
        x += int(count) * x_rle[i]
        count = ''
print(x)
