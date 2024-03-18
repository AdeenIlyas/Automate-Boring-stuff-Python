import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_outcomes = []
    for _ in range(100):
      flip_coin = random.randint(0,1)
      if flip_coin == 1:
        coin_outcomes.append("H")
      else:
        coin_outcomes.append("T")

    for i in range (len(coin_outcomes)):
      if coin_outcomes[i:i+6] == ["H"]*6:
        numberOfStreaks +=1
        break
      
      elif coin_outcomes[i:i+7] == ["T"] *6:
        numberOfStreaks +=1 
        break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))