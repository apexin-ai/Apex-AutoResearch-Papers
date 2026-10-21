"""shuffled_token_control.py - Control experiment: does shuffling instruction tokens
destroy goal classification in untrained VLA?

If shuffled accuracy drops to chance (~10%): token ORDER creates separable representations.
If shuffled accuracy stays ~100%: token SET (bag-of-tokens) is sufficient in high-dim space.
"""

import os
import json
import random
import glob
import gc
import time
from collections import defaultdict
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
from PIL import Image

MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/"
FEATURES_DIR = "/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
OUTPUT_PATH = "/root/autodl-tmp/vla-ssd/results/shuffled_token_control.json"
DEVICE = "cuda:0"
TARGET_LAYER = 1
NUM_SHUFFLES = 5
SEED = 42
HIDDEN_DIM = 4096


class GoalClassificationProbe(nn.Module):
    def __init__(self, in_dim, n_classes, hidden_dim=256, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, n_classes),
        )

    def forward(self, x):
        return self.net(x)


def load_t0_features():
    task_files = sorted(glob.glob(os.path.join(FEATURES_DIR, "*.h5")))
    task_names = []
    samples = []

    for h5_path in task_files:
        task_name = Path(h5_path).stem
        task_names.append(task_name)
        task_idx = len(task_names) - 1

        with h5py.File(h5_path, "r") as f:
            demo_keys = sorted(
                [k for k in f.keys() if k.startswith("demo_")],
                key=lambda x: int(x.split("_")[1]),
            )
            for dk in demo_keys:
                feat = np.asarray(
                    f[dk]["last_preaction"][0, TARGET_LAYER, :], dtype=np.float32
                )
                samples.append((task_idx, dk, feat))

    return task_names, samples


def split_80_20(samples, n_classes):
    by_task = defaultdict(list)
    for i, (task_idx, dk, feat) in enumerate(samples):
        by_task[task_idx].append(i)

    train_ids, val_ids = [], []
    for task_idx in sorted(by_task.keys()):
        ids = by_task[task_idx]
        n_train = int(len(ids) * 0.8)
        train_ids.extend(ids[:n_train])
        val_ids.extend(ids[n_train:])
    return train_ids, val_ids


def train_probe(X_tr, y_tr, X_val, y_val, in_dim, n_classes, device,
                lr=1e-3, epochs=50, patience=5, batch_size=256):
    model = GoalClassificationProbe(in_dim, n_classes).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    crit = nn.CrossEntropyLoss()
    X_tr, y_tr = X_tr.to(device), y_tr.to(device)
    X_val, y_val = X_val.to(device), y_val.to(device)

    best_acc, best_state, wait = 0.0, None, 0
    for ep in range(epochs):
        model.train()
        perm = torch.randperm(len(X_tr), device=device)
        for s in range(0, len(X_tr), batch_size):
            idx = perm[s : s + batch_size]
            loss = crit(model(X_tr[idx]), y_tr[idx])
            opt.zero_grad()
            loss.backward()
            opt.step()

        model.eval()
        with torch.no_grad():
            acc = (model(X_val).argmax(1) == y_val).float().mean().item()

        if acc > best_acc:
            best_acc = acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            wait = 0
        else:
            wait += 1
            if wait >= patience:
                break

    model.load_state_dict(best_state)
    model.eval()
    return model, best_acc


def shuffle_tokens(prompt, tokenizer, rng):
    token_ids = tokenizer.encode(prompt, add_special_tokens=False)
    shuffled = list(token_ids)
    rng.shuffle(shuffled)
    return tokenizer.decode(shuffled, skip_special_tokens=False)


def extract_l1_features(vla_model, processor, images, prompt, device):
    inputs = processor(
        text=[prompt] * len(images),
        images=images,
        padding=True,
        return_tensors="pt",
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.bfloat16):
        out = vla_model(**inputs, output_hidden_states=True)

    hs = out.hidden_states[TARGET_LAYER]
    feats = hs[:, -1, :].float().cpu()
    del out, inputs
    torch.cuda.empty_cache()
    return feats


