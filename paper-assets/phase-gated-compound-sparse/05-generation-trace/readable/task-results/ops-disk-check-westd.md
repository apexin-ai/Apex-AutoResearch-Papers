# ops disk check westd

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_check_westd_20260517T021605_result.json`
- **Structured JSON:** [`8c8f4bde7cf31b2e311d.json`](../../sessions/8c/8c8f4bde7cf31b2e311d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 项目 | 数值 |
|------|------|
| `/root/autodl-tmp` 总空间 | 250G |
| 已用 | 112G |
| 可用 | **139G** |
| 使用率 | 45% |
| pacs 项目总占用 | 27G |
| 模型目录 (`/root/autodl-tmp/models/`) | 86G |
| 单个 GPQA 条件（s015，已完成） | **40M** |

**结论：能跑。**

每个 GPQA 条件约 40MB，4-5 个条件总计 ~200MB。可用空间 139G，完全不构成瓶颈。

注：其余 4 个 GPQA profiling 目录（s020/s025/s030/random_s020）大小为 0，看起来尚未跑完或只创建了空目录。

---
