def test():
    assert beta0 > 0 and beta0 < 5, "It seems you beta0 guess is off. Look carefully when x=0"
    assert beta1 > 10, "It seems you beta1 guess is off. Look carefully at the slope"

    __msg__.good("Great Job!")