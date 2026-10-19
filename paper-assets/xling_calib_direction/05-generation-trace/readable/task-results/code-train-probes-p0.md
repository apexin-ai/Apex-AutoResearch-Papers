# code train probes p0

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train-probes-p0_20260521T070213_result.json`
- **Structured JSON:** [`7df8700d7f6209ba228e.json`](../../sessions/7d/7df8700d7f6209ba228e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已完成并通过验证：

**`code/train_probes.py`** (500 行):
- 自动检测 3 种激活格式 (npy/pt_split/pt_flat)
- LR + MLP 两种 probe
- 5 种 transfer conditions (zero_shot, mean_shift, procrustes, few_shot_25/100) + CaCLR placeholder
- 完整评估: AUROC (decision_function), SB-ECE (15 bins), Brier, bootstrap CI, paired permutation test, Cohen's d
- Hewitt & Liang control task + selectivity
- Spearman ρ (depth vs ZS AUROC) + Pareto 分析
- 输出: `results/{model}/` 下的 probes/, metrics/ (5 个 JSON), report.txt

**`code/run_p0.sh`** (51 行):
- conda 环境激活 + 错误处理 (set -euo pipefail)
- Step 1: extract_activations.py (GPU) → Step 2: train_probes.py (CPU)
- 日志重定向到 `logs/`

---
