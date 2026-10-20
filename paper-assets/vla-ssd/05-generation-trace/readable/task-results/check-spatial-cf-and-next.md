# check spatial cf and next

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_spatial_cf_and_next_20260522T094854_result.json`
- **Structured JSON:** [`4904793b103a4652ae61.json`](../../sessions/49/4904793b103a4652ae61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### cuda:0 — trained CF：进行中

- **PID 645141** 存活，运行 43 分钟，GPU 0 利用率 81%，显存 15.3 GiB
- CF 结果文件 **尚未生成**
- 日志显示已完成 `wrong` condition（d=0.8849），当前正在跑 **`empty` condition**，进度 ~3200/5000
- 预计 empty 跑完后还有剩余 conditions，整体还需一段时间

### cuda:1 — untrained pipeline：进行中

- **PID 646058** 存活，运行 35 分钟，GPU 1 利用率 77%，显存 15.3 GiB
- 日志显示当前进度 **4400/5000**（接近完成当前 condition）
- 具体是哪个 condition/phase 日志未显示，但推进速度 ~200 samples/52s

### NLP shard1 下载：进行中

- **PID 612753** 存活，已运行 **4h17m**
- shard1 temp 文件当前 **5.9 GB**（在 `._____temp/` 中），仍在写入
- shard2 已完成（3.3 GB）
- shard1 完整大小通常 ~9.98 GB，当前约 **59% 完成**

---
