# harvest gsm8k alpha4 westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_gsm8k_alpha4_westd_20260522T052702_result.json`
- **Structured JSON:** [`0b2bb92deb489e26373d.json`](../../sessions/0b/0b2bb92deb489e26373d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== eval_gsm8k_grpo_alpha4_20_v3 ==
Status: DONE
Accuracy: 62.77% (828/1319) ± 1.33%
EOS rate: 98.56%, avg_len=188, truncated=19
Log: "GSM8K Accuracy: 0.6277 ± 0.0133 (828/1319)" → sentinel written

== eval_gsm8k_sft_alpha4_20_v5 ==
Status: STILL_RUNNING (PID 3586)
Progress: 93.6% (1235/1319)
Interim accuracy @1200: 62.25%, eos_rate=98.25%, avg_len=195
Estimated ~3-4 min remaining

== GPU Status ==
cuda:0: 占用 (17541/97887 MiB, 98%)
cuda:1: 占用 (15329/97887 MiB, 97%)
cuda:2: 占用 — SFT eval 运行中 (16507/97887 MiB, 90%)
cuda:3: 空闲 (0 MiB, 0%)
```

GRPO α=4.0 已完成收割：**62.77%**。SFT α=4.0 还剩 84 samples，几分钟内完成，interim accuracy 62.25% 和 GRPO 非常接近。

---
