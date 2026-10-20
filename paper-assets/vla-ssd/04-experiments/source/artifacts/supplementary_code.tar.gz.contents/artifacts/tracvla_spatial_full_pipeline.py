#!/usr/bin/env python3
"""
LIBERO-Spatial Full Analysis Pipeline for TracVLA-Phi3V

Phases:
  1. Representation extraction: forward passes -> hidden states + L1 attention
  2. Action R2 probing: per-layer MLP probe, 15 seeds
  3. L1 attention profile: per-head instruction/image attention classification
  4. Cross-instruction classification: 10-way per-layer
  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d

Runs both trained (TracVLA-Phi3V) and untrained (base Phi-3-Vision) sequentially.
All results -> RESULTS_DIR/{trained,untrained}/*.json
No intermediate features saved to disk.
"""

import argparse, json, os, random, sys, time
from collections import defaultdict

import h5py
import numpy as np
import torch
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPRegressor
from transformers import AutoModelForCausalLM, AutoProcessor

# --- Checkpoints ---
TRAINED_CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/"
UNTRAINED_CKPT = "microsoft/Phi-3-vision-128k-instruct"
UNTRAINED_CACHE = "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/"

# --- Data ---
DATA = "/root/autodl-tmp/vla-ssd/data/libero/libero_spatial"
RESULTS_BASE = "/root/autodl-tmp/vla-ssd/results/tracvla_spatial"
DEVICE = "cuda:0"  # submit_training_job sets CUDA_VISIBLE_DEVICES

# --- Architecture ---
N_LAYERS = 32
N_HEADS = 32
HIDDEN = 3072
N_IMG_TOKENS = 0  # auto-detected
IMG_TOKEN_ID = -1  # auto-detected

# --- Data config ---
N_DEMOS = 10
N_TIMESTEPS = 50
N_PROBE_SEEDS = 15

TASKS = [
    "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate",
    "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate",
]
INSTRUCTIONS = [t.replace("_", " ") for t in TASKS]
PARAPHRASES = [
    "grab the black bowl between the plate and ramekin and put it on the plate",
    "grab the black bowl on the ramekin and put it on the plate",
    "grab the black bowl on the cookie box and put it on the plate",
    "grab the black bowl in the top drawer of the wooden cabinet and put it on the plate",
    "grab the black bowl from the center of the table and put it on the plate",
    "grab the black bowl next to the cookie box and put it on the plate",
    "grab the black bowl on the stove and put it on the plate",
    "grab the black bowl on the wooden cabinet and put it on the plate",
    "grab the black bowl next to the plate and put it on the plate",
    "grab the black bowl next to the ramekin and put it on the plate",
]


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def make_prompt(instruction):
    return (
        f"<|user|>\n<|image_1|>\n"
        f"What action should the robot take to {instruction}?<|end|>\n"
        f"<|assistant|>\n"
    )


def prepare_inputs(processor, instruction, image):
    prompt = make_prompt(instruction)
    inputs = processor(prompt, [image], return_tensors="pt").to(DEVICE)
    if "pixel_values" in inputs:
        inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)
    return inputs


def detect_image_token_id(processor):
    return -1
    for tid in range(32044, 32050):
        token = processor.tokenizer.decode([tid])
        if "image" in token.lower():
            return tid
    return 32044


def find_token_regions(input_ids, img_token_id):
    """Find image and text regions in Phi3V input_ids.
    In Phi3V, image placeholder tokens are embedded within input_ids."""
    ids = input_ids[0].cpu().numpy()
    img_mask = ids < 0
    img_positions = np.where(img_mask)[0]

    if len(img_positions) > 0:
        img_s = int(img_positions[0])
        img_e = int(img_positions[-1]) + 1
    else:
        img_s = img_e = 1

    txt_s = img_e
    txt_e = len(ids)

    return {"bos": (0, img_s), "image": (img_s, img_e), "text": (txt_s, txt_e)}


