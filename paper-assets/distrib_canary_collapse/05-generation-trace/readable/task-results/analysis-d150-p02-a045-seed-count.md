# analysis d150 p02 a045 seed count

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d150_p02_a045_seed_count_20260520T132027_result.json`
- **Structured JSON:** [`e07f5b5bacc4656000ac.json`](../../sessions/e0/e07f5b5bacc4656000ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/d150_p02_a045_seed_audit.md`。

**核心发现**：

- **实际 seed 数 = 2**（s42 + s43），无 s44
- **PermG 结果**：s42 = 0/8 (min FDR-p 0.091)，s43 = 0/8 (min FDR-p 0.059)，两 seed 一致
- **不一致确认**：`experiments.tex` L14-15 把 α=0.45 归入 "single-seed probing points"，但 appendix Table `fdr_gradient_a045` 明确报了 2 seeds 的数据

建议将 α=0.45 从 "seven single-seed probing points" 列表中移出，在 L15 补充说明其使用了 2 seeds {42, 43}。

---
