"""Extract fused backbone features (2176d projector input) from OpenVLA.

Saves patch-mean-pooled features before the projector MLP, enabling
branch-split RSA analysis (DINOv2 branch vs SigLIP branch).

Usage:
    python extract_fused_backbone.py \
        --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b \
        --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/ \
        --output_dir /root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/
"""

import argparse
import gc
import glob
import os
import re
import time

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
from pathlib import Path
from PIL import Image
from tqdm import tqdm


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", default="/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b")
    p.add_argument("--data_dir", default="/root/autodl-tmp/vla-ssd/data/libero/libero_goal/")
    p.add_argument("--output_dir", default="/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--max_demos", type=int, default=50)
    p.add_argument("--batch_size", type=int, default=16)
    return p.parse_args()


def task_desc_from_filename(fname):
    stem = Path(fname).stem.replace("_demo", "")
    m = re.match(r"^[A-Z_]+SCENE\d+_(.+)$", stem)
    if m:
        return m.group(1).replace("_", " ")
    return stem.replace("_", " ")


def load_model(model_path, device):
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        model_path, trust_remote_code=True, local_files_only=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )
    model.vision_backbone = model.vision_backbone.to(device).eval()
    del model.projector, model.language_model
    gc.collect()

    vb_params = sum(p.numel() for p in model.vision_backbone.parameters()) / 1e6
    print(f"Vision backbone ({vb_params:.0f}M) on {device}")
    return model, processor


def extract_one_task(model, processor, hdf5_path, task_desc, device,
                     batch_size, max_demos, out_path):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    f = h5py.File(hdf5_path, "r")
    demo_keys = sorted(
        [k for k in f["data"].keys() if k.startswith("demo_")],
        key=lambda x: int(x.split("_")[1]),
    )[:max_demos]

    total_frames = sum(f["data"][k]["obs"]["agentview_rgb"].shape[0] for k in demo_keys)
    print(f"  {len(demo_keys)} demos, {total_frames} frames")

    prompt = f"In: What action should the robot take to {task_desc}?\nOut:"

    out_f = h5py.File(out_path, "w")
    out_f.attrs["task"] = task_desc
    out_f.attrs["prompt"] = prompt
    out_f.attrs["dim_layout"] = "DINOv2(0:1024)|SigLIP(1024:2176)"
    pbar = tqdm(total=total_frames, desc="frames")

    for demo_key in demo_keys:
        images_ds = f["data"][demo_key]["obs"]["agentview_rgb"]
        T = images_ds.shape[0]
        feat_list = []

        for t0 in range(0, T, batch_size):
            t1 = min(t0 + batch_size, T)
            batch_imgs = [Image.fromarray(images_ds[t]) for t in range(t0, t1)]

            inputs = processor(
                text=[prompt] * len(batch_imgs),
                images=batch_imgs,
                padding=True,
                return_tensors="pt",
            )
            pixel_values = inputs["pixel_values"].to(device)

            with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.bfloat16):
                patch_features = model.vision_backbone(pixel_values)  # (B, 256, 2176)
                pooled = patch_features.mean(dim=1)  # (B, 2176)

            feat_list.append(pooled.cpu().half().numpy())
            del pixel_values, patch_features, pooled, inputs
            pbar.update(t1 - t0)

        feat_arr = np.concatenate(feat_list, axis=0)  # (T, 2176)
        g = out_f.create_group(demo_key)
        g.create_dataset(
            "patch_mean", data=feat_arr, dtype="float16",
            compression="gzip", compression_opts=4,
        )
        out_f.flush()
        del feat_list, feat_arr

    pbar.close()
    f.close()
    out_f.close()

    sz = os.path.getsize(out_path) / 1024**2
    print(f"  Saved {out_path} ({sz:.1f} MB)")


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")

    print("=== Fused Backbone Feature Extraction (pre-projector, 2176d) ===")
    model, processor = load_model(args.model_path, device)

    hdf5_files = sorted(glob.glob(os.path.join(args.data_dir, "*.hdf5")))
    print(f"Found {len(hdf5_files)} task files")

    t_all = time.time()
    for i, hdf5_path in enumerate(hdf5_files):
        task_desc = task_desc_from_filename(hdf5_path)
        task_id = Path(hdf5_path).stem.replace("_demo", "")
        out_path = os.path.join(args.output_dir, f"{task_id}.h5")

        if os.path.exists(out_path):
            print(f"[{i+1}/{len(hdf5_files)}] Skip {task_id} (exists)")
            continue

        print(f"\n[{i+1}/{len(hdf5_files)}] {task_desc}")
        t0 = time.time()
        extract_one_task(
            model, processor, hdf5_path, task_desc, device,
            args.batch_size, args.max_demos, out_path,
        )
        print(f"  Took {time.time()-t0:.0f}s")

        gc.collect()
        torch.cuda.empty_cache()

    print(f"\nTotal: {(time.time()-t_all)/60:.1f} min")


if __name__ == "__main__":
    main()
