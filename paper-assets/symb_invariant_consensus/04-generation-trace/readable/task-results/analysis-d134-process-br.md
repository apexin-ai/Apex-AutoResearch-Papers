# analysis d134 process br

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d134-process-br_20260521T082251_result.json`
- **Structured JSON:** [`7ae9dd56ed34da2acc08.json`](../../sessions/7a/7ae9dd56ed34da2acc08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到服务器 (`results/exp_d134_process_br/results.json`) 和本地 artifacts，已注册。

**关键发现：**

| 维度 | 结果 | 预测是否成立 |
|------|------|-------------|
| **Position** (early/mid/late) | BR 均匀 ~5.2-5.4，Fisher p=0.71 | **否** — 偏差不集中在 late-step，而是均匀渗透整个推理链 |
| **Difficulty** (easy vs hard) | BR_easy=18.8 >> BR_hard=2.7，p≈0 | **反向** — 高 SC 一致性问题中 SICA-wrong 的偏差远更极端 |
| **Type** (conditional vs other) | conditional BR=5.69 vs other BR=4.91，p=0.06 | **边际** — conditional 约束略偏更高，但不显著 |

Position 的结果是最有意义的 negative finding：SCB 不是 answer-adjacent 的局部现象，而是从推理链开始就系统性地存在。Difficulty 方向逆转的解释：当 LLM 高度一致（SC≥10/12）时，如果这个一致意见恰好是错的，FOL 提取几乎完全被 LLM 的错误推理带偏（BR≈19）。

---
