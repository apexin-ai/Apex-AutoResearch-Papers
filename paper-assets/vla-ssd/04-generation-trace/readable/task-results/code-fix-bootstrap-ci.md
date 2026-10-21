# code fix bootstrap ci

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-bootstrap-ci_20260515T112616_result.json`
- **Structured JSON:** [`d40bf1a28658075a7054.json`](../../sessions/d4/d40bf1a28658075a7054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Smoke test 通过。结果验证：

- **`per_task_rho`**: 10 个 task 各自的 Spearman ρ 已正确输出（范围 0.41–0.68）
- **`per_task_n_pairs`**: 每个 task 500 对，记录完整
- 全局 `spearman_rho=0.5542` 与 per-task 均值一致

**已完成的修改：**

1. **`train_probes.py`**:
   - `train_regression_probe` 现在返回 `(metrics, pred, y_np)` 三元组
   - `run_temporal_distance` 按 task 分组 val pairs，对每个 task 单独计算 Spearman ρ，输出 `per_task_rho` 和 `per_task_n_pairs`
   - `run_oracle` 适配新返回格式

2. **`analyze_results.py`**:
   - `bootstrap_delta_rho` 改为 task-level bootstrap：以 best layer 的 per-task ρ 为采样单元，返回 `(observed_delta, ci_lower, ci_upper, p_value)`，附加 permutation test
   - `compute_judgment` 在 best layer 上用 task-level bootstrap 计算 CI，判定条件改为 `ci_lower > 0 AND p_value < 0.05`

3. 原文件已备份为 `.bak2`

---
