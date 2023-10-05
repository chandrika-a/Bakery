from django.db import models

TYPE_CHOICES = (
    ("MAIDA BREAD", "MAIDA BREAD"),
    ("AATA BREAD", "AATA BREAD"), 
    ("BROWN BREAD", "BROWN BREAD"),
    ("TUTI FRUITY", "TUTI FRUITY"),
    ("GARLIC BREAD", "GARLIC BREAD"),
)

COLOR_CHOICES = (
    ("wHITE", "WHITE"), 
    ("BROWN", "BROWN"),
    ("YELLOW", "YELLOW"),
)

SIZE_CHOICES = (
    (10, "10g"),
    (15, "15g"),
    (20, "20g"),
    (25, "25g"),
    (30, "30g"),
    (40, "40g"),
    (50, "50g"),
    (100, "100g"),
)

PRIZE_CHOICES = (
    (15, "Rs 15"),
    (25, "Rs 25"),
    (40, "Rs 40"),
    (50, "Rs 50"),
)

class Bread(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="AATA BREAD")
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="WHITE") 
    size = models.IntegerField(choices=SIZE_CHOICES)
    prize = models.IntegerField(choices=PRIZE_CHOICES)

    def __str__(self):
        return self.type