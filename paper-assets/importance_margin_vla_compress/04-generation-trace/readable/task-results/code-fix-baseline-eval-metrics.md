# code fix baseline eval metrics

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-baseline-eval-metrics_20260515T201138_result.json`
- **Structured JSON:** [`73940e34732d501718ac.json`](../../sessions/73/73940e34732d501718ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。结果符合预期：

**修改内容 (evaluate.py)**：

1. **行 279-319**（原 baseline 路径）：在 `baseline_forward()` 计算 action_loss 后，新增 random importance score 生成和 metric 计算：
   - 用 `torch.rand(B, 64)` 生成均匀分布 random scores（通过 `torch.Generator` + seed 确保可复现）
   - epsilon>0 时生成独立 random scores 作为 scores_pert，epsilon=0 时 scores_pert = scores_clean
   - 计算 margin、preservation_rate、kendall_tau、certified_bound、l_eps_delta_ratio 并追加到累积列表

2. **行 365**：`if imm_enabled and all_margins:` → `if all_margins:` — 去掉 imm_enabled 守卫，使 baseline 也能聚合 metric

3. **行 436-447**（main 的 Gate Summary）：去掉 `if imm_enabled:` 包裹，baseline 也输出 summary；新增 margin_median 字段

**验证结果**：
- margin_median ≈ 0.005（random uniform 的 margin 很小，符合预期）
- preservation = 1.0（eps=0 时，同一 scores 的 top-k 完全一致）
- preservation ≈ 0.36（eps>0 时，两组独立 random scores 的 top-k 重叠率低，符合预期）
- l_eps_delta_ratio = 0.0（baseline 无 Lipschitz 常数，L=0）
- 可复现性检验通过

---
