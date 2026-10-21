# analysis 018 figures

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_018-figures_20260516T124339_result.json`
- **Structured JSON:** [`cc9962915bae0b7b8b09.json`](../../sessions/cc/cc9962915bae0b7b8b09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成的产出：

**文件** (`figures/paper/`):
- `018_eval_comparison.pdf` / `.png` — 学习曲线对比图
- `018_nve_comparison.pdf` / `.png` — NVE 轨迹图
- `018_summary.json` — 机器可读结果

**`plot_018_results.py` 不存在**，已跳过。

---

**018_summary.json 完整内容：**

```json
{
  "experiment": "018_full_sgs",
  "nve_threshold": 1.5,
  "min_consecutive_checkpoints": 2,
  "verdict_018": "CIVO_ABSENT",
  "verdict_detail": "NVE always <= 1.5x (max 1.000x)",
  "interpretation": "gradient-level: Full-SGS eliminates CIVO",
  "summaries": [
    {"exp_id": "018", "peak_eval": 915.67, "final_eval": 915.67, "max_NVE": 1.0, "CIVO_verdict": "CIVO_ABSENT"},
    {"exp_id": "008d", "peak_eval": 167.22, "final_eval": 82.75, "max_NVE": 4.1292, "CIVO_verdict": "CIVO_PRESENT"},
    {"exp_id": "008f", "peak_eval": 503.21, "final_eval": 503.21, "max_NVE": 1.0198, "CIVO_verdict": "CIVO_ABSENT"},
    {"exp_id": "016e", "peak_eval": 326.67, "final_eval": 69.03, "max_NVE": 10.4166, "CIVO_verdict": "CIVO_PRESENT"},
    {"exp_id": "baseline", "peak_eval": 970.41, "final_eval": 970.41, "max_NVE": 1.0, "CIVO_verdict": "CIVO_ABSENT"}
  ],
  "nve_trajectories": {
    "018": {"5000": 1.0, "15000": 1.0, "25000": 1.0, "35000": 1.0, "45000": 1.0, "55000": 1.0, "65000": 1.0, "75000": 1.0, "85000": 1.0, "95000": 1.0, "105000": 1.0},
    "008d": {"5000": 0.797, "15000": 0.846, "25000": 1.773, "35000": 1.705, "45000": 2.093, "55000": 4.129},
    "008f": {"5000": 0.810, "15000": 0.633, "25000": 1.020, "35000": 0.728, "45000": 0.832, "55000": 0.970, "65000": 0.367, "75000": 0.422, "85000": 0.649, "95000": 0.535, "105000": 0.297},
    "016e": {"5000": 0.797, "15000": 0.851, "25000": 1.857, "35000": 1.283, "45000": 1.401, "55000": 1.863, "65000": 0.834, "75000": 0.809, "85000": 1.200, "95000": 10.417, "105000": 3.804},
    "baseline": {"5000": 1.0, ... "505000": 1.0}
  }
}
```

**核心结论**: Exp-018 (Full-SGS, 93% gradient detach) verdict = **CIVO_ABSENT**，NVE 恒为 1.0。CIVO 是 gradient-level 现象——obs decoder 梯度是 CIVO 的必要条件，Paper claim C2 strengthened。

---
