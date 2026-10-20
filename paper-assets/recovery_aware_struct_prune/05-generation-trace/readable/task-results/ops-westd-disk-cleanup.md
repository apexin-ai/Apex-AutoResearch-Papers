# ops westd disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_20260520T092518_result.json`
- **Structured JSON:** [`96151df3361d46afd396.json`](../../sessions/96/96151df3361d46afd396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘实际上 **并不满**：

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 5.4G | 25G | 18% |
| 数据盘 `/dev/sda2` | 879G | 18G | 817G | 3% |

数据盘有 **817GB 可用空间**，完全不构成阻塞。

不过项目在 `/root/autodl-tmp/recovery_aware_struct_prune/` 占用了 **580GB**，其中 GRPO checkpoint 的 optimizer 状态占了大头。如果你想预防性清理以留出更多空间，我可以列出各 checkpoint 中 optimizer 占用情况。但当前空间充裕（817G free），**30% eval、多种子 GRPO、15% pipeline 等实验不会被磁盘阻塞**。

ROADMAP 中的 P0 blocker 可能是旧信息（可能指已宕机的 westd-11672），建议更新。需要我做预防性清理还是直接标记此任务为已解决？

---
