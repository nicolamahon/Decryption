"""
Program to find the key for Caesar Cipher encryption/decryption when the plaintext and ciphertext are known.
Author: Nicola Mahon C15755031
Date: 2018-10-07

Ciphertext and Plaintext are hard coded.
A data structure named 'alphabet' is created to identify the indices for each English letter.
The program looks at the first element in the plaintext and ciphertext.
It calculates their index values based on the alphabet data structure.
It subtracts those indices in mod 26 and returns that value as the Key.

"""


def main():
    # the ciphertext
    ciphertext = 'FEV MRIZRKZFE KF KYV JKREURIU TRVJRI TZGYVI ZJ NYVE KYV RCGYRSVK ZJ "BVPVU" SP LJZEX R NFIU. ' \
                 'ZE KYV KIRUZKZFERC MRIZVKP, FEV TFLCU NIZKV KYV RCGYRSVK FE KNF JKIZGJ REU ALJK DRKTY LG KYV ' \
                 'JKIZGJ RWKVI JCZUZEX KYV SFKKFD JKIZG KF KYV CVWK FI IZXYK. KF VETFUV, PFL NFLCU WZEU R CVKKVI ' \
                 'ZE KYV KFG IFN REU JLSJKZKLKV ZK WFI KYV CVKKVI ZE KYV SFKKFD IFN. WFI R BVPVU MVIJZFE, FEV ' \
                 'NFLCU EFK LJV R JKREURIU RCGYRSVK, SLK NFLCU WZIJK NIZKV R NFIU (FDZKKZEX ULGCZTRKVU CVKKVIJ) ' \
                 'REU KYVE NIZKV KYV IVDRZEZEX CVKKVIJ FW KYV RCGYRSVK. WFI KYV VORDGCV SVCFN, Z LJVU R BVP FW ' \
                 '"ILDBZE.TFD" REU PFL NZCC JVV KYRK KYV GVIZFU ZJ IVDFMVU SVTRLJV ZK ZJ EFK R CVKKVI. PFL NZCC ' \
                 'RCJF EFKZTV KYV JVTFEU "D" ZJ EFK ZETCLUVU SVTRLJV KYVIV NRJ RE D RCIVRUP REU PFL TRE\'K YRMV ' \
                 'ULGCZTRKVJ.'

    # the plaintext
    plaintext = 'ONE VARIATION TO THE STANDARD CAESAR CIPHER IS WHEN THE ALPHABET IS "KEYED" BY USING A WORD. ' \
                'IN THE TRADITIONAL VARIETY, ONE COULD WRITE THE ALPHABET ON TWO STRIPS AND JUST MATCH UP THE ' \
                'STRIPS AFTER SLIDING THE BOTTOM STRIP TO THE LEFT OR RIGHT. TO ENCODE, YOU WOULD FIND A LETTER ' \
                'IN THE TOP ROW AND SUBSTITUTE IT FOR THE LETTER IN THE BOTTOM ROW. FOR A KEYED VERSION, ONE ' \
                'WOULD NOT USE A STANDARD ALPHABET, BUT WOULD FIRST WRITE A WORD (OMITTING DUPLICATED LETTERS) ' \
                'AND THEN WRITE THE REMAINING LETTERS OF THE ALPHABET. FOR THE EXAMPLE BELOW, I USED A KEY OF ' \
                '"RUMKIN.COM" AND YOU WILL SEE THAT THE PERIOD IS REMOVED BECAUSE IT IS NOT A LETTER. YOU WILL ' \
                'ALSO NOTICE THE SECOND "M" IS NOT INCLUDED BECAUSE THERE WAS AN M ALREADY AND YOU CAN\'T HAVE ' \
                'DUPLICATES. '

    # empty array for storing alphabet i.e. possible keys
    alphabet = ''

    # build the alphabet, list of possible keys
    for one in range(97, 123):
        letter = chr(one).upper()
        alphabet = alphabet + letter

    # check to see if alphabet populates correct indices
    # for i in range(len(alphabet)):
        # print(str(i) + ": " + alphabet[i])

    # look at the first character in the plaintext and cipher text
    plain_char = plaintext[0]
    cipher_char = ciphertext[0]

    # get their indexes in the alphabet
    plain_num = alphabet.find(plain_char)
    print("Plaintext Index:" + str(plain_num))
    cipher_num = alphabet.find(cipher_char)
    print("Ciphertext Index:" + str(cipher_num))

    # subtract their indexes in mod 26
    key = (cipher_num - plain_num) % 26

    # print the found key
    print("Key is: " + str(key))


if __name__ == "__main__":
    main()
