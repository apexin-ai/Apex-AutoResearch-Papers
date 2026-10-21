# code grpo qwen math prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_qwen_math_prep_20260516T113804_result.json`
- **Structured JSON:** [`bd120e3a968464c28f4e.json`](../../sessions/bd/bd120e3a968464c28f4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇报如下：

---

## 兼容性分析结果

### 1. EOS 问题：**需要修复**

两个 SFT 模型的 `generation_config.json` 都只有：
```json
"eos_token_id": [151643]
```
缺少 `151645` (`<|im_end|>`)。

`config.json` 中 `eos_token_id` 也只是 `151643`（标量）。

**GRPO 脚本（`train_grpo.py` 和 `train_grpo_v5.py`）都没有显式设置 `eos_token_id`**——只有一处 `tokenizer.pad_token = tokenizer.eos_token`，没有任何 `generation_config` 或 `eos_token_id` 的覆盖。TRL 的 `GRPOTrainer` 内部调用 `model.generate()` 时会使用 `model.generation_config`，因此生成时**不会在 `<|im_end|>` 处停止**。

`max_completion_length` 会截断（v5 脚本支持此参数），所以不会真正无限生成，但会浪费大量计算在无意义 token 上，且奖励信号质量下降（答案可能被噪声淹没）。

### 2. 模型路径：**存在，但目录名与预期不同**

实际路径：
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/` ✅ 存在（12.3GB）
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/` — 需确认

（你任务描述中写的是 `sft_rasp_20_qwen_math`，但实际是 `sft_qwen_math_rasp_20`）

### 3. v5 vs v1 脚本选择

应该用 **`train_grpo_v5.py`**，因为它有：
- `beta` 参数（v1 没有）
- `loss_type` 参数（支持 dapo）
- `format_reward_weight` 参数
- `repetition_penalty` 参数
- `gradient_checkpointing` 参数
- `optim` 参数（支持 adamw_8bit）
- monkey-patch 让 ref_model 正确加载剪枝模型

### 4. 推荐修复方案（最小侵入）

**方案 A**（推荐）：修改两个 SFT 模型的 `generation_config.json`，将 `eos_token_id` 改为 `[151643, 151645]`。一次修改，所有下游脚本（GRPO + eval）都受益。

**方案 B**：在 `train_grpo_v5.py` 中加载模型后覆盖 `model.generation_config.eos_token_id`。侵入代码，但不改模型文件。

### 5. 启动命令

修复 EOS 后，Qwen Math GRPO 启动命令（参照 DeepSeek 版本参数，`beta` 调为 0.04, `lr` 调为 5e-7）：

```bash
# RASP on GPU 2
cd /root/recovery_aware_struct_prune
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache

CUDA_VISIBLE_DEVICES=2 nohup python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_rasp_20 \
  --gpu 2 \
  --max_completion_length 1024 \
  --beta 0.04 \
  --temperature 0.4 \
  --repetition_penalty 1.15 \
  --format_reward_weight 0.1 \
  --gradient_checkpointing true \
  --optim adamw_bnb_8bit \
  --loss_type dapo \
  --learning_rate 5e-7 \
  --max_steps 100 \
  --save_total_limit 2 \
  --save_steps 5 \
  --reward_desert_patience 50 \
  --run_name grpo_qwen_math_rasp_20 \
  > /root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_qwen_math_rasp_20.log 2>&1 &

# Standard on GPU 3
CUDA_VISIBLE_DEVICES=3 nohup python3 src/train_grpo_v5.py \
  --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 \
  --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_standard_20 \
  --gpu 3 \
  --max_completion_length 1024 \
  --beta 0.04 \
  --temperature 0.4 \
  --repetition_penalty 1.15 \
  --format_reward_weight 0.1 \
  --gradient_checkpointing true \
  --optim adamw_bnb_8bit \
  --loss_type dapo \
  --learning_rate 5e-7 \
  --max_steps 100 \
  --save_total_limit 2 \
  --save_steps 5 \
  --reward_desert_patience 50 \
  --run_name grpo_qwen_math_standard_20 \
  > /root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_qwen_math_standard_20.log 2>&1 &
```

等你确认选方案 A 还是 B 来修复 EOS。

---
