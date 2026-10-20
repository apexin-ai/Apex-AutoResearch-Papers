# code length confound control

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_length-confound-control_20260516T200207_result.json`
- **Structured JSON:** [`d46a5c4c8ba6934be04b.json`](../../sessions/d4/d46a5c4c8ba6934be04b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `/root/gen-depth-fingerprint/results/8gen_length_confound.json`。

**结论：`length_partial_confound`**

| 指标 | 值 |
|------|-----|
| 原始 binary F1 | 0.7697 |
| Length-matched binary F1 | 0.7242 |
| F1 drop | 0.0455 (6% relative) |
| Random-subsample control F1 | 0.767 (sample-size effect仅0.001) |
| KS test (matched lengths) | p=0.82 (分布已对齐) |

**关键发现**：
- Text length 在 depth classes 间有统计差异（KW p=0.002），但 median 几乎相同（179-180 words）
- 最受 length 影响的 features：tail_decay (ρ=-0.38), hapax_ratio (ρ=-0.30), ttr (ρ=-0.29)
- Length deconfounding 后 F1 下降 0.046，random-subsample control 确认这不是样本量减少的效应
- 但 matched F1 仍达 0.724，depth fingerprint 信号在去除 length 后仍然显著存在

---
