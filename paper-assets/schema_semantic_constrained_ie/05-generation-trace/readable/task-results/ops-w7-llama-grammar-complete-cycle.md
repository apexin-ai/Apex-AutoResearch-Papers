# ops w7 llama grammar complete cycle

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w7_llama_grammar_complete_cycle_20260516T074809_result.json`
- **Structured JSON:** [`c570914e1769ba2295f4.json`](../../sessions/c5/c570914e1769ba2295f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## Part 1: w7_llama_scierc_ft_grammar_only Metrics

| 指标 | 值 |
|------|-----|
| Samples | 551/551 (0 parse failures) |
| ET% | **0%** |
| RV% | **0%** |
| DR% | **1.11%** (12/1082) |
| CF% | **0%** |
| E_F1 | 0.6776 (P=0.6647, R=0.691) |
| R_F1 | 0.4545 (P=0.432, R=0.4795) |

符合预期：grammar_only 不约束 DR（与 unconstrained FT 的 DR≈1.11% 一致），ET/RV/CF 全部清零。

## Part 2: Registry

w7_llama_scierc_ft_grammar_only → **DONE / success**，metrics 已写入。

## Part 3: w7_llama_scierc_ft_semantic_only

- 已提交到 tmux session `w7_llama_ft_semantic`，cuda:0
- **PID: 344026**，模型已加载，正在推理
- Registry: PREPARING → QUEUED → **RUNNING**

## Part 4: Cron

已注册 12 分钟周期监控（job `17f6b8e3`），完成后自动收尾。

---
