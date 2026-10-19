# fix cqa1 max3 concurrent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-max3-concurrent_20260526T031559_result.json`
- **Structured JSON:** [`0ddbbdab0524bcc419fd.json`](../../sessions/0d/0ddbbdab0524bcc419fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cqa1-32758 当前状态已经符合要求：

**只有 3 个进程在跑（全部是最高优先级的 π0.5 τ-sweep Goal s42）：**

| tmux session | GPU | 实验 | τ |
|---|---|---|---|
| `pi05-tau050` | 0 | π0.5 adaptive Goal s42 | 0.50 |
| `pi05-tau070` | 1 | π0.5 adaptive Goal s42 | 0.70 |
| `pi05-tau090` | 2 | π0.5 adaptive Goal s42 | 0.90 |

GPU 3-5 空闲，无 SmolVLA 残留进程。

**不需要 kill 任何实验** — 另外 3 个（K=2 mean baseline、Adaptive Object、Adaptive Long）没有在这台机器上运行。已经满足 max-3-concurrent 规则。

需要我查一下那另外 3 个实验是否在 registry 中有记录需要更新状态？

---
