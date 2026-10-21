# code bocpd cusum r1 32b qwq

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bocpd_cusum_r1_32b_qwq_20260517T135527_result.json`
- **Structured JSON:** [`40f337a2c366a802d1e7.json`](../../sessions/40/40f337a2c366a802d1e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 模型对比结果：

| Model | Layer | W | BOCPD Det | Lead | CUSUM Det | Lead | FCP Det | Lead |
|-------|-------|---|-----------|------|-----------|------|---------|------|
| R1-8B | L14 | 15 | **93.0%** | 3.45 | 74.4% | 7.46 | 65.1% | 4.89 |
| R1-32B | L10 | 10 | 0.0% | N/A | 85.0% | 2.59 | **95.0%** | 5.68 |
| OT-7B | L16 | 3 | 0.0% | N/A | 74.5% | 7.46 | **89.4%** | 11.83 |
| QwQ-32B | L2 | 5 | 0.0% | N/A | 73.7% | 9.86 | **78.9%** | 9.40 |

**结论：BOCPD 在 3/4 模型上检测率为 0%（仅 R1-8B 例外），CUSUM 检测率均低于 FCP。简单阈值方法 (FCP) 在所有 4 个模型上表现最优或并列最优。高级变点检测方法不优于简单阈值，验证了负面结果的普适性。**

结果 JSON 已保存至：
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_bocpd_r1_32b/results.json`
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_bocpd_qwq/results.json`

---
