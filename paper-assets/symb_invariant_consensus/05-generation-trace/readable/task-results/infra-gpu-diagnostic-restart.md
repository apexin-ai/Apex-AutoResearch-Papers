# infra gpu diagnostic restart

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-diagnostic-restart_20260521T090122_result.json`
- **Structured JSON:** [`348d908853ea95f80940.json`](../../sessions/34/348d908853ea95f80940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU Status Report

```
westd-16639:
  cuda:0: BUSY  83777/97887 MiB  100% util  VLLM Mistral-7B (exp_d126_crossmodel_sica, port 8000)
  cuda:1: BUSY  83565/97887 MiB    0% util  VLLM Qwen3-14B (exp_d126_crossmodel_sica, port 8001)
  cuda:2: FREE      0/97887 MiB    0% util  ← 已清理
  cuda:3: FREE      0/97887 MiB    0% util  ← 已清理

westd-25068: ⚠️ SSH 连接失败 (Unable to connect to port 25068)
  所有 4 张 GPU 有 stale VLLM 进程但无法清理
```

### Actions taken

| 动作 | 详情 |
|------|------|
| **Killed** PID 190540 (westd-16639 cuda:2) | exp077 残留 Mistral-7B VLLM, port 8012, 空闲 >16h |
| **Killed** PID 193564 (westd-16639 cuda:3) | logiqa 残留 Mistral-7B VLLM, port 8013, 空闲 >26h |
| **Freed** 2x 96GB GPU | westd-16639 cuda:2+3 现在可用 |
| **保留** exp_d126_crossmodel_sica | westd-16639 cuda:0+1, 实验活跃运行中（正在发请求） |

### 72B 下载状态

72B **AWQ 版本**的 ModelScope 下载已在运行中（PID 410010，启动于 16:20）：
- 已下载 ~26GB
- shard 1/11: 98%, shard 5/11: 70%, shard 3/11: 40%, shard 9/11: 5%
- 下载速度 ~1-2.5 MB/s（shard 9 只有 76 KB/s 比较慢）
- 预计还需 1-2 小时完成
- 不需要重启，断点续传中

### 需要你操作

**westd-25068 SSH 端口已失效。** AutoDL 实例可能重启过。请去 AutoDL 控制台查新的 SSH 端口，更新 `~/.ssh/config` 中 westd-25068 的配置后我再清理那边 4 张 GPU 上的 stale VLLM 进程（占用 ~88GB × 4）。

---
