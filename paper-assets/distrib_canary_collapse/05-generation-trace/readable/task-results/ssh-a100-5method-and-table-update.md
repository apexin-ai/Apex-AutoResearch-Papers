# ssh a100 5method and table update

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a100_5method_and_table_update_20260517T094159_result.json`
- **Structured JSON:** [`6e9d7f0928da52e60d9e.json`](../../sessions/6e/6e9d7f0928da52e60d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出总结

### 1. Per-method per-seed sig counts at α=1.0 (seeds 42, 43, 45)

| Method | s42 | s43 | s45 |
|---|---|---|---|
| Naive XCorr | 8/8 | 8/8 | 8/8 |
| Diff XCorr (FDR) | 8/8 | 8/8 | 8/8 |
| Threshold Onset | 8/8 | 8/8 | 8/8 |
| Perm Granger (FDR) | 6/8 | 6/8 | 6/8 |
| TY Granger | 6/8 | 6/8 | 4/8 |

PermG 和 TY 未检出的 2-4 pairs 全部是 `→perplexity` 方向（entropy→ppl, ece→ppl），跨 seed 完全一致。

### 2. 分类（ground truth = YES causal signal）

| Method | Majority ≥4/8? | Verdict | Classification |
|---|---|---|---|
| Naive XCorr | 3/3 seeds | sig | ✓ correct |
| Diff XCorr | 3/3 seeds | sig | ✓ correct |
| Threshold Onset | 3/3 seeds | sig | ✓ correct |
| Perm Granger | 3/3 seeds | sig | ✓ correct |
| TY Granger | 3/3 seeds (6,6,4 all ≥4) | sig | ✓ correct |

### 3. Consensus (K≥3/5) at α=1.0
5/5 methods agree → **✓ correct**

### 4. LaTeX 表格已更新
- 服务器: `docs/paper/tables/single_method_errors.tex`（真源，per C002）
- 本地: `artifacts/tables/single_method_errors.tex`
- 已注册 artifact `art_20260517_ae8937`

注：α=1.0 数据来自 `method_ablation_phase2_panel.json`（n_perm=1000），原始 mvp_v4 训练目录已清理。α=1.0 效应量极大（f²>100），n_perm 差异不影响任何结论。

---
