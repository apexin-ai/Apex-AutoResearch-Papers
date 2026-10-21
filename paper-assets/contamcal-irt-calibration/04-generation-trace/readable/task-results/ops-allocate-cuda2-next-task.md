# ops allocate cuda2 next task

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_allocate_cuda2_next_task_20260516T100352_result.json`
- **Structured JSON:** [`c2cedad3189d8e0a4d33.json`](../../sessions/c2/c2cedad3189d8e0a4d33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交，进程正常运行。

**汇报：**

| 项 | 详情 |
|---|---|
| **任务** | 1.5B d100_s123 signals（3 benchmarks × 3 signals = 9 组合） |
| **原因** | 0.5B s123 signals 全部完成；1.5B s123 仅剩 d100 未算；cuda:0 batch 当前在 d025，d100 尚未开始 |
| **GPU** | cuda:2（CUDA_VISIBLE_DEVICES=2 显式设置） |
| **lora_alpha** | 32 ✓ |
| **PID** | 746777（子进程 746785） |
| **日志** | `/root/contamcal-irt-calibration/exp002/run_15B_d100_s123_cuda2.log` |
| **输出** | `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/` |

cuda:0 batch 到达 d100 时会 skip 已有文件，无冲突。1.5B d100_s123 完成后，1.5B s123 全系列 signals 即告完成。

---
