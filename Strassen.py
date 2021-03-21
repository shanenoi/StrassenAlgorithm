import re


def is_number(content:object) -> bool:
    return bool(re.search(r"^(\d+\.\d+)|(\d+)$", str(content)))


def shape(array:list) -> list:
    shapes = []
    temp_var = array
    while type(temp_var) in [list, tuple] and len(temp_var) != 0:
        shapes.append(len(temp_var))
        temp_var = temp_var[0]
    return shapes


def split_block(block:list) -> list:
    if len(shape(block)) == 1:
        return block

    vertical_len = len(block[0])
    horizontal_len = len(block)

    x11 = [ [number for number in line[0:int(vertical_len/2)]]
            for line in block[0:int(horizontal_len/2)] ]

    x12 = [ [number for number in line[int(vertical_len/2):]]
            for line in block[0:int(horizontal_len/2)] ]

    x21 = [ [number for number in line[0:int(vertical_len/2)]]
            for line in block[int(horizontal_len/2):] ]

    x22 = [ [number for number in line[int(vertical_len/2):]]
            for line in block[int(horizontal_len/2):] ]

    return x11, x12, x21, x22


def concat(block1:object, block2:object, block1_prefix:int = 1, block2_prefix:int = 1) -> list:
    if is_number(block1) and is_number(block2):
        return block1_prefix * block1 + block2_prefix * block2

    return [ concat(_block1, _block2, block1_prefix, block2_prefix)
        for _block1, _block2 in zip(block1, block2)
    ]


# i have no idea to name the returing type 
def strassen(block1:list, block2:list) -> None:
    if type(block1) == type(block2) == int:
        return block1 * block2

    a11, a12, a21, a22 = split_block(block1)
    b11, b12, b21, b22 = split_block(block2)

    print(a11, a12, a21, a22)
    print(b11, b12, b21, b22)

    m1 = strassen(concat(a11, a22), concat(b11, b22))
    m2 = strassen(concat(a21, a22), b11)
    m3 = strassen(a11, concat(b12, b22, block2_prefix = -1))
    m4 = strassen(a22, concat(b21, b11, block2_prefix = -1))
    m5 = strassen(concat(a11, a12), b22)
    m6 = strassen(concat(a12, a11, block2_prefix = -1), concat(b11, b12))
    m7 = strassen(concat(a11, a22, block2_prefix = -1), concat(b21, b22))


def test_concat() -> None:
    assert(concat([1], [2]) == [3])
    assert(concat([2], [2], block2_prefix = -1) == [0])

def test_shape() -> None:
    assert(shape([1, 2]) == [2])
    assert(shape([[1], [1]]) == [2, 1])

def test_strassen() -> None:
    assert(strassen(1,2))


def main():
    # a = [
    #         [0,1,2,3,  4,5,6,7],
    #         [8,9,4,2,  5,7,1,7],

    #         [3,2,1,0,  7,6,5,4],
    #         [7,6,5,4,  3,2,1,0],
    # ]

    a = [
            [0,7],
            [8,7]
    ]
    print()
    strassen(a, a)


if __name__ == '__main__':
    main()
