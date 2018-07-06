import random

with open('prompts.txt') as file: prompts = [prompt.rstrip('\n') for prompt in file]
print prompts[random.randint(0 , len(prompts) - 1)]

