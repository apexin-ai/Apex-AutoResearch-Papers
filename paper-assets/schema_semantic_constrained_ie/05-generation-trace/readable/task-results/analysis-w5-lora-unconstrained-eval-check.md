# analysis w5 lora unconstrained eval check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_lora_unconstrained_eval_check_20260515T155407_result.json`
- **Structured JSON:** [`addb05d973eea5931760.json`](../../sessions/ad/addb05d973eea5931760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

## W5 LoRA Unconstrained Eval — 完成

### Violation 指标

| 指标 | 值 |
|------|-----|
| JSON Parse Rate | 100% |
| Entity Type (ET%) | 0% |
| Relation Vocab (RV%) | 0% |
| **Domain/Range (DR%)** | **1.95% (22/1128)** |
| Cross-Field (CF%) | 0% |

### Quality 指标

| 指标 | P | R | F1 |
|------|---|---|-----|
| Entity | 0.652 | 0.690 | **0.671** |
| Relation | 0.409 | 0.473 | **0.439** |

### DR 热点

`Evaluate-for` 关系违规最严重：13.1% (13/99)，其次 `Part-of` 5.8%、`Compare` 5.0%。

### DR Gate 判断

**DR = 1.95% < 2% → GATE FAILED — 暂停，需报告 Director。**

LoRA 微调已将 DR 压到 gate 阈值以下，假设（unconstrained 仍 >2% 需要 constrained decoding）不成立。

### GPU 状态

- GPU 0: 空闲 (0 MiB)
- GPU 1: 17.4 GB 被 PID 276937 占用 — 是 `run_constrained_ext` 进程（已运行 ~51 min），不是之前的 eval

---
