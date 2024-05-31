from django.contrib import admin
from .models import CartItem, Review, OrderComment

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user_name', 'comment', 'published_date']
    ordering = ['-published_date']  
    list_filter = ['product', 'user_name'] 
    search_fields = ['comment']  

    fieldsets = [
        (
            'Сведения об обзоре',
            {
                'classes': ['wide'],
                'fields': [
                    ('Продукт', 'product'), 
                    'user_name',
                    'comment',
                ],
            },
        ),
        (
            'Метаданные',
            {
                'classes': ['collapse'],
                'fields': [
                    'published_date', 
                ],
            },
        ),
    ]

class OrderCommentAdmin(admin.ModelAdmin):
    list_display = ['order', 'user_name', 'comment', 'comment_date']
    ordering = ['-comment_date'] 
    list_filter = ['order', 'user_name']  
    search_fields = ['comment']  

    fieldsets = [
        (
            'Сведения о комментарии',
            {
                'classes': ['wide'],
                'fields': [
                    ('Заказ', 'order'), 
                    'user_name',
                    'comment',
                ],
            },
        ),
        (
            'Метаданные',
            {
                'classes': ['collapse'],
                'fields': [
                    'comment_date',
                ],
            },
        ),
    ]

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'added_date', 'total_price'] 
    ordering = ['-added_date']  
    list_filter = ['product', 'user']  
    search_fields = ['product__name'] 

    fieldsets = [
        (
            'Сведения о товаре в корзине',
            {
                'classes': ['wide'],
                'fields': [
                    ('Продукт', 'product'), 
                    ('Пользователь', 'user'),
                    'quantity',
                    ('Общая стоимость', 'total_price'),
                ],
            },
        ),
        (
            'Метаданные',
            {
                'classes': ['collapse'],
                'fields': [
                    'added_date',
                ],
            },
        ),
    ]
admin.site.register(Review, ReviewAdmin)
admin.site.register(OrderComment, OrderCommentAdmin)
admin.site.register(CartItem, CartItemAdmin)