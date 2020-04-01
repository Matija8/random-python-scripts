#! /usr/bin/env python3

cyrillic = list('абвгдђежзијклљмнњопрстћуфхцчџшАБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЂУФХЦЧЏШ')
latin =    list('abvgddezzijkllmnnoprstcufhccdsABVGDDEZZIJKLLMNNOPRSTCUFHCCDS')
mapping = {}
for i in range(len(cyrillic)):
    mapping[cyrillic[i]] = latin[i]

mapping['ђ'] = 'dj'
mapping['Ђ'] = 'Dj'
mapping['ж'] = 'z'
mapping['Ж'] = 'Z'
mapping['љ'] = 'lj'
mapping['Љ'] = 'Lj'
mapping['ч'] = 'c'
mapping['Ч'] = 'C'
mapping['џ'] = 'dz'
mapping['Џ'] = 'Dz'
mapping['ш'] = 's'
mapping['Ш'] = 'S'
