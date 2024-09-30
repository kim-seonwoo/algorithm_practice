import sys
sys.stdin = open('input.txt', 'r')

year = int(input())

def is_lunar_year(year) :
    if four_year(year) or four_hundred(year):
        return True
    else:
        return False

def four_year(year) :
    if year % 4 == 0 and year % 100 != 0 :
        return True
    else:
        return False
    
def four_hundred(year) :
    if year % 400 == 0:
        return True
    else:
        return False
    
print(int(is_lunar_year(year)))