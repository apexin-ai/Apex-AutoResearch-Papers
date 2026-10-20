# eval plan002 b01 s42 reeval h8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-b01-s42-reeval-h8_20260515T124623_result.json`
- **Structured JSON:** [`643939c61ef70ce91df5.json`](../../sessions/64/643939c61ef70ce91df5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总：

## 产出

### 1. s42 H8 re-eval 结果

| 指标 | Pre-H8 | Post-H8 | Δ |
|------|--------|---------|---|
| H7 (single prem=concl) | 13/81 (16.1%) | 13/81 (16.1%) | — |
| H1 (multi-prem embed) | 42/81 (51.9%) | 42/81 (51.9%) | — |
| **H8 (conjunction collapse)** | — | **12/81 (14.8%)** | **+12** |
| Content-independent | — | 19/81 (23.5%) | — |
| **Genuine** | **26/81 (32.1%)** | **14/81 (17.3%)** | **-12** |

H8 典型模式：conclusion = P1 ∧ P2（premises 的 top-level conjunction），Prover9 trivially 成立。genuine_rate 几乎腰斩。

### 2. s43/s44 H8 回溯状态

**无法执行。** 两者的 checkpoint 和 eval 文件均已从磁盘删除（含 backup 目录），无残留文件可供 classify_h7 运行。

- **s43**: Registry 记录 100% proved 样本仅 1 premise、97% premise=conclusion（全量 H7）。H8 不适用于单 premise 情况，即使有 eval 文件 H8 count 也为 0。
- **s44**: Registry 记录 conclusion duplication hacking（ISR=0.902, 65% ISR=1.0）。有 multi-premise 样本，H8 可能非零，但无 eval 文件无法验证。

### 3. Registry 已更新

plan002-additive-b01-s42 的 metrics 和 notes 已更新为含 H8 的完整分类结果。

### 4. H8 修正前后对比

genuine_rate: **0.321 → 0.173**（降幅 46%）。ISR β=0.1 additive bonus (s42) 的 "genuine" proofs 进一步缩水，82.7% proved 样本存在某种 hacking pattern（H7+H1+H8）。这进一步削弱 Claim 2 "genuine structural guidance"。

---
