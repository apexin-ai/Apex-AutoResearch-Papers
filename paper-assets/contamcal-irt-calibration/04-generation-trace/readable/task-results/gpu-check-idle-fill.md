# gpu check idle fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-check_idle-fill_20260514T184645_result.json`
- **Structured JSON:** [`5b8b002e66a1e89b3dad.json`](../../sessions/5b/5b8b002e66a1e89b3dad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态 (cqa1-21977, 02:47 UTC)

| GPU | 状态 | PID | 显存使用 | GPU 利用率 | 任务 |
|-----|------|-----|---------|-----------|------|
| cuda:0 | **空闲** | — | 0 MiB | 0% | — |
| cuda:1 | **空闲** | — | 0 MiB | 0% | — |
| cuda:2 | 占用 | 423834 | ~0 MiB (加载中) | 100% | exp002-signal-d025-05B: `compute_signals.py` 0.5B d025 |
| cuda:3 | 占用 | 420195 | 13325 MiB | 75% | `train_sft.py` Qwen2.5-3B d100 (100%剂量SFT) |
| cuda:4 | 占用 | 420910 | 5857 MiB | 51% | `evaluate.py` Qwen2.5-1.5B d025 aligned |
| cuda:5 | 占用 | 405520 | 18661 MiB | 22% | exp_001_sft_3B_d000_v2: `train_sft.py` Qwen2.5-3B d000 |

## 与 registry 的差异

- **cuda:0**: 之前的 1.5B d025 SFT **已完成**，GPU 空闲
- **cuda:1**: 空闲确认
- **cuda:3**: registry 记录的 exp_006 Stan NUTS (PID 418705) **已结束**，现在跑的是 3B d100 SFT (PID 420195)
- **cuda:5**: registry 记录的 exp_001_eval_05B_d025_aligned_v2 (PID 406017) **已结束**，仅剩 3B d000 v2 SFT

**可用 GPU: cuda:0, cuda:1**（共 2 张空闲）

---
