from core.loading import *

def getNonLiked(user, userList):
    nonLiked = userList
    for person in user.likes:
        if person in nonLiked:
            nonLiked.remove(person)
    return nonLiked

def makeWeights(user, nonLiked):
    nonLikedWeights = []
    for personShow in nonLiked:
        weight = 1
        for personLiked in user.likes:
            if personShow in personLiked.likes:
                weight = weight + 1
        weight = weight + round(personShow.elo / 1000)
        nonLikedWeights.append(weight)
    return nonLikedWeights

def toShow(nonLiked, nonLikedWeights, amount):
    show = random.choices(nonLiked, weights = nonLikedWeights, k = amount)
    return show