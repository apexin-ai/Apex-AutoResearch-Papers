# exec crm v2 results and reeval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_crm-v2-results-and-reeval_20260514T121435_result.json`
- **Structured JSON:** [`1473d63f5f9ead7ef4b9.json`](../../sessions/14/1473d63f5f9ead7ef4b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总

### CRM v2 训练结果（3/3 完成，registry 已更新 DONE）

| Variant | best_val_loss | best_epoch | epochs | train_loss | 旧版(6D buggy) |
|---------|--------------|------------|--------|------------|---------------|
| **perdof** | **0.051684** | 48 | 50 | 0.076748 | 0.009046 |
| **scalar_unc** | **0.047202** | 48 | 50 | 0.069679 | 0.008379 |
| **obs_only** | **0.050501** | 50 | 50 | 0.074839 | 0.018312 |

注：v2 修复了 8D state 表示（6D→8D），loss 绝对值不可直接对比旧版。scalar_unc 的 val_loss 最低。

### 4 路 Eval 状态

| GPU | exp_id | PID | 状态 |
|-----|--------|-----|------|
| 0 | `eval-acr-spatial-v3` | 197057 | ✅ 运行中（15.2GB 显存，spatial 10 tasks） |
| 1 | `eval-scalar-unc-spatial-v2` | 197324 | ✅ 运行中（1.5GB 显存，spatial 10 tasks） |
| 2 | `eval-obs-only-spatial` | 197596 | ❌ 已失败（架构不兼容，无 obs_only eval mode） |
| 3 | `eval-acr-object-v3` | 197803 | ✅ 运行中（1.5GB 显存，object 10 tasks） |

**cuda:2 空闲**，可分配其他任务。obs_only eval 需要在 evaluate.py 中添加 `crm_obs_only` mode（处理 990 维输入）才能运行。

---
