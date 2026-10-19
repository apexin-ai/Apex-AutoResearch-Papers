# ssh check westd evals urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_evals_urgent_20260523T024822_result.json`
- **Structured JSON:** [`b16356d17279eb7e9702.json`](../../sessions/b1/b16356d17279eb7e9702.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. seed100 step10 OOD eval (westd, PID 340462) — **COMPLETED**

| Metric | Value |
|--------|-------|
| **pass@1** | **12.69%** |
| action_is_valid | 70.56% |
| num_actions | 44.88 |
| response_length | 7466.4 |
| reward mean@134 | 1.269 |
| best@2 | 2.63 |
| best@4 | 4.57 |
| best@8 | 6.71 |
| best@16 | 8.90 |
| best@32 | 9.84 |
| best@64 | 10.0 |

wandb atexit BrokenPipeError 是无害的清理错误，不影响结果。

---

### 2. seed7 step7 v3 eval (westd, PID 340542) — **CRASHED**

**错误原因**: vLLM 初始化时 cuda:0 显存不足。`Free memory on device cuda:0 (79.36/94.97 GiB) < desired 0.85 * 94.97 = 80.73 GiB`。

推测是 seed100 eval 同时占用了 cuda:0 导致的。指定的是 cuda:3 但 vLLM 仍尝试在 cuda:0 上初始化。现在 GPU 已全部释放，可以重跑。

---

### 3. seed200 step5 OOD eval (bjb1, PID 477932) — **COMPLETED**

| Metric | Value |
|--------|-------|
| **pass@1** | **10.45%** |
| action_is_valid | 61.06% |
| num_actions | 45.5 |
| response_length | 6854.9 |
| reward mean@134 | 1.045 |
| best@2 | 2.15 |
| best@4 | 3.70 |
| best@8 | 5.86 |
| best@16 | 8.22 |
| best@32 | 9.72 |
| best@64 | 10.0 |

---

### GPU 状态
- **westd-47453**: 4 GPU 全部空闲 (0 MiB)，GPU 3 显示 100% utilization（残留，无实际进程）
- **bjb1-17606**: 2 GPU 全部空闲 (0 MiB)

### 待处理
seed7 step7 v3 eval 需要重跑，确保 `CUDA_VISIBLE_DEVICES` 正确设置为 cuda:3 以避免 vLLM 默认抢占 cuda:0。

---
