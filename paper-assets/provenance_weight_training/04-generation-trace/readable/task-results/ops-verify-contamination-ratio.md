# ops verify contamination ratio

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-contamination-ratio_20260514T093910_result.json`
- **Structured JSON:** [`a8af71aa55565ce8eeb0.json`](../../sessions/a8/a8af71aa55565ce8eeb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

## 验证结果

### 代码分析

`tau = 1 - contamination_ratio * 0.5`（第 275 行）

三种模式对 tau/contamination_ratio 的使用：

- **uniform**（第 138-139 行）：`loss = per_sample_loss.mean()`，**不使用** q_scores/tau/b，纯等权平均
- **grid**（第 140-146 行）：`weights = compute_sample_weights(q_scores, b_val)`，用固定 b 值计算 `(1-q)^b`，**不使用** tau
- **adaptive**（第 147-153 行）：`b_val = find_optimal_b(q_scores, tau=self.tau, n_min=self.n_min)`，**使用** tau

### 日志确认表

| 实验 | 命令行传参 | 日志确认值 | tau | 是否影响结果 |
|------|-----------|-----------|-----|-------------|
| uniform_seed42 | 无（默认 0.2） | **0.2** | 0.9 | **不影响**（uniform 不用 tau） |
| uniform_seed123 | 无（默认 0.2） | **0.2** | 0.9 | **不影响** |
| uniform_seed456 | 无（默认 0.2） | **0.2** | 0.9 | **不影响** |
| adaptive_seed42 | 0.4 | **0.4** | 0.8 | ✅ 正确 |
| adaptive_seed123 | 0.4 | **0.4** | 0.8 | ✅ 正确 |
| adaptive_seed456 | 0.4 | **0.4** | 0.8 | ✅ 正确 |
| grid_b_seed42_batch | **0.4**（脚本确认） | **0.4** | 0.8 | **不影响**（grid 不用 tau） |
| grid_b0_5_seed123 | 0.4 | **0.4** | 0.8 | **不影响** |
| grid_b1_0_seed123 | 0.4 | **0.4** | 0.8 | **不影响** |
| grid_b1_5_seed123 | 0.4 | **0.4** | 0.8 | **不影响** |

### 关键结论

1. **grid_b_seed42_batch**：`run_grid_b_seed42.sh` 显式传了 `--contamination_ratio 0.4`，日志确认 0.4。✅ 无问题。

2. **uniform 模式不受 contamination_ratio 影响**：代码路径直接走 `per_sample_loss.mean()`，不涉及 q_scores、tau 或 b。虽然日志记录的是默认值 0.2，但该值完全未被使用（运行时 b=0, alpha_eff=1.0, ESS=4.0 也佐证了这一点）。

3. **grid 模式不受 contamination_ratio 影响**：权重计算 `compute_sample_weights(q_scores, b_val)` 只依赖 q_scores 和固定 b 值，不经过 tau。

**所有实验结果有效，无需重跑。**

---
