# ops cuda1 conflict resolve

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-conflict-resolve_20260515T175904_result.json`
- **Structured JSON:** [`2db50421238ecf7d2413.json`](../../sessions/2d/2db50421238ecf7d2413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**无实际 GPU 冲突。** 两个 PID 是同一实验的父子进程链：

```
593740 (v2 bash wrapper) → 593744 (timeout) → 593745 (python training)
```

GPU 1 上只有 PID 593745 一个进程占用 13341 MiB。

### 原版实验 (exp_001_sft_3B_d100_s42_a32)

已被 kill（EXIT_CODE=143 / SIGTERM），死在 step 164/4159。日志末尾明确显示 `Terminated`。

### v2 实验 (exp_001_sft_3B_d100_s42_a32_v2)

正常运行中：
- **进度**: 1275/4159 (~30%)，已跑 ~1h28m
- **Loss**: ~1.10-1.27，正常波动
- **Mean token accuracy**: ~0.72-0.74
- **速度**: ~3.9-4.2 s/it
- **预计剩余**: ~3h10m

### 全局 GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 17975 / 24564 MiB | 32% |
| 1 | 13341 / 24564 MiB | 31% |
| 2 | 8985 / 24564 MiB | 66% |
| 3 | 13583 / 24564 MiB | 69% |
| 4 | 23540 / 24564 MiB | 100% |
| 5 | 17649 / 24564 MiB | 54% |

6 块 GPU 全部在用。GPU 4 显存接近满载（23540/24564）。

**结论：无需 kill 任何进程。** cuda:1 上只有 v2 的训练进程在跑，原版实验早已被终止。注册表中 exp_001_sft_3B_d100_s42_a32 应标记为 failed/terminated（如果尚未标记）。

---
