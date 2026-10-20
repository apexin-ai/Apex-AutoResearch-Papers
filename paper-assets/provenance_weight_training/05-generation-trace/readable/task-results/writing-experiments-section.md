# writing experiments section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-section_20260515T211527_result.json`
- **Structured JSON:** [`cc3c0fd62de8dad6a2ab.json`](../../sessions/cc/cc3c0fd62de8dad6a2ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入并注册。JSON 报告：

```json
{
  "files_written": [
    "artifacts/_project/paper/experiments.tex",
    "artifacts/_project/paper/results.tex"
  ],
  "section4_experiments": {
    "structure": ["Training Data", "Detector", "Training", "Evaluation", "Methods (5 baselines)"],
    "estimated_length": "~1 page",
    "new_citations_needed": ["penedo_2024_fineweb", "yang_2025_qwen3"],
    "labels": ["sec:experiments"],
    "cross_refs": ["sec:method"]
  },
  "section5_results": {
    "structure": ["Main Comparison (Table 1)", "Sensitivity Analysis: τ sweep (Table 2) + n_min"],
    "estimated_length": "~1.3 pages + 2 tables (~0.5 page) ≈ 1.5 pages total",
    "tables": {
      "tab:main": "5 methods × 3 seeds, ESS-only/Golden Ratio seed42 only",
      "tab:tau": "6 τ values with PPL, Δ_unif, mean b*"
    },
    "labels": ["sec:results", "tab:main", "tab:tau"],
    "cross_refs": ["sec:method", "sec:algorithm", "app:grid"],
    "forward_refs_needed": ["app:grid (grid-b full sweep appendix)"]
  },
  "number_harmonization": {
    "decision": "Used registry 3dp values for cross-table consistency",
    "uniform_seed42": "17.694 (consistent with τ sweep reference)",
    "adaptive_seed42": "17.653 (consistent with τ=0.80 row)",
    "key_claims": [
      "Adaptive mean 17.651 vs Grid-best mean 17.646: gap ≤0.007 per seed",
      "ESS-only 17.728: +0.034 worse than uniform",
      "Golden Ratio 17.654: adaptive within 0.001",
      "τ ∈ [0.5, 0.8] all beat uniform; τ=0.8 recommended default",
      "n_min=1 degrades to 17.789; n_min=2,3 stable"
    ]
  },
  "deferred_to_appendix": ["Full grid-b sweep (app:grid)", "seed456 b≥1.5 checkpoint artifact note"],
  "missing_data_noted": ["ESS-only seed123/456 in progress", "n_min=4 running"],
  "binding_analysis": "Already in method.tex §3.3; results.tex references it, adds b* distribution stats (median 0.87, IQR [0.54,1.51])"
}
```

**关键设计决策**：
- 使用 registry 3dp 数值（如 uniform-s42=17.694）确保 Table 1 和 Table 2 的 baseline 一致
- Binding constraint 分析已在 method.tex 中呈现，results.tex 补充 b* 分布统计并引用 `\S\ref{sec:algorithm}`，避免重复
- `\label{sec:experiments}` 避免与 method.tex 的 `\label{sec:setup}` 冲突
- 需新增 bib 条目：`penedo_2024_fineweb`、`yang_2025_qwen3`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "files_written": [
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/results.tex"
    ],
    "section4_experiments": {
      "structure": [
        "Training Data",
        "Detector",
        "Training",
        "Evaluation",
        "Methods (5 baselines)"
      ],
      "estimated_length": "~1 page",
      "new_citations_needed": [
        "penedo_2024_fineweb",
        "yang_2025_qwen3"
      ],
      "labels": [
        "sec:experiments"
      ],
      "cross_refs": [
        "sec:method"
      ]
    },
    "section5_results": {
      "structure": [
        "Main Comparison (Table 1)",
        "Sensitivity Analysis: τ sweep (Table 2) + n_min"
      ],
      "estimated_length": "~1.3 pages + 2 tables (~0.5 page) ≈ 1.5 pages total",
      "tables": {
        "tab:main": "5 methods × 3 seeds, ESS-only/Golden Ratio seed42 only",
        "tab:tau": "6 τ values with PPL, Δ_unif, mean b*"
      },
      "labels": [
        "sec:results",
        "tab:main",
        "tab:tau"
      ],
      "cross_refs": [
        "sec:method",
        "sec:algorithm",
        "app:grid"
      ],
      "forward_refs_needed": [
        "app:grid (grid-b full sweep appendix)"
      ]
    },
    "number_harmonization": {
      "decision": "Used registry 3dp values for cross-table consistency",
      "uniform_seed42": "17.694 (consistent with τ sweep reference)",
      "adaptive_seed42": "17.653 (consistent with τ=0.80 row)",
      "key_claims": [
        "Adaptive mean 17.651 vs Grid-best mean 17.646: gap ≤0.007 per seed",
        "ESS-only 17.728: +0.034 worse than uniform",
        "Golden Ratio 17.654: adaptive within 0.001",
        "τ ∈ [0.5, 0.8] all beat uniform; τ=0.8 recommended default",
        "n_min=1 degrades to 17.789; n_min=2,3 stable"
      ]
    },
    "deferred_to_appendix": [
      "Full grid-b sweep (app:grid)",
      "seed456 b≥1.5 checkpoint artifact note"
    ],
    "missing_data_noted": [
      "ESS-only seed123/456 in progress",
      "n_min=4 running"
    ],
    "binding_analysis": "Already in method.tex §3.3; results.tex references it, adds b* distribution stats (median 0.87, IQR [0.54,1.51])"
  }
}
```

</details>

---
