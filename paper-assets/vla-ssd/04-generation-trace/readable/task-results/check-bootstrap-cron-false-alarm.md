# check bootstrap cron false alarm

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_cron_false_alarm_20260523T002801_result.json`
- **Structured JSON:** [`85fd1578aa2a5402726c.json`](../../sessions/85/85fd1578aa2a5402726c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**假警报确认。** cuda:0 进程正常完成退出，cuda:1 仍在运行。

状态汇总：

| 项 | 状态 |
|---|---|
| GPU 0 | 空闲（0%, 0 MiB）— cuda:0 batch 已于 08:26:35 全部完成 |
| GPU 1 | 运行中（48%, 12623 MiB）— 正在提取 task 6/10, 3400/5000 samples |
| 已完成 JSON | 17 个 |

**cuda:0 已完成的最后一项：** `nora_spatial/untrained` (Peak R²=0.5125 @ L4, Exit R²=0.424 @ L35)

**cuda:1 进度：** 正在处理中（~68% extraction），预计还需数小时完成剩余任务。

缺失结果（待 cuda:1 完成）：
- `tracvla_object/untrained`（当前正在跑）
- `nora_object/trained` + `untrained`
- `tracvla_long/trained` + `untrained`
- `nora_long/trained` + `untrained`

无需干预。

---
