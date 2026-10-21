#!/usr/bin/env python3
"""Inter-Annotator Agreement Analysis: Human vs GPT-4o labels."""

import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

BASE = "/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/data/human_annotation"

# ─── Load data ───
# Full file has llm_label; completed file has human_label
df_full = pd.read_csv(f"{BASE}/annotation_sheet_full.csv", quotechar='"', escapechar='\\')
df_comp = pd.read_csv(f"{BASE}/annotation_sheet_completed.csv", quotechar='"', escapechar='\\')

# Merge: take llm_label from full, human_label+confidence from completed
df = df_full[["msg_id", "backbone", "topology", "task_id", "round", "position", "sender", "llm_label"]].merge(
    df_comp[["msg_id", "human_label", "confidence", "notes"]],
    on="msg_id",
    how="inner",
)

# Clean labels
df["llm_label"] = df["llm_label"].astype(str).str.strip().str.lower()
df["human_label"] = df["human_label"].astype(str).str.strip().str.lower()

# Drop any rows with missing labels
df = df[(df["llm_label"] != "nan") & (df["human_label"] != "nan")].copy()

print(f"Total merged rows with both labels: {len(df)}")
print(f"Backbones: {sorted(df['backbone'].unique())}")
print()

# ─── 1. Distribution of labels ───
print("=" * 70)
print("1. LABEL DISTRIBUTIONS")
print("=" * 70)

all_labels = sorted(set(df["llm_label"].unique()) | set(df["human_label"].unique()))
print(f"\nAll unique labels: {all_labels}")

print("\nHuman labels:")
human_counts = df["human_label"].value_counts().sort_index()
for lab, cnt in human_counts.items():
    print(f"  {lab:30s}: {cnt:4d}  ({cnt/len(df)*100:5.1f}%)")

print("\nLLM (GPT-4o) labels:")
llm_counts = df["llm_label"].value_counts().sort_index()
for lab, cnt in llm_counts.items():
    print(f"  {lab:30s}: {cnt:4d}  ({cnt/len(df)*100:5.1f}%)")

# ─── 2. Overall Cohen's kappa (5-category) ───
print("\n" + "=" * 70)
print("2. OVERALL COHEN'S KAPPA (5-category)")
print("=" * 70)

kappa_overall = cohen_kappa_score(df["human_label"], df["llm_label"], labels=all_labels)
print(f"\nCohen's kappa (overall, 5-cat): {kappa_overall:.4f}")

# ─── 3. Per-backbone Cohen's kappa ───
print("\n" + "=" * 70)
print("3. PER-BACKBONE COHEN'S KAPPA (5-category)")
print("=" * 70)

backbones = sorted(df["backbone"].unique())
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        print(f"\n  {bb}: too few samples ({len(sub)})")
        continue
    k = cohen_kappa_score(sub["human_label"], sub["llm_label"], labels=all_labels)
    print(f"\n  {bb}: kappa = {k:.4f}  (n={len(sub)})")

# ─── 4. Confusion matrix ───
print("\n" + "=" * 70)
print("4. CONFUSION MATRIX (rows=human, cols=LLM)")
print("=" * 70)

cm = confusion_matrix(df["human_label"], df["llm_label"], labels=all_labels)
col_width = max(len(l) for l in all_labels) + 2
print(f"\n{'':20s}", end="")
for lab in all_labels:
    print(f"{lab:>{col_width}s}", end="")
print(f"{'TOTAL':>{col_width}s}")

for i, lab in enumerate(all_labels):
    print(f"{lab:20s}", end="")
    for j in range(len(all_labels)):
        print(f"{cm[i,j]:{col_width}d}", end="")
    print(f"{cm[i].sum():{col_width}d}")

print(f"{'TOTAL':20s}", end="")
for j in range(len(all_labels)):
    print(f"{cm[:,j].sum():{col_width}d}", end="")
print(f"{cm.sum():{col_width}d}")

# ─── 5. Binary ack/non-ack kappa (original labels) ───
print("\n" + "=" * 70)
print("5. BINARY ACK/NON-ACK KAPPA (original 5-category labels)")
print("=" * 70)

def binarize_orig(labels):
    return ["ack" if l == "acknowledgment" else "non-ack" for l in labels]

