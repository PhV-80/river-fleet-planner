from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Ship(models.Model):
    """Schiff mit Name, Kapazität und Status."""

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Name des Schiffs',
    )
    capacity = models.IntegerField(
        help_text='Ladekapazität in Tonnen',
    )

    STATUS_CHOICES = [
        ('available', 'Verfügbar'),
        ('in_voyage', 'Auf Fahrt'),
        ('maintenance', 'Wartung'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Schiff'
        verbose_name_plural = 'Schiffe'

class Voyage(models.Model):
    """Fahrt eines Schiffs von Start- zu Zielhafen."""

    ship = models.ForeignKey(
        Ship,
        on_delete=models.CASCADE,
        related_name='voyages',
        verbose_name='Schiff'
    )
    start_port = models.CharField(
        max_length=100,
        verbose_name='Starthafen'
    )
    destination_port = models.CharField(
        max_length=100,
        verbose_name='Zielhafen'
    )
    start_date = models.DateTimeField(
        verbose_name='Startdatum'
    )
    end_date = models.DateTimeField(
        verbose_name='Enddatum'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ship.name}: {self.start_port} -> {self.destination_port}"

    def clean(self):
        """Validierung: Datum + Konflikt-Check"""

        # Check 1: end_date muss nach start_date liegen
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError(
                    "Enddatum muss nach Startdatum liegen."
                )

        # Check 2: Schiff darf nicht doppelt gebucht sein
        if self.ship_id:
            overlapping = Voyage.objects.filter(
                ship=self.ship,
                start_date__lt=self.end_date,
                end_date__gt=self.start_date
            ).exclude(pk=self.pk)

            if overlapping.exists():
                conflict = overlapping.first()
                raise ValidationError(
                    f"Konflikt: Schiff '{self.ship.name}' ist bereits gebucht "
                    f"vom {conflict.start_date.strftime('%d.%m.%Y %H:%M')} "
                    f"bis {conflict.end_date.strftime('%d.%m.%Y %H:%M')}."
                )

    def save(self, *args, **kwargs):
        """Überschreibt save(), um clean() automatisch aufzurufen."""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Fahrt'
        verbose_name_plural = 'Fahrten'