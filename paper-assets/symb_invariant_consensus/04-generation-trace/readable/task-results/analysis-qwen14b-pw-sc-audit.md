# analysis qwen14b pw sc audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-pw-sc-audit_20260521T095214_result.json`
- **Structured JSON:** [`cccbd6407ae27e838444.json`](../../sessions/cc/cccbd6407ae27e838444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

## 三个值的来源

| 值 | 正确数 | 来源 | 出现位置 |
|---|---|---|---|
| **75.17%** | 451/600 | `sica_expanded_14b` (早期实验, westd-25068) | Main Table (experiments.tex) |
| **74.00%** | 444/600 | `exp032` (westd-16639) + **alphabetical tiebreaking** | Cross-gen NLI Table (solutions.tex) |
| **70.33%** | 422/600 | `exp034` intermediates (westd-25068, 已下线) | CIL 初始计算 (已修正为 74.00%) |

## 根因

**不是 tiebreaking 差异，是三次不同的实验 run**（不同 trace 生成），产生了不同的 SC 正确数（451 vs 441 vs 422）。

Tiebreaking 只在 exp032 上造成额外 ~0.5pp 差异：
- **21 个 tie**（3.5%），全部是 6:6 平票（K=12）
- First-seen: 441/600 = 73.50%
- Alphabetical: 444/600 = 74.00%（+3 正确）
- Random: 435-442/600（72.50%-73.67%）

## Canonical 推荐

**73.50%**（exp032, first-seen tiebreaking）：
- exp032 是可访问服务器上的完整 run，有全部 per-question 数据
- NLI combo 实验 (exp-091) 基于同一组 traces
- First-seen 匹配原始 SICA pipeline 行为

**关键不一致**：Main Table 用 sica_expanded_14b (75.17%)，NLI 分析用 exp032 (73.50/74.00%)——同一模型同一数据集引用了不同实验 run 的结果。需统一。

---
