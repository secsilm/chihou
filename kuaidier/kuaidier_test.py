import kuaidier

def test_kuaidier():
    fromaddr = 'secsilm@qq.com'
    password = 'uuzcjrntpfveebbg'
    toaddr = fromaddr
    subject = 'HELLO'
    body = 'SECSILM'
    smtp = 'smtp.qq.com'
    server = kuaidier.Kuaidier(fromaddr, password, smtp)
    server.send(toaddr, subject, body)
    server.rest()

def test_kuaidier_with():
    fromaddr = 'secsilm@qq.com'
    password = 'uuzcjrntpfveebbg'
    toaddr = fromaddr
    subject = 'HELLO'
    body = 'SECSILM'
    smtp = 'smtp.qq.com'
    with kuaidier.Kuaidier(fromaddr, password, smtp) as server:
        server.send(toaddr, subject, body)