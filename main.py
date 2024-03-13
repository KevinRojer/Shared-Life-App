from models.bill import Bill
from models.flatmate import Flatmate

bill = Bill(500, "March 2024")

kevin = Flatmate("Kevin", 16)
federika = Flatmate("Federika", 9)
keath = Flatmate("Keath", 27)

total_days = 30

flatmates = [kevin, keath, federika]

for mates in flatmates:
    print(f"{mates.name} owes {mates.pay_share(bill, total_days)}")
    
