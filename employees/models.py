from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Shift(models.Model):
    SHIFT_CHOICES = [
        ("8AM-8PM", "8AM-8PM"),
        ("8PM-8AM", "8PM-8AM"),
    ]

    shift = models.CharField(max_length=100, choices=SHIFT_CHOICES, unique=True)

    def __str__(self):
        return self.shift

class Day(models.Model):
    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]

    day = models.CharField(max_length=100, choices=DAY_CHOICES, unique=True)

    def __str__(self):
        return self.day

class Availability(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="availability")
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee} - {self.day} - {self.shift}"