# ops urgent status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260519T040641_result.json`
- **Structured JSON:** [`27f967b160e2771c1064.json`](../../sessions/27/27f967b160e2771c1064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 进程 & GPU

| GPU | 实验 | VRAM | Util |
|-----|------|------|------|
| 0 | exp_023_cheetah_baseline_s4 | 4776 MiB | 8% |
| 1 | exp_023_cheetah_baseline_s3 | 4776 MiB | 18% |
| — | exp_001_baseline_s3 | **已完成** | — |

### 实验指标

| 实验 | Task | Seed | 状态 | Step | Target | eval_return @target | peak eval_return (step) | value_mean @final | ve_ratio |
|------|------|------|------|------|--------|---------------------|------------------------|-------------------|----------|
| exp_001_baseline_s3 | Walker Walk | 3 | **完成** | 120K | 105K | 869.03 (@102K) | **898.89** (@112K) | 622.20 | 0.692 |
| exp_023_cheetah_s3 | Cheetah Run | 3 | 运行中 | 204K | 200K | 642.13 (@202K) | **685.93** (@172K) | 445.42 | 0.694 |
| exp_023_cheetah_s4 | Cheetah Run | 4 | 运行中 72% | 144K | 200K | — | **397.60** (@134K) | 280.78 | 0.743 |

**备注：**
- exp_001 的 eval 间隔为 10K，105K 无精确 eval，取最近的 102K
- exp_023_s3 已过目标步数，仍在运行（`--steps 200000` 但 step 计数到 204K）
- exp_023_s4 预计还需 ~1.5h（按 ~10 fps 估算）
- 三个实验 ve_ratio 均在 0.69-0.74，value 普遍高估

---
