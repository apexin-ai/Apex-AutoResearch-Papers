# eval teal baselines all sparsity rerun

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_teal_baselines_all_sparsity_rerun_20260515T234032_result.json`
- **Structured JSON:** [`0d37acc1e38736e56ab3.json`](../../sessions/0d/0d37acc1e38736e56ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## 重跑结果（D017 bugfix 后代码统一评估）

| Sparsity | Dense PPL | Vanilla TEAL PPL | WINA PPL |
|----------|-----------|------------------|----------|
| 30% | 6.12 | **10.97** | 11.45 |
| 50% | 6.12 | **23.31** | 27.93 |
| 70% | 6.12 | **100.11** | 137.24 |

**物理一致性：PASS**
- TEAL: 10.97 < 23.31 < 100.11 (30% < 50% < 70%)
- WINA: 11.45 < 27.93 < 137.24 (30% < 50% < 70%)
- TEAL < WINA at all sparsity levels

**关键发现：**
- `_global_topk_masks` 已确认包含 per-layer mean normalization fix (`s_f / mu`)
- 旧 70% TEAL=17.91 是 **predictor-based TEAL**（`kl_sparsity70_s42_v2` 实验），不是 vanilla TEAL，二者不可直接比较
- Registry 中值已经一致（此次重跑确认了数据可靠性）
- 代码中无 "uniform" baseline（任务中标注"如果有"）
- Registry 和 artifact 已更新

**KL Predictor vs TEAL 对比（50% sparsity 为例）：**
- KL predictor PPL: 9.14（`mvp_kl_norm_v2_s456`）vs Vanilla TEAL: 23.31 → predictor 大幅优于 TEAL baseline

---
