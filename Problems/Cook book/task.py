#  Posted from EduTools plugin
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

word: str = input()

# write a condition for plurals
if word in pasta:
    print('You can make pasta')
if word in apple_pie:
    print('You can make apple pie')
if word in ratatouille:
    print('You can make ratatouille')
if word in chocolate_cake:
    print('You can make chocolate cake')
if word in omelette:
    print('You can make omelette')
