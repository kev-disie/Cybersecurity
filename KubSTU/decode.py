#!/usr/bin/env python3

import sys

ZWSP = "\u200b"

def extract_bits(data):
    bits = ""

    for ch in data:
        if ch == ZWSP:
            bits += "1"
        else:
            # treat any visible char as separator → optional 0
            bits += "0"

    return bits


def bits_to_bytes(bits):
    # Trim to full bytes
    bits = bits[:len(bits) - (len(bits) % 8)]

    result = bytearray()

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        result.append(int(byte, 2))

    return result


def main(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    bits = extract_bits(data)

    print(f"[+] Total bits: {len(bits)}")

    decoded = bits_to_bytes(bits)

    try:
        print("[+] Decoded text:")
        print(decoded.decode("utf-8"))
    except:
        print("[!] Raw bytes:")
        print(decoded)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} ancient_note.txt")
        sys.exit(1)

    main(sys.argv[1])
