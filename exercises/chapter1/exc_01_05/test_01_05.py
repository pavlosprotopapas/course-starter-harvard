def test():
    assert beta0 > 0 and beta0 < 5, "It seems you beta0 guess is off. Look carefully when x=0"
    assert beta1 > 0.5 and beta1 < 2, "It seems you beta1 guess is off. Look carefully at the slope"
    assert MSE < 2, "It seems your guesses are off. MSE should definitely be below 1"

    __msg__.good("Excellent!")