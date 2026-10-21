# analysis compute n err table2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compute-n-err-table2_20260522T134409_result.json`
- **Structured JSON:** [`e52df972077a8aba9611.json`](../../sessions/e5/e52df972077a8aba9611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have enough data. Let me compute the table. The paper_framing V16 table has the SC values, but I need to verify GPT-4o's n and LLaMA-8B's SC.

Key findings from data gathering:
- **LLaMA-8B**: SC=66.18% from exp-063 (n=204), shown as "—" in the V16 table
- **GPT-4o**: SC=73.91%, likely n=161 (73.91% × 161 ≈ 119, an integer; 73.91% × 204 = 150.78, not integer)
- **Gemini**: SC=87.37%, n=95 interim (87.37% × 95 ≈ 83, an integer)
- All other models: n=204

Here's the computed table:

```
| Model              | Extraction    | SC (%) | n   | n_err | n_err notes                    |
|--------------------|---------------|--------|-----|-------|--------------------------------|
| Mistral-7B         | self          | 55.88  | 204 |  90   | 114 correct                    |
| LLaMA-8B           | self          | 66.18  | 204 |  69   | exp-063; "—" in V16 table      |
| Qwen2.5-14B        | self          | 75.49  | 204 |  50   | 154 correct                    |
| R1-Distill-8B      | cross→Mistral | 74.51  | 204 |  52   | 152 correct                    |
| GPT-4o             | self          | 73.91  | 161 |  42   | ⚠️ only 161/204 completed      |
| GPT-4.1            | cross→Mistral | 82.84  | 204 |  35   | 169 correct                    |
| GPT-5.5            | cross→Mistral | 84.31  | 204 |  32   | 172 correct                    |
| o3                 | cross→Mistral | 82.65  | 204 |  35†  | 168.6→169 correct (rounding)   |
| Gemini-2.5-Pro     | cross→Mistral | 87.37  | 95  |  12   | ⚠️ only 95/204 interim         |
```

†o3: 82.65% × 204 = 168.6, 不是整数。可能 SC 是 168/204=82.35% 或 169/204=82.84%。82.65% 这个值需要验证来源——可能是小数精度问题或基于子集 n 计算。

**需要澄清的问题**：

1. **GPT-4o n=161**: 如果按 n=204 统一报告，n_err = 204 × (1 - 73.91/100) = 53（但 SC 基于 161 题计算，按 204 题算 SC 实际是 119/204=58.33%，n_err=85）。需要确认论文用哪个 n。

2. **Gemini n=95 interim**: 同理，按 n=204 统一的话 n_err = 204 × 0.1263 = 26，但 SC 基于 95 题。实验未完成，数据可能不宜写入正式表格。

3. **LLaMA-8B**: 在 V16 SCB 表中 SC/SICA/Δ 标为 "—"，仅有 BR=2.88。exp-063 有 SC=66.18%，但可能因代码版本不一致（westd-16639-legacy）未被纳入 V16 table。

---
