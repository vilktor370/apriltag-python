tag_faimly = [
    10184,
    12726,
    14425,
    22172,
    27766,
    32219,
    44809,
    62881,
    64395,
    7353,
    10442,
    59612,
    5158,
    22384,
    37459,
    46850,
    1594,
    36660,
    46272,
    20972,
    59120,
    24484,
    56643,
    6826,
    58927,
    28092,
    46827,
    56848,
    5453,
    46458     
]
rcode = 31874

def rightRotate(n, d):
 
    # In n>>d, first d bits are 0.
    # To put last 3 bits of at
    # first, do bitwise or of n>>d
    # with n <<(INT_BITS - d)
    return (n >> d)|(n << (32 - d)) & 0xFFFFFFFF

def leftRotate(n, d):
 
    # In n<<d, last d bits are 0.
    # To put first 3 bits of n at
    # last, do bitwise or of n<<d
    # with n >>(INT_BITS - d)
    return (n << d)|(n >> (32 - d))


def rotate90(self,w, d):
        """
        rotate the code(bin) 90
        :param w: code(int)
        :param d: tag family`s d(edge length)
        :return: rotate 90 point
        """
        wr = 0
        for r in range(d - 1, -1, -1):
            for c in range(self._d):
                b = r + self._d * c
                wr = wr << 1
                if ((w & (1 << b))) != 0:
                    wr |= 1
        return wr



# 0b 0111 1100 1000 0010 31874
# 0b 0010 0111 1100 1000 10184
# 0b 0011 0001 1011 0110 12726
a = 0b1100100000100111
print(bin(12726))

# for i in [0, 4, 8, 12]:
    # print(bin(leftRotate(rcode, i)), leftRotate(rcode, i))
# print(bin(rcode), bin(tag_faimly[0]))

# for tag in tag_faimly:
    # hamming_dis = bin(rcode ^ tag).count('1')
    # print(hamming_dis)