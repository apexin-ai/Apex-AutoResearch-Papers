#!/usr/bin/env python3
"""A2: Confidence-Margin Prediction Framework.
Logistic regression predicting helped/hurt from pure-model confidence margin.
Within-arch 5-fold CV AUC + cross-arch leave-one-architecture-out transfer AUC.
"""
import json, os, sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

BASE = "/root/entrainment_gated_ft/lm_eval_clean"
OUT_DIR = "/root/entrainment_gated_ft/results/a2_prediction_framework"
os.makedirs(OUT_DIR, exist_ok=True)

ARCHS = ["GDN", "RetNet", "HGRN2"]
BENCHMARKS = ["lambada", "hellaswag", "arc_easy", "piqa"]
MODEL_NAMES = {"GDN": "GatedDeltaNet", "RetNet": "RetNet", "HGRN2": "HGRN2"}
ACC_FIELDS = {"lambada": "acc", "hellaswag": "acc_norm", "arc_easy": "acc", "piqa": "acc"}
JSONL_NAMES = {
    "lambada": "lambada_openai.jsonl",
    "hellaswag": "hellaswag.jsonl",
    "arc_easy": "arc_easy.jsonl",
    "piqa": "piqa.jsonl",
}


def get_sample_path(benchmark, arch, variant):
    if benchmark == "lambada":
        if variant == "pure":
            return os.path.join(BASE, "exp007", "1.3b", f"{arch}-pure", "samples", "lambada_openai.jsonl")
        else:
            if arch == "GDN":
                return os.path.join(BASE, "1.3b", "GDN-h3-1-logsamples", "samples", "lambada_openai.jsonl")
            else:
                return os.path.join(BASE, "exp007", "1.3b", f"{arch}-h3-1", "samples", "lambada_openai.jsonl")
    else:
        mn = MODEL_NAMES[arch]
        if variant == "pure":
            dn = f"1.3B-100B-{mn}-pure"
        else:
            dn = f"1.3B-100B-{mn}-hybrid-3-1"
        return os.path.join(BASE, benchmark, dn, "samples", JSONL_NAMES[benchmark])


def load_samples(path):
    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))
    return samples


def extract_features(samples, benchmark):
    acc_field = ACC_FIELDS[benchmark]
    doc_ids, margins, accs = [], [], []
    for s in samples:
        doc_ids.append(s["doc_id"])
        accs.append(int(s[acc_field]))
        fr = s["filtered_resps"]
        if benchmark == "lambada":
            ll = fr[0][0] if isinstance(fr[0], (list, tuple)) else fr[0]
            margins.append(abs(float(ll)))
        else:
            gold = int(s["target"])
            ll = fr[gold][0] if isinstance(fr[gold], (list, tuple)) else fr[gold]
            margins.append(abs(float(ll)))
    return np.array(doc_ids), np.array(margins), np.array(accs)


def run_cv_auc(X, y, n_splits=5):
    if len(np.unique(y)) < 2:
        return np.nan, np.nan, 0
    n_pos, n_neg = int(y.sum()), int(len(y) - y.sum())
    if min(n_pos, n_neg) < n_splits:
        n_splits = max(2, min(n_pos, n_neg))
    pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, solver="lbfgs"))
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    aucs = cross_val_score(pipe, X, y, cv=skf, scoring="roc_auc")
    return float(aucs.mean()), float(aucs.std()), n_splits


def run_transfer_auc(X_train, y_train, X_test, y_test):
    if len(np.unique(y_train)) < 2 or len(np.unique(y_test)) < 2:
        return np.nan
    pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, solver="lbfgs"))
    pipe.fit(X_train, y_train)
    y_prob = pipe.predict_proba(X_test)[:, 1]
    return float(roc_auc_score(y_test, y_prob))


# ======== Main ========
results = {
    "analysis": "a2_confidence_margin_prediction",
    "date": "2026-05-22",
    "method": {
        "model": "LogisticRegression (sklearn, L2, lbfgs)",
        "feature": "abs(target_loglikelihood) from pure model",
        "within_arch_cv": "stratified 5-fold",
        "cross_arch_transfer": "leave-one-architecture-out (train on 2, test on 1)",
        "hybrid_config": "h3-1 (25% attention) for all architectures",
        "note": "Helped population = pure-wrong examples; Hurt population = pure-correct examples",
    },
    "within_arch": {},
    "cross_arch_transfer": {},
    "summary": {},
}

benchmark_data = {}

