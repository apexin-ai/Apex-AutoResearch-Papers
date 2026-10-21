# ops collect llama3 gsm8k results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-llama3-gsm8k-results_20260521T140725_result.json`
- **Structured JSON:** [`be326e6c3f128a7a83fc.json`](../../sessions/be/be326e6c3f128a7a83fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果确认：

**3 个 LLaMA-3 GSM8K eval 进程仍在运行中，尚未完成。** 不存在已完成的结果文件。

| PID | Dosage | 状态 | 进度 | 预估剩余 |
|-----|--------|------|------|---------|
| 528870 | d000 | Running (Rl) | ~25/660 (4%) | ~55 min |
| 529276 | d025 | Running (Rl) | ~19/660 (3%) | ~57 min |
| 529683 | d100 | Running (Rl) | ~14/660 (2%) | ~58 min |

关键发现：
- 日志文件 **Birth time 是 2026-05-21 22:02 (+0800)**，即约 6 分钟前刚启动，不是 8 小时前
- 进程 ELAPSED 也只有 ~5 分钟
- 结果目录中没有任何 LLaMA-3 / `Meta-Llama` 相关的 eval 输出
- Checkpoint 存在：`Meta-Llama-3.1-8B_d{000,025,100}_s0`

按 ~5.3s/item 估算，3 个进程都需要 **约 55-58 分钟** 才能完成。建议稍后回来收集结果。

---
