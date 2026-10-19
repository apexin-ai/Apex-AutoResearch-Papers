#!/usr/bin/env python3
"""Holdout verification for OT-7B (Table 3) and R1-32B (Table 3 + Table 4).

Extracts hidden states if not cached, runs HS vs text holdout evaluation
with 10k BCa bootstrap, and generates JSON verification files.

Usage:
    python verify_holdout.py --model ot_7b
    python verify_holdout.py --model r1_32b
    python verify_holdout.py --model all
"""

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_HUB_DISABLE_XET"] = "1"

import argparse
import json
import time
import gc
import warnings
import numpy as np
import torch
from pathlib import Path
from collections import defaultdict
from datetime import datetime

from scipy.stats import norm
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import balanced_accuracy_score

warnings.filterwarnings("ignore")

SEED = 42
PCA_DIM = 100
MAX_ITER = 2000
N_BOOTSTRAP = 10000
SAFETY_LABELS = {"RA", "AL", "CC", "ED", "IA"}
BASE = Path("/root/autodl-tmp/contrastive_trace_safety")
OUT_DIR = BASE / "artifacts" / "verification"

MODEL_CFGS = {
    "ot_7b": {
        "hf_name": "open-thoughts/OpenThinker-7B",
        "dataset_name": "ot-7b",
        "layer": 16,
        "window": 3,
        "hidden_dim": 3584,
        "num_layers": 28,
        "hs_dir": BASE / "artifacts" / "hidden_states_ot7b_verify",
        "paper_values": {
            "delta_ba": 10.7, "delta_prec": 21.9,
            "ci": [14.4, 29.6], "delta_fpr": -17.1,
        },
    },
    "r1_32b": {
        "hf_name": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        "dataset_name": "r1-32b",
        "layer": 63,
        "window": 1,
        "hidden_dim": 5120,
        "num_layers": 64,
        "hs_dir": BASE / "artifacts" / "hidden_states_r1_32b_verify",
        "paper_values": {
            "delta_ba": 18.7, "delta_prec": 15.4,
            "ci": [8.7, 22.6], "delta_fpr": -14.6,
        },
        "table4_values": {
            "coverage": 0.25, "lead_range": [11.7, 13.3],
            "position_margin": 14.2,
        },
    },
}


def ts():
    return time.strftime("[%H:%M:%S]")


# ── Data loading ────────────────────────────────────────────────────────

def load_harmthoughts():
    print(f"{ts()} Loading HarmThoughts dataset...", flush=True)
    from datasets import load_dataset
    ds = load_dataset("ishitakakkar-10/HarmThoughts", split="train",
                      cache_dir="/root/autodl-tmp/.hf_cache")
    traces_by_model = defaultdict(lambda: defaultdict(list))
    for row in ds:
        model = row["model_name"]
        sid = row["sentence_id"]
        trace_id, step_str = sid.rsplit("-", 1)
        step_idx = int(step_str) - 1
        traces_by_model[model][trace_id].append({
            "step_idx": step_idx,
            "sentence": row["sentence"],
            "annotation": row["llm_annotation"],
            "final_judgment": row["final_judgment"],
        })
    return traces_by_model


def prepare_traces(trace_data):
    traces = []
    for trace_id, steps in sorted(trace_data.items()):
        steps.sort(key=lambda x: x["step_idx"])
        if steps[0]["final_judgment"] != 1.0:
            continue
        sentences = [s["sentence"] for s in steps]
        annotations = [s["annotation"] for s in steps]
        last_safety_idx = None
        for i, ann in enumerate(annotations):
            if ann in SAFETY_LABELS:
                last_safety_idx = i
        if last_safety_idx is None or last_safety_idx >= len(annotations) - 1:
            continue
        cp = last_safety_idx + 1
        step_labels = [0 if i < cp else 1 for i in range(len(sentences))]
        traces.append({
            "trace_id": trace_id,
            "sentences": sentences,
            "step_labels": step_labels,
            "commitment_point": cp,
        })
    return traces


# ── Hidden state extraction ─────────────────────────────────────────────

