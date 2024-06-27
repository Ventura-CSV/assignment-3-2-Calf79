def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
   
    minval= num1 
    minval= num2 if num2<= minval else minval
    minval= num3 if num3<= minval else minval
    ########################################
    maxval= num1 
    maxval= num2 if num2>= maxval else maxval
    maxval= num3 if num3>= maxval else maxval
    
    #########################################
    median= num1
    median= num1 if minval<num1 and maxval>num1 else median
    median= num2 if minval<num2 and maxval>num2 else median
    median= num3 if minval<num3 and maxval>num3 else median    


    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
