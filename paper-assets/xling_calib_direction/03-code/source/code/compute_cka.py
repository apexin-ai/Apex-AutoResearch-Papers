"""
Compute Linear CKA (Centered Kernel Alignment) between cross-lingual activations.

Measures representational similarity between English and target language activations
at each layer of an LLM, using parallel data (same samples in same order).

Input:  activation files `layer{i}_{lang}.pt`, each containing
        {"activations": Tensor(N, hidden_dim), "labels": Tensor(N,)}
Output: CSV with columns (layer, language, cka_value) + summary statistics.

Reference: Kornblith et al., "Similarity of Neural Network Representations Revisited",
           ICML 2019. https://arxiv.org/abs/1905.00414

Requires: torch
"""

import argparse
import os
import re
import sys
from pathlib import Path

import torch


def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
    """Linear CKA between two activation matrices.

    Args:
        X: (n, p) activations for language A
        Y: (n, q) activations for language B
        Both must share the same n (parallel samples in identical order).
    """
    X = X - X.mean(0)
    Y = Y - Y.mean(0)

    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2

    return (hsic_xy / (hsic_xx.sqrt() * hsic_yy.sqrt())).item()


def detect_layers(activations_dir: str) -> list[int]:
    """Auto-detect available layer indices from filenames."""
    pattern = re.compile(r"^layer(\d+)_\w+\.pt$")
    layers = set()
    for f in os.listdir(activations_dir):
        m = pattern.match(f)
        if m:
            layers.add(int(m.group(1)))
    return sorted(layers)


def load_activations(activations_dir: str, layer: int, lang: str) -> torch.Tensor:
    path = os.path.join(activations_dir, f"layer{layer}_{lang}.pt")
    data = torch.load(path, map_location="cpu", weights_only=True)
    return data["activations"].float()


def main():
    parser = argparse.ArgumentParser(description="Compute Linear CKA across languages and layers")
    parser.add_argument("--activations_dir", default="./activations", help="Directory with activation .pt files")
    parser.add_argument("--output_dir", default="./results", help="Output directory")
    parser.add_argument("--layers", default=None, help="Comma-separated layer indices (default: auto-detect)")
    parser.add_argument("--languages", nargs="+", default=["zh", "ar", "hi", "sw", "ko"], help="Target languages")
    parser.add_argument("--reference_lang", default="en", help="Reference language")
    parser.add_argument("--output_file", default="cka_matrix.csv", help="Output CSV filename")
    args = parser.parse_args()

    if not os.path.isdir(args.activations_dir):
        print(f"Error: activations_dir not found: {args.activations_dir}", file=sys.stderr)
        sys.exit(1)

    layers = [int(x) for x in args.layers.split(",")] if args.layers else detect_layers(args.activations_dir)
    if not layers:
        print("Error: no layers detected", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    output_path = os.path.join(args.output_dir, args.output_file)

    print(f"Layers: {layers}")
    print(f"Languages: {args.languages} (ref: {args.reference_lang})")

    results = []

    for layer in layers:
        ref_acts = load_activations(args.activations_dir, layer, args.reference_lang)
        for lang in args.languages:
            tgt_acts = load_activations(args.activations_dir, layer, lang)
            n = min(ref_acts.shape[0], tgt_acts.shape[0])
            cka_val = linear_cka(ref_acts[:n], tgt_acts[:n])
            results.append((layer, lang, cka_val))
            print(f"  layer {layer:2d} | {lang} | CKA = {cka_val:.6f} (n={n})")

    # Write CSV
    with open(output_path, "w") as f:
        f.write("layer,language,cka_value\n")
        for layer, lang, cka_val in results:
            f.write(f"{layer},{lang},{cka_val:.6f}\n")
    print(f"\nResults saved to {output_path}")

    # Summary
    print("\n=== Per-language mean CKA ===")
    for lang in args.languages:
        vals = [c for _, l, c in results if l == lang]
        print(f"  {lang}: {sum(vals)/len(vals):.6f}")

    print("\n=== Per-layer mean CKA ===")
    for layer in layers:
        vals = [c for la, _, c in results if la == layer]
        print(f"  layer {layer:2d}: {sum(vals)/len(vals):.6f}")


if __name__ == "__main__":
    main()
