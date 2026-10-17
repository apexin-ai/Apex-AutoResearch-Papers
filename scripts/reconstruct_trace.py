#!/usr/bin/env python3
"""Concatenate a split sanitized trace archive and verify its manifest."""
from __future__ import annotations
import csv, hashlib, sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 3:
        print(f"usage: {Path(sys.argv[0]).name} PARTS_DIR OUTPUT_TAR_GZ", file=sys.stderr)
        return 2
    parts_dir, output = Path(sys.argv[1]), Path(sys.argv[2])
    rows = list(csv.DictReader((parts_dir / 'manifest.csv').open(newline='', encoding='utf-8')))
    digest = hashlib.sha256()
    with output.open('wb') as dst:
        for row in rows:
            part = parts_dir / row['part']
            data = part.read_bytes()
            if len(data) != int(row['bytes']) or hashlib.sha256(data).hexdigest() != row['sha256']:
                raise SystemExit(f"hash/size mismatch: {part}")
            dst.write(data)
            digest.update(data)
    print(f"reconstructed {output} ({output.stat().st_size:,} bytes)")
    print(f"sha256 {digest.hexdigest()}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
