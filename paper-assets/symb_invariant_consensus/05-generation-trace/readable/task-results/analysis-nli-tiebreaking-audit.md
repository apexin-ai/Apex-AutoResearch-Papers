# analysis nli tiebreaking audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-tiebreaking-audit_20260521T050838_result.json`
- **Structured JSON:** [`898c756d9f2df51236a4.json`](../../sessions/89/898c756d9f2df51236a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。核心发现：

## BUG 确认

**所有 NLI combo 脚本** 使用 `Counter.most_common(1)[0][0]`（insertion-order tiebreaking），**DRC cascade pilot** 使用 alphabetical tiebreaking。论文的 SC baseline 已统一为 alphabetical，但 NLI combo 没有同步修复。

## Mistral-7B PW600 重算结果

| Weight | Paper (Counter) | Corrected (Alpha) | Delta | Changed Qs |
|--------|-----------------|-------------------|-------|------------|
| w=1 | 40.17% (241) | 40.17% (241) | 0pp | 17 |
| **w=3** | **42.83% (257)** | **46.00% (276)** | **+3.17pp** | 30 |
| w=5 | 50.00% (300) | 50.33% (302) | +0.33pp | 53 |

**McNemar (combo_w3 vs SC)**: p 从 0.0125 变为 **1.1e-05**（显著性大幅提升）

DRC pilot cross-check: 276/600 = 46.0% — **完美匹配** alphabetical 重算结果。

## SC baseline 本身
11 题在两种 tiebreaking 下结果不同，但总正确数恰好相同 (236/600)。

## FOLIO
8 题受影响，alphabetical 反而更差 (-1.47pp: 56.37% vs 57.84%)。

## 其他 3 个模型
原始数据在 westd-16639，用了相同的 `Counter.most_common()` 代码，需从原服务器重算。高 SC 模型 (70-85%) 预期影响较小。

## 建议行动
1. 用 alphabetical tiebreaking 重算全部 4 个 PW 模型的 NLI combo
2. Mistral w=3 从 42.83% → 46.00%，McNemar p 从 0.0125 → 1.1e-05
3. 重跑 BH correction table
4. 修复所有 combo 脚本的 tiebreaking 代码

---
