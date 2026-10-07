import struct

TAG_FORMAT = ">HHc"          # offset: 2 bytes, length: 2 bytes, next byte: 1 byte
TAG_SIZE = struct.calcsize(TAG_FORMAT)   # = 5 bytes


# read .bin file -> tags list of [offset, length, next_byte]
def read_tags(bin_path="compressed_output.bin"):
    with open(bin_path, "rb") as f:
        data = f.read()

    if len(data) % TAG_SIZE != 0:
        raise ValueError("Corrupted file: size is not a multiple of 5 bytes")

    tags = []
    for i in range(0, len(data), TAG_SIZE):
        offset, length, next_byte = struct.unpack(TAG_FORMAT, data[i:i + TAG_SIZE])
        tags.append([offset, length, next_byte])
    return tags


# tags -> text (works on bytes, so non-ASCII text is safe)
def decompress(tags):
    output = bytearray()

    for offset, length, next_byte in tags:
        if offset > len(output):
            raise ValueError("Corrupted file: offset points before the start")

        start = len(output) - offset
        for k in range(length):                 # copy one by one (handles overlap)
            output.append(output[start + k])

        if next_byte != b"\x00":                # \x00 = no next char (end of data)
            output += next_byte

    return output.decode("utf-8")


# full pipeline
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
