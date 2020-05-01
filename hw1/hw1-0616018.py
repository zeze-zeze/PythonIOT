# calculate e with the spec formula
def e(epsilon = pow(0.1, 8)):
    now = 1
    floor = 1
    ans = 2
    while float(1) / floor > epsilon:
        now += 1
        floor *= now
        ans += float(1) / floor
    return ans

# find max and min for binary search
final = e(pow(10, -50))
max_ = pow(10, -1)
min_ = pow(10, -2)
while e(min_) != final:
    max_ = min_
    min_ *= 0.5

# do binary search (at most 1000 times)
times = 0
while max_ != min_:
    times += 1
    if times > 1000:
        break
    mid = (max_ + min_) / 2
    if mid != final:
        max_ = mid
    else:
        min_ = mid

# get the close epsilon
close = -1
while e(pow(10, close)) != final:
    close -= 1

print('當 epsilon = 10 ^', close+2, '時，e =', e(pow(10, close+2)))
print('當 epsilon = 10 ^', close+1, '時，e =', e(pow(10, close+1)))
print('當 epsilon <= ', max_, '時，可得最精確結果:', e(max_))
