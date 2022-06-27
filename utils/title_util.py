import random

# this function generates a random title (too cringe)
def title_selector():
       nouns = ['house', 'car', 'bike', 'plane']  # use your content related nouns, adjectives and ends!
       adjectives = ['big', 'small', 'Beautiful', 'Gorgeous']
       end = [' flying', ' | Something', '... Watch till end']
       return random.choice(adjectives)+' '+ random.choice(nouns) + random.choice(end)

