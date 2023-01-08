
def main():
    
    # bits = 0xff
    # for i in range(8):
    #     for j in range(0, i, 1):
    #         for m in range(0, j, 1):
    #             for a in range(0, m , 1):
    #                 for b in range(0, a, 1):
    #                     print(bin(bits ^ (1 << i) ^ (1 << j) ^ (1 << m) ^ (1 << a) ^ (1 << b)))
    
    bits = 0xf1
    nbits = 8
    count_1 = bin(bits).count('1')
    bit_arr = [0, 0]
    bit_arr[1] = count_1
    bit_arr[0] = nbits - count_1
    min_val =[0, 0]
    if bit_arr[0] > bit_arr[1]:
        min_val[1] = bit_arr[1]
        min_val[0] = (nbits//2) - bit_arr[1]
    else:
        min_val[1] = (nbits//2) - bit_arr[0]
        min_val[0] = bit_arr[0]
    print(min_val)
if __name__ == '__main__':
    main()