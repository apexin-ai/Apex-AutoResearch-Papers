# analysis multi seed llama table

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi-seed-llama-table_20260523T213746_result.json`
- **Structured JSON:** [`01c960a9fbfbf345a16b.json`](../../sessions/01/01c960a9fbfbf345a16b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/multi_seed_llama_table.tex`。

汇总：

| Seed | SC (%) | SICA (%) | Δ (pp) | p-value | Sig |
|------|--------|----------|--------|---------|-----|
| 42 | 72.50 | 65.00 | −7.50 | <.001 | *** |
| 123 | 71.33 | 64.17 | −7.17 | <.001 | *** |
| 456 | 71.67 | 66.17 | −5.50 | <.001 | *** |
| 789 | 71.17 | 66.50 | −4.67 | <.001 | *** |
| **Mean±Std** | **71.67±0.59** | **65.46±1.07** | **−6.21±1.35** | | |

**数据来源说明：**
- seed456 完整数据(n=600)在 **westd-30973** 的 `llama8b_pw_seed456_v2/results.json`，westd-16639 上只有 184/600 的旧版本
- seed789 SICA 从 66.17% 修正为 **66.50%**（2 个 tie 问题用 alphabetical tiebreaking 均修正为正确答案）
- 4 个 seed 的 McNemar exact p-value 全部 < .001，均达到 *** 显著性

---
