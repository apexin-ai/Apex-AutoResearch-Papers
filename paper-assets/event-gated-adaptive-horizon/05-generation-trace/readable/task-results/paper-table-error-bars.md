# paper table error bars

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table-error-bars_20260529T075726_result.json`
- **Structured JSON:** [`71704d416f13caa2bf24.json`](../../sessions/71/71704d416f13caa2bf24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无 overfull 警告。

**Table 1 修改汇总：**

| 行 | 原值 | 新值 |
|---|---|---|
| 001 Baseline | 915.7 (s1) | $787.7 \pm 230.8$ (n=4) |
| 008d Factorial | 82.8 @55K (s1), NVE 4.12× | $190.6 \pm 90.2$ (n=5), NVE $3.32 \pm 1.61\times$ |
| 008f No dt_emb | 两行 (s0: 139.5, s1: 468.8) | 合并为一行: $302.4 \pm 134.8$ (n=4), NVE $1.09 \pm 0.42\times$ |
| 008a Unexposed | 777.7 (s0), NVE 0.93× | $820.9 \pm 68.8$ (n=4), NVE $0.46 \pm 0.19\times$ |
| Cheetah trigger | 两行 (010b: 51.7, 078: 119.5) | 合并为一行: $123.2 \pm 132.9$ (n=4), NVE med. 2.3× |

**Table 3 (appendix)**: `tab:cross_env_civo` 已有 mean±std error bars，无需修改。`tab:intervention_hierarchy` 的 Eval(%BL) 列已有 mean±std。

**注意**：Caption 已更新，添加了 footnote $^g$（Cheetah NVE median+range 说明），以及 "Multi-seed entries report mean±std" 说明。NVE 基准仍为 Walker s1 (915.7)。

---
