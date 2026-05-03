import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load data
    if Path(database).exists():
        with open(database, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    @classmethod
    def save(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def generate_account():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    @classmethod
    def find_user(cls, acc, pin):
        return next((u for u in cls.data if u["accountNo"] == acc and u["pin"] == pin), None)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return "Invalid age or PIN"

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": cls.generate_account(),
            "balance": 0
        }

        cls.data.append(user)
        cls.save()
        return user

    @classmethod
    def deposit(cls, acc, pin, amount):
        user = cls.find_user(acc, pin)
        if not user:
            return "User not found"

        if amount <= 0 or amount > 10000:
            return "Invalid amount"

        user["balance"] += amount
        cls.save()
        return "Deposited"

    @classmethod
    def withdraw(cls, acc, pin, amount):
        user = cls.find_user(acc, pin)
        if not user:
            return "User not found"

        if amount > user["balance"]:
            return "Insufficient balance"

        user["balance"] -= amount
        cls.save()
        return "Withdrawn"

    @classmethod
    def delete(cls, acc, pin):
        user = cls.find_user(acc, pin)
        if not user:
            return "User not found"

        cls.data.remove(user)
        cls.save()
        return "Deleted"
    
    @classmethod
    def update(cls, acc, pin, field, new_value):
        user = cls.find_user(acc, pin)

        if not user:
            return "User not found"

        if field not in ["name", "email", "pin"]:
            return "Invalid field"

        # Validation
        if field == "pin":
            if len(str(new_value)) != 4:
                return "PIN must be 4 digits"
            new_value = int(new_value)

        user[field] = new_value
        cls.save()
        return f"{field} updated"
    
    @classmethod
    def get_details(cls, acc, pin):
        user = cls.find_user(acc, pin)

        if not user:
            return "User not found"

        # Don't expose PIN in output
        return {
            "name": user["name"],
            "age": user["age"],
            "email": user["email"],
            "accountNo": user["accountNo"],
            "balance": user["balance"]
        }