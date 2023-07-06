future_val = float(input('Enter future value '))
inter_rate = float(input('Enter interest rate (as %) '))
years = int(input('Enter number of years '))
inter_rate = inter_rate/100
present_val = future_val / (1+inter_rate)**years
print("${:.2f}".format(present_val))
