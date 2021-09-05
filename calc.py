from functools import reduce

def sum(x,y) -> int:
    return x + y

def sub(x,y) -> int:
    return x - y

def lsum (y) -> int:
    return reduce (lambda x, y:  x + y, y)

if __name__ == "__main__":
    x = 100
    y = 200
    print (sum(x,y))
    print (sub(x,y))
    y = [10, 20, 30]
    print (lsum(y))