def generate_action_phi3v(model, processor, instruction, image):
    """Generate action using TracVLA-Phi3V's predict_action interface."""
    inputs = prepare_inputs(processor, instruction, image)

    with torch.no_grad():
        gen_ids = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs.get("attention_mask"),
            pixel_values=inputs.get("pixel_values"),
            image_sizes=inputs.get("image_sizes"),
            max_new_tokens=7,
            do_sample=False,
        )

    token_ids = gen_ids[0, -7:].cpu().numpy()
    vocab_size = model.config.vocab_size
    n_bins = 256
    bins = np.linspace(-1, 1, n_bins)
    bin_centers = (bins[:-1] + bins[1:]) / 2.0

    disc = np.clip(vocab_size - token_ids - 1, a_min=0, a_max=bin_centers.shape[0] - 1)
    norm_act = bin_centers[disc]

    del inputs, gen_ids
    return norm_act.astype(np.float64), token_ids


# ============================================================
# Phase 1: Feature Extraction
# ============================================================
def extract_features(model, processor, n_tasks, n_demos, n_timesteps, img_token_id):
    log("Phase 1: representation extraction")
    total = n_tasks * n_demos * n_timesteps

    reps = {
        l: {
            "image_mean": np.zeros((total, HIDDEN), dtype=np.float32),
            "last_preaction": np.zeros((total, HIDDEN), dtype=np.float32),
        }
        for l in range(N_LAYERS)
    }
    actions_arr = np.zeros((total, 7), dtype=np.float32)
    task_labels = np.zeros(total, dtype=np.int64)
    l1_attns = []
    token_regions = []

    idx = 0
    for ti in range(n_tasks):
        hdf5_path = os.path.join(DATA, f"{TASKS[ti]}_demo.hdf5")
        log(f"  Task {ti}/{n_tasks}: {TASKS[ti]}")

        with h5py.File(hdf5_path, "r") as hf:
            for di in range(n_demos):
                demo = f"data/demo_{di}"
                n_avail = hf[demo]["actions"].shape[0]
                for t in range(min(n_timesteps, n_avail)):
                    img = Image.fromarray(hf[f"{demo}/obs/agentview_rgb"][t])
                    act = np.array(hf[f"{demo}/actions"][t], dtype=np.float32)

                    inputs = prepare_inputs(processor, INSTRUCTIONS[ti], img)
                    original_ids = inputs["input_ids"].clone()
                    with torch.no_grad():
                        out = model(
                            **inputs,
                            output_hidden_states=True,
                            output_attentions=True,
                        )

                    tr = find_token_regions(original_ids, img_token_id)
                    img_s, img_e = tr["image"]
                    seq_len = out.hidden_states[0].shape[1]

                    for l in range(N_LAYERS):
                        hs = out.hidden_states[l + 1][0]
                        reps[l]["image_mean"][idx] = (
                            hs[img_s:img_e].float().mean(0).cpu().numpy()
                        )
                        reps[l]["last_preaction"][idx] = (
                            hs[-1].float().cpu().numpy()
                        )

                    l1 = out.attentions[1][0].float().cpu().numpy()
                    l1_attns.append(l1)
                    token_regions.append(tr)

                    actions_arr[idx] = act
                    task_labels[idx] = ti
                    idx += 1

                    del out, inputs
                    if idx % 100 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total}")

    log(f"Phase 1 done: {idx} samples")
    return reps, actions_arr[:idx], task_labels[:idx], l1_attns, token_regions


# ============================================================
# Phase 2: Action R2 Probing
# ============================================================
def run_probing(reps, actions, n_seeds):
    log("Phase 2: action R2 probing")
    results = {}
    for l in range(N_LAYERS):
        for pos in ("image_mean", "last_preaction"):
            X, y = reps[l][pos], actions
            r2s = []
            for s in range(n_seeds):
                n = len(X)
                nt = int(n * 0.8)
                perm = np.random.RandomState(s).permutation(n)
                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]
                Xv, yv = X[perm[nt:]], y[perm[nt:]]

                use_es = len(Xtr) >= 10
                probe = MLPRegressor(
                    hidden_layer_sizes=(256,),
                    max_iter=200,
                    early_stopping=use_es,
                    validation_fraction=0.2 if use_es else 0.1,
                    random_state=s,
                    n_iter_no_change=10,
                )
                probe.fit(Xtr, ytr)
                pred = probe.predict(Xv)
                ss_res = np.sum((yv - pred) ** 2)
                ss_tot = np.sum((yv - yv.mean(0)) ** 2)
                r2s.append(float(1 - ss_res / ss_tot) if ss_tot > 1e-10 else 0.0)

            results[f"L{l}_{pos}"] = {
                "mean": round(float(np.mean(r2s)), 4),
                "std": round(float(np.std(r2s)), 4),
                "values": [round(v, 4) for v in r2s],
            }
        if l % 8 == 0:
            log(
                f"  L{l}: img_mean R2={results[f'L{l}_image_mean']['mean']:.4f}  "
                f"last_pre R2={results[f'L{l}_last_preaction']['mean']:.4f}"
            )
    return results


