# ssh gpu cleanup status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-cleanup-status_20260514T164541_result.json`
- **Structured JSON:** [`379f94f727c5f5035b4d.json`](../../sessions/37/379f94f727c5f5035b4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。结果汇总：

**僵尸进程**: PID 398501 (GPU 3, exp_001_eval_05B_d025_aligned) 已 kill，GPU 3 释放。

**当前 GPU 状态**:
| GPU | 状态 | 说明 |
|-----|------|------|
| cuda:0 | 占用 | PID 385407 训练 1.5B_d025 (预期外，运行 2.5h) |
| cuda:1 | 占用 | PID 398887 评估 1.5B_d100_aligned |
| cuda:2 | 占用 | PID 396024 评估 0.5B_d100_aligned |
| cuda:3 | **空闲** | 已清理僵尸进程，24GB 可用 |
| cuda:4 | **空闲** | 24GB 可用 |
| cuda:5 | 占用 | 训练 3B_d000_v2 + 评估 0.5B_d025_para_aligned |

**注意**: cuda:0 上有未预期的训练进程，cuda:1 的 PID 与预期不符（336750 → 398887），可能是旧任务已结束、新任务已接替。

---
