# analysis eval gsm8k grpo standard 20 extended 300

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_gsm8k_grpo_standard_20_extended_300_20260519T055703_result.json`
- **Structured JSON:** [`500917fbe41d8f76cb35.json`](../../sessions/50/500917fbe41d8f76cb35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(negative)，cron 已删除。

**结果汇总：**

| 指标 | 值 |
|---|---|
| Accuracy | **59.29%** (782/1319) |
| Stderr | ±1.35% |
| EOS Rate | 97.95% |
| Avg Response Length | 229.6 tokens |

**Conclusion: negative** — Hypothesis 被证伪。Standard 20% extended 300步的 GSM8K accuracy 为 59.29%，显著高于 Standard 100步的 ~52-53%，说明额外训练步数确实带来了 downstream gain。这挑战了 E2 "reward collapse = no downstream improvement" 的叙事。

59.29% 处于 55-60% 边界区间（±1.35% stderr），但方向性结论明确：extended training 对 Standard pruning 也有效，尽管存在 reward collapse。这意味着 reward collapse 并不完全阻止 downstream 能力恢复，E2 的 framing 需要调整。

---
