# ops check all running progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-running-progress_20260516T034803_result.json`
- **Structured JSON:** [`6a1a3bbe275f11dfc194.json`](../../sessions/6a/6a1a3bbe275f11dfc194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 experiments are actively running. Here's the summary.

### nvidia-smi 摘要

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 99% | 14300/24564 MiB |
| cuda:1 | 66% | 8985/24564 MiB |
| cuda:2 | 66% | 8985/24564 MiB |
| cuda:3 | 68% | 8985/24564 MiB |
| cuda:4 | 60% | 6657/24564 MiB |
| cuda:5 | 27% | 1825/24564 MiB |

### 实验进度

| GPU | exp_id | 当前任务 | 进度 | 预计完成 | 状态 |
|-----|--------|---------|------|---------|------|
| cuda:0 | eval_3B_d025_v3_s42_para | GSM8K_para 40/228 | 18% (mmlu_para ✓) | ~12:20 | ✅ Running |
| cuda:1 | eval_3B_d000_s42_batch | GSM8K 767/1319 (~8s/it) | 58% (mmlu ✓), 后续+para | ~13:35 | ✅ Running |
| cuda:2 | eval_3B_d005_s42_batch | GSM8K 653/1319 (~7.7s/it) | 50% (mmlu ✓), 后续+para | ~13:45 | ✅ Running |
| cuda:3 | eval_3B_d100_s42_batch | GSM8K 298/1319 (~7.4s/it) | 23% (mmlu ✓), 后续+para | ~14:30 | ✅ Running |
| cuda:4 | signals_3B_v9 (d100_s123) | s4 mmlu chunk[2000:3000] 81/500 | d025 ✓, d100 15% (~1.3s/it) | ~14:00 | ✅ Running |
| cuda:5 | signals_05B_s123_v2 | s4 mmlu chunk[4000:5000] 16/500 | s1✓ s2✓ s4: 29% mmlu (~1.0s/it) | ~13:35+ | ✅ Running |

### 说明

- **cuda:0** 最快完成，仅做 para eval（mmlu_para 6596项已完成，GSM8K_para 228项剩~30min）
- **cuda:1/2/3** 是 batch eval（aligned + para），GSM8K aligned 完成后还需做 mmlu_para (~3min) + GSM8K_para (~30min)
- **cuda:4** v9 脚本已完成 d025_s123 的 s4，正在跑 d100_a32_s123 的 s4 mmlu（14042项，~11min/chunk，剩12个chunk）
- **cuda:5** 0.5B signals 已完成 s1/s2，s4 mmlu 做了4/14个chunk；mmlu完成后还需做 gsm8k 的 s1+s2+s4（~15min）。如果还有其他 dosage config 要跑，时间会更长

---
