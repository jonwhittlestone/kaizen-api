from pyamex import AmexClient
from django.conf import settings

creds = settings.PROVIDER_CREDS

username = creds.get('amex', {}).get('username')
password = creds.get('amex', {}).get('password')
locale = creds.get('amex', {}).get('locale')

client = AmexClient(username=username, password=password, locale=locale)


# Print all account balances
def get_balance(product_name='British Airways American Express Credit Card'):
    accounts = client.accounts()
    for account in accounts:
        if account.card_product == product_name:
            return account.total_balance