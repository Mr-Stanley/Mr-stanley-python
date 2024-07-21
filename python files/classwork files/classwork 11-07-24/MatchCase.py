name = "Stanley"
print(id(name))
name = name + "Ugochukwu"
print (id(name))

for number in range(0, 100):
    print(number, end ='\t')
    
score = 80
    
result = 'Passed' if score > 45 else 'failed'
print(result)