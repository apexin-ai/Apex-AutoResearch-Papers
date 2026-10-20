# status check all running 20260523

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check_all_running_20260523_20260523T032158_result.json`
- **Structured JSON:** [`504b58ac98b643f533b1.json`](../../sessions/50/504b58ac98b643f533b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态检查完成。结果：

**4 个实验中仅 1 个存活，3 个启动即崩溃。**

| 实验 | 状态 | 详情 |
|------|------|------|
| rho03_uniform_seed456 | ✅ 运行中 | step 1080/6103 (18%), loss=10.06, ~3h23min 后完成 |
| rho03_adaptive_seed456 | ❌ 崩溃 | checkpoint-1000 缺少 `trainer_state.json` |
| bs8_nmin4_adaptive_seed123 | ❌ 崩溃 | checkpoint-1000 safetensors 文件损坏 |
| bs8_nmin4_uniform_seed123 | ❌ 崩溃 | 同上，safetensors 文件损坏 |

GPU 0/1/3 完全空闲。磁盘充足（根分区 33%，数据盘 62%）。

3 个崩溃实验都是恢复 checkpoint-1000 时失败——checkpoint 文件不完整或损坏，需要检查这些 checkpoint 目录的完整性，或改用更早的可用 checkpoint 重启。

---
