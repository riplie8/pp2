import pygame
keys = filter(lambda x:'K_' in x, dir(pygame))
print(list(keys))