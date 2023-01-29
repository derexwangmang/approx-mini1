import testing


if __name__ == "__main__":
    repeat = 1
    while repeat == 1:
        n = input("How many data points would you like to use for this test?")
        results = testing.test(n)
        

        repeat = input("Would you like to run another test?  If yes, input 1, else input any number.")

        