# ============================================================
# Phase 3: L1 Attention Profile
# ============================================================
def analyze_attention(l1_attns, token_regions):
    log("Phase 3: L1 attention profile")
    n = len(l1_attns)
    head_ratios = {h: [] for h in range(N_HEADS)}

    for i in range(n):
        attn = l1_attns[i]
        tr = token_regions[i]
        last = attn.shape[1] - 1
        is_, ie = tr["image"]
        ts, te = tr["text"]

        for h in range(N_HEADS):
            row = attn[h, last, :]
            img_a = row[is_:ie].sum()
            txt_a = row[ts:te].sum()
            bos_s, bos_e = tr["bos"]
            bos_a = row[bos_s:bos_e].sum()
            total = img_a + txt_a + bos_a
            head_ratios[h].append(float(txt_a / total) if total > 1e-10 else 0.0)

    profiles = {}
    for h in range(N_HEADS):
        r = head_ratios[h]
        m = float(np.mean(r))
        cat = (
            "instruction_dominant"
            if m > 0.5
            else ("image_dominant" if m < 0.2 else "mixed")
        )
        profiles[f"head_{h}"] = {
            "instruction_ratio_mean": round(m, 4),
            "instruction_ratio_std": round(float(np.std(r)), 4),
            "category": cat,
        }

    cats = [v["category"] for v in profiles.values()]
    summary = {
        "instruction_dominant": cats.count("instruction_dominant"),
        "image_dominant": cats.count("image_dominant"),
        "mixed": cats.count("mixed"),
        "instruction_dominant_heads": [
            h
            for h in range(N_HEADS)
            if profiles[f"head_{h}"]["category"] == "instruction_dominant"
        ],
        "image_dominant_heads": [
            h
            for h in range(N_HEADS)
            if profiles[f"head_{h}"]["category"] == "image_dominant"
        ],
    }
    log(
        f"  {summary['instruction_dominant']} instr-dom, "
        f"{summary['image_dominant']} img-dom, {summary['mixed']} mixed"
    )
    return {"per_head": profiles, "summary": summary}


# ============================================================
# Phase 4: Cross-Instruction Classification
# ============================================================
def run_classification(reps, labels, layers=None):
    log("Phase 4: cross-instruction classification")
    if layers is None:
        layers = list(range(N_LAYERS))
    n_cls = int(labels.max()) + 1
    if n_cls < 2:
        log("  Skipping: need >= 2 classes")
        return {"chance": 1.0, "skipped": True}
    results = {"chance": round(1.0 / n_cls, 4)}

    for l in layers:
        for pos in ("image_mean", "last_preaction"):
            X, y = reps[l][pos], labels
            n = len(X)
            nt = int(n * 0.8)
            perm = np.random.RandomState(42).permutation(n)
            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]
            Xv, yv = X[perm[nt:]], y[perm[nt:]]

            clf = LogisticRegression(max_iter=2000, C=1.0, random_state=42)
            clf.fit(Xtr, ytr)
            results[f"L{l}_{pos}"] = round(float(clf.score(Xv, yv)), 4)

        log(
            f"  L{l}: img={results[f'L{l}_image_mean']:.3f}  "
            f"last_pre={results[f'L{l}_last_preaction']:.3f}"
        )
    return results


