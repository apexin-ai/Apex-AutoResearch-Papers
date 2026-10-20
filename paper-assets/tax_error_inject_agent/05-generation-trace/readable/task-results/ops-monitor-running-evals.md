# ops monitor running evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-running-evals_20260514T214146_result.json`
- **Structured JSON:** [`b1d226bb20ae6fdbaf9c.json`](../../sessions/b1/b1d226bb20ae6fdbaf9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE。

## 汇总

| | v4-random-recovery-eval | v4-taxei-recovery-eval-r2 |
|---|---|---|
| **状态** | DONE | DONE |
| **Recovery rate** | **0.638** (30/47) | **0.596** (28/47) |
| **Detection rate** | 0.0 | 0.0 |
| **C1_context_truncation** | 8/12 (0.667) | 8/12 (0.667) |
| **C4_observation_masking** | 6/11 (0.545) | 7/11 (0.636) |
| **P1_step_order_swap** | 9/12 (0.750) | 7/12 (0.583) |
| **P2_sub_goal_deletion** | 7/12 (0.583) | 6/12 (0.500) |

**GPU 状态**：4 张 RTX 5090 全部空闲（0MiB / 0% util），无运行进程。

Random SFT 的 recovery rate (0.638) 略高于 TaxEI SFT (0.596)。两者的 detection rate 均为 0——模型在 think 分析中未显式检测到注入的错误。

---
