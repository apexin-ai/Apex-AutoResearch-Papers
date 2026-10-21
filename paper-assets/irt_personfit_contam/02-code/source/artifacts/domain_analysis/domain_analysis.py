"""MMLU Domain-Specific lz* Analysis for 12-model Case Study."""

import sys
sys.path.insert(0, "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/src")

import numpy as np
import pandas as pd
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from person_fit import prob_4pl, compute_lz_star

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
OUT = f"{BASE}/artifacts/domain_analysis"

MODEL_NAMES = [
    "360GPT2-Pro", "DeepSeek-V3", "Doubao-pro", "Gemini-1.5",
    "Gemma-2B-it", "Hunyuan-Turbo", "Mistral-7B-Instruct-v0.1",
    "Moonshot-v1", "Qwen-Plus", "Qwen2.5-3B-Instruct",
    "Vicuna-7B-v1.3", "Yi-Lightning"
]

CATEGORY_MAP = {
    "STEM": [
        "abstract_algebra", "anatomy", "astronomy", "clinical_knowledge",
        "college_biology", "college_chemistry", "college_computer_science",
        "college_mathematics", "college_physics", "computer_security",
        "conceptual_physics", "electrical_engineering", "elementary_mathematics",
        "high_school_biology", "high_school_chemistry", "high_school_computer_science",
        "high_school_mathematics", "high_school_physics", "high_school_statistics",
        "machine_learning", "medical_genetics", "college_medicine",
        "professional_medicine", "virology", "nutrition", "human_aging"
    ],
    "Humanities": [
        "formal_logic", "high_school_european_history", "high_school_us_history",
        "high_school_world_history", "international_law", "jurisprudence",
        "logical_fallacies", "moral_disputes", "moral_scenarios", "philosophy",
        "prehistory", "world_religions"
    ],
    "Social Sciences": [
        "econometrics", "high_school_geography", "high_school_government_and_politics",
        "high_school_macroeconomics", "high_school_microeconomics",
        "high_school_psychology", "human_sexuality", "professional_law",
        "professional_psychology", "public_relations", "security_studies",
        "sociology", "us_foreign_policy"
    ],
    "Other": [
        "business_ethics", "global_facts", "management", "marketing",
        "miscellaneous", "professional_accounting"
    ]
}

SUBJECT_TO_CAT = {}
for cat, subjects in CATEGORY_MAP.items():
    for s in subjects:
        SUBJECT_TO_CAT[s] = cat

# ── Step 1: Build item-subject mapping ──
print("Step 1: Building MMLU subject mapping...")

from datasets import load_dataset
ds = load_dataset("cais/mmlu", "all", split="test")

subjects_raw = ds["subject"]
subject_list_sorted = sorted(set(subjects_raw))
print(f"  Unique subjects: {len(subject_list_sorted)}")
print(f"  Total items in dataset: {len(ds)}")

# Build per-subject indices in the dataset order
# The PSN-IRT data is arranged by subject alphabetical order
# We need to sort items by subject to match
subject_item_counts = {}
for s in subject_list_sorted:
    count = sum(1 for x in subjects_raw if x == s)
    subject_item_counts[s] = count

total_items = sum(subject_item_counts.values())
print(f"  Sum of per-subject counts: {total_items}")
assert total_items == 14042, f"Expected 14042, got {total_items}"

# Build cumulative offsets (items in PSN-IRT MMLU are sorted by subject alphabetically)
subject_offsets = {}
offset = 0
for s in subject_list_sorted:
    n = subject_item_counts[s]
    subject_offsets[s] = (offset, offset + n)
    offset += n

print(f"  Subject offsets built. Total: {offset}")

# ── Step 2: Load data ──
print("Step 2: Loading data...")

responses = np.loadtxt(f"{BASE}/artifacts/psn_irt_phase_b/combine.csv", delimiter=",", dtype=np.float64).astype(np.int8)
print(f"  Response matrix: {responses.shape}")

