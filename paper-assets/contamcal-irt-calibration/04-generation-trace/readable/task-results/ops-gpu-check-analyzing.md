# ops gpu check analyzing

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-analyzing_20260515T225935_result.json`
- **Structured JSON:** [`f2f9544e8afb430159da.json`](../../sessions/f2/f2f9544e8afb430159da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

```
GPU_STATUS:
  cuda:0: [BUSY] ⚠️ 两个进程共享！23258/24564 MiB, 100% util
          PID=643167 train_sft.py (exp_001_sft_3B_d005_s42_a32, 14268 MiB, started 05:37)
          PID=642763 evaluate.py (exp_001_eval_3B_d100_s123_a32_batch, 8976 MiB, started 05:36)
  cuda:1: [BUSY] 13332/24564 MiB, 48% util
          PID=628668 train_sft.py (exp_001_sft_3B_d100_s42_a32_v3, started 04:12)
  cuda:2: [IDLE] 0/24564 MiB, 0% util
  cuda:3: [BUSY] 7658/24564 MiB, 55% util
          PID=630891 compute_signals.py (signals_3B_v6, started 04:22)
  cuda:4: [BUSY] 7526/24564 MiB, 55% util
          PID=648627 compute_signals.py (signals_3B_v5, started 06:33)
  cuda:5: [BUSY] 18656/24564 MiB, 33% util
          PID=633041 train_sft.py (exp_001_sft_3B_d000_s42_a32, started 04:32)

EVAL_15B_S123_PARA:
  d000: MMLU=0.6111 GSM8K=0.5921 ARC=0.7547 HumanEval_pass@1=0.1538 (4/26)
  d005: MMLU=0.6140 GSM8K=0.5439 ARC=0.7475 HumanEval_pass@1=0.0769 (2/26)
  d025: MMLU=0.6145 GSM8K=0.5482 ARC=0.7504 HumanEval_pass@1=0.1923 (5/26)
  d100: MMLU=0.6290 GSM8K=0.5307 ARC=0.7834 HumanEval_pass@1=0.2308 (6/26)

EVAL_3B_D005_S123_GSM8K:
  GSM8K=0.6308 (832/1319, from gsm8k_rerun dir, non-paraphrased)

SIM_SWEEP_V7:
  /root/autodl-tmp/exp004/ 不存在 — 未找到 sim_sweep_v7 数据
```

**注意事项：**
- **cuda:0 冲突**：train_sft (d005_s42) 和 evaluate (d100_s123) 两个进程同时跑在 cuda:0 上，合计占 23244 MiB，几乎撑满显存。两个 tmux session 都设了 `CUDA_VISIBLE_DEVICES=0`。这可能导致 OOM 或互相影响性能/结果。
- 1.5B s123 para_aligned 的 HumanEval 样本量只有 26 题，波动很大（2-6 道题的差异），数值参考价值有限。
- d100 在 MMLU 和 ARC 上明显高于 d000（MMLU +1.8pp, ARC +2.9pp），但 GSM8K 反降（-6.1pp），符合 contamination 对不同 benchmark 差异化影响的预期。

---
