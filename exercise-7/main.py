import module.calculator as calculator


def operations():
    return "The result sum is {}" \
           "\nThe result substraction is {}" \
           "\nThe result multiply is {}" \
           "\nThe result divide is {}".format(calculator.sum(2, 2)
                                              ,calculator.subtraction(234, 453)
                                              ,calculator.multiply(2, 2)
                                              ,calculator.divide(16, 2))


print(operations())

