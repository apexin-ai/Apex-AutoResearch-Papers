# diagnose server status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server_status_check_20260521T232339_result.json`
- **Structured JSON:** [`d32ac47da94cd2b87d08.json`](../../sessions/d3/d32ac47da94cd2b87d08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/worker_output_server_status_check.md`。

**摘要：**
- **PID 584349 (cf_batch_missing_v1)** — 运行中，GPU 0。Task 1 (openvla/object/untrained) 已完成，Task 2 (tracvla/spatial/untrained) 进行中 (condition 2/4)。队列共 5 个任务，预估还需 ~100 min。
- **PID 585447 (cf_batch_part2_v1)** — 运行中，GPU 1。Task 1 (tracvla/goal/untrained) 进行中 (condition 3/4)。队列共 2 个任务，预估还需 ~37 min。
- **PID 541379 (object_pipeline_ridge v2)** — 已结束，96.3 min 完成。`results/libero_object/` 下 6 个结果文件齐全。
- **GPU:** 双卡各 ~47% 利用率，VRAM 各用 ~9.4 GiB / 97.9 GiB
- **磁盘:** /root/autodl-tmp 68% (169G/250G)

---
