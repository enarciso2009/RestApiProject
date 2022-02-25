from flask import request

name = " Everton Narciso"
print(name)

rateOfInterest = 75.77

print(rateOfInterest)

print(type(name))
print(type(rateOfInterest))

print(name[:3])
print(len(name))
print(name[2:3])
print(name[-1])
print(name[-1:])
print(name.split("t"))
print(name.split('t'[0]))
print(name.split())
print('Everton' in name.split())
if len(name.split()[0]) < 20:
    print("name is fine")
print(request.data)


# testando o git esta apresentando erro 
