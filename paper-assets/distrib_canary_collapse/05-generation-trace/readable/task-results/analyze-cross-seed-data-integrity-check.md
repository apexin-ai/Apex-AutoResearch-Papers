# analyze cross seed data integrity check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cross-seed-data-integrity-check_20260522T020315_result.json`
- **Structured JSON:** [`59bdb4e83065dd5408de.json`](../../sessions/59/59bdb4e83065dd5408de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 数据完整性汇总

### 1. t15_a045_s43 (westd-17855)

| 项目 | 状态 |
|------|------|
| gen 目录 | 2/16 (仅 gen_14, gen_15 保留，gen_0-13 已清理) |
| all_metrics.json | **完整** — 16 entries (gen_0 ~ gen_15) |
| analysis/ | 有 `5method_leadlag.json` + `5method_summary.txt` |
| 5method 结果 | PermG=6/8, DiffXCorr=6/8, Robust pairs=2/8 |

### 2. t15_a060_s43 (westd-17855)

| 项目 | 状态 |
|------|------|
| gen 目录 | **0** (全部清理) |
| all_metrics.json | **完整** — 16 entries (gen_0 ~ gen_15) |
| analysis/ | 有 `5method_leadlag.json` + `5method_summary.txt` |
| 5method 结果 | PermG=0/8, DiffXCorr=7/8, Robust pairs=2/8 |

### 3. t20_a045_s43 (westd-19828)

| 项目 | 状态 |
|------|------|
| gen 目录 | **21/21** (gen_0 ~ gen_20 全部保留) |
| all_metrics.json | **完整** — 21 entries (gen_0 ~ gen_20) |
| analysis/ | 有 `5method_leadlag.json` + `5method_summary.txt` |
| 5method 结果 | PermG=4/8, DiffXCorr=8/8, Robust pairs=5/8 |

### 结论

**三个实验的 all_metrics.json 均完整**，d102 分析基于 all_metrics.json 而非 gen 目录，因此：

- **t15_a045_s43**: all_metrics.json 有完整 16 entries (gen_0-15)，PermG=6/8 结果有效，**无需重跑实验**。gen 目录清理不影响分析结论。
- **t15_a060_s43**: all_metrics.json 完整 16 entries，分析有效。
- **t20_a045_s43**: gen 目录和 all_metrics.json 均完整 (21 entries)，数据最完整。

如需重跑 5method 分析（而非实验本身），all_metrics.json 足够支撑。

---
