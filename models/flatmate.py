class Flatmate:
    """
    Represents a flatmate.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    
    def pay_share(self, bill):
        """
        Calculates the share of the bill the flatmate has to pay based on
        the number of days they stayed in the house.
        """
        return bill.amount * (self.days_in_house / 30)