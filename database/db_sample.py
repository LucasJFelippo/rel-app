from core.loading import *
from database.person import *
from core.userActions import *

# Generate random data for testing
userList = []
for i in range(100):
    userList.append(Person(random.randint(0,10000), "Test " + str(i), random.randint(18, 60), random.randint(800, 1200)))

for person in userList:
    for i in range(random.randint(0, 20)):
        randPerson = userList[random.randint(0, len(userList) - 1)]
        swipeRight(person, randPerson)