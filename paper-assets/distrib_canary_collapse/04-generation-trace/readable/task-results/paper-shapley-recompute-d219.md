# paper shapley recompute d219

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_shapley_recompute_d219_20260524T085055_result.json`
- **Structured JSON:** [`3f5c23fdb5522e080082.json`](../../sessions/3f/3f5c23fdb5522e080082.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Shapley v3 结果 (6-seed null, 36 pairs)**

| Method | φ^FPR | φ^FNR | φ^comb |
|--------|-------|-------|--------|
| Naive | +0.609 | -0.419 | +0.190 |
| **DiffXCorr** | **+0.007** | **-0.306** | **-0.299** |
| Threshold | +0.111 | -0.027 | +0.084 |
| PermG | +0.039 | -0.180 | -0.141 |
| TY | +0.150 | -0.069 | +0.082 |

**关键变化**: DiffXCorr 取代 PermG 成为 combined Shapley 最优方法（-0.299 vs -0.141），因其 FPR 极低（1/36=2.8%）。PermG 仍是最优 directional method。

**更新清单**:
- `artifacts/shapley_v3/shapley_values_v3.json` — 新 Shapley 数据
- `docs/paper/figures/gen_shapley_contribution.py` — 指向 v3 数据，移除 "zero FPR" 标注
- `docs/paper/figures/shapley_method_contribution.pdf/png` — 重新生成
- `docs/paper/appendix.tex` — 7 处 TODO-D219 全部删除并更新：
  - FDR sensitivity table: null 改为 /36 (3/4/8 at q=0.01/0.05/0.10)
  - Shapley intro: 6 null seeds 45-50, 36 pairs
  - Shapley body: DiffXCorr best overall, PermG best directional
  - Shapley table: 新数值，DiffXCorr 加粗
  - Figure caption: 更新
  - 8-pair robustness: DiffXCorr -0.263, PermG -0.112
  - Weight robustness: 标注使用 3-seed null，注明 6-seed 结果偏移

**FDR sensitivity (null)**:
- q=0.01: 3/36, q=0.05: 4/36, q=0.10: 8/36

---
