# paper fix table2 355m 2seed mean

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_table2_355m_2seed_mean_20260514T084140_result.json`
- **Structured JSON:** [`c67442e276480418d7e4.json`](../../sessions/c6/c67442e276480418d7e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§5.7 验证通过：

- Line 145: RGDS mean=86.55, Random=71.40, +21% — (86.55−71.40)/71.40×100=21.2% ✓
- Line 151: +21% perplexity penalty ✓
- Table 3 (tab:medium_comparison) 已有两 seed 的 per-seed 数据 ✓

完成的修改：

1. **Table 2 355M Δ 值**：+12.59→+15.15, −21.41→−17.96, −8.82/+3.20→−2.81；新增 RGDS vs External-only +7.90
2. **355M 节标题**：`statistical tests pending ≥3 seeds` → `n=2 seeds (42, 123); seed=456 pending`
3. **脚注**：移除 †/‡ 标注，替换为 `355M: n=2 seeds (42, 123); seed=456 pending; t-tests deferred until n≥3`
4. **§5.7**：已有数字与 Table 2 一致，无需改动

---
