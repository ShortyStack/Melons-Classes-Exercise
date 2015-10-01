"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 3:
            total = (self.base_price * qty) * .75
        else:
            total = self.base_price * qty

        # TODO, calculate the real amount!

        print total


class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >=5:
            total = (self.base_price / 2) * qty
        else: 
            total = self.base_price * qty

        print total


class Ogens(object):
    species = "Ogens"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_price = 6.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.base_price * qty

        print total

class Casabas(object):
    species = "Casabas"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    base_price = 6.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.base_price * 1.5) * qty

        print total

class Sharlyn(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.base_price * 1.5) * qty

        print total


class SantaClaus(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.base_price * 1.5) * qty

        print total

class HornedMelon(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.base_price * 1.5) * qty

        print total

class Xigua(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']
    base_price = 10.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.base_price * 1.5) * qty

        print total