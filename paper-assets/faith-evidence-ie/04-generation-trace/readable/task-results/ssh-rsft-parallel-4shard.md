# ssh rsft parallel 4shard

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-parallel-4shard_20260515T013659_result.json`
- **Structured JSON:** [`893906884c170da51781.json`](../../sessions/89/893906884c170da51781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个分片全部正常运行，无 OOM：

| Shard | GPU | Docs | 速度 | 预计耗时 |
|-------|-----|------|------|---------|
| s0 | cuda:0 | 756 | ~14s/doc | ~3h |
| s1 | cuda:1 | 756 | ~19s/doc | ~4h |
| s2 | cuda:2 | 756 | ~12.5s/doc | ~2.6h |
| s3 | cuda:3 | 759 | ~18s/doc | ~3.8h |

总计 3027 文档 × 8 generations，batch_size=1，输出到 `/root/autodl-tmp/rsft_generations/shard_{0-3}/generations.jsonl`。

---
