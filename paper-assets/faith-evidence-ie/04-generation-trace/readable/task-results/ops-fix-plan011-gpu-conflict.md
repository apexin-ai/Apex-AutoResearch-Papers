# ops fix plan011 gpu conflict

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_plan011_gpu_conflict_20260515T195135_result.json`
- **Structured JSON:** [`570c7104cec240ddb359.json`](../../sessions/57/570c7104cec240ddb359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 步骤 | 状态 |
|------|------|
| Kill plan_011 eval (PID 246051) | 已 kill，plan_001 (236779) 安全 |
| nvidia-smi 确认 cuda:1 | 0 MiB / 32607 MiB，完全空闲 |
| 重新提交到 cuda:1 | PID 247234，循环 eval checkpoint-30/50/70 |
| 验证 cuda:1 | 20312 MiB 占用，正在运行 |
| Registry 更新 | status=RUNNING, gpu=cuda:1, spec.gpu=["cuda:1"] |

**注意**：checkpoint 实际路径是 `/root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-{30,50,70}`（非原始指令中的 `grpo_g8_bf16_output`），已修正。三个 checkpoint 的 eval 结果会分别存到 `/root/autodl-tmp/eval_results/bf16_g8_step{30,50,70}/`。

---
