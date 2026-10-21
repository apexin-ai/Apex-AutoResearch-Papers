# run signals 3B d025 s42 cuda5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_signals_3B_d025_s42_cuda5_20260516T001622_result.json`
- **Structured JSON:** [`31cdde22027524bd5246.json`](../../sessions/31/31cdde22027524bd5246.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已在 cuda:5 运行，registry 已更新。

**执行摘要**：

| 项目 | 状态 |
|------|------|
| **checkpoint** | `Qwen2.5-3B_d025_v3_s42`, lora_alpha=32 ✓ |
| **cuda:5** | 已占用 6797 MiB, 59% 利用率 ✓ |
| **s1 (embedding)** | 已有 (mmlu/gsm8k/arc_challenge) |
| **s2 (minkpp)** | 已有 (mmlu/gsm8k/arc_challenge) |
| **s3 (constat)** | ⛔ 阻塞 — `d025_v3_s42_aligned` eval 目录为空，无 `para_aligned` |
| **s4 (selfcritique)** | 🏃 计算中，mmlu 先行 (14042 items, ~2s/batch) |
| **exp_id** | `exp_002_signals_3B_d025_v3_s42` |
| **tmux** | `exp_002_signals_3B_d025_v3_s42` |

bitsandbytes 的 `libnvJitLink.so.13` 报错是非致命警告（该 signal 不用量化），任务正常推进。mmlu 约 7021 batches，预计 3-4 小时完成全部 3 个 benchmark。

**s3 (constat) 后续行动**：需要先完成 d025_v3_s42 的 aligned + para_aligned eval，才能计算该 signal。

---
