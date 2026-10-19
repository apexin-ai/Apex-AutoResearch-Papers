#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch


ROOT = Path(os.environ.get("AUTOREP_ROOT", "."))
REPO_DIR = ROOT / "repositories/VAR"
DATA_ROOT = ROOT / "data/paper_exact/var_imagenet256"


def dump_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def npz_image_array(path: Path) -> np.ndarray:
    data = np.load(path, mmap_mode="r")
    for key in data.files:
        arr = data[key]
        if arr.ndim == 4:
            return arr
    raise ValueError(f"no 4D image array found in {path}")


def select_images(arr: np.ndarray, max_items: int, seed: int, stride: int = 1) -> np.ndarray:
    n = min(int(max_items), int(arr.shape[0]))
    if stride > 1:
        idx = (np.arange(n, dtype=np.int64) * stride) % arr.shape[0]
    else:
        rng = np.random.default_rng(seed)
        idx = rng.choice(arr.shape[0], size=n, replace=False)
    images = np.asarray(arr[idx])
    if images.shape[1] == 3:
        images = np.transpose(images, (0, 2, 3, 1))
    return images.astype(np.uint8, copy=False)


def generate_var_images(
    *,
    cfg: float,
    top_k: int,
    top_p: float,
    more_smooth: bool,
    seed: int,
    num_classes: int,
    samples_per_class: int,
    batch_size: int,
    device: str,
) -> np.ndarray:
    sys.path.insert(0, str(REPO_DIR))
    from models import build_vae_var

    torch.backends.cuda.matmul.allow_tf32 = True
    torch.backends.cudnn.allow_tf32 = True
    dev = torch.device(device)
    depth = 16
    patch_nums = (1, 2, 3, 4, 5, 6, 8, 10, 13, 16)
    vae, var = build_vae_var(
        device=dev,
        patch_nums=patch_nums,
        depth=depth,
        shared_aln=False,
        flash_if_available=True,
        fused_if_available=True,
    )
    vae_ckpt = torch.load(DATA_ROOT / "checkpoints/vae_ch160v4096z32.pth", map_location="cpu")
    var_ckpt = torch.load(DATA_ROOT / "checkpoints/var_d16.pth", map_location="cpu")
    vae.load_state_dict(vae_ckpt, strict=True)
    var.load_state_dict(var_ckpt, strict=True)
    vae.eval()
    var.eval()

    labels = np.repeat(np.arange(num_classes, dtype=np.int64), samples_per_class)
    images: list[np.ndarray] = []
    with torch.inference_mode():
        for start in range(0, len(labels), batch_size):
            chunk = labels[start : start + batch_size]
            label_b = torch.tensor(chunk, dtype=torch.long, device=dev)
            out = var.autoregressive_infer_cfg(
                B=len(chunk),
                label_B=label_b,
                cfg=float(cfg),
                top_k=int(top_k),
                top_p=float(top_p),
                g_seed=int(seed + start),
                more_smooth=bool(more_smooth),
            )
            out = (out.add(1).mul_(127.5)).clamp_(0, 255).to(torch.uint8)
            images.append(out.permute(0, 2, 3, 1).cpu().numpy())
    return np.concatenate(images, axis=0)


def load_detector(path: Path, device: str):
    detector = torch.jit.load(str(path), map_location=device).eval()
    for param in detector.parameters():
        param.requires_grad_(False)
    return detector


def extract_features(images_nhwc: np.ndarray, detector_path: Path, batch_size: int, device: str) -> torch.Tensor:
    detector = load_detector(detector_path, device)
    feats = []
    for start in range(0, len(images_nhwc), batch_size):
        batch = images_nhwc[start : start + batch_size]
        tensor = torch.from_numpy(np.transpose(batch, (0, 3, 1, 2))).to(device=device, dtype=torch.uint8)
        with torch.inference_mode():
            try:
                out = detector(tensor, return_features=True)
            except Exception:
                out = detector(tensor)
        if isinstance(out, (tuple, list)):
            out = out[-1]
        feats.append(out.detach().float().cpu())
    return torch.cat(feats, dim=0)


