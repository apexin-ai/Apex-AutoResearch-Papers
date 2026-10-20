# eval plan 011 grpo g8 bf16 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_011_grpo_g8_bf16_eval_20260515T143923_result.json`
- **Structured JSON:** [`1d6cc63df146edee2e54.json`](../../sessions/1d/1d6cc63df146edee2e54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已在运行，registry 已更新。

**状态总结：**
- **Job**: `eval_grpo_g8_bf16` on cuda:3, tmux session `eval_grpo_g8_bf16`
- **评估内容**: GRPO G=8 bf16 checkpoint-80, 90, 100（bf16 LoRA, `--no-quantize`）
- **数据**: DocRED dev 985 docs, max_new_tokens=1024
- **注意**: checkpoint-85 不存在（训练每 10 步保存），best_reward_step=85 的前后两个 checkpoint 是 80 和 90
- **预计耗时**: 每 checkpoint ~1.5-2h，总计 ~5h
- **日志**: `~/runs/faith-evidence-ie/eval_grpo_g8_bf16.log`

checkpoint-80 inference 已开始（62 batches）。完成后检查 metrics 并报告。

---
