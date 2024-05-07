import email
import imaplib
import json
from bs4 import BeautifulSoup
import html2text

def getMail():
    imap_host = 'imap.qiye.aliyun.com'
    imap_port = 993
    email_address = 'zelun.su@amperetime.com'
    password = 'CD4H3OsYpC26aMGb'

    imap_server = imaplib.IMAP4_SSL(imap_host, imap_port)
    imap_server.login(email_address, password)

    imap_server.select('INBOX')
    status, messages = imap_server.search(None, 'UNSEEN')

    if messages[0]:
        latest_email_id = messages[0].split()[-1]
        status, data = imap_server.fetch(latest_email_id, '(RFC822)')
        if status == 'OK' and data:
            email_message = email.message_from_bytes(data[0][1])
            for part in email_message.walk():
                if part.get_content_type() == "text/html":
                    content = part.get_payload(decode=True)
                    content_str = content.decode('utf-8')
                    h = html2text.HTML2Text()
                    text = h.handle(content_str)
                    return text


    imap_server.close()
    imap_server.logout()

if __name__ == '__main__':
    result = getMail()
    print("邮件内容:",result)