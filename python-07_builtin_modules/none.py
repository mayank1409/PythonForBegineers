print(type(None))

def email(subject, content, to, cc=None, bcc=None):
    print(f'{subject}, {content}, {to}, {cc}, {bcc}....')


email("Subject", "This is the email content", "hello@python.com")
email("Subject 2", "Great Work", "hello@python.com", "hello1@python.com")

var = '123'

if var is None:
    print(f'var is None')
else:
    print(f'var is {var}')