mmlu_responses = responses[:, 27029:41071]
print(f"  MMLU responses: {mmlu_responses.shape}")
assert mmlu_responses.shape[1] == 14042

params = pd.read_csv(f"{BASE}/artifacts/psn_irt_params/mmlu_params.csv")
a = params["a_discrimination"].values
b = params["b_difficulty"].values
c = params["c_guessing"].values
d = params["d_feasibility"].values
print(f"  IRT params: {len(a)} items")

abilities = pd.read_csv(f"{BASE}/artifacts/psn_irt_phase_b/student_abilities.csv")
thetas = abilities["ability"].values
print(f"  Thetas: {thetas}")

# ── Step 3: Per-subject lz* and accuracy ──
print("Step 3: Computing per-subject lz* and accuracy...")

n_models = 12
n_subjects = len(subject_list_sorted)

lz_matrix = np.full((n_models, n_subjects), np.nan)
acc_matrix = np.full((n_models, n_subjects), np.nan)

for j, subj in enumerate(subject_list_sorted):
    start, end = subject_offsets[subj]
    resp_s = mmlu_responses[:, start:end]
    a_s, b_s, c_s, d_s = a[start:end], b[start:end], c[start:end], d[start:end]

    for i in range(n_models):
        acc_matrix[i, j] = resp_s[i].mean()
        lz_matrix[i, j] = compute_lz_star(resp_s[i], thetas[i], a_s, b_s, c_s, d_s)

print("  Done.")

# ── Step 4: Per-category lz* and accuracy ──
print("Step 4: Computing per-category lz* and accuracy...")

categories = ["STEM", "Humanities", "Social Sciences", "Other"]
n_cats = len(categories)

lz_cat_matrix = np.full((n_models, n_cats), np.nan)
acc_cat_matrix = np.full((n_models, n_cats), np.nan)

for k, cat in enumerate(categories):
    cat_subjects = CATEGORY_MAP[cat]
    indices = []
    for s in cat_subjects:
        if s in subject_offsets:
            start, end = subject_offsets[s]
            indices.extend(range(start, end))
    indices = sorted(indices)

    resp_c = mmlu_responses[:, indices]
    a_c, b_c, c_c, d_c = a[indices], b[indices], c[indices], d[indices]

    for i in range(n_models):
        acc_cat_matrix[i, k] = resp_c[i].mean()
        lz_cat_matrix[i, k] = compute_lz_star(resp_c[i], thetas[i], a_c, b_c, c_c, d_c)

print("  Done.")

# ── Step 5: Gemini-1.5 deep analysis ──
print("Step 5: Gemini-1.5 analysis...")
gemini_idx = 3
gemini_mmlu_acc = mmlu_responses[gemini_idx].mean()
gemini_mmlu_correct = mmlu_responses[gemini_idx].sum()
gemini_mmlu_total = mmlu_responses.shape[1]
print(f"  Gemini-1.5 MMLU accuracy: {gemini_mmlu_acc:.4f} ({gemini_mmlu_correct}/{gemini_mmlu_total})")

# Subjects where Gemini got errors
gemini_error_subjects = []
for j, subj in enumerate(subject_list_sorted):
    start, end = subject_offsets[subj]
    subj_acc = mmlu_responses[gemini_idx, start:end].mean()
    n_items = end - start
    n_correct = mmlu_responses[gemini_idx, start:end].sum()
    n_wrong = n_items - n_correct
    if n_wrong > 0:
        gemini_error_subjects.append({
            "subject": subj,
            "accuracy": float(subj_acc),
            "n_items": int(n_items),
            "n_correct": int(n_correct),
            "n_wrong": int(n_wrong),
            "lz_star": float(lz_matrix[gemini_idx, j])
        })

print(f"  Subjects with errors: {len(gemini_error_subjects)}")
for es in sorted(gemini_error_subjects, key=lambda x: x["n_wrong"], reverse=True)[:10]:
    print(f"    {es['subject']}: {es['n_correct']}/{es['n_items']} ({es['accuracy']:.3f}), lz*={es['lz_star']:.2f}")

