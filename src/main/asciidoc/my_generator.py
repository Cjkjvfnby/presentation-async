def my_generator():
    while True:
        result = yield "generator: Give me input"
        if result.upper() == 'QUIT':
            return
        else:
            print(f'generator: {result}')


while True:
    a = my_generator()
    print(next(a))
    a.send(input())
