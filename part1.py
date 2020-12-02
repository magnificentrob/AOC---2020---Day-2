# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:10:50 2020

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


count = 0
file = open('input.csv', 'r')
for lines in file:
    isbetween = minValue(lines) <= password(lines).count(passwordPolicy(lines)) <= maxValue(lines)
    if isbetween == True:
        count +=1