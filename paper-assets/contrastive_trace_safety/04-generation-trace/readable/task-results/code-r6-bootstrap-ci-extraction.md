# code r6 bootstrap ci extraction

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r6_bootstrap_ci_extraction_20260518T024936_result.json`
- **Structured JSON:** [`92d591611ba55cf259a3.json`](../../sessions/92/92d591611ba55cf259a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已有 percentile-based 95% CI。提取 precision metric 结果：

| Model | Precision Δ (HS − Text) | 95% CI lower | 95% CI upper | p-value |
|---------|------------------------|-------------|-------------|---------|
| R1-8B | +0.2786 | +0.1854 | +0.3781 | <0.0001 |
| OT-7B | +0.2189 | +0.1441 | +0.2961 | <0.0001 |
| QwQ-32B | +0.2349 | +0.1287 | +0.3510 | <0.0001 |
| R1-32B | +0.1544 | +0.0867 | +0.2262 | <0.0001 |

**R1-32B 分析**: delta 最小 (+0.154)，但 CI 下界 +0.087，远离 0，统计显著性没有问题。CI 宽度 0.140，与其他模型相当。

补充信息：
- 所有 12 项 Holm-Bonferroni 校正测试通过 (12/12 pass)
- p 值均为 0.0（10000 次 resampling 中零次出现反向结果）
- QwQ-32B 的 CI 最宽（0.222），R1-32B 次之（0.140），OT-7B 最窄（0.152）

---
