def fun(str):
    def demo(demo):
        return "Hello " + str(demo)
    return demo

@fun
def wel(demo):
    return demo
print(wel("Python"))