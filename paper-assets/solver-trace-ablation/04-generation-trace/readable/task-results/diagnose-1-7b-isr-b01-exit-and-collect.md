# diagnose 1 7b isr b01 exit and collect

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_1_7b-isr-b01-exit-and-collect_20260516T221339_result.json`
- **Structured JSON:** [`3378eea0f1ba3d72ca4e.json`](../../sessions/33/3378eea0f1ba3d72ca4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: ISR β=0.1 训练 — 已完成

| 指标 | 值 |
|------|-----|
| global_step | **500/500** |
| 训练时间 | 60 min 20s |
| **Final prove_rate** | **0.5205** |
| **Final mean_isr** | **0.2457** |
| 模型已保存 | checkpoint-500 + final (~6.4GB) |

### Part 2: ISR β=0.3 Eval 结果

| 指标 | 值 |
|------|-----|
| prove_rate | **17/100 = 17.0%** |
| mean_isr | **0.0309** |
| proved_only_mean_isr | 0.1815 |
| elapsed | 727s (~12 min) |

**classify_h7 分类：**

| 类别 | 数量 | 占比 |
|------|------|------|
| H7 (tautology) | 0 | 0.0% |
| H1 (conclusion in premises) | 12 | 70.6% |
| H8 (conj-collapse) | 0 | 0.0% |
| Content-independent | 1 | 5.9% |
| **Genuine** | **5** | **29.4%** |

β=0.3 的 prove_rate 17% 远低于 β=0.1 的 52%，且 70.6% 的 proved 样本属于 H1 hacking（conclusion in premises）。Genuine 只有 5 个。ISR 均值极低 (0.031)，说明β=0.3 模型学到了高度冗余/低 ISR 的证明策略。

---
