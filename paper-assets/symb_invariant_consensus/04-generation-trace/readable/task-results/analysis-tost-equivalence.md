# analysis tost equivalence

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-equivalence_20260520T152416_result.json`
- **Structured JSON:** [`4ba42bde7a90e0f6fb4f.json`](../../sessions/4b/4ba42bde7a90e0f6fb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是 TOST 结果汇总：

## TOST Equivalence Test — Table 1 (15 条件, margin ±2pp, α=0.05)

| # | Condition | n | Δ(pp) | b | c | b+c | TOST p | Eq? |
|---|-----------|---|-------|---|---|-----|--------|-----|
| 1 | Mistral-7B FOLIO s42 | 204 | +4.9 | 2 | 12 | 14 | 0.943 | NO |
| 2 | Mistral-7B FOLIO s789 | 204 | -0.5 | 6 | 5 | 11 | 0.177 | NO |
| 3 | Qwen2.5-14B FOLIO def | 204 | -0.5 | 3 | 2 | 5 | 0.084 | NO |
| 4 | Qwen2.5-14B FOLIO s123 | 204 | +0.5 | 1 | 2 | 3 | **0.038** | **YES** |
| 5 | Qwen2.5-7B FOLIO (r1) | 204 | -0.5 | 2 | 1 | 3 | **0.038** | **YES** |
| 6 | Qwen2.5-7B FOLIO (r2) | 204 | +0.5 | 3 | 4 | 7 | 0.122 | NO |
| 7 | Qwen3-14B FOLIO | 204 | +0.5 | 4 | 5 | 9 | 0.152 | NO |
| 8 | Gemma-2-7B FOLIO | 204 | -0.5 | 1 | 0 | 1 | **0.001** | **YES** |
| 9 | Qwen2.5-14B PW-600 | 600 | +0.5 | 12 | 15 | 27 | **0.042** | **YES** |
| 10 | Mistral-7B PW-600 | 600 | -2.8 | 30 | 13 | 43 | 0.777 | NO |
| 11 | Qwen2.5-7B PW-600 | 600 | -4.0 | 36 | 12 | 48 | 0.958 | NO |
| 12 | Mistral-7B LogiQA-200 | 200 | -3.0 | 11 | 5 | 16 | 0.692 | NO |
| 13 | Qwen2.5-7B LogiQA def | 200 | +2.5 | 1 | 6 | 7 | 0.647 | NO |
| 14 | Qwen2.5-7B LogiQA s123 | 200 | -0.5 | 3 | 2 | 5 | 0.090 | NO |
| 15 | Qwen2.5-7B LogiQA s456 | 200 | +2.0 | 1 | 5 | 6 | 0.500 | NO |

**结果: 4/15 条件在 ±2pp 通过等价性检验** (放宽至 ±3pp 时 8/15 通过)

### 三类分类

**等价 (4):** 低 discordant pairs + 小 |Δ|，统计功效足以证明等价

**真实差异 (5):** |Δ|>2pp，SICA 和 SC 确实不同
- exp033 (+4.9pp)、PW-600 Mistral (-2.8pp)、PW-600 Qwen7B (-4.0pp)、LogiQA Mistral (-3.0pp)、LogiQA Qwen7B def (+2.5pp)

**功效不足 (6):** |Δ|≤2pp 但 discordant pairs 太少（n=204 时 b+c 需 ≤6 才能证等价），无法下结论。这是统计功效问题，不是证据支持差异。

### 关键洞察
n=204 时最多允许 b+c≤6 个 discordant pairs 才能在 ±2pp margin 通过 TOST。大部分 FOLIO 条件的 b+c 刚好卡在边界（5-11），导致 underpowered。n=600 的 PW 数据有更好的功效（允许 b+c≤53）。

---
