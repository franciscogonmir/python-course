import module.calculator as calculator


def operations():
    sum = "{} + {} = {}".format(2, 2, calculator.sum(2, 2))
    substr = "{} - {} = {}".format(234, 453, calculator.subtraction(234, 453))
    multiply = "{} x {} = {}".format(2, 2, calculator.multiply(2, 2))
    divide = "{} / {} = {}".format(16, 2, calculator.divide(16, 2))
    return sum + "\n" + substr + "\n" + multiply + "\n" + divide


print(operations())
