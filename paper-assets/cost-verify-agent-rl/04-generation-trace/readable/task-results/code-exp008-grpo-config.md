# code exp008 grpo config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008_grpo_config_20260514T030338_result.json`
- **Structured JSON:** [`b61943c19ceb04cd64fa.json`](../../sessions/b6/b61943c19ceb04cd64fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT checkpoint 目录尚不存在（符合预期，SFT 正在进行中）。

---

## 产出报告

### 1. exp007 GRPO 配置
路径：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp007_fixed.yaml`
- 模型：`/root/cost-verify-agent-rl/models/Qwen3-1.7B`
- GRPO, 30 steps, 2 GPU, 64 traj/step (8 groups × 8), max_turn 30
- KL loss enabled (coef=0.01), collapse_detection off
- Checkpoint: `/root/autodl-tmp/checkpoints/exp_007/`

### 2. exp008 GRPO 配置
路径：**`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp008_sft_grpo.yaml`**

与 exp007 的差异：
| 字段 | exp007 | exp008 |
|------|--------|--------|
| `model_path` | `.../models/Qwen3-1.7B` | `/root/autodl-tmp/checkpoints/exp008_sft/checkpoint-final/` |
| `experiment_name` | `exp007-alfworld-speed-optimized` | `exp008-alfworld-sft-grpo` |
| `local_log_dir` / `default_local_dir` | `.../exp_007/` | `/root/autodl-tmp/checkpoints/exp008_grpo/` |

其余参数完全一致（64 traj/step, 30 max_turns, 30 steps, collapse_detection off）。

### 3. Checkpoint 兼容性结论
**直接兼容，无需转换脚本。** verl/RAGEN 底层通过 `AutoModelForCausalLM.from_pretrained(path)` 和 `AutoConfig.from_pretrained(path)` 加载模型。TRL SFTTrainer 输出的标准 HuggingFace 格式（`config.json` + `model.safetensors` + `tokenizer*`）可直接使用。

⚠️ SFT 完成后需确认实际 checkpoint 子目录名：
- 若 SFTTrainer 用 `save_strategy="steps"` → 子目录形如 `checkpoint-{step}`
- 若调用了 `trainer.save_model()` → 直接保存在根目录
- 确认后更新 `model_path` 中的 `checkpoint-final/` 为实际路径

### 4. 监控指标 Key Name

| 指标 | Key Name | 预警阈值 | 代码位置 |
|------|----------|----------|----------|
| KL divergence | **`actor/ppo_kl`** | > 0.1 | `verl/trainer/ppo/core_algos.py:973` |
| Entropy | **`actor/entropy`** | < 0.01 | `ragen/trainer/agent_trainer.py:1316` |

补充指标（如有需要）：
- `actor/entropy_loss` — entropy loss 项（`ragen/workers/actor/dp_actor.py:477`）
- `actor/reward_kl_penalty` — reward 中的 KL penalty（`verl/trainer/ppo/ray_trainer.py:158`）

### 5. 转换脚本
不需要。TRL SFT 输出与 RAGEN/verl 完全兼容。

---
