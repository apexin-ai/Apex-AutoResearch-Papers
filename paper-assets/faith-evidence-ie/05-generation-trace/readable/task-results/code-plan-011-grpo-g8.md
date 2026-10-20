# code plan 011 grpo g8

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_011_grpo_g8_20260515T135227_result.json`
- **Structured JSON:** [`e48174d5d0ea37101244.json`](../../sessions/e4/e48174d5d0ea37101244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `plan_011_grpo_g8_bf16` 已提交并正在运行。

**总结：**
- 服务器：rtx5090-4x, GPU cuda:3 (32GB RTX 5090)
- 修复了 TRL 的 `generation_batch_size` 约束（设为 `num_generations`）
- Dry-run 验证通过：~32s/step，GPU 峰值 25.9GB/32GB，无 OOM
- 训练已通过 tmux 提交，100 steps 预估 ~53 分钟
- 输出目录：`/root/autodl-tmp/grpo_ced_g8_bf16`
- 日志：`/root/runs/faith-evidence-ie/plan_011_grpo_g8_bf16.log`
- Registry exp_id: `plan_011_grpo_g8_bf16`, plan_id: `plan_011`

---
