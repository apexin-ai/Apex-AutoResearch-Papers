# diagnose d112 shard0 crash

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d112_shard0_crash_20260519T020607_result.json`
- **Structured JSON:** [`f9e31f52eb1649820f41.json`](../../sessions/f9/f9e31f52eb1649820f41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Shard 0：正常完成，不是异常退出。**
- 756 unique docs × 8 generations = 6048 行，全部生成完毕
- 最后写入时间 10:04，cuda:3 已释放（0MiB）
- 日志文件不存在（可能输出到 tmux stdout 而非文件），但无错误
- Registry 已更新为 DONE/success

**其他 3 个 shard 进度：**

| Shard | GPU | PID | 进度 | 预计剩余 |
|-------|-----|--------|------|---------|
| 1 | cuda:0 | 590568 | 542/756 (72%) | ~55 min |
| 2 | cuda:1 | 587729 | ~540/756 (71%) | ~55 min |
| 3 | cuda:2 | 587819 | 471/759 (62%) | ~75 min |

所有 shard 运行正常，shard 0 先完成是因为 resume 模式下它已有部分缓存（468 docs 待处理 vs 其他从头开始）。cuda:3 现在空闲可用。

---
