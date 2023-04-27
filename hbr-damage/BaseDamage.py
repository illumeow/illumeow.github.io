from math import ceil

border = int(input("border: "))
STR = int(input("力量: "))
DEX = int(input("靈巧: "))
weight = int(input("對HP: 1/ 對DP: 2/ 皆無: 3\n"))
power = (STR*(3-weight) + DEX*weight)/3 if weight!= 3 else (STR+DEX)/2

target = int(input("單體: 1/ 全體: 2\n"))
SP = int(input("模SP: "))
skill_lvl = int(input("技能等級: "))
if target%2:  # 單體
    minPow = (162 + 12*(SP**2 - 1))*(1 + (skill_lvl - 1)*0.05)
    maxPow = (810 + 60*(SP**2 - 1))*(1 + (skill_lvl - 1)*0.02)
else:   # 全體
    minPow = (159 + 9*(SP**2 - 1))*(1 + (skill_lvl - 1)*0.05)
    maxPow = (795 + 45*(SP**2 - 1))*(1 + (skill_lvl - 1)*0.02)
minPow = ceil(minPow)
maxPow = ceil(maxPow)

SD = ceil(105+3*SP)

critical = input("暴擊: y/n\n")
if critical == 'y':    border -= 50

#basedmg = max(minPow*min(SD/2+diff, SD/2)/(SD/2) + (maxPow-minPow)*max(min(diff/SD, 1), 0), 1)
basedmg = 1
power = 366.7
if (border+SD) <= power:
    print('first')
    basedmg = maxPow
elif border <= power:
    print('second')
    print(f'(({maxPow}-{minPow})*({power}-{border}))/{SD} + {minPow}')
    basedmg = ((maxPow-minPow)*(power-border))/SD + minPow
elif (border-(SD/2)) < power:
    print('third')
    basedmg = (minPow/(SD/2))*(power-(border-(SD/2)))

print(basedmg)
