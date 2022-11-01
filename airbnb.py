import math
with open('travelers.txt') as t:
    traveler = {a.strip(): idx for idx, a in enumerate(t.readlines())}

with open('days.txt') as d:
    days = {a: idx for idx, a in enumerate(d.readlines())}


with open('mat2.txt') as mat:
    m = [[int(i.strip()) for i in line.split(' ')] for line in mat.readlines()]

TOTAL = 21542

NIGHTS = len(days)-1
NIGHT_PRICE = TOTAL/NIGHTS
print(m)
print(days.items())


def enterdays(name, arr, dep):
    n = traveler[name]
    for r in range(days[dep] - days[arr]):
        m[n][r] = 1

def calc_ppd():
    peoplepd = [0] * NIGHTS
    for d in range(NIGHTS):
        for n in range(len(traveler)):
            if m[n][d]:
                peoplepd[d] += 1
    return peoplepd


def calc_my_price(name, pricepdb):
    n = traveler[name]
    sum = 0
    for day in range(NIGHTS):
        if m[n][day]:
            sum += pricepdb[day]
    return sum


peoplepd = calc_ppd()
print(peoplepd)
print(traveler)


pricepd = [NIGHT_PRICE / nbrp for nbrp in peoplepd]
print(pricepd)

def calc_night(pricepd):

    res = {name: math.ceil(calc_my_price(name, pricepd)) for name in traveler}

    for name, price in res.items():
        print(f'{name} {price}')

    print(sum(res.values()))
    return res

res = calc_night(pricepd)


def calc_man_nights(peoplepd):
    man_nights = sum(peoplepd)
    nightp = TOTAL/man_nights
    return [nightp] * 7

print(calc_man_nights(peoplepd))
res = calc_night(calc_man_nights(peoplepd))

with open('airbnb_res.txt', 'w') as f:
    for name, price in res.items():
        f.write(f'{name} {price}\n')


