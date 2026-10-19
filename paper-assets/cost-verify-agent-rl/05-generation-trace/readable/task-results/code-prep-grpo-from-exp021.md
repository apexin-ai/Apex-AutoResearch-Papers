# code prep grpo from exp021

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_grpo_from_exp021_20260515T030050_result.json`
- **Structured JSON:** [`a60f0fa25695369d0984.json`](../../sessions/a6/a60f0fa25695369d0984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

### 1. Checkpoint 状态
- **路径**: `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final/`
- **完整**: config.json, model.safetensors (3.4GB), tokenizer 文件齐全
- **模型**: Qwen2.5 系列, 1720.6M 参数, vocab_size=151643
- 另有 checkpoint-160 和 checkpoint-320 两个中间 checkpoint

### 2. Symlink
```
/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4 → .../exp021_ragen_sft_v4/final
```
已创建，路径含 "qwen"，可通过 train.py:137 的断言检查。

### 3. GRPO 配置文件
已写入: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp022_grpo_from_sft_v4.yaml`

启动命令：
```bash
cd /root/cost-verify-agent-rl/RAGEN && \
CUDA_VISIBLE_DEVICES=0,1 python train.py \
  --config-name _alfworld_exp022_grpo_from_sft_v4
```

或用 override 方式（基于 exp020b 的模式）：
```bash
cd /root/cost-verify-agent-rl/RAGEN && \
CUDA_VISIBLE_DEVICES=0,1 python train.py \
  --config-name _alfworld_exp022_grpo_from_sft_v4 \
  model_path=/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4 \
  trainer.experiment_name=exp022-alfworld-grpo-from-sft-v4 \
  trainer.local_log_dir=/root/autodl-tmp/checkpoints/exp022/ \
  trainer.default_local_dir=/root/autodl-tmp/checkpoints/exp022/ \
  es_manager.val.env_groups=4 \
  es_manager.val.env_configs.n_groups=[4]
```

关键参数：LR=5e-7, kl_loss_coef=0.1, grad_clip=1.0, format_penalty=0 (sparse), 30 steps, 双卡。

### 4. Dry-run 结果
模型加载成功，tokenizer 和权重均正常。stderr 有两个无害 warning（Mistral regex 误报、torch_dtype 弃用提示），不影响训练。

### 5. 注意事项
- **磁盘**: /root/autodl-tmp 已用 192G/250G (77%)，剩 59G。exp022 checkpoint 每个约 3.4GB，30 steps save_freq=5 会存 6 个 checkpoint + final = ~24GB，空间足够但偏紧。训练结束后可清理旧实验。
- **val 组数**: 配置用 4 组 val（与 exp020b 一致），而非 exp018 的 16 组，加快 val 速度。
- **前置条件**: 启动前需确认 exp021 eval 结果（RAGEN val success >= 10%）。

---
