# See high_performance_computing for parallel version


def midpoint(a,b,n,f):
    """
    midpoint rule (source https://plainenglish.io/blog/how-is-numerical-integration-done-using-python-4585344e5800)
    a: interval start
    b: interval end
    n: steps
    f: function
    return: approximation
    """
    res = 0
    h = (b-a)/n #number of steps
    x = a + (h/2)
    # evaluate
    for _ in range(n):
        res += f(x)
        x += h
    return h * res

def basic_quad(x):
    return (-1 * (x*x)) + (2 * x) + 0

print(midpoint(0,2,100,basic_quad))
