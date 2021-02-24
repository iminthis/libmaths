from funcMath import linear, polynomial, trig, special, other

def test_sigmoid():

    print(other.sigmoid(0))

def test_sigmoid1():
    
    special.sigmoid()

def test_relu():

    print(other.relu(5))

def test_relu1():

    special.relu()

def test_constant():

    linear.constant(100)

def test_linear():

    linear.linear(5, 2)

def test_psflinear():

    linear.psflinear(6, 0.5, 20)

def test_quadratic():

    polynomial.quadratic(1, 0, 0)

def test_vtquadratic():

    polynomial.vtquadratic(2, -6, 20)

def test_cubic():

    polynomial.cubic(2, -3, -3, -35)

def test_trigsin():

    trig.trigsin(1, 0.5)

def test_trigcos():

    trig.trigcos(2, 1)

def test_trigtan():

    trig.trigtan(5, 2)

def test_quartic():

    polynomial.quartic(10, -10, 5, 5, -150)

def test_quintic():

    polynomial.quintic(1, -5, 5, 5, -6, -1)

def test_sextic():

    polynomial.sextic(2, 4, 0, 2, 10, 4, 2)

def test_logFun():

    special.logFun(10, 20)

def test_absVal():

    special.absVal(12, -11, 12)

def test_isPrime():

    other.isPrime(15)

def test_isSquare():

    other.isSquare(36)

def test_divisor():

    other.divisor(12)