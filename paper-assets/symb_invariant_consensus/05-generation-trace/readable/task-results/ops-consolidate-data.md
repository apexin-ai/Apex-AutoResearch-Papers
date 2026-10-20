# ops consolidate data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_consolidate-data_20260525T204351_result.json`
- **Structured JSON:** [`d8033ffc7323f7d32fd2.json`](../../sessions/d8/d8033ffc7323f7d32fd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 迁移汇报

**1. 归档路径和总大小**
- 路径：`/root/symb_invariant_consensus_archive/westd-30973/`（16639 上）
- 总大小：**5.3M**
- 本地 symlink：`/root/symb_invariant_consensus_archive/local/` → 16639 自有数据

**2. 文件数对比**
- 源（30973）：**104 个文件**（results 3 + artifacts 5 + scripts 87 + folio_traces 8 + autodl-tmp/results 3，figures 目录不存在已跳过）
- 归档（16639）：**104 个文件** — 完全匹配

**3. 传输异常**
- `/root/symb_invariant_consensus/figures/` 在 30973 上不存在，已自动跳过，无影响

**4. 重复文件（30973 独有但 16639 已有）**
artifacts/ 目录下 **5 个文件全部重复**（文件名、大小、时间戳完全一致）：
| 文件 | 大小 |
|------|------|
| capability_gap_scatter.pdf | 33K |
| capability_gap_scatter.png | 124K |
| deberta_ft_combo_all.json | 2.6K |
| nli_recompute_exp091_exp092.json | 1.4K |
| nondeterminism_root_cause.md | 1.8K |

这 5 个文件已在 16639 本地 `/root/symb_invariant_consensus/artifacts/` 中存在相同副本，归档中的是冗余备份。

---
