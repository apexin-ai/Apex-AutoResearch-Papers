import os
import hashlib
import shutil
from collections import defaultdict

TRAIN_DIR = "/root/autodl-tmp/imagenet100/train"
VAL_DIR = "/root/autodl-tmp/imagenet100/val"
OUT_DIR = "/root/autodl-tmp/imagenet100_deduped"

def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def get_classes(d):
    return sorted([c for c in os.listdir(d) if os.path.isdir(os.path.join(d, c))])

print("Computing val hashes...")
val_hashes = set()
val_classes = get_classes(VAL_DIR)
val_total = 0
for cls in val_classes:
    cls_dir = os.path.join(VAL_DIR, cls)
    for fname in os.listdir(cls_dir):
        fpath = os.path.join(cls_dir, fname)
        if os.path.isfile(fpath):
            val_hashes.add(md5_file(fpath))
            val_total += 1
print(f"Val images: {val_total}, unique hashes: {len(val_hashes)}")

print("Computing train hashes and finding overlaps...")
train_classes = get_classes(TRAIN_DIR)
overlap_count = 0
train_total = 0
keep_files = defaultdict(list)  # cls -> [(fname, fpath)]

for cls in train_classes:
    cls_dir = os.path.join(TRAIN_DIR, cls)
    for fname in sorted(os.listdir(cls_dir)):
        fpath = os.path.join(cls_dir, fname)
        if not os.path.isfile(fpath):
            continue
        train_total += 1
        h = md5_file(fpath)
        if h in val_hashes:
            overlap_count += 1
        else:
            keep_files[cls].append((fname, fpath))

print(f"\n=== Dedup Report ===")
print(f"Original train size: {train_total}")
print(f"Overlapping images found: {overlap_count}")
deduped_size = train_total - overlap_count
print(f"Deduped train size: {deduped_size}")

# Copy deduped train + original val to output
print("\nCopying deduped data...")
os.makedirs(OUT_DIR, exist_ok=True)
train_out = os.path.join(OUT_DIR, "train")
val_out = os.path.join(OUT_DIR, "val")

# Copy deduped train
per_class_counts = {}
for cls in train_classes:
    cls_out = os.path.join(train_out, cls)
    os.makedirs(cls_out, exist_ok=True)
    count = 0
    for fname, fpath in keep_files.get(cls, []):
        shutil.copy2(fpath, os.path.join(cls_out, fname))
        count += 1
    per_class_counts[cls] = count

# Symlink val (no changes needed)
if os.path.exists(val_out):
    if os.path.islink(val_out):
        os.unlink(val_out)
    else:
        shutil.rmtree(val_out)
os.symlink(os.path.realpath(VAL_DIR), val_out)

# Verify no overlap
print("Verifying zero overlap...")
verify_hashes = set()
for cls in get_classes(train_out):
    cls_dir = os.path.join(train_out, cls)
    for fname in os.listdir(cls_dir):
        fpath = os.path.join(cls_dir, fname)
        if os.path.isfile(fpath):
            verify_hashes.add(md5_file(fpath))
verify_overlap = len(verify_hashes & val_hashes)

min_count = min(per_class_counts.values())
max_count = max(per_class_counts.values())

print(f"Overlap after dedup: {verify_overlap}")
print(f"Min samples per class: {min_count}")
print(f"Max samples per class: {max_count}")
print(f"Data saved to: {OUT_DIR}")
