def bin_to_num(bits):
    if bits is None: return None
    bits.reverse()
    num = 0
    for idx,bit in enumerate(bits):
        if bit == 1:
            num += 2**idx
    return num

