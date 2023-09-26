#Leap year 
defisLeapyear (year)
if(year%4==0andyear%100 !=0)or  year %400==0:
     return True 



year=20/2
if is leapyear(year):
print('{}is a leap year.'.format (year))
else:
print('{}is a not a leap year .'.format(year))

