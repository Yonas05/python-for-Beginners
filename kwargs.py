def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="William", middle="Johnson", last="Backers")
