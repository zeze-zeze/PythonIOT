#coding=utf-8
import string
import sys

def notid(err):
    print('不合格的身份證字號 - {}\n'.format(err))
    sys.exit(0)

uid = input('輸入身分證字號: ')
if len(uid) != 10:
    notid('長短不對')
elif uid[0] not in string.printable[36:62]:
    notid('首碼須為大寫英文字母')
elif not uid[1:].isnumeric():
    notid('後面九碼須為數字')
elif uid[1] != '1' and uid[1] != '2':
    notid('次碼須為 1(男) 或 2(女)')

trans = {'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16', 'H':'17', 'I':'34', 'J':'18', 'K':'19', 'L':'20', 'M':'21', 'N':'22', 'O':'35', 'P':'23', 'Q':'24', 'R':'25', 'S':'26', 'T':'27', 'U':'28', 'V':'29', 'W':'32', 'X':'30', 'Y':'31', 'Z':'33'}
weight = '1 9 8 7 6 5 4 3 2 1 1'.split(' ')

uid = trans[uid[0]] + uid[1:]

assert len(uid) == len(weight)

res = 0
for i, j in zip(uid, weight):
    res += int(i) * int(j)

if res % 10 == 0:
    print('合格的身分證字號')
else:
    notid('總和未整除 10')
