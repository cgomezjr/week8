#func = user's function
#funcDeriv = derivative of the function
#x = user's inital guess
#iterations = number of iterations the user wants to run

def newton():
    while True:
        func = input("Input the function: ")
        funcDeriv = input("Input the derivative of the function: ")
        x = input("Input guess: ")
        if func == '' or funcDeriv == '' or x == '':
            break
        x = int(x)
        
        def f(x):
            f = eval(func)
            return f

        def df(x):
            df = eval(funcDeriv)
            return df
        
        i = x - (f(x)/df(x))
        x = i
        print(f"The root was found to be at {x}")

newton()
