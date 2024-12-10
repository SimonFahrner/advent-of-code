import re

def get_input():
    
    with open('input.txt') as f:
        data = f.read().replace('\n', ' ')
        
    return data

def calculate_match(match):
    num1, num2 = map(int, re.findall(r"\d+", match))
    return num1 * num2