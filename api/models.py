from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    product_ids = models.JSONField()
    quantities = models.JSONField()
    payment_info = models.JSONField() 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by User {self.user_id}"
