# code d146 eval final check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-eval-final-check_20260520T032447_result.json`
- **Structured JSON:** [`bfbf55428ef4d73a215d.json`](../../sessions/bf/bfbf55428ef4d73a215d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 Eval/Classify 状态

**6/7 完成，isr_s44 仍在运行（eval 阶段 ~51/100）。**

| 实验 | proved | genuine | genuine_rate | H1 (CE) | H7 (TS) | H8 (PG) | CI |
|------|--------|---------|-------------|---------|---------|---------|-----|
| **base** | 16 | 16 | **100%** | 0 | 0 | 0 | 0 |
| **exec_s42** | 99 | 0 | **0%** | 0 | 99 (TS strict) | 0 | 0 |
| **exec_s43** | 63 | 32 | **50.8%** | 31 (CE) | 0 | 0 | 0 |
| **exec_s44** | 72 | 1 | **1.4%** | 71 (CE) | 0 | 0 | 0 |
| **isr_s42** | 46 | 46 | **100%** | 0 | 0 | 0 | 0 |
| **isr_s43** | 56 | 17 | **30.4%** | 39 (CE) | 0 | 0 | 0 |
| **isr_s44** | — | — | — | — | — | — | — |

### GPU
- 16401 MiB used, 70% utilization (isr_s44 eval running)

### 关键观察
- **Exec-only** 几乎全部 hacking：s42 全量 TS (99/99)，s44 几乎全量 CE (71/72)，s43 一半 CE
- **ISR** 显著更干净：s42 全量 genuine (46/46)，s43 仍有 CE 但 genuine 率 30%
- Base model 16 个 proved 全部 genuine（无 hacking 能力）
- 无 summary 文件，isr_s44 的 eval_sta_results.json 也尚未生成（eval 还在跑）

预计 isr_s44 还需 ~4-5 分钟完成 eval + classify。

---
