# Polynominals

# p := 2+x²
# q := -2+x+x⁴

def main():
    print("hello world")


# print p and q

def poly_to_string(p, q):
    p = [2, 0, 1]
    q = [-2, 1, 0, 0, 1]


    >>>poly_to_string(p)
    '2 + x^2'



    poly_to_string(q)
    '-2 + x + x^4'



    print(p)
    [2, 0, 1]

    print(q)
    [-2, 1, 0, 0, 1]

    poly_to_string(p, q)
    '2 + x^2'
    '-2 + x + x^4'
    [2, 0, 1]
    [-2, 1, 0, 0, 1]

    print(poly_to_string(p))
    print(poly_to_string(q))

    print(p)
    print(q)