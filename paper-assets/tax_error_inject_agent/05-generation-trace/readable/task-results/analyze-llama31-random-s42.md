# analyze llama31 random s42

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama31-random-s42_20260516T083752_result.json`
- **Structured JSON:** [`06eab77b7e814fb6500e.json`](../../sessions/06/06eab77b7e814fb6500e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新至 DONE。汇总：

## llama31-random-s42 训练结果

| 指标 | Random (本次) | Vanilla (baseline) |
|------|-------------|-------------------|
| train_loss | **0.3366** | 0.4003 |
| token_acc | **0.9364** | 0.9067 |
| train_steps | 3387 | 1635 |
| train_duration_s | 7622 | 4157 |
| epochs | 3.0 | ~1.45 |

- Checkpoint 完整：`adapter_model.safetensors` (168MB) + `adapter_config.json` ✓
- 无 W&B run（`report_to=tensorboard`）
- Checkpoint 路径：`/root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s42/v0-20260516-142300/checkpoint-3387/`

注意 random 训了 3 epochs（3387 steps），vanilla 只训了 ~1.45 epochs（1635 steps），训练 epochs 数不同，loss/acc 不能直接比较。需要 eval 阶段的下游任务指标才能判断 random injection 对 LLaMA-3.1 的实际效果。

---
