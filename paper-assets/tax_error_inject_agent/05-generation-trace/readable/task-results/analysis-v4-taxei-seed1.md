# analysis v4 taxei seed1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-seed1_20260515T153218_result.json`
- **Structured JSON:** [`8bd0b759e061dd75404b.json`](../../sessions/8b/8bd0b759e061dd75404b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## v4-taxei-seed1 训练结果报告

| 指标 | seed1 | seed123 (参考) |
|------|-------|---------------|
| final_loss | **0.3561** | 0.355 |
| token_accuracy | **0.915** | 0.900 |
| train_steps | 3387/3387 | 3387 |
| train_epochs | 3 | 3 |
| duration | 108.9 min | 109.2 min |
| speed | 1.929 s/it | — |
| memory | 18.49 GiB | — |
| EXIT_CODE | 0 | — |

**Checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387`
- adapter_model.safetensors: 174MB

**W&B**: 未启用（日志和目录中均无 wandb 记录）

**Registry**: DONE / success

seed1 与 seed123 结果高度一致：loss 相差 0.001，token_accuracy seed1 略高（0.915 vs 0.900），训练时长几乎相同。训练正常完成。

---
