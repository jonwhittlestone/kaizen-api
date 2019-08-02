import imapclient
from django.conf import settings

# set up an App password
# if 2fa is enabled
# https://is.gd/zz2IfV
creds = settings.PROVIDER_CREDS


def inbox_count():

    # username = creds.get('gmail', {}).get('username')
    # password = creds.get('gmail', {}).get('password')

    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(creds['gmail']['email'], creds['gmail']['app_pwd'])
    inbox = imap_obj.select_folder('INBOX', readonly=True)
    try:
        return inbox[b'EXISTS']
    except KeyError:
        return ''