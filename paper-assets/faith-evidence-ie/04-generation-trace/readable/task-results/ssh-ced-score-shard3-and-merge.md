# ssh ced score shard3 and merge

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ced-score-shard3-and-merge_20260515T050014_result.json`
- **Structured JSON:** [`0f2e956893662b56e93a.json`](../../sessions/0f/0f2e956893662b56e93a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Shard 3 CED 打分已在 GPU 3 启动（5272 条记录，659 docs）。4 个 shard 全部在跑：

| Shard | GPU | PID | 记录数 | 进度 |
|-------|-----|-----|--------|------|
| 0 | 0 | 160921 | 5560 | 刚启动 |
| 1 | 1 | 156417 | 5552 | 2500/5552 (~45%) |
| 2 | 2 | 156591 | 5568 | 2500/5568 (~45%) |
| 3 | 3 | 新启动 | 5272 | NLI 模型已加载 |

Shard 1/2 预计 ~20 分钟完成，shard 0/3 预计 ~40 分钟。2.5 分钟后自动轮询。

---
