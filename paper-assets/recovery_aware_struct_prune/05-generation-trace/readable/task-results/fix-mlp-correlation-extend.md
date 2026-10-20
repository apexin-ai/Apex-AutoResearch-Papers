# fix mlp correlation extend

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mlp-correlation-extend_20260514T052804_result.json`
- **Structured JSON:** [`679520d33609aba32add.json`](../../sessions/67/679520d33609aba32add.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

--help 验证通过。汇报：

### 1. cka_overlap.py — 无需修改
`mlp_cka_matrix` 已存在。输出包含 `attn_overlap`, `mlp_overlap`, `attn_cka_matrix`, `mlp_cka_matrix` 四个 key。

### 2. prune.py — 无需修改
`pruning_metadata.pt` 已包含 `attn_keep_masks` 和 `mlp_keep_masks`。

### 3. correlation_analysis.py — 重写完成

**修复的问题**：
- 旧代码用 `n_heads=28`（Q head 数）做 recoverability 计算，但 CKA matrix 是 `[4, 4]`（GQA group 粒度），会 index out of bounds。改为用 `--n_gqa_groups=4`，与 CKA matrix 和 pruning_metadata 的 GQA group 粒度对齐。

**新增内容**：
- `collect_all_activations()` — 单次 forward pass 同时 hook q_proj + gate_proj，收集 attention GQA group 和 MLP group 两种激活，避免重复推理
- `compute_attn_recoverability()` — GQA group 粒度的 attention recoverability
- `compute_mlp_recoverability()` — MLP group 粒度的 recoverability（hook gate_proj，按 group_size 切分 intermediate channels）
- `compute_correlation_stats()` — 统一的统计计算（Spearman rho + bootstrap CI + permutation test），处理 N<3 的退化情况
- 新增 `--n_gqa_groups`（default=4）和 `--n_mlp_groups`（default=28）参数

### 4. 输出格式
```json
{
  "attention": { "spearman_rho", "p_value", "bootstrap_ci_95", "permutation_p_value", "n_pruned_groups", "per_group_data" },
  "mlp":       { ... 同上 ... },
  "combined":  { ... + "n_total_pruned" },
  "mvp_verdict": "PASS/WARNING/FAIL"  // 基于 combined rho
}
```

Scatter plots：
- `fh_vs_recoverability_attention.png`（按 layer 着色）
- `fh_vs_recoverability_mlp.png`（按 layer 着色）
- `fh_vs_recoverability_combined.png`（按 attention/MLP 类型着色，蓝/橙区分）

### 5. --help 验证通过
新增参数 `--n_gqa_groups`, `--n_mlp_groups` 正确显示。

---
