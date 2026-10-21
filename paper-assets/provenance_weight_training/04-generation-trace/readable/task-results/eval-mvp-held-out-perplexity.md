# eval mvp held out perplexity

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp-held-out-perplexity_20260514T070406_result.json`
- **Structured JSON:** [`99b0fa648552f5b68c37.json`](../../sessions/99/99b0fa648552f5b68c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结果

### 1. Train loss 是 weighted 还是 unweighted？

**代码证据**（`training/pretrain_weighted.py`, `compute_loss` 方法）：
- `uniform`: `loss = per_sample_loss.mean()` — 标准 unweighted CE
- `adaptive`/`grid`: `loss = (per_sample_loss * weights).sum() / weights.sum()` — **weighted loss**
- 日志记录的就是 `compute_loss` 的返回值，因此 adaptive 的 train_loss (~9.2) 和 uniform 的 train_loss (~7.3) **不可直接比较**

### 2. Held-out Eval Perplexity

| Model | Seed | Eval PPL (held-out) | Train Loss |
|-------|------|---------------------|------------|
| uniform | 42 | **17.69** | 7.310 |
| uniform | 123 | **17.69** | 7.312 |
| uniform | 456 | **17.70** | 7.289 |
| adaptive | 42 | **17.64** | 9.267 |
| adaptive | 123 | **17.63** | 9.267 |
| adaptive | 456 | **17.64** | 9.235 |

- **Uniform 均值**: 17.694 (std=0.008)
- **Adaptive 均值**: 17.639 (std=0.006)
- **Δ = -0.055 PPL**，adaptive 一致性地优于 uniform（3 个 adaptive seed 全部低于 3 个 uniform seed，无重叠）

### 3. Held-out 数据描述
- 来源：`data/human/eval_holdout.jsonl`，纯 FineWeb 人类文本（`source: fineweb`, `depth: 0`）
- 使用 5000 docs，~4.08M tokens
- 无合成数据污染

### 4. Eval 脚本
`/root/provenance_weight_training/eval_perplexity.py`
结果 JSON：`/root/autodl-tmp/provenance_weight_training/output/eval_perplexity_results.json`

### 5. 注意事项
- 效果差异较小（0.055 PPL / 0.3%），但方向一致、三个 seed 无重叠
- 训练进程未受干扰（eval 在 GPU 3 上与 grid-b 训练共享，模型仅 1.2GB）
- tokenizer 有一个 regex 警告但不影响结果（Qwen3 tokenizer 的已知 issue）

---
