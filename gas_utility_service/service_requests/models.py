from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # Allow file uploads
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)  # Timestamp when resolved

    def __str__(self):
        return f"{self.name} - {self.request_type}"
