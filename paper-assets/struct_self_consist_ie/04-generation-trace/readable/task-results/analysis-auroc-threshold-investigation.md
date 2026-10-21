# analysis auroc threshold investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_auroc_threshold_investigation_20260516T111512_result.json`
- **Structured JSON:** [`1ba5bad4c246e988f2cd.json`](../../sessions/1b/1ba5bad4c246e988f2cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 调查结果

**根因**: `evaluation.py:compute_auroc` 用 `F1 > median`（strict），Paper Table 1 用 `F1 >= median`（inclusive）。SciERC NER 中 65 个 instance 恰好处于 median (F1=2/3)，被不同地分配到正/负类，导致系统性偏差 0.013–0.034。

## 已完成的修复

| 修改 | 内容 |
|------|------|
| `code/evaluation.py` (服务器) | `l > med` → `l >= med` |
| `artifacts/evaluation.py` (本地) | 同上 |
| `docs/paper/sections/appendix.tex` | 多 seed AUROC 行用修正值替换 |

## 关键结论

- **Table 1 无需更新** — 已用正确定义 (`>=`)
- **Appendix multi-seed AUROC 已更新** — 值降低 0.013–0.034
- **AUROC 信号排名不变** — VC>SJ>EM>FK>LP 在所有 seed×model 组合中一致
- **σ≤0.026 声明仍有效** — 修正后最大 σ=.016

输出保存在 `/root/autodl-tmp/struct_self_consist_ie/output/d114_auroc_investigation/`（investigation.md, unified_auroc.json, table1_update.md）。

---
