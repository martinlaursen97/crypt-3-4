from passlib.hash import sha512_crypt
from itertools import product


def find_password(iterable: str, size: int, salt: str, hash: str, rounds: int) -> str:
    for combination in product(iterable, repeat=size):
        password = ''.join(combination)

        if sha512_crypt.using(salt=salt, rounds=rounds).hash(password) == hash:
            return password
    return 'Not found'


if __name__ == '__main__':
    hash = '$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0'

    password = find_password(iterable="0123456789",
                             size=3,
                             salt='penguins',
                             hash=hash,
                             rounds=5000)

    print(f'Password: {password}')
