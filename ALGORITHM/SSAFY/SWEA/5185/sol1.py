T = int(input())
hex_to_bi = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

for tc in range(1, T+1):
    N, s = input().split()
    new_s = ''
    for char in s:
        new_s += hex_to_bi[char]
    print(f'#{tc} {new_s}')