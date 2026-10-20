# diagnose pass k8 standard v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pass_k8_standard_v2_20260516T232218_result.json`
- **Structured JSON:** [`38fd7434df67395255c9.json`](../../sessions/38/38fd7434df67395255c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，registry 已更新为 success（cron 已不存在，无需删除）。

**结果汇总：**

| Metric | Value |
|--------|-------|
| pass@8 | **0.91** ± 0.0202 |
| n_problems | 200 |
| k | 8 |
| temperature | 0.7 |
| eos_rate | 0.9994 (1599/1600 natural EOS) |
| truncated | 1 |
| avg_response_length | 130.0 tokens |
| 运行时间 | ~68 min |

Standard 20% 剪枝模型 post-GRPO 的 pass@8 = 0.91，EOS rate 接近 1.0，几乎无 truncation。

---
