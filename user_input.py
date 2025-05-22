"""F_name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"your name is : {F_name} and your age is: {age}")
"""
#Note: anything from input is consider a string 
# write a program that takes 2 numbers from user and display the sum of both numbers
#num1= int(input("Enter your first num: "))
#num2 = int(input ("Enter your second  num: "))
#sum= num1+num2
#print(sum)

# Write a code to help your client with money transfer 
# it should ask for user total amount to send in USD
# then it should tell how much the receiver will get in cameroon ==> CFA
# sending fees should be 0.02 added to the total amount
# exchange rate should 655
sending_fees = 0.02
exchange_rate = 655
user_amount = int(input("Enter the amount: "))
fee_amount= sending_fees * user_amount
amount_plus_fees = user_amount + fee_amount
receiving_amount = exchange_rate * user_amount
print(f"The amount plus sending fees is:{amount_plus_fees:,} and your familly will recieved {receiving_amount:,}")

user_answer = input(" Do you want to proceed(yes/no)? ")
if user_answer == 'yes':
    print("Proceed with the payment")
else:
    print("Thank you for stopping by ")