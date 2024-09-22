# queries.py

from .models import TestEntry

def create_test_entry(name, description):
    test_entry = TestEntry(name=name, description=description)
    test_entry.save()
    return test_entry

def get_all_test_entries():
    return TestEntry.objects.all()

def get_test_entry_by_id(entry_id):
    return TestEntry.objects.get(id=entry_id)

def delete_test_entry_by_id(entry_id):
    test_entry = TestEntry.objects.get(id=entry_id)
    test_entry.delete()
