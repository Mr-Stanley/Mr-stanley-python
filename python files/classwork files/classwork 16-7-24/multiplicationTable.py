
for number in range(1, 21): 
    for index in range(1, 13):
        product = number * index
        print(f'{number : <2}*{index}={number*index: <4}', end='  ')
    print()