"""
Program to decrypt a ciphertext encrypted with Vigenere Cipher
Author: Nicola Mahon C15755031
Date: 2018-10-10

Ciphertext is hard coded.
Program ignores non-alphabetic characters such as: numbers, brackets, single/double quotations, hyphen, etc
Key is: KISWAHILI
Key is stored also stored as numeric values based on indexes of the alphabet: [10, 8, 18, 22, 0, 7, 8, 11, 8]

"""


def main():
    # the ciphertext
    ciphertext = "XQKP IZ IMWEB LK AUVZCXKW PHL VPE RIKD ASOZZSBZI TOIE ESTD XEJWXM CPS-3. PHPA TA DPW NEZCWB YN S " \
              "OIE-GPIB " \
              "KGIPLBTBSWF, WNK UJ WGV KGEPV TA YVW KF APP NSDW NETITVSVY BIUIWQCBK (KUA WQ IX QFETPIW 64). QD'A " \
              "HNOIIMTI BGK LHBP NYZ EA TV IQNOKL PHL NTVKT VACPATWX, JMP I HU SWZQFC FVZ \"YW KESND.\" PB'D VYB LDAA " \
              "BSM XMO DAZP QCXKLEOUA LZOV'L WNF OZWN, QL'O TOIE EO LGJ'T YMLTVG FAEK WYM. GPWJ WL AEIBBWZ TOQD " \
              "XBWUASZ JLKU QF 2006, ET " \
              "SWZSOL SO IM EP EYCDZ BL VPMNQFC A UMH PKAZ BUUKEQYV KKOU. BSM CPS BATQWG (GPAYH PA CMKTDU PHZE WP BZA " \
              "MK4 IYL WL5 XWMPTJ), EKA MJDLZ TVMZWWSPVR XBMKOUYM QZYU FAW AGAMC WX YRFXEIXIDUSPA. HM NQVJ'T RVZE RWO " \
              "HOUO EPO DSNIVCD ARI-2 NWRPIYBC EGQLK ZPUKQF OEJCCM. LCL ET'Z 2012, IYL CPS-512 ES ZBTTV TGKKPVR OYWV. " \
              "AVLV HWBAW, JOUM ZN DPW OHH-3 KLVNQVWTLA TA CQYJIMQNIXBDU BLBEMB. AGIE HZP NKALAR, ICE VYB GNDLZD WP " \
              "USCNPBFLO NSOTLZ. DWWM SNE ZULTVMJ EN OICLGIJA, BBB YWD WJZEYA ZN WIYJIACOM CUSHLLZ. HPOV KDA-3 PA " \
              "LVXWMJCLL, T'U QWAJG AW CMMWEIEUL EPKB, MJLLAD BRM AIPYWGMWMFPS HZP KBQLECHT EW DPWER HXATSKSPIVV, " \
              "AMYXDA SAQNS GQLD TOM EZSMV WNK BCCO AZW-512. AA TPICB XKR H ESQVM. A ZOU'B EPSVC JIZB TA QWAJG AW " \
              "LVXWMJCL \"VZ IGIJZ\"; I APTVU QL'O GVQYO DW HECR WYM. KVV KF APP NSDW NETITVSVY, E DVV'E ZOIDHY " \
              "OIGM K NSROYQEM. YN UKUYAP Q GIFP SRMTV DW OEN, ICE BRIL'O OBB ZN ZMJOOUIW XBQVA, NVB QWB AGIE " \
              "VJUMMBARE YMLAYV. SJD DPTTO Q DEKL AZUO UGNE APLV YBZARZ, Q EPSVC WNF EZCVL TA ORIJ. EOTD, IAFJP " \
              "BRMJA'S VVP ZOIKKN UQDB CPGQLK KSWYAW OKLQY. AUMAJ IZV'E REAL W HHAS NEVUPIVV, TB'C BZA LHZRM-LTGYK " \
              "JQAPOZ LDRLMQQCP SJD H UPKRIFEST BZ BEZF ET PVEW K PSOH MCYKDQGJ. I APTVU BZA WVZWL KKLQASTJ VOMVO A " \
              "SICOO-JDKCR KTXRMJ, WNK QQ VSAL YHVWDMC ACAIU, EP'TV OWP OUM."

    # define the keyword used to encrypt
    keyword = "KISWAHILI"
    print("Keyword: " + keyword)

    # empty variable for storing alphabet i.e. possible keys
    alphabet = ''

    # empty variable for storing the decrypted plaintext
    plaintext = ''

    # empty array variable to store the keyword as as array of numbers based on indices in the alphabet
    number_keyword = []

    # build the alphabet, list of possible keys
    for one in range(97, 123):
        letter = chr(one).upper()
        alphabet = alphabet + letter

    # test alphabet successfully created
    print("Alphabet: " + alphabet)

    # convert the keyword letters to numeric values for decryption
    for symbol in keyword:
        # get the index of the symbol in the alphabet
        num = alphabet.find(symbol)
        # add it to the number_keyword array
        number_keyword.append(num)

    # check keyword successfully converted to numeric values
    print("Numeric Keyword: " + str(number_keyword))

    # variable to track what index of the key we are accessing
    index = 0

    # MAIN DECRYPTION HAPPENS HERE
    # this piece of code gets the alphabet-index of a letter from the ciphertext
    # it ignores those characters that are not in the alphabet
    # it determines what letter from the KEY was used to encrypt the CT-letter (using modular arithmetic)
    # it subtracts that KEY value from the CT value to get the PT value
    # it concatenates the PT characters and prints the result

    for symbol in ciphertext:
        if symbol not in alphabet:
            # ignore non-alphabetic characters
            plaintext = plaintext + symbol
        else:
            # find the index of the letter in the ciphertext
            cipher_num = alphabet.find(symbol)
            # figure out what modular index this translates to in the keyword i.e. cipher_num (mod 9)
            key_index = index % len(keyword)
            # now find the alphabet_index value of the key that was used to encrypt (saved in the number_keyword array)
            key_num = number_keyword[key_index]
            # simply subtract the CT from the KEY to get the PT index
            plain_num = cipher_num - key_num
            # find this resulting index in the alphabet
            plain_letter = alphabet[plain_num]
            # append the decrypted letter to the plaintext string
            plaintext = plaintext + plain_letter
            # increment the index for the next value
            index += 1

    # print the final decrypted plaintext
    print("DECRYPTED PLAINTEXT: " + plaintext)


if __name__ == "__main__":
    main()
