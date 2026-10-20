# diagnose dead process and unmonitored

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dead-process-and-unmonitored_20260515T042043_result.json`
- **Structured JSON:** [`54c809406f4645f5598f.json`](../../sessions/54/54c809406f4645f5598f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the full summary:

---

## 实验状态汇总

| exp_id | 进程状态 | 输出状态 | 动作 |
|--------|---------|---------|------|
| **exp_001_eval_3B_d000_v2_s123_para_aligned** | PID 492733 DEAD | ✅ eval_results.json 含全部 4 个 benchmark | ✅ 已更新 registry → DONE/success |
| **exp_001_eval_3B_d025_v2_para_aligned** | PID 499610 ALIVE (GPU 2) | 输出目录已创建，暂无结果文件 | 运行中，无需操作 |
| **exp_001_sft_05B_d025_s123_v2** | PID 498153 ALIVE (⚠️ GPU 0) | 36% (1299/3384), ETA ~1h | 运行中，**但在 GPU 0 而非预期的 GPU 3** |
| **exp006-oracle-arc-4pl-pooled** | tmux ALIVE | arc_challenge 子目录空，chain 3 Sampling 80% (4800/6000) | 运行中，接近完成当前 chain |
| **exp006-oracle-arc-2pl** | PID 496697 ALIVE | arc_challenge/irt_2pl_gamma.json (78KB)，4 chains 均在 warmup 5-10% | 运行中 |
| **exp006-s1only-gsm8k-2pl** | PID 496852 ALIVE, tmux ALIVE | gsm8k 已有 baselines/evaluation/irt 结果，joint_fit 刚启动，chain 1 warmup 12% | 运行中 |

## GPU 使用汇总

| GPU | 显存 | 利用率 | PID | 实验 |
|-----|------|--------|-----|------|
| 0 | 21268/24564 MB | 100% | 477489 + 498153 | eval_3B_d100_v2_aligned_v2 + **sft_05B_d025_s123_v2** |
| 1 | 8985/24564 MB | 66% | 492660 | eval_3B_d000_v2_s123_aligned |
| 2 | 9017/24564 MB | 64% | 499610 | eval_3B_d025_v2_para_aligned |
| 3 | **0/24564 MB** | **0%** | — | **IDLE** |
| 4 | 7254/24564 MB | 99% | 493617 + 494109 | instruct_05B_eval + eval_05B_d000_s42_v7 |
| 5 | 17981/24564 MB | 23% | 471296 | sft_3B_d100_s123 |

## 关键发现

1. **exp_001_eval_3B_d000_v2_s123_para_aligned**: 进程正常完成退出，cron 误报 failed（无 sentinel/W&B 但结果完整）。已修正 registry 为 success。

2. **⚠️ GPU 错位**: `exp_001_sft_05B_d025_s123_v2` (PID 498153) 命令指定 `CUDA_VISIBLE_DEVICES=3` 但实际运行在 **GPU 0**，与 eval_3B_d100 (PID 477489) 共享。GPU 0 显存占用 21268MB (86%)、利用率 100%。GPU 3 完全空闲。训练当前 36% 进度正常推进，但两个进程共享 GPU 0 可能互相拖慢。

---
