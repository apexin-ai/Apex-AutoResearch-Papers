# code fill 35694 3gpu now

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fill-35694-3gpu-now_20260521T103650_result.json`
- **Structured JSON:** [`088f3a4d73cd92e93a20.json`](../../sessions/08/088f3a4d73cd92e93a20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在顺利推进：
- **contam_15** (GPU 3): 276/948 steps (29%), ~12 分钟剩余
- **clean_s2** (GPU 1): 125/939 steps (13%), ~13 分钟剩余

---

## 当前状态汇总

### 4/4 GPU 全部在用

| GPU | 任务 | 进度 |
|-----|------|------|
| 0 | pilot clean_s10 eval (MMLU 14K items) | 运行中，预计 1-2h |
| 1 | ARC-C clean_s2 train | 13% (125/939 steps) |
| 2 | GRPO training（原有） | 持续运行 |
| 3 | ARC-C contam_15 train | 29% (276/948 steps) |

### 已收集结果

**MIA SFT 结果：**
- loss AUC-ROC = 0.592
- min_k_10 AUC-ROC = 0.611（最优）
- min_k_pp_10 AUC-ROC = 0.569

**ARC-C clean_s1 eval：**
- acc_overall = 0.8949
- theta_MLE = 0.6872
- lz* = -5.5107

### 待办
- s10 eval 完成后 → GPU 0 启动 ARC-C contam_50 训练
- contam_15 和 clean_s2 训练各约 12-15 分钟完成

---
