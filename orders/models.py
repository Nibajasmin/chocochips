from django.db import models

class Order(models.Model):
    PAYMENT_CHOICES = [
        ("Gpay", "Gpay"),
        ("COD", "Cash on Delivery"),
    ]

    # PRICE TABLE (backend source of truth)
    CAKE_PRICES = {
        "CheeseCake": 750,
        "ChocolateCake": 680,
        "StrawberryCake": 700,
        "HoneyCake": 700,
        "NutellaCake": 750
    }

    BROWNIE_PRICES = {
        "Chocolate Brownies": 110,
        "Fudge Walnut Brownies": 130,
        "Nutella Brownies": 130
    }

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    cake = models.CharField(max_length=100, blank=True, null=True)
    cake_quantity = models.IntegerField(default=0)

    brownie = models.CharField(max_length=100, blank=True, null=True)
    brownie_quantity = models.IntegerField(default=0)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    # ✅ NEW FIELD (IMPORTANT)
    total_price = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        cake_price = self.CAKE_PRICES.get(self.cake, 0)
        brownie_price = self.BROWNIE_PRICES.get(self.brownie, 0)

        return (cake_price * self.cake_quantity) + (brownie_price * self.brownie_quantity)

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ₹{self.total_price}"