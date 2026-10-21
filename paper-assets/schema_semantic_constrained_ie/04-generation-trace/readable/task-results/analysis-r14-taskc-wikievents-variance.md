# analysis r14 taskC wikievents variance

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_taskC_wikievents_variance_20260520T201658_result.json`
- **Structured JSON:** [`f7dc73d5adb1e9320cf2.json`](../../sessions/f7/f7dc73d5adb1e9320cf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `westd-16980:/root/autodl-tmp/schema_outputs/r14_wikievents_perdoc_variance.json`。

**关键发现：**

| Model | Mode | Metric | Micro-avg | Per-doc Mean±Std | 95% CI | #Zero docs |
|-------|------|--------|-----------|-----------------|--------|------------|
| **Qwen FT** | uncon | Trig-F1 | 0.3208 | 0.267±0.145 | [0.253, 0.372] | 3/17 |
| | uncon | Arg-F1 | 0.0785 | 0.075±0.084 | [0.049, 0.113] | 7/17 |
| | uncon | RoV | 0.3831 | 0.216±0.224 | [0.254, 0.467] | 8/17 |
| | con | Trig-F1 | 0.2672 | 0.235±0.140 | [0.208, 0.329] | 4/19 |
| | con | Arg-F1 | 0.0818 | 0.073±0.078 | [0.055, 0.111] | 6/19 |
| **Llama FT** | uncon | Trig-F1 | 0.2752 | 0.276±0.161 | [0.230, 0.323] | 2/20 |
| | uncon | Arg-F1 | 0.0998 | 0.079±0.091 | [0.066, 0.125] | 8/20 |
| | uncon | RoV | 0.1107 | 0.060±0.130 | [0.038, 0.182] | 13/20 |
| | con | Trig-F1 | 0.2691 | 0.253±0.175 | [0.206, 0.326] | 4/20 |
| | con | Arg-F1 | 0.0891 | 0.098±0.105 | [0.058, 0.122] | 6/20 |

**统计功效问题确认：**
- Per-doc std 普遍 ≥ mean 的 50%（如 Llama uncon Trig-F1 std=0.161 vs mean=0.276），variance 极大
- Argument F1 有 ~35-47% 的文档为零，被少数高分文档拉高
- 20-doc 测试集下 95% CI 宽度通常 ≥ 0.06-0.12，微小差异无法区分
- RoV 的 per-doc mean (0.216) 远低于 micro-avg (0.383)——少数高 violation 文档的 argument 数量多，拉高了 micro 指标

---
