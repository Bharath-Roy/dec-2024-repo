def add(x: int, y: int) -> int:
    return x+y

x = int(input('Enter number x: '))
y = int(input('Enter number y: '))

result = add(x,y)
print(f'Sum of {x} and {y} is {result}')
