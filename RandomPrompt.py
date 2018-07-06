import random

with open('C:\Users\Varshini\PycharmProjects\PracticePython\prompts.txt') as file: prompts = [prompt.rstrip('\n') for prompt in file]
print prompts[random.randint(0 , len(prompts) - 1)]

