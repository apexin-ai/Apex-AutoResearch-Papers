# analysis d140 4b fair tax

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d140_4b_fair_tax_20260521T113700_result.json`
- **Structured JSON:** [`4cc77ecbd70503f92f66.json`](../../sessions/4c/4cc77ecbd70503f92f66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/autodl-tmp/eval_results/d140_4b_matched_fair_tax_2048.json`。

**4B SFT s42 matched@2048 fair evidence tax：**

| | with-evi | no-evi |
|---|---|---|
| format_ok | 983 | 983 |
| truncated (总) | 243 | 178 |

- **fair subset docs**: 981（交集）
- **fair with-evi ign_f1**: 0.3951
- **fair no-evi ign_f1**: 0.4024
- **fair_tax**: **+0.73pp**（no-evi 更高，即 evidence 有负面影响）

对比其他 scale：1.7B fair_tax = -5.63pp（evidence 大幅帮助），8B 待查。4B 的 evidence tax 接近零且方向反转。

---
