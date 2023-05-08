print("Welcome to Tip calculator!")
bill = float(input("What was the Total Bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 :"))
people = int(input("How many People to spilt the bill? "))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each Person should pay: ${final_amount}")
print("Thank you and Please Visit Again")
