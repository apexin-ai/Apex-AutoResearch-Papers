# analysis fdr gradient a045

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fdr_gradient_a045_20260520T110756_result.json`
- **Structured JSON:** [`de80633c8b175343d39e.json`](../../sessions/de/de80633c8b175343d39e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地和远程均无 git 仓库，无法执行 git commit。两个文件已生成并注册：

- `artifacts/fdr_gradient_a045.json` — 8 pairs × 2 seeds 完整 fdr_p 数据
- `artifacts/fdr_gradient_interpretation.md` — 表格 + 解读 + cross-seed stability 评估

关键数据摘要：
- **s42**: 0/8 FDR-significant，min_fdr_p = 0.091
- **s43**: 0/8 FDR-significant，min_fdr_p = 0.059
- Cross-seed min_fdr_p 差异 1.55×（0.059 vs 0.091），mauve pairs 在两个 seed 中均最弱

---
