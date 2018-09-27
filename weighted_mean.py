no_val, score, weight, tot = int(input()), input().split(), input().split(), 0
for i in range(no_val): tot = (tot + (int(score[i])*int(weight[i]))) 
print('%.1f' % float(tot/sum(map(int,weight))))