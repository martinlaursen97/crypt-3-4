from passlib.hash import sha512_crypt


# pw 000-999
for i in range(1000):
    pw = str(i)
    if i < 10:
        pw = '00' + pw
    elif i < 100:
        pw = '0' + pw

    hash = sha512_crypt.using(salt='penguins', rounds=5000).hash(pw)
    if hash == '$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0':
        print(f'Password: {pw}')
        break
