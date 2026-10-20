# analysis classification sensitivity sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_classification-sensitivity-sweep_20260519T185355.jsonl`
- **Structured JSON:** [`12399eddc46a4bca99fa.json`](../../sessions/12/12399eddc46a4bca99fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-19T18:55:58.135964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T18:55:58.137096+00:00_

1	"""Dose-response profile classifier for contamination calibration.
2	
3	Classifies a model's accuracy trajectory across contamination dosages
4	into one of five canonical patterns: Immune, U-collapse, V-recovery,
5	Benefit, or Benefit-saturation.
6	"""
7	
8	from __future__ import annotations
9	
10	DOSAGES = ("d000", "d005", "d025", "d050", "d100")
11	PATTERNS = ("Immune", "U-collapse", "V-recovery", "Benefit", "Benefit-sat")
12	
13	
14	def classify_profile(
15	    accuracies: dict[str, float],
16	    *,
17	    noise_threshold: float = 1.0,
18	    severe_threshold: float = 5.0,
19	    saturation_ratio: float = 0.3,
20	    late_gain_floor: float = 0.5,
21	) -> dict:
22	    """Classify a dose-response accuracy profile into a canonical pattern.
23	
24	    Args:
25	        accuracies: Mapping from dosage key to accuracy (percentage points),
26	            e.g. {"d000": 76.44, "d005": 76.56, "d025": 76.50,
27	                   "d050": 76.02, "d100": 76.27}.
28	        noise_threshold: Maximum |delta| (pp) to be considered noise (Immune).
29	        severe_threshold: Minimum |delta| (pp) for severe degradation (U-collapse).
30	        saturation_ratio: If second-half gain < first-half gain * ratio,
31	            the benefit is saturating.
32	        late_gain_floor: If d100 - d050 < this value, late gain has stalled.
33	
34	    Returns:
35	        {"pattern": str, "confidence": float, "delta": float, "reasoning": str}
36	    """
37	    for d in DOSAGES:
38	        if d not in accuracies:
39	            raise ValueError(f"Missing dosage key: {d}")
40	
41	    a = {d: float(accuracies[d]) for d in DOSAGES}
42	    delta = a["d100"] - a["d000"]
43	    mid_vals = [a["d005"], a["d025"], a["d050"]]
44	    mid_min = min(mid_vals)
45	
46	    # ── Decision tree ────────────────────────────────────────────────
47	
48	    if abs(delta) <= noise_threshold:
49	        margin = noise_threshold - abs(delta)
50	        return _result(
51	            "Immune", delta, margin, noise_thresh
…[truncated 4805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T18:55:58.137400+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T18:55:58.137579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T18:55:58.137712+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/analysis/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/analysis/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T18:55:58.137841+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T18:55:58.137972+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T18:55:58.138099+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_profile_stability.py\\nitem_vulnerability.py\\nresults\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:55:58.138221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/analysis/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/analysis/results/"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:55:58.138364+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_delta_arc_challenge.png\\nbootstrap_delta_mmlu.png\\nbootstrap_dose_response_arc_challenge.png\\nbootstrap_dose_response_mmlu.png\\nbootstrap_results_arc_challenge.json\\nbootstrap_results_mmlu.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T18:55:58.138569+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "mkdir -p /root/contamcal-irt-calibration/analysis/results/sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "mkdir -p /root/contamcal-irt-calibration/analysis/results/sensitivity"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:55:58.138770+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T18:55:58.139030+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "cat << 'PYEOF' > /root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py\n\"\"\"Threshold sensitivity sweep for dose-response profile classification.\n\nSweeps noise_threshold (τ) and severe_threshold (σ) to show classification\nrobustness across parameter choices.\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport os\nfrom itertools import product\nfrom pathlib import Path\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\nimport numpy as np\n\n# ── Classification logic (self-contained) ──────────────────────────────\n\nDOSAGES = (\"d000\", \"d005\", \"d025\", \"d050\", \"d100\")\nPATTERNS = (\"Immune\", \"U-collapse\", \"V-recovery\", \"Benefit\", \"Benefit-sat\")\nPATTERN_TO_INT = {p: i for i, p in enumerate(PATTERNS)}\n\n\ndef classify_profile(\n    accuracies: dict[str, float],\n    *,\n    noise_threshold: float = 1.0,\n    severe_threshold: float = 5.0,\n    saturation_ratio: float = 0.3,\n    late_gain_floor: float = 0.5,\n) -> str:\n    a = {d: float(accuracies[d]) for d in DOSAGES}\n    delta = a[\"d100\"] - a[\"d000\"]\n    mid_vals = [a[\"d005\"], a[\"d025\"], a[\"d050\"]]\n    mid_min = min(mid_vals)\n\n    if abs(delta) <= noise_threshold:\n        return \"Immune\"\n\n    if delta < -noise_threshold:\n        if delta <= -severe_threshold:\n            return \"U-collapse\"\n        v_dip = mid_min < a[\"d100\"] and mid_min < a[\"d000\"]\n        if v_dip:\n            return \"V-recovery\"\n        return \"U-collapse\"\n\n    # delta > noise_threshold\n    first_half = a[\"d025\"] - a[\"d000\"]\n    second_half = a[\"d100\"] - a[\"d025\"]\n    late_gain = a[\"d100\"] - a[\"d050\"]\n    saturating = (\n        (first_half > 0 and second_half < first_half * saturation_ratio)\n        or late_gain < late_gain_floor\n    )\n    if saturating:\n        return \"Benefit-sat\"\n    return \"Benefit\"\n\n\n# ── Data ───────────────────────────────────────────────────────────────\n\n# seed=42 MMLU accuracies (percentage points)\nDATA = {\n    \"Phi-4\":     {\"d000\": 76.44, \"d005\": 76.56, \"d025\": 76.50, \"d050\": 76.02, \"d100\": 76.27},\n    \"Qwen2.5-14B\": {\"d000\": 69.44, \"d005\": 68.36, \"d025\": 64.07, \"d050\": 59.41, \"d100\": 60.07},\n    \"Qwen2.5-7B\":  {\"d000\": 66.11, \"d005\": 65.04, \"d025\": 63.01, \"d050\": 63.56, \"d100\": 64.33},\n    \"Gemma-2-9B\":  {\"d000\": 61.86, \"d005\": 62.89, \"d025\": 63.54, \"d050\": 64.71, \"d100\": 65.62},\n    \"OLMo-2-7B\":   {\"d000\": 53.79, \"d005\": 55.08, \"d025\": 56.19, \"d050\": 57.00, \"d100\": 57.00},\n}\nMODEL_ORDER = list(DATA.keys())\n\n# ── Sweep ──────────────────────────────────────────────────────────────\n\nTAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\nSIGMA_VALUES = [3, 4, 5, 6, 7]\nDEFAULT_TAU = 1.0\nDEFAULT_SIGMA = 5.0\n\n\ndef run_sweep():\n    results = {}\n    for tau, sigma in product(TAU_VALUES, SIGMA_VALUES):\n        key = f\"tau={tau:.2f}_sigma={sigma}\"\n        classifications = {}\n        for model, accs in DATA.items():\n            classifications[model] = classify_profile(\n                accs, noise_threshold=tau, severe_threshold=sigma\n            )\n        results[key] = classifications\n    return results\n\n\ndef get_default_classifications():\n    return {\n        model: classify_profile(accs, noise_threshold=DEFAULT_TAU, severe_threshold=DEFAULT_SIGMA)\n        for model, accs in DATA.items()\n    }\n\n\n# ── Visualization ──────────────────────────────────────────────────────\n\ndef plot_heatmaps(results, default_cls, output_dir: Path):\n    plt.rcParams.update({\n        \"font.family\": \"DejaVu Sans\",\n        \"font.size\": 9,\n        \"axes.linewidth\": 0.8,\n        \"axes.labelsize\": 10,\n        \"axes.titlesize\": 11,\n    })\n\n    # --- Figure 1: Agreement count heatmap ---\n    agree_matrix = np.zeros((len(SIGMA_VALUES), len(TAU_VALUES)), dtype=int)\n    for i, sigma in enumerate(SIGMA_VALUES):\n        for j, tau in enumerate(TAU_VALUES):\n            key = f\"tau={tau:.2f}_sigma={sigma}\"\n            count = sum(\n                1 for m in MODEL_ORDER\n                if results[key][m] == default_cls[m]\n            )\n            agree_matrix[i, j] = count\n\n    fig1, ax1 = plt.subplots(figsize=(5.0, 3.5))\n    cmap_agree = mcolors.ListedColormap([\"#d73027\", \"#fc8d59\", \"#fee08b\", \"#d9ef8b\", \"#91cf60\", \"#1a9850\"])\n    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]\n    norm_agree = mcolors.BoundaryNorm(bounds, cmap_agree.N)\n\n    im1 = ax1.imshow(agree_matrix, cmap=cmap_agree, norm=norm_agree, aspect=\"auto\")\n    ax1.set_xticks(range(len(TAU_VALUES)))\n    ax1.set_xticklabels([f\"{t:.2f}\" for t in TAU_VALUES])\n    ax1.set_yticks(range(len(SIGMA_VALUES)))\n    ax1.set_yticklabels([str(s) for s in SIGMA_VALUES])\n    ax1.set_xlabel(r\"$\\tau$ (noise threshold, pp)\")\n    ax1.set_ylabel(r\"$\\sigma$ (severe threshold, pp)\")\n    ax1.set_title(\"Models agreeing with default classification\")\n\n    for i in range(len(SIGMA_VALUES)):\n        for j in range(len(TAU_VALUES)):\n            val = agree_matrix[i, j]\n            color = \"white\" if val <= 2 else \"black\"\n            ax1.text(j, i, str(val), ha=\"center\", va=\"center\", fontsize=10, fontweight=\"bold\", color=color)\n\n    # Mark default\n    def_j = TAU_VALUES.index(DEFAULT_TAU)\n    def_i = SIGMA_VALUES.index(int(DEFAULT_SIGMA))\n    ax1.plot(def_j, def_i, marker=\"s\", ms=22, mec=\"black\", mew=2, mfc=\"none\")\n\n    cb1 = fig1.colorbar(im1, ax=ax1, ticks=range(6), shrink=0.85)\n    cb1.set_label(\"# models agreeing (out of 5)\")\n    fig1.tight_layout()\n    fig1.savefig(output_dir / \"sensitivity_agreement_heatmap.pdf\", dpi=300, bbox_inches=\"tight\")\n    fig1.savefig(output_dir / \"sensitivity_agreement_heatmap.png\", dpi=300, bbox_inches=\"tight\")\n    plt.close(fig1)\n\n    # --- Figure 2: Per-model classification heatmaps ---\n    pattern_cmap = mcolors.ListedColormap([\"#4575b4\", \"#d73027\", \"#fdae61\", \"#1a9850\", \"#a6d96a\"])\n    pattern_norm = mcolors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], pattern_cmap.N)\n    pattern_labels_short = [\"Imm\", \"U-col\", \"V-rec\", \"Ben\", \"B-sat\"]\n\n    fig2, axes = plt.subplots(1, 5, figsize=(16, 3.0), sharey=True)\n    for ax, model in zip(axes, MODEL_ORDER):\n        mat = np.zeros((len(SIGMA_VALUES), len(TAU_VALUES)), dtype=int)\n        for i, sigma in enumerate(SIGMA_VALUES):\n            for j, tau in enumerate(TAU_VALUES):\n                key = f\"tau={tau:.2f}_sigma={sigma}\"\n                mat[i, j] = PATTERN_TO_INT[results[key][model]]\n\n        im = ax.imshow(mat, cmap=pattern_cmap, norm=pattern_norm, aspect=\"auto\")\n        ax.set_xticks(range(len(TAU_VALUES)))\n        ax.set_xticklabels([f\"{t}\" for t in TAU_VALUES], fontsize=7)\n        ax.set_yticks(range(len(SIGMA_VALUES)))\n        if ax == axes[0]:\n            ax.set_yticklabels([str(s) for s in SIGMA_VALUES])\n            ax.set_ylabel(r\"$\\sigma$ (pp)\")\n        ax.set_xlabel(r\"$\\tau$ (pp)\")\n        ax.set_title(model, fontsize=9)\n\n        for i in range(len(SIGMA_VALUES)):\n            for j in range(len(TAU_VALUES)):\n                label = pattern_labels_short[mat[i, j]]\n                color = \"white\" if mat[i, j] in (0, 1) else \"black\"\n                ax.text(j, i, label, ha=\"center\", va=\"center\", fontsize=6, fontweight=\"bold\", color=color)\n\n        ax.plot(def_j, def_i, marker=\"s\", ms=18, mec=\"black\", mew=1.5, mfc=\"none\")\n\n    # Legend\n    from matplotlib.patches import Patch\n    legend_patches = [Patch(facecolor=pattern_cmap(i), label=PATTERNS[i]) for i in range(5)]\n    fig2.legend(handles=legend_patches, loc=\"lower center\", ncol=5, fontsize=8,\n                bbox_to_anchor=(0.5, -0.08), frameon=False)\n\n    fig2.suptitle(\"Per-model classification across threshold combinations\", fontsize=11, y=1.02)\n    fig2.tight_layout()\n    fig2.savefig(output_dir / \"sensitivity_permodel_heatmap.pdf\", dpi=300, bbox_inches=\"tight\")\n    fig2.savefig(output_dir / \"sensitivity_permodel_heatmap.png\", dpi=300, bbox_inches=\"tight\")\n    plt.close(fig2)\n\n    return agree_matrix\n\n\n# ── Summary ────────────────────────────────────────────────────────────\n\ndef write_summary(results, default_cls, agree_matrix, output_dir: Path):\n    lines = [\"Classification Sensitivity Sweep Summary\", \"=\" * 45, \"\"]\n    lines.append(f\"Parameters swept: tau in {TAU_VALUES}, sigma in {SIGMA_VALUES}\")\n    lines.append(f\"Total combinations: {len(TAU_VALUES) * len(SIGMA_VALUES)}\")\n    lines.append(f\"Default: tau={DEFAULT_TAU}, sigma={DEFAULT_SIGMA}\")\n    lines.append(\"\")\n\n    lines.append(\"Default classifications:\")\n    for m in MODEL_ORDER:\n        lines.append(f\"  {m:20s} -> {default_cls[m]}\")\n    lines.append(\"\")\n\n    # Per-model stability\n    lines.append(\"Per-model stability across all 30 combinations:\")\n    lines.append(\"-\" * 50)\n    for model in MODEL_ORDER:\n        cls_set = set()\n        for key in results:\n            cls_set.add(results[key][model])\n        if len(cls_set) == 1:\n            lines.append(f\"  {model:20s} ROBUST — always {cls_set.pop()}\")\n        else:\n            cls_counts = {}\n            for key in results:\n                c = results[key][model]\n                cls_counts[c] = cls_counts.get(c, 0) + 1\n            detail = \", \".join(f\"{c}: {n}/30\" for c, n in sorted(cls_counts.items(), key=lambda x: -x[1]))\n            lines.append(f\"  {model:20s} SENSITIVE — {detail}\")\n    lines.append(\"\")\n\n    # Agreement stats\n    lines.append(\"Agreement heatmap stats:\")\n    lines.append(f\"  All 5 agree: {np.sum(agree_matrix == 5)} / 30 combinations\")\n    lines.append(f\"  4+ agree:    {np.sum(agree_matrix >= 4)} / 30 combinations\")\n    lines.append(f\"  3+ agree:    {np.sum(agree_matrix >= 3)} / 30 combinations\")\n    lines.append(\"\")\n\n    # Flipping details\n    lines.append(\"Classification transitions (where models flip):\")\n    lines.append(\"-\" * 50)\n    for model in MODEL_ORDER:\n        transitions = []\n        for tau in TAU_VALUES:\n            for sigma in SIGMA_VALUES:\n                key = f\"tau={tau:.2f}_sigma={sigma}\"\n                cls = results[key][model]\n                if cls != default_cls[model]:\n                    transitions.append(f\"  tau={tau:.2f}, sigma={sigma}: {default_cls[model]} -> {cls}\")\n        if transitions:\n            lines.append(f\"\\n  {model}:\")\n            for t in transitions:\n                lines.append(t)\n\n    text = \"\\n\".join(lines)\n    (output_dir / \"sensitivity_summary.txt\").write_text(text)\n    print(text)\n\n\n# ── Main ───────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--output-dir\", default=\"/root/contamcal-irt-calibration/analysis/results/sensitivity/\")\n    args = parser.parse_args()\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    results = run_sweep()\n    default_cls = get_default_classifications()\n\n    # Save matrix\n    with open(output_dir / \"sensitivity_matrix.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved sensitivity_matrix.json ({len(results)} combinations)\")\n\n    # Plot\n    agree_matrix = plot_heatmaps(results, default_cls, output_dir)\n\n    # Summary\n    write_summary(results, default_cls, agree_matrix, output_dir)\n\n    print(f\"\\nAll outputs in: {output_dir}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat << 'PYEOF' > /root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py\n\"\"\"Threshold sensitivity sweep for dose-response profile classification.\n\nSweeps noise_threshold (τ) and severe_threshold (σ) to show classification\nrobustness across parameter choices.\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport os\nfrom itertools import product\nfrom pathlib import Path\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\nimport numpy as np\n\n# ── Classification logic (self-contained) ──────────────────────────────\n\nDOSAGES = (\"d000\", \"d005\", \"d025\", \"d050\", \"d100\")\nPATTERNS = (\"Immune\", \"U-collapse\", \"V-recovery\", \"Benefit\", \"Benefit-sat\")\nPATTERN_TO_INT = {p: i for i, p in enumerate(PATTERNS)}\n\n\ndef classify_profile(\n    accuracies: dict[str, float],\n    *,\n    noise_threshold: float = 1.0,\n    severe_threshold: float = 5.0,\n    saturation_ratio: float = 0.3,\n    late_gain_floor: float = 0.5,\n) -> str:\n    a = {d: float(accuracies[d]) for d in DOSAGES}\n    delta = a[\"d100\"] - a[\"d000\"]\n    mid_vals = [a[\"d005\"], a[\"d025\"], a[\"d050\"]]\n    mid_min = min(mid_vals)\n\n    if abs(delta) <= noise_threshold:\n        return \"Immune\"\n\n    if delta < -noise_threshold:\n        if delta <= -severe_threshold:\n            return \"U-collapse\"\n        v_dip = mid_min < a[\"d100\"] and mid_min < a[\"d000\"]\n        if v_dip:\n            return \"V-recovery\"\n        return \"U-collapse\"\n\n    # delta > noise_threshold\n    first_half = a[\"d025\"] - a[\"d000\"]\n    second_half = a[\"d100\"] - a[\"d025\"]\n    late_gain = a[\"d100\"] - a[\"d050\"]\n    saturating = (\n        (first_half > 0 and second_half < first_half * saturation_ratio)\n        or late_gain < late_gain_floor\n    )\n    if saturating:\n        return \"Benefit-sat\"\n    return \"Benefit\"\n\n\n# ── Data ───────────────────────────────────────────────────────────────\n\n# seed=42 MMLU accuracies (percentage points)\nDATA = {\n    \"Phi-4\":     {\"d000\": 76.44, \"d005\": 76.56, \"d025\": 76.50, \"d050\": 76.02, \"d100\": 76.27},\n    \"Qwen2.5-14B\": {\"d000\": 69.44, \"d005\": 68.36, \"d025\": 64.07, \"d050\": 59.41, \"d100\": 60.07},\n    \"Qwen2.5-7B\":  {\"d000\": 66.11, \"d005\": 65.04, \"d025\": 63.01, \"d050\": 63.56, \"d100\": 64.33},\n    \"Gemma-2-9B\":  {\"d000\": 61.86, \"d005\": 62.89, \"d025\": 63.54, \"d050\": 64.71, \"d100\": 65.62},\n    \"OLMo-2-7B\":   {\"d000\": 53.79, \"d005\": 55.08, \"d025\": 56.19, \"d050\": 57.00, \"d100\": 57.00},\n}\nMODEL_ORDER = list(DATA.keys())\n\n# ── Sweep ──────────────────────────────────────────────────────────────\n\nTAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\nSIGMA_VALUES = [3, 4, 5, 6, 7]\nDEFAULT_TAU = 1.0\nDEFAULT_SIGMA = 5.0\n\n\ndef run_sweep():\n    results = {}\n    for tau, sigma in product(TAU_VALUES, SIGMA_VALUES):\n        key = f\"tau={tau:.2f}_sigma={sigma}\"\n        classifications = {}\n        for model, accs in DATA.items():\n            classifications[model] = classify_profile(\n                accs, noise_threshold=tau, severe_threshold=sigma\n            )\n        results[key] = classifications\n    return results\n\n\ndef get_default_classifications():\n    return {\n        model: classify_profile(accs, noise_threshold=DEFAULT_TAU, severe_threshold=DEFAULT_SIGMA)\n        for model, accs in DATA.items()\n    }\n\n\n# ── Visualization ──────────────────────────────────────────────────────\n\ndef plot_heatmaps(results, default_cls, output_dir: Path):\n    plt.rcParams.update({\n        \"font.family\": \"DejaVu Sans\",\n        \"font.size\": 9,\n        \"axes.linewidth\": 0.8,\n        \"axes.labelsize\": 10,\n        \"axes.titlesize\": 11,\n    })\n\n    # --- Figure 1: Agreement count heatmap ---\n    agree_matrix = np.zeros((len(SIGMA_VALUES), len(TAU_VALUES)), dtype=int)\n    for i, sigma in enumerate(SIGMA_VALUES):\n        for j, tau in enumerate(TAU_VALUES):\n            key = f\"tau={tau:.2f}_sigma={sigma}\"\n            count = sum(\n                1 for m in MODEL_ORDER\n                if results[key][m] == default_cls[m]\n            )\n            agree_matrix[i, j] = count\n\n    fig1, ax1 = plt.subplots(figsize=(5.0, 3.5))\n    cmap_agree = mcolors.ListedColormap([\"#d73027\", \"#fc8d59\", \"#fee08b\", \"#d9ef8b\", \"#91cf60\", \"#1a9850\"])\n    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]\n    norm_agree = mcolors.BoundaryNorm(bounds, cmap_agree.N)\n\n    im1 = ax1.imshow(agree_matrix, cmap=cmap_agree, norm=norm_agree, aspect=\"auto\")\n    ax1.set_xticks(range(len(TAU_VALUES)))\n    ax1.set_xticklabels([f\"{t:.2f}\" for t in TAU_VALUES])\n    ax1.set_yticks(range(len(SIGMA_VALUES)))\n    ax1.set_yticklabels([str(s) for s in SIGMA_VALUES])\n    ax1.set_xlabel(r\"$\\tau$ (noise threshold, pp)\")\n    ax1.set_ylabel(r\"$\\sigma$ (severe threshold, pp)\")\n    ax1.set_title(\"Models agreeing with default classification\")\n\n    for i in range(len(SIGMA_VALUES)):\n        for j in range(len(TAU_VALUES)):\n            val = agree_matrix[i, j]\n            color = \"white\" if val <= 2 else \"black\"\n            ax1.text(j, i, str(val), ha=\"center\", va=\"center\", fontsize=10, fontweight=\"bold\", color=color)\n\n    # Mark default\n    def_j = TAU_VALUES.index(DEFAULT_TAU)\n    def_i = SIGMA_VALUES.index(int(DEFAULT_SIGMA))\n    ax1.plot(def_j, def_i, marker=\"s\", ms=22, mec=\"black\", mew=2, mfc=\"none\")\n\n    cb1 = fig1.colorbar(im1, ax=ax1, ticks=range(6), shrink=0.85)\n    cb1.set_label(\"# models agreeing (out of 5)\")\n    fig1.tight_layout()\n    fig1.savefig(output_dir / \"sensitivity_agreement_heatmap.pdf\", dpi=300, bbox_inches=\"tight\")\n    fig1.savefig(output_dir / \"sensitivity_agreement_heatmap.png\", dpi=300, bbox_inches=\"tight\")\n    plt.close(fig1)\n\n    # --- Figure 2: Per-model classification heatmaps ---\n    pattern_cmap = mcolors.ListedColormap([\"#4575b4\", \"#d73027\", \"#fdae61\", \"#1a9850\", \"#a6d96a\"])\n    pattern_norm = mcolors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], pattern_cmap.N)\n    pattern_labels_short = [\"Imm\", \"U-col\", \"V-rec\", \"Ben\", \"B-sat\"]\n\n    fig2, axes = plt.subplots(1, 5, figsize=(16, 3.0), sharey=True)\n    for ax, model in zip(axes, MODEL_ORDER):\n        mat = np.zeros((len(SIGMA_VALUES), len(TAU_VALUES)), dtype=int)\n        for i, sigma in enumerate(SIGMA_VALUES):\n            for j, tau in enumerate(TAU_VALUES):\n                key = f\"tau={tau:.2f}_sigma={sigma}\"\n                mat[i, j] = PATTERN_TO_INT[results[key][model]]\n\n        im = ax.imshow(mat, cmap=pattern_cmap, norm=pattern_norm, aspect=\"auto\")\n        ax.set_xticks(range(len(TAU_VALUES)))\n        ax.set_xticklabels([f\"{t}\" for t in TAU_VALUES], fontsize=7)\n        ax.set_yticks(range(len(SIGMA_VALUES)))\n        if ax == axes[0]:\n            ax.set_yticklabels([str(s) for s in SIGMA_VALUES])\n            ax.set_ylabel(r\"$\\sigma$ (pp)\")\n        ax.set_xlabel(r\"$\\tau$ (pp)\")\n        ax.set_title(model, fontsize=9)\n\n        for i in range(len(SIGMA_VALUES)):\n            for j in range(len(TAU_VALUES)):\n                label = pattern_labels_short[mat[i, j]]\n                color = \"white\" if mat[i, j] in (0, 1) else \"black\"\n                ax.text(j, i, label, ha=\"center\", va=\"center\", fontsize=6, fontweight=\"bold\", color=color)\n\n        ax.plot(def_j, def_i, marker=\"s\", ms=18, mec=\"black\", mew=1.5, mfc=\"none\")\n\n    # Legend\n    from matplotlib.patches import Patch\n    legend_patches = [Patch(facecolor=pattern_cmap(i), label=PATTERNS[i]) for i in range(5)]\n    fig2.legend(handles=legend_patches, loc=\"lower center\", ncol=5, fontsize=8,\n                bbox_to_anchor=(0.5, -0.08), frameon=False)\n\n    fig2.suptitle(\"Per-model classification across threshold combinations\", fontsize=11, y=1.02)\n    fig2.tight_layout()\n    fig2.savefig(output_dir / \"sensitivity_permodel_heatmap.pdf\", dpi=300, bbox_inches=\"tight\")\n    fig2.savefig(output_dir / \"sensitivity_permodel_heatmap.png\", dpi=300, bbox_inches=\"tight\")\n    plt.close(fig2)\n\n    return agree_matrix\n\n\n# ── Summary ────────────────────────────────────────────────────────────\n\ndef write_summary(results, default_cls, agree_matrix, output_dir: Path):\n    lines = [\"Classification Sensitivity Sweep Summary\", \"=\" * 45, \"\"]\n    lines.append(f\"Parameters swept: tau in {TAU_VALUES}, sigma in {SIGMA_VALUES}\")\n    lines.append(f\"Total combinations: {len(TAU_VALUES) * len(SIGMA_VALUES)}\")\n    lines.append(f\"Default: tau={DEFAULT_TAU}, sigma={DEFAULT_SIGMA}\")\n    lines.append(\"\")\n\n    lines.append(\"Default classifications:\")\n    for m in MODEL_ORDER:\n        lines.append(f\"  {m:20s} -> {default_cls[m]}\")\n    lines.append(\"\")\n\n    # Per-model stability\n    lines.append(\"Per-model stability across all 30 combinations:\")\n    lines.append(\"-\" * 50)\n    for model in MODEL_ORDER:\n        cls_set = set()\n        for key in results:\n            cls_set.add(results[key][model])\n        if len(cls_set) == 1:\n            lines.append(f\"  {model:20s} ROBUST — always {cls_set.pop()}\")\n        else:\n            cls_counts = {}\n            for key in results:\n                c = results[key][model]\n                cls_counts[c] = cls_counts.get(c, 0) + 1\n            detail = \", \".join(f\"{c}: {n}/30\" for c, n in sorted(cls_counts.items(), key=lambda x: -x[1]))\n            lines.append(f\"  {model:20s} SENSITIVE — {detail}\")\n    lines.append(\"\")\n\n    # Agreement stats\n    lines.append(\"Agreement heatmap stats:\")\n    lines.append(f\"  All 5 agree: {np.sum(agree_matrix == 5)} / 30 combinations\")\n    lines.append(f\"  4+ agree:    {np.sum(agree_matrix >= 4)} / 30 combinations\")\n    lines.append(f\"  3+ agree:    {np.sum(agree_matrix >= 3)} / 30 combinations\")\n    lines.append(\"\")\n\n    # Flipping details\n    lines.append(\"Classification transitions (where models flip):\")\n    lines.append(\"-\" * 50)\n    for model in MODEL_ORDER:\n        transitions = []\n        for tau in TAU_VALUES:\n            for sigma in SIGMA_VALUES:\n                key = f\"tau={tau:.2f}_sigma={sigma}\"\n                cls = results[key][model]\n                if cls != default_cls[model]:\n                    transitions.append(f\"  tau={tau:.2f}, sigma={sigma}: {default_cls[model]} -> {cls}\")\n        if transitions:\n            lines.append(f\"\\n  {model}:\")\n            for t in transitions:\n                lines.append(t)\n\n    text = \"\\n\".join(lines)\n    (output_dir / \"sensitivity_summary.txt\").write_text(text)\n    print(text)\n\n\n# ── Main ───────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument(\"--output-dir\", default=\"/root/contamcal-irt-calibration/analysis/results/sensitivity/\")\n    args = parser.parse_args()\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    results = run_sweep()\n    default_cls = get_default_classifications()\n\n    # Save matrix\n    with open(output_dir / \"sensitivity_matrix.json\", \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved sensitivity_matrix.json ({len(results)} combinations)\")\n\n    # Plot\n    agree_matrix = plot_heatmaps(results, default_cls, output_dir)\n\n    # Summary\n    write_summary(results, default_cls, agree_matrix, output_dir)\n\n    print(f\"\\nAll outputs in: {output_dir}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:55:58.139466+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T18:55:58.139717+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py --output-dir /root/contamcal-irt-calibration/analysis/results/sensitivity/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/analysis/classification_sensitivity_sweep.py --output-dir /root/contamcal-irt-calibration/analysis/results/sensitivity/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:55:58.139987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved sensitivity_matrix.json (30 combinations)\\nClassification Sensitivity Sweep Summary\\n=============================================\\n\\nParameters swept: tau in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0], sigma in [3, 4, 5, 6, 7]\\nTotal combinations: 30\\nDefault: tau=1.0, sigma=5.0\\n\\nDefault classifications:\\n  Phi-4                -> Immune\\n  Qwen2.5-14B          -> U-collapse\\n  Qwen2.5-7B           -> V-recovery\\n  Gemma-2-9B           -> Benefit\\n  OLMo-2-7B            -> Benefit-sat\\n\\nPer-model stability across all 30 combinations:\\n--------------------------------------------------\\n  Phi-4                ROBUST — always Immune\\n  Qwen2.5-14B          ROBUST — always U-collapse\\n  Qwen2.5-7B           SENSITIVE — V-recovery: 25/30, Immune: 5/30\\n  Gemma-2-9B           ROBUST — always Benefit\\n  OLMo-2-7B            ROBUST — always Benefit-sat\\n\\nAgreement heatmap stats:\\n  All 5 agree: 25 / 30 combinations\\n  4+ agree:    30 / 30 combinations\\n  3+ agree:    30 / 30 combinations\\n\\nClassification transitions (where models flip):\\n--------------------------------------------------\\n\\n  Qwen2.5-7B:\\n  tau=2.00, sigma=3: V-recovery -> Immune\\n  tau=2.00, sigma=4: V-recovery -> Immune\\n  tau=2.00, sigma=5: V-recovery -> Immune\\n  tau=2.00, sigma=6: V-recovery -> Immune\\n  tau=2.00, sigma=7: V-recovery -> Immune\\n\\nAll outputs in: /root/contamcal-irt-calibration/analysis/results/sensitivity\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T18:55:58.140266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls -lh /root/contamcal-irt-calibration/analysis/results/sensitivity/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls -lh /root/contamcal-irt-calibration/analysis/results/sensitivity/"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T18:55:58.140549+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 284K\\n-rw-r--r-- 1 root root  20K May 20 02:55 sensitivity_agreement_heatmap.pdf\\n-rw-r--r-- 1 root root  86K May 20 02:55 sensitivity_agreement_heatmap.png\\n-rw-r--r-- 1 root root 5.2K May 20 02:55 sensitivity_matrix.json\\n-rw-r--r-- 1 root root  29K May 20 02:55 sensitivity_permodel_heatmap.pdf\\n-rw-r--r-- 1 root root 132K May 20 02:55 sensitivity_permodel_heatmap.png\\n-rw-r--r-- 1 root root 1.3K May 20 02:55 sensitivity_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T18:55:58.140761+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:55:58.140960+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T18:55:58.141155+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T18:55:58.141372+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T18:55:58.141640+00:00_

全部完成。汇报结果：

## Classification Sensitivity Sweep 结果

**30 个 (τ, σ) 组合的分类结果：**

| Model | 稳定性 | 详情 |
|-------|--------|------|
| **Phi-4** | ROBUST | 30/30 = Immune |
| **Qwen2.5-14B** | ROBUST | 30/30 = U-collapse |
| **Qwen2.5-7B** | SENSITIVE | 25/30 V-recovery, 5/30 Immune |
| **Gemma-2-9B** | ROBUST | 30/30 = Benefit |
| **OLMo-2-7B** | ROBUST | 30/30 = Benefit-sat |

**关键发现：**

- **4/5 family 完全稳定**——在所有 30 种阈值组合下分类不变
- **Qwen2.5-7B 是唯一 sensitive case**，仅在 τ=2.0（最宽松 noise band）时从 V-recovery 翻转为 Immune。这符合预期：其 delta = -1.78pp，恰好在 noise/recovery 边界附近
- σ 的变化对所有 model 的分类**零影响**（因为没有 model 的 delta 在 -3pp ~ -7pp 范围内翻转）
- **25/30 组合 5 个 model 全部一致，30/30 组合至少 4/5 一致**

这个结果对审稿人很有说服力——分类对阈值选择高度 robust。

**输出文件：**
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.pdf` — 总体一致性热力图
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.pdf` — 5 个 model 分别的分类热力图
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json` — 完整分类数据
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt` — 文本摘要

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_classification-sensitivity-sweep_20260519T185355"
}
```

</details>

---
