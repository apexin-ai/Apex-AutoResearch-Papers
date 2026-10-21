# ops westb harvest and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_harvest_and_launch_20260518T194813_result.json`
- **Structured JSON:** [`47834ea200a50a0306f8.json`](../../sessions/47/47834ea200a50a0306f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在运行中。

**汇报：**

| GPU | 状态 | 实验 | 详情 |
|-----|------|------|------|
| **cuda:0** | 忙碌 (96%, 6537MiB) | eval_gsm8k_grpo_standard_20_1p5b | 仍在运行（已跑 ~3h10m），结果文件尚未生成 |
| **cuda:1** | 刚启动 | eval_gsm8k_grpo_rasp_20_1p5b | PID 832359，模型加载中 |

**收割结果：**
- **eval_gsm8k_grpo_cka_only_20_1p5b** → DONE (success)
  - accuracy = **35.48%** (468/1319), stderr = 0.0132

**新启动实验：**
- **eval_gsm8k_grpo_rasp_20_1p5b** on cuda:1 → RUNNING
  - checkpoint: grpo_rasp_20_1p5b/checkpoint-100

**未启动：**
- eval_gsm8k_sft_cka_only_20_1p5b — cuda:0 被 Standard eval 占用，等 Standard 完成后启动。

---
