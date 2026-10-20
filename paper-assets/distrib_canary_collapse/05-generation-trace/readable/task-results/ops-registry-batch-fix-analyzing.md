# ops registry batch fix analyzing

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_batch_fix_analyzing_20260520T193905_result.json`
- **Structured JSON:** [`caf778106de8c0342a3b.json`](../../sessions/ca/caf778106de8c0342a3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部更新完成 ANALYZING → DONE：

| 实验 | conclusion | PermG FDR | K≥3 | K≥4 | 关键修正 |
|------|-----------|-----------|------|------|---------|
| **t20_a100_s42_fp32** | ~~negative~~ → **success** | 6/8 | 6/8 | 6/8 | conclusion 从错误的 negative 修正为 success |
| **t20_a050_s42_fp32** | success（不变） | 6/8 | 6/8 | 2/8 | 补充完整 metrics |
| **data_strategy_ablation_s43** | **negative** | 0/8 | 0/8 | 0/8 | accumulate 策略下检测失效，符合预期 |

---
