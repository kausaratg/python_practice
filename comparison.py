print(ord('b'))
temperature = 35
if temperature > 30:
    print('it is warm')
    print("drink water")
elif  temperature > 20:
    print("It's nice")
else:
    print("it's cold")
print('done')
age = 22
# if age >= 18:
#     print('Eligible')
# else:
#     print('Not eligible')




message = "eligible" if age >= 18 else "not eligble"
print(message)

num = 30
message = "old" if num > 15 else "young"
print(message)


high_income = True
good_credit = False
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print('Not eligble')