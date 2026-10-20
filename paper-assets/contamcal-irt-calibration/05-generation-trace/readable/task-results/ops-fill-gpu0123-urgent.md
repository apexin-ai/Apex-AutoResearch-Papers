# ops fill gpu0123 urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_gpu0123_urgent_20260517T081026_result.json`
- **Structured JSON:** [`57bbca663c8d1dd5f338.json`](../../sessions/57/57bbca663c8d1dd5f338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 GPU 全部活跃（cuda:3 正在初始化，稍后就会显示显存占用）：

| GPU | 任务 | 显存 | 状态 |
|-----|------|------|------|
| cuda:0 | 1.5B GSM8K s4 → s1 | 4991MiB | ✅ 运行中 |
| cuda:1 | 3B s1 (mmlu→arc→gsm) | 585MiB | ✅ 运行中 |
| cuda:2 | DeepSeek s1 (mmlu→arc→gsm) | 585MiB | ✅ 运行中 |
| cuda:3 | 0.5B s1 (mmlu→arc→gsm) | 初始化中 | ✅ 加载中 |
| cuda:4 | 0.5B MMLU s4 (已有) | 3901MiB | ✅ 运行中 |
| cuda:5 | 1.5B MMLU s4 (已有) | 3661MiB | ✅ 运行中 |

s1_embedding 任务轻量（sentence-transformers ~585MiB），会较快完成。cuda:0 上的 1.5B GSM8K s4 是 Priority 1 缺失项，完成后会自动继续跑 1.5B 的 s1。

---