# ── Step 6: Save matrices ──
print("Step 6: Saving CSV outputs...")

df_lz = pd.DataFrame(lz_matrix, index=MODEL_NAMES, columns=subject_list_sorted)
df_lz.to_csv(f"{OUT}/subject_lz_matrix.csv")

df_acc = pd.DataFrame(acc_matrix, index=MODEL_NAMES, columns=subject_list_sorted)
df_acc.to_csv(f"{OUT}/subject_accuracy_matrix.csv")

df_lz_cat = pd.DataFrame(lz_cat_matrix, index=MODEL_NAMES, columns=categories)
df_lz_cat.to_csv(f"{OUT}/category_lz_matrix.csv")

df_acc_cat = pd.DataFrame(acc_cat_matrix, index=MODEL_NAMES, columns=categories)
df_acc_cat.to_csv(f"{OUT}/category_accuracy_matrix.csv")

# ── Step 7: Heatmaps ──
print("Step 7: Generating heatmaps...")

# --- Main heatmap: models × subjects lz* ---
fig, ax = plt.subplots(figsize=(24, 8))
cmap = plt.cm.RdYlBu_r
norm = mcolors.TwoSlopeNorm(vmin=np.nanmin(lz_matrix), vcenter=0, vmax=np.nanmax(lz_matrix))

im = ax.imshow(lz_matrix, aspect="auto", cmap=cmap, norm=norm)
ax.set_xticks(range(n_subjects))
short_names = [s.replace("high_school_", "hs_").replace("college_", "c_").replace("professional_", "pr_") for s in subject_list_sorted]
ax.set_xticklabels(short_names, rotation=90, fontsize=6)
ax.set_yticks(range(n_models))
ax.set_yticklabels(MODEL_NAMES, fontsize=8)
ax.set_title("MMLU Per-Subject $lz^*$ (12 Models × 57 Subjects)", fontsize=14)
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("$lz^*$", fontsize=12)

# Add category boundaries
prev_cat = None
for j, subj in enumerate(subject_list_sorted):
    cat = SUBJECT_TO_CAT.get(subj, "Other")
    if cat != prev_cat and prev_cat is not None:
        ax.axvline(x=j - 0.5, color="black", linewidth=1, linestyle="--")
    prev_cat = cat

