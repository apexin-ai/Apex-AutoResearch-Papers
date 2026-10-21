# analysis br shuffle control

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_br-shuffle-control_20260522T012840_result.json`
- **Structured JSON:** [`0c2f07f8e41f8ea427be.json`](../../sessions/0c/0c2f07f8e41f8ea427be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇报如下：

---

## BR Shuffle Control 分析结果

### 数据结构
`per_trace_constraints/folio_X.json` 每题包含 ~12 traces，每 trace 有 `answer` + `constraints`（逻辑规则列表，含 `expression`, `z3_formula`, `source_step`）。约束无独立 "supported_answer" 字段，归属由来源 trace 的 answer 决定。

### 结果汇总

| 指标 | Qwen3 (n=62) | GPT-4o (n=80) | Mistral-7B (n=189) |
|------|-------------|---------------|-------------------|
| **Original BR mean** | 5.70 | 6.32 | 3.16 |
| **Trace count ratio** | 5.30 | 5.85 | 2.89 |
| **Shuffle BR mean** | 6.16 ± 0.59 | 6.89 ± 0.61 | 3.31 ± 0.24 |
| **p-value** | 0.783 | 0.822 | 0.706 |
| **Cohen's d** | −0.78 | −0.93 | −0.62 |
| **Aligned c/trace** | 6.57 | 6.23 | 5.62 |
| **Unaligned c/trace** | 7.48 | 6.52 | 6.00 |

### 结论

**BR 不是约束提取设计的产物，而是多数投票的结构性副产品。**

1. **p-value 全部 > 0.7**：原始 BR 甚至 *低于* 随机 shuffle 的期望值（Cohen's d 均为负）。约束提取没有向 SICA 答案倾斜。
2. **BR ≈ trace count ratio**：BR 主要由 aligned vs unaligned trace 的数量比决定。SICA 选共识答案 → 多数 trace 天然 aligned → BR > 1 是同义反复。
3. **Unaligned traces 产出更多约束**：三个模型一致显示 unaligned traces 的 constraints/trace 高于 aligned（7.48 vs 6.57, 6.52 vs 6.23, 6.00 vs 5.62），说明约束提取对少数派 trace 不存在压制。

---
