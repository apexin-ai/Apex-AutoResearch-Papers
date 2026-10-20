#!/usr/bin/env python3
"""Ordinal baseline: test if existing AI detectors' scores carry depth signal.
Input:  data/{model}/generations.jsonl
Output: results/ordinal_baseline_results.json
"""
import argparse, json, os, sys, time
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from scipy.spatial.distance import jensenshannon
from scipy.stats import spearmanr
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier
import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
DEVICE = "cuda:0"
MAX_LEN = 512
HF_CACHE = "/root/autodl-tmp/.hf_cache"
N_BOOTSTRAP = 1000

MODEL_SOURCES = {
    "pythia-2.8b": DATA / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
}


def load_texts(max_per_model=None):
    records = []
    for model_name, path in MODEL_SOURCES.items():
        if not path.exists():
            print(f"  SKIP {path}")
            continue
        count = 0
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = model_name
                records.append(rec)
                count += 1
                if max_per_model and count >= max_per_model:
                    break
        print(f"  {model_name}: {count}")
    df = pd.DataFrame(records)
    df["label"] = df["depth"].clip(upper=2)
    print(f"  Total: {len(df)}, labels: {df['label'].value_counts().sort_index().to_dict()}")
    return df


# -- LD-Score ----------------------------------------------

def build_trigram_data(texts, n=3):
    all_counts = []
    global_vocab = set()
    for text in texts:
        t = text.lower()
        counts = Counter(t[j:j+n] for j in range(len(t) - n + 1))
        all_counts.append(counts)
        global_vocab.update(counts.keys())
    vocab = sorted(global_vocab)
    ng2i = {ng: i for i, ng in enumerate(vocab)}
    V = len(vocab)
    print(f"  Trigram vocab: {V}")
    return all_counts, ng2i, V


def ld_scores_from_ref(all_counts, ref_indices, ng2i, V):
    ref_total = Counter()
    for i in ref_indices:
        ref_total.update(all_counts[i])
    total_ref = sum(ref_total.values())
    if total_ref == 0:
        return np.zeros(len(all_counts))
    ref_vec = np.zeros(V, dtype=np.float64)
    for ng, c in ref_total.items():
        if ng in ng2i:
            ref_vec[ng2i[ng]] = c / total_ref
    scores = np.empty(len(all_counts))
    for idx, counts in enumerate(all_counts):
        total = sum(counts.values())
        if total == 0:
            scores[idx] = 0.0
            continue
        vec = np.zeros(V, dtype=np.float64)
        for ng, c in counts.items():
            if ng in ng2i:
                vec[ng2i[ng]] = c / total
        js = jensenshannon(ref_vec, vec)
        scores[idx] = float(js) if not np.isnan(js) else 0.0
    return scores


def compute_ld_scores(texts, labels, n=3):
    trigram_data = build_trigram_data(texts, n)
    all_counts, ng2i, V = trigram_data
    ref_indices = [i for i, l in enumerate(labels) if l == 0]
    scores = ld_scores_from_ref(all_counts, ref_indices, ng2i, V)
    return scores.tolist(), trigram_data


# -- FastDetectGPT + avg log-prob --------------------------

def compute_fastdetectgpt_and_logprob(texts, model, tokenizer, device, bs=8):
    fdg_scores, lp_scores = [], []
    n = len(texts)
    for i in range(0, n, bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model(**enc).logits

        log_probs = F.log_softmax(logits[:, :-1], dim=-1)
        probs = torch.exp(log_probs)
        targets = enc["input_ids"][:, 1:]
        mask = enc["attention_mask"][:, 1:].bool()

        actual = log_probs.gather(2, targets.unsqueeze(-1)).squeeze(-1)
        expected = (probs * log_probs).sum(dim=-1)
        curv = actual - expected

        for j in range(len(batch)):
            m = mask[j]
            n_tok = m.sum().item()
            if n_tok < 2:
                fdg_scores.append(0.0)
                lp_scores.append(0.0)
                continue
            c = curv[j][m]
            mean_c = c.mean().item()
            std_c = c.std().item()
            fdg_scores.append(mean_c / (std_c + 1e-8) if std_c > 1e-8 else mean_c)
            lp_scores.append(actual[j][m].mean().item())

        done = min(i + bs, n)
        if (i // bs) % 200 == 0:
            print(f"    {done}/{n}")
    return fdg_scores, lp_scores


# -- Binoculars (FIXED: denominator uses actual_ids) -------

def compute_binoculars_scores(texts, observer, performer, tokenizer, device, bs=8):
    scores = []
    n = len(texts)
    for i in range(0, n, bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            obs_logits = observer(**enc).logits
            perf_logits = performer(**enc).logits

        shifted_obs = obs_logits[:, :-1].contiguous()
        shifted_perf = perf_logits[:, :-1].contiguous()
        shifted_ids = enc["input_ids"][:, 1:].contiguous()
        mask = enc["attention_mask"][:, 1:].float()
        B, T, V = shifted_obs.shape

        ppl_loss = F.cross_entropy(
            shifted_obs.view(-1, V), shifted_ids.view(-1), reduction="none"
        ).view(B, T)
        ppl = (ppl_loss * mask).sum(1) / mask.sum(1).clamp(min=1)

        ce_loss = F.cross_entropy(
            shifted_perf.view(-1, V), shifted_ids.view(-1), reduction="none"
        ).view(B, T)
        ce = (ce_loss * mask).sum(1) / mask.sum(1).clamp(min=1)

        bino = ppl / ce.clamp(min=1e-8)
        scores.extend(bino.cpu().float().tolist())

        done = min(i + bs, n)
        if (i // bs) % 200 == 0:
            print(f"    {done}/{n}")
    return scores


# -- Evaluation --------------------------------------------

def eval_cv(scores, labels, name, n_splits=5):
    X = np.array(scores).reshape(-1, 1)
    y = np.array(labels)
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    f1s, pcs = [], []
    for tr, te in skf.split(X, y):
        clf = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        f1s.append(f1_score(y[te], pred, average="macro"))
        pcs.append(f1_score(y[te], pred, average=None))
    rho, pval = spearmanr(scores, labels)
    return {
        "feature": name,
        "macro_f1_mean": round(float(np.mean(f1s)), 4),
        "macro_f1_std":  round(float(np.std(f1s)), 4),
        "per_class_f1":  [round(float(x), 4) for x in np.mean(pcs, axis=0)],
        "spearman_rho":  round(float(rho), 4),
        "spearman_pval": float(pval),
    }


def eval_cv_ld(trigram_data, labels, n_splits=5):
    all_counts, ng2i, V = trigram_data
    y = np.array(labels)
    indices = np.arange(len(y))
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    f1s, pcs = [], []
    for tr, te in skf.split(indices, y):
        ref_idx = tr[y[tr] == 0]
        scores = ld_scores_from_ref(all_counts, ref_idx, ng2i, V)
        X_tr = scores[tr].reshape(-1, 1)
        X_te = scores[te].reshape(-1, 1)
        clf = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X_tr, y[tr])
        pred = clf.predict(X_te)
        f1s.append(f1_score(y[te], pred, average="macro"))
        pcs.append(f1_score(y[te], pred, average=None))
    global_ref = np.where(y == 0)[0]
    global_scores = ld_scores_from_ref(all_counts, global_ref, ng2i, V)
    rho, pval = spearmanr(global_scores, y)
    return {
        "feature": "LD-Score",
        "macro_f1_mean": round(float(np.mean(f1s)), 4),
        "macro_f1_std":  round(float(np.std(f1s)), 4),
        "per_class_f1":  [round(float(x), 4) for x in np.mean(pcs, axis=0)],
        "spearman_rho":  round(float(rho), 4),
        "spearman_pval": float(pval),
    }


def eval_logo(scores, labels, model_names, name):
    X = np.array(scores).reshape(-1, 1)
    y = np.array(labels)
    models = np.array(model_names)
    unique = sorted(set(model_names))
    f1s = {}
    for hold in unique:
        tr, te = models != hold, models == hold
        clf = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        f1s[hold] = round(f1_score(y[te], pred, average="macro"), 4)
    vals = list(f1s.values())
    return {
        "logo_macro_f1_mean": round(float(np.mean(vals)), 4),
        "logo_macro_f1_std":  round(float(np.std(vals)), 4),
        "logo_per_model_f1":  f1s,
    }


def eval_logo_ld(trigram_data, labels, model_names):
    all_counts, ng2i, V = trigram_data
    y = np.array(labels)
    models = np.array(model_names)
    unique = sorted(set(model_names))
    f1s = {}
    for hold in unique:
        tr_mask = models != hold
        te_mask = models == hold
        tr_idx = np.where(tr_mask)[0]
        te_idx = np.where(te_mask)[0]
        ref_idx = tr_idx[y[tr_idx] == 0]
        scores = ld_scores_from_ref(all_counts, ref_idx, ng2i, V)
        X_tr = scores[tr_idx].reshape(-1, 1)
        X_te = scores[te_idx].reshape(-1, 1)
        clf = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X_tr, y[tr_idx])
        pred = clf.predict(X_te)
        f1s[hold] = round(f1_score(y[te_idx], pred, average="macro"), 4)
    vals = list(f1s.values())
    return {
        "logo_macro_f1_mean": round(float(np.mean(vals)), 4),
        "logo_macro_f1_std":  round(float(np.std(vals)), 4),
        "logo_per_model_f1":  f1s,
    }


def eval_seven_features():
    feat_cols = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                 "tail_decay", "ttr", "hapax_ratio"]
    df = pd.read_csv(DATA / "features_all_models.csv")
    df = df[df["model_name"].isin(MODEL_SOURCES.keys())]
    df["label"] = df["depth"].clip(upper=2)
    X, y = df[feat_cols].values, df["label"].values
    models = df["model_name"].values

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    f1s, pcs = [], []
    for tr, te in skf.split(X, y):
        clf = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        f1s.append(f1_score(y[te], pred, average="macro"))
        pcs.append(f1_score(y[te], pred, average=None))

    unique = sorted(set(models))
    logo_f1s = {}
    for hold in unique:
        tr, te = models != hold, models == hold
        clf = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        logo_f1s[hold] = round(f1_score(y[te], pred, average="macro"), 4)
    logo_vals = list(logo_f1s.values())

    return {
        "feature": "7-feature ensemble",
        "macro_f1_mean": round(float(np.mean(f1s)), 4),
        "macro_f1_std":  round(float(np.std(f1s)), 4),
        "per_class_f1":  [round(float(x), 4) for x in np.mean(pcs, axis=0)],
        "logo_macro_f1_mean": round(float(np.mean(logo_vals)), 4),
        "logo_macro_f1_std":  round(float(np.std(logo_vals)), 4),
        "logo_per_model_f1":  logo_f1s,
        "n_samples": len(df),
    }


# -- Bootstrap CI -----------------------------------------

def _xgb_logo_f1(X, y, models, unique, max_depth=3):
    f1s = []
    for hold in unique:
        tr = models != hold
        te = models == hold
        y_tr, y_te = y[tr], y[te]
        if len(np.unique(y_tr)) < 2 or len(y_te) == 0:
            continue
        clf = XGBClassifier(n_estimators=100, max_depth=max_depth, learning_rate=0.1,
                            objective="multi:softmax", num_class=3,
                            eval_metric="mlogloss", verbosity=0, random_state=42,
                            n_jobs=1)
        clf.fit(X[tr], y_tr)
        pred = clf.predict(X[te])
        f1s.append(f1_score(y_te, pred, average="macro", zero_division=0))
    return np.mean(f1s) if f1s else np.nan


def bootstrap_logo_ci(scores, labels, model_names, n_boot=N_BOOTSTRAP, seed=42, max_depth=3):
    rng = np.random.RandomState(seed)
    scores = np.array(scores)
    labels = np.array(labels)
    models = np.array(model_names)
    unique = sorted(set(model_names))
    gen_idx = {g: np.where(models == g)[0] for g in unique}

    boot_f1s, boot_rhos = [], []
    for _ in range(n_boot):
        bi = np.concatenate([rng.choice(gen_idx[g], size=len(gen_idx[g]), replace=True) for g in unique])
        b_s, b_l, b_m = scores[bi], labels[bi], models[bi]
        f1_val = _xgb_logo_f1(b_s.reshape(-1, 1), b_l, b_m, unique, max_depth)
        if not np.isnan(f1_val):
            boot_f1s.append(f1_val)
        if len(np.unique(b_l)) > 1:
            rho, _ = spearmanr(b_s, b_l)
            if not np.isnan(rho):
                boot_rhos.append(rho)

    f1_ci = np.percentile(boot_f1s, [2.5, 97.5]) if boot_f1s else [np.nan, np.nan]
    rho_ci = np.percentile(boot_rhos, [2.5, 97.5]) if boot_rhos else [np.nan, np.nan]
    return {
        "logo_f1_95ci": [round(float(f1_ci[0]), 4), round(float(f1_ci[1]), 4)],
        "spearman_rho_95ci": [round(float(rho_ci[0]), 4), round(float(rho_ci[1]), 4)],
    }


def bootstrap_logo_ci_multi(X, labels, model_names, n_boot=N_BOOTSTRAP, seed=42, max_depth=5):
    rng = np.random.RandomState(seed)
    labels = np.array(labels)
    models = np.array(model_names)
    unique = sorted(set(model_names))
    gen_idx = {g: np.where(models == g)[0] for g in unique}

    boot_f1s = []
    for _ in range(n_boot):
        bi = np.concatenate([rng.choice(gen_idx[g], size=len(gen_idx[g]), replace=True) for g in unique])
        f1_val = _xgb_logo_f1(X[bi], labels[bi], models[bi], unique, max_depth)
        if not np.isnan(f1_val):
            boot_f1s.append(f1_val)

    f1_ci = np.percentile(boot_f1s, [2.5, 97.5]) if boot_f1s else [np.nan, np.nan]
    return {"logo_f1_95ci": [round(float(f1_ci[0]), 4), round(float(f1_ci[1]), 4)]}


def bootstrap_paired_test(scores_a, scores_b, labels, model_names,
                           n_boot=N_BOOTSTRAP, seed=42, md_a=5, md_b=3,
                           multi_a=False, multi_b=False):
    rng = np.random.RandomState(seed)
    labels = np.array(labels)
    models = np.array(model_names)
    unique = sorted(set(model_names))
    gen_idx = {g: np.where(models == g)[0] for g in unique}
    X_a = scores_a if multi_a else np.array(scores_a).reshape(-1, 1)
    X_b = scores_b if multi_b else np.array(scores_b).reshape(-1, 1)

    diffs = []
    for _ in range(n_boot):
        bi = np.concatenate([rng.choice(gen_idx[g], size=len(gen_idx[g]), replace=True) for g in unique])
        b_l, b_m = labels[bi], models[bi]
        f1_a = _xgb_logo_f1(X_a[bi], b_l, b_m, unique, md_a)
        f1_b = _xgb_logo_f1(X_b[bi], b_l, b_m, unique, md_b)
        if not np.isnan(f1_a) and not np.isnan(f1_b):
            diffs.append(f1_a - f1_b)

    ci = np.percentile(diffs, [2.5, 97.5]) if diffs else [np.nan, np.nan]
    mean_diff = np.mean(diffs) if diffs else np.nan
    significant = bool(ci[0] > 0 or ci[1] < 0) if diffs else False
    return {
        "mean_diff": round(float(mean_diff), 4),
        "ci_95": [round(float(ci[0]), 4), round(float(ci[1]), 4)],
        "significant": significant,
    }


# -- Main --------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--device", default=DEVICE)
    args = ap.parse_args()
    device = args.device
    RESULTS.mkdir(exist_ok=True)

    max_pm = 20 if args.dry_run else None
    print("=" * 60)
    print("Ordinal Baseline Comparison" + (" [DRY RUN]" if args.dry_run else ""))
    print("=" * 60)

    print("\n[Load]")
    df = load_texts(max_per_model=max_pm)
    texts = df["text"].tolist()
    labels = df["label"].values
    depths = df["depth"].values
    model_names = df["model_name"].tolist()

    results = {"n_texts": len(texts), "dry_run": args.dry_run}
    all_scores = {}

    # 1. LD-Score
    print("\n[1/3] LD-Score")
    t0 = time.time()
    ld_global, trigram_data = compute_ld_scores(texts, labels)
    all_scores["ld_score"] = ld_global
    print(f"  {time.time()-t0:.1f}s")

    # 2. FastDetectGPT + log-prob
    print("\n[2/3] FastDetectGPT (pythia-410m)")
    t0 = time.time()
    performer = None
    try:
        scoring = "EleutherAI/pythia-410m"
        print(f"  Loading {scoring}...")
        tok = AutoTokenizer.from_pretrained(scoring, cache_dir=HF_CACHE)
        tok.pad_token = tok.eos_token
        mdl = AutoModelForCausalLM.from_pretrained(
            scoring, dtype=torch.float16, cache_dir=HF_CACHE
        ).to(device).eval()
        fdg, lp = compute_fastdetectgpt_and_logprob(texts, mdl, tok, device)
        all_scores["fastdetectgpt"] = fdg
        all_scores["avg_logprob"] = lp
        performer = mdl
        print(f"  {time.time()-t0:.1f}s")
    except Exception as e:
        print(f"  FAILED: {e}")
        import traceback; traceback.print_exc()

    # 3. Binoculars
    print("\n[3/3] Binoculars (pythia-160m x pythia-410m)")
    t0 = time.time()
    try:
        obs_name = "EleutherAI/pythia-160m"
        print(f"  Loading observer {obs_name}...")
        observer = AutoModelForCausalLM.from_pretrained(
            obs_name, dtype=torch.float16, cache_dir=HF_CACHE
        ).to(device).eval()
        if performer is None:
            tok = AutoTokenizer.from_pretrained("EleutherAI/pythia-410m", cache_dir=HF_CACHE)
            tok.pad_token = tok.eos_token
            performer = AutoModelForCausalLM.from_pretrained(
                "EleutherAI/pythia-410m", dtype=torch.float16, cache_dir=HF_CACHE
            ).to(device).eval()
        bino = compute_binoculars_scores(texts, observer, performer, tok, device)
        all_scores["binoculars"] = bino
        print(f"  {time.time()-t0:.1f}s")
        del observer
    except Exception as e:
        print(f"  FAILED: {e}")
        import traceback; traceback.print_exc()

    # Free GPU
    if performer is not None:
        del performer
    if "mdl" in locals():
        del mdl
    torch.cuda.empty_cache()

    # Evaluate
    print("\n[Eval]")
    det_keys = ["ld_score", "fastdetectgpt", "avg_logprob", "binoculars"]
    det_names = {"ld_score": "LD-Score", "fastdetectgpt": "FastDetectGPT",
                 "avg_logprob": "Avg-LogProb", "binoculars": "Binoculars"}

    for key in det_keys:
        sc = all_scores.get(key)
        if sc is None:
            results[key] = {"error": "computation failed"}
            continue
        name = det_names[key]
        if key == "ld_score":
            r = eval_cv_ld(trigram_data, labels)
            r.update(eval_logo_ld(trigram_data, labels, model_names))
            r_leaked = eval_cv(sc, labels, name)
            r_leaked.update(eval_logo(sc, labels, model_names, name))
            r["leaked_cv_f1"] = r_leaked["macro_f1_mean"]
            r["leaked_logo_f1"] = r_leaked["logo_macro_f1_mean"]
        else:
            r = eval_cv(sc, labels, name)
            r.update(eval_logo(sc, labels, model_names, name))
        rho_raw, _ = spearmanr(sc, depths)
        r["spearman_rho_raw_depth"] = round(float(rho_raw), 4)
        results[key] = r
        print(f"  {name:<15} F1={r['macro_f1_mean']:.4f}+/-{r['macro_f1_std']:.4f}"
              f"  LOGO={r['logo_macro_f1_mean']:.4f}  rho={r['spearman_rho']:.4f}")

    # 7-feature comparison
    try:
        results["seven_feature"] = eval_seven_features()
        sf = results["seven_feature"]
        print(f"  {'7-feat':<15} F1={sf['macro_f1_mean']:.4f}+/-{sf['macro_f1_std']:.4f}"
              f"  LOGO={sf['logo_macro_f1_mean']:.4f}")
    except Exception as e:
        print(f"  7-feature FAILED: {e}")
        results["seven_feature"] = {"error": str(e)}

    # Bootstrap CI
    print("\n[Bootstrap CI]")
    t0 = time.time()
    n_boot = 50 if args.dry_run else N_BOOTSTRAP

    for key in det_keys:
        sc = all_scores.get(key)
        if sc is None:
            continue
        name = det_names[key]
        print(f"  {name}...")
        ci = bootstrap_logo_ci(sc, labels, model_names, n_boot=n_boot)
        results[key].update(ci)
        print(f"    LOGO F1 95% CI: {ci['logo_f1_95ci']}")
        print(f"    rho 95% CI: {ci['spearman_rho_95ci']}")

    # 7-feature bootstrap
    sf = results.get("seven_feature", {})
    if "error" not in sf:
        print("  7-feature...")
        feat_cols = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                     "tail_decay", "ttr", "hapax_ratio"]
        df_feat = pd.read_csv(DATA / "features_all_models.csv")
        df_feat = df_feat[df_feat["model_name"].isin(MODEL_SOURCES.keys())]
        df_feat["label"] = df_feat["depth"].clip(upper=2)
        X_7 = df_feat[feat_cols].values
        y_7 = df_feat["label"].values
        m_7 = df_feat["model_name"].values
        ci_7 = bootstrap_logo_ci_multi(X_7, y_7, m_7, n_boot=n_boot)
        results["seven_feature"]["logo_f1_95ci"] = ci_7["logo_f1_95ci"]
        print(f"    LOGO F1 95% CI: {ci_7['logo_f1_95ci']}")

        # Paired test: 7-feature vs Avg-LogProb
        lp = all_scores.get("avg_logprob")
        if lp is not None and len(lp) == len(X_7):
            print("  Paired: 7-feature vs Avg-LogProb...")
            paired = bootstrap_paired_test(
                X_7, np.array(lp), y_7, m_7,
                n_boot=n_boot, md_a=5, md_b=3,
                multi_a=True, multi_b=False
            )
            results["paired_7feat_vs_avglogprob"] = paired
            print(f"    Diff: {paired['mean_diff']:.4f}, CI: {paired['ci_95']}, sig: {paired['significant']}")
        elif lp is not None:
            print(f"    SKIP paired: sample mismatch ({len(lp)} vs {len(X_7)})")

    print(f"  Bootstrap: {time.time()-t0:.1f}s")

    # Summary table
    print("\n" + "=" * 90)
    print(f"{'Detector':<20} {'CV F1':>8} {'LOGO F1':>8} {'LOGO 95% CI':>18} {'rho(3c)':>8} {'rho(depth)':>10}")
    print("-" * 90)
    for key in det_keys + ["seven_feature"]:
        r = results.get(key, {})
        if "error" in r:
            print(f"{key:<20} {'ERR':>8}")
            continue
        nm = r.get("feature", key)
        ci = r.get("logo_f1_95ci", ["-", "-"])
        ci_s = f"[{ci[0]}, {ci[1]}]" if isinstance(ci[0], float) else "[-,-]"
        print(f"{nm:<20} {r.get('macro_f1_mean',0):>8.4f} "
              f"{r.get('logo_macro_f1_mean',0):>8.4f} "
              f"{ci_s:>18} "
              f"{r.get('spearman_rho',0):>8.4f} "
              f"{r.get('spearman_rho_raw_depth', r.get('spearman_rho',0)):>10.4f}")

    # LD-Score leak comparison
    ld = results.get("ld_score", {})
    if "leaked_cv_f1" in ld:
        print(f"\nLD-Score leak fix: CV F1 {ld['leaked_cv_f1']:.4f} -> {ld['macro_f1_mean']:.4f}")
        print(f"                  LOGO F1 {ld['leaked_logo_f1']:.4f} -> {ld['logo_macro_f1_mean']:.4f}")

    # Paired test summary
    paired = results.get("paired_7feat_vs_avglogprob", {})
    if paired:
        print(f"\n7-feature vs Avg-LogProb paired bootstrap:")
        print(f"  Diff: {paired['mean_diff']:.4f} (95% CI: {paired['ci_95']})")
        print(f"  Significant: {paired['significant']}")

    # Save JSON
    out = RESULTS / "ordinal_baseline_results.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")

    # Save text report
    report_dir = ROOT / "artifacts" / "plan-015" / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "ordinal_baseline_results.txt"
    with open(report_path, "w") as f:
        f.write("=== Binoculars Verification ===\n")
        f.write("Conclusion: BUG\n")
        f.write("Evidence: compute_binoculars_scores() denominator used\n")
        f.write("  obs_argmax = shifted_obs.argmax(dim=-1)\n")
        f.write("  CE(performer_logits, obs_argmax) -- WRONG\n")
        f.write("Fix applied: CE(performer_logits, shifted_ids) -- standard Binoculars\n\n")

        f.write("=== Detector Results (LOGO F1 / Spearman rho) ===\n")
        hdr = f"{'Detector':<20} {'LOGO F1':>8} {'95% CI':>18} {'Spearman rho':>12} {'95% CI':>18}\n"
        f.write(hdr)
        f.write("-" * 80 + "\n")
        for key in det_keys + ["seven_feature"]:
            r = results.get(key, {})
            if "error" in r:
                continue
            nm = r.get("feature", key)
            ci_f1 = r.get("logo_f1_95ci", ["-", "-"])
            ci_rho = r.get("spearman_rho_95ci", ["-", "-"])
            ci_f1_s = f"[{ci_f1[0]}, {ci_f1[1]}]" if isinstance(ci_f1[0], float) else "[-,-]"
            ci_rho_s = f"[{ci_rho[0]}, {ci_rho[1]}]" if isinstance(ci_rho[0], float) else "[-,-]"
            rho_val = r.get("spearman_rho", 0)
            f.write(f"{nm:<20} {r.get('logo_macro_f1_mean',0):>8.4f} {ci_f1_s:>18} {rho_val:>12.4f} {ci_rho_s:>18}\n")
        f.write("\n")

        if paired:
            f.write("=== 7-feature vs Avg-LogProb Significance ===\n")
            f.write(f"Mean diff: {paired['mean_diff']:.4f} pp\n")
            f.write(f"95% CI: [{paired['ci_95'][0]}, {paired['ci_95'][1]}]\n")
            sig_txt = "Yes" if paired["significant"] else "No"
            cross_txt = "does not cross" if paired["significant"] else "crosses"
            f.write(f"Significant: {sig_txt} (CI {cross_txt} 0)\n\n")

        if "leaked_cv_f1" in ld:
            f.write("=== LD-Score Leak Fix Comparison ===\n")
            f.write(f"Before fix CV F1:   {ld['leaked_cv_f1']:.4f}\n")
            f.write(f"After fix CV F1:    {ld['macro_f1_mean']:.4f}\n")
            f.write(f"Before fix LOGO F1: {ld['leaked_logo_f1']:.4f}\n")
            f.write(f"After fix LOGO F1:  {ld['logo_macro_f1_mean']:.4f}\n")

    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
