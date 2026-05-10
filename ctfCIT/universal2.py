#!/usr/bin/env python3

import sys
import base64
import string
from collections import Counter

ZW_CHARS = [
    "\u200b",  # ZWSP
    "\u200c",  # ZWNJ
    "\u200d",  # ZWJ
    "\ufeff",  # BOM
    "\u2060",  # Word Joiner
]

# -------------------------
# Utils
# -------------------------

def is_printable(s):
    return all(c in string.printable for c in s)

def try_base64(s):
    try:
        decoded = base64.b64decode(s).decode()
        return decoded if is_printable(decoded) else None
    except:
        return None

def try_hex(s):
    try:
        decoded = bytes.fromhex(s).decode()
        return decoded if is_printable(decoded) else None
    except:
        return None

# -------------------------
# Extraction
# -------------------------

def extract_hidden(data):
    return [c for c in data if c in ZW_CHARS]

# -------------------------
# Frequency Analysis
# -------------------------

def analyze_frequency(hidden):
    print("\n[+] Frequency Analysis:")
    freq = Counter(hidden)
    for k, v in freq.items():
        print(f"  U+{ord(k):04X}: {v}")
    print()

# -------------------------
# Binary decoding (2 symbols)
# -------------------------

def try_binary(hidden):
    print("[+] Trying binary decoding...")

    unique = list(set(hidden))
    if len(unique) < 2:
        print("[-] Not enough symbols\n")
        return []

    results = []

    for a, b in [(unique[0], unique[1]), (unique[1], unique[0])]:
        bits = ''.join('0' if c == a else '1' for c in hidden)

        for size in [8, 7]:
            out = ""
            for i in range(0, len(bits), size):
                chunk = bits[i:i+size]
                if len(chunk) == size:
                    try:
                        out += chr(int(chunk, 2))
                    except:
                        pass

            results.append(out)
            print(f"\n--- {ord(a):04X}=0, {ord(b):04X}=1 | {size}-bit ---")
            print(out)

    return results

# -------------------------
# Multi-symbol (2-bit encoding)
# -------------------------

def try_multisymbol(hidden):
    print("\n[+] Trying multi-symbol decoding (2-bit)...")

    unique = list(set(hidden))
    if len(unique) < 4:
        print("[-] Not enough symbols for 2-bit encoding\n")
        return []

    mapping = dict(zip(unique[:4], ["00", "01", "10", "11"]))

    bits = ''.join(mapping[c] for c in hidden if c in mapping)

    out = ""
    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) == 8:
            try:
                out += chr(int(chunk, 2))
            except:
                pass

    print("\n--- 2-bit decoded ---")
    print(out)

    return [out]

# -------------------------
# Count-based decoding
# -------------------------

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

    out = ''.join(chr(c) for c in counts if 32 <= c < 127)

    print("\n--- Count decoded ---")
    print(out)

    return [out]

# -------------------------
# Post-processing
# -------------------------

def post_process(results):
    print("\n[+] Post-processing (Base64 / Hex detection)...")

    for r in results:
        if not r.strip():
            continue

        # Base64
        b64 = try_base64(r.strip())
        if b64:
            print("\n[✔] Base64 decoded:")
            print(b64)

        # Hex
        hx = try_hex(r.strip())
        if hx:
            print("\n[✔] Hex decoded:")
            print(hx)

# -------------------------
# Main
# -------------------------

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

    print(f"[+] Found {len(hidden)} hidden characters")

    analyze_frequency(hidden)

    results = []
    results += try_binary(hidden)
    results += try_multisymbol(hidden)
    results += try_counts(data)

    post_process(results)

if __name__ == "__main__":
    main()
