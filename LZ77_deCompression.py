from LZ77_Compression import compress

def decompress(tags):
    output = []

    for offset, length, char in tags:
        start = len(output) - offset

        for k in range(length):
            output.append(output[start + k])

        if char != "":
            output.append(char)

    return "".join(output)


originalData = list(input("Enter your Text to decompression:"))
tags = compress(originalData)
print("Tags:", tags)

result = decompress(tags)
print("Decompressed:", result)
print("Same as input?", result == "".join(originalData))
