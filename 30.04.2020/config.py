#from win32api import GetSystemMetrics

#x =GetSystemMetrics(0)
#y = GetSystemMetrics(1)

### SCREEN
screen = dict(
    width = 800,
    height = 600,
)

### PYGAME DATA
delay = 1000
FPS = 60
font = dict(
    smallSize = 30,
    smallFamily = "calibri",
    mediumSize = 50,
    mediumFamily = "calibri",
    bigSize = 80,
    bigFamily = "calibri",
)
### FOOD

food = dict(
    startingFoodCount = 5,
    freshness = 10,
    rottingPeace = 1
)


animalsBeggining = dict(
    startingPeacocksCount=10,
    startingTigersCount=10
)

peacocks = dict(
    maxCount = 1000,
    minHungerPeace = 1,
    maxHungerPeace = 5,
    minHunger = 0,
    maxHunger = 100,
    eatingPoints = 5,
    moveCost = 1,
    startingHunger = 50,
    hungerPoint = 50,
    minWeight = 3,
    maxWeight = 6,
    avgSpeed = 16,
    fertilityLvl = 70,
    fertilityCost = 15,
    minEggCount = 1,
    maxEggCount = 4,

)

tigers = dict(
    maxCount = 1000,
    minHungerPeace = 1,
    maxHungerPeace = 5,
    minHunger = 0,
    maxHunger = 100,
    eatingPoints = 10,
    moveCost = 2,
    startingHunger = 50,
    hungerPoint = 50,
    minWeight = 65,
    maxWeight = 300,
    avgSpeed = 25,
    fertilityLvl = 70,
    fertilityCost = 20,
    minCubCount = 1,
    maxCubCount = 2
)