human_bin = binarize_orig(df["human_label"])
llm_bin = binarize_orig(df["llm_label"])

k_bin = cohen_kappa_score(human_bin, llm_bin)
print(f"\nBinary kappa (overall): {k_bin:.4f}")

cm_bin = confusion_matrix(human_bin, llm_bin, labels=["ack", "non-ack"])
print(f"\n  Binary confusion matrix (rows=human, cols=LLM):")
print(f"  {'':12s} {'ack':>8s} {'non-ack':>8s} {'TOTAL':>8s}")
print(f"  {'ack':12s} {cm_bin[0,0]:8d} {cm_bin[0,1]:8d} {cm_bin[0].sum():8d}")
print(f"  {'non-ack':12s} {cm_bin[1,0]:8d} {cm_bin[1,1]:8d} {cm_bin[1].sum():8d}")

print(f"\n  Per-backbone binary kappa (original):")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    h_b = binarize_orig(sub["human_label"])
    l_b = binarize_orig(sub["llm_label"])
    k = cohen_kappa_score(h_b, l_b)
    print(f"    {bb}: kappa = {k:.4f}  (n={len(sub)})")

# ─── 6. Merged taxonomy kappa (info_provision → ack) ───
print("\n" + "=" * 70)
print("6. MERGED TAXONOMY KAPPA (information_provision -> acknowledgment)")
print("=" * 70)

def merge_info_to_ack(labels):
    return [l.replace("information_provision", "acknowledgment") for l in labels]

human_merged = merge_info_to_ack(df["human_label"].tolist())
llm_merged = merge_info_to_ack(df["llm_label"].tolist())

merged_labels = sorted(set(human_merged) | set(llm_merged))
print(f"\nMerged label set: {merged_labels}")

k_merged = cohen_kappa_score(human_merged, llm_merged)
print(f"Merged taxonomy kappa (overall): {k_merged:.4f}")

print(f"\n  Per-backbone merged taxonomy kappa:")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    h_m = merge_info_to_ack(sub["human_label"].tolist())
    l_m = merge_info_to_ack(sub["llm_label"].tolist())
    k = cohen_kappa_score(h_m, l_m)
    print(f"    {bb}: kappa = {k:.4f}  (n={len(sub)})")

# Merged confusion matrix
cm_merged = confusion_matrix(human_merged, llm_merged, labels=merged_labels)
col_w2 = max(len(l) for l in merged_labels) + 2
print(f"\n  Merged confusion matrix (rows=human, cols=LLM):")
print(f"  {'':25s}", end="")
for lab in merged_labels:
    print(f"{lab:>{col_w2}s}", end="")
print(f"{'TOTAL':>{col_w2}s}")
for i, lab in enumerate(merged_labels):
    print(f"  {lab:25s}", end="")
    for j in range(len(merged_labels)):
        print(f"{cm_merged[i,j]:{col_w2}d}", end="")
    print(f"{cm_merged[i].sum():{col_w2}d}")

# ─── 7. Per-backbone binary ack/non-ack kappa with merged taxonomy ───
print("\n" + "=" * 70)
print("7. PER-BACKBONE BINARY ACK/NON-ACK KAPPA (merged taxonomy)")
print("=" * 70)

def binarize_any(labels):
    return ["ack" if l == "acknowledgment" else "non-ack" for l in labels]

human_merged_bin = binarize_any(human_merged)
llm_merged_bin = binarize_any(llm_merged)

k_merged_bin = cohen_kappa_score(human_merged_bin, llm_merged_bin)
print(f"\nMerged binary kappa (overall): {k_merged_bin:.4f}")

cm_mbin = confusion_matrix(human_merged_bin, llm_merged_bin, labels=["ack", "non-ack"])
print(f"\n  Merged binary confusion matrix (rows=human, cols=LLM):")
print(f"  {'':12s} {'ack':>8s} {'non-ack':>8s} {'TOTAL':>8s}")
print(f"  {'ack':12s} {cm_mbin[0,0]:8d} {cm_mbin[0,1]:8d} {cm_mbin[0].sum():8d}")
print(f"  {'non-ack':12s} {cm_mbin[1,0]:8d} {cm_mbin[1,1]:8d} {cm_mbin[1].sum():8d}")

