from random import *

print("Please enter a number 1-10:")

# Populate the initial deck order from user input.
# For simplification the initial order is always from 0 to 9.

decksize = int(input())
if decksize < 1 or decksize > 10:
    print ("Wrong input!")
    exit()

initial_deck = ""
for i in range(decksize):
    initial_deck = initial_deck + str(i)

# Initial variables.
# The deck starts on stack 1.
shuffling = True
stack1 = initial_deck
stack2 = ""
stack3 = ""

'''
The algorithm:
 For every card in stack 1, top to bottom, I toss a coin:
    heads, card goes to stack 2, tails, card goes to stack 3.
When deck 1 is depleted this way, I go to stack 2, and repeat the process:
    heads, card goes to stack 3, tails, card goes to stack 1.
Then I do this for stack 3 as well:
    heads goes to stack 1 and tails goes to stack 2.
Then I cycle back to stack 1, and go through the cards there again with the same priority as before:
    heads to 2, tails to 3.
I do this until all cards end up on a single stack again, and their ordering on this stack is the new ordering.
'''

while shuffling:
    while len(stack1) != 0:
        x = getrandbits(1)
        if x == 0:
            stack2 = stack2 + stack1[-1]
            stack1 = stack1[:-1]
        if x == 1:
            stack3 = stack3 + stack1[-1]
            stack1 = stack1[:-1]

    if len(stack2) == 0 or len(stack3) == 0:
        shuffling = False
        break

    while len(stack2) != 0:
        x = getrandbits(1)
        if x == 0:
            stack3 = stack3 + stack2[-1]
            stack2 = stack2[:-1]
        if x == 1:
            stack1 = stack1 + stack2[-1]
            stack2 = stack2[:-1]

    if len(stack3) == 0 or len(stack2) == 0:
        shuffling = False
        break

    while len(stack3) != 0:
        x = getrandbits(1)
        if x == 0:
            stack1 = stack1 + stack3[-1]
            stack3 = stack3[:-1]
        if x == 1:
            stack2 = stack2 + stack3[-1]
            stack3 = stack3[:-1]

    if len(stack1) == 0 or len(stack2) == 0:
        shuffling = False
        break

print("The new order is: ", stack1 + stack2 + stack3)
