# eval cuda3 serial queue

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda3_serial_queue_20260520T035855_result.json`
- **Structured JSON:** [`29f1a0a7b8ac99ff1e88.json`](../../sessions/29/29f1a0a7b8ac99ff1e88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个 eval 已完成，registry 已更新。汇总结果：

| Checkpoint | Loss | PPL |
|---|---|---|
| ngram_uniform_seed42 | 2.8733 | **17.69** |
| contamination_60_ess_only_seed123 | 2.8771 | 17.76 |
| contamination_60_ess_only_seed456 | 2.8771 | 17.76 |
| ngram_adaptive_seed42 | 2.8803 | 17.82 |
| contamination_60_random_seed123 | 2.8832 | 17.87 |
| contamination_60_random_seed456 | 2.8837 | 17.88 |

关键发现：
- **ngram_uniform** PPL 最低 (17.69)，优于 ngram_adaptive (17.82)
- **ESS-only** (17.76) 优于 **random** (17.87/17.88)，两个 seed 结果完全一致
- 所有模型 PPL 差异在 0.19 范围内（17.69-17.88）

---