def find_sentence_boundaries(tokenizer, sentences):
    full_text = " ".join(sentences)
    encoding = tokenizer(
        full_text, return_offsets_mapping=True,
        return_tensors="pt", truncation=True, max_length=8192,
    )
    offsets = encoding["offset_mapping"][0]
    boundaries = []
    char_pos = 0
    for sent in sentences:
        char_end = char_pos + len(sent)
        last_token_idx = 0
        for tok_idx, (start, end) in enumerate(offsets):
            if start < char_end:
                last_token_idx = tok_idx
        boundaries.append(last_token_idx)
        char_pos = char_end + 1
    return boundaries


def extract_hs_single(model, tokenizer, sentences, target_layer, device="cuda:0"):
    boundaries = find_sentence_boundaries(tokenizer, sentences)
    full_text = " ".join(sentences)
    inputs = tokenizer(full_text, return_tensors="pt", truncation=True,
                       max_length=8192).to(device)
    num_tokens = inputs["input_ids"].shape[1]
    boundaries = [min(p, num_tokens - 1) for p in boundaries]

    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)

    hs_layer = outputs.hidden_states[target_layer + 1]
    hidden_dim = hs_layer.shape[-1]
    result = torch.zeros(len(sentences), hidden_dim, dtype=torch.float16)
    for i, pos in enumerate(boundaries):
        result[i] = hs_layer[0, pos, :].cpu().half()

    del outputs
    torch.cuda.empty_cache()
    return result


def extract_all_hs(model_key, cfg, traces):
    hs_dir = cfg["hs_dir"]
    hs_dir.mkdir(parents=True, exist_ok=True)

    existing = {f.stem for f in hs_dir.glob("*.pt")}
    remaining = [t for t in traces if t["trace_id"] not in existing]

    if not remaining:
        print(f"{ts()} All {len(traces)} traces already extracted for {model_key}.", flush=True)
        return

    print(f"{ts()} Extracting {len(remaining)}/{len(traces)} traces for {model_key}...", flush=True)
    from transformers import AutoTokenizer, AutoModelForCausalLM

    print(f"{ts()} Loading model: {cfg['hf_name']}...", flush=True)
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(
        cfg["hf_name"], trust_remote_code=True,
        cache_dir="/root/autodl-tmp/.hf_cache",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        cfg["hf_name"], torch_dtype=torch.float16, device_map="cuda:0",
        trust_remote_code=True, cache_dir="/root/autodl-tmp/.hf_cache",
    )
    model.eval()
    print(f"{ts()} Model loaded in {time.time()-t0:.0f}s", flush=True)

    for i, trace in enumerate(remaining):
        hs = extract_hs_single(model, tokenizer, trace["sentences"], cfg["layer"])
        save_dict = {
            "hidden_states": hs,
            "trace_id": trace["trace_id"],
            "step_labels": trace["step_labels"],
            "commitment_point": trace["commitment_point"],
            "num_sentences": len(trace["sentences"]),
        }
        torch.save(save_dict, hs_dir / f"{trace['trace_id']}.pt")
        if (i + 1) % 20 == 0 or (i + 1) == len(remaining):
            print(f"  [{i+1}/{len(remaining)}] extracted", flush=True)

    del model, tokenizer
    torch.cuda.empty_cache()
    gc.collect()
    print(f"{ts()} Extraction done for {model_key}.", flush=True)


# ── Feature building ────────────────────────────────────────────────────

def build_windowed_concat(traces_data, dim, window):
    X_list, y_list, n_per = [], [], []
    for t in traces_data:
        feats = t["feats"]
        labels = np.array(t["step_labels"], dtype=np.int32)
        T = min(feats.shape[0], len(labels))
        feats, labels = feats[:T], labels[:T]
        padded = np.concatenate([np.repeat(feats[:1], window - 1, axis=0), feats])
        win = np.empty((T, window * dim), dtype=feats.dtype)
        for w in range(window):
            win[:, w * dim:(w + 1) * dim] = padded[w:w + T]
        X_list.append(win)
        y_list.append(labels)
        n_per.append(T)
    return np.vstack(X_list), np.concatenate(y_list), n_per


