# ops prep 30 sparsity

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_30_sparsity_20260516T084317_result.json`
- **Structured JSON:** [`e39c70e405273c016268.json`](../../sessions/e3/e39c70e405273c016268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 30% Sparsity 准备报告

### 1. prune.py 支持情况
- `--sparsity` 参数接受任意 float，30% 直接可用
- 无 `--dry_run` 参数
- 需要外部文件：`--importance_path` (必需) + `--cka_path` (RASP 模式必需)

### 2. Scores 可复用
Scores 是 per-head/per-layer 的绝对值。RASP 组合公式：`importance * (1 - overlap)^alpha`。sparsity 参数只决定剪多少结构（threshold），**不影响 score 计算，无需重算**。

Score 文件位置：
- `/root/recovery_aware_struct_prune/results/importance_scores.pt` (17KB)
- `/root/recovery_aware_struct_prune/results/cka_scores.pt` (122KB)

### 3. RASP 30% 已完成

| 指标 | 值 |
|------|-----|
| 路径 | `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30/` |
| 目标 sparsity | 30.00% |
| 实际 sparsity | **28.73%** |
| 剪枝参数量 | 5,427,842,560 |
| Attn GQA groups 剪枝 | 0 / 112 |
| MLP groups 剪枝 | 301 / 784 |
| Forward pass | OK |
| 磁盘占用 | 11GB |

注意：实际 28.73% < 目标 30%，因为 `min_keep_mlp` 约束（每层保留 ≥40% MLP 容量）限制了进一步剪枝。同时 RASP scoring 将所有注意力 group 评为高重要性，0 个被剪。

### 4. Standard 30% — 磁盘空间不足

当前 `/root/autodl-tmp` **仅剩 8.7GB**，standard 30% 需要 ~11GB，无法执行。

可清理候选（需确认）：

| 目录 | 大小 | 说明 |
|------|------|------|
| `pruned_rasp_alpha_0.0` | 12GB | 20% α=0 消融模型 |
| `pruned_rasp_alpha_1.0` | 12GB | 20% α=1 消融模型 |
| `grpo_stage2_standard_20_v8` | 12GB | 旧 GRPO checkpoint |
| 多个空 GRPO 目录 | ~0 | v5/v6/v7 等 |

### 5. 预计 SFT 后模型大小
- 30% 剪枝后模型 ~11GB (bf16)
- SFT 后大小类似（同参数量，不同权重值）

### 需要你决定
清理哪些旧产物来释放空间给 `pruned_standard_30`？

---