# ============================================================
# Phase 5: Counterfactual
# ============================================================
def _cf_instruction(task_idx, condition):
    if condition == "wrong":
        return INSTRUCTIONS[(task_idx + 1) % len(TASKS)]
    elif condition == "empty":
        return ""
    elif condition == "shuffled":
        words = INSTRUCTIONS[task_idx].split()
        random.Random(42 + task_idx).shuffle(words)
        return " ".join(words)
    elif condition == "paraphrased":
        return PARAPHRASES[task_idx]


def run_counterfactual(model, processor, n_tasks, n_demos, n_timesteps):
    log("Phase 5: counterfactual analysis")
    conditions = ["wrong", "empty", "shuffled", "paraphrased"]

    all_res = {
        "config": {
            "experiment": "counterfactual_tracvla_spatial",
            "conditions": conditions,
            "n_tasks": n_tasks,
            "n_demos_per_task": n_demos,
            "n_timesteps_per_demo": n_timesteps,
            "model": "tracevla-phi3v",
            "action_space": "normalized_bins",
            "seed": 42,
            "task_names": TASKS[:n_tasks],
        }
    }

    for cond in conditions:
        log(f"  Condition: {cond}")
        all_mses, all_tok_div = [], []
        per_task_mses = defaultdict(list)
        per_task_demo_mses = defaultdict(lambda: defaultdict(list))
        per_task_correct = defaultdict(list)
        per_task_cf = defaultdict(list)
        sample_n = 0

        for ti in range(n_tasks):
            cf_instr = _cf_instruction(ti, cond)
            hdf5_path = os.path.join(DATA, f"{TASKS[ti]}_demo.hdf5")

            with h5py.File(hdf5_path, "r") as hf:
                for di in range(n_demos):
                    n_avail = hf[f"data/demo_{di}/actions"].shape[0]
                    for t in range(min(n_timesteps, n_avail)):
                        img = Image.fromarray(
                            hf[f"data/demo_{di}/obs/agentview_rgb"][t]
                        )

                        c_act, c_tok = generate_action_phi3v(
                            model, processor, INSTRUCTIONS[ti], img
                        )
                        f_act, f_tok = generate_action_phi3v(
                            model, processor, cf_instr, img
                        )

                        mse = float(np.mean((c_act - f_act) ** 2))
                        tok_div = int(not np.array_equal(c_tok, f_tok))

                        all_mses.append(mse)
                        all_tok_div.append(tok_div)
                        per_task_mses[ti].append(mse)
                        per_task_demo_mses[ti][di].append(mse)
                        per_task_correct[ti].append(c_act)
                        per_task_cf[ti].append(f_act)

                        sample_n += 1
                        if sample_n % 200 == 0:
                            torch.cuda.empty_cache()
                            log(
                                f"    {sample_n}/{n_tasks * n_demos * n_timesteps}"
                            )

        mse_arr = np.array(all_mses)
        global_d = (
            float(mse_arr.mean() / mse_arr.std(ddof=1))
            if mse_arr.std(ddof=1) > 0
            else 0.0
        )

        ca_all = np.concatenate(
            [np.array(per_task_correct[ti]) for ti in range(n_tasks)]
        )
        cf_all = np.concatenate(
            [np.array(per_task_cf[ti]) for ti in range(n_tasks)]
        )
        pdm = np.abs(ca_all - cf_all).mean(0).tolist()
        pds = np.abs(ca_all - cf_all).std(0).tolist()

        cond_res = {
            "global_metrics": {
                "paired_mse": {
                    "mean": round(float(mse_arr.mean()), 6),
                    "std": round(float(mse_arr.std()), 6),
                    "cohens_d": round(global_d, 4),
                },
                "per_dim_shift": {
                    "means": [round(v, 6) for v in pdm],
                    "stds": [round(v, 6) for v in pds],
                    "dim_names": ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"],
                },
                "token_divergence_rate": round(float(np.mean(all_tok_div)), 4),
                "n_samples": len(mse_arr),
            },
            "per_task": {},
            "cross_task_variance": {},
        }

        per_task_ds = []
        for ti in range(n_tasks):
            tm = np.array(per_task_mses[ti])
            td = (
                float(tm.mean() / tm.std(ddof=1)) if tm.std(ddof=1) > 0 else 0.0
            )
            per_task_ds.append(td)

            demo_means = [
                float(np.mean(per_task_demo_mses[ti][di])) for di in range(n_demos)
            ]
            da = np.array(demo_means)
            dd = (
                float(da.mean() / da.std(ddof=1)) if da.std(ddof=1) > 0 else 0.0
            )

            entry = {
                "cohens_d": round(td, 4),
                "demo_level_cohens_d": round(dd, 4),
                "n_samples": len(tm),
                "mean_mse": round(float(tm.mean()), 6),
                "demo_mses": [round(v, 6) for v in demo_means],
                "instruction_correct": INSTRUCTIONS[ti],
                "instruction_counterfactual": _cf_instruction(ti, cond),
            }
            cond_res["per_task"][TASKS[ti]] = entry

        cond_res["cross_task_variance"] = {
            "cohens_d": {
                "values": [round(v, 4) for v in per_task_ds],
                "mean": round(float(np.mean(per_task_ds)), 4),
                "std": round(float(np.std(per_task_ds)), 4),
                "cv": (
                    round(float(np.std(per_task_ds) / np.mean(per_task_ds)), 4)
                    if np.mean(per_task_ds) > 0
                    else 0.0
                ),
            }
        }
        all_res[cond] = cond_res
        log(
            f"  {cond}: global d={global_d:.4f}  "
            f"cross-task mean={np.mean(per_task_ds):.4f}  "
            f"token_div={np.mean(all_tok_div):.3f}"
        )

    ranking = sorted(
        conditions,
        key=lambda c: all_res[c]["global_metrics"]["paired_mse"]["cohens_d"],
        reverse=True,
    )
    all_res["ranking_by_cohens_d"] = [
        {
            "condition": c,
            "cohens_d": all_res[c]["global_metrics"]["paired_mse"]["cohens_d"],
            "paired_mse_mean": all_res[c]["global_metrics"]["paired_mse"]["mean"],
        }
        for c in ranking
    ]
    return all_res


