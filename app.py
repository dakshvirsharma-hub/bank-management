import streamlit as st
from bank import Bank  # your class file

st.title("🏦 Simple Bank App")

menu = ["Create Account", "Deposit", "Withdraw", "Update", "View Details", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# CREATE ACCOUNT
if choice == "Create Account":
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create"):
        result = Bank.create_account(name, age, email, int(pin))
        st.write(result)

# DEPOSIT
elif choice == "Deposit":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        st.write(Bank.deposit(acc, int(pin), amount))

# WITHDRAW
elif choice == "Withdraw":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        st.write(Bank.withdraw(acc, int(pin), amount))

# DELETE
elif choice == "Delete":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        st.write(Bank.delete(acc, int(pin)))

elif choice == "Update":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    field = st.selectbox("What to update?", ["name", "email", "pin"])
    new_value = st.text_input("New Value")

    if st.button("Update"):
        if field == "pin":
            new_value = int(new_value)
        st.write(Bank.update(acc, int(pin), field, new_value))
    
elif choice == "View Details":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        result = Bank.get_details(acc, int(pin))

        if isinstance(result, dict):
            st.success("Account Details")
            st.json(result)
        else:
            st.error(result)