from django.db import models


class Staff(models.Model):
    uid = models.CharField(max_length=25, unique=True)
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    chat_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    uid = models.CharField(max_length=25, unique=True)
    active = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    chat_id = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    uid = models.CharField(max_length=25, unique=True)

    STATUS_CHOICES = [
        ('CREATED', 'Созданный'),
        ('APPROVED', 'Одобренный'),
        ('CLOSED', 'Завершенный'),
    ]
    number = models.CharField(max_length=30, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class OrderDetail(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Video(models.Model):
    STATUS_CHOICES = [
        ('OK', 'Принято'),
        ('COMMENT', 'Оставлен комментарий'),
        ('NOT OK', 'Не принято'),
    ]
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    path = models.FileField()
    data_seen = models.DateTimeField(null=True)
    data_sent = models.DateTimeField(null=True)
    comment = models.TextField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)