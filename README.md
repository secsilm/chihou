# kuaidier

A package for notifying you by email when something is done.

## Usage

```python
from kuaidier import kuaidier

fromaddr = 'from@example.com'
password = 'yourpassword'  # or get it via env using os.environ
toaddr = 'to@example.com'
smtp = 'smtp.server.com'
subject = 'this is the email subject'
body = 'this is the email body'
with kuaidier.Kuaidier(fromaddr, password, smtp) as server:
    server.send(toaddr, subject, body)
```
