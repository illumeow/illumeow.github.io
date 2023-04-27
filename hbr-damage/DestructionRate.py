# formula: (self_DR)*(enemy_DR)*(pierce_bonus)
# pierce_bonus: 5 + (hit_count-1)*((pierce%-5)/9)%

pierce = int(input("破壞率耳環 +?% : 10/12/15\n"))
hit = int(input("技能 ? hit\n"))
pierce_bonus = 5+(hit-1)*((pierce-5)/9)
print(pierce_bonus)
contnue = input("continue? y/n\n")
if contnue == 'y':
    self_DR = float(input("自身破壞係數 :\n"))
    enemy_DR = float(input("敵方破壞係數 :\n"))
    print(self_DR*enemy_DR*(1+pierce_bonus/100))