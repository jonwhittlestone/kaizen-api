#!/usr/bin/env python
from gmail.gmail import inbox_count
from amex.amex import get_balance as get_amex_balance
from sjd.sjd import HowappedReader
from pocket.pocket import pocket_client

def formatter(raw):
    return raw.strip()

def main():
    howapped = HowappedReader()
    print('')
    print('**********************')
    print('')
    print(f"GMAIL INBOX:\t\t\t{inbox_count()}")
    print(f"AMEX BALANCE:\t\t\t{get_amex_balance()}")
    print(f"HOWAPPED PROFITS:\t\t{howapped.reported_profits}")
    print(f"POCKET ARTICLES:\t\t{pocket_client.acticle_count()}")

    print('')
    print('**********************')


if __name__ == '__main__':
    main()
