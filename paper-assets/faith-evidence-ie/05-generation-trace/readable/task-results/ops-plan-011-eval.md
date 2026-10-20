# ops plan 011 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_011_eval_20260515T144027_result.json`
- **Structured JSON:** [`5c382ef5c462b8229369.json`](../../sessions/5c/5c382ef5c462b8229369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常启动：PID 216361 在 GPU 0 上，已加载 8.2 GB（模型加载中）。GPU 0 有 32 GB，空间充足。

**状态汇总：**
- `plan_011_grpo_g8_bf16_eval` 已提交到 cuda:0（PID 216361）
- 模型加载中（Qwen3-4B base → merge SFT adapter → load GRPO ckpt-100 adapter）
- bf16 无量化，985 docs，预计 ~1.5h
- 输出目录：`/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json`
- 另有 `eval_grpo_g8_bf16` batch_eval 在 cuda:3 同时跑 ckpt 80/90/100，可交叉验证

---