for bench in BENCHMARKS:
    print(f"\n{'='*60}")
    print(f"Benchmark: {bench}")
    print(f"{'='*60}")
    results["within_arch"][bench] = {}
    benchmark_data[bench] = {}

    for arch in ARCHS:
        pure_path = get_sample_path(bench, arch, "pure")
        hyb_path = get_sample_path(bench, arch, "h3-1")

        if not os.path.exists(pure_path):
            print(f"  {arch}: MISSING pure {pure_path}")
            continue
        if not os.path.exists(hyb_path):
            print(f"  {arch}: MISSING hybrid {hyb_path}")
            continue

        pure_ids, pure_margins, pure_accs = extract_features(load_samples(pure_path), bench)
        hyb_ids, _, hyb_accs = extract_features(load_samples(hyb_path), bench)
        assert np.array_equal(pure_ids, hyb_ids), f"doc_id mismatch {arch}/{bench}"

        helped = (pure_accs == 0) & (hyb_accs == 1)
        hurt = (pure_accs == 1) & (hyb_accs == 0)
        n_h, n_u = int(helped.sum()), int(hurt.sum())
        n_sr = int(((pure_accs == 1) & (hyb_accs == 1)).sum())
        n_sw = int(((pure_accs == 0) & (hyb_accs == 0)).sum())

        pw = pure_accs == 0
        X_helped = pure_margins[pw].reshape(-1, 1)
        y_helped = helped[pw].astype(int)
        h_auc, h_std, h_folds = run_cv_auc(X_helped, y_helped)

        pr = pure_accs == 1
        X_hurt = pure_margins[pr].reshape(-1, 1)
        y_hurt = hurt[pr].astype(int)
        u_auc, u_std, u_folds = run_cv_auc(X_hurt, y_hurt)

        print(f"  {arch}: helped={n_h} hurt={n_u} | helped AUC={h_auc:.4f}+/-{h_std:.4f} hurt AUC={u_auc:.4f}+/-{u_std:.4f}")

        results["within_arch"][bench][arch] = {
            "n_helped": n_h, "n_hurt": n_u, "n_stayed_right": n_sr, "n_stayed_wrong": n_sw,
            "helped_prediction": {
                "population": int(pw.sum()), "auc_mean": round(h_auc, 4), "auc_std": round(h_std, 4), "cv_folds": h_folds,
            },
            "hurt_prediction": {
                "population": int(pr.sum()), "auc_mean": round(u_auc, 4), "auc_std": round(u_std, 4), "cv_folds": u_folds,
            },
        }
        benchmark_data[bench][arch] = {"X_helped": X_helped, "y_helped": y_helped, "X_hurt": X_hurt, "y_hurt": y_hurt}

# ======== Cross-arch transfer ========
print(f"\n\n{'='*60}")
print("Cross-Architecture Transfer")
print(f"{'='*60}")

for bench in BENCHMARKS:
    results["cross_arch_transfer"][bench] = {}
    avail = [a for a in ARCHS if a in benchmark_data.get(bench, {})]
    if len(avail) < 2:
        continue

    for target in avail:
        sources = [a for a in avail if a != target]
        results["cross_arch_transfer"][bench][target] = {}

        for tt in ["helped", "hurt"]:
            Xk, yk = f"X_{tt}", f"y_{tt}"
            X_tr = np.vstack([benchmark_data[bench][a][Xk] for a in sources])
            y_tr = np.concatenate([benchmark_data[bench][a][yk] for a in sources])
            X_te = benchmark_data[bench][target][Xk]
            y_te = benchmark_data[bench][target][yk]
            t_auc = run_transfer_auc(X_tr, y_tr, X_te, y_te)
            results["cross_arch_transfer"][bench][target][f"{tt}_transfer_auc"] = round(t_auc, 4) if not np.isnan(t_auc) else None

        ha = results["cross_arch_transfer"][bench][target].get("helped_transfer_auc")
        ua = results["cross_arch_transfer"][bench][target].get("hurt_transfer_auc")
        print(f"  {bench} leave-{target}-out: helped={ha} hurt={ua}")

# ======== Summary ========
w_h, w_u, t_h, t_u = [], [], [], []
for bench in BENCHMARKS:
    for arch in ARCHS:
        w = results["within_arch"].get(bench, {}).get(arch, {})
        if w:
            v = w["helped_prediction"]["auc_mean"]
            if v is not None and not np.isnan(v): w_h.append(v)
            v = w["hurt_prediction"]["auc_mean"]
            if v is not None and not np.isnan(v): w_u.append(v)
        t = results["cross_arch_transfer"].get(bench, {}).get(arch, {})
        if t:
            v = t.get("helped_transfer_auc")
            if v is not None: t_h.append(v)
            v = t.get("hurt_transfer_auc")
            if v is not None: t_u.append(v)