plt.tight_layout()
plt.savefig(f"{OUT}/domain_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()

# --- Category-level heatmap ---
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(lz_cat_matrix, aspect="auto", cmap=cmap,
               norm=mcolors.TwoSlopeNorm(vmin=np.nanmin(lz_cat_matrix), vcenter=0, vmax=np.nanmax(lz_cat_matrix)))
ax.set_xticks(range(n_cats))
ax.set_xticklabels(categories, fontsize=10)
ax.set_yticks(range(n_models))
ax.set_yticklabels(MODEL_NAMES, fontsize=9)
ax.set_title("MMLU Per-Category $lz^*$", fontsize=14)
for i in range(n_models):
    for j in range(n_cats):
        ax.text(j, i, f"{lz_cat_matrix[i,j]:.1f}", ha="center", va="center", fontsize=8,
                color="white" if abs(lz_cat_matrix[i,j]) > 5 else "black")
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label("$lz^*$", fontsize=12)
plt.tight_layout()
plt.savefig(f"{OUT}/category_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()

# --- Gemini analysis figure ---
fig, axes = plt.subplots(2, 1, figsize=(20, 12))

# Panel 1: Gemini per-subject lz*
gemini_lz = lz_matrix[gemini_idx]
colors_gemini = ["red" if v > 2 else ("orange" if v > 1 else "steelblue") for v in gemini_lz]
axes[0].bar(range(n_subjects), gemini_lz, color=colors_gemini)
axes[0].set_xticks(range(n_subjects))
axes[0].set_xticklabels(short_names, rotation=90, fontsize=6)
axes[0].axhline(y=0, color="black", linewidth=0.5)
axes[0].axhline(y=1.96, color="red", linewidth=0.8, linestyle="--", label="z=1.96")
axes[0].axhline(y=-1.96, color="red", linewidth=0.8, linestyle="--")
axes[0].set_ylabel("$lz^*$", fontsize=12)
axes[0].set_title(f"Gemini-1.5 Per-Subject $lz^*$ (θ={thetas[gemini_idx]:.2f}, Overall MMLU Acc={gemini_mmlu_acc:.3f})", fontsize=13)
axes[0].legend()

# Panel 2: Gemini per-subject accuracy
gemini_acc = acc_matrix[gemini_idx]
colors_acc = ["red" if a_val == 1.0 else "steelblue" for a_val in gemini_acc]
axes[1].bar(range(n_subjects), gemini_acc, color=colors_acc)
axes[1].set_xticks(range(n_subjects))
axes[1].set_xticklabels(short_names, rotation=90, fontsize=6)
axes[1].axhline(y=1.0, color="gray", linewidth=0.5, linestyle=":")
axes[1].set_ylabel("Accuracy", fontsize=12)
axes[1].set_title("Gemini-1.5 Per-Subject Accuracy", fontsize=13)
axes[1].set_ylim(0, 1.05)

plt.tight_layout()
plt.savefig(f"{OUT}/gemini_analysis.png", dpi=200, bbox_inches="tight")
plt.close()

# --- Cross-model comparison: top anomalous subjects per model ---
fig, ax = plt.subplots(figsize=(20, 10))

# For each model, find the top-5 most anomalous subjects
top_k = 5
model_top_subjects = {}
for i in range(n_models):
    sorted_idx = np.argsort(lz_matrix[i])[::-1]
    top = [(subject_list_sorted[j], float(lz_matrix[i, j])) for j in sorted_idx[:top_k]]
    model_top_subjects[MODEL_NAMES[i]] = top

# Scatter plot: each model's lz* across subjects
for i in range(n_models):
    ax.scatter(range(n_subjects), lz_matrix[i], s=15, alpha=0.6, label=MODEL_NAMES[i])

ax.axhline(y=1.96, color="red", linewidth=0.8, linestyle="--", label="z=1.96")
ax.axhline(y=-1.96, color="red", linewidth=0.8, linestyle="--")
ax.axhline(y=0, color="black", linewidth=0.3)
ax.set_xticks(range(n_subjects))
ax.set_xticklabels(short_names, rotation=90, fontsize=6)
ax.set_ylabel("$lz^*$", fontsize=12)
ax.set_title("All Models: Per-Subject $lz^*$ Distribution", fontsize=14)
ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=7)
plt.tight_layout()
plt.savefig(f"{OUT}/all_models_scatter.png", dpi=200, bbox_inches="tight")
plt.close()

# ── Step 8: Domain summary JSON ──
print("Step 8: Building summary...")

# Overall MMLU lz* per model (for reference)
overall_mmlu_lz = np.array([
    compute_lz_star(mmlu_responses[i], thetas[i], a, b, c, d)
    for i in range(n_models)
])

# Identify flagged models (overall lz* > 1.96)
flagged = [(MODEL_NAMES[i], float(overall_mmlu_lz[i])) for i in range(n_models) if overall_mmlu_lz[i] > 1.96]

# Per-model: number of subjects with lz* > 1.96
subjects_flagged_per_model = {}
for i in range(n_models):
    n_flagged = int(np.sum(lz_matrix[i] > 1.96))
    flagged_list = [subject_list_sorted[j] for j in range(n_subjects) if lz_matrix[i, j] > 1.96]
    subjects_flagged_per_model[MODEL_NAMES[i]] = {
        "n_flagged_subjects": n_flagged,
        "flagged_subjects": flagged_list,
        "overall_mmlu_lz_star": float(overall_mmlu_lz[i]),
        "overall_mmlu_accuracy": float(mmlu_responses[i].mean()),
        "category_lz_star": {cat: float(lz_cat_matrix[i, k]) for k, cat in enumerate(categories)},
        "category_accuracy": {cat: float(acc_cat_matrix[i, k]) for k, cat in enumerate(categories)}
    }

# Gemini-specific
gemini_100pct_subjects = [subject_list_sorted[j] for j in range(n_subjects) if acc_matrix[gemini_idx, j] == 1.0]

# Subject difficulty ranking
subject_mean_acc = acc_matrix.mean(axis=0)
hardest_subjects = [(subject_list_sorted[j], float(subject_mean_acc[j])) for j in np.argsort(subject_mean_acc)[:10]]
easiest_subjects = [(subject_list_sorted[j], float(subject_mean_acc[j])) for j in np.argsort(subject_mean_acc)[-10:][::-1]]

summary = {
    "n_models": n_models,
    "n_subjects": n_subjects,
    "n_items_mmlu": 14042,
    "gemini_1_5": {
        "overall_mmlu_accuracy": float(gemini_mmlu_acc),
        "n_correct": int(gemini_mmlu_correct),
        "n_total": int(gemini_mmlu_total),
        "overall_mmlu_lz_star": float(overall_mmlu_lz[gemini_idx]),
        "n_subjects_100pct_accuracy": len(gemini_100pct_subjects),
        "subjects_100pct_accuracy": gemini_100pct_subjects,
        "n_subjects_with_errors": len(gemini_error_subjects),
        "error_subjects_detail": sorted(gemini_error_subjects, key=lambda x: x["n_wrong"], reverse=True),
        "top5_anomalous_subjects": model_top_subjects["Gemini-1.5"]
    },
    "flagged_models_overall": flagged,
    "per_model_detail": subjects_flagged_per_model,
    "subject_difficulty": {
        "hardest_10": hardest_subjects,
        "easiest_10": easiest_subjects
    }
}

with open(f"{OUT}/domain_summary.json", "w") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

# ── Step 9: Report ──
print("Step 9: Writing report...")

report_lines = [
    "# MMLU Domain-Specific lz* Analysis Report",
    "",
    "## Overview",
    f"- **Models**: {n_models}",
    f"- **MMLU Subjects**: {n_subjects}",
    f"- **MMLU Items**: 14,042",
    f"- **Broad Categories**: {', '.join(categories)}",
    "",
    "## Overall MMLU lz* (all 14042 items)",
    "",
    "| Model | θ | MMLU Acc | MMLU lz* | Flagged? |",
    "|-------|---|----------|----------|----------|",
]
for i in range(n_models):
    flag = "⚠️" if overall_mmlu_lz[i] > 1.96 else ""
    report_lines.append(
        f"| {MODEL_NAMES[i]} | {thetas[i]:.2f} | {mmlu_responses[i].mean():.3f} | {overall_mmlu_lz[i]:.2f} | {flag} |"
    )

report_lines += [
    "",
    "## Gemini-1.5 Deep Dive",
    f"- **Overall MMLU accuracy**: {gemini_mmlu_acc:.4f} ({gemini_mmlu_correct}/{gemini_mmlu_total})",
    f"- **Overall MMLU lz***: {overall_mmlu_lz[gemini_idx]:.2f}",
    f"- **Subjects with 100% accuracy**: {len(gemini_100pct_subjects)}/57",
    f"- **Subjects with errors**: {len(gemini_error_subjects)}/57",
    "",
    "### Subjects with 100% accuracy:",
    ", ".join(gemini_100pct_subjects) if gemini_100pct_subjects else "None",
    "",
    "### Subjects with errors (sorted by n_wrong):",
    "",
    "| Subject | Accuracy | N_items | N_wrong | lz* |",
    "|---------|----------|---------|---------|-----|",
]
for es in sorted(gemini_error_subjects, key=lambda x: x["n_wrong"], reverse=True):
    report_lines.append(
        f"| {es['subject']} | {es['accuracy']:.3f} | {es['n_items']} | {es['n_wrong']} | {es['lz_star']:.2f} |"
    )

report_lines += [
    "",
    "## Category-Level lz*",
    "",
    "| Model | STEM | Humanities | Social Sci | Other |",
    "|-------|------|------------|------------|-------|",
]
for i in range(n_models):
    vals = " | ".join(f"{lz_cat_matrix[i,k]:.2f}" for k in range(n_cats))
    report_lines.append(f"| {MODEL_NAMES[i]} | {vals} |")

report_lines += [
    "",
    "## Per-Model Flagged Subjects (lz* > 1.96)",
    "",
]
for i in range(n_models):
    n_f = int(np.sum(lz_matrix[i] > 1.96))
    if n_f > 0:
        flagged_subjs = [(subject_list_sorted[j], float(lz_matrix[i,j])) for j in range(n_subjects) if lz_matrix[i,j] > 1.96]
        flagged_subjs.sort(key=lambda x: x[1], reverse=True)
        top_str = ", ".join(f"{s} ({v:.1f})" for s, v in flagged_subjs[:10])
        report_lines.append(f"- **{MODEL_NAMES[i]}** ({n_f}/57 subjects): {top_str}")

report_lines += [
    "",
    "## Domain Concentration Analysis",
    "",
    "### Is Gemini-1.5's anomaly domain-concentrated?",
    "",
]

# Compute concentration metric: std of per-subject lz* vs mean
gemini_lz_std = float(np.nanstd(lz_matrix[gemini_idx]))
gemini_lz_mean = float(np.nanmean(lz_matrix[gemini_idx]))
gemini_lz_cv = gemini_lz_std / abs(gemini_lz_mean) if abs(gemini_lz_mean) > 0.01 else float('inf')

report_lines.append(f"- Gemini-1.5 per-subject lz* mean: {gemini_lz_mean:.2f}, std: {gemini_lz_std:.2f}, CV: {gemini_lz_cv:.2f}")

# Compare with other models
for i in range(n_models):
    m = float(np.nanmean(lz_matrix[i]))
    s = float(np.nanstd(lz_matrix[i]))
    cv = s / abs(m) if abs(m) > 0.01 else float('inf')
    report_lines.append(f"- {MODEL_NAMES[i]}: mean={m:.2f}, std={s:.2f}, CV={cv:.2f}")

report_lines += [
    "",
    "## Files Generated",
    "- `subject_lz_matrix.csv`: 12 models × 57 subjects lz*",
    "- `category_lz_matrix.csv`: 12 models × 4 categories lz*",
    "- `subject_accuracy_matrix.csv`: 12 models × 57 subjects accuracy",
    "- `category_accuracy_matrix.csv`: 12 models × 4 categories accuracy",
    "- `domain_heatmap.png`: Full heatmap (models × subjects)",
    "- `category_heatmap.png`: Category-level heatmap",
    "- `gemini_analysis.png`: Gemini-1.5 breakdown",
    "- `all_models_scatter.png`: All models scatter",
    "- `domain_summary.json`: Machine-readable summary",
]

with open(f"{OUT}/domain_report.md", "w") as f:
    f.write("\n".join(report_lines))

print("\n=== DONE ===")
print(f"All outputs saved to {OUT}/")
print(f"\nGemini-1.5 MMLU accuracy: {gemini_mmlu_acc:.4f}")
print(f"Gemini-1.5 MMLU lz*: {overall_mmlu_lz[gemini_idx]:.2f}")
print(f"Gemini-1.5 subjects at 100%: {len(gemini_100pct_subjects)}/57")
print(f"Gemini-1.5 subjects with errors: {len(gemini_error_subjects)}/57")
print(f"\nOverall MMLU lz* per model:")
for i in range(n_models):
    print(f"  {MODEL_NAMES[i]:30s}: lz*={overall_mmlu_lz[i]:+7.2f}, acc={mmlu_responses[i].mean():.3f}")
