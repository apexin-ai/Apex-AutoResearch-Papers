# code cka fh reliability

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cka_fh_reliability_20260515T031935_result.json`
- **Structured JSON:** [`5d3b07ce98ead24a64e5.json`](../../sessions/5d/5d3b07ce98ead24a64e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确，所有新参数都在。

修改总结：
- **Phase 4** (`fh_attn_reliability`): 对原始模型 attention heads 做 split-half F(h) 排名 Spearman ρ，阈值 0.9
- **Phase 5** (`fh_mlp_reliability`): 对 MLP groups 做同样的 split-half F(h) reliability
- 新增 `collect_mlp_activations` 收集 gate_proj 激活（与 `cka_overlap.py` 一致）
- 新增 `compute_fh_scores` 计算 intra-layer pairwise CKA → F(h)
- 新增 `compute_fh_reliability` 做 n_splits 次 split-half 并报告 Spearman ρ
- `--pruned_model` 改为可选（`--skip_cross_model` 时不需要）
- `--mlp_groups` 默认 28
- 原始模型加载一次，两次 forward pass 分别收集 q_proj 和 gate_proj 激活
- Phase 1-3 保留不变，仅在未设 `--skip_cross_model` 时执行

---
