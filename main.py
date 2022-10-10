from passlib.hash import sha512_crypt
from itertools import product


def find_password(iterable: str, size: int, salt: str, hash: str, rounds: int) -> str:
    for i in product(iterable, repeat=size):
        password = ''.join(i)

        if sha512_crypt.using(salt=salt, rounds=rounds).hash(password) == hash:
            return password
    return 'Not found'


if __name__ == '__main__':
    hash = '$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0'

    pw = find_password("0123456789",
                       3,
                       'penguins',
                       hash,
                       5000)

    print(f'Password: {pw}')
