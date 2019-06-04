def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    assert len(df.x)==30, "are you missing the x column?"
    #assert df.y, "are you missing the y column?"

    __msg__.good("Brilliant!")