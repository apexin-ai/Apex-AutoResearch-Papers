# fix r15 sf4 sobel audit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r15-sf4-sobel-audit_20260523T063528_result.json`
- **Structured JSON:** [`db7caf6aff6cdb4e022d.json`](../../sessions/db/db7caf6aff6cdb4e022d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心结论：

**根因**：Worker 1 使用了不一致的数据子集。`verified_verbosity_filtered.jsonl` 是预过滤的（86条全部 passed_cf=True），但 `verified_32b.jsonl` 未过滤（100条中仅36条通过 NLI）。混入 64 条未验证的 formality 对拉高了 n，压低了 SE，导致 z 虚高。

**数值对照**：
| 子集 | n | Sobel z | Sobel p |
|------|---|---------|---------|
| Worker 1 混合（bug） | 186 | 3.36 | .0008 |
| passed_only（正确） | 122 | **2.15** | **.031** |
| all_pairs（参考） | 200 | 4.89 | <.001 |

**正确值**：z=2.15, p=.031（passed_only，与论文其他分析的数据宇宙一致）。中介效应仍显著（p<.05），定性结论不变，但 p 值差了约 40 倍。论文需将 "z=3.36, p<.001" 修正为 "z=2.15, p=.031"。

审计报告已写入 `artifacts/r15_analysis/sobel_audit.json`。

---
