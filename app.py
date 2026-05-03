import streamlit as st
from bank import Bank

st.title("🏦 Simple Bank App")

menu = [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Update",
    "View Details",
    "Delete"
]

choice = st.sidebar.selectbox("Menu", menu)

# ---------------- CREATE ----------------
if choice == "Create Account":
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4 digit)", type="password")

    if st.button("Create"):
        if not name or not email or not pin:
            st.error("All fields required")
        elif not pin.isdigit():
            st.error("PIN must be numeric")
        else:
            result = Bank.create_account(name, age, email, int(pin))

            if isinstance(result, dict):
                st.success("Account Created")
                st.write("Account No:", result["accountNo"])
            else:
                st.error(result)


# ---------------- DEPOSIT ----------------
elif choice == "Deposit":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            st.success(Bank.deposit(acc, int(pin), amount))


# ---------------- WITHDRAW ----------------
elif choice == "Withdraw":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            st.success(Bank.withdraw(acc, int(pin), amount))


# ---------------- UPDATE ----------------
elif choice == "Update":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    field = st.selectbox("Field", ["name", "email", "pin"])
    new_value = st.text_input("New Value")

    if st.button("Update"):
        if field == "pin" and not new_value.isdigit():
            st.error("PIN must be numeric")
        else:
            st.success(Bank.update(acc, int(pin), field, new_value))


# ---------------- VIEW ----------------
elif choice == "View Details":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            result = Bank.get_details(acc, int(pin))
            st.write(result)


# ---------------- DELETE ----------------
elif choice == "Delete":
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        if not pin.isdigit():
            st.error("Invalid PIN")
        else:
            st.warning(Bank.delete(acc, int(pin)))