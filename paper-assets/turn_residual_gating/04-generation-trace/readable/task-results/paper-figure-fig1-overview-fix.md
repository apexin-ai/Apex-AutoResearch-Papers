# paper figure fig1 overview fix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_overview_fix_20260519T200811_result.json`
- **Structured JSON:** [`39c779914530ab1dd299.json`](../../sessions/39/39c779914530ab1dd299.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 和 PNG 均已生成。

修改总结：

1. **字号 ≥ 7pt** — 所有 `fs=` 参数已从 4/4.5/4.8/5/5.5/6/6.5 提升至 ≥7pt；图高从 `6/16` 改为 `8/16` 以容纳更大文字；部分文字适当简化（"IID evaluation" → "IID eval"，"Gate should recover goal attention" 等）
2. **术语修正** — "Same-dist eval" → "IID eval"
3. **数据来源标注** — GAR 0.02→0.48 和 GAR=0.49 加 "(§5, Table 1)"；GAR=0.016 加 "(Table 1)"；↓ 70.8% 加 "(§3)"；AUC=0.98 加 "(Dongre et al.)"
4. **PCGrad 引用** — 改为 "① Gradient conflict → PCGrad / ablation (§6.3) → not causal"（分两行显示，带删除线）

---
