# verify pre mvp relaunch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_pre-mvp-relaunch_20260514T054825_result.json`
- **Structured JSON:** [`868cc1f721336a71d51d.json`](../../sessions/86/868cc1f721336a71d51d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 全部通过。汇报如下：

---

## 汇报

### 1. 代码一致性检查 — 全部通过

| 文件 | GQA group | MLP group | 状态 |
|------|-----------|-----------|------|
| cka_overlap.py | attn_cka_matrix [4 groups/layer] | mlp_cka_matrix [28 groups/layer] | ✅ |
| importance_score.py | attn_importance [4 groups/layer] | mlp_importance [28 groups/layer] | ✅ |
| prune.py | attn_keep_masks + GQA group pruning + forward validation | mlp_keep_masks + MLP channel pruning | ✅ |
| correlation_analysis.py | compute_attn_recoverability + n_gqa_groups | compute_mlp_recoverability + n_mlp_groups + combined | ✅ |
| rasp_scoring.py | attn_scores + attn_ranking | mlp_scores + mlp_ranking | ✅ |

无覆盖冲突，两个 Worker 的改动完整共存。

### 2. run_mvp.sh 修复内容

- **Step 1+2 改为并行**：CKA→cuda:0, Importance→cuda:1
- **所有 `wait` 改为逐个检查**：每个 PID 独立 wait + exit code 检测
- **新增 Step 3.5**：Post-prune eval（pruned_standard 和 pruned_rasp 的 GSM8K 评测）
- **correlation_analysis.py 加上** `--n_gqa_groups 4 --n_mlp_groups 28`
- **结果汇总更新**：新增 pruned eval 输出路径

### 3. 旧产出清理 — 完成

`models/pruned_standard_35`, `models/pruned_rasp_35`, `results/` 已删除。`models/DeepSeek-R1-Distill-Qwen-7B` (symlink) 保留。

### 4. Dry-run 验证结果

| 步骤 | 结果 |
|------|------|
| CKA (n=4) | ✅ 28 layers × 4 GQA groups + 28 MLP groups |
| Importance (n=4) | ✅ 28 layers × 4 GQA groups + 28 MLP groups |
| Standard prune | ✅ forward pass OK, sparsity=35.03% |
| RASP prune | ✅ forward pass OK, sparsity=35.03% |

**剪枝统计**：
- Standard: **0 attn GQA groups pruned**, 367/784 MLP groups pruned
- RASP: **0 attn GQA groups pruned**, 367/784 MLP groups pruned

### 5. 注意事项

**N_pruned_attn = 0**：两种模式在 35% sparsity 下均未剪任何 attention GQA group。全局排序下 GQA group 的 importance 分数普遍高于 MLP group，所以 367 个最低分结构全部落在 MLP 侧。这不是 bug，是全局排序在当前 sparsity 下的自然结果（4 GQA groups/layer × 28 layers = 112 vs 784 MLP groups，112 个 attn 结构全排在前面）。如果需要强制剪 attention，需要改为分组配额（如 attn 和 MLP 各自独立分配 sparsity）。

### 结论

**READY TO LAUNCH** — pipeline 端到端通过，代码一致，run_mvp.sh 已修复。唯一需决策：是否接受 35% sparsity 下 attn groups 不被剪的结果，还是需要改为 attn/MLP 分组配额剪枝。

---
