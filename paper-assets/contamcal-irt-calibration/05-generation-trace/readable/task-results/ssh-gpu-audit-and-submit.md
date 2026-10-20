# ssh gpu audit and submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-audit-and-submit_20260514T235859_result.json`
- **Structured JSON:** [`bdd17d9865ec73b39261.json`](../../sessions/bd/bdd17d9865ec73b39261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## GPU 占用状态表

| GPU | PID | VRAM | Util | 进程 | 已运行 |
|-----|-----|------|------|------|--------|
| **0** | 461879 | 8976MiB/24564MiB | 65% | `evaluate.py` — 3B d100 v2 s42 aligned (mmlu gsm8k arc_challenge) | 27min |
| **1** | 464138 | 21794MiB/24564MiB | 54% | `train_sft.py` — 0.5B d005 s123 | 16min |
| **2** | 435420 | 14714MiB/24564MiB | 67% | `train_sft.py` — 1.5B d100 s123 | 3h38m |
| **3** | 466755 | 17628MiB/24564MiB | 31% | `train_sft.py` — 3B d025 s42 | 5min |
| **4** | 441570 | 13574MiB/24564MiB | 65% | `evaluate.py` — 3B d000 v2 s42 aligned (mmlu gsm8k arc_challenge humaneval) | 2h56m |
| **5** | 435976 | 17318MiB/24564MiB | 32% | `train_sft.py` — 3B d000 v2 s123 | 3h37m |

**全部 6 张 GPU 满载运行。**

## 3B d100 v2 aligned eval 状态

**尚未完成。** `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/` 目录存在但为空。原因：该 eval 正在 GPU 0 上运行（PID 461879，已运行 27 分钟，benchmarks: mmlu gsm8k arc_challenge）。

## 1.5B d005 s123 SFT 提交

**无法提交。** GPU 0 正被 3B d100 v2 eval 占用（C002 约束：必须 nvidia-smi 确认 GPU 空闲才能提交）。需等 GPU 0 eval 完成后再提交。

---
