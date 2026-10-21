# code alpha4 eval collect

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha4-eval-collect_20260515T134704_result.json`
- **Structured JSON:** [`ad445d1604677e92a5f6.json`](../../sessions/ad/ad445d1604677e92a5f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**sft_alpha4_0_westd_retry — DONE (success)**

| 阶段 | 指标 | 值 |
|------|------|-----|
| 训练 | final loss | 0.7393 |
| 训练 | steps / epochs | 1870 / 2 |
| 训练 | runtime | ~30 min |
| Eval | GSM8K accuracy (N=100) | **62% ± 4.9%** |
| Eval | eos_rate | 98% |
| Eval | avg_response_length | 238.56 |
| 恢复 | post-prune → post-SFT | 40% → 62% (+22pp) |

---
