# analysis tost exact recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-exact-recompute_20260521T074058_result.json`
- **Structured JSON:** [`d09c46d5e209f21e3c15.json`](../../sessions/d0/d09c46d5e209f21e3c15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**精确 TOST ±2pp（SE = √(b+c)/n）：4 / 2 / 10**

| # | Model | Dataset | b | c | Δpp | SE | TOST p | 分类 |
|---|-------|---------|---|---|-----|-----|--------|------|
| 1 | Mistral-7B | PW-D5 | 13 | 30 | -2.83 | 1.09 | 0.777 | **different** |
| 2 | Mistral-7B | LogiQA | 6 | 5 | +0.50 | 1.66 | 0.183 | underpowered |
| 3 | Mistral-7B | FOLIO s123 | 7 | 1 | +2.94 | 1.39 | 0.751 | underpowered |
| 4 | Mistral-7B (4s) | FOLIO | 10 | 3 | +3.43 | 1.77 | 0.791 | underpowered |
| 5 | Mistral-7B | FOLIO s456 | 3 | 3 | 0.00 | 1.20 | 0.048 | **equivalent** |
| 6 | Mistral-7B | FOLIO s789 | 5 | 6 | -0.49 | 1.63 | 0.177 | underpowered |
| 7 | LLaMA-3.1-8B | FOLIO | 7 | 16 | -4.41 | 2.35 | 0.848 | underpowered |
| 8 | LLaMA-3.1-8B | StrategyQA | 9 | 5 | +2.00 | 1.87 | 0.500 | underpowered |
| 9 | Qwen2.5-14B | FOLIO ICL | 6 | 5 | +0.50 | 1.67 | 0.184 | underpowered |
| 10 | Qwen2.5-14B | PW-D5 | 8 | 23 | -2.50 | 0.93 | 0.705 | **different** |
| 11 | Qwen2.5-14B | FOLIO | 1 | 3 | -0.98 | 0.98 | 0.149 | underpowered |
| 12 | Qwen2.5-7B | FOLIO | 4 | 3 | +0.49 | 1.30 | 0.122 | underpowered |
| 13 | Qwen2.5-14B | LogiQA | 1 | 2 | -0.50 | 0.87 | 0.042 | **equivalent** |
| 14 | Qwen3-14B | FOLIO | 3 | 4 | -0.49 | 1.30 | 0.122 | underpowered |
| 15 | Qwen3-14B | PW-D5 | 12 | 8 | +0.67 | 0.75 | 0.037 | **equivalent** |
| 16 | Qwen3-14B (think) | FOLIO | 2 | 1 | +0.49 | 0.85 | 0.038 | **equivalent** |

注意事项：
- **条件 8** (StrategyQA) 的 b,c 通过 delta_pp=+2.0 和 raw_p=0.424 反推（binomtest(5,14,0.5)=0.424 精确匹配），服务器上未找到独立实验目录
- **条件 10** (Qwen14B PW) 的 b,c 来自 mcnemar_recomputed（exp-039 tiebreak），SC%=74.0 与 Table 1 的 75.17 有差异但 delta 和 raw_p 完全匹配
- **条件 15** 实际 McNemar raw_p=0.503（非 Table 1 中的 1.000），但不影响 TOST 分类

---
