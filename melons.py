"""Classes for melon orders."""

## Create supur class: AbstractMelonOrder(). Other classes inherit from super class.
# Recognize what methods to move to the super class.
# Recognize which attributes that belong to international vs national.
#

#QUESTIONS
# Is it better to have an attribute declared on the subclass, or to have an INIT

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5
        flat_rate = 0

        #Check if melon species is "christmas", if so base price is base price * 1.5
        if self.species.lower() == "christmas":
            base_price = base_price * 1.5

        #If international order & the quantity is less than 10, apply flat_rate fee of $3
        if self.order_type == "international" and self.qty < 10:
            flat_rate = 3


        total = (1 + self.tax) * self.qty * base_price + flat_rate
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the government"""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'government', 0)
        """Initialize melon order attributes"""

    passed_inspection = False

    def mark_inspection(self, boolean_input):
        """Record the fact that am order has passed inspection"""
        if boolean_input == True:
            self.passed_inspection = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'domestic', 0.08)
        """Initialize melon order attributes."""

    
    country_code = "USA"



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, 'international', 0.17)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


