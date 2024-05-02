cup = input('в кружке: ')
glass = input('в стакане: ')
print('в кружке', cup, ', а в стакане', glass)
bag = cup
cup = glass
glass = bag
print(
    'в пакет мы перелили', cup, ', в кружку перелили', glass +
    ', в стакан слили пакет и теперь в кружке ' + cup + ', а в стакане', glass)
#check git
