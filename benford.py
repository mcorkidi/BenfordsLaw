#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:06 2021

@author: Moises Corkidi
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    dataFile = input('Enter path to data file >>> ')
    try:
        df = pd.read_csv(dataFile)
    except Exception as e:
        print(f'Error reading dataset. \n {e}')
        return
    print(df.head())
    column = input('Select column to test >>> ')
    try:
        data = df[column]
    except Exception as e:
        print(f'Error reading column, check spelling try again. \n {e}')
        return
    rows = len(data)
    
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    invalid = -1
    
    
    for i in data:
        x = str(i)[0]
        if x == '1':
            one +=1
        elif x == '2':
            two += 1
        elif x == '3':
            three += 1
        elif x == '4':
            four += 1
        elif x == '5':
            five += 1
        elif x == '6':
            six += 1
        elif x == '7':
            seven += 1
        elif x == '8':
            eight += 1
        elif x == '9':
            nine += 1
        else:
            invalid += 1
    
    
        
    benfordsLaw = {'1': 30.1, '2': 17.16, '3': 12.5, '4': 9.7,\
                '5': 7.9, '6': 6.7, '7': 5.8, '8': 5.1, '9': 4.6 }
    
    dataPlot = {'1': one/rows, '2': two/rows, '3': three/rows, '4': four/rows,\
                '5': five/rows, '6': six/rows, '7': seven/rows, '8': eight/rows,\
                '9': nine/rows }
    dataPlot.update((x, y*100) for x, y in dataPlot.items())
    plt.bar(*zip(*dataPlot.items()))
    plt.plot(*zip(*benfordsLaw.items()), color='red')
    plt.ylabel('Percent')
    plt.xlabel('First Digit')
    plt.title('Benford\'s Law Test')
    
    plt.show()    
            
    print(f'1s happen  {round((one/rows)*100, 2)}% should be 30.1%')
    print(f'2s happen  {round((two/rows)*100, 2)}% should be 17.16%')
    print(f'3s happen  {round((three/rows)*100, 2)}% should be 12.5%')
    print(f'4s happen  {round((four/rows)*100, 2)}% should be 9.7%')
    print(f'5s happen  {round((five/rows)*100, 2)}% should be 7.9%')
    print(f'6s happen  {round((six/rows)*100, 2)}% should be 6.7%')
    print(f'7s happen  {round((seven/rows)*100, 2)}% should be 5.8%')
    print(f'8s happen  {round((eight/rows)*100, 2)}% should be 5.1%')
    print(f'9s happen  {round((nine/rows)*100, 2)}% should be 4.6%')
    print(f'Total entries {rows}')
    print(f'Invalid entries found: {invalid}')
            
if __name__ == '__main__':
   
    x = 'y'
    while x == 'y':
        main()
        x = input('Try again? (y/n) >>> ')
        
    
    
    
    