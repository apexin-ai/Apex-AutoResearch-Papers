#!/usr/bin/env bash
# Download MAVEN event detection dataset from GitHub releases / Google Drive.
#
# Usage:
#   bash download_maven.sh [output_dir]
#
# Default output_dir: ./data/maven
#
# Data source: https://github.com/THU-KEG/MAVEN-dataset
# Google Drive: https://drive.google.com/drive/folders/19Q0lqJE6A98OLnRqQVhbX3e6rG4BVGn8
#
# The script downloads train.jsonl, valid.jsonl, test.jsonl and verifies
# that all expected files are present and non-empty.

set -euo pipefail

OUTPUT_DIR="${1:-./data/maven}"
mkdir -p "$OUTPUT_DIR"

echo "=== MAVEN Dataset Downloader ==="
echo "Output directory: $OUTPUT_DIR"

# --- Method 1: Try gdown (Google Drive) ---
download_gdrive() {
    local file_id="$1"
    local output="$2"
    if command -v gdown &>/dev/null; then
        echo "Downloading $output via gdown..."
        gdown "$file_id" -O "$output" && return 0
    fi
    if command -v python3 &>/dev/null; then
        echo "Downloading $output via python3+gdown..."
        python3 -m pip install -q gdown 2>/dev/null
        python3 -c "import gdown; gdown.download(id='$file_id', output='$output', quiet=False)" && return 0
    fi
    return 1
}

# Google Drive file IDs for MAVEN v1.0
# Folder: https://drive.google.com/drive/folders/19Q0lqJE6A98OLnRqQVhbX3e6rG4BVGn8
TRAIN_ID="1E1F5bleqAlYs17RbZvJAXVtLMFKF6VS3"
VALID_ID="1Xux7MdwfRNmE07VCpJ1jYghIz2sWlKYn"
TEST_ID="1jNt0KLHYV1Lg8SnM1lr8OYQXK-V2b5F1"

NEED_DOWNLOAD=false
for f in train.jsonl valid.jsonl test.jsonl; do
    if [[ ! -s "$OUTPUT_DIR/$f" ]]; then
        NEED_DOWNLOAD=true
        break
    fi
done

if [[ "$NEED_DOWNLOAD" == "true" ]]; then
    echo ""
    echo "Attempting Google Drive download..."

    if download_gdrive "$TRAIN_ID" "$OUTPUT_DIR/train.jsonl" && \
       download_gdrive "$VALID_ID" "$OUTPUT_DIR/valid.jsonl" && \
       download_gdrive "$TEST_ID" "$OUTPUT_DIR/test.jsonl"; then
        echo "Google Drive download complete."
    else
        echo ""
        echo "=== Automatic download failed ==="
        echo "Please download MAVEN manually:"
        echo ""
        echo "  Option A - Google Drive:"
        echo "    https://drive.google.com/drive/folders/19Q0lqJE6A98OLnRqQVhbX3e6rG4BVGn8"
        echo ""
        echo "  Option B - Tsinghua Cloud:"
        echo "    https://cloud.tsinghua.edu.cn/d/874e0ad810f34272a03b/"
        echo ""
        echo "  Download train.jsonl, valid.jsonl, test.jsonl into: $OUTPUT_DIR/"
        exit 1
    fi
else
    echo "All files already present, skipping download."
fi

# --- Verification ---
echo ""
echo "=== Verification ==="
PASS=true
for f in train.jsonl valid.jsonl test.jsonl; do
    filepath="$OUTPUT_DIR/$f"
    if [[ ! -f "$filepath" ]]; then
        echo "FAIL: $f not found"
        PASS=false
    elif [[ ! -s "$filepath" ]]; then
        echo "FAIL: $f is empty"
        PASS=false
    else
        lines=$(wc -l < "$filepath")
        size=$(du -h "$filepath" | cut -f1)
        echo "OK:   $f ($lines docs, $size)"
    fi
done

if [[ "$PASS" == "true" ]]; then
    echo ""
    echo "All files verified. Dataset ready at: $OUTPUT_DIR/"
else
    echo ""
    echo "Some files are missing or empty. Please re-download."
    exit 1
fi
