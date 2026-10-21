# ssh check alpha3p0 math500 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_alpha3p0_math500_result_20260523T074742_result.json`
- **Structured JSON:** [`e0645112b06195fb0615.json`](../../sessions/e0/e0645112b06195fb0615.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 不存在（已被删除或未创建）。

**结果汇报：**

| 指标 | 值 |
|------|-----|
| MATH-500 accuracy | **22.8%** (114/500) |
| stderr | ±1.88% |
| truncated | 140/500 (28%) |
| avg response length | 745 tokens |

**GPU 状态 (westd-32935)：**
- GPU 0: **空闲** (0% util, 0 MiB)
- GPU 1-3: 占用中（其他实验）

对比参考：SFT α=3.0 MATH-500 = 23.2%，GRPO α=3.0 = 22.8%，基本持平，GRPO 在 MATH-500 上未带来提升（与 GSM8K 上 GRPO 63.45% vs SFT 的提升形成对比）。

---
