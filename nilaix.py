#Program menentukan nilai f(x) dengan array
nilai_x=list(range(-7,8))
f=[]
print("|   x  |   f(x)  |")
print("|------|---------|")
for x in nilai_x:
    if x>0:
        f.append(x**3-x)
    elif x<0:
        f.append(round(1/x**2,3))
    else:
        f.append(1)

for i in range(len(nilai_x)):
    print(f"|{nilai_x[i]:5} | {f[i] : 7} |")
