#!/usr/bin/env python
from re import sub
from decimal import Decimal
import mechanicalsoup
from getpass import getpass
from django.conf import settings

creds = settings.PROVIDER_CREDS

DIVIDEND_TAX_LOWER_THRESHOLD = Decimal(7.5)
URL = 'https://online.sjdaccountancy.com/system/login'

class HowappedReader:
    
    def __init__(self):
        username = creds.get('sjd', {}).get('username')
        password = creds.get('sjd', {}).get('password')

        self.browser = mechanicalsoup.StatefulBrowser(
            soup_config={'features': 'lxml'},
            raise_on_404=True,
            user_agent='MyBot/0.1: mysite.example.com/bot_info',
        )
        self.browser.open(URL)
        self.browser.select_form('.loginmain form')
        self.browser["username"] = username
        self.browser["password"] = password
        resp = self.browser.submit_selected()
        self.homepage = self.browser.get_current_page()


    def __clean_currency(self, money:str):
        return Decimal(sub(r'[^\d.]', '', money))

    @property
    def total_dividends_withdrawn(self):
        self.browser.open("https://online.sjdaccountancy.com/dividends")
        dividends_page = self.browser.get_current_page()

        dividend_values = dividends_page.select("table tr td:nth-of-type(2)")
        dividend_values = [self.__clean_currency(value.text) for value in dividend_values]
        return sum(dividend_values)

    @property
    def reported_profits(self):
        company_overview_div = self.homepage.find("div", class_="threecolwidget")
        reported_profits = self.__clean_currency(company_overview_div.select("span:nth-of-type(2)")[0].text)
        est_dividend_tax_owed = self.total_dividends_withdrawn * \
            round((DIVIDEND_TAX_LOWER_THRESHOLD / 100), 2)
        net_reported_profits = reported_profits - est_dividend_tax_owed
        return net_reported_profits