print(f"\n  Per-backbone merged binary kappa:")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    h_m = merge_info_to_ack(sub["human_label"].tolist())
    l_m = merge_info_to_ack(sub["llm_label"].tolist())
    h_b = binarize_any(h_m)
    l_b = binarize_any(l_m)
    k = cohen_kappa_score(h_b, l_b)
    print(f"    {bb}: kappa = {k:.4f}  (n={len(sub)})")

# ─── 8. Agreement rate per backbone ───
print("\n" + "=" * 70)
print("8. AGREEMENT RATE (simple percent agreement)")
print("=" * 70)

agree_overall = (df["human_label"] == df["llm_label"]).mean()
print(f"\nOverall agreement (5-cat): {agree_overall:.4f} ({agree_overall*100:.1f}%)")

for bb in backbones:
    sub = df[df["backbone"] == bb]
    agree = (sub["human_label"] == sub["llm_label"]).mean()
    print(f"  {bb}: {agree:.4f} ({agree*100:.1f}%)  (n={len(sub)})")

print(f"\n  Merged taxonomy agreement:")
agree_merged_overall = np.mean([h == l for h, l in zip(human_merged, llm_merged)])
print(f"  Overall: {agree_merged_overall:.4f} ({agree_merged_overall*100:.1f}%)")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    h_m = merge_info_to_ack(sub["human_label"].tolist())
    l_m = merge_info_to_ack(sub["llm_label"].tolist())
    agree = np.mean([h == l for h, l in zip(h_m, l_m)])
    print(f"  {bb}: {agree:.4f} ({agree*100:.1f}%)  (n={len(sub)})")

print(f"\n  Binary agreement (original):")
agree_bin = np.mean([h == l for h, l in zip(human_bin, llm_bin)])
print(f"  Overall: {agree_bin:.4f} ({agree_bin*100:.1f}%)")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    h_b = binarize_orig(sub["human_label"])
    l_b = binarize_orig(sub["llm_label"])
    agree = np.mean([h == l for h, l in zip(h_b, l_b)])
    print(f"  {bb}: {agree:.4f} ({agree*100:.1f}%)  (n={len(sub)})")

print(f"\n  Binary agreement (merged taxonomy):")
agree_mbin = np.mean([h == l for h, l in zip(human_merged_bin, llm_merged_bin)])
print(f"  Overall: {agree_mbin:.4f} ({agree_mbin*100:.1f}%)")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    h_m = merge_info_to_ack(sub["human_label"].tolist())
    l_m = merge_info_to_ack(sub["llm_label"].tolist())
    h_b = binarize_any(h_m)
    l_b = binarize_any(l_m)
    agree = np.mean([h == l for h, l in zip(h_b, l_b)])
    print(f"  {bb}: {agree:.4f} ({agree*100:.1f}%)  (n={len(sub)})")

# ─── 9. Krippendorff's alpha ───
print("\n" + "=" * 70)
print("9. KRIPPENDORFF'S ALPHA")
print("=" * 70)

def krippendorff_alpha_nominal(data):
    """
    Compute Krippendorff's alpha for nominal data.
    data: list of lists, each inner list is one coder's labels (length = n_items).
    """
    n_coders = len(data)
    n_items = len(data[0])

    categories = set()
    for coder in data:
        for val in coder:
            if val is not None:
                categories.add(val)
    categories = sorted(categories)
    cat_idx = {c: i for i, c in enumerate(categories)}
    n_cats = len(categories)

    coincidence = np.zeros((n_cats, n_cats))

    for item in range(n_items):
        codes = []
        for coder in range(n_coders):
            if data[coder][item] is not None:
                codes.append(data[coder][item])
        m = len(codes)
        if m < 2:
            continue
        for i in range(m):
            for j in range(m):
                if i != j:
                    ci = cat_idx[codes[i]]
                    cj = cat_idx[codes[j]]
                    coincidence[ci, cj] += 1.0 / (m - 1)

    n_total = coincidence.sum()
    if n_total == 0:
        return float("nan")

    marginals = coincidence.sum(axis=1)
    D_o = 1.0 - np.trace(coincidence) / n_total
    D_e = 1.0 - np.sum(marginals * (marginals - 1)) / (n_total * (n_total - 1))

    if D_e == 0:
        return 1.0
    return 1.0 - D_o / D_e

