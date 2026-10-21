# eval meanpool multiseed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_meanpool-multiseed_20260518T233025_result.json`
- **Structured JSON:** [`a71f4862158a7192758a.json`](../../sessions/a7/a71f4862158a7192758a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完毕。结果已保存到 `results/meanpool_multiseed.json`。

**Mean Pooling (9-class DeBERTa) 3-seed macro F1 汇总：**

| K | DD OOD (mean±std) | ActorAttack (mean±std) |
|---|---|---|
| 1 | 0.9905±0.0134 | 0.8301±0.0272 |
| 2 | 0.9936±0.0090 | 0.9030±0.0229 |
| 3 | 0.9842±0.0160 | 0.9622±0.0076 |
| 5 | 0.9968±0.0045 | 0.9716±0.0153 |
| Full | 0.9905±0.0134 | 0.9623±0.0151 |

DD OOD 上 mean pooling 几乎全部 ≥0.97，和 BiGRU 差距极小。ActorAttack 上 K≥3 后也达到 0.96+，说明对该任务而言 BiGRU temporal modeling 确实不是必需的。

---
