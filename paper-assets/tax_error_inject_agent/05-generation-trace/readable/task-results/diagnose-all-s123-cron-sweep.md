# diagnose all s123 cron sweep

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_all-s123-cron-sweep_20260516T151948_result.json`
- **Structured JSON:** [`d8f451983b4242d0199f.json`](../../sessions/d8/d8f451983b4242d0199f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 cron 已不存在（之前已被清除）。

---

## S123 Eval 结果汇总

### 已完成 ✓

| Experiment | Type | Success Rate | Recovery Rate | Detection Rate | Episodes |
|---|---|---|---|---|---|
| **vanilla-s123-clean** | clean | 0.723 | — | — | 47 |
| **vanilla-s123-eval** | injected | 0.702 | 0.702 | 0.213 | 47 |
| **random-s123-clean** | clean | 0.766 | — | — | 47 |

**vanilla-s123 injected by operator:**

| Operator | Total | Recovery Rate | Detection Rate |
|---|---|---|---|
| C1_context_truncation | 12 | 0.750 | 0.083 |
| C4_observation_masking | 11 | 0.727 | 0.364 |
| P1_step_order_swap | 12 | 0.667 | 0.333 |
| P2_sub_goal_deletion | 12 | 0.667 | 0.083 |

### 仍在运行中 (GPU 0-2 active, ~87-89% util)

| Process | GPU | PID | Started | Est. progress |
|---|---|---|---|---|
| taxei-s123-clean | cuda:2 | 291995 | 23:03 | ~17 min elapsed |
| taxei-s123-injected | cuda:0 | 293496 | 23:07 | ~13 min elapsed |
| random-s123-injected | cuda:1 | 294869 | 23:14 | ~6 min elapsed |

### Registry 操作
- `llama31-random-s123-clean`: 修复 conclusion→success，补充 metrics ✓
- `llama31-random-s123-eval`: QUEUED→RUNNING ✓
- `llama31-taxei-s123-clean/eval`: 状态机不允许 DONE→RUNNING，待进程完成后更新 metrics+conclusion
- Cron：全部已不存在，无需清理

### 下一步
3 个进程预计 20-40 分钟内完成（基于 vanilla 的执行时间参考）。完成后需要再次检查结果文件并更新 registry 中 taxei-s123-clean、taxei-s123-eval、random-s123-eval 的 metrics 和 conclusion。

---
