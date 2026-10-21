#!/usr/bin/env python3
"""Three-annotator Inter-Annotator Agreement Analysis."""

import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score
from statsmodels.stats.inter_rater import fleiss_kappa
from collections import Counter

BASE = "/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/data/human_annotation"

df1 = pd.read_csv(f"{BASE}/annotation_sheet_completed.csv", quotechar='"', escapechar='\\')
df2 = pd.read_csv(f"{BASE}/annotation_sheet_completed2.csv", quotechar='"', escapechar='\\')
df3 = pd.read_csv(f"{BASE}/annotation_sheet_completed3.csv")

for df in [df1, df2, df3]:
    df["human_label"] = df["human_label"].str.strip().str.lower()

common_ids = sorted(set(df1["msg_id"]) & set(df2["msg_id"]) & set(df3["msg_id"]))
N = len(common_ids)

h1 = df1.set_index("msg_id").loc[common_ids, "human_label"].values
h2 = df2.set_index("msg_id").loc[common_ids, "human_label"].values
h3 = df3.set_index("msg_id").loc[common_ids, "human_label"].values

all_cats = sorted(set(h1) | set(h2) | set(h3))
cat2idx = {c: i for i, c in enumerate(all_cats)}

# Fleiss' kappa (3 human raters)
matrix = np.zeros((N, len(all_cats)), dtype=int)
for i in range(N):
    for label in [h1[i], h2[i], h3[i]]:
        matrix[i, cat2idx[label]] += 1

fk = fleiss_kappa(matrix)
print(f"3-human Fleiss kappa (5-cat, N={N}): {fk:.4f}")

# Pairwise Cohen's kappa
k12 = cohen_kappa_score(h1, h2)
k13 = cohen_kappa_score(h1, h3)
k23 = cohen_kappa_score(h2, h3)
print(f"Pairwise: A1-A2={k12:.4f}, A1-A3={k13:.4f}, A2-A3={k23:.4f}")

# Agreement patterns
full_agree = sum(1 for i in range(N) if h1[i] == h2[i] == h3[i])
two_agree = sum(1 for i in range(N) if len(set([h1[i], h2[i], h3[i]])) == 2)
print(f"Unanimous: {full_agree}/{N} ({full_agree/N*100:.1f}%)")
print(f"Majority: {two_agree}/{N} ({two_agree/N*100:.1f}%)")

# 2-annotator full dataset
d1_full = df1.set_index("msg_id")["human_label"]
d2_full = df2.set_index("msg_id")["human_label"]
common_full = sorted(set(d1_full.index) & set(d2_full.index))
k_full = cohen_kappa_score(d1_full[common_full], d2_full[common_full])
print(f"\n2-annotator Cohen kappa (full N={len(common_full)}): {k_full:.4f}")
