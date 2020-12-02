# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 04:28:39 2020

@author: Rob
"""

def minValue(line):
    value = ''
    for element in line:
        if element != '-':
            value += element
        else:
            break
    return int(value)

def maxValue(line):
    value = ''
    start = line.find('-')+1
    for element in line[start:]:
        if element == ' ':
            break
        else:
            value += element
    return int(value)

def passwordPolicy(line):
    return line[line.find(':')-1]
    
    
def password(line):
    start = line.find(':')+2
    return line[start:]


file = open('input.csv', 'r')
count = 0
for lines in file:
    minimum = minValue(lines)-1
    maximum = maxValue(lines)-1
    policy = passwordPolicy(lines)
    pWord = password(lines)
    if pWord[minimum] == policy or pWord[maximum] == policy:
        if pWord[minimum] != pWord[maximum]:
            count +=1

print(count)
