size=input("what size do you want?s/m/l")
bill=0
if size=='s':
    bill+=100
    print("the small pizza is 100")
elif size=='m':
    bill+=200
    print("the medium pizza is 200")
else:
    bill+=300
    print("large pizza is 300")
add_pepperoni=input("do you want pepporoni? y/n")
if add_pepperoni=='y':
    if size=='s':
        bill+=30
    else:
        bill+=50
extra_cheese=input("do you want extra cheese?y/n")
if extra_cheese=='y':
    bill+=20

print(f"your final bill is {bill}")

