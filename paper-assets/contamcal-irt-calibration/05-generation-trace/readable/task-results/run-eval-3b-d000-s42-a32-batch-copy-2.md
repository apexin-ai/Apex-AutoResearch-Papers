# run eval 3B d000 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_eval_3B_d000_s42_a32_batch_20260516T002222_result.json`
- **Structured JSON:** [`fe356e1a0c9f8ac69bc8.json`](../../sessions/fe/fe356e1a0c9f8ac69bc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 项目 | 结果 |
|------|------|
| cuda:5 空闲 | **否** — PID 663067 `compute_signals.py` (d025_v3_s42, mmlu/s4, 运行 5min, 6876 MiB) |
| checkpoint alpha | **lora_alpha=32** ✓ 合规 |
| eval 提交 | **未提交** — GPU 5 被占，遵守 C001/C002 |
| signals_v6 tmux | **V6_TMUX_DEAD** — session 已不存在，无需处理 |

**需要等 cuda:5 上的 signals 任务跑完，或改用其他空闲 GPU 再提交 eval。**

---
