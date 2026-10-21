"""Phi3V untrained (base Phi-3-instruct LLM) cross-instruction feature extraction + 10-way classification probe."""

import gc
import json
import os
import sys
import time

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
from collections import Counter
from pathlib import Path
from PIL import Image
from tqdm import tqdm

TRACVLA_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/"
BASE_PHI3_PATHS = [
    "/root/autodl-tmp/.hf_cache/modelscope/LLM-Research/Phi-3-mini-4k-instruct",
    "/root/autodl-tmp/.hf_cache/models--microsoft--Phi-3-mini-4k-instruct",
]
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
OUTPUT_DIR = "/root/autodl-tmp/vla-ssd/results/cross_instruction/"
H5_PATH = os.path.join(OUTPUT_DIR, "phi3v_untrained_cross_inst.h5")
JSON_PATH = os.path.join(OUTPUT_DIR, "phi3v_untrained_probe_results.json")

NUM_LAYERS = 32
LAYER_INDICES = list(range(32))
MAX_DEMOS = 50
FRAMES_PER_DEMO = 1
SEED = 42
TRAIN_TASKS = list(range(8))
TEST_TASKS = list(range(8, 10))
TOKEN_POSITIONS = ["image_mean", "last_preaction"]


def task_desc_from_filename(fname):
    return Path(fname).stem.replace("_demo", "").replace("_", " ")


def find_base_phi3():
    for p in BASE_PHI3_PATHS:
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "config.json")):
            return p
    for p in BASE_PHI3_PATHS:
        parent = Path(p)
        if parent.exists():
            for child in parent.rglob("config.json"):
                return str(child.parent)
    raise FileNotFoundError(f"Base Phi-3-mini not found in {BASE_PHI3_PATHS}")


def detect_image_boundaries(input_ids_list):
    neg_pos = [i for i, tid in enumerate(input_ids_list) if tid < 0]
    if len(neg_pos) >= 50:
        return neg_pos[0], neg_pos[-1] + 1
    counts = Counter(input_ids_list)
    for tid, count in counts.most_common():
        if 50 <= count <= 800:
            positions = [i for i, t in enumerate(input_ids_list) if t == tid]
            if positions[-1] - positions[0] + 1 == count:
                return positions[0], positions[-1] + 1
    raise ValueError(f"Cannot detect image tokens. Top counts: {counts.most_common(10)}")


def load_untrained_model(device):
    from transformers import AutoModelForCausalLM, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        TRACVLA_PATH, trust_remote_code=True, local_files_only=True
    )

    print("Loading TracVLA-Phi3V architecture (CPU)...", flush=True)
    model = AutoModelForCausalLM.from_pretrained(
        TRACVLA_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )

    base_path = find_base_phi3()
    print(f"Loading base Phi-3-mini from {base_path}...", flush=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        base_path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True,
    )

    print("Replacing LLM decoder layer weights (32 layers)...", flush=True)
    for i in range(NUM_LAYERS):
        model.model.layers[i].load_state_dict(base_model.model.layers[i].state_dict())

    try:
        model.model.embed_tokens.load_state_dict(base_model.model.embed_tokens.state_dict())
        model.lm_head.load_state_dict(base_model.lm_head.state_dict())
        print("Replaced embed_tokens + lm_head", flush=True)
    except RuntimeError as e:
        print(f"Skipping embed_tokens/lm_head (dim mismatch): {e}", flush=True)

    del base_model
    gc.collect()
    torch.cuda.empty_cache()

    model = model.to(device)
    model.eval()
    n_params = sum(p.numel() for p in model.parameters()) / 1e9
    print(f"Untrained model loaded: {n_params:.1f}B params on {device}", flush=True)
    return model, processor


def sample_frame_indices(demo_length, frames_per_demo):
    if frames_per_demo == 1:
        return [demo_length // 2]
    return np.linspace(0, demo_length - 1, frames_per_demo, dtype=int).tolist()


@torch.no_grad()
def extract_features_single(model, processor, image, instruction, device, layer_indices):
    prompt = f"<|user|>\n<|image_1|>\nWhat action should the robot take to {instruction}?<|end|>\n<|assistant|>\n"
    inputs = processor(text=prompt, images=[image], return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    if "pixel_values" in inputs and inputs["pixel_values"].dtype == torch.float32:
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)

    input_ids = inputs["input_ids"][0].cpu().tolist()
    img_start, img_end = detect_image_boundaries(input_ids)
    n_img_tokens_input = img_end - img_start

    out = model(**inputs, output_hidden_states=True)
    hs = out.hidden_states

    actual_seq_len = hs[0].shape[1]
    if actual_seq_len != len(input_ids):
        expansion = actual_seq_len - len(input_ids)
        img_end_actual = img_start + n_img_tokens_input + expansion
    else:
        img_end_actual = img_end

    image_mean = torch.stack([
        hs[li][:, img_start:img_end_actual, :].mean(dim=1).squeeze(0)
        for li in layer_indices
    ])
    last_preaction = torch.stack([
        hs[li][:, -1, :].squeeze(0)
        for li in layer_indices
    ])

    image_mean = image_mean.cpu().half().numpy()
    last_preaction = last_preaction.cpu().half().numpy()

    del out, hs, inputs
    return image_mean, last_preaction


def extract_all(dry_run=False):
    device = "cuda:0"
    print("=== Stage 1: Feature Extraction (UNTRAINED) ===", flush=True)

    model, processor = load_untrained_model(device)

    hdf5_files = sorted(
        Path(DATA_DIR).glob("*.hdf5"),
        key=lambda p: p.stem,
    )
    all_instructions = [task_desc_from_filename(f.name) for f in hdf5_files]
    print(f"Found {len(hdf5_files)} tasks, {len(all_instructions)} instructions", flush=True)
    for i, inst in enumerate(all_instructions):
        print(f"  [{i}] {inst}", flush=True)

    if dry_run:
        hdf5_files = hdf5_files[:1]
        all_instructions_to_use = all_instructions[:2]
        max_demos = 1
        layer_indices = [0, 1, 31]
        print(f"DRY-RUN: 1 task, 2 instructions, 1 demo, layers {layer_indices}", flush=True)
    else:
        all_instructions_to_use = all_instructions
        max_demos = MAX_DEMOS
        layer_indices = LAYER_INDICES

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_f = h5py.File(H5_PATH, "w")

    meta = out_f.create_group("metadata")
    meta.create_dataset("instructions", data=[s.encode() for s in all_instructions])
    meta.create_dataset("layers", data=layer_indices)
    meta.create_dataset("task_files", data=[f.name.encode() for f in hdf5_files])

    total_forwards = 0
    t_start = time.time()

    for task_idx, hdf5_path in enumerate(hdf5_files):
        task_name = task_desc_from_filename(hdf5_path.name)
        print(f"\n[Task {task_idx}] {task_name}", flush=True)

        f = h5py.File(str(hdf5_path), "r")
        data = f["data"]
        demo_keys = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))
        demo_keys = demo_keys[:max_demos]

        task_grp = out_f.create_group(f"task_{task_idx}")
        frame_counter = 0

        for demo_idx, dk in enumerate(tqdm(demo_keys, desc=f"task_{task_idx}")):
            images_ds = data[dk]["obs"]["agentview_rgb"]
            T = images_ds.shape[0]
            frame_indices = sample_frame_indices(T, FRAMES_PER_DEMO)

            for t in frame_indices:
                img = Image.fromarray(images_ds[t])
                frame_grp = task_grp.create_group(f"frame_{frame_counter}")
                frame_grp.attrs["demo_key"] = dk
                frame_grp.attrs["timestep"] = t
                frame_grp.attrs["demo_length"] = T

                for inst_idx, instruction in enumerate(all_instructions_to_use):
                    im_mean, lp = extract_features_single(
                        model, processor, img, instruction, device, layer_indices
                    )
                    inst_grp = frame_grp.create_group(f"instruction_{inst_idx}")
                    inst_grp.create_dataset("image_mean", data=im_mean, dtype="float16")
                    inst_grp.create_dataset("last_preaction", data=lp, dtype="float16")
                    total_forwards += 1

                frame_counter += 1

        f.close()
        out_f.flush()
        elapsed = time.time() - t_start
        rate = total_forwards / elapsed if elapsed > 0 else 0
        print(f"  {frame_counter} frames, {total_forwards} total forwards, {rate:.1f} fwd/s, {elapsed:.0f}s", flush=True)

        gc.collect()
        torch.cuda.empty_cache()

    out_f.close()
    total_time = time.time() - t_start
    sz = os.path.getsize(H5_PATH) / 1024**2
    print(f"\nExtraction done. {total_forwards} forwards in {total_time/60:.1f} min", flush=True)
    print(f"Output: {H5_PATH} ({sz:.1f} MB)", flush=True)


