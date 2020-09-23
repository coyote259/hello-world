#!/user/bin/env python3
# -*- coding: utf-8 -*-

# age = 20
# if age >= 6:
#     print('tennager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

bmi = 80.5/1.75**2
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <25:
    print('正常')
elif bmi <28:
    print('过重')
elif bmi <32:
    print('肥胖')
else :
    print('严重肥胖')

