#!/usr/bin/env python
"""OpenVLA-OFT Token Importance CV (Coefficient of Variation) computation.

Computes per-token L2 norm CV from vision token hidden states after forward pass.
Matches methodology used for SmolVLA CV analysis.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_XET"] = "1"
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["REQUESTS_CA_BUNDLE"] = "/etc/ssl/certs/ca-certificates.crt"
os.environ["SSL_CERT_FILE"] = "/etc/ssl/certs/ca-certificates.crt"

import json
import io
import sys
import traceback
from pathlib import Path
from collections import defaultdict

import torch
import numpy as np
import pyarrow.parquet as pq
from PIL import Image

MODEL_ID = "moojink/openvla-7b-oft-finetuned-libero-object"
SNAP = Path("/root/autodl-tmp/.hf_cache/lerobot/hub/"
            "datasets--HuggingFaceVLA--libero/snapshots/"
            "86958911c0f959db2bbbdb107eb3e17c5f9c798e")
DATA_DIR = SNAP / "data" / "chunk-000"
OUT_DIR = Path("/root/autodl-tmp/importance_margin_vla_compress/eval_results")

TASKS = range(20, 30)
FRAMES_PER_TASK = 26


def gini_coefficient(values):
    v = np.sort(np.abs(values))
    n = len(v)
    if n == 0 or v.sum() == 0:
        return 0.0
    index = np.arange(1, n + 1)
    return (2 * np.sum(index * v) / (n * np.sum(v))) - (n + 1) / n


def load_frames():
    tasks_df = pq.read_table(SNAP / "meta" / "tasks.parquet").to_pandas()
    task_names = tasks_df.index.tolist()

    per_task = defaultdict(list)
    for pf in sorted(os.listdir(DATA_DIR)):
        if not pf.endswith(".parquet"):
            continue
        tbl = pq.read_table(DATA_DIR / pf, columns=["task_index"])
        for idx, tid in enumerate(tbl.column("task_index").to_pylist()):
            if tid in TASKS:
                per_task[tid].append((pf, idx))

    frames = []
    for tid in sorted(per_task.keys()):
        rows = per_task[tid]
        step = max(1, len(rows) // FRAMES_PER_TASK)
        for pf, idx in rows[::step][:FRAMES_PER_TASK]:
            tbl = pq.read_table(DATA_DIR / pf)
            frames.append({
                "img1": Image.open(io.BytesIO(
                    tbl.column("observation.images.image")[idx]["bytes"].as_py()
                )).convert("RGB"),
                "img2": Image.open(io.BytesIO(
                    tbl.column("observation.images.image2")[idx]["bytes"].as_py()
                )).convert("RGB"),
                "task_idx": tid,
                "task_name": task_names[tid] if tid < len(task_names) else f"task_{tid}",
            })

    ntasks = len(set(f["task_idx"] for f in frames))
    print(f"Loaded {len(frames)} frames from {ntasks} tasks")
    return frames


@torch.no_grad()
def main():
    gpu_id = int(os.environ.get("CUDA_VISIBLE_DEVICES", "0").split(",")[0])
    device = torch.device("cuda:0")
    print("=" * 60)
    print("OpenVLA-OFT Token Importance CV Analysis")
    print("=" * 60)

    from transformers import AutoModelForVision2Seq, AutoProcessor

    print(f"\nLoading {MODEL_ID}...")
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_ID,
        trust_remote_code=True,
        torch_dtype=torch.float16,
        attn_implementation="eager",
    )
    model.eval().to(device)

    processor = AutoProcessor.from_pretrained(MODEL_ID, trust_remote_code=True)

    llm = model.language_model
    n_layers = llm.config.num_hidden_layers
    hidden_dim = llm.config.hidden_size
    embed_fn = llm.get_input_embeddings()

    print(f"  LLM: {n_layers} layers, dim={hidden_dim}")

    # Load data
    print("\nLoading LIBERO-Object frames...")
    frames = load_frames()

    # Probe input format
    print("\nProbing input format...")
    f0 = frames[0]
    prompt = f"In: What action should the robot take to {f0['task_name']}?\nOut:"

    inputs = None
    for attempt, call_fn in enumerate([
        lambda: processor(prompt, [f0["img1"], f0["img2"]], return_tensors="pt"),
        lambda: processor(text=prompt, images=[f0["img1"], f0["img2"]], return_tensors="pt"),
        lambda: processor(text=prompt, images=[[f0["img1"], f0["img2"]]], return_tensors="pt"),
    ]):
        try:
            inputs = call_fn()
            print(f"  Processor call mode {attempt} works")
            proc_mode = attempt
            break
        except Exception:
            continue

    if inputs is None:
        raise RuntimeError("Could not find working processor call format")

    def make_inputs(frame):
        p = f"In: What action should the robot take to {frame['task_name']}?\nOut:"
        if proc_mode == 0:
            inp = processor(p, [frame["img1"], frame["img2"]], return_tensors="pt")
        elif proc_mode == 1:
            inp = processor(text=p, images=[frame["img1"], frame["img2"]], return_tensors="pt")
        else:
            inp = processor(text=p, images=[[frame["img1"], frame["img2"]]], return_tensors="pt")
        return {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inp.items()}

    # Determine vision token count
    inputs_dev = make_inputs(f0)
    ids = inputs_dev["input_ids"][0]
    text_embeds = embed_fn(ids)
    outputs = model(**inputs_dev, output_hidden_states=True)
    hs0 = outputs.hidden_states[0][0]
    N_VIS = hs0.shape[0] - ids.shape[0]
    if N_VIS <= 0:
        cos = torch.nn.functional.cosine_similarity(hs0[:ids.shape[0]], text_embeds, dim=-1)
        mismatch = (cos < 0.99).nonzero(as_tuple=True)[0]
        if len(mismatch) > 0:
            vis_start = mismatch[0].item()
            vis_end = mismatch[-1].item() + 1
            N_VIS = vis_end - vis_start
        else:
            raise RuntimeError("Cannot identify vision tokens")
    else:
        vis_start = 0
        vis_end = N_VIS

    print(f"  Vision tokens: {N_VIS} (pos {vis_start}..{vis_end})")

    last_hs = outputs.hidden_states[-1][0]
    vis_hs = last_hs[vis_start:vis_end]
    norms_check = vis_hs.float().norm(dim=-1).cpu().numpy()
    print(f"  Sample norms: mean={norms_check.mean():.2f}, std={norms_check.std():.2f}")

    del outputs
    torch.cuda.empty_cache()

    # Main loop: compute per-frame L2 norm CV
    print(f"\nProcessing {len(frames)} frames...")
    all_norms = []
    per_frame_cv = []
    per_frame_gini = []

    for fi, frame in enumerate(frames):
        if fi % 20 == 0:
            print(f"  [{fi}/{len(frames)}]", flush=True)

        inputs_dev = make_inputs(frame)
        outputs = model(**inputs_dev, output_hidden_states=True)

        last_hs = outputs.hidden_states[-1][0]
        vis_hs = last_hs[vis_start:vis_end]
        norms = vis_hs.float().norm(dim=-1).cpu().numpy()

        all_norms.append(norms)
        cv = norms.std() / (norms.mean() + 1e-10)
        per_frame_cv.append(cv)
        per_frame_gini.append(gini_coefficient(norms))

        del outputs
        torch.cuda.empty_cache()

    # Aggregate stats
    pooled = np.concatenate(all_norms)
    pooled_cv = pooled.std() / pooled.mean()
    pooled_gini = gini_coefficient(pooled)

    stacked = np.stack(all_norms)
    pos_mean = stacked.mean(axis=0)
    pos_cv = pos_mean.std() / pos_mean.mean()

    results = {
        "model": "OpenVLA-OFT-7B",
        "model_id": MODEL_ID,
        "connector": "2-layer MLP (trained)",
        "dataset": "LIBERO-Object (task_index 20-29)",
        "n_frames": len(frames),
        "n_tasks": len(set(f["task_idx"] for f in frames)),
        "vision_tokens": int(N_VIS),
        "hidden_dim": int(hidden_dim),
        "n_llm_layers": int(n_layers),

        "per_frame_cv_mean": round(float(np.mean(per_frame_cv)), 6),
        "per_frame_cv_std": round(float(np.std(per_frame_cv)), 6),
        "per_frame_cv_median": round(float(np.median(per_frame_cv)), 6),

        "per_frame_gini_mean": round(float(np.mean(per_frame_gini)), 6),
        "per_frame_gini_std": round(float(np.std(per_frame_gini)), 6),

        "pooled_cv": round(float(pooled_cv), 6),
        "pooled_gini": round(float(pooled_gini), 6),

        "position_cv": round(float(pos_cv), 6),

        "norm_stats": {
            "mean": round(float(pooled.mean()), 4),
            "std": round(float(pooled.std()), 4),
            "min": round(float(pooled.min()), 4),
            "max": round(float(pooled.max()), 4),
            "p25": round(float(np.percentile(pooled, 25)), 4),
            "p75": round(float(np.percentile(pooled, 75)), 4),
        },

        "comparison": {
            "pi0_cv": 0.038,
            "pi0_gini": 0.009,
            "openvla_oft_cv": round(float(np.mean(per_frame_cv)), 6),
            "openvla_oft_gini": round(float(np.mean(per_frame_gini)), 6),
            "smolvla_cv": 0.102,
        },
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = OUT_DIR / "openvla_oft_importance_cv.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"OpenVLA-OFT Token Importance CV Analysis")
    print(f"{'='*60}")
    print(f"Vision tokens: {results['vision_tokens']}")
    print(f"Hidden dim: {results['hidden_dim']}")
    print(f"\nPer-frame CV:   {results['per_frame_cv_mean']:.4f} ± {results['per_frame_cv_std']:.4f}")
    print(f"Per-frame Gini: {results['per_frame_gini_mean']:.4f} ± {results['per_frame_gini_std']:.4f}")
    print(f"Position CV:    {results['position_cv']:.4f}")
    print(f"Pooled CV:      {results['pooled_cv']:.4f}")
    print(f"\nNorm stats: mean={results['norm_stats']['mean']:.2f}, "
          f"std={results['norm_stats']['std']:.2f}, "
          f"range=[{results['norm_stats']['min']:.2f}, {results['norm_stats']['max']:.2f}]")
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
