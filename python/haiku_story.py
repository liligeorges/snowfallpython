from random import *

adj = ["cool", "amazing", "interesting", "borish", "difficult", "gamy", "jazzy", "macabre", "quizzical", "whimsical", "taboo", "zazzy", "maniacal", "fierce", "fragrant", "defiant", "cumbersome", "berserk", "rotten", "sore", "gigantic", "creepy", "evil", "addicting"]
items = ["Ipod Nano", "MacBook", "video game", "watch", "stereo", "app"]
verb = ["soothed", "shouted at", "followed", "jabbed", "tumbled", "floated", "affirmed", "suggested", "condensed", "created", "cut", "deleted", "flicked", "hijacked", "licked", "mimicked", "nagged", "pinched", "pounced on", "pummeled", "recorded", "repelled", "scolded"]
famousPeep = ["Donald Trump", "Britney Spears", "Beyonce", "Dory", "Kim Kardashian", "Drake", "Barack Obama", "Justin Bieber", "Madonna", "Jay Z", "Elvis", "Bill Clinton", "Bill Gates", "Oprah", "Adele", "Michael Jackson", "David Beckham", "Shakira"]

lenAdj = len(adj)
lenItems = len(items)
lenVerb = len(verb)
lenFamousPeep = len(famousPeep)

randomAdj = randint(0, lenAdj-1)
randomItems = randint(0, lenItems-1)
randomVerb = randint(0, lenVerb-1)
randomPerson = randint(0, lenFamousPeep-1)


print("There was a girl.")
print("She was a coder.")
print("She coded the " + adj[randomAdj] + " " + items[randomItems] + " that " + verb[randomVerb] + " " + famousPeep[randomPerson] + ".")

