# code plan b batch adaptive tau

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_b_batch_adaptive_tau_20260516T101050_result.json`
- **Structured JSON:** [`a91b1e014cb7875c04f8.json`](../../sessions/a9/a91b1e014cb7875c04f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，3 步全部通过。`tau_batch` 按 batch 自适应调整：

| Step | mean_q | tau_batch | b* | alpha_eff |
|------|--------|-----------|-----|-----------|
| 0 | 0.654 | 0.646 | 0.628 | 0.646 |
| 1 | 0.582 | 0.718 | 0.448 | 0.718 |
| 2 | 0.580 | 0.720 | 0.460 | 0.720 |

tau_batch 在 0.646~0.720 之间变化（全局 τ=0.8），符合预期：batch 越脏（mean_q 越高，natural α_eff 越低），tau_batch 越低，减少不可能达成的过度干预。

## 汇报

### 代码改动

1. **`weighting/alpha_eff.py`**：新增 `find_optimal_b_adaptive_tau()` 函数（插入在 `compute_concentration_bound` 之后、`if __name__` 之前）
   - 计算 `alpha_eff_natural = compute_alpha_eff(q_scores, 0.0)`
   - `tau_batch = clamp(alpha_eff_natural + delta, tau_min, tau)`
   - 用 `tau_batch` 调用 `find_optimal_b`，返回 `(b_star, tau_batch)`

2. **`training/pretrain_weighted.py`**（9 处修改）：
   - 新增 import `find_optimal_b_adaptive_tau`
   - `WeightedTrainer.__init__` 新增 `adaptive_tau`, `tau_delta`, `tau_min` 参数
   - `compute_loss` 的 `adaptive` 分支：`adaptive_tau=True` 时调用新函数
   - `step_info` 和 wandb 日志增加 `tau_batch` 字段
   - `parse_args` 新增 `--adaptive_tau`, `--tau_delta`, `--tau_min` 三个 CLI 参数
   - `WeightedTrainer` 构造传参
   - `config_summary` 记录新参数

### 脚本路径

- `scripts/run_batch_adaptive_tau_rho04_seed42.sh` — ρ=0.4, τ=0.8, delta=0.3, τ_min=0.5
- `scripts/run_batch_adaptive_tau_rho06_seed42.sh` — ρ=0.6, τ=0.7, delta=0.3, τ_min=0.5

### 向后兼容

`--adaptive_tau` 默认 False，不加此 flag 时行为完全不变。

---
