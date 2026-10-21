# analysis g q progress check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g-q-progress-check_20260520T122052_result.json`
- **Structured JSON:** [`c1382ecc9e2314177103.json`](../../sessions/c1/c1382ecc9e2314177103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据都够了，汇总如下：

---

## 实验进度报告

### 1. G Decoupling (PID 307169)
| 项目 | 值 |
|------|-----|
| 进程状态 | **alive** (运行 2h05m) |
| 当前策略 | conservative (standard 已完成, 3题, acc=66.7%) |
| conservative 进度 | **120 / 204** (58.8%) |
| 当前 accuracy | **57.5%** (69/120) |
| 处理速度 | 0.02 prob/s (~1.2 问题/分钟) |
| ETA | **~87 分钟** (日志报 ETA=5250s) |

注：results.json 只记录已完成的 standard 策略 (3题 pilot)，conservative 策略完成后会更新。

### 2. Q Premise Mutation (PID 314817)
| 项目 | 值 |
|------|-----|
| 进程状态 | **alive** (运行 1h05m) |
| 已完成 | **54 / 204** (26.5%) |
| 速度 | ~0.82 问题/分钟 |
| ETA | **~183 分钟 (~3h)** |

中间结果 (54题, 5种变体):

| Mutation | SC Acc | SICA Acc | SC Flip Rate | SICA Flip Rate |
|----------|--------|----------|-------------|----------------|
| original | 59.3% | 63.0% | — | — |
| synonym | 64.8% | 59.3% | 13.0% | 13.0% |
| reorder | 66.7% | 59.3% | 22.2% | 25.9% |
| inject | 55.6% | 55.6% | 7.4% | 13.0% |
| combined | 57.4% | 55.6% | 22.2% | 20.4% |

reorder 和 combined 的 flip rate 最高 (~22-26%)，说明前提顺序变化对模型推理一致性影响较大。

---
