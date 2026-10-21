# harvest eval pi05 attention k05 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_attention_k05_goal_seed43_20260523T225557_result.json`
- **Structured JSON:** [`4187ea23c18da46963d4.json`](../../sessions/41/4187ea23c18da46963d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No cron to delete (not in this session). Registry is updated.

## 结果报告

**eval_pi05_attention_k05_goal_seed43** — DONE (negative)

| Experiment | SR | Episodes |
|---|---|---|
| Attention k=0.5 Goal **seed42** | 70.2% | 500 |
| Attention k=0.5 Goal **seed43** | **72.2%** | 500 |
| Attention k=0.5 Goal **mean** | **71.2%** | — |
| Random k=0.5 Goal seed42 | 73.6% | 500 |

**结论：negative。** 双 seed 均低于 Random baseline（seed42: -3.4pp, seed43: -1.4pp, mean: -2.4pp）。Attention-based importance 对 π0.5 MLP connector 持续 anti-informative，不是 seed 噪声。

**D185 crossover 确认：**
- X-VLA（cross-attention connector）: attention importance 有效
- π0.5（MLP connector）: attention importance anti-informative → MLP connector 隐藏了 token-level attention signal

**westd-41074 GPU 0 已空闲**（1 MiB used），可分配新任务。GPU 1/2/3 仍被占用。

---