def load_hs_traces(cfg, traces):
    loaded = []
    for trace in traces:
        pt = cfg["hs_dir"] / f"{trace['trace_id']}.pt"
        if not pt.exists():
            continue
        d = torch.load(pt, map_location="cpu", weights_only=False)
        hs = d["hidden_states"].float().numpy()
        loaded.append({
            "trace_id": trace["trace_id"],
            "feats": hs,
            "sentences": trace["sentences"],
            "step_labels": trace["step_labels"][:hs.shape[0]],
            "commitment_point": trace["commitment_point"],
        })
    return loaded


def encode_text_traces(traces, st_model):
    encoded = []
    for t in traces:
        sents = t["sentences"]
        labels = t["step_labels"]
        T = min(len(sents), len(labels))
        embs = st_model.encode(sents[:T], show_progress_bar=False,
                               normalize_embeddings=True)
        encoded.append({
            "trace_id": t["trace_id"],
            "feats": embs,
            "step_labels": labels[:T],
            "commitment_point": t["commitment_point"],
        })
    return encoded


# ── Split ────────────────────────────────────────────────────────────────

def split_60_20_20(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(traces))
    n_tr = int(len(traces) * 0.6)
    n_va = int(len(traces) * 0.2)
    return (
        [traces[i] for i in idx[:n_tr]],
        [traces[i] for i in idx[n_tr:n_tr + n_va]],
        [traces[i] for i in idx[n_tr + n_va:]],
    )


# ── Evaluation ───────────────────────────────────────────────────────────

def train_predict(X_tr, y_tr, X_te, y_te, n_per_te):
    pca_dim = min(PCA_DIM, X_tr.shape[1], X_tr.shape[0])
    pca = PCA(n_components=pca_dim, random_state=SEED)
    X_tr_p = pca.fit_transform(X_tr)
    X_te_p = pca.transform(X_te)

    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_tr_p)
    X_te_s = scaler.transform(X_te_p)

    clf = LogisticRegression(C=1.0, class_weight="balanced", solver="lbfgs",
                             max_iter=MAX_ITER, random_state=SEED)
    clf.fit(X_tr_s, y_tr)

    y_pred = clf.predict(X_te_s)
    y_prob = clf.predict_proba(X_te_s)[:, 1]

    tp = int(((y_pred == 1) & (y_te == 1)).sum())
    fp = int(((y_pred == 1) & (y_te == 0)).sum())
    tn = int(((y_pred == 0) & (y_te == 0)).sum())
    fn = int(((y_pred == 0) & (y_te == 1)).sum())

    ba = (tp / (tp + fn) if (tp + fn) > 0 else 0) + (tn / (tn + fp) if (tn + fp) > 0 else 0)
    ba /= 2
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    per_trace_ba, per_trace_prec, per_trace_fpr = [], [], []
    per_trace_probs = []
    offset = 0
    for nt in n_per_te:
        yp = y_pred[offset:offset + nt]
        yt = y_te[offset:offset + nt]
        prob = y_prob[offset:offset + nt]

        t_tp = int(((yp == 1) & (yt == 1)).sum())
        t_fp = int(((yp == 1) & (yt == 0)).sum())
        t_tn = int(((yp == 0) & (yt == 0)).sum())
        t_fn = int(((yp == 0) & (yt == 1)).sum())

        tpr_ = t_tp / (t_tp + t_fn) if (t_tp + t_fn) > 0 else 0
        tnr_ = t_tn / (t_tn + t_fp) if (t_tn + t_fp) > 0 else 0
        per_trace_ba.append((tpr_ + tnr_) / 2)
        per_trace_prec.append(t_tp / (t_tp + t_fp) if (t_tp + t_fp) > 0 else 0.0)
        per_trace_fpr.append(t_fp / (t_fp + t_tn) if (t_fp + t_tn) > 0 else 0.0)
        per_trace_probs.append(prob)
        offset += nt

    return {
        "ba": round(ba, 4), "prec": round(prec, 4), "fpr": round(fpr, 4),
        "per_ba": np.array(per_trace_ba),
        "per_prec": np.array(per_trace_prec),
        "per_fpr": np.array(per_trace_fpr),
        "per_probs": per_trace_probs,
        "pca_var": round(float(pca.explained_variance_ratio_.sum()), 4),
    }


