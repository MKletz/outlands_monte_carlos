import random

class Debuff:
    def __init__(self, name, swingsRemaining):
        self.name = name
        self.swingsRemaining = swingsRemaining

    def reduceSwing(self):
        self.swingsRemaining = (self.swingsRemaining - 1)

class Armor:
    def __init__(self, Armor):
        self.BaseArmor = Armor
        self.EffectiveArmor = Armor
    
    def getMinimumReduction(self):
        MinReduction = (.333 * self.EffectiveArmor)
        return MinReduction

    def getMaximumReduction(self):
        MaxReduction = (.666 * self.EffectiveArmor)
        return MaxReduction

    def getReductionPercentage(self):
        MinReduction = self.getMaximumReduction()
        MaxReduction = self.getMaximumReduction()
        ActualReduction = random.uniform(MinReduction,MaxReduction)
        ActualReduction = round(ActualReduction,1) / 100
        return ActualReduction
    
    def reduceEffectiveArmor(self, reductionAmount):
        self.EffectiveArmor = (self.EffectiveArmor - reductionAmount)

    def resetEffectiveArmor(self):
        self.EffectiveArmor = self.BaseArmor

class Damage:
    def __init__(self, minimumDamage, maximumDamage):
        self.MinimumDamage = minimumDamage
        self.MaximumDamage = maximumDamage

    def getBaseDamage(self):
        BaseDamage = random.randrange(self.MinimumDamage ,self.MaximumDamage)
        return BaseDamage

    def getFinalDamage(self, armor, damageModifier):
        damage = self.getBaseDamage()
        damage = (damage * damageModifier)
        reductionPercentage = armor.getReductionPercentage()
        damage = (damage - (damage * reductionPercentage))
        return damage