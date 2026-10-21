#!/usr/bin/env python3
"""Seed robustness check for OpenVLA-Goal action probe.
Extracts features once, then probes with multiple split seeds.
Runs on cuda:1.
"""
import json, os, time
import h5py
import numpy as np
import torch
from PIL import Image
from sklearn.linear_model import RidgeCV
from transformers import AutoModelForVision2Seq, AutoProcessor

TRAINED_CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal"
DEVICE = "cuda:1"
N_LAYERS = 32
HIDDEN = 4096
N_IMG_TOKENS = 256
N_DEMOS = 10
N_TIMESTEPS = 50
SEEDS = [0, 1, 2, 42]
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results/seed_robustness"

DATA = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal"
TASKS = [
    "open_the_middle_drawer_of_the_cabinet",
    "open_the_top_drawer_and_put_the_bowl_inside",
    "push_the_plate_to_the_front_of_the_stove",
    "put_the_bowl_on_the_plate",
    "put_the_bowl_on_the_stove",
    "put_the_bowl_on_top_of_the_cabinet",
    "put_the_cream_cheese_in_the_bowl",
    "put_the_wine_bottle_on_the_rack",
    "put_the_wine_bottle_on_top_of_the_cabinet",
    "turn_on_the_stove",
]
INSTRUCTIONS = [
    "open the middle drawer of the cabinet",
    "open the top drawer and put the bowl inside",
    "push the plate to the front of the stove",
    "put the bowl on the plate",
    "put the bowl on the stove",
    "put the bowl on top of the cabinet",
    "put the cream cheese in the bowl",
    "put the wine bottle on the rack",
    "put the wine bottle on top of the cabinet",
    "turn on the stove",
]


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def make_prompt(instruction):
    return f"In: What action should the robot take to {instruction}?\nOut:"


def prepare_inputs(processor, instruction, image):
    prompt = make_prompt(instruction)
    inputs = processor(prompt, image).to(DEVICE)
    if "pixel_values" in inputs:
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
    return inputs


def extract_features(model, processor):
    log("Extracting features for OpenVLA-Goal")
    n_tasks = len(TASKS)
    total = n_tasks * N_DEMOS * N_TIMESTEPS

    reps = {
        l: {
            "image_mean": np.zeros((total, HIDDEN), dtype=np.float32),
            "last_preaction": np.zeros((total, HIDDEN), dtype=np.float32),
        }
        for l in range(N_LAYERS)
    }
    actions_arr = np.zeros((total, 7), dtype=np.float32)
    idx = 0

    for ti in range(n_tasks):
        hdf5_path = os.path.join(DATA, f"{TASKS[ti]}_demo.hdf5")
        log(f"  Task {ti}/{n_tasks}: {TASKS[ti]}")
        with h5py.File(hdf5_path, "r") as hf:
            for di in range(N_DEMOS):
                demo = f"data/demo_{di}"
                n_avail = hf[demo]["actions"].shape[0]
                for t in range(min(N_TIMESTEPS, n_avail)):
                    img = Image.fromarray(hf[f"{demo}/obs/agentview_rgb"][t])
                    act = np.array(hf[f"{demo}/actions"][t], dtype=np.float32)
                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)
                    with torch.no_grad():
                        out = model(**inputs, output_hidden_states=True, output_attentions=False)
                    seq_len = out.hidden_states[0].shape[1]
                    img_s, img_e = 1, 1 + N_IMG_TOKENS
                    for l in range(N_LAYERS):
                        hs = out.hidden_states[l + 1][0]
                        reps[l]["image_mean"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()
                        reps[l]["last_preaction"][idx] = hs[-1].float().cpu().numpy()
                    actions_arr[idx] = act
                    idx += 1
                    del out, inputs
                    if idx % 100 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total}")

    log(f"Extraction done: {idx} samples")
    return reps, actions_arr[:idx]


def run_multiseed_probing(reps, actions, seeds):
    log(f"Probing with seeds {seeds}")
    n = len(actions)
    nt = int(n * 0.8)
    all_r2 = {seed: {} for seed in seeds}

    for seed in seeds:
        perm = np.random.RandomState(seed).permutation(n)
        for l in range(N_LAYERS):
            for pos in ("image_mean", "last_preaction"):
                X, y = reps[l][pos], actions
                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]
                Xv, yv = X[perm[nt:]], y[perm[nt:]]
                probe = RidgeCV(alphas=[0.01, 0.1, 1.0, 10.0, 100.0])
                probe.fit(Xtr, ytr)
                pred = probe.predict(Xv)
                ss_res = np.sum((yv - pred) ** 2)
                ss_tot = np.sum((yv - yv.mean(0)) ** 2)
                r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0
                all_r2[seed][f"L{l}_{pos}"] = round(r2, 4)
        log(f"  seed={seed} done")
    return all_r2


def compute_delta_r2(all_r2, pos="last_preaction"):
    summary = {}
    seeds = list(all_r2.keys())
    for seed in seeds:
        r2_vals = [all_r2[seed][f"L{l}_{pos}"] for l in range(N_LAYERS)]
        peak_layer = int(np.argmax(r2_vals))
        peak_r2 = r2_vals[peak_layer]
        exit_r2 = r2_vals[N_LAYERS - 1]
        delta = peak_r2 - exit_r2
        summary[seed] = {
            "peak_layer": peak_layer,
            "peak_r2": round(peak_r2, 4),
            "exit_r2": round(exit_r2, 4),
            "delta_r2": round(delta, 4),
        }
    deltas = [summary[s]["delta_r2"] for s in seeds]
    summary["aggregate"] = {
        "mean_delta_r2": round(float(np.mean(deltas)), 4),
        "std_delta_r2": round(float(np.std(deltas)), 4),
        "all_deltas": deltas,
    }
    return summary


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    log("Loading OpenVLA model...")
    model = AutoModelForVision2Seq.from_pretrained(
        TRAINED_CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(DEVICE)
    model.eval()
    processor = AutoProcessor.from_pretrained(TRAINED_CKPT, trust_remote_code=True)
    log("Model loaded")

    t0 = time.time()
    reps, actions = extract_features(model, processor)
    log(f"Extraction: {(time.time()-t0)/60:.1f} min")

    t1 = time.time()
    all_r2 = run_multiseed_probing(reps, actions, SEEDS)
    log(f"Probing: {time.time()-t1:.1f}s")

    delta_summary = compute_delta_r2(all_r2, pos="last_preaction")
    delta_summary_img = compute_delta_r2(all_r2, pos="image_mean")

    result = {
        "cell": "openvla_goal",
        "seeds": SEEDS,
        "per_seed_r2": {str(s): all_r2[s] for s in SEEDS},
        "delta_r2_last_preaction": delta_summary,
        "delta_r2_image_mean": delta_summary_img,
    }
    out_path = os.path.join(RESULTS_DIR, "openvla_goal_seed_robustness.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    log(f"Saved {out_path}")

    agg = delta_summary["aggregate"]
    log(f"  last_preaction ΔR²: {agg['mean_delta_r2']:.4f} ± {agg['std_delta_r2']:.4f}")
    agg_img = delta_summary_img["aggregate"]
    log(f"  image_mean ΔR²: {agg_img['mean_delta_r2']:.4f} ± {agg_img['std_delta_r2']:.4f}")

    log("OpenVLA-Goal done")


if __name__ == "__main__":
    main()