def bca_ci(va, vb, n_boot=N_BOOTSTRAP, alpha=0.05, seed=SEED):
    n = len(va)
    observed = float(va.mean() - vb.mean())
    rng = np.random.default_rng(seed)

    deltas = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        deltas[i] = va[idx].mean() - vb[idx].mean()

    prop = np.clip(np.mean(deltas < observed), 1e-10, 1 - 1e-10)
    z0 = norm.ppf(prop)

    jack = np.empty(n)
    for i in range(n):
        m = np.ones(n, dtype=bool)
        m[i] = False
        jack[i] = va[m].mean() - vb[m].mean()
    jm = jack.mean()
    num = ((jm - jack) ** 3).sum()
    den = 6 * (((jm - jack) ** 2).sum() ** 1.5)
    a = num / den if den != 0 else 0

    z_lo, z_hi = norm.ppf(alpha / 2), norm.ppf(1 - alpha / 2)
    t1 = z0 + z_lo
    a1 = norm.cdf(z0 + t1 / (1 - a * t1))
    t2 = z0 + z_hi
    a2 = norm.cdf(z0 + t2 / (1 - a * t2))

    ci_lo = float(np.percentile(deltas, 100 * np.clip(a1, 0.001, 0.999)))
    ci_hi = float(np.percentile(deltas, 100 * np.clip(a2, 0.001, 0.999)))

    p_val = float(np.mean(deltas <= 0))

    return {
        "observed": round(observed, 4),
        "ci_lo": round(ci_lo, 4), "ci_hi": round(ci_hi, 4),
        "p": round(p_val, 6),
    }


# ── Table 4 (R1-32B) ────────────────────────────────────────────────────

def compute_table4(hs_results, test_traces, n_per_te):
    K = 5
    threshold = 0.5

    n_test = len(test_traces)
    n_crossing = 0
    lead_times = []

    for i, t in enumerate(test_traces):
        probs = hs_results["per_probs"][i]
        cp = t["commitment_point"]
        T = len(probs)

        fc = None
        count = 0
        for j in range(T):
            if probs[j] > threshold:
                count += 1
                if count >= K:
                    fc = j - K + 1
                    break
            else:
                count = 0

        if fc is not None and fc < cp:
            n_crossing += 1
            lead_times.append(cp - fc)

    coverage = n_crossing / n_test if n_test > 0 else 0.0
    lead_mean = float(np.mean(lead_times)) if lead_times else 0.0
    lead_range = [float(np.min(lead_times)), float(np.max(lead_times))] if lead_times else [0, 0]

    # Position baseline: train probe on t/T only
    X_pos_list, y_pos_list = [], []
    for t in test_traces:
        T = len(t["step_labels"])
        positions = np.array([i / T for i in range(T)]).reshape(-1, 1)
        X_pos_list.append(positions)
        y_pos_list.append(np.array(t["step_labels"][:T], dtype=np.int32))

    # Need train traces for position baseline training
    # This will be called with full context in run_r1_32b_table4

    return {
        "coverage": round(coverage, 4),
        "lead_mean": round(lead_mean, 1),
        "lead_range": [round(x, 1) for x in lead_range],
        "n_crossing": n_crossing,
        "n_test": n_test,
    }


def run_position_baseline(train_val_traces, test_traces):
    X_tr, y_tr = [], []
    for t in train_val_traces:
        T = len(t["step_labels"])
        pos = np.array([i / T for i in range(T)]).reshape(-1, 1)
        X_tr.append(pos)
        y_tr.append(np.array(t["step_labels"][:T]))
    X_tr = np.vstack(X_tr)
    y_tr = np.concatenate(y_tr)

    clf = LogisticRegression(C=1.0, class_weight="balanced", solver="lbfgs",
                             max_iter=MAX_ITER, random_state=SEED)
    clf.fit(X_tr, y_tr)

    X_te, y_te = [], []
    for t in test_traces:
        T = len(t["step_labels"])
        pos = np.array([i / T for i in range(T)]).reshape(-1, 1)
        X_te.append(pos)
        y_te.append(np.array(t["step_labels"][:T]))
    X_te = np.vstack(X_te)
    y_te = np.concatenate(y_te)

    y_pred = clf.predict(X_te)
    ba = balanced_accuracy_score(y_te, y_pred)
    return round(float(ba), 4)


