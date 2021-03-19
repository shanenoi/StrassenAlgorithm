def split_block(block):
    vertical_len = len(block[0])
    horizontal_len = len(block)

    assert vertical_len % 2 == 0
    assert horizontal_len % 2 == 0

    x11 = [ [number for number in line[0:int(vertical_len/2)]]
            for line in block[0:int(horizontal_len/2)] ]
    x12 = [ [number for number in line[int(vertical_len/2):]]
            for line in block[0:int(horizontal_len/2)] ]
    x21 = [ [number for number in line[0:int(vertical_len/2)]]
            for line in block[int(horizontal_len/2):] ]
    x22 = [ [number for number in line[int(vertical_len/2):]]
            for line in block[int(horizontal_len/2):] ]

    return x11, x12, x21, x22


def concat(block1, block2):
    result = [[]]
    if len(block1) == len(block2) == 1:
        return block1[0] + block2[0]

    for i in range(len(block1)):
        for j in range(len(block1[0])):
            result[i].append(block1[i][j] + block2[i][j])
        result.append([]) if i != len(block1) -1 else None

    return result


def strassen(block1, block2):
    if len(block1) == len(block2) == 1:
        return block1 * block2

    a11, a12, a21, a22 = split_block(block1)
    b11, b12, b21, b22 = split_block(block2)

    m1 = concat(a11, a22) * concat(b11, b22)
    m1 = concat(a11, a22) * concat(b11, b22)


a = [
        [0,1,2,3,  4,5,6,7],
        [8,9,4,2,  5,7,1,7],

        [3,2,1,0,  7,6,5,4],
        [7,6,5,4,  3,2,1,0],
]
print()
strassen(a, a)
