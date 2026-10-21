# ssh autodl cuda2 w7 check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_cuda2_w7_check_20260523T040544_result.json`
- **Structured JSON:** [`df9451227b11a5a5cf5a.json`](../../sessions/df/df9451227b11a5a5cf5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

**1. cuda:2 上无进程在跑**
- 全部 4 张 GPU（RTX PRO 6000 Blackwell 96GB）显存占用均为 0 MiB，利用率 0%。cuda:2 完全空闲。
- `/proc/*/comm` 中无任何 ablation 相关进程。

**2. W7 结果文件状态**
- 4 个结果 CSV 文件，每个 81 行（含 header = 80 条数据），大小均为 9958 bytes：
  - `results_w7_ablation.csv` — 最后修改 May 23 08:44
  - `results_w7_ablation_original_20seeds.csv` — May 23 09:12
  - `results_w7_ablation_partial.csv` — May 23 08:44
  - `results_w7_ablation_partial_backup.csv` — May 23 09:12

**3. 结论：W7 rerun 已终止，无残留进程。** GPU 完全空闲，结果文件自今早 09:12 后未再更新，与 registry 中 DONE/success 状态一致。

---
