# ops urgent gpu check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-check_20260519T062430_result.json`
- **Structured JSON:** [`a2c12aa3fbd190ac3e85.json`](../../sessions/a2/a2c12aa3fbd190ac3e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态

| GPU | 型号 | VRAM | 利用率 | 进程 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Black | 1MiB / 97887MiB | 0% | 无 |
| 1 | RTX PRO 6000 Black | 9462MiB / 97887MiB | 30% | python ×2 (4757+4671 MiB) |

GPU 0 空闲，GPU 1 有两个 python 进程在跑。

---

## exp_023_cheetah_baseline_s4 — 仍在运行，当前 step 212K

已过 200K，仍在继续。最近 eval 在 step 204K。

| 指标 | 值 |
|------|----|
| eval_return @194K（最近200K附近） | **537.03** |
| eval_return @204K | 301.69 |
| **peak eval_return** | **537.03 @ step 194K** |
| value_mean @204K | 339.14 |
| ve_ratio (value_mean/eval_return) @204K | 339.14 / 301.69 = **1.124** |
| civo/ve_ratio @204K | **1.124** |
| fps | 9.65 |

注意：eval_return 从 194K 的 537 骤降到 204K 的 302，波动较大。value 高估（ve_ratio > 1）。

---

## 其他实验进度

| 实验 | 当前 step | 目标 200K 进度 | 状态 |
|------|-----------|----------------|------|
| exp_001_baseline_s2 | 184K | 92% | 运行中 |
| exp_001_baseline_s4 | 55K | 27.5% | 运行中（刚输出 step 55K 的 header，应在 GPU 1 上） |

---
