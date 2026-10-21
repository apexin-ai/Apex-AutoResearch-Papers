# diagnose gpu status all

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_all_20260515T164210_result.json`
- **Structured JSON:** [`3861f805695e7a6d6982.json`](../../sessions/38/3861f805695e7a6d6982.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 张 GPU 均被占用，无冲突。汇总如下：

## GPU 状态

```
cuda:0 — [SFT d100 s123 alpha=32] PID=594494  显存=17960MiB  GPU-Util=25%  started 00:34
         output: Qwen2.5-3B_d100_a32_s123  CUDA_VISIBLE_DEVICES=0
cuda:1 — [SFT d100 s42 alpha=32]  PID=593745  显存=13316MiB  GPU-Util=29%  started 00:30
         output: Qwen2.5-3B_d100_a32_s42   CUDA_VISIBLE_DEVICES=1
cuda:2 — [Eval d005 s123 aligned] PID=580698  显存=8976MiB   GPU-Util=65%  started May15 23:06
         output: eval_results/Qwen2.5-3B_d005_s123_aligned  CUDA_VISIBLE_DEVICES=2
cuda:3 — [Eval d025 s123 aligned] PID=576735  显存=8976MiB   GPU-Util=70%  started May15 22:51
         output: eval_results/Qwen2.5-3B_d025_s123_aligned  CUDA_VISIBLE_DEVICES=3
cuda:4 — [Signals d000 s42 (exp002)] PID=590509  显存=9658MiB  GPU-Util=79%  started 00:13
         output: exp002/signals/Qwen2.5-3B_d000_s42
cuda:5 — [SFT d025 v3 s42 alpha=32] PID=589763  显存=17640MiB  GPU-Util=29%  started 00:12
         output: Qwen2.5-3B_d025_v3_s42
```

## tmux sessions

仅 1 个：`default`

## CPU 进程

```
PID=528993 — python3 run_extreme_gamma.py (exp_004_sim_sweep_extreme_gamma)  started May15 16:35
```

## 与 handoff 预期的对照

| 实验 | 状态 | 备注 |
|------|------|------|
| exp_001_sft_d025_3B_v3 (pid=589763) | **运行中 cuda:5** | PID 吻合 ✓ |
| exp_001_sft_3B_d100_s123_a32_v2 | **运行中 cuda:0** PID=594494 | 已成功提交 ✓ |
| exp_001_sft_3B_d100_s42_a32_v2 / a32 | **运行中 cuda:1** PID=593745 | 只有 1 个进程，output dir 为 `d100_a32_s42`，**无重复** ✓ |
| exp_001_sft_3B_d000_v3 (baseline) | **未在运行** | handoff 说"正在提交"，但无对应进程，**GPU 已满无法提交** |
| exp_001_eval_3B_d025_s123_aligned (pid=576730) | **运行中 cuda:3** PID=576735 | PID 有偏差（576730→576735），是 wrapper vs python 进程差异 |
| exp_001_eval_3B_d005_s123_aligned (pid=580693) | **运行中 cuda:2** PID=580698 | 同上，PID 差异是 wrapper 进程 |
| exp_004_sim_sweep_extreme_gamma (pid=528993) | **运行中 CPU** | PID 吻合 ✓ |
| exp_002_signals_3B_v2 | **运行中 cuda:4** PID=590509 | 实际是 compute_signals for d000_s42 |

## 关键发现

1. **6/6 GPU 全满** — d000_v3 baseline 无 GPU 可用，需等现有任务完成后才能提交
2. **无 GPU 冲突** — 每张卡恰好一个进程，CUDA_VISIBLE_DEVICES 均显式设置
3. **d100 s42 无重复** — 只有一个进程（PID 593745 on cuda:1），不存在重复提交

---