# ============================================================
# Model Loading
# ============================================================
def load_model(ckpt_path, condition):
    log(f"Loading {condition} model from {ckpt_path} ...")
    t0 = time.time()

    model = AutoModelForCausalLM.from_pretrained(
        ckpt_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation="eager",
    ).to(DEVICE).eval()

    processor = AutoProcessor.from_pretrained(
        ckpt_path, trust_remote_code=True, num_crops=1
    )

    log(f"  Model loaded in {time.time()-t0:.1f}s")
    return model, processor


# ============================================================
# Run all phases for one condition
# ============================================================
def run_pipeline(model, processor, condition, results_dir, args):
    global N_IMG_TOKENS, IMG_TOKEN_ID
    os.makedirs(results_dir, exist_ok=True)

    nt = 2 if args.dry_run else len(TASKS)
    nd = 1 if args.dry_run else N_DEMOS
    ns = 2 if args.dry_run else N_TIMESTEPS
    nps = 2 if args.dry_run else N_PROBE_SEEDS
    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None

    log(f"=== {condition.upper()} pipeline ===")
    log(f"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}")
    log(f"Output: {results_dir}")

    # Detect image token ID
    IMG_TOKEN_ID = detect_image_token_id(processor)
    log(f"  Image token ID: {IMG_TOKEN_ID}")

    # Validate token layout
    log("Validating token layout ...")
    hdf5_path = os.path.join(DATA, f"{TASKS[0]}_demo.hdf5")
    with h5py.File(hdf5_path, "r") as hf:
        img = Image.fromarray(hf["data/demo_0/obs/agentview_rgb"][0])
    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)
    original_ids = inputs["input_ids"].clone()
    log(f"  input_ids shape: {inputs['input_ids'].shape}")
    if "pixel_values" in inputs:
        log(f"  pixel_values shape: {inputs['pixel_values'].shape}")
    if "image_sizes" in inputs:
        log(f"  image_sizes: {inputs['image_sizes']}")

    with torch.no_grad():
        out = model(**inputs, output_hidden_states=True, output_attentions=True)

    hs0_shape = out.hidden_states[0].shape
    log(f"  hidden_states[0] shape: {hs0_shape}")

    tr = find_token_regions(original_ids, IMG_TOKEN_ID)
    N_IMG_TOKENS = tr["image"][1] - tr["image"][0]
    log(f"  Token regions: bos={tr['bos']} image={tr['image']} text={tr['text']}")
    log(f"  N_IMG_TOKENS={N_IMG_TOKENS}")
    log(f"  Total seq_len: input_ids={inputs['input_ids'].shape[1]}, hidden={hs0_shape[1]}")

    n_attn_layers = len(out.attentions)
    attn_shape = out.attentions[0].shape
    log(f"  Attention: {n_attn_layers} layers, shape={attn_shape}")

    del out, inputs
    torch.cuda.empty_cache()

    # Phase 1
    t1 = time.time()
    reps, actions, labels, l1_attns, tok_regs = extract_features(
        model, processor, nt, nd, ns, IMG_TOKEN_ID
    )
    log(f"Phase 1: {time.time()-t1:.1f}s")

    # Phase 2
    if not args.skip_probing:
        t2 = time.time()
        probe_res = run_probing(reps, actions, nps)
        with open(os.path.join(results_dir, "action_r2_probing.json"), "w") as f:
            json.dump(probe_res, f, indent=2)
        log(f"Phase 2: {time.time()-t2:.1f}s -> action_r2_probing.json")

    # Phase 3
    t3 = time.time()
    attn_res = analyze_attention(l1_attns, tok_regs)
    with open(os.path.join(results_dir, "l1_attention_profile.json"), "w") as f:
        json.dump(attn_res, f, indent=2)
    log(f"Phase 3: {time.time()-t3:.1f}s -> l1_attention_profile.json")

    del l1_attns, tok_regs

    # Phase 4
    t4 = time.time()
    cls_res = run_classification(reps, labels, layers=cls_layers)
    with open(os.path.join(results_dir, "cross_instruction_classification.json"), "w") as f:
        json.dump(cls_res, f, indent=2)
    log(f"Phase 4: {time.time()-t4:.1f}s -> cross_instruction_classification.json")

    del reps, actions, labels

    # Phase 5: Counterfactual (trained only)
    if condition == "trained" and not args.skip_counterfactual:
        t5 = time.time()
        cf_res = run_counterfactual(model, processor, nt, nd, ns)
        with open(os.path.join(results_dir, "counterfactual_combined.json"), "w") as f:
            json.dump(cf_res, f, indent=2)
        log(f"Phase 5: {time.time()-t5:.1f}s -> counterfactual_combined.json")
    elif condition != "trained":
        log("Phase 5: skipped (untrained model cannot generate meaningful actions)")


