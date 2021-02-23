from funcMath import fm, fmgraph

def test_sigmoid():

    print(fm.sigmoid(0))

def test_sigmoid1():
    
    fmgraph.sigmoid()

def test_relu():

    print(fm.relu(5))

def test_relu1():

    fmgraph.relu()

def test_constant():

    fmgraph.constant(100)

def test_linear():

    fmgraph.linear(5, 2)

def test_psflinear():

    fmgraph.psflinear(6, 0.5, 20)

def test_quadratic():

    fmgraph.quadratic(1, 0, 0)

def test_vtquadratic():

    fmgraph.vtquadratic(2, -6, 20)

def test_cubic():

    fmgraph.cubic(2, -3, -3, -35)

def test_trigsin():

    fmgraph.trigsin(1, 0.5)

def test_trigcos():

    fmgraph.trigcos(2, 1)

def test_trigtan():

    fmgraph.trigtan(5, 2)

def test_quartic():

    fmgraph.quartic(10, -10, 5, 5, -150)

def test_quintic():

    fmgraph.quintic(1, -5, 5, 5, -6, -1)

def test_sextic():

    fmgraph.sextic(2, 4, 0, 2, 10, 4, 2)

def test_logFun():

    fmgraph.logFun(10, 20)

def test_absVal():

    fmgraph.absVal(12, -11, 12)

def test_isPrime():

    fm.isPrime(15)

def test_isSquare():

    fm.isSquare(36)