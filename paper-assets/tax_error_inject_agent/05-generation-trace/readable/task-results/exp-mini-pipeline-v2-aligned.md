# exp mini pipeline v2 aligned

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mini-pipeline-v2-aligned_20260514T110830_result.json`
- **Structured JSON:** [`93c796c4c1de0ca74dc4.json`](../../sessions/93/93c796c4c1de0ca74dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 组训练全部正常运行。

## 汇总

| 组 | GPU | 训练 samples | Steps (3 epochs) | 预计耗时 | exp_id |
|---|---|---|---|---|---|
| **Vanilla** | cuda:0 | 4,176 | 1,566 | ~58 min | mini-vanilla-sft-v3 |
| **TaxEI** | cuda:1 | 7,545 (clean 4176 + injected 3369) | 2,832 | ~1h 30min | mini-taxei-sft-v3 |
| **Random** | cuda:2 | 9,076 (clean 4176 + injected 4900) | 3,405 | ~1h 50min | mini-random-sft-v3 |

训练配置：LoRA r=16/α=32, bs=1, grad_accum=8, max_len=4096, lr=1e-4, 3 epochs, bf16, gradient_checkpointing。

格式对齐：每个 sample 是单轮对话，prompt 完全匹配 eval 的 `build_prompt()`（task_desc + step_count + history + current_obs + admissible_actions + think/action 指令）。injected 数据缺少 `admissible_commands`（采集时未记录），prompt 中该字段为空列表。

---
