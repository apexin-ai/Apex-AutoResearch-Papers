# infra data migration westb to westd

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_data-migration-westb-to-westd_20260521T050229_result.json`
- **Structured JSON:** [`5132b32446a5bc5b1555.json`](../../sessions/51/5132b32446a5bc5b1555.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**迁移完成汇报**

| 目录/文件 | westb-13313 (源) | westd-18266 (目标) | 状态 |
|---|---|---|---|
| alfworld_data/ | 2.2G | 2.2G | ✅ |
| models/ | 115G | 144G* | ✅ |
| simgate-modular-routing/ | 11G | 11G | ✅ |
| episodes_full_FINAL.jsonl.gz | 11,507,105,718 bytes | 11,507,105,718 bytes | ✅ |
| episodes_slim_FINAL.jsonl | 28,782,838,545 bytes | 28,782,838,545 bytes | ✅ |
| recovery_episodes_full.jsonl.gz | 7,564,770,674 bytes | 7,564,770,674 bytes | ✅ |
| .hf_cache/ | ✓ | ✓ | ✅ |
| .autodl/ | ✓ | ✓ | ✅ |

*models/ 目标端比源端大 29G，因为 Meta-Llama-3.1-8B-Instruct 目录在源端是硬链接（du 显示 18M），rsync 没加 `-H` 参数将其展开为完整文件。数据完整性无影响。

- **传输总量**: 138.6 GB (压缩)，实际 200.3 GB
- **平均速度**: 238 MB/s
- **westd-18266 剩余空间**: 50G (250G 中已用 201G)
- **westb-13313 数据未删除**，可安全释放

---
