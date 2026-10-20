# diag check running experiments

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check-running-experiments_20260514T145754_result.json`
- **Structured JSON:** [`9351fc0ed9a7aed451c1.json`](../../sessions/93/9351fc0ed9a7aed451c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已完成，进程已退出，GPU 空闲。

---

### 1. data-scaling-v2 — **done** (EXIT_CODE=0)

| Ratio | Instances | Windows | Val F1 | Test F1 | Test Acc |
|-------|-----------|---------|--------|---------|----------|
| 10% | 138 | 1,107 | 0.8393 | 0.8054 | 0.8514 |
| 25% | 346 | 2,749 | 0.8970 | 0.8203 | 0.8640 |
| 50% | 693 | 5,715 | 0.9259 | 0.8715 | 0.9030 |
| 100% | 1,386 | 10,634 | 0.9511 | **0.9055** | **0.9282** |

结果已保存至 `/root/autodl-tmp/agent_progress_probe/data/data_scaling_results.json`

---

### 2. ablation-lf-holdout-v2 — **done** (EXIT_CODE=0)

| Excluded LF | conf≥2 | macro_f1 | accuracy |
|---|---|---|---|
| command_repetition | 2,801 | 0.9563 | 0.9665 |
| file_diff_delta | 3,941 | 0.9178 | 0.9267 |
| outcome_backpropagation | 10,243 | 0.9510 | 0.9763 |
| **(baseline: all 3 LFs)** | 15,401 | **0.9050** | — |

结果已保存至 `/root/autodl-tmp/agent_progress_probe/lf_holdout_results.json`

---

### GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| cuda:0 | 0% | 0 / 32,607 MiB |
| cuda:1 | 0% | 0 / 32,607 MiB |

两块 GPU 完全空闲，可用于下一轮实验。

---
