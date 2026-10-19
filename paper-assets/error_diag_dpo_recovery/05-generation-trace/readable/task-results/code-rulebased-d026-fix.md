# code rulebased d026 fix

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rulebased-d026-fix_20260512T232423_result.json`
- **Structured JSON:** [`f24a060ad4d6742a129e.json`](../../sessions/f2/f24a060ad4d6742a129e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### 修改前 vs 修改后对比（v6, 21 条 matched failures）

| 类别 | 修改前 | 修改后 |
|------|--------|--------|
| **action** | ~80% (17) | **14.3% (3)** |
| **verification** | ~20% (4) | **14.3% (3)** |
| **planning** | 0% (0) | **71.4% (15)** |

### Late-divergence subset（divergence_step > 1，共 5 条）

| 类别 | 数量 | 比例 |
|------|------|------|
| action | 3 | 60% |
| verification | 2 | 40% |
| mean correction span (action) | 5.7 | min=4, max=8 |

### 已完成
1. `classify_errors_rulebased.py` — step-1 divergence 的 action 规则（wrong_object/instance/receptacle/verb）override 为 planning，`rule_fired` 带 `_step1_planning` 标记
2. 新增 late-divergence subset 分析（error type 分布 + correction span by type）+ step-1 override 汇总
3. `outputs/p1_analysis.json` 和 `data/classified/p1_analysis.json` 已备份为 `*_pre_d026_backup.json`
4. 原文件备份在 `src/classify_errors_rulebased.py.bak_pre_d026`

---
