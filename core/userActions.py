from core.loading import *

# Swipe functions, calculate the Expected Score of the Swiped
# Consider a win if it was Swiped Right and a Lose if it was Swiped Left
# Then, if Swiped Right, add the Swiped to the like list of the Swiper
def swipeRight(swiper, swiped):
    swipedExpectedScore = 1 / (1 + pow(10, (swiper.elo - swiped.elo) / 400))
    swipedScoreIncrement = round(8 * (1 - swipedExpectedScore))
    swiped.elo = swiped.elo + swipedScoreIncrement
    if swiped not in swiper.likes:
        swiper.likes.append(swiped)
    else:
        swiper.likes.remove(swiped)
        swiper.likes.append(swiped)

def swipeLeft(swiper, swiped):
    swipedExpectedScore = 1 / (1 + pow(10, (swiper.elo - swiped.elo) / 400))
    swipedScoreIncrement = round(8 * (0 - swipedExpectedScore))
    swiped.elo = swiped.elo + swipedScoreIncrement