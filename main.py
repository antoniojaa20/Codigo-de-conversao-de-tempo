s = int(input())
h = s / 3600
sr = s % 3600
m = sr/60
sr2 = sr % 60
print('{}:{}:{}'.format(int(h),int(m),sr2))
