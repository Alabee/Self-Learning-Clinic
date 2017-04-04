def loan_calculator(amount, rate, time):
    total_amount = (amount * rate/100 * time/12) + amount
    return total_amount
'''
amount = int(input("Enter the loan amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time in months:"))

print(loan_calculator(amount, rate, time))

'''

if __name__ == "__main__":
    main()
