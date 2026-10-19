# writing empirical section draft

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_empirical_section_draft_20260524T055523_result.json`
- **Structured JSON:** [`9eb3b3528e04c60b7b4a.json`](../../sessions/9e/9eb3b3528e04c60b7b4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已保存到 `artifacts/empirical_section_draft.tex`。

4段结构：
1. **Setup** — 8 configs (3 models × 2-3 prompting), HumAID K=10, analytical limits
2. **Topology ranking** — IV 最高 (30.3%), collider 最低 (4.9%), 与 Dirichlet simulation 一致
3. **F1 vs bias** — 整体 ρ=-0.156; per-topology 分解显示 IV (ρ=-0.700) 和 M-bias (ρ=+0.867) 方向相反，聚合后相消
4. **Sign flips** — 7/8 exposure sign flip, 0 sign flips across non-exposure topologies, IV 0% (vs Dirichlet 52.6%) 因 diagonal dominance

所有数字均可追溯到 `empirical_humaid_k10_results.json` (topology ranking, sign flips, F1 range) 和 `within_topo_f1_bias_results.json` (per-topology ρ 分解)。引用了 `Proposition~\ref{prop:signflip}` 和 `Appendix~\ref{app:empirical_details}`（后者需确认 label 是否存在）。

---
