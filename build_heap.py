# python3
# Kirills Vasiljevs 221RDB427

def swap(i, data, swaps):
    minCon = i

    # left condition
    leftCon = 2 * i + 1

    # right condition
    rightCon = 2 * i + 2

# If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.
    if rightCon < len(data) and  data[minCon] > data[rightCon]:
        minCon = rightCon

# If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
    if leftCon < len(data) and data[minCon] > data[leftCon]:
        minCon = leftCon

    if i != minCon:
        swaps.append((i, minCon))

        el = data[i]
        data[i] = data[minCon]
        data[minCon] = el

        swap(minCon, data, swaps)

def build_heap(data):
    swaps = []

    for i in range(len(data), -1, -1):
        swap(i, data, swaps)

    return swaps


def main():
    inputType = input()

    if 'I' in inputType:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in inputType:
        fileName = input()

        # Check a name of test file
        if 'a' in fileName:
            return
        
        # open a test file
        with open("./tests/%s" % (fileName), "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split(" ")))
    else:
        return

# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
    assert len(data) == n

    swaps = build_heap(data)

    # print a result
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()