results["summary"] = {
    "within_arch_helped": {"mean": round(float(np.mean(w_h)), 4), "std": round(float(np.std(w_h)), 4), "n": len(w_h)},
    "within_arch_hurt": {"mean": round(float(np.mean(w_u)), 4), "std": round(float(np.std(w_u)), 4), "n": len(w_u)},
    "transfer_helped": {"mean": round(float(np.mean(t_h)), 4), "std": round(float(np.std(t_h)), 4), "n": len(t_h)},
    "transfer_hurt": {"mean": round(float(np.mean(t_u)), 4), "std": round(float(np.std(t_u)), 4), "n": len(t_u)},
    "specificity_delta": {
        "helped": round(float(np.mean(w_h) - np.mean(t_h)), 4) if w_h and t_h else None,
        "hurt": round(float(np.mean(w_u) - np.mean(t_u)), 4) if w_u and t_u else None,
        "interpretation": "positive = within > transfer = architecture-specific component",
    },
}

# Save JSON
json_path = os.path.join(OUT_DIR, "confidence_margin_prediction.json")
with open(json_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {json_path}")

# ======== LaTeX table ========
BL = {"lambada": "LAMBADA", "hellaswag": "HellaSwag", "arc_easy": "ARC-Easy", "piqa": "PIQA"}
lines = []
lines.append(r"\begin{table}[t]")
lines.append(r"\centering")
lines.append(r"\small")
lines.append(r"\caption{Confidence-margin logistic regression: within-architecture (5-fold CV) vs.\ cross-architecture (leave-one-out) AUC-ROC. Baseline (random) = 0.50.}")
lines.append(r"\label{tab:prediction_auc}")
lines.append(r"\begin{tabular}{llcccccc}")
lines.append(r"\toprule")
lines.append(r" & & \multicolumn{2}{c}{GDN} & \multicolumn{2}{c}{RetNet} & \multicolumn{2}{c}{HGRN2} \\")
lines.append(r"\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}")
lines.append(r"Benchmark & Type & Within & Transfer & Within & Transfer & Within & Transfer \\")
lines.append(r"\midrule")

for bench in BENCHMARKS:
    for tt, label in [("helped", "Helped"), ("hurt", "Hurt")]:
        row = f"{BL[bench]} & {label}"
        for arch in ARCHS:
            w = results["within_arch"].get(bench, {}).get(arch, {})
            t = results["cross_arch_transfer"].get(bench, {}).get(arch, {})
            wa = w.get(f"{tt}_prediction", {}).get("auc_mean") if w else None
            ta = t.get(f"{tt}_transfer_auc") if t else None
            ws = f"{wa:.2f}" if wa is not None and not np.isnan(wa) else "--"
            ts = f"{ta:.2f}" if ta is not None else "--"
            row += f" & {ws} & {ts}"
        row += r" \\"
        lines.append(row)
    if bench != BENCHMARKS[-1]:
        lines.append(r"\addlinespace")

lines.append(r"\midrule")
for tt, label in [("helped", r"\textbf{Mean} Helped"), ("hurt", r"\textbf{Mean} Hurt")]:
    row = f" & {label}"
    for arch in ARCHS:
        wv, tv = [], []
        for bench in BENCHMARKS:
            w = results["within_arch"].get(bench, {}).get(arch, {})
            t = results["cross_arch_transfer"].get(bench, {}).get(arch, {})
            wa = w.get(f"{tt}_prediction", {}).get("auc_mean") if w else None
            ta = t.get(f"{tt}_transfer_auc") if t else None
            if wa is not None and not np.isnan(wa): wv.append(wa)
            if ta is not None: tv.append(ta)
        wm = f"{np.mean(wv):.2f}" if wv else "--"
        tm = f"{np.mean(tv):.2f}" if tv else "--"
        row += f" & {wm} & {tm}"
    row += r" \\"
    lines.append(row)

lines.append(r"\bottomrule")
lines.append(r"\end{tabular}")
lines.append(r"\end{table}")

tex_path = os.path.join(OUT_DIR, "prediction_summary_table.tex")
with open(tex_path, "w") as f:
    f.write("\n".join(lines))
print(f"Saved: {tex_path}")

# Print summary
s = results["summary"]
print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
print(f"Within-arch helped AUC: {s['within_arch_helped']['mean']:.4f} +/- {s['within_arch_helped']['std']:.4f} (n={s['within_arch_helped']['n']})")
print(f"Within-arch hurt AUC:   {s['within_arch_hurt']['mean']:.4f} +/- {s['within_arch_hurt']['std']:.4f} (n={s['within_arch_hurt']['n']})")
print(f"Transfer helped AUC:    {s['transfer_helped']['mean']:.4f} +/- {s['transfer_helped']['std']:.4f} (n={s['transfer_helped']['n']})")
print(f"Transfer hurt AUC:      {s['transfer_hurt']['mean']:.4f} +/- {s['transfer_hurt']['std']:.4f} (n={s['transfer_hurt']['n']})")
print(f"Specificity delta: helped={s['specificity_delta']['helped']}, hurt={s['specificity_delta']['hurt']}")
