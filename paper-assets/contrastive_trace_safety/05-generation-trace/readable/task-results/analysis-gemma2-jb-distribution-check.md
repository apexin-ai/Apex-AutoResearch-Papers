# analysis gemma2 jb distribution check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_jb_distribution_check_20260522T165526_result.json`
- **Structured JSON:** [`e438262ec225fe5a67c4.json`](../../sessions/e4/e438262ec225fe5a67c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma-2 JB/Safe 分布报告

| 指标 | 数值 |
|------|------|
| 已完成 trace | **258 / 520** (49.6%) |
| JB (jailbreak) | **4** |
| Safe | **254** |
| **JB rate** | **1.55%** |
| 当前进度 | ~250/520, ETA ~27min |

**JB 出现位置**: #0026, #0123, #0185, #0256 — 分布稀疏，无聚集趋势。

**结论**: Gemma-2 JB rate (1.55%) 甚至低于 Gemma-4 的 2.7%。最近 70 条 (#185-#257) 中仅 2 条 JB。趋势持续偏低，需要调整策略。

---
