# analysis fpr transparency table

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fpr_transparency_table_20260524T062949_result.json`
- **Structured JSON:** [`eaf133dd0cf092e5d76f.json`](../../sessions/ea/eaf133dd0cf092e5d76f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

1. **`artifacts/fpr_transparency_all_seeds.json`** — 6 seeds × 6 pairs 的完整 per-pair p-value 数据
2. **`artifacts/appendix_fpr_transparency_table.tex`** — 附录 LaTeX 表（36 行，K≥3 行灰底高亮）

关键数据：
- K≥3 FPR = **6/36 = 16.7%**（逐 seed: s45=1, s46=1, s47=2, s48=0, s49=0, s50=2）
- 6 个 K≥3 假阳全部由 **naive + threshold + TY** 三个弱方法驱动（无 PermG/DiffXcorr 参与）
- PermG FDR 假阳仅出现在 s45（2/6）和 s50（2/6），其他 4 seeds 均为 0/6

LaTeX 表需要额外加载 `\usepackage[table]{xcolor}`（用于 `\rowcolor`），文件顶部已注明。

---
