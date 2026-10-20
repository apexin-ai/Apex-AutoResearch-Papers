# research dose response hyperparams

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dose_response_hyperparams_20260523T184941_result.json`
- **Structured JSON:** [`398f73d53ec0b4d43dc1.json`](../../sessions/39/398f73d53ec0b4d43dc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dose-response GRPO 超参审计

| α值 | exp_id | max_completion_length | temperature | rep_penalty | format_reward | optimizer | 备注 |
|-----|--------|----------------------|-------------|-------------|---------------|-----------|------|
| 0.5 | `pipeline_alpha0p5_20` (内嵌) | 512 (默认) | 0.4 (默认) | 1.15 (默认) | 0.1 (默认) | adamw_8bit (默认) | pipeline 无独立 GRPO 记录，参数推断自脚本默认值 |
| 1.0 | `grpo_rasp_20_fair` | **1024** | 0.4 | 1.15 | 0.1 | adamw_bnb_8bit | registry hyperparams 明确记录 max_completion_length=1024 |
| 2.0 | `pipeline_alpha2p0_20` (内嵌) | 512 (默认) | 0.4 (默认) | 1.15 (默认) | 0.1 (默认) | adamw_8bit (默认) | 同 α=0.5，参数推断 |
| 3.0 | `grpo_rasp_alpha3p0_20_v2` | 512 (默认) | 0.4 (默认) | 1.15 (默认) | 0.1 (默认) | adamw_8bit (默认) | v1 checkpoint 磁盘满损坏，v2 仅指定 --max_steps 100 --save_total_limit 1 |
| 4.0 | `grpo_alpha4_20` | 512 (默认) | 0.4 (默认) | 1.15 (默认) | 0.1 (默认) | adamw_8bit (默认) | 命令仅指定 --alpha 4.0 --max_steps 100 |

### `train_grpo_v5.py` 默认值确认

从 `src/train_grpo_v5.py` line 199-217 的 argparse 定义：
- `--max_completion_length`: 512
- `--temperature`: 0.4
- `--repetition_penalty`: 1.15
- `--format_reward_weight`: 0.1
- `--optim`: adamw_8bit

### 内部一致性: **No**

**关键问题：α=1.0 的 max_completion_length=1024，其余四个为 512。**

α=1.0 (`grpo_rasp_20_fair`) 的 registry hyperparams 字段明确记录了 `"max_completion_length": 1024`，同时 optimizer 名也略有不同（`adamw_bnb_8bit` vs `adamw_8bit`，实际是同一个 optimizer 的不同写法）。

其余四个 α 值均未在命令中显式指定 `--max_completion_length`，使用脚本默认值 512。α=0.5 和 α=2.0 的参数是推断值（pipeline 内嵌运行，registry 无独立 GRPO 命令记录），置信度略低但大概率也是默认 512。

### 影响

max_completion_length 1024 vs 512 意味着 α=1.0 的 GRPO 训练允许生成更长的推理链，这可能系统性地影响 reward signal 和最终性能。如果用于论文 dose-response 曲线，需要用统一的 max_completion_length 重跑 α=1.0，或者将其余四个对齐到 1024。

---
