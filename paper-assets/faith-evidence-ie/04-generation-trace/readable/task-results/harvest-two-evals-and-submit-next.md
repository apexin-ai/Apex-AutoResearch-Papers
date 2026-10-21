# harvest two evals and submit next

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_two_evals_and_submit_next_20260518T200453_result.json`
- **Structured JSON:** [`a1f174a3ec9dbd6fdd24.json`](../../sessions/a1/a1f174a3ec9dbd6fdd24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 卡全在工作。

```
=== random_rsft_k1_eval 结果 ===
状态: 完成 (success)
ign_f1: 0.4114
f1: 0.4198
evi_f1: 0.7964
EDCR: 0.6971
truncated: 235/985
format_compliance: 99.9%
field_compliance: 74.8%
关键对比: CED RSFT k=1 mean ign_f1=0.4596, Random 差距: -4.82pp → CED 选择显著优于随机

=== grpo_bf16_g4_ckpt100_eval 结果 ===
状态: 完成 (success)
ign_f1: 0.4431 (vs SFT baseline 0.4057 → +3.74pp)
f1: 0.4511
evi_f1: 0.8010
EDCR: 0.6453
truncated: 182/985
format_compliance: 99.9%
field_compliance: 81.4%
D106 判断: 继续 — ign_f1 0.4431 > SFT baseline 0.4057，无 catastrophic forgetting

=== GPU 填充 ===
cuda:0: 训练中 (32045 MiB)
cuda:1: wave1_sft_4b_s44_eval_r2 (PID 571192, 8181 MiB 加载中)
cuda:2: 训练中 (31328 MiB)
cuda:3: grpo_bf16_g4_ckpt200_eval (PID 571115, 8181 MiB 加载中)
```

---
