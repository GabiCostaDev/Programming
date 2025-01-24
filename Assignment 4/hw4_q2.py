"""
Your program will work is as follows:
- The user will enter a certain amount of mochiko, sugar, cornstarch, and anko in grams.
- The program will then convert those gram amounts to cups (1 cup = 220g).
- The program will then calculate how many batches of daifuku mochi can be made with this quantity of ingredients.
"""

mochiko = float(input('Enter an amount (g) of mochiko: '))
sugar = float(input('Enter an amount (g) of sugar: '))
cornstarch = float(input('Enter an amount (g) of cornstarch: '))
anko = float(input('Enter an amount (g) of anko: '))

mochiko_cups = mochiko/220
sugar_cups = sugar/220
cornstarch_cups = cornstarch/220
anko_cups = anko/220

mochiko = mochiko_cups - (mochiko_cups % 3)
sugar = sugar_cups - (sugar_cups % 1.5)
cornstarch = cornstarch_cups - (cornstarch_cups % 2)
anko = anko_cups - (anko_cups % 1)

if mochiko < sugar and mochiko < cornstarch and mochiko < anko:
    number_of_batches = int(mochiko/3)
    print('With this amount of ingredients, you can make', number_of_batches, 'batch(es) of 24 mochi.')
elif sugar < mochiko and sugar < cornstarch and sugar < anko:
    number_of_batches = int(sugar/3)
    print('With this amount of ingredients, you can make', number_of_batches, 'batch(es) of 24 mochi.')
elif cornstarch < mochiko and cornstarch < sugar and cornstarch < anko:
    number_of_batches = int(cornstarch/3)
    print('With this amount of ingredients, you can make', number_of_batches, 'batch(es) of 24 mochi.')
else:
    number_of_batches = int(anko/3)
    print('With this amount of ingredients, you can make', number_of_batches, 'batch(es) of 24 mochi.')

