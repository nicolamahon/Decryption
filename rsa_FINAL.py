# import GCD function
from math import gcd


# calculate private key
def mod_inverse(a, m):
    x = 1/a
    y = x % m
    return y


# get list of coprimes
def get_coprimes(a):
    _list = []
    # where 1 < e < t
    for x in range(2, a):
        # and gcd (e,t) = 1
        if gcd(a, x) == 1:
            _list.append(x)
    return _list


# encrypt value
def encrypt(m):
    # m^^e mod n = c
    c = (m ** e) % n
    return c


# decrypt value
def decrypt(c):
    # p = c ^^ d mod n
    m = (c ** d) % n
    return m


# main method
def main():
    # get initial prime values
    p = int(input('Enter prime p: '))
    q = int(input('Enter prime q: '))

    # display user input
    print("Chosen primes:")
    print("p = " + str(p) + ", q = " + str(q))

    # calculate mod value n
    n = p * q
    print("n = p * q = " + str(n))

    # calculate totient t
    t = (p - 1) * (q - 1)
    print("Totient [phi(n)]: " + str(t))

    # ask user to pick coprime value from list
    print("Choose a value e from the following list of coprimes: ")
    print(get_coprimes(t))

    # e is coprime to t
    e = int(input())

    # calculate private key; d = e ^^ -1 (mod t)
    d = mod_inverse(e, t)

    # display public and private keys
    print("Your public key is (e=" + str(e) + ", n=" + str(n) + ")")
    print("Your private key is (d=" + str(d) + ", n=" + str(n) + ")")

    # ask for value to encrypt
    user_string = int(input("Enter a number to encrypt: "))
    print("Plaintext: " + str(user_string))

    # encrypt the value
    encrypted = encrypt(user_string)
    print("Encrypted Ciphertext: " + str(encrypted))

    # decrypt the value
    decrypted = decrypt(enc)
    print("Decrypted Plaintext: " + str(decrypted))


if __name__ == "__main__":
    main()
