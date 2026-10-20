# exp temp curve parallelize

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_temp-curve-parallelize_20260517T225505_result.json`
- **Structured JSON:** [`b2cf1af87f874101f442.json`](../../sessions/b2/b2cf1af87f874101f442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**并行化无法执行 — 容器只有 1 块 RTX 5090。**

### 实际状态

| Session | 任务 | 进度 | GPU | 速度 |
|---------|------|------|-----|------|
| `tc_fix` | Pythia-2.8B t=0.5 p=0.9 (Job 1/3) | 113/995 (11%) | cuda:0 | ~14.1s/seed |
| `indep_seed` | Pythia-2.8B indepA | 70/500 (14%) | cuda:0 | ~12.9s/seed |

两个实验共享同一块 GPU（显存 12.4GB/32.6GB，利用率 92%）。`tc_fix` 脚本本身就是 3 个 job 串行 + 3 个 feature extraction 串行，全在 `cuda:0`。

### 时间预估（当前双进程共享）

- `indep_seed` 剩余：(500-70) × 12.9s ≈ **1.5h**
- `tc_fix` Job 1 剩余：(995-113) × 14.1s ≈ **3.5h**
- `tc_fix` Job 2+3（Pythia t=0.9 + Qwen t=0.9）：串行排在 Job 1 之后，预计额外 **~5h**
- 总计 `tc_fix` 全部完成（含 feature extraction）：**~10h+**

### 可选方案

1. **保持现状** — 两个实验共享 GPU，tc_fix ~10h 跑完全部 3 个 job
2. **暂停 indep_seed，让 tc_fix 独占 GPU** — 单进程可能快 20-30%（~8h），但 indep_seed 进度丢失
3. **等 indep_seed 跑完（~1.5h）后 tc_fix 独占** — tc_fix 总计 ~9h，但 indep_seed 不受影响
4. **升级容器到多 GPU 实例** — 真正的并行化方案

如何处理？

---
