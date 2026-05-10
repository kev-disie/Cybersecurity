#!/usr/bin/env python3

import sys

# Common zero-width characters
ZW_CHARS = {
    "\u200b": "ZWSP",   # 0?
    "\u200c": "ZWNJ",   # 1?
    "\u200d": "ZWJ",
    "\ufeff": "BOM",
    "\u2060": "WJ",
}

def extract_hidden(data):
    return [c for c in data if c in ZW_CHARS]

def show_stats(hidden):
    print("[+] Detected zero-width characters:")
    for k, v in ZW_CHARS.items():
        count = hidden.count(k)
        if count:
            print(f"  {v} ({repr(k)}): {count}")
    print()

def try_binary(hidden):
    print("[+] Trying binary decoding...")

    unique = list(set(hidden))

    if len(unique) < 2:
        print("[-] Not enough symbols for binary\n")
        return

    a, b = unique[0], unique[1]

    # Try both mappings
    for mapping in [(a, b), (b, a)]:
        bits = ''.join('0' if c == mapping[0] else '1' for c in hidden)

        for size in [8, 7]:
            out = ""
            for i in range(0, len(bits), size):
                chunk = bits[i:i+size]
                if len(chunk) == size:
                    try:
                        out += chr(int(chunk, 2))
                    except:
                        pass

            print(f"\n--- Mapping {ZW_CHARS.get(mapping[0], '?')}=0, {ZW_CHARS.get(mapping[1], '?')}=1 | {size}-bit ---")
            print(out)

def try_counts(data):
    print("\n[+] Trying count-based decoding...")

    counts = []
    count = 0

    for c in data:
        if c in ZW_CHARS:
            count += 1
        else:
            if count > 0:
                counts.append(count)
                count = 0

    decoded = ''.join(chr(c) for c in counts if 32 <= c < 127)

    print("\n--- Count decoding ---")
    print(decoded)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} file.txt")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        data = f.read()

    hidden = extract_hidden(data)

    if not hidden:
        print("[-] No zero-width characters found")
        return

    show_stats(hidden)

    try_binary(hidden)
    try_counts(data)

if __name__ == "__main__":
    main()
