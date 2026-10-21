# fix precision unification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_precision-unification_20260524T062228_result.json`
- **Structured JSON:** [`5a3063b7fe075aaee4b7.json`](../../sessions/5a/5a3063b7fe075aaee4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功（29 pages）。

## 修改清单

### 已修复的 3 处 inline-vs-table precision mismatch

| 文件 | 行号 | 旧值 | 新值 | 原因 |
|------|------|------|------|------|
| analysis.tex | 118 | `$\Delta = -18.6$\,pp` | `$\Delta = -18.63$\,pp` | Table tab:method_interventions 有 -18.63 |
| analysis.tex | 40 | `$p = 0.008$` | `$p = 0.0083$` | Table tab:process-gradient caption 有 $p = 0.0083$ |
| diagnosis.tex | 138 | `$-18.6$\,pp` | `$-18.63$\,pp` | 同上，同一 Debate Δ 值 |

### 用户列出的 12 对 — 全部为不同数字，跳过

逐一验证后，12 对均为**不同指标**碰巧数值相近：

| # | analysis.tex | experiments.tex | 判定 |
|---|-------------|-----------------|------|
| 1 | 无 2.5 数据值（仅模型名） | -2.50 (Δ) | 找不到 |
| 2 | ≈1.0× (体积放大) | -1.00 (Δ) | 不同指标 |
| 3 | ρ = -1.0 (Spearman) | 1.000 (p-value) | 不同指标 |
| 4 | 83.3% (约束支持率, Mistral-7B) | 83.33 (SC accuracy, Qwen3-14B) | 不同指标 |
| 5 | κ range 0.41–0.51 | κ range [0.45, 0.51] | 不同范围 |
| 6 | K_eff shift < 0.5 | 0.581 (p-value) | 不同指标 |
| 7 | 同上 | +0.50 (Δ) | 不同指标 |
| 8 | CV = 0.26 | 0.267 (p-value) | 不同指标 |
| 9 | p = 0.008 (Spearman) | 0.00 (Δ) | 不同指标 |
| 10 | 2.65 (BR, gpt-4o table) | 2.6× (SC-correct ratio) | 不同指标 |
| 11 | 0.00 (Δ, table) | p < 0.001 | 不同指标 |
| 12 | 0.172 (MAX-SAT exclusion rate) | -0.17 (Δ) | 不同指标 |

### Orphan bib entry

`kamoi2024selfcorrect` **并非 orphan** — 在 related_work.tex:22 有引用：`\citep[cf.][]{kamoi2024selfcorrect}`。未删除。

---
