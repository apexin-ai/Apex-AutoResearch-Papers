# eval sparsity30 v3 correct target

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sparsity30_v3_correct_target_20260515T225829_result.json`
- **Structured JSON:** [`b92dc1ae1185195e9902.json`](../../sessions/b9/b92dc1ae1185195e9902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P0-A 完成了！结果如下：

---

## 1. P0-A: sparsity30_v3 正确 eval 结果（`--sparsity_target 0.3`）

| 指标 | 值 |
|------|-----|
| **true_dense_ppl** | 6.12 |
| **predictor_hard_mask_ppl** | 7.30 |
| **teal_sparse_ppl** | **8.98** |
| **model_level_sparsity** | 0.300 (精确 30%) |

**与旧结果对比：**
- 旧 teal_sparse_ppl = 8.76（@ 50% target，错误配置）
- 新 teal_sparse_ppl = **8.98**（@ 30% target，正确配置）
- 差值 +0.22，说明旧的 50% target mask 恰好比 30% target 更激进地裁剪，但 PPL 差异不大

Per-layer sparsity 分布合理：早期层低（0.13-0.23），中间层升高（0.30-0.34），最后几层最高（0.50-0.70），全局平均精确命中 0.300。

---

## 2. P0-C: 70% eval 交叉检查

**结论：kl_sparsity70_s42 的 predictor eval 从未正确完成过。**

证据：
- `plan_007_sparsity70.json` 记录 `"sparsity70_hard_mask": "not_measured_killed"`——predictor eval 被 kill 了
- `sparsity70_teal: 17.913` 是 TEAL static mask baseline，不是 predictor eval
- `eval_benchmark.py` 的 CONDITIONS 字典中**没有** sparsity30/sparsity70 的 predictor 条件
- `eval_benchmark.py` 默认 `SPARSITY_TARGET = 0.5`
- checkpoint 目录是 `kl_sparsity70_s42`（无 v2 后缀）
- 无 bash_history，无法追溯历史命令中是否传了 `--sparsity_target 0.7`

**判定：70% 数据点无效，需要用 `--sparsity_target 0.7` 重跑 predictor eval。**

---

## 新规范确认

所有 sparsity sweep 的 eval 必须显式传 `--sparsity_target`，禁止依赖默认值 0.5。后续需要重跑：
- `kl_sparsity70_s42` predictor eval：`--checkpoint checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt --sparsity_target 0.7`

---
