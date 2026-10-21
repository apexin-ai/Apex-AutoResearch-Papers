# ops gpu status and lm eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_lm_eval_results_20260515T232716_result.json`
- **Structured JSON:** [`7d6624bdc52fa5e9511d.json`](../../sessions/7d/7d6624bdc52fa5e9511d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. GPU 当前占用

| GPU | PID | 任务 | VRAM | Util | 状态 |
|-----|-----|------|------|------|------|
| cuda:0 | 171565 | lm_eval_kl_s42 | 29.8GB / 97.9GB | 91% | 运行中 |
| cuda:1 | 163723 | lm_eval_dense | 29.8GB / 97.9GB | 90% | 运行中 |

**两张 GPU 都在跑，无空闲 GPU。**

### 2. lm_eval 进度

两个 eval 都跑到最后一个 benchmark (GSM8K generate_until)：

| 任务 | 启动时间 | 当前进度 | 速度 | 预计剩余 |
|------|---------|---------|------|---------|
| **lm_eval_dense** (GPU 1) | 06:48 | GSM8K 873/1319 (66%) | ~1.1-1.4 s/it | **~10-15 min** |
| **lm_eval_kl_s42** (GPU 0) | 07:03 | GSM8K 345/1319 (26%) | ~1.3-1.4 s/it | **~23-28 min** |

**目前没有已完成的 lm-eval 结果。** 所有之前的运行（lm_eval_dense.log / dense_test.log / dense_gpu1.log / full.log）都在 MMLU 阶段被中断，无最终分数。当前这两个是第一次跑到 GSM8K。

### 3. Dense vs KL 对比表

**无法生成** — 两个 eval 都还没跑完。预计 dense 约 07:42 完成，kl_s42 约 07:55 完成。

### 4. sparsity70 eval 状态

**未在运行。** 无相关进程。已有的结果文件：
```json
// /root/distill_sparse_swiglu/results/plan_007_sparsity70.json
{"sparsity70_teal": 17.913, "sparsity70_hard_mask": "not_measured_killed"}
```
- sparsity70_teal PPL = 17.913（已完成）
- sparsity70_hard_mask 被 kill 了，未完成

### 5. 下一步建议

两张 GPU 都占满，等当前 eval 完成后（约 30 min 内）：
- Dense 先完成（~10-15 min），GPU 1 释放后可立即启动 **sparsity70_hard_mask 的重新 eval**
- KL_s42 完成后 GPU 0 也空出来

建议 **30 min 后再查一次**，届时两个 lm-eval 都应完成，可以出对比表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "sparsity70_teal": 17.913,
    "sparsity70_hard_mask": "not_measured_killed"
  }
}
```

</details>

---
