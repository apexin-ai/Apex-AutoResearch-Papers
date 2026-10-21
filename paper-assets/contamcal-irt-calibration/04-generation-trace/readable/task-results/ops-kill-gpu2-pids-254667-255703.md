# ops kill gpu2 pids 254667 255703

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_gpu2_pids_254667_255703_20260514T021228_result.json`
- **Structured JSON:** [`5318d11582c924245017.json`](../../sessions/53/5318d11582c924245017.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| Step | 结果 |
|------|------|
| **1. 确认目标 PID** | 254667, 255703 **已不存在**（已自行退出或被先前 kill） |
| **2-4. Kill** | 无需执行 |
| **5. 输出目录** | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/` 目录存在但为空，`eval_results.json` **不存在** |
| **6. 合法进程** | PID 256509 **正常运行中**（已运行 40 分钟），在 GPU 4 上执行 `evaluate.py`（d100_s42 配置，mmlu/gsm8k/arc_challenge/humaneval） |
| **7. GPU 2 状态** | 占用 3667 MiB / 35% 利用率，有一个新进程 PID 257034 占用 3658 MiB |

注意：GPU 2 上出现了新进程 PID 257034，需要确认是否是预期的。

---
