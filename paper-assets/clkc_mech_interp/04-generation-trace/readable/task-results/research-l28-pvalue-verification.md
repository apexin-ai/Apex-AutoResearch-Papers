# research L28 pvalue verification

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_L28-pvalue-verification_20260524T072739_result.json`
- **Structured JSON:** [`3b63d688a041dc3739bb.json`](../../sessions/3b/3b63d688a041dc3739bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。以下是完整汇总。

---

## L28 原始数据与 p 值验证结果

### 1. 唯一存在的 JSON 文件：`steering_results_L28_last.json`

**Config**: N=201, position="last", probe_acc=0.8525

| alpha | steer_flips | ctrl_flips | steer% | ctrl% | JSON p | 验证 p |
|-------|------------|------------|--------|-------|--------|--------|
| -20.0 | 12 | 11 | 5.97 | 5.47 | 1.000 | 1.000 ✓ |
| -10.0 | 5 | 8 | 2.49 | 3.98 | 0.575 | 0.575 ✓ |
| -5.0 | 3 | 5 | 1.49 | 2.49 | 0.724 | 0.724 ✓ |
| +5.0 | 4 | 2 | 1.99 | 1.00 | 0.685 | 0.685 ✓ |
| **+10.0** | **6** | **2** | **2.99** | **1.00** | **0.284** | **0.284** ✓ |
| +20.0 | 16 | 15 | 7.96 | 7.46 | 1.000 | 1.000 ✓ |

**Best p = 0.284** at alpha=+10 — 与 `main.tex:79` Appendix 表一致。

### 2. N=136 旧实验（JSON 已不存在，从论文表格反推）

论文表格 `L28, alpha=-20, steer=14.7%, ctrl=16.9%, p=0.740`：
- 反推: steer=20/136=14.71%, ctrl=23/136=16.91%
- Fisher p 验证: **0.740** ✓（与 `main.tex:103` 和 `experiments.tex:184` 一致）

### 3. L28 (all) — 争议行

论文数据: steer=11.8%, ctrl=11.8%

验证: **不论 N=136 还是 N=201，当 steer 和 ctrl flip 计数相同或差 ±1 时，Fisher p 全部等于 1.000。** 不存在任何合理的 2×2 列联表能同时产生 11.8% vs 11.8% 的 flip rate 和 p=0.370。

### 4. 结论

| 位置 | 值 | 判定 |
|------|-----|------|
| `docs/paper/experiments.tex:185` | L28 (all) p = **1.000** | ✅ **正确** |
| `artifacts/_project/paper/experiments.tex:159` | L28 (all) p = **0.370** | ❌ **错误**（数学上不可能） |
| `main.tex:103` | L28 best p = 0.740 (N=136) | ✅ 正确（旧实验） |
| `main.tex:79` | L28 best p = 0.284 (N=201) | ✅ 正确（新实验） |
| Registry 曾报 p = 0.31 | — | ❌ 近似 0.284 但不精确，可能是取整或查找错误 |

**修复建议**: `artifacts/_project/paper/experiments.tex:159` 的 `0.370` 应改为 `1.000`。提交版 (`docs/paper/`) 的值已经是正确的。

---
