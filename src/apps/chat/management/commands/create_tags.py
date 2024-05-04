from django.core.management.base import BaseCommand
from src.apps.chat.models import Tag


class Command(BaseCommand):
    help = "Create Default Tags"

    default_tags = [
        "Prospect",
        "Customer",
        "Insurer",
        "Broker"
    ]

    def handle(self, *args, **kwargs):
        print("[!] Creating default tags")
        objs = Tag.objects.bulk_create([Tag(name=tag) for tag in self.default_tags])
        for obj in objs:
            print(f"[+] Tag {obj.name} created successfully")
        print("[+] Default tags created successfully")