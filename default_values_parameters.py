accounts = {
    'checking': 3456.00,
    'balance': 9870.00
}
def add_balance(amount: float, name: str = 'checking') -> float:
    """
    Function to update the balance of an account and return the new balance.
    """
    accounts[name] += amount
    return accounts[name]

add_balance(600.00)
print(accounts['checking'])