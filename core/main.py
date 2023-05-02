from core.loading import *
from core.userActions import *
from core.userFeed import *

from database.main import *


def execute():
    user = userList[random.randint(0, len(userList) - 1)]
    nonLiked = getNonLiked(user, userList)
    weights = makeWeights(user, nonLiked)
    showList = toShow(userList, weights, 10)