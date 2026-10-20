# analyze llama31 taxei s42

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_llama31-taxei-s42_20260516T083746_result.json`
- **Structured JSON:** [`89e3464c9886e69567dc.json`](../../sessions/89/89e3464c9886e69567dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `llama31-taxei-s42` 分析完成，已推进至 DONE。

## 结果汇总

| 指标 | llama31-taxei-s42 | llama31-vanilla-s42 (baseline) | 差异 |
|------|-------------------|-------------------------------|------|
| train_loss | **0.3366** | 0.4003 | -15.9% |
| token_acc | **0.9357** | 0.9067 | +2.9pp |
| train_steps | 3387 | 1635 | 2x (数据量更大) |
| train_duration_s | 7782 (~2h10m) | 4157 (~1h9m) | 与步数成比例 |

**结论**: 训练成功完成，checkpoint 完整（adapter_model.safetensors + adapter_config.json）。TaxEI 条件下 LLaMA-3.1-8B 的 loss 比 vanilla 低 16%，token_acc 高 ~3pp，与 Qwen3-8B 上的趋势一致，支持跨模型泛化假设。

**注意**: 该实验未配置 W&B（report_to=tensorboard），无 wandb_run_id。

---
