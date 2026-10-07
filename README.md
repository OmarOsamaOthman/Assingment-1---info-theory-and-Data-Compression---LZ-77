# LZ77 Compression & Decompression Assignment

This repository contains a complete Python implementation of the **LZ77 (Lempel-Ziv 1977)** data compression algorithm. The project compresses UTF-8 text files into a compact binary format using sliding window pattern matching and accurately reconstructs the original file during decompression.

---

##  Assignment Overview

The primary objective of this assignment is to understand and implement dictionary-based data compression:
1. **LZ77 Encoding:** Identify repeating character sequences within a sliding history window and encode them as `(offset, length, next_char)` tokens.
2. **Binary Output Serialization:** Compress human-readable text into a structured binary file using fixed-width byte packing (`struct`).
3. **LZ77 Decoding:** Parse the packed binary tokens and reconstruct the exact original string character-by-character without information loss.

---

##  Core Concepts

### 1. Sliding Window Model
The algorithm moves sequentially across the source text using two buffers:
* **Search Window (SW):** Historical window containing previously processed characters.
* **Lookahead Window (LW):** Upcoming characters waiting to be compressed.

### 2. LZ77 Tag Structure
When a match is found between the search and lookahead windows, LZ77 generates a 3-part token:
$$\langle \text{Offset}, \text{Length}, \text{Next Character} \rangle$$

* **Offset:** How many positions back in the Search Window the match starts.
* **Length:** The number of matching characters found.
* **Next Character:** The character immediately following the matched sequence in the Lookahead Window.

### 3. Self-Overlapping Matches
The implementation handles redundant repeating patterns (e.g., `"AAAAAA"` or `"ABCABCABC"`) where `Length > Offset` by dynamically cycling through the search pattern during compression and appending characters sequentially during decompression.

---

##  Binary Storage Format

To optimize space, tags are written to disk as raw 5-byte binary chunks using Python's `struct` package (`>HHc`):

| Tag Component | Data Type | Size | Description |
| :--- | :--- | :--- | :--- |
| **Offset** | Unsigned Short (`>H`) | **2 Bytes** | Distance back into history (0–65,535) |
| **Length** | Unsigned Short (`>H`) | **2 Bytes** | Length of the matched pattern (0–65,535) |
| **Next Char** | Character (`c`) | **1 Byte** | Next unmatched character (`\x00` if empty) |
| **Total Tag Size** | — | **5 Bytes** | **Fixed binary payload per tag** |

---