# ── Main evaluation ─────────────────────────────────────────────────────

def run_model(model_key, cfg, all_traces_by_model, st_model):
    print(f"\n{'='*60}", flush=True)
    print(f"  {model_key}: Layer {cfg['layer']}, W={cfg['window']}", flush=True)
    print(f"{'='*60}", flush=True)

    dataset_name = cfg["dataset_name"]
    traces = prepare_traces(all_traces_by_model[dataset_name])
    print(f"{ts()} Prepared {len(traces)} traces (jailbreak with valid CP)", flush=True)

    # Phase 1: Extract hidden states
    extract_all_hs(model_key, cfg, traces)

    # Phase 2: Load and evaluate
    hs_traces = load_hs_traces(cfg, traces)
    print(f"{ts()} Loaded {len(hs_traces)} HS traces", flush=True)

    train, val, test = split_60_20_20(hs_traces)
    train_val = train + val
    print(f"{ts()} Split: train={len(train)}, val={len(val)}, test={len(test)}", flush=True)

    hidden_dim = cfg["hidden_dim"]
    window = cfg["window"]

    # HS features
    print(f"{ts()} Building HS features (W={window}, concat)...", flush=True)
    X_tr_hs, y_tr_hs, _ = build_windowed_concat(train_val, hidden_dim, window)
    X_te_hs, y_te_hs, n_te_hs = build_windowed_concat(test, hidden_dim, window)
    print(f"  HS feature dim: {X_tr_hs.shape[1]}", flush=True)

    # Text features
    print(f"{ts()} Building text features (MiniLM, W={window}, concat)...", flush=True)
    text_train_val = encode_text_traces(train_val, st_model)
    text_test = encode_text_traces(test, st_model)
    text_dim = 384
    X_tr_txt, y_tr_txt, _ = build_windowed_concat(text_train_val, text_dim, window)
    X_te_txt, y_te_txt, n_te_txt = build_windowed_concat(text_test, text_dim, window)
    print(f"  Text feature dim: {X_tr_txt.shape[1]}", flush=True)

    # Train and predict
    print(f"{ts()} Training HS probe...", flush=True)
    hs_res = train_predict(X_tr_hs, y_tr_hs, X_te_hs, y_te_hs, n_te_hs)
    print(f"  HS: BA={hs_res['ba']}, Prec={hs_res['prec']}, FPR={hs_res['fpr']} "
          f"(PCA var={hs_res['pca_var']})", flush=True)

    print(f"{ts()} Training Text probe...", flush=True)
    txt_res = train_predict(X_tr_txt, y_tr_txt, X_te_txt, y_te_txt, n_te_txt)
    print(f"  Text: BA={txt_res['ba']}, Prec={txt_res['prec']}, FPR={txt_res['fpr']}", flush=True)

    delta_ba = round(hs_res["ba"] - txt_res["ba"], 4)
    delta_prec = round(hs_res["prec"] - txt_res["prec"], 4)
    delta_fpr = round(hs_res["fpr"] - txt_res["fpr"], 4)
    print(f"  Delta: BA={delta_ba}, Prec={delta_prec}, FPR={delta_fpr}", flush=True)

    # BCa bootstrap
    print(f"{ts()} Running {N_BOOTSTRAP} BCa bootstrap...", flush=True)
    t0 = time.time()
    prec_ci = bca_ci(hs_res["per_prec"], txt_res["per_prec"], seed=SEED)
    ba_ci = bca_ci(hs_res["per_ba"], txt_res["per_ba"], seed=SEED + 1)
    fpr_ci = bca_ci(hs_res["per_fpr"], txt_res["per_fpr"], seed=SEED + 2)
    print(f"  Bootstrap done in {time.time()-t0:.1f}s", flush=True)
    print(f"  Prec CI: [{prec_ci['ci_lo']}, {prec_ci['ci_hi']}], p={prec_ci['p']}", flush=True)
    print(f"  BA CI: [{ba_ci['ci_lo']}, {ba_ci['ci_hi']}], p={ba_ci['p']}", flush=True)
    print(f"  FPR CI: [{fpr_ci['ci_lo']}, {fpr_ci['ci_hi']}], p={fpr_ci['p']}", flush=True)

    # Table 4 for R1-32B
    table4 = None
    if model_key == "r1_32b":
        print(f"\n{ts()} Computing Table 4 (R1-32B temporal analysis)...", flush=True)
        t4 = compute_table4(hs_res, test, n_te_hs)
        pos_ba = run_position_baseline(train_val, test)
        hs_ba = hs_res["ba"]
        pos_margin = round(hs_ba - pos_ba, 4)
        t4["position_ba"] = pos_ba
        t4["hs_ba"] = hs_ba
        t4["position_margin_pp"] = round(pos_margin * 100, 1)
        table4 = t4
        print(f"  Coverage: {t4['coverage']}", flush=True)
        print(f"  Lead: {t4['lead_mean']} steps ({t4['lead_range']})", flush=True)
        print(f"  Position margin: {t4['position_margin_pp']}pp", flush=True)

    return {
        "hs": hs_res, "text": txt_res,
        "delta_ba": delta_ba, "delta_prec": delta_prec, "delta_fpr": delta_fpr,
        "prec_ci": prec_ci, "ba_ci": ba_ci, "fpr_ci": fpr_ci,
        "n_train_val": len(train_val), "n_test": len(test),
        "n_total": len(hs_traces),
        "table4": table4,
    }


def build_json(model_key, cfg, results):
    pv = cfg["paper_values"]
    delta_ba_pp = round(results["delta_ba"] * 100, 1)
    delta_prec_pp = round(results["delta_prec"] * 100, 1)
    delta_fpr_pp = round(results["delta_fpr"] * 100, 1)
    ci_lo_pp = round(results["prec_ci"]["ci_lo"] * 100, 1)
    ci_hi_pp = round(results["prec_ci"]["ci_hi"] * 100, 1)

    match = (
        abs(delta_ba_pp - pv["delta_ba"]) <= 1.0 and
        abs(delta_prec_pp - pv["delta_prec"]) <= 1.0 and
        abs(ci_lo_pp - pv["ci"][0]) <= 2.0 and
        abs(ci_hi_pp - pv["ci"][1]) <= 2.0 and
        abs(delta_fpr_pp - pv["delta_fpr"]) <= 1.0
    )

    out = {
        "task": f"{model_key}_holdout_verification",
        "model": cfg["hf_name"],
        "layer": cfg["layer"],
        "window": cfg["window"],
        "split": "60/20/20",
        "seed": SEED,
        "results": {
            "hs_ba": results["hs"]["ba"],
            "text_ba": results["text"]["ba"],
            "delta_ba": delta_ba_pp,
            "hs_precision": results["hs"]["prec"],
            "text_precision": results["text"]["prec"],
            "delta_precision": delta_prec_pp,
            "ci_95_lower": ci_lo_pp,
            "ci_95_upper": ci_hi_pp,
            "hs_fpr": results["hs"]["fpr"],
            "text_fpr": results["text"]["fpr"],
            "delta_fpr": delta_fpr_pp,
            "n_bootstrap": N_BOOTSTRAP,
            "pca_dim": PCA_DIM,
            "pca_explained_var_hs": results["hs"]["pca_var"],
        },
        "paper_values": pv,
        "match": match,
        "data_path": str(cfg["hs_dir"]),
        "timestamp": datetime.now().isoformat(),
    }
    return out


