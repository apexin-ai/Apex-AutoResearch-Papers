# fix oh fewshot retrain

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_oh-fewshot-retrain_20260514T224451_result.json`
- **Structured JSON:** [`d7480ba3d1c3f71ed88a.json`](../../sessions/d7/d7480ba3d1c3f71ed88a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**实验完成总结：**

修复 OH 标签后 few-shot probe 结果：

| 配置 | Macro-F1 | F1(stag) | F1(prog) |
|------|----------|----------|----------|
| Zero-shot | 0.5984 | 0.3074 | 0.8895 |
| 5% (118 inst) | 0.8503 | 0.7641 | 0.9366 |
| 10% (237 inst) | 0.9179 | 0.8683 | 0.9675 |
| 20% (475 inst) | 0.9475 | 0.9159 | 0.9791 |
| 50% (1187 inst) | 0.9682 | 0.9487 | 0.9878 |

关键发现：标签质量是瓶颈而非数据量。新 5% 数据（0.850）已超过旧 50%（0.688），新 10%（0.918）已超过 SWE in-domain（0.906）。

---
