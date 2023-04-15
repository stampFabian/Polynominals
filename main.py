#create a function that takes two polynomials as lists and returns the sum of the two polynomials as a string.
p = [2, 0, 1]  # 2 + x^2
q = [-2, 1, 0, 0, 1]  # -2 + x + x^4


def polynomial_sum(p, q):
    result = []
    max_deg = max(len(p), len(q))
    p = [0] * (max_deg - len(p)) + p
    q = [0] * (max_deg - len(q)) + q
    for i in range(max_deg):
        coeff_sum = p[i] + q[i]
        if coeff_sum != 0:
            result.append(f"{coeff_sum}" + ("x" if i != max_deg - 1 else ""))
            if i != max_deg - 1:
                result.append("^" + f"{max_deg - i - 1}")
            result.append(" + ")
    if not result:
        result.append("0")
    else:
        result.pop()
    return "".join(result)


result = polynomial_sum(p, q)
print(result)