def build_table4_json(cfg, results):
    t4 = results["table4"]
    tv = cfg.get("table4_values", {})

    lead_ok = (len(t4["lead_range"]) == 2 and
               abs(t4["lead_range"][0] - tv.get("lead_range", [0, 0])[0]) <= 3.0 and
               abs(t4["lead_range"][1] - tv.get("lead_range", [0, 0])[1]) <= 3.0)
    cov_ok = abs(t4["coverage"] - tv.get("coverage", 0)) <= 0.10
    margin_ok = abs(t4["position_margin_pp"] - tv.get("position_margin", 0)) <= 3.0

    return {
        "task": "r1_32b_table4_verification",
        "model": cfg["hf_name"],
        "layer": cfg["layer"],
        "window": cfg["window"],
        "results": {
            "coverage": t4["coverage"],
            "lead_mean": t4["lead_mean"],
            "lead_range": t4["lead_range"],
            "n_crossing": t4["n_crossing"],
            "n_test": t4["n_test"],
            "hs_ba": t4["hs_ba"],
            "position_ba": t4["position_ba"],
            "position_margin_pp": t4["position_margin_pp"],
        },
        "paper_values": tv,
        "match": cov_ok and lead_ok and margin_ok,
        "match_detail": {
            "coverage_ok": cov_ok,
            "lead_ok": lead_ok,
            "margin_ok": margin_ok,
        },
        "timestamp": datetime.now().isoformat(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="all", choices=["ot_7b", "r1_32b", "all"])
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    models_to_run = ["ot_7b", "r1_32b"] if args.model == "all" else [args.model]

    all_traces = load_harmthoughts()

    # Load text encoder
    print(f"{ts()} Loading MiniLM-L6-v2...", flush=True)
    from sentence_transformers import SentenceTransformer
    st_model = SentenceTransformer("all-MiniLM-L6-v2",
                                   cache_folder="/root/autodl-tmp/.hf_cache/sentence_transformers")
    print(f"{ts()} MiniLM loaded.", flush=True)

    for model_key in models_to_run:
        cfg = MODEL_CFGS[model_key]
        results = run_model(model_key, cfg, all_traces, st_model)

        # Save holdout JSON
        holdout_json = build_json(model_key, cfg, results)
        out_path = OUT_DIR / f"{model_key}_holdout_verification.json"
        with open(out_path, "w") as f:
            json.dump(holdout_json, f, indent=2)
        print(f"\n{ts()} Saved: {out_path}", flush=True)

        match_str = "MATCH" if holdout_json["match"] else "MISMATCH"
        print(f"  Paper vs Rerun ({match_str}):", flush=True)
        print(f"    DBA:  paper={cfg['paper_values']['delta_ba']:+.1f}, "
              f"rerun={holdout_json['results']['delta_ba']:+.1f}", flush=True)
        print(f"    DPrec: paper={cfg['paper_values']['delta_prec']:+.1f}, "
              f"rerun={holdout_json['results']['delta_precision']:+.1f}", flush=True)
        ci = cfg['paper_values']['ci']
        print(f"    CI:   paper=[{ci[0]:+.1f}, {ci[1]:+.1f}], "
              f"rerun=[{holdout_json['results']['ci_95_lower']:+.1f}, "
              f"{holdout_json['results']['ci_95_upper']:+.1f}]", flush=True)
        print(f"    DFPR: paper={cfg['paper_values']['delta_fpr']:+.1f}, "
              f"rerun={holdout_json['results']['delta_fpr']:+.1f}", flush=True)

        # Table 4 for R1-32B
        if model_key == "r1_32b" and results["table4"]:
            t4_json = build_table4_json(cfg, results)
            t4_path = OUT_DIR / "r1_32b_table4_verification.json"
            with open(t4_path, "w") as f:
                json.dump(t4_json, f, indent=2)
            print(f"\n{ts()} Saved: {t4_path}", flush=True)
            t4_match = "MATCH" if t4_json["match"] else "MISMATCH"
            tv = cfg["table4_values"]
            t4r = t4_json["results"]
            print(f"  Table 4 ({t4_match}):", flush=True)
            print(f"    Coverage: paper={tv['coverage']}, rerun={t4r['coverage']}", flush=True)
            print(f"    Lead: paper={tv['lead_range']}, rerun={t4r['lead_range']}", flush=True)
            print(f"    Pos margin: paper={tv['position_margin']}pp, "
                  f"rerun={t4r['position_margin_pp']}pp", flush=True)

    print(f"\n{ts()} ALL DONE.", flush=True)


if __name__ == "__main__":
    main()
