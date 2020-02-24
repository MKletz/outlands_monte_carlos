import random

class Debuff:
  def __init__(self, SwingsRemaining):
    self.SwingsRemaining = SwingsRemaining

Armor = 100
SpecialChance = 18
DamageMin = 28
DamageMax = 94
#SpecialChance = 20
#DamageMin = 27
#DamageMax = 90
SwingSpeed = 2.77
debuffTimer = 16

hitsPerDeuff = debuffTimer / SwingSpeed
hitsPerDeuff = round(hitsPerDeuff,0)

Results = []
Debuffs = []

for swing in range(1,1000):
    EffectiveArmor = Armor
    BaseDamage = random.randrange(DamageMin,DamageMax)
    isSpecial = random.randrange(1,100) <= SpecialChance

    if isSpecial == True:
        BaseDamage = BaseDamage * 1.5
        Debuffs.append(hitsPerDeuff)

    for Debuff in range(len(Debuffs)):
        if EffectiveArmor > 0:
            EffectiveArmor = EffectiveArmor - 50
        Debuffs[Debuff] = Debuffs[Debuff] - 1
    
    if isSpecial == True and EffectiveArmor < 0:
        BaseDamage = BaseDamage * (1 + (EffectiveArmor * -1)/100)

    if EffectiveArmor > 0:
        MinReduc = (.333 * EffectiveArmor) 
        MaxReduc = (.666 * EffectiveArmor)
        ActualReduc = random.uniform(MinReduc,MaxReduc)
        ActualReduc = round(ActualReduc,1) / 100
        DamageDelt = BaseDamage - (BaseDamage * ActualReduc)
    else:
        DamageDelt = BaseDamage

    DamageDelt = round(DamageDelt,0)
    Results.append(DamageDelt)

    while 0 in Debuffs:
        Debuffs.remove(0)

average = sum(Results)/len(Results)
average = round(average,0)
print(average)