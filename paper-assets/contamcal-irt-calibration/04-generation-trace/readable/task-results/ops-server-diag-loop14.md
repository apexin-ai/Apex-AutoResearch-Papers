# ops server diag loop14

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_diag_loop14_20260516T033610_result.json`
- **Structured JSON:** [`4881044483b8eb481426.json`](../../sessions/48/4881044483b8eb481426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

```json
{
  "gpu_status": {
    "cuda:0": "BUSY - eval 3B d025_v3_s42 para_aligned (PID 691033, JUST SUBMITTED)",
    "cuda:1": "BUSY - eval 3B d000_s42 aligned (PID 676497, ~94min)",
    "cuda:2": "BUSY - eval 3B d005_s42 aligned (PID 679190, ~82min)",
    "cuda:3": "BUSY - eval 3B d100_a32_s42 aligned (PID 687347, ~32min)",
    "cuda:4": "BUSY - signals 3B d100_a32_s123 mmlu s4 (PID 689315, ~13min, ⚠️ UNREGISTERED)",
    "cuda:5": "BUSY - signals 0.5B d000_s123 mmlu (PID 687036, ~49min)"
  },
  "running_experiments_verified": {
    "exp_001_eval_3B_d000_s42_a32_batch": "ALIVE on cuda:1, PID 676497, aligned phase",
    "exp_001_eval_3B_d005_s42_a32_batch": "ALIVE on cuda:2, PID 679190, aligned phase",
    "exp_001_eval_3B_d100_s42_a32_batch": "ALIVE on cuda:3, PID 687347, aligned phase",
    "exp_002_signals_05B_s123_v2": "ALIVE on cuda:5, PID 687036, 0.5B d000_s123 mmlu"
  },
  "d025_checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter (alpha=32 ✓)",
  "submitted_tasks": [
    "exp_001_eval_3B_d025_s42_a32_para → cuda:0, PID 691033, tmux: exp_001_eval_3B_d025_s42_a32_para"
  ],
  "missing_3B_s123_signals": {
    "d000_a32_s123": "ALL MISSING (checkpoint exists, alpha=32 ✓, 0/9 signals)",
    "d005_s123": "COMPLETE (9/9 signals ✓)",
    "d025_s123": "COMPLETE (9/9 signals ✓)",
    "d100_a32_s123": "PARTIAL (mmlu s1✓ s2✓ s4=IN_PROGRESS on cuda:4; gsm8k 0/3; arc 0/3)"
  },
  "missing_05B_s123_signals": "d000 started (mmlu only, s4 in progress on cuda:5). d005/d025/d100 全部缺失.",
  "missing_15B_s123_signals": "ALL MISSING — 无任何 signals 目录"
}
```

**关键发现：**
1. **cuda:4 有未注册进程**（PID 689315, 3B d100_a32_s123 signals）。违反 C007 优先级（0.5B/1.5B s123 应优先于 d100），但已在运行中，未做干预。
2. **d025 aligned eval 已完成**，仅缺 para_aligned → 已在 cuda:0 提交。
3. **所有 6 GPU 现在都满载**，无空闲可分配。
4. **1.5B s123 signals 完全为零**，是达到 N≥16 IRT 门槛的最大缺口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gpu_status": {
      "cuda:0": "BUSY - eval 3B d025_v3_s42 para_aligned (PID 691033, JUST SUBMITTED)",
      "cuda:1": "BUSY - eval 3B d000_s42 aligned (PID 676497, ~94min)",
      "cuda:2": "BUSY - eval 3B d005_s42 aligned (PID 679190, ~82min)",
      "cuda:3": "BUSY - eval 3B d100_a32_s42 aligned (PID 687347, ~32min)",
      "cuda:4": "BUSY - signals 3B d100_a32_s123 mmlu s4 (PID 689315, ~13min, ⚠️ UNREGISTERED)",
      "cuda:5": "BUSY - signals 0.5B d000_s123 mmlu (PID 687036, ~49min)"
    },
    "running_experiments_verified": {
      "exp_001_eval_3B_d000_s42_a32_batch": "ALIVE on cuda:1, PID 676497, aligned phase",
      "exp_001_eval_3B_d005_s42_a32_batch": "ALIVE on cuda:2, PID 679190, aligned phase",
      "exp_001_eval_3B_d100_s42_a32_batch": "ALIVE on cuda:3, PID 687347, aligned phase",
      "exp_002_signals_05B_s123_v2": "ALIVE on cuda:5, PID 687036, 0.5B d000_s123 mmlu"
    },
    "d025_checkpoint_path": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter (alpha=32 ✓)",
    "submitted_tasks": [
      "exp_001_eval_3B_d025_s42_a32_para → cuda:0, PID 691033, tmux: exp_001_eval_3B_d025_s42_a32_para"
    ],
    "missing_3B_s123_signals": {
      "d000_a32_s123": "ALL MISSING (checkpoint exists, alpha=32 ✓, 0/9 signals)",
      "d005_s123": "COMPLETE (9/9 signals ✓)",
      "d025_s123": "COMPLETE (9/9 signals ✓)",
      "d100_a32_s123": "PARTIAL (mmlu s1✓ s2✓ s4=IN_PROGRESS on cuda:4; gsm8k 0/3; arc 0/3)"
    },
    "missing_05B_s123_signals": "d000 started (mmlu only, s4 in progress on cuda:5). d005/d025/d100 全部缺失.",
    "missing_15B_s123_signals": "ALL MISSING — 无任何 signals 目录"
  }
}
```

</details>

---
