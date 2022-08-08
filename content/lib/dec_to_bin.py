def dec_to_bin(num, nb_qbits):
    bin = "{:b}".format(num)
    if len(bin) < nb_qbits:
        diff = "0" * (nb_qbits - len(bin))
        bin = diff +  bin
    elif len(bin) > nb_qbits:
        raise Exception("Unsufficient number of bits to represent the number")
    return bin