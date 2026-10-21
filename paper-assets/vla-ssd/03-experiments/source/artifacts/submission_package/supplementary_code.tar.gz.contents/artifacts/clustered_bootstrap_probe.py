#!/usr/bin/env python3
"""Clustered Bootstrap R2 Probing — fixes temporal leakage via demo-level splitting."""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import argparse, json, os, sys, time, types
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import numpy as np
import h5py
import torch
from PIL import Image
from sklearn.linear_model import RidgeCV
import importlib.util


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


CKPT = {
    "openvla": {
        "goal":    {"trained": f"{PROJECT_ROOT}/checkpoints/openvla-7b-finetuned-libero-goal",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/openvla-7b"},
        "spatial": {"trained": f"{PROJECT_ROOT}/checkpoints/openvla-7b-finetuned-libero-spatial",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/openvla-7b"},
        "object":  {"trained": f"{PROJECT_ROOT}/checkpoints/openvla-7b-finetuned-libero-object",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/openvla-7b"},
    },
    "tracvla": {
        "goal":    {"trained": f"{PROJECT_ROOT}/checkpoints/tracevla-phi3v",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/phi3v-base"},
        "spatial": {"trained": f"{PROJECT_ROOT}/checkpoints/tracevla-phi3v",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/phi3v-base"},
        "object":  {"trained": f"{PROJECT_ROOT}/checkpoints/tracevla-phi3v",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/phi3v-base"},
    },
    "nora": {
        "goal":    {"trained": f"{PROJECT_ROOT}/checkpoints/nora-libero-goal",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/qwen25-vl-3b-base"},
        "spatial": {"trained": f"{PROJECT_ROOT}/checkpoints/nora-libero-spatial",
                    "untrained": f"{PROJECT_ROOT}/checkpoints/qwen25-vl-3b-base"},
    },
}

ARCH_INFO = {
    "openvla": {"n_layers": 32, "hidden": 4096},
    "tracvla": {"n_layers": 32, "hidden": 3072},
    "nora":    {"n_layers": 36, "hidden": 2048},
}

DATA_ROOT = f"{PROJECT_ROOT}/data/libero"


def _load_openvla_modules(ckpt_path):
    pkg_name = "_openvla_pkg"
    pkg = types.ModuleType(pkg_name)
    pkg.__path__ = [ckpt_path]
    pkg.__package__ = pkg_name
    sys.modules[pkg_name] = pkg

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        # Fix transformers 5.x import changes
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        mod = types.ModuleType(full)
        mod.__file__ = fpath
        mod.__package__ = pkg_name
        sys.modules[full] = mod
        sys.modules[name] = mod
        setattr(pkg, name, mod)

    for name in ["configuration_prismatic", "modeling_prismatic", "processing_prismatic"]:
        full = f"{pkg_name}.{name}"
        fpath = os.path.join(ckpt_path, f"{name}.py")
        with open(fpath) as f:
            src = f.read()
        src = src.replace(
            "from transformers.tokenization_utils import PaddingStrategy, PreTokenizedInput, TextInput, TruncationStrategy",
            "from transformers.utils import PaddingStrategy\n"
            "from transformers.tokenization_utils_base import PreTokenizedInput, TextInput, TruncationStrategy"
        )
        src = src.replace(
            "def tie_weights(self) -> None:",
            "def tie_weights(self, **kwargs) -> None:"
        )
        code = compile(src, fpath, "exec")
        exec(code, sys.modules[full].__dict__)


def load_model(arch, ckpt_path, device):
    log(f"Loading {arch} from {ckpt_path}")
    t0 = time.time()

    if arch == "openvla":
        _load_openvla_modules(ckpt_path)
        config_cls = sys.modules["configuration_prismatic"].OpenVLAConfig
        model_cls = sys.modules["modeling_prismatic"].OpenVLAForActionPrediction
        proc_cls = sys.modules["processing_prismatic"].PrismaticProcessor

        config = config_cls.from_pretrained(ckpt_path)
        model = model_cls.from_pretrained(
            ckpt_path, config=config, dtype=torch.bfloat16
        ).to(device).eval()
        # Patch transformers.tokenization_utils for HF cache loading
        import transformers.tokenization_utils_base as _tub
        from transformers.utils import PaddingStrategy as _PS
        _tu = sys.modules["transformers.tokenization_utils"]
        _tu.PaddingStrategy = _PS
        _tu.PreTokenizedInput = _tub.PreTokenizedInput
        _tu.TextInput = _tub.TextInput
        _tu.TruncationStrategy = _tub.TruncationStrategy
        processor = proc_cls.from_pretrained(ckpt_path, trust_remote_code=True)

        ds_path = os.path.join(ckpt_path, "dataset_statistics.json")
        if os.path.exists(ds_path):
            with open(ds_path) as f:
                ds_stats = json.load(f)
            for k, v in ds_stats.items():
                if k not in model.norm_stats:
                    model.norm_stats[k] = v

    elif arch == "tracvla":
        from transformers import AutoModelForCausalLM, AutoProcessor
        model = AutoModelForCausalLM.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    elif arch == "nora":
        from transformers import AutoModelForImageTextToText, AutoProcessor
        model = AutoModelForImageTextToText.from_pretrained(
            ckpt_path, dtype=torch.bfloat16, trust_remote_code=True
        ).to(device).eval()
        processor = AutoProcessor.from_pretrained(ckpt_path, trust_remote_code=True)

    log(f"  Loaded in {time.time()-t0:.1f}s")
    return model, processor


def prepare_inputs(arch, processor, instruction, image, device):
    if arch == "openvla":
        prompt = f"In: What action should the robot take to {instruction}?\nOut:"
        inputs = processor(prompt, image).to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        ids = inputs["input_ids"]
        if not torch.all(ids[:, -1] == 29871):
            ids = torch.cat(
                (ids, torch.tensor([[29871]], device=device, dtype=ids.dtype)), dim=1)
            if "attention_mask" in inputs:
                inputs["attention_mask"] = torch.cat(
                    (inputs["attention_mask"],
                     torch.ones(1, 1, device=device, dtype=inputs["attention_mask"].dtype)),
                    dim=1)
        inputs["input_ids"] = ids
        return inputs

    elif arch == "tracvla":
        prompt = ("<|user|>\n<|image_1|>\n"
                  f"What action should the robot take to {instruction}?<|end|>\n"
                  "<|assistant|>\n")
        inputs = processor(prompt, [image], return_tensors="pt").to(device)
        if "pixel_values" in inputs:
            inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
        return inputs

    elif arch == "nora":
        messages = [{"role": "user", "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": instruction},
        ]}]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(text=[text], images=[image], return_tensors="pt", padding=True)
        return {k: v.to(device) if isinstance(v, torch.Tensor) else v
                for k, v in inputs.items()}


def discover_tasks(data_dir):
    tasks = []
    for f in sorted(os.listdir(data_dir)):
        if f.endswith("_demo.hdf5"):
            tasks.append(f.replace("_demo.hdf5", ""))
    instructions = [t.replace("_", " ") for t in tasks]
    return tasks, instructions


def extract_features(arch, model, processor, tasks, instructions, data_dir,
                     device, n_demos, n_timesteps):
    info = ARCH_INFO[arch]
    n_layers = info["n_layers"]
    hidden = info["hidden"]
    total = len(tasks) * n_demos * n_timesteps

    features = {l: np.zeros((total, hidden), dtype=np.float32) for l in range(n_layers)}
    actions = np.zeros((total, 7), dtype=np.float32)
    demo_ids = np.zeros(total, dtype=np.int64)

    idx = 0
    gd = 0

    for ti, (task, instr) in enumerate(zip(tasks, instructions)):
        hdf5_path = os.path.join(data_dir, f"{task}_demo.hdf5")
        log(f"  Task {ti}/{len(tasks)}: {task}")

        with h5py.File(hdf5_path, "r") as hf:
            for di in range(n_demos):
                demo_key = f"data/demo_{di}"
                if demo_key not in hf:
                    gd += 1
                    continue
                n_avail = hf[demo_key]["actions"].shape[0]

                for t in range(min(n_timesteps, n_avail)):
                    img = Image.fromarray(hf[f"{demo_key}/obs/agentview_rgb"][t])
                    act = np.array(hf[f"{demo_key}/actions"][t], dtype=np.float32)

                    inputs = prepare_inputs(arch, processor, instr, img, device)
                    with torch.no_grad():
                        out = model(**inputs, output_hidden_states=True)

                    for l in range(n_layers):
                        hs = out.hidden_states[l + 1][0]
                        features[l][idx] = hs[-1].float().cpu().numpy()

                    actions[idx] = act
                    demo_ids[idx] = gd
                    idx += 1

                    del out, inputs
                    if idx % 50 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total} samples")

                gd += 1

    log(f"  Extraction done: {idx} samples, {gd} demos")
    features = {l: features[l][:idx] for l in range(n_layers)}
    return features, actions[:idx], demo_ids[:idx]


def clustered_bootstrap_r2(features, actions, demo_ids, n_layers, n_bootstrap, seed=42):
    unique_demos = np.unique(demo_ids)
    n_total = len(unique_demos)
    n_train = int(0.8 * n_total)
    log(f"  {n_total} demos, split {n_train}/{n_total - n_train}")

    demo_idx_map = {int(d): np.where(demo_ids == d)[0] for d in unique_demos}

    rng = np.random.RandomState(seed)
    canon_perm = rng.permutation(unique_demos)
    canon_train = set(canon_perm[:n_train].tolist())
    train_mask = np.array([d in canon_train for d in demo_ids])
    test_mask = ~train_mask

    y_tr_canon = actions[train_mask]
    y_te_canon = actions[test_mask]

    alphas_list = [0.01, 0.1, 1.0, 10.0, 100.0]
    best_alpha = {}
    canon_r2 = {}

    log("  Canonical split -- fitting RidgeCV per layer...")
    for l in range(n_layers):
        probe = RidgeCV(alphas=alphas_list)
        probe.fit(features[l][train_mask], y_tr_canon)
        best_alpha[l] = float(probe.alpha_)
        pred = probe.predict(features[l][test_mask])
        ss_res = np.sum((y_te_canon - pred) ** 2)
        ss_tot = np.sum((y_te_canon - y_te_canon.mean(0)) ** 2)
        canon_r2[l] = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0

    # Precompute kernel matrices per layer for efficient bootstrap
    log("  Precomputing kernel matrices...")
    N = len(actions)
    kernels = {}
    for l in range(n_layers):
        kernels[l] = features[l] @ features[l].T  # (N, N)

    log(f"  Bootstrap ({n_bootstrap} iterations)...")
    boot_r2 = np.zeros((n_bootstrap, n_layers), dtype=np.float64)
    rng2 = np.random.RandomState(seed + 1)
    report_every = max(1, n_bootstrap // 10)

    for b in range(n_bootstrap):
        resampled = rng2.choice(unique_demos, size=n_total, replace=True)
        tr_demos = resampled[:n_train]
        te_demos = resampled[n_train:]

        tr_idx = np.concatenate([demo_idx_map[int(d)] for d in tr_demos])
        te_idx = np.concatenate([demo_idx_map[int(d)] for d in te_demos])

        if len(te_idx) == 0:
            continue

        y_tr = actions[tr_idx]
        y_te = actions[te_idx]
        y_te_mean = y_te.mean(axis=0)
        ss_tot = np.sum((y_te - y_te_mean) ** 2)
        if ss_tot < 1e-10:
            continue

        n_tr = len(tr_idx)
        for l in range(n_layers):
            K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]
            K_tr[np.diag_indices(n_tr)] += best_alpha[l]
            K_te_tr = kernels[l][np.ix_(te_idx, tr_idx)]
            try:
                w = np.linalg.solve(K_tr, y_tr)
                pred = K_te_tr @ w
                ss_res = np.sum((y_te - pred) ** 2)
                boot_r2[b, l] = 1.0 - ss_res / ss_tot
            except np.linalg.LinAlgError:
                boot_r2[b, l] = 0.0

        if (b + 1) % report_every == 0:
            log(f"    {b+1}/{n_bootstrap}")

    exit_l = n_layers - 1
    peak_r2_boot = np.max(boot_r2, axis=1)
    exit_r2_boot = boot_r2[:, exit_l]
    deltas = peak_r2_boot - exit_r2_boot
    ci_lo, ci_hi = np.percentile(deltas, [2.5, 97.5])

    canon_peak_l = max(canon_r2, key=canon_r2.get)

    return {
        "per_layer_r2": {f"L{l}": round(canon_r2[l], 4) for l in range(n_layers)},
        "peak_r2": round(canon_r2[canon_peak_l], 4),
        "peak_layer": f"L{canon_peak_l}",
        "exit_r2": round(canon_r2[exit_l], 4),
        "exit_layer": f"L{exit_l}",
        "delta": round(canon_r2[canon_peak_l] - canon_r2[exit_l], 4),
        "delta_ci_95": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "bootstrap_deltas_summary": {
            "mean": round(float(np.mean(deltas)), 4),
            "std": round(float(np.std(deltas)), 4),
            "median": round(float(np.median(deltas)), 4),
        },
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--arch", required=True, choices=["openvla", "tracvla", "nora"])
    p.add_argument("--suite", required=True, choices=["goal", "spatial", "object"])
    p.add_argument("--condition", required=True, choices=["trained", "untrained"])
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--n_bootstrap", type=int, default=10000)
    p.add_argument("--n_demos", type=int, default=10)
    p.add_argument("--n_timesteps", type=int, default=50)
    p.add_argument("--output_dir",
                   default=f"{PROJECT_ROOT}/results/clustered_bootstrap/")
    p.add_argument("--dry_run", action="store_true")
    args = p.parse_args()

    if args.dry_run:
        args.n_demos = 2
        args.n_timesteps = 5
        args.n_bootstrap = min(args.n_bootstrap, 100)

    if args.suite not in CKPT.get(args.arch, {}):
        log(f"ERROR: no checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)
    if args.condition not in CKPT[args.arch][args.suite]:
        log(f"ERROR: no {args.condition} checkpoint for {args.arch}/{args.suite}")
        sys.exit(1)

    device = f"cuda:{args.gpu}"
    ckpt_path = CKPT[args.arch][args.suite][args.condition]
    data_dir = os.path.join(DATA_ROOT, f"libero_{args.suite}")

    log(f"=== {args.arch} / {args.suite} / {args.condition} ===")
    log(f"Checkpoint: {ckpt_path}")
    log(f"Data: {data_dir}")
    log(f"demos={args.n_demos} timesteps={args.n_timesteps} bootstrap={args.n_bootstrap}")
    if args.dry_run:
        log("DRY RUN")

    tasks, instructions = discover_tasks(data_dir)
    if args.dry_run:
        tasks = tasks[:2]
        instructions = instructions[:2]
    log(f"Tasks: {len(tasks)}")

    model, processor = load_model(args.arch, ckpt_path, device)

    t0 = time.time()
    features, actions, demo_ids = extract_features(
        args.arch, model, processor, tasks, instructions, data_dir,
        device, args.n_demos, args.n_timesteps)
    log(f"Extraction: {time.time()-t0:.1f}s")

    del model, processor
    torch.cuda.empty_cache()

    t1 = time.time()
    n_layers = ARCH_INFO[args.arch]["n_layers"]
    result = clustered_bootstrap_r2(
        features, actions, demo_ids, n_layers, args.n_bootstrap)
    log(f"Bootstrap: {time.time()-t1:.1f}s")

    result["arch"] = args.arch
    result["suite"] = args.suite
    result["condition"] = args.condition
    result["n_demos"] = int(len(np.unique(demo_ids)))
    result["n_total_samples"] = int(len(actions))
    result["n_bootstrap"] = args.n_bootstrap
    result["dry_run"] = args.dry_run

    out_dir = os.path.join(args.output_dir, f"{args.arch}_{args.suite}")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{args.condition}.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    log(f"Saved: {out_path}")

    log(f"Peak R2={result['peak_r2']} @ {result['peak_layer']}")
    log(f"Exit R2={result['exit_r2']} @ {result['exit_layer']}")
    log(f"Delta={result['delta']}  CI95={result['delta_ci_95']}")


if __name__ == "__main__":
    main()
