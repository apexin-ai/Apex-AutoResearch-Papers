# eval math500 grpo alpha3p0 submit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_math500_grpo_alpha3p0_submit_20260524T095815_result.json`
- **Structured JSON:** [`52df13d40ac364dfa1cb.json`](../../sessions/52/52df13d40ac364dfa1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**GRPO α=3.0 20% 的 checkpoint 不存在。** 两台服务器上都找不到 model.safetensors：

- `westd-32935:/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/` — 只有 TRL 自动生成的 README.md，训练被 kill 前模型未保存。旧的 `checkpoint-100` 也已被清理。
- `westb-23072` — 有 `pruned_rasp_alpha3p0_20` 和 `sft_rasp_alpha3p0_20`，但没有 GRPO stage 的产物。

**grpo_standard_20 fixed eval 结果**（文件名为 `eval_math500_grpo_standard_20_fair_fixed.json`）：
- accuracy = **27.0%** (135/500)

**要获得 α=3.0 的 MATH-500 数据点，需要先重新跑 GRPO 训练**（从 westb-23072 上的 `sft_rasp_alpha3p0_20` checkpoint 开始），然后再 eval。是否需要我提交 GRPO 训练任务？

---
