from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    APPROVED = 'AP'
    MODERATION = 'MO'
    REJECTED = 'RJ'
    STATUS_CHOICES = [
        (APPROVED, 'Approved'),
        (MODERATION, 'Moderation'),
        (REJECTED, 'Rejected'),
    ]
    status_choice = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=APPROVED,
    )
    
    def __str__(self) -> str:
        return f"{self.name} - {self.description} - {self.status_choice}"