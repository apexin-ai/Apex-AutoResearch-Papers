"""
CARC TEAL calibration: collect per-layer MLP activation histograms and compute
magnitude thresholds at 40% and 55% sparsity levels.

Input:  DeepSeek-R1-Distill-Qwen-14B + calibration dataset (default 300 samples)
Output: JSON file with per-layer, per-component thresholds:
        { "layer_idx": { "component": { "40": val, "55": val } } }

Usage:
    python carc_calibrate.py --output thresholds.json
    python carc_calibrate.py --dry-run  # 2 samples, 2 layers only
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

from carc_utils import load_eval_data, threshold_from_histogram

MODEL_ID = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
SPARSITY_LEVELS = [0.40, 0.55]


def parse_args():
    p = argparse.ArgumentParser(
        description="CARC TEAL calibration: activation histograms → sparsity thresholds."
    )
    p.add_argument("--model", default=MODEL_ID, help="HF model name or local path")
    p.add_argument("--output", default="thresholds.json", help="Output JSON path")
    p.add_argument("--num-samples", type=int, default=300, help="Calibration samples")
    p.add_argument("--seq-len", type=int, default=2048, help="Sequence length")
    p.add_argument("--dataset", default="c4", choices=["c4", "wikitext", "alpaca"])
    p.add_argument("--batch-size", type=int, default=1, help="Forward pass batch size")
    p.add_argument("--num-bins", type=int, default=1000, help="Histogram bins")
    p.add_argument("--dry-run", action="store_true", help="2 samples, 2 layers only")
    p.add_argument("--dtype", default="bf16", choices=["fp16", "bf16"])
    return p.parse_args()


# ---------------------------------------------------------------------------
# Histogram collector
# ---------------------------------------------------------------------------

class LayerHistogram:
    """
    Incremental absolute-value histogram for one (layer, component) pair.

    Bin range is fixed after the first batch (1.2x observed max).
    Values exceeding the range in later batches go into the last bin —
    acceptable since we only compute low-percentile thresholds (40%/55%).
    """

    def __init__(self, num_bins: int):
        self.num_bins = num_bins
        self.counts: Optional[torch.Tensor] = None
        self.bin_edges: Optional[torch.Tensor] = None
        self._range_set = False

    def update(self, x_abs_flat: torch.Tensor):
        if not self._range_set:
            vmax = x_abs_flat.max().item() * 1.2 + 1e-6
            self.bin_edges = torch.linspace(0.0, vmax, self.num_bins + 1)
            self.counts = torch.zeros(self.num_bins, dtype=torch.float64)
            self._range_set = True

        vmax = self.bin_edges[-1].item()
        n_outlier = (x_abs_flat > vmax).sum().item()
        x_clamped = x_abs_flat.clamp(max=vmax - 1e-10).cpu()
        self.counts += torch.histc(x_clamped, bins=self.num_bins, min=0.0, max=vmax).double()
        if n_outlier > 0:
            self.counts[-1] += n_outlier


MLP_COMPONENTS = ("gate_proj", "up_proj", "down_proj")


class HistogramCollector:
    """Registers forward hooks on MLP projection inputs and accumulates histograms."""

    def __init__(self, model, num_bins: int, max_layers: int):
        self.histograms: Dict[str, LayerHistogram] = {}
        self._hooks = []

        for i in range(max_layers):
            mlp = model.model.layers[i].mlp
            for name in MLP_COMPONENTS:
                key = f"{i}/{name}"
                hist = LayerHistogram(num_bins)
                self.histograms[key] = hist
                module = getattr(mlp, name)
                self._hooks.append(module.register_forward_hook(self._make_hook(hist)))

    @staticmethod
    def _make_hook(hist: LayerHistogram):
        def fn(_module, inp, _out):
            x = inp[0].detach().float().abs().reshape(-1)
            hist.update(x)
        return fn

    def remove_hooks(self):
        for h in self._hooks:
            h.remove()
        self._hooks.clear()

    def compute_thresholds(self) -> Dict[int, Dict[str, Dict[str, float]]]:
        result: Dict[int, Dict[str, Dict[str, float]]] = {}
        for key, hist in self.histograms.items():
            layer_str, comp = key.split("/")
            layer_idx = int(layer_str)
            result.setdefault(layer_idx, {}).setdefault(comp, {})
            for s in SPARSITY_LEVELS:
                t = threshold_from_histogram(hist.counts, hist.bin_edges, s)
                result[layer_idx][comp][str(int(s * 100))] = round(t, 6)
        return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    dtype = torch.float16 if args.dtype == "fp16" else torch.bfloat16

    if args.dry_run:
        args.num_samples = 2
        print("[DRY RUN] 2 samples, 2 layers")

    print(f"Loading tokenizer: {args.model}")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)

    print(f"Loading model: {args.model} ({args.dtype})")
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True
    )
    model.eval()

    num_layers = len(model.model.layers)
    max_layers = 2 if args.dry_run else num_layers
    assert hasattr(model.model.layers[0].mlp, "gate_proj"), (
        f"Expected Qwen2-style MLP (gate_proj/up_proj/down_proj); "
        f"got {type(model.model.layers[0].mlp)}"
    )
    print(f"Layers: {num_layers} total, calibrating {max_layers}")

    print(f"Loading {args.num_samples} samples from {args.dataset}")
    split = "train" if args.dataset == "alpaca" else "validation"
    samples = load_eval_data(
        dataset_name=args.dataset,
        num_samples=args.num_samples,
        seq_len=args.seq_len,
        tokenizer=tokenizer,
        split=split,
    )
    print(f"Got {len(samples)} samples")

    collector = HistogramCollector(model, args.num_bins, max_layers)

    print("Running calibration forward passes...")
    with torch.no_grad():
        for i in tqdm(range(0, len(samples), args.batch_size), desc="Calibrating"):
            batch = torch.stack(samples[i : i + args.batch_size]).to(model.device)
            model(batch, use_cache=False)

    collector.remove_hooks()
    thresholds = collector.compute_thresholds()

    out = {str(k): v for k, v in sorted(thresholds.items())}
    Path(args.output).write_text(json.dumps(out, indent=2))
    print(f"\nThresholds saved to {args.output}")

    for layer_idx in sorted(thresholds)[:5]:
        for comp, vals in thresholds[layer_idx].items():
            print(f"  Layer {layer_idx:2d} {comp:10s}: 40%={vals['40']:.4f}  55%={vals['55']:.4f}")
    if len(thresholds) > 5:
        print(f"  ... ({len(thresholds)} layers total)")


if __name__ == "__main__":
    main()
