from django.db import models

from myapp3.models import Client, Product, Order


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Обзор для {self.product.name} by {self.user_name}'



class OrderComment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий к заказу {self.order.id} by {self.user_name}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)  
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user') 

    def __str__(self):
        return f'{self.quantity}x {self.product.name} (added by {self.user.username})'