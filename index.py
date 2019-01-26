# drukowanie do konsoli

print("drukowanie stringa")
print(20 + 30)
print("konkatencja stinga i liczby: " + str(20 + 30))

# zmienne

x = "hello world"
y = 10
print(x, y, str(y))

zmA: int = 10
zmB: str = 20
zmC: bool = True

print(zmA, zmB, zmC)

# sprawdzenie typu zmiennej

print(type(zmA))
print(type(zmB))
print(type(zmC))

type_zmA = type(zmA)
print("checking type: " + str(type_zmA))

# changing variable type

_zm1 = 10
_zm2 = float(_zm1)
print(_zm2, type(_zm2))

_zm3 = 101.123
_zm4 = str(_zm3)
print("reformat float to string: ", _zm4, type(_zm4))

# simple operation on string variables

textHello = "hello world"
textHello = textHello + "!!! "
textHello = textHello * 3
print(textHello)

# getting info from user by input

userInfo = input()
print(userInfo, type(userInfo))
