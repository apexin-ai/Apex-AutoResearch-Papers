# code app 4pl ablation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_app-4pl-ablation_20260521T015640_result.json`
- **Structured JSON:** [`a286b8b2faaba10f1b82.json`](../../sessions/a2/a286b8b2faaba10f1b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

**服务器端：**
- CSV: `/root/autodl-tmp/irt_personfit_contam/results/appendix_4pl_ablation.csv` (70 rows)
- JSON: `/root/autodl-tmp/irt_personfit_contam/results/appendix_4pl_ablation_summary.json`

**本地 artifacts：**
- `artifacts/4pl_ablation/appendix_4pl_ablation.csv`
- `artifacts/4pl_ablation/appendix_4pl_ablation_summary.json`

**关键结果（4PL vs 3PL power, two-sided α=0.05）：**

| Benchmark | contam | 4PL power | 3PL power | Δ |
|-----------|--------|-----------|-----------|---|
| MMLU (14042) | 15% | **0.969** | 0.412 | +0.557 |
| HellaSwag (10042) | 15% | **0.656** | 0.313 | +0.343 |
| GSM8K (1319) | 15% | **0.492** | 0.285 | +0.207 |
| ARC-C (295) | 15% | 0.087 | 0.071 | +0.016 |
| HumanEval (164) | 15% | 0.197 | 0.120 | +0.077 |

4PL 在所有 benchmark 和所有 contamination level 上均优于 3PL，差距随 benchmark size 和 contamination level 增大而增大。100% contamination 下两者均 power=1.0（两侧检验拒绝，因 lz* 极端正值）。无 NaN。

---
