# diagnose d112 shard1 and shard3 status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d112_shard1_and_shard3_status_20260519T025945_result.json`
- **Structured JSON:** [`cc61cbf4ed22ad8f28ad.json`](../../sessions/cc/cc61cbf4ed22ad8f28ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| Shard | 行数 | 状态 |
|-------|------|------|
| 0 | 6048 | 完成 |
| 1 | 6048 | 完成 (registry 已更新 success) |
| 2 | 6048 | 完成 |
| 3 | 5696/6048 | 进行中 (94.2%) |

**总行数**: 23840 / 24192，还差 shard 3 的 352 行（44 docs）。

**GPU 状态**:

| GPU | 显存 | 状态 |
|-----|------|------|
| cuda:0 | 18132/32607 MiB | 占用 (PID 590568) |
| **cuda:1** | **0/32607 MiB** | **空闲** (shard 1 完成已释放) |
| cuda:2 | 29110/32607 MiB | 占用 (PID 601718) |
| cuda:3 | 18882/32607 MiB | 占用 (PID 598911) |

**Step 2 CED scoring 脚本**已就绪，通过 `GPU=X bash step2_ced_score.sh` 启动，使用 NLI-DeBERTa 打分 + top_k=1 筛选。shard 3 完成后即可在 cuda:1 上启动。

---
