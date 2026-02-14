from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError

from datetime import datetime, timedelta

from .models import Ship, Voyage

# Create your tests here.


class ShipModelTest(TestCase):
    # Test für Ship-Model
    def test_ship_creation(self):
        ship = Ship.objects.create(name="MS Test", capacity=300)
        self.assertEqual(ship.name, "MS Test")
        self.assertEqual(ship.status, "available")

    def test_ship_unique_name(self):
        ship = Ship.objects.create(name="MS Test", capacity=300)

        with self.assertRaises(IntegrityError):
            ship = Ship.objects.create(name="MS Test", capacity=250)

class VoyageModelTest(TestCase):
    # Test für Voyage-Model
    def setUp(self):
        self.ship = Ship.objects.create(name="MS Test", capacity=300)

    def test_voyage_creation(self):
        voyage = Voyage.objects.create(
            ship=self.ship,
            start_port="Bremerhaven",
            destination_port="Rotterdam",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=3, hours=14)
        )

        self.assertEqual(voyage.ship, self.ship)

    def test_voyage_end_before_start_fails(self):
        with self.assertRaises(ValidationError):
            voyage = Voyage.objects.create(
                ship=self.ship,
                start_port="Bremerhaven",
                destination_port="Rotterdam",
                start_date=datetime(2026,3,5,10,00),
                end_date=datetime(2026,3,3,10,00)
            )

    def test_voyage_conflict_detection(self):
        voyage = Voyage.objects.create(
            ship=self.ship,
            start_port="Bremerhaven",
            destination_port="Rotterdam",
            start_date=datetime(2026, 3, 1, 10, 00),
            end_date=datetime(2026, 3, 5, 18, 00)
        )

        with self.assertRaises(ValidationError):
            voyage2 = Voyage.objects.create(
                ship=self.ship,
                start_port="Singapore",
                destination_port="Amsterdam",
                start_date=datetime(2026, 3, 3, 10, 00),
                end_date=datetime(2026, 3,7,18,00)
            )

    def test_voyage_no_conflict_different_ship(self):
        ship2 = Ship.objects.create(name="MS Kreuzberg", capacity=800)

        voyage = Voyage.objects.create(
            ship=self.ship,
            start_port="Bremerhaven",
            destination_port="Rotterdam",
            start_date=datetime(2026, 3, 1, 10, 00),
            end_date=datetime(2026, 3, 5, 18, 00)
        )

        voyage2 = Voyage.objects.create(
            ship=ship2,
            start_port="Trier",
            destination_port="Saarbrücken",
            start_date=datetime(2026, 3, 3, 10, 00),
            end_date=datetime(2026, 3, 7,16,00)
        )

        self.assertIsNotNone(voyage2)
        self.assertEqual(voyage2.ship, ship2)