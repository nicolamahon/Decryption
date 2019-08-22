"""
Program to brute force decrypt a ciphertext encrypted with Caeser Cipher
Author: Nicola Mahon C15755031
Date: 2018-10-03

Ciphertext is hard coded.
Program will terminate when first two words in the decrypted plaintext are identified as English words.
"""


# regex for dealing with the ciphertext
import re

# to check for english words in the plaintext
from pyaspeller import Word


def main():
    # the ciphertext
    ciphertext = 'RQH YDULDWLRQ WR WKH VWDQGDUG FDHVDU FLSKHU LV ZKHQ WKH DOSKDEHW LV "NHBHG" EB XVLQJ D ZRUG. LQ WKH ' \
                     'WUDGLWLRQDO YDULHWB, RQH FRXOG ZULWH WKH DOSKDEHW RQ WZR VWULSV DQG MXVW PDWFK XS WKH VWULSV DIWHU ' \
                     'VOLGLQJ WKH ERWWRP VWULS WR WKH OHIW RU ULJKW. WR HQFRGH, BRX ZRXOG ILQG D OHWWHU LQ WKH WRS URZ DQG ' \
                     'VXEVWLWXWH LW IRU WKH OHWWHU LQ WKH ERWWRP URZ. IRU D NHBHG YHUVLRQ, RQH ZRXOG QRW XVH D VWDQGDUG ' \
                     'DOSKDEHW, EXW ZRXOG ILUVW ZULWH D ZRUG (RPLWWLQJ GXSOLFDWHG OHWWHUV) DQG WKHQ ZULWH WKH UHPDLQLQJ OHWWHUV ' \
                     'RI WKH DOSKDEHW. IRU WKH HADPSOH EHORZ, L XVHG D NHB RI "UXPNLQ.FRP" DQG BRX ZLOO VHH WKDW WKH SHULRG LV ' \
                     'UHPRYHG EHFDXVH LW LV QRW D OHWWHU. BRX ZLOO DOVR QRWLFH WKH VHFRQG "P" LV QRW LQFOXGHG EHFDXVH WKHUH ZDV ' \
                     'DQ P DOUHDGB DQG BRX FDQ\'W KDYH GXSOLFDWHV. '

    # empty array for storing alphabet i.e. possible keys
    alphabet = ''

    # build the alphabet, list of possible keys
    for one in range(97, 123):
        letter = chr(one).upper()
        alphabet = alphabet + letter

    # check to see if alphabet populates correctly
    print(alphabet)

    # start decrypting
    # for every index value in the alphabet (0 - 25)
    for key in range(len(alphabet)):
        # reset the plaintext string on each round
        plaintext = ''
        # look at each value in the ciphertext
        for symbol in ciphertext:
            # if the value exists in the alphabet
            if symbol in alphabet:
                # get the index of the symbol in the alphabet
                num = alphabet.find(symbol)
                # try every variation of the index from 0-25
                num = num - key  # key here is the index of the outer for loop
                # if the index goes out of bounds i.e. < 0 or < A
                if num < 0:
                    # reset the value to start at Z again
                    num = num + len(alphabet)
                # update the plaintext with the indexed value from alphabet
                plaintext = plaintext + alphabet[num]
            # otherwise the symbol is not in alphabet i.e. white space
            else:
                # therefore just append the symbol to the plaintext unchanged
                plaintext = plaintext + symbol
        # split the plaintext to try identify english words
        words = re.split("[^a-zA-Z]+", plaintext)

        # look at the first two words in the string
        check1 = Word(words[0])
        check2 = Word(words[1])

        # if they are not english words
        if check1.correct is False:
            if check2.correct is False:
                # print("not in dictionary")
                continue
        else:
            print("FOUND IT!")
            # print the value of the key and plaintext
            print("The key is: " + str(key) + "\nPlaintext: " + plaintext)
            # no need to check other keys
            break


if __name__ == "__main__":
    main()
