from collections import namedtuple
total_rec, scores, total = int(input()), namedtuple('scores',input().split()), 0 
for i in range(total_rec): 
    access = scores(*input().split())
    total += int(access.MARKS)
print('%.2f' % float(total/total_rec))