# ============================================================
# Main
# ============================================================
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--skip-counterfactual", action="store_true")
    p.add_argument("--skip-probing", action="store_true")
    p.add_argument(
        "--conditions",
        default="trained,untrained",
        help="Comma-separated: trained,untrained",
    )
    args = p.parse_args()

    conditions = [c.strip() for c in args.conditions.split(",")]
    log(f"Pipeline conditions: {conditions}")

    t_start = time.time()

    for condition in conditions:
        if condition == "trained":
            ckpt = TRAINED_CKPT
        elif condition == "untrained":
            if os.path.exists(os.path.join(UNTRAINED_CACHE, "config.json")):
                ckpt = UNTRAINED_CACHE
            else:
                ckpt = UNTRAINED_CKPT
                log(f"  Will download untrained model from {ckpt}")
        else:
            log(f"  Unknown condition: {condition}, skipping")
            continue

        results_dir = os.path.join(RESULTS_BASE, condition)

        try:
            model, processor = load_model(ckpt, condition)
        except Exception as e:
            log(f"  ERROR loading {condition} model: {e}")
            log(f"  Skipping {condition} condition")
            continue

        tc = time.time()
        run_pipeline(model, processor, condition, results_dir, args)
        log(f"  {condition} complete in {(time.time()-tc)/60:.1f} min")

        del model, processor
        torch.cuda.empty_cache()

    log(f"All done in {(time.time()-t_start)/60:.1f} min")


if __name__ == "__main__":
    main()
