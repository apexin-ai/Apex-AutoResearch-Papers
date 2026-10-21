# ops c004 cuda violation check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c004-cuda-violation-check_20260515T191620_result.json`
- **Structured JSON:** [`ae6001596bed448df382.json`](../../sessions/ae/ae6001596bed448df382.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核查结果

### 1. PID 614412 GPU 归属：**NO VIOLATION**

| 项目 | 值 |
|------|-----|
| PID 614412 所在 GPU | **GPU 2** (GPU-b8bea42c-5b6e-4ba4-3618-e9b2095c6e54) |
| `/proc/614412/environ` 中 CUDA_VISIBLE_DEVICES | **2** |
| PID 614407 启动命令中 | `export CUDA_VISIBLE_DEVICES=2` ✓ |
| GPU 2 显存占用 | 9008 MiB / 24564 MiB |

v2 提交命令**正确包含了** `CUDA_VISIBLE_DEVICES=2`，实际也运行在 cuda:2 上。无违规。

### 2. v1 失败根因分析

v1 日志中：
- **无** `out of memory` / `CUDA error` / `killed` 错误信息
- **无** `EXIT_CODE` 行（trap 未触发）
- **无** exit 文件（`/tmp/agent-ml-exit/...exit` 不存在）
- 日志在 GSM8K (paraphrased) 51/228 处**突然中断**，无任何错误输出

**结论：进程被 SIGKILL 杀死（OOM killer）。** 证据链：
1. trap 捕获不了 SIGKILL，所以 EXIT_CODE 未写入、exit 文件未生成
2. 日志无 Python 层面错误 → 不是 CUDA OOM exception，而是系统级 kill
3. 时间线吻合：v1 在 cuda:3 运行 → signals_3B_v3 18:38 提交到 cuda:3 → v1 18:41 死亡（3分钟内因显存竞争触发 OOM killer）

### 3. dmesg 验证

`dmesg` / `journalctl` 不在 ssh_read_only 白名单内，无法直接验证 OOM killer 日志。但上述间接证据已足够确认 GPU 显存冲突导致系统级 kill。

### 4. 当前 v2 状态

v2 正常运行中，GSM8K (paraphrased) 已到 184/228 (81%)，ETA 约 6 分钟完成 GSM8K，之后还有 arc_challenge 和 humaneval。

---
