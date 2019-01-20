class Ability:
    def __init__(self,name,style,effect,info,myDict,cost):
        self.name = name
        self.style = style
        self.effect = effect
        self.info = info
        self.dict = myDict
        self.cost = cost
        self.status = "LOCKED"

    def toString(self):
        print("Skill Name:",self.name)
        print("Style:",self.style)
        print("Effect:",self.effect)
        print("Info:",self.info)
        print("Furor Cost:",self.cost)
        print("Status:",self.status)

    #getters
    def getName(self):
        return self.name
    def getEffect(self):
        return self.effect
    def getStyle(self):
        return self.style
    def getInfo(self):
        return self.info
    def getDict(self):
        return self.dict
    def getCost(self):
        return self.cost
    def getStatus(self):
        return self.status

    #setters
    def setStlye(self,value):
        self.style = value
    def setCost(self,value):
        self.cost = value
    def setDict(self,value):
        self.dict = value
    def Unlock(self,value):
        self.status = "UNLOCKED"

#ASSASSIN
throwing_knives = Ability("Throwing Knives","Super","Super Attack,Debuff,Unique","Throw knives at the enemy [10]. Each knife that hits dealing percantage of power damage and flat reduction to enemy defense",{"H":0,"F":0,"P":.25,"D":-5,"S":0,"C":0},100)
poison_daggers = Ability("Poisoned Daggers","Super","Super Attack,Debuff,Unique","Coat daggers in poison dealing percentage damage to enemy and chance to poison enemy",{"H":0,"F":0,"P":.75,"D":0,"S":0,"C":0},150)
shredder = Ability("Shredder","Super","Debuff","Apply supericial cuts to the enemy,reducing defense",{"H":0,"F":0,"P":0,"D":-.10,"S":0,"C":0},200)
shroud = Ability("Shroud","Super","Buff","Cloak youself in a veil of darkness,boosting defense",{"H":0,"F":0,"P":0,"D":.15,"S":0,"C":0},200)

shadow_step = Ability("Shadow Step","Super","Super Attack,Unique","Merge into the shadows,immune to the enemy's attack and retaliate",{"H":0,"F":0,"P":1.75,"D":0,"S":0,"C":0},350)
invisibile = Ability("Invisibility","Super","Debuff,Unique","Hide among the shadows,invisble and immune to damage, your next attack applies bleed to the enemy",{"H":0,"F":0,"P":0,"D":0,"S":0,"C":0},250)
vengeful_strike = Ability("Vengeful Strike","Super","Super Attack,Unique","Deal a deathly strike in the enemy's chest based on health missing",{"H":0,"F":0,"P":0,"D":0,"S":0,"C":0},300)

behind_you = Ability("BEHIND YOU!","Ultimate","Super Attack,Unique","Teleport behind the target and deliver a powerful strike, chane to execute if target's health below threshold",{"H":0,"F":0,"P":2.25,"D":0,"S":0,"C":0},500)
last_breath = Ability("Last Breath","Ultimate","Super Attack,Debuff,Unique","Hurl your dagger at the oppnent, grazing them and applying a special poison, each turn the enemy takes percentage of max health as damage and percentage reduction to defense [4 turns]",{"H":0,"F":0,"P":1.25,"D":-.15,"S":0,"C":0},500)
die = Ability("YOU WILL DIE BY MY HANDS!","Ultimate","Super Attack,Buff,Unique","Sacrifice all defense and furor adding them to your power as a boost for the remainder of the battle, and perform a regular attack.",{"H":0,"F":0,"P":0,"D":0,"S":0,"C":0},400)

#ARCHER
steady_aim = Ability("Steady Aim","Super","Buff","Gives a slight shred boost",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},200)
poison_arrows = Ability("Poison Arrows","Super","Super Attack,Unique","A regular arrow tipped with poison",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},300)
cripple_shot = Ability("Crippling Shot","Super","Super Attack,Debuff,Unique","A regular arrow strung with great strength leaving the target's defenses weakened",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)
hunter_vision = Ability("Hunter's Vision","Super","Buff,Unique","Gains a hunter's enhanced vision allowing you to see points of weakness on the target,next attack will crit",{"H":0,"F":0,"P":0,"D":-.1,"S":0,"C":0},350)

