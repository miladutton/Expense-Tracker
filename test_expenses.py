import pytest
import csv
import os
from project import add_expense, track_expenses, save_csv

test_expenses = [
    {"category": "Food", "amount": 50.0, "date": "2024-10-01"},
    {"category": "Transportation", "amount": 20.0, "date": "2024-10-02"},
    {"category": "Entertainment", "amount": 30.0, "date": "2024-10-03"},
]

def test_add_expense():
    expenses = []
    add_expense(expenses, "Food", 50.0, "2024-10-01")
    assert len(expenses) == 1
    assert expenses[0] == {"category": "Food", "amount": 50.0, "date": "2024-10-01"}

def test_track_expenses():
    summary = track_expenses(test_expenses)
    assert summary["Food"] == 50.0
    assert summary["Transportation"] == 20.0
    assert summary["Entertainment"] == 30.0

def test_save_csv():
    save_csv(test_expenses)
    assert os.path.exists("expense_tracker.csv")
    with open("expense_tracker.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == len(test_expenses)  # Ensure the number of rows matches
        for expense, row in zip(test_expenses, rows):
            assert expense["category"] == row["category"]
            assert float(expense["amount"]) == float(row["amount"])
            assert expense["date"] == row["date"]
    os.remove("expense_tracker.csv")

 
if __name__ == "__main__":
    pytest.main()