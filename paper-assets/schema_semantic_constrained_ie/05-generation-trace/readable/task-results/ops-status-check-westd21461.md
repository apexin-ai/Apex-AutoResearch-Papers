# ops status check westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd21461_20260516T053814_result.json`
- **Structured JSON:** [`2092b21de75e3c80c224.json`](../../sessions/20/2092b21de75e3c80c224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-21461 状态汇总

| 实验 | GPU | PID | --mode | --dataset | 进度 | 状态 |
|------|-----|-----|--------|-----------|------|------|
| w6_mistral_docred_unconstrained | GPU 0 (90%, 15.3/97.9GB) | 7740 | `unconstrained` | `docred` | 49/998 (5%) | 运行中 |
| w6_mistral_docred_constrained | GPU 1 (86%, 15.3/97.9GB) | 8347 | `full_s1` | `docred` | 10/998 (1%) | 运行中（刚启动） |

### 关键回答

1. **PID 7813 已不存在**（被成功 kill）— 原先跑的什么无法追溯
2. **DocRED constrained 新进程已在跑** — PID 8341(bash wrapper) → PID 8347(python3)，`CUDA_VISIBLE_DEVICES=1`，`--mode full_s1 --dataset docred`，输出到 `w6_mistral_docred_constrained.jsonl`
3. **每个 GPU 恰好一个实验**，无冲突
4. `w6_mistral_scierc_constrained.jsonl` 尚未创建（实验未启动）

---