# 5-category
coder1 = df["human_label"].tolist()
coder2 = df["llm_label"].tolist()
alpha_5cat = krippendorff_alpha_nominal([coder1, coder2])
print(f"\nKrippendorff's alpha (5-category, nominal):  {alpha_5cat:.4f}")

# Binary (original)
alpha_bin = krippendorff_alpha_nominal([human_bin, llm_bin])
print(f"Krippendorff's alpha (binary ack/non-ack):   {alpha_bin:.4f}")

# Merged taxonomy (4-cat)
alpha_merged = krippendorff_alpha_nominal([human_merged, llm_merged])
print(f"Krippendorff's alpha (merged 4-category):    {alpha_merged:.4f}")

# Merged binary
alpha_merged_bin = krippendorff_alpha_nominal([human_merged_bin, llm_merged_bin])
print(f"Krippendorff's alpha (merged binary):        {alpha_merged_bin:.4f}")

# Per-backbone alpha (5-cat)
print(f"\n  Per-backbone Krippendorff's alpha (5-category):")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    c1 = sub["human_label"].tolist()
    c2 = sub["llm_label"].tolist()
    a = krippendorff_alpha_nominal([c1, c2])
    print(f"    {bb}: alpha = {a:.4f}  (n={len(sub)})")

# Per-backbone alpha (merged 4-cat)
print(f"\n  Per-backbone Krippendorff's alpha (merged 4-category):")
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    c1 = merge_info_to_ack(sub["human_label"].tolist())
    c2 = merge_info_to_ack(sub["llm_label"].tolist())
    a = krippendorff_alpha_nominal([c1, c2])
    print(f"    {bb}: alpha = {a:.4f}  (n={len(sub)})")

# Try krippendorff package for cross-validation
try:
    import krippendorff as kripp
    all_labs = sorted(set(coder1 + coder2))
    lab2int = {l: i for i, l in enumerate(all_labs)}
    r1 = [lab2int[l] for l in coder1]
    r2 = [lab2int[l] for l in coder2]
    reliability_data = np.array([r1, r2])
    alpha_pkg = kripp.alpha(reliability_data=reliability_data, level_of_measurement="nominal")
    print(f"\n  [krippendorff package cross-check] alpha (5-cat): {alpha_pkg:.4f}")
except ImportError:
    print("\n  [krippendorff package not installed; using custom implementation]")

# ─── SUMMARY TABLE ───
print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print(f"\n{'Metric':<50s} {'Value':>10s}")
print("-" * 62)
print(f"{'N (annotated pairs)':<50s} {len(df):>10d}")
print(f"{'Overall agreement (5-cat)':<50s} {agree_overall*100:>9.1f}%")
print(f"{'Cohen kappa (5-cat)':<50s} {kappa_overall:>10.4f}")
print(f"{'Cohen kappa (binary ack/non-ack, original)':<50s} {k_bin:>10.4f}")
print(f"{'Cohen kappa (merged 4-cat)':<50s} {k_merged:>10.4f}")
print(f"{'Cohen kappa (merged binary ack/non-ack)':<50s} {k_merged_bin:>10.4f}")
print(f"{'Krippendorff alpha (5-cat)':<50s} {alpha_5cat:>10.4f}")
print(f"{'Krippendorff alpha (binary ack/non-ack)':<50s} {alpha_bin:>10.4f}")
print(f"{'Krippendorff alpha (merged 4-cat)':<50s} {alpha_merged:>10.4f}")
print(f"{'Krippendorff alpha (merged binary)':<50s} {alpha_merged_bin:>10.4f}")

