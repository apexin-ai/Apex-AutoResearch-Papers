# ssh plan010 libero spatial

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan010-libero-spatial_20260516T020355_result.json`
- **Structured JSON:** [`9d11100f05b3a7c79c65.json`](../../sessions/9d/9d11100f05b3a7c79c65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认：**LIBERO-Spatial 数据不在服务器上。**

服务器上有的 LIBERO 数据：
- `libero_goal/` — 10 tasks（已完成分析）
- `libero_10/` — 10 tasks（LIBERO-Long，长时域多步任务）
- `libero_90/` — 90 tasks（预训练集）

没有 `libero_spatial/` 或 `libero_object/`。服务器无外网，无法下载。

**可行替代方案：** 用 `libero_10`（LIBERO-Long）作为第二个 benchmark。它有 10 个来自不同场景（kitchen/living room/study）的长时域任务，任务结构与 LIBERO-Goal 差异更大（多步操作 vs 单步目标），更能测试 findings 的 generalizability。

是否用 LIBERO-Long（libero_10）替代执行？还是等获取 LIBERO-Spatial 数据后再做？

---
