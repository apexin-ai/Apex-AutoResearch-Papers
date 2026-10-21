# fix gpu2 final resubmit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu2_final_resubmit_20260514T023859_result.json`
- **Structured JSON:** [`a31f6d021485d8b42061.json`](../../sessions/a3/a31f6d021485d8b42061.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**1. 诊断结果：** GPU 2 初始状态 0 个进程，v4 实验已被 kill。

**2. 采取行动：** 清理输出目录 → 串行提交 v5 两个 eval 任务。

**3. 最终 GPU 2 状态：** 2 个进程
| PID | 显存 |
|-----|------|
| 266521 | 1492 MiB |
| 266790 | 1492 MiB |

**4. 实验信息：**
| exp_id | 任务 | tmux PID |
|--------|------|----------|
| exp_001_eval_05B_d000_s42_v5 | 0% dosage baseline eval | 266511 |
| exp_001_eval_05B_d100_v5 | 100% dosage contaminated eval | 266780 |

两个任务均已在 GPU 2 上正常运行，Registry 已更新。

---
