import requests
from django.core.management.base import BaseCommand
from api.models import Employee   # adjust import to your app

EXTERNAL_API = "https://example.com/employees.json"   # replace with your API

class Command(BaseCommand):
    help = "Sync employees from external API"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching employees...")

        response = requests.get(EXTERNAL_API)
        employees = response.json()

        created_count = 0
        updated_count = 0

        for item in employees:
            emp, created = Employee.objects.update_or_create(
                employee_id=item["employee_id"],     # unique identifier
                defaults={
                    "name": item["name"],
                    "email": item["email"],
                    "company": item["company"],
                    "role": item["role"],
                    "joining_date" : item["joining_date"]
                }
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"Sync complete: {created_count} created, {updated_count} updated."
        ))
