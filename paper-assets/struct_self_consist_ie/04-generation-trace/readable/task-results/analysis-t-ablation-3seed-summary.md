# analysis t ablation 3seed summary

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t_ablation_3seed_summary_20260521T044117_result.json`
- **Structured JSON:** [`36434bc653c22366f064.json`](../../sessions/36/36434bc653c22366f064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已保存并注册：

- **JSON**: `artifacts/t_ablation_3seed_summary.json` — 完整 mean±std 数据
- **Table**: `artifacts/t_ablation_table.md` — 论文用表格

**数据覆盖情况：**

| 数据集 | 3-seed 完整 | 缺失 |
|--------|------------|------|
| FewNERD | T=0.8 ✓ | T=0.5/1.2 缺 s456（RUNNING）；T=1.0 仅1seed 且不同 pipeline |
| CoNLL | T=0.5/0.8/1.2 ✓ | T=1.0 仅1seed |
| SciERC | T=0.5/0.8/1.0/1.2 ✓ | s42 来自 exp_026 analysis（NER only），pipeline 略有差异 |

**主要发现：**
1. Greedy F1 对 T 不敏感（CoNLL≈0.907, SciERC≈0.663, FewNERD≈0.789）
2. Oracle headroom 随 T 单调递增（更多多样性 → 更高理论上限）
3. ρ(SJ,F1) 在 T=0.8 达到峰值（diversity-noise 最佳平衡点）
4. ρ\_advantage 随 T 递增：结构一致性相对表面一致性的优势在高 T 下更明显
5. FewNERD T=1.0 数据需要等 `exp_fewnerd_n16_s*` 完成后补充

---
