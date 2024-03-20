def distance(f, b, s):
    step = f - b
    lens = f + b
    remin = s % lens
    cycle = s // lens
    distance = lens * cycle

    if (s > distance):
        if remin <= b:
            return step * cycle - (b - remin)
        else:
            return step * cycle + remin
    else:
        return step * cycle



a = int(input()) # 앞으로
b = int(input()) # 뒤로
c = int(input()) # 앞으로 
d = int(input()) # 뒤로
s = int(input())

Nikky = distance(a, b, s)
Byron = distance(c, d, s)

if Nikky < Byron:
    print('Byron')
elif Byron < Nikky:
    print('Nikky')
else:
    print('Tied')
