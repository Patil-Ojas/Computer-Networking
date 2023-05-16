
def adder(a, b):
    carry = 0
    result = ""
    max_length = max(len(a), len(b))

    a = a.zfill(max_length)
    b = b.zfill(max_length)

    for i in range(max_length - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry

        sum_bit = bit_sum % 2
        carry = bit_sum // 2

        result = str(sum_bit) + result

    if carry == 1:
        # print(result)
        result = adder(result[0:7], "000001")

    return result


t_data = str(input())
# t_data = "000111000111000111"
# t_data = "111000111000111000"
blocks = []

for i in range(1,4):
    blocks.append(str(t_data[(i-1)*6:6*i]))


temp = adder(blocks[0],blocks[1])
checksum = adder(temp, blocks[2])

checksum = checksum.replace("1", "2")
checksum = checksum.replace("0", "1")
checksum = checksum.replace("2", "0")

print(checksum)
final = t_data+checksum
print(final)
