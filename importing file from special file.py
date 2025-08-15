from calculatork import *
#we can also use 'import calculatork' or 'import calculatork as calc'
import platform

a=int(input('enter the 1st number:'))

b=int(input('enter the 2nd number:'))

add(a,b)
print('')
print(f'your platform is:{platform.system()}')

print(__name__)

            
