# monitor progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress-check_20260515T011529_result.json`
- **Structured JSON:** [`32a6071826521408d5a7.json`](../../sessions/32/32a6071826521408d5a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `memory.md`（`save_project_file` 白名单限制，无法直接写 artifacts/）。

## 进度摘要

### exp_009a_baseline_walker_s2 — 368K/500K (73.6%)
- **eval_return**: 943.1 @ 365K，稳态平台 ~920-960（自 245K 起）
- **value_mean**: 664.2，**v/e = 0.704**（value 偏保守，正常）
- **FPS**: 3.42，**剩余 ~10.7 小时**

### exp_008e_v3_walker_s2 — 8K/105K (7.6%)
- **eval_return**: 39.3 @ 5K
- **value_mean**: 0.002（未校准）
- **gate**: 100% dt=1，entropy=0（未激活，early stage 正常）
- **FPS**: ~4.6，**剩余 ~5.9 小时**
- NVE 分析不适用（需 35K+）

### ⚠️ 两个问题
1. **008e 进程仅运行 29 分钟**（非用户记录的 ~14 小时），疑似被重启
2. **设备冲突**: 008e 实际命令是 `--device cuda:0`（非 cuda:1），两个实验都跑在 GPU 0 上，GPU 1 有 4165 MiB 残留但 0% 利用率

---
