#We are going to make a rent calculator that will calculate the rent based on the number of bedrooms and bathrooms in an apartment. The user will input the number of bedrooms and bathrooms, and the program will output the total rent.


rent_we_have = int(input("Enter Rent : "))
total_person = int(input("Enter how many people lives together : "))
food = int(input("Enter food bill : "))
electricity_unit = int(input("How much electricity units used : "))
charge_per_unit = int(input("Charge per unit : "))
total_bill = electricity_unit * charge_per_unit
total = (rent_we_have + food + total_bill) // total_person
print(total)