print(f"\n{'Backbone':<12s} {'n':>5s} {'Agr5%':>7s} {'k5cat':>7s} {'kBin':>7s} {'kMrg':>7s} {'kMBin':>7s}")
print("-" * 58)
for bb in backbones:
    sub = df[df["backbone"] == bb]
    if len(sub) < 2:
        continue
    n = len(sub)
    ag = (sub["human_label"] == sub["llm_label"]).mean() * 100
    k5 = cohen_kappa_score(sub["human_label"], sub["llm_label"], labels=all_labels)

    h_b = binarize_orig(sub["human_label"])
    l_b = binarize_orig(sub["llm_label"])
    kb = cohen_kappa_score(h_b, l_b)

    h_m = merge_info_to_ack(sub["human_label"].tolist())
    l_m = merge_info_to_ack(sub["llm_label"].tolist())
    km = cohen_kappa_score(h_m, l_m)

    h_mb = binarize_any(h_m)
    l_mb = binarize_any(l_m)
    kmb = cohen_kappa_score(h_mb, l_mb)

    print(f"{bb:<12s} {n:>5d} {ag:>6.1f}% {k5:>7.4f} {kb:>7.4f} {km:>7.4f} {kmb:>7.4f}")

# ─── DISAGREEMENT ANALYSIS ───
print("\n" + "=" * 70)
print("DISAGREEMENT ANALYSIS")
print("=" * 70)

disagree = df[df["human_label"] != df["llm_label"]]
print(f"\nTotal disagreements (5-cat): {len(disagree)} / {len(df)} ({len(disagree)/len(df)*100:.1f}%)")

print("\nDisagreement patterns (human -> LLM):")
patterns = Counter(zip(disagree["human_label"], disagree["llm_label"]))
for (h, l), cnt in patterns.most_common():
    print(f"  {h:30s} -> {l:30s}: {cnt}")

print("\nDisagreements by backbone:")
for bb in backbones:
    sub_d = disagree[disagree["backbone"] == bb]
    sub_all = df[df["backbone"] == bb]
    print(f"  {bb}: {len(sub_d)} / {len(sub_all)} ({len(sub_d)/len(sub_all)*100:.1f}%)")

print("\nDisagreements AFTER merge (information_provision -> acknowledgment):")
merged_disagree = [(h, l) for h, l in zip(human_merged, llm_merged) if h != l]
print(f"Total: {len(merged_disagree)} / {len(df)} ({len(merged_disagree)/len(df)*100:.1f}%)")
patterns_merged = Counter(merged_disagree)
for (h, l), cnt in patterns_merged.most_common():
    print(f"  {h:30s} -> {l:30s}: {cnt}")

# ─── CONFIDENCE ANALYSIS ───
print("\n" + "=" * 70)
print("CONFIDENCE ANALYSIS")
print("=" * 70)

df["confidence_num"] = pd.to_numeric(df["confidence"], errors="coerce")
conf_data = df.dropna(subset=["confidence_num"])
if len(conf_data) > 0:
    conf_data = conf_data.copy()
    conf_data["agree"] = conf_data["human_label"] == conf_data["llm_label"]
    print(f"\nN with confidence: {len(conf_data)}")
    print(f"Mean confidence: {conf_data['confidence_num'].mean():.2f}")
    print(f"Confidence distribution: {dict(conf_data['confidence_num'].value_counts().sort_index())}")
    n_agree = conf_data['agree'].sum()
    n_disagree = (~conf_data['agree']).sum()
    print(f"Confidence when agree:    {conf_data[conf_data['agree']]['confidence_num'].mean():.2f} (n={n_agree})")
    print(f"Confidence when disagree: {conf_data[~conf_data['agree']]['confidence_num'].mean():.2f} (n={n_disagree})")

    # Kappa stratified by confidence
    print("\n  Kappa by confidence level:")
    for conf_val in sorted(conf_data["confidence_num"].unique()):
        sub_c = conf_data[conf_data["confidence_num"] == conf_val]
        if len(sub_c) >= 2 and len(set(sub_c["human_label"])) > 1:
            k_c = cohen_kappa_score(sub_c["human_label"], sub_c["llm_label"])
            agree_c = (sub_c["human_label"] == sub_c["llm_label"]).mean()
            print(f"    confidence={int(conf_val)}: kappa={k_c:.4f}, agreement={agree_c*100:.1f}% (n={len(sub_c)})")
        else:
            agree_c = (sub_c["human_label"] == sub_c["llm_label"]).mean()
            print(f"    confidence={int(conf_val)}: agreement={agree_c*100:.1f}% (n={len(sub_c)}, too few categories for kappa)")
else:
    print("\nNo confidence data available.")

print("\n[Analysis complete]")
