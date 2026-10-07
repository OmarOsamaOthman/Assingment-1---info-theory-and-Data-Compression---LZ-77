import struct

TAG_FORMAT = ">HHc"          # offset: 2 bytes, length: 2 bytes, char: 1 byte
TAG_SIZE = struct.calcsize(TAG_FORMAT)   # = 5 bytes


#read .bin file -> tags list
def read_tags(bin_path="compressed_output.bin"):
    tags = []
    with open(bin_path, "rb") as f:
        data = f.read()

    for i in range(0, len(data), TAG_SIZE):
        chunk = data[i:i + TAG_SIZE]
        offset, length, char_byte = struct.unpack(TAG_FORMAT, chunk)

        char = "" if char_byte == b"\x00" else char_byte.decode("utf-8")

        tags.append([offset, length, char])

    return tags


#tags -> text (handles redundancy / overlap)
def decompress(tags):
    output = []

    for offset, length, char in tags:
        start = len(output) - offset           # where to start copying from

        for k in range(length):                # copy character by character
            output.append(output[start + k])   # handles overlapping/repetitive matches

        if char != "":
            output.append(char)

    return "".join(output)


#full pipeline
def decompress_file(bin_path="compressed_output.bin", output_path="decompressed.txt"):
    tags = read_tags(bin_path)
    print("Tags:", tags)

    text = decompress(tags)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("Decompressed text:", text)
    print(f"Saved to '{output_path}'")
    return text


if __name__ == "__main__":
    decompress_file()