def main():
    t_start = time.time()
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    random.seed(SEED)
    device = torch.device(DEVICE)

    # Phase 1: Load pre-extracted t=0 features, train probe
    print("Phase 1: Load pre-extracted t=0 features & train probe")
    task_names, samples = load_t0_features()
    n_classes = len(task_names)
    print(f"  {n_classes} tasks, {len(samples)} total samples")

    train_ids, val_ids = split_80_20(samples, n_classes)
    print(f"  Split: {len(train_ids)} train / {len(val_ids)} val")

    X_tr = torch.stack([torch.from_numpy(samples[i][2]) for i in train_ids])
    y_tr = torch.tensor([samples[i][0] for i in train_ids], dtype=torch.long)
    X_val = torch.stack([torch.from_numpy(samples[i][2]) for i in val_ids])
    y_val = torch.tensor([samples[i][0] for i in val_ids], dtype=torch.long)

    probe, probe_val_acc = train_probe(
        X_tr, y_tr, X_val, y_val, HIDDEN_DIM, n_classes, device
    )
    print(f"  Probe val accuracy (original features): {probe_val_acc:.4f}")

    # Phase 2: Load untrained VLA model
    print("\nPhase 2: Load untrained VLA model")
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        MODEL_PATH, trust_remote_code=True, local_files_only=True
    )
    vla = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )
    vla = vla.to(device).eval()
    print(f"  Model loaded ({time.time() - t_start:.0f}s elapsed)")

    # Phase 3: Load t=0 images for val demos
    print("\nPhase 3: Load val images from LIBERO HDF5")
    val_images = {}
    for idx in val_ids:
        task_idx, demo_key, _ = samples[idx]
        task_name = task_names[task_idx]
        demo_num = int(demo_key.split("_")[1])
        hdf5_path = os.path.join(DATA_DIR, f"{task_name}_demo.hdf5")
        with h5py.File(hdf5_path, "r") as f:
            img_arr = f[f"data/demo_{demo_num}"]["obs"]["agentview_rgb"][0]
            val_images[(task_name, demo_key)] = Image.fromarray(img_arr)
    print(f"  Loaded {len(val_images)} images")

    # Phase 4: Run original & shuffled evaluations
    print("\nPhase 4: Extract features & evaluate")
    all_run_results = []

    for run_idx in range(NUM_SHUFFLES + 1):
        is_original = run_idx == 0
        rng = random.Random(SEED + run_idx)

        all_feats = []
        all_labels = []

        for task_idx, task_name in enumerate(task_names):
            task_desc = task_name.replace("_", " ")
            original_prompt = (
                f"In: What action should the robot take to {task_desc}?\nOut:"
            )

            if is_original:
                prompt = original_prompt
            else:
                prompt = shuffle_tokens(original_prompt, processor.tokenizer, rng)

            task_val_demos = [
                (i, samples[i][1]) for i in val_ids if samples[i][0] == task_idx
            ]
            if not task_val_demos:
                continue

            images = [val_images[(task_name, dk)] for _, dk in task_val_demos]
            feats = extract_l1_features(vla, processor, images, prompt, device)

            for f_vec in feats:
                all_feats.append(f_vec)
                all_labels.append(task_idx)

        X_eval = torch.stack(all_feats).to(device)
        y_eval = torch.tensor(all_labels, dtype=torch.long)

        probe.eval()
        with torch.no_grad():
            preds = probe(X_eval).argmax(1).cpu().numpy()
        y_np = y_eval.numpy()

        acc = float((preds == y_np).mean())
        per_task = {}
        for c in range(n_classes):
            mask = y_np == c
            if mask.sum() > 0:
                per_task[task_names[c]] = float((preds[mask] == c).mean())

        label = "original" if is_original else f"shuffle_{run_idx}"
        if not is_original:
            print(
                f"  {label}: acc={acc:.4f}  prompt_sample='{prompt[:60]}...'"
            )
        else:
            print(f"  {label}: acc={acc:.4f}")
        all_run_results.append(
            {"condition": label, "accuracy": acc, "per_task_accuracy": per_task}
        )

    # Summary
    shuffle_accs = [r["accuracy"] for r in all_run_results[1:]]

    results = {
        "experiment": "shuffled_token_control",
        "model": "openvla-7b-untrained",
        "layer": TARGET_LAYER,
        "num_shuffles": NUM_SHUFFLES,
        "num_val_samples": len(val_ids),
        "num_classes": n_classes,
        "probe_val_accuracy_original_hdf5": probe_val_acc,
        "original_accuracy_reextracted": all_run_results[0]["accuracy"],
        "shuffled_accuracy_mean": float(np.mean(shuffle_accs)),
        "shuffled_accuracy_std": float(np.std(shuffle_accs)),
        "shuffled_accuracy_individual": shuffle_accs,
        "per_run_results": all_run_results,
        "task_names": task_names,
        "elapsed_seconds": time.time() - t_start,
    }

    if results["shuffled_accuracy_mean"] < 0.2:
        results["conclusion"] = (
            "Token ORDER matters: shuffling destroys separability"
        )
    elif results["shuffled_accuracy_mean"] > 0.8:
        results["conclusion"] = (
            "Token SET sufficient: bag-of-tokens already separable in high-dim space"
        )
    else:
        results["conclusion"] = (
            f"Partial effect: accuracy {results['shuffled_accuracy_mean']:.1%}"
        )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*50}")
    print(f"Original (pre-extracted, probe val): {probe_val_acc:.4f}")
    print(f"Original (re-extracted via model):   {all_run_results[0]['accuracy']:.4f}")
    print(
        f"Shuffled ({NUM_SHUFFLES}x mean±std): "
        f"{results['shuffled_accuracy_mean']:.4f} ± {results['shuffled_accuracy_std']:.4f}"
    )
    print(f"Conclusion: {results['conclusion']}")
    print(f"Saved to {OUTPUT_PATH}")
    print(f"Total time: {results['elapsed_seconds']:.0f}s")


if __name__ == "__main__":
    main()
