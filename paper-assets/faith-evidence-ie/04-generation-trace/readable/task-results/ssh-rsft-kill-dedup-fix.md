# ssh rsft kill dedup fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rsft-kill-dedup-fix_20260515T014732_result.json`
- **Structured JSON:** [`5b5560f1e3fffab18ff8.json`](../../sessions/5b/5b5560f1e3fffab18ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。最终状态：

| GPU | PID | 显存 | Shard | 已处理 docs | 总 docs | 进度 |
|-----|-----|------|-------|------------|---------|------|
| cuda:0 | 135867 | 15,132 MiB | shard_0 (302-984) | 47 / 682 | 682 | 6.9% |
| cuda:1 | 136270 | 12,250 MiB | shard_1 (984-1665) | 49 / 681 | 681 | 7.2% |
| cuda:2 | 136649 | 17,466 MiB | shard_2 (1665-2346) | 50 / 681 | 681 | 7.3% |
| cuda:3 | 137985 | 13,154 MiB | shard_3 (2346-3027) | 6 / 681 | 681 | 0.9% |

执行摘要：
- Set A 4 个旧进程已全部 kill
- Set B 3 个进程确认存活且正常运行
- shard_3 旧数据已备份并清空，新进程已启动
- cuda:3 上的重复进程 (137070) 已发现并清除
- Registry s0-s3 的 PID 已全部更新为 Set B 的正确值
- 无 doc_id 冲突（每个 doc 8 条记录是 `num_generations=8` 的预期行为）

---
