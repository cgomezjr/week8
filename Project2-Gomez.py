#func = user's function
#funcDeriv = derivative of the function
#x = user's inital guess
#iterations = number of iterations the user wants to run


def newton(func, funcDeriv, x, iterations):

    def f(x):
        f = eval(func)
        return f

    def df(x):
        df = eval(funcDeriv)
        return df
    for intercept in range(1, iterations):
        i = x - (f(x)/df(x))
        x = i
    print(f"The root was found to be at {x} after {iterations} iterations")

newton(input("Input the function: "),
       input("Input the derivative of the function: "),
       int(input("Input guess: ")),
       int(input("Input the number of iterations: ")))