def fid_from_features(a: torch.Tensor, b: torch.Tensor, mode: str) -> float:
    a = a.double()
    b = b.double()
    mu_a = a.mean(dim=0)
    mu_b = b.mean(dim=0)
    diff = (mu_a - mu_b).pow(2).sum()
    if mode == "diag":
        # The benchmark uses small standard-budget subsets, so use the
        # population variance to keep the metric finite even for tiny smoke runs.
        var_a = a.var(dim=0, unbiased=False).clamp_min(0)
        var_b = b.var(dim=0, unbiased=False).clamp_min(0)
        cov_term = (var_a + var_b - 2.0 * torch.sqrt((var_a * var_b).clamp_min(0))).sum()
        return float((diff + cov_term).item())
    ca = torch.cov(a.T)
    cb = torch.cov(b.T)
    prod = ca @ cb
    eigvals = torch.linalg.eigvals(prod).real.clamp_min(0)
    covmean_trace = torch.sqrt(eigvals).sum()
    value = diff + torch.trace(ca) + torch.trace(cb) - 2.0 * covmean_trace
    return float(value.item())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--sample-npz", default=str(DATA_ROOT / "samples/var_d16_cfg1.5_topk900_topp0.96_50k.npz"))
    parser.add_argument("--ref-npz", default=str(DATA_ROOT / "fid_refs/VIRTUAL_imagenet256_labeled.npz"))
    parser.add_argument("--detector", default=str(DATA_ROOT / "detectors/inception-2015-12-05.pt"))
    parser.add_argument("--max-items", type=int, default=int(os.environ.get("VAR_MAX_ITEMS", "64")))
    parser.add_argument("--feature-batch-size", type=int, default=16)
    parser.add_argument("--fid-mode", choices=["diag", "full"], default=os.environ.get("VAR_FID_MODE", "diag"))
    parser.add_argument("--device", default=os.environ.get("VAR_CUDA_DEVICE", "cuda:0" if torch.cuda.is_available() else "cpu"))
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--stride", type=int, default=1)
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--cfg", type=float, default=1.5)
    parser.add_argument("--top-k", type=int, default=900)
    parser.add_argument("--top-p", type=float, default=0.96)
    parser.add_argument("--more-smooth", action="store_true")
    parser.add_argument("--num-classes", type=int, default=int(os.environ.get("VAR_NUM_CLASSES", "16")))
    parser.add_argument("--samples-per-class", type=int, default=int(os.environ.get("VAR_SAMPLES_PER_CLASS", "2")))
    parser.add_argument("--sample-batch-size", type=int, default=int(os.environ.get("VAR_SAMPLE_BATCH_SIZE", "8")))
    args = parser.parse_args()

    started = time.time()
    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    ref_arr = npz_image_array(Path(args.ref_npz))
    ref_images = select_images(ref_arr, args.max_items, seed=args.seed + 1009, stride=args.stride)

    if args.generate:
        sample_images = generate_var_images(
            cfg=args.cfg,
            top_k=args.top_k,
            top_p=args.top_p,
            more_smooth=args.more_smooth,
            seed=args.seed,
            num_classes=args.num_classes,
            samples_per_class=args.samples_per_class,
            batch_size=args.sample_batch_size,
            device=args.device,
        )
        if len(sample_images) > args.max_items:
            sample_images = sample_images[: args.max_items]
    else:
        sample_arr = npz_image_array(Path(args.sample_npz))
        sample_images = select_images(sample_arr, args.max_items, seed=args.seed, stride=args.stride)

    n = min(len(ref_images), len(sample_images), args.max_items)
    ref_images = ref_images[:n]
    sample_images = sample_images[:n]
    sample_features = extract_features(sample_images, Path(args.detector), args.feature_batch_size, args.device)
    ref_features = extract_features(ref_images, Path(args.detector), args.feature_batch_size, args.device)
    fid = fid_from_features(sample_features, ref_features, mode=args.fid_mode)

    payload = {
        "repo": "VAR",
        "task": "var_imagenet256",
        "dataset": "ImageNet-1K 256x256 FID reference",
        "metric": f"subset_{args.fid_mode}_fid",
        "subset_fid": fid,
        "subset_diag_fid": fid if args.fid_mode == "diag" else None,
        "fid_mode": args.fid_mode,
        "direction": "lower_is_better",
        "num_images": int(n),
        "max_items": int(args.max_items),
        "generated": bool(args.generate),
        "cfg": float(args.cfg),
        "top_k": int(args.top_k),
        "top_p": float(args.top_p),
        "more_smooth": bool(args.more_smooth),
        "seed": int(args.seed),
        "seconds": round(time.time() - started, 3),
        "sample_npz": str(args.sample_npz),
        "ref_npz": str(args.ref_npz),
        "detector": str(args.detector),
    }
    dump_json(out_dir / "results.json", payload)
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