double_shot = Ability("Double Shot","Super","Super Attack,Debuff,Unique","Shoot two arrows at the enemy dealing 150% power as damage",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
true_shot = Ability("True Shot","Super","Super Attack,Unique","A steel tipped arrow strung with great strength dealing true damage to the target",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
hunters_blessing = Ability("Hunter's Blessing","Super","Super Attack,Buff","A prayers to the huntress blesses you with a boost to power,shred and defense",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

the_hunt = Ability("The Hunt","Ultimate","Super Attack,Unique","A prayer to the huntress blesses your bow allowing susequent attacks until an arrow misses",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
orbital_shot = Ability("Orbital Shot","Ultimate","Super Attack,Unique","Leap into the air and shoot and arrow to the target's location, dealing more damge at longer distances",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
cobra_kiss = Ability("Cobra's Kiss","Ultimate","Super Attack,Unique","Use your toxic blowpipe and hurl a dart at the target poisoning them with special poison leaving them unable to attack for two turns",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

#Dragonfiend TREE

flame_blast = Ability("Flame Blast","Super","Super Attack,Unique","Blast the target with a sphere of flames, chance to burn the target",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},200)
tail_smash = Ability("Tail Smash","Super","Super Attack,Unique","Lash your tail at the target dealing boosted damage and ignoring some of the target's protections",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},300)
quick_fang = Ability("Quick Fang","Super","Super Attack,Debuff,Unique","Dash at the enemy and sink your fang into them weaking their defenses.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)
roar = Ability("Roar","Super","Super Attack,Buff,Debuff,Unique","Let out a piercing roar boosting your power and weaking the target's defenses",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)

omega_eraser = Ability("Omega Eraser","Super","Super Attack,Debuff,Unique","A charged ability, after second turn of charging attack is released dealing 2.5 times damage, after third turn attack is realeased dealing 4 times damage",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
dragon_rush = Ability("Dragon Rush","Super","Super Attack,Unique","Fly into the air skipping eneimies attack and come crashing down dealing damage and reducing their defense ",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
dragon_dance = Ability("Dragon Dance","Super","Super Attack,Buff","A sacred dance that boosts power and penetration",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

quasar = Ability("Quasar","Ultimate","Super Attack,Unique","Fire a stream of beam projectiles (max. 3). Each beam projectile that hits the enemy does damage and decreases enemy defense and boosts power follow by ascending into the sky before charing and releasing a catastrophic quasar blast at the opponent.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
hellkite_blast = Ability("Hellkite Blast","Super","Super Attack,Unique","Wield the power of black flames and launch a sphere for fire at the opponent burning them and applying Hellkite Burn as well.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
end = Ability("E.N.D.","Super","Super Attack,Unique","Mark your target before flying miles into the air and releasing a blast from the sky, the further the distance flown the higher the damage",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

#Samurai TREE

meditate = Ability("Meditate","Super","Buff","Focus your mind, increase your temporary power and defense by 10%",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},200)
driving_strike = Ability("Driving Strike","Super","Super Attack,Unique","A single decisive attack inflicts 110% power that ignores 75% of the enemies defense",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},300)
thousand_blade_dance = Ability("Thousand Blade Dance","Super","Super Attack,Debuff,Unique","A multi strike technique that inflicts 150% damage and boosts temporay power by 5%",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)
dodge_roll = Ability("Dodge Roll","Super","Super Attack,Buff,Debuff,Unique","Chance to avoid enemy attack and counter with 50% power as true damage, if sucessful you gain 10% of your defense as temporay defense",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)

seppuku = Ability("Seppuku","Super","Super Attack,Unique","You perform a powerful ritual and stab yourself with your sword in return you gain 25% temporary power, defense, penetration and 25% of max esseence",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
tenshino = Ability("Tenshino","Super","Super Attack,Unique","Slice a wave of magical energy at the enmey dealing 200% power damage, chance to use attack again",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
d_stance = Ability("Defensive Stance","Super","Buff","Switch to a defensive style of fighting style",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

retribution = Ability("Retribution","Ultimate","Super Attack,Unique","Awaits the enemy's attack and attempt to parry the oncoming attack, if succcesful the knock the enemy to the ground and thrusts your blade through the enemy's chest, inflicting critical TRUE damage to the enemy and leaves them in a bleeding state. If failed,releases a moderately damaging attack, but still receives the enemy's attack.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
change_stance = Ability("Change Stance","Ultimate","Unique","Allows a change of stance to a purely aggressive or purely defensive fighting style. AGGR: Gain 30% power and 15% shred and lose 40% defense. DEF: Gain 45% defense and 20% health back lose 35% power and 20% shred",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
senbonsakura = Ability("Senbonsakura","Ultimate","Super Attack,Unique","Let your katana fade in the wind and delevier countless stikes to the enemy leaving them bleeding",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

#Titan TREE

warcry = Ability("Warcry","Super","Buff","Let our a cry and bolster your power by 10%",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},200)
overhead_smash = Ability("Overhead Smash","Super","Super Attack,Unique","Raise your greatsword above and slam it down upon your enemy, dealing 120% power as damage",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},300)
uppercut = Ability("Uppercut","Super","Super Attack,Debuff,Unique","Drag your sword across the ground and upward slash the enemy dealing 90% damage and increase temporary power by 10%",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)
crush_blow = Ability("Dodge Toll","Super","Super Attack,Buff,Debuff,Unique","Swing your sword with great force crushing the enemies defenses dealing 90% damage, reducing them by 15%",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)

blowback = Ability("Blowback","Super","Super Attack,Unique","Strike down the enemy dealing 120% power, there is a chance you will knock the oppenent down, skipping their attack phase",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
spin = Ability("Spin","Super","Super Attack,Unique","As the enemy attack, charge and perform a spinning strike avoidng their attack and dealing 80% damage",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
warriors_blessing = Ability("Warrior's Blessing","Super","Buff","Gain 10% temporary power,defense,penetration and 15% of max health",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

rampage = Ability("Rampage","Ultimate","Super Attack,Unique","Impale your sword into the ground, causing a shockwave. The shockwave damages and staggers the opponent, allowing a forward dash into an upward slash knocking the enemy into the air. Jump into the air above the enemy and come  crashing down at the targets location. Gain health back based on the amount of damage done.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
outrage = Ability("Outrage","Ultimate","Unique","Wield your greatsword and shortsword at once unleashing consecutive blows on the enemy, each blow boosts your power by 2%",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
juggernaut = Ability("Juggernaut","Ultimate","Super Attack,Unique","All damage taken it reduce by 50% and if health should reach 0 it is left at 1 [3 turns]",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

#Tempest TREE

storm_call = Ability("Storm Call","Super","Buff","Storm meter gains 50% capacity",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},200)
wind_scythe = Ability("Wind Scythe","Super","Super Attack,Unique","Conjure a scythe of winds and strike your enemy, you gain health equal to damage done (Leaves 1 air counter on target). At full storm meter this ability does double damage",{"H":0,"F":0,"P":0,"D":0,"S":.1,"C":0},300)
wind_devour = Ability("Wind Devour","Super","Super Attack,Debuff,Unique","Reduce storm meter by 50%, in exchange gain 25% health back and boost power,defense and shred by 5%",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)
glide = Ability("Glide","Super","Super Attack,Buff,Debuff,Unique","Chance to evade enemy's attack and couner. At full storm meter chance is certain.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},300)

storm_callx = Ability("I AM THE STORM!","Super","Super Attack,Unique","Ascend into the air and dive at the enemu cloaking yourself in winds (Leaves 3 air counters on target). At max Storm Meter this attack does true damage and you gain 100% Storm Meter",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
blow_away = Ability("I'LL BLOW YOU AWAY!","Super","Super Attack,Unique","Flap your wings releasing a gust of wind knocking the enemy into the air and unable to attack! At full storm meter enemy's defense is cut in half.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
howling_winds = Ability("Howling Winds","Super","Buff","Call forth a strorm of winds, for the next [5 turns] all abilities deal more damage and your storm meter does not diminish at all (Leaves 1 air counter on target each turn, 2 if at max furror upon cast). Gain 5% power,shred and defense each turn. At max Storm Meter gain 10% health and furror back each turn as well",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

rampage = Ability("Rampage","Emit a rampage of furious winds from your body, blasting the enemy into the air reducing power, defense letting the enemy plummet to the ground. The whirlwind boosts power and defense equal to that lost by the enemy. The whirlwind also restores health and furor based on damage done. At max Storm Meter, the attack continues by diving at the enemy, dealing damage and leaving them unable to attack.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
air_combat = Ability("Air Combat","Ultimate","Unique","Launch the enemy into the air with a blast of wind and release [air counter] close combat attacks on the enemy. At max Storm Meter number of attacks is doubled.",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)
siphon = Ability("Siphon","Ultimate","Super Attack,Unique","For each air counter on the enemy, they lose 5% of their max health,",{"H":0,"F":0,"P":0,"D":-.1,"S":.1,"C":0},350)

