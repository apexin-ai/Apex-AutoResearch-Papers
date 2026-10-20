# analysis cf batch part2 v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cf_batch_part2_v1_20260522T000604_result.json`
- **Structured JSON:** [`3ee13e70efda50e9c9ce.json`](../../sessions/3e/3ee13e70efda50e9c9ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验 `cf_batch_part2_v1` 分析结果：

**状态**: 成功完成 (EXIT_CODE=0)，两个 suite 各 4 个 condition 全部跑完。

**核心数据**:

| Suite | Condition | cos_dist (L31) | 
|-------|-----------|---------------|
| **Goal untrained** | empty | 0.1530 |
| | shuffled | 0.0839 |
| | wrong | 0.0160 |
| | paraphrased | 0.0043 |
| **Long untrained** | empty | 0.1734 |
| | shuffled | 0.1204 |
| | wrong | 0.0221 |
| | paraphrased | 0.0070 |

**Untrained ordering**: `empty >> shuffled > wrong > para` (两个 suite 一致)

**与 trained 对比** (⚠️ 方法不同: trained 用 paired_mse, untrained 用 cosine_dist, 仅 ordering 可比):
- Trained: `empty > wrong > shuffled > para`
- Untrained: `empty >> shuffled > wrong > para`
- 差异: wrong 和 shuffled 在 untrained 中互换了位置；untrained 的 empty 占绝对主导地位 (cos_dist 比第二名大 2-10 倍)

已更新 registry (status=DONE, conclusion=success) 并注册分析报告 artifact。

---
