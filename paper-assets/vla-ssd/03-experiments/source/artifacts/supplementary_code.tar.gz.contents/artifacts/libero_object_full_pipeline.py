#!/usr/bin/env python3
"""
LIBERO-Object Full Analysis Pipeline (Streaming)

Phases:
  1. Representation extraction: forward passes → hidden states + L1 attention
  2. Action R² probing: per-layer MLP probe, 15 seeds
  3. L1 attention profile: per-head instruction/image attention classification
  4. Cross-instruction classification: 10-way per-layer
  5. Counterfactual: 4 conditions (wrong/empty/shuffled/paraphrased), paired Cohen's d

All results → RESULTS_DIR/*.json
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
from transformers import AutoModelForVision2Seq, AutoProcessor

# ─── Configuration ────────────────────────────────────────────────
CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object"
DATA = "/root/autodl-tmp/vla-ssd/data/libero/libero_object"
RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results/libero_object"
DEVICE = "cuda:0"
UNNORM = "libero_object"

TASKS = [
    "pick_up_the_alphabet_soup_and_place_it_in_the_basket",
    "pick_up_the_cream_cheese_and_place_it_in_the_basket",
    "pick_up_the_salad_dressing_and_place_it_in_the_basket",
    "pick_up_the_bbq_sauce_and_place_it_in_the_basket",
    "pick_up_the_ketchup_and_place_it_in_the_basket",
    "pick_up_the_tomato_sauce_and_place_it_in_the_basket",
    "pick_up_the_butter_and_place_it_in_the_basket",
    "pick_up_the_milk_and_place_it_in_the_basket",
    "pick_up_the_chocolate_pudding_and_place_it_in_the_basket",
    "pick_up_the_orange_juice_and_place_it_in_the_basket",
]
INSTRUCTIONS = [t.replace("_", " ") for t in TASKS]
PARAPHRASES = [
    "grab the alphabet soup and put it into the basket",
    "grab the cream cheese and put it into the basket",
    "grab the salad dressing and put it into the basket",
    "grab the bbq sauce and put it into the basket",
    "grab the ketchup and put it into the basket",
    "grab the tomato sauce and put it into the basket",
    "grab the butter and put it into the basket",
    "grab the milk and put it into the basket",
    "grab the chocolate pudding and put it into the basket",
    "grab the orange juice and put it into the basket",
]

N_LAYERS = 32
N_HEADS = 32
HIDDEN = 4096
N_IMG_TOKENS = 256
N_DEMOS = 10
N_TIMESTEPS = 50
N_PROBE_SEEDS = 15


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def make_prompt(instruction):
    return f"In: What action should the robot take to {instruction}?\nOut:"


# ─── Shared utilities ─────────────────────────────────────────────

def prepare_inputs(processor, instruction, image):
    """Tokenize + image-process, move to device."""
    prompt = make_prompt(instruction)
    inputs = processor(prompt, image).to(DEVICE)
    return inputs


def generate_action(model, processor, instruction, image):
    """predict_action wrapper returning (continuous_action_7d, token_ids_7)."""
    inputs = prepare_inputs(processor, instruction, image)
    input_ids = inputs["input_ids"]

    if not torch.all(input_ids[:, -1] == 29871):
        input_ids = torch.cat(
            (input_ids, torch.tensor([[29871]], device=DEVICE, dtype=input_ids.dtype)), dim=1
        )
        if "attention_mask" in inputs:
            inputs["attention_mask"] = torch.cat(
                (inputs["attention_mask"],
                 torch.ones(1, 1, device=DEVICE, dtype=inputs["attention_mask"].dtype)), dim=1
            )
    inputs["input_ids"] = input_ids

    with torch.no_grad():
        gen_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs.get("attention_mask"),
            pixel_values=inputs.get("pixel_values"),
            max_new_tokens=7, do_sample=False,
        )
    token_ids = gen_ids[0, -7:].cpu().numpy()

    vocab_size = model.vocab_size
    disc = np.clip(vocab_size - token_ids - 1, 0, model.bin_centers.shape[0] - 1)
    norm_act = model.bin_centers[disc]

    stats = model.get_action_stats(UNNORM)
    mask = np.array(stats.get("mask", [True] * 7))
    high, low = np.array(stats["q99"]), np.array(stats["q01"])
    action = np.where(mask, 0.5 * (norm_act + 1) * (high - low) + low, norm_act)

    del inputs, gen_ids
    return action.astype(np.float64), token_ids


# ─── Phase 1: Representation Extraction ──────────────────────────

def extract_features(model, processor, n_tasks, n_demos, n_timesteps):
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
                    with torch.no_grad():
                        out = model(**inputs,
                                    output_hidden_states=True,
                                    output_attentions=True)

                    # Token layout after merge: [BOS(1)] [image(256)] [text(input_len-1)]
                    seq_len = out.hidden_states[0].shape[1]
                    img_s, img_e = 1, 1 + N_IMG_TOKENS
                    txt_s, txt_e = img_e, seq_len

                    for l in range(N_LAYERS):
                        hs = out.hidden_states[l + 1][0]  # [seq, hidden]
                        reps[l]["image_mean"][idx] = hs[img_s:img_e].float().mean(0).cpu().numpy()
                        reps[l]["last_preaction"][idx] = hs[-1].float().cpu().numpy()

                    # L1 attention (layer index 1)
                    l1 = out.attentions[1][0].float().cpu().numpy()  # [heads, seq, seq]
                    l1_attns.append(l1)
                    token_regions.append({"bos": (0, 1), "image": (img_s, img_e),
                                          "text": (txt_s, txt_e)})

                    actions_arr[idx] = act
                    task_labels[idx] = ti
                    idx += 1

                    del out, inputs
                    if idx % 100 == 0:
                        torch.cuda.empty_cache()
                        log(f"    {idx}/{total}")

    log(f"Phase 1 done: {idx} samples")
    return (reps, actions_arr[:idx], task_labels[:idx],
            l1_attns, token_regions)


# ─── Phase 2: Action R² Probing ──────────────────────────────────

def run_probing(reps, actions, n_seeds):
    log("Phase 2: action R² probing")
    results = {}
    for l in range(N_LAYERS):
        for pos in ("image_mean", "last_preaction"):
            X, y = reps[l][pos], actions
            r2s = []
            for s in range(n_seeds):
                n = len(X); nt = int(n * 0.8)
                perm = np.random.RandomState(s).permutation(n)
                Xtr, ytr = X[perm[:nt]], y[perm[:nt]]
                Xv, yv = X[perm[nt:]], y[perm[nt:]]

                probe = MLPRegressor(hidden_layer_sizes=(256,), max_iter=200,
                                     early_stopping=True, validation_fraction=0.2,
                                     random_state=s, n_iter_no_change=10)
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
            log(f"  L{l}: img_mean R²={results[f'L{l}_image_mean']['mean']:.4f}  "
                f"last_pre R²={results[f'L{l}_last_preaction']['mean']:.4f}")
    return results


# ─── Phase 3: L1 Attention Profile ───────────────────────────────

def analyze_attention(l1_attns, token_regions):
    log("Phase 3: L1 attention profile")
    n = len(l1_attns)
    head_ratios = {h: [] for h in range(N_HEADS)}

    for i in range(n):
        attn = l1_attns[i]  # [heads, seq, seq]
        tr = token_regions[i]
        last = attn.shape[1] - 1
        is_, ie = tr["image"]
        ts, te = tr["text"]

        for h in range(N_HEADS):
            row = attn[h, last, :]
            img_a = row[is_:ie].sum()
            txt_a = row[ts:te].sum()
            bos_a = row[0]
            total = img_a + txt_a + bos_a
            head_ratios[h].append(float(txt_a / total) if total > 1e-10 else 0.0)

    profiles = {}
    for h in range(N_HEADS):
        r = head_ratios[h]
        m = float(np.mean(r))
        cat = "instruction_dominant" if m > 0.5 else ("image_dominant" if m < 0.2 else "mixed")
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
        "instruction_dominant_heads": [h for h in range(N_HEADS)
                                       if profiles[f"head_{h}"]["category"] == "instruction_dominant"],
        "image_dominant_heads": [h for h in range(N_HEADS)
                                  if profiles[f"head_{h}"]["category"] == "image_dominant"],
    }
    log(f"  {summary['instruction_dominant']} instr-dom, "
        f"{summary['image_dominant']} img-dom, {summary['mixed']} mixed")
    return {"per_head": profiles, "summary": summary}


# ─── Phase 4: Cross-Instruction Classification ───────────────────

def run_classification(reps, labels, layers=None):
    log("Phase 4: cross-instruction classification")
    if layers is None:
        layers = list(range(N_LAYERS))
    n_cls = int(labels.max()) + 1
    results = {"chance": round(1.0 / n_cls, 4)}

    for l in layers:
        for pos in ("image_mean", "last_preaction"):
            X, y = reps[l][pos], labels
            n = len(X); nt = int(n * 0.8)
            perm = np.random.RandomState(42).permutation(n)
            Xtr, ytr = X[perm[:nt]], y[perm[:nt]]
            Xv, yv = X[perm[nt:]], y[perm[nt:]]

            clf = LogisticRegression(max_iter=2000, C=1.0, random_state=42)
            clf.fit(Xtr, ytr)
            results[f"L{l}_{pos}"] = round(float(clf.score(Xv, yv)), 4)

        log(f"  L{l}: img={results[f'L{l}_image_mean']:.3f}  "
            f"last_pre={results[f'L{l}_last_preaction']:.3f}")
    return results


# ─── Phase 5: Counterfactual ──────────────────────────────────────

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
            "experiment": "counterfactual_libero_object",
            "conditions": conditions,
            "n_tasks": n_tasks, "n_demos_per_task": n_demos,
            "n_timesteps_per_demo": n_timesteps,
            "model": "openvla-7b-finetuned-libero-object",
            "unnorm_key": UNNORM, "seed": 42,
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
                            hf[f"data/demo_{di}/obs/agentview_rgb"][t])

                        c_act, c_tok = generate_action(
                            model, processor, INSTRUCTIONS[ti], img)
                        f_act, f_tok = generate_action(
                            model, processor, cf_instr, img)

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
                            log(f"    {sample_n}/{n_tasks * n_demos * n_timesteps}")

        mse_arr = np.array(all_mses)
        global_d = float(mse_arr.mean() / mse_arr.std(ddof=1)) if mse_arr.std(ddof=1) > 0 else 0.0

        # Per-dim shift (global)
        ca_all = np.concatenate([np.array(per_task_correct[ti]) for ti in range(n_tasks)])
        cf_all = np.concatenate([np.array(per_task_cf[ti]) for ti in range(n_tasks)])
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
                    "dim_names": ["dx","dy","dz","rx","ry","rz","gripper"],
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
            td = float(tm.mean() / tm.std(ddof=1)) if tm.std(ddof=1) > 0 else 0.0
            per_task_ds.append(td)

            demo_means = [float(np.mean(per_task_demo_mses[ti][di]))
                          for di in range(n_demos)]
            da = np.array(demo_means)
            dd = float(da.mean() / da.std(ddof=1)) if da.std(ddof=1) > 0 else 0.0

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
                "cv": round(float(np.std(per_task_ds) / np.mean(per_task_ds)), 4)
                     if np.mean(per_task_ds) > 0 else 0.0,
            }
        }
        all_res[cond] = cond_res
        log(f"  {cond}: global d={global_d:.4f}  "
            f"cross-task mean={np.mean(per_task_ds):.4f}  "
            f"token_div={np.mean(all_tok_div):.3f}")

    ranking = sorted(conditions,
                     key=lambda c: all_res[c]["global_metrics"]["paired_mse"]["cohens_d"],
                     reverse=True)
    all_res["ranking_by_cohens_d"] = [
        {"condition": c,
         "cohens_d": all_res[c]["global_metrics"]["paired_mse"]["cohens_d"],
         "paired_mse_mean": all_res[c]["global_metrics"]["paired_mse"]["mean"]}
        for c in ranking
    ]
    return all_res


# ─── Main ─────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true",
                   help="1 task, 1 demo, 2 timesteps, 2 probe seeds")
    p.add_argument("--skip-counterfactual", action="store_true")
    p.add_argument("--skip-probing", action="store_true")
    args = p.parse_args()

    os.makedirs(RESULTS_DIR, exist_ok=True)

    nt = 1 if args.dry_run else len(TASKS)
    nd = 1 if args.dry_run else N_DEMOS
    ns = 2 if args.dry_run else N_TIMESTEPS
    nps = 2 if args.dry_run else N_PROBE_SEEDS
    cls_layers = [0, 8, 16, 24, 31] if args.dry_run else None

    log(f"Config: tasks={nt} demos={nd} timesteps={ns} seeds={nps} dry_run={args.dry_run}")
    log(f"Output: {RESULTS_DIR}")

    # ── Load model ──
    log("Loading model …")
    t0 = time.time()
    model = AutoModelForVision2Seq.from_pretrained(
        CKPT, torch_dtype=torch.bfloat16, trust_remote_code=True
    ).to(DEVICE).eval()
    processor = AutoProcessor.from_pretrained(CKPT, trust_remote_code=True)
    log(f"Model loaded in {time.time()-t0:.1f}s")

    # ── Validate token layout (one sample) ──
    log("Validating token layout …")
    hdf5_path = os.path.join(DATA, f"{TASKS[0]}_demo.hdf5")
    with h5py.File(hdf5_path, "r") as hf:
        img = Image.fromarray(hf["data/demo_0/obs/agentview_rgb"][0])
    inputs = prepare_inputs(processor, INSTRUCTIONS[0], img)
    log(f"  input_ids shape: {inputs['input_ids'].shape}")
    log(f"  pixel_values shape: {inputs['pixel_values'].shape}")
    with torch.no_grad():
        out = model(**inputs, output_hidden_states=True, output_attentions=True)
    hs0_shape = out.hidden_states[0].shape
    log(f"  hidden_states[0] shape: {hs0_shape}  "
        f"(expect seq_len = input_ids_len + {N_IMG_TOKENS})")
    expected_seq = inputs["input_ids"].shape[1] + N_IMG_TOKENS
    actual_seq = hs0_shape[1]
    assert actual_seq == expected_seq, (
        f"Seq len mismatch: expected {expected_seq}, got {actual_seq}. "
        f"Adjust N_IMG_TOKENS."
    )
    log(f"  ✓ token layout validated: BOS(1) + img({N_IMG_TOKENS}) + text({inputs['input_ids'].shape[1]-1})")
    del out, inputs
    torch.cuda.empty_cache()

    # ── Phase 1 ──
    t1 = time.time()
    reps, actions, labels, l1_attns, tok_regs = extract_features(
        model, processor, nt, nd, ns)
    log(f"Phase 1: {time.time()-t1:.1f}s")

    # ── Phase 2 ──
    if not args.skip_probing:
        t2 = time.time()
        probe_res = run_probing(reps, actions, nps)
        with open(os.path.join(RESULTS_DIR, "action_r2_probing.json"), "w") as f:
            json.dump(probe_res, f, indent=2)
        log(f"Phase 2: {time.time()-t2:.1f}s  → action_r2_probing.json")

    # ── Phase 3 ──
    t3 = time.time()
    attn_res = analyze_attention(l1_attns, tok_regs)
    with open(os.path.join(RESULTS_DIR, "l1_attention_profile.json"), "w") as f:
        json.dump(attn_res, f, indent=2)
    log(f"Phase 3: {time.time()-t3:.1f}s  → l1_attention_profile.json")

    del l1_attns, tok_regs

    # ── Phase 4 ──
    t4 = time.time()
    cls_res = run_classification(reps, labels, layers=cls_layers)
    with open(os.path.join(RESULTS_DIR, "cross_instruction_classification.json"), "w") as f:
        json.dump(cls_res, f, indent=2)
    log(f"Phase 4: {time.time()-t4:.1f}s  → cross_instruction_classification.json")

    del reps, actions, labels

    # ── Phase 5 ──
    if not args.skip_counterfactual:
        t5 = time.time()
        cf_res = run_counterfactual(model, processor, nt, nd, ns)
        with open(os.path.join(RESULTS_DIR, "counterfactual_combined.json"), "w") as f:
            json.dump(cf_res, f, indent=2)
        log(f"Phase 5: {time.time()-t5:.1f}s  → counterfactual_combined.json")

    total_t = time.time() - t0
    log(f"Pipeline complete in {total_t/60:.1f} min")


if __name__ == "__main__":
    main()
