# ops v3 kill and diversity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v3_kill_and_diversity_20260515T220317_result.json`
- **Structured JSON:** [`b4bde3b515097ef2ed95.json`](../../sessions/b4/b4bde3b515097ef2ed95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. v3 处理结果
**已 kill**（PID 129992）。进程运行 6h11m，卡在 22/30，无进展。

### 2. 每题 unique candidates 数量

| 问题 | SC unique | SICA candidates | sica | sc | gold | 正确 |
|------|-----------|-----------------|------|----|------|------|
| II_01 | 1 | 1 | 73 | 73 | 73 | OK |
| II_02 | 0 | 0 | (空) | (空) | 236 | WRONG |
| II_03 | 1 | 1 | 45 | 45 | 45 | OK |
| II_04 | 1 | 1 | 33 | 33 | 33 | OK |
| II_05 | 1 | 1 | 80 | 80 | 80 | OK |
| II_06 | 1 | 1 | 55 | 55 | 55 | OK |
| II_07 | 1 | 1 | 699 | 699 | 699 | OK |
| II_08 | 0 | 0 | (空) | (空) | 127 | WRONG |
| II_09 | 0 | 0 | (空) | (空) | 902 | WRONG |
| II_10 | 1 | 1 | 468 | 468 | 468 | OK |
| II_11 | 0 | 0 | (空) | (空) | 601 | WRONG |
| II_12 | 1 | 1 | 23 | 23 | 23 | OK |
| II_13 | 1 | 1 | 321 | 321 | 321 | OK |
| II_14 | 0 | 0 | (空) | (空) | 211 | WRONG |
| II_15 | 0 | 0 | (空) | (空) | 315 | WRONG |
| I_01 | 1 | 1 | 204 | 204 | 204 | OK |
| I_02 | 1 | 1 | 25 | 25 | 25 | OK |
| I_03 | 1 | 1 | 809 | 809 | 809 | OK |
| I_04 | 1 | 1 | 116 | 116 | 116 | OK |
| I_05 | 1 | 1 | 104 | 104 | 104 | OK |
| I_06 | 1 | 1 | 294 | 294 | 294 | OK |
| I_07 | 1 | 1 | 540 | 540 | 540 | OK |

### 3. Divergent 题目
**0/22** — 没有任何题目存在多个候选答案。所有成功提取答案的题目都是 unanimous vote。

### 4. SICA vs SC 不一致
**0 个** — SICA 和 SC 在所有 22 题上完全一致。

### 5. 总结

| 指标 | 值 |
|------|-----|
| 完成题数 | 22/30 (8题卡住未完成) |
| SICA 准确率 | 16/22 (72.7%) |
| SC 准确率 | 16/22 (72.7%) |
| Vote diversity 比率 | **0%** — 无任何 divergence |
| SICA/SC 分歧 | 0 |
| 约束提取总数 | 902, 去重后 315 |
| MaxSAT 排除数 | 122 |
| 平均耗时 | 630s/题 |

关键发现：在这组数据上 vote diversity 为零。6 个错题全是 extraction 完全失败（0 constraints, 0 votes），不是因为候选答案冲突导致选错，而是模型根本没能产出有效 trace。SICA 相对 SC 没有提供任何额外价值——二者答案完全相同。

---
