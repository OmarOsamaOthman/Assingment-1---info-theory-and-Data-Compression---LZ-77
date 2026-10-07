import os
from Comp import compress
from Decomp import decompress_file

def handle_compress():
    file_path = input("\nEnter the path of the file to compress: ").strip()
    if not os.path.exists(file_path):
        print(f"Error: File path '{file_path}' does not exist.")
        return None

    out_bin = input("Enter output binary filename [default: compressed_output.bin]: ").strip()
    if not out_bin:
        out_bin = "compressed_output.bin"

    with open(file_path, "r", encoding="utf-8") as file:
        originalData = file.read()

    print("\nCompressing file...")
    tags = compress(originalData)
    
    if out_bin != "compressed_output.bin" and os.path.exists("compressed_output.bin"):
        os.replace("compressed_output.bin", out_bin)

    print("\nCompression Successful!")
    print(f"• Generated Tags: {tags}")
    print(f"• Saved output file to: {out_bin}")
    
    return out_bin


def handle_decompress(default_bin="compressed_output.bin"):
    print(f"\n[INFO] Suggested file to decompress: {default_bin}")
    bin_path = input(f"Enter path of binary file [default: {default_bin}]: ").strip()
    if not bin_path:
        bin_path = default_bin

    if not os.path.exists(bin_path):
        print(f"Error: Binary file '{bin_path}' does not exist.")
        return

    out_txt = input("Enter path for decompressed text output [default: decompressed.txt]: ").strip()
    if not out_txt:
        out_txt = "decompressed.txt"

    print("\nDecompressing file...")
    decompress_file(bin_path=bin_path, output_path=out_txt)
    print("\nDecompression Successful!")
    print(f"• Restored text saved to: {out_txt}")


def main():
    last_compressed_bin = "compressed_output.bin"

    while True:
        print("\n" + "=" * 40)
        print("          LZ77 COMPRESSOR SYSTEM          ")
        print("=" * 40)
        print("1. Compress File")
        print("2. Decompress File")
        print("3. Full Pipeline (Compress & Decompress)")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            out_file = handle_compress()
            if out_file:
                last_compressed_bin = out_file

        elif choice == "2":
            handle_decompress(default_bin=last_compressed_bin)

        elif choice == "3":
            out_file = handle_compress()
            if out_file:
                last_compressed_bin = out_file
                handle_decompress(default_bin=last_compressed_bin)

        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()
