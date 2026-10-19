# diagnose seed8 ood precollapse result

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed8_ood_precollapse_result_20260521T214401_result.json`
- **Structured JSON:** [`262ca69ed3cf7c236ae7.json`](../../sessions/26/262ca69ed3cf7c236ae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp029_seed8_ood_precollapse 完成，registry 已更新至 DONE。**

结果汇总：

| Metric | Value |
|--------|-------|
| OOD success rate | **11.94%** |
| pass@1 | 11.94% |
| action_is_valid | 57.54% |
| num_actions | 44.92 |
| response_length | 6503 |

OOD 横向对比（pre-collapse vs 其他 seed）：

| Checkpoint | OOD Success |
|-----------|-------------|
| SFT baseline | 5.97% |
| Seed 3 | 10.45% |
| **Seed 8 pre-collapse (step 5)** | **11.94%** |
| Seed 1 | 23.88% |
| Seed 5 | 29.10% |
| Seed 6 | 29.10% |

Seed 8 pre-collapse 的 OOD 泛化能力（11.94%）略高于 SFT 和 Seed 3，但远低于 Seed 1/5/6。结合这是 step 5（训练早期、崩溃前）的 checkpoint，说明 seed 8 在崩溃前 OOD 能力处于中等偏下水平。

tmux session 无残留，进程已完全退出。

---