def classify_all():
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    print("\n=== Stage 2: Classification Probe (UNTRAINED) ===", flush=True)
    np.random.seed(SEED)

    f = h5py.File(H5_PATH, "r")
    layers = f["metadata/layers"][:]
    layer_names = [f"L{l}" for l in layers]
    n_tasks = 10
    n_instructions = 10

    frames_per_task = []
    for task_id in range(n_tasks):
        grp = f[f"task_{task_id}"]
        n = len([k for k in grp.keys() if k.startswith("frame_")])
        frames_per_task.append(n)
    print(f"Frames per task: {frames_per_task}", flush=True)
    n_frames = min(frames_per_task)

    features = {tp: {ln: {"train_X": [], "train_y": [], "test_X": [], "test_y": []}
                      for ln in layer_names}
                for tp in TOKEN_POSITIONS}

    for task_id in range(n_tasks):
        split = "train" if task_id in TRAIN_TASKS else "test"
        for frame_id in range(n_frames):
            for inst_id in range(n_instructions):
                grp = f[f"task_{task_id}/frame_{frame_id}/instruction_{inst_id}"]
                for tp in TOKEN_POSITIONS:
                    data = grp[tp][:]
                    for li, ln in enumerate(layer_names):
                        features[tp][ln][f"{split}_X"].append(data[li])
                        features[tp][ln][f"{split}_y"].append(inst_id)

    for tp in TOKEN_POSITIONS:
        for ln in layer_names:
            for key in ["train_X", "test_X"]:
                features[tp][ln][key] = np.array(features[tp][ln][key], dtype=np.float32)
            for key in ["train_y", "test_y"]:
                features[tp][ln][key] = np.array(features[tp][ln][key], dtype=np.int64)

    f.close()

    train_n = features[TOKEN_POSITIONS[0]][layer_names[0]]["train_X"].shape[0]
    test_n = features[TOKEN_POSITIONS[0]][layer_names[0]]["test_X"].shape[0]
    print(f"Train samples: {train_n}, Test samples: {test_n}", flush=True)

    results = {tp: {} for tp in TOKEN_POSITIONS}
    for tp in TOKEN_POSITIONS:
        print(f"\n--- {tp} ---", flush=True)
        for ln in layer_names:
            d = features[tp][ln]
            train_X, train_y = d["train_X"], d["train_y"]
            test_X, test_y = d["test_X"], d["test_y"]

            n_components = min(256, train_X.shape[0], train_X.shape[1])
            pca = PCA(n_components=n_components, random_state=SEED)
            train_X_pca = pca.fit_transform(train_X)
            test_X_pca = pca.transform(test_X)

            clf = LogisticRegression(max_iter=2000, C=1.0, random_state=SEED, n_jobs=-1)
            clf.fit(train_X_pca, train_y)
            pred = clf.predict(test_X_pca)
            acc = accuracy_score(test_y, pred)
            results[tp][ln] = round(float(acc), 4)
            print(f"  {ln}: {acc:.4f}", flush=True)

    output = {
        "model": "phi3v-untrained-base-instruct",
        "condition": "untrained",
        "results": results,
        "metadata": {
            "n_classes": n_instructions,
            "n_tasks": n_tasks,
            "n_frames_per_task": n_frames,
            "n_train_tasks": len(TRAIN_TASKS),
            "n_test_tasks": len(TEST_TASKS),
            "train_tasks": TRAIN_TASKS,
            "test_tasks": TEST_TASKS,
            "pca_components": min(256, train_n),
            "classifier": "LogisticRegression(C=1.0, max_iter=2000)",
            "seed": SEED,
            "layers": layer_names,
        },
    }

    with open(JSON_PATH, "w") as fp:
        json.dump(output, fp, indent=2)
    print(f"\nResults saved to {JSON_PATH}", flush=True)

    print("\n=== KEY METRICS ===", flush=True)
    for tp in TOKEN_POSITIONS:
        for ln in ["L1", "L31"]:
            if ln in results[tp]:
                print(f"  {tp} {ln}: {results[tp][ln]:.4f}")

    return output


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("*** DRY-RUN MODE ***", flush=True)

    extract_all(dry_run=dry_run)

    if not dry_run:
        classify_all()


if __name__ == "__main__":
    main()
