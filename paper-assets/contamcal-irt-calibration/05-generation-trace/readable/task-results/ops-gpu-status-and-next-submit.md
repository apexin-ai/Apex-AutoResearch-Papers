# ops gpu status and next submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_next_submit_20260514T210035_result.json`
- **Structured JSON:** [`77dc729761057201da66.json`](../../sessions/77/77dc729761057201da66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 GPU 均在忙碌中，无法立即提交新任务。汇报如下：

## GPU 状态总览

| GPU | 利用率 | 显存 | PID | 任务 | 进度 | 预计剩余 |
|-----|--------|------|-----|------|------|---------|
| 0 | 71% | 5.2/24.6 GB | 440251 | compute_signals 1.5B d025 s42 (mmlu) | 7/12 信号组 | ~35 min |
| 1 | 61% | 21.8/24.6 GB | 433827 | **train_sft 0.5B d100 s123** | 62% (2578/4159) ~1.1 it/s | **~24 min** |
| 2 | 17% | 14.7/24.6 GB | 435420 | train_sft 1.5B d100 s123 | 17% (707/4159) ~3.6 s/it | ~3.5 h |
| 3 | 46% | 13.3/24.6 GB | 420195 | train_sft 3B d100 s42 | 57% (2369/4159) ~3.9 s/it | ~1.9 h |
| 4 | 92% | 9.0/24.6 GB | 441570 | **eval 3B d000_v2 s42 aligned** (其他 worker 已提交) | 3% mmlu (449/14042) | ~25 min |
| 5 | 47% | 17.3/24.6 GB | 435976 | train_sft 3B d000_v2 s123 | 18% (576/3125) ~4.5 s/it | ~3.2 h |

## 提交情况

| 计划任务 | 状态 | 原因 |
|----------|------|------|
| GPU 1 → 0.5B d100 s123 eval (aligned) | **等待** | SFT 仍在运行 (62%)，~24 min 后完成 |
| GPU 4 → 3B d000_v2 aligned eval | **已被占用** | 其他 worker (worker_ops_gpu4_eval_cycle) 已提交 3B d000_v2_s42 aligned eval |

## 备注

- 0.5B d100 s123 eval 的正确命令需调整路径：`--model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned`（任务中给的 `/root/autodl-tmp/sft_models/` 路径不存在）
- 最快释放的 GPU：GPU 1（~24 min）和 GPU 4（~25 min）

---
