# Self-Guide ALFWorld GRPO 完整训练 Recipe

**日期**: 2026-05-15
**目标**: 提取 Self-Guide (arXiv 2604.03098) 的 ALFWorld GRPO recipe，对齐 exp028c

---

## 1. 参数对照表

| 参数 | Self-Guide 值 | 来源 | GiGPO GRPO baseline | 来源 | exp027 值 | exp028c 建议值 | 硬件限制 |
|------|-------------|------|---------------------|------|----------|--------------|---------|
| **模型** | Qwen3-1.7B | 论文 Table 1 | Qwen2.5-1.5B-Instruct | 代码 | Qwen3-1.7B (SFT) | **Qwen3-1.7B** (原版) | — |
| **SFT 预训练** | 无 (cold start) | 论文 §4.1 | 无 (cold start) | 代码 | 有 (exp021 SFT) | **无** | — |
| **框架** | verl-agent | 论文 Appendix A | verl-agent | 代码 | RAGEN (自研) | RAGEN | — |
| **LR (actor)** | 1e-6 | 推断¹ | 1e-6 | 代码+论文 E.1 | 5e-7 | **1e-6** | — |
| **总训练步数** | 100 | 论文 Appendix A | 150 | 代码+论文 E.1 | 50 | **100** | — |
| **Env groups (train)** | 16 | 推断¹ | 16 | 代码+论文 E.1 | 8 | **16** | ⚠️ |
| **Group size** | 8 | 推断¹ | 8 | 代码+论文 E.1 | 16 | **8** | — |
| **总 rollouts/step** | 128 | 推断 (16×8) | 128 (16×8) | 论文 E.1 | 128 (8×16) | **128** (16×8) | — |
| **总 rollouts** | 12,800 | 推断 | 19,200 | 计算 | 6,400 | **12,800** | — |
| **Mini-batch size** | 256 | 推断¹ | 256 | 代码+论文 E.1 | 32 | **256** | — |
| **PPO micro batch/GPU** | 32 | 推断¹ | 32 | 代码 | — | **32** | — |
| **PPO epochs** | 1 | 推断² | 1 | 默认配置 | 1 | **1** | — |
| **KL loss coef** | 0.01 | 推断¹ | 0.01 | 代码+论文 E.1 | 0.005 | **0.01** | — |
| **KL loss type** | low_var_kl | 推断¹ | low_var_kl | 代码 | low_var_kl | **low_var_kl** | — |
| **Use KL in reward** | False | 推断¹ | False | 代码 | False | **False** | — |
| **Entropy coef** | 0.001 | 推断² | 0.001 | 默认配置 | 0.01 | **0.001** | — |
| **Clip ratio** | 0.2 | 推断² | 0.2 | 默认配置 | 0.2 | **0.2** | — |
| **Max grad norm** | 1.0 | 推断² | 1.0 | 默认配置 | 1.0 | **1.0** | — |
| **Gamma (discount)** | 0.95 | 推断¹ | 0.95 | 论文 E.1 | 0.95 | **0.95** | — |
| **Max episode steps** | 50 | 论文 Appendix A | 50 | 代码+论文 E.1 | 50 | **50** | — |
| **Max prompt length** | 4096 | 论文 Appendix A | 2048 | 代码+论文 E.1 | 4096 | **4096** | ⚠️ |
| **Max response length** | 1024 | 论文 Appendix A | 512 | 代码+论文 E.1 | 1024 | **1024** | ⚠️ |
| **History length** | 2 | 推断³ | 2 | 论文 E.2 | 5 | **2** | — |
| **Context mode** | step_independent | 推断¹ | step-by-step | 代码 | step_independent | **step_independent** | — |
| **Rollout temperature** | 1.0 | 论文 Appendix A | 1.0 | 论文 E.1 | — | **1.0** | — |
| **Val temperature** | 0.4 | 论文 Appendix A | 0.4 | 代码+论文 E.1 | — | **0.4** | — |
| **奖励: 成功** | +10 | 推断¹ | +10 | 论文 E.1 | +10 | **+10** | — |
| **奖励: 失败** | 0 | 推断¹ | 0 | 论文 E.1 | 0 | **0** | — |
| **Invalid action penalty** | -0.1 | 推断¹ | -0.1 | 代码+论文 E.1 | 0 (binary) | **-0.1** | — |
| **Reward normalization** | mean_std_norm | 推断² | mean_std_norm | 推断 | identity | **mean_std_norm** | — |
| **Loss agg mode** | token-mean | 推断¹ | token-mean | 推断 | seq-mean-token-mean | **token-mean** | — |
| **Weight decay** | 0.01 | 推断² | 0.01 | 默认配置 | — | **0.01** | — |
| **Warmup** | 0 | 推断² | 0 | 默认配置 | — | **0** | — |
| **Val episodes** | 128 | 推断¹ | 128 | 代码 | 16 | **128** | — |
| **Test freq** | 5 | 推断¹ | 5 | 代码 | 5 | **5** | — |
| **Save freq** | -1 | 推断¹ | -1 | 代码 | 5 | **5** | — |
| **Val before train** | True | 推断¹ | True | 代码 | — | **True** | — |
| **Gradient checkpointing** | True | 推断¹ | True | 代码 | — | **True** | — |
| **Ref param offload** | True | 推断¹ | True | 代码 | — | **True** | — |
| **Actor param offload** | False | 推断¹ | False | 代码 | — | **False** | — |
| **TP size** | 2 | 推断¹ | 2 | 代码 | — | **2** | — |
| **GPU memory util** | 0.6 | 推断¹ | 0.6 | 代码 | — | **0.6** | ⚠️ |
| **硬件** | 未披露 | — | 2×H100 (80GB) | 论文 E.1 | 2×RTX PRO 6000 (48GB) | 2×RTX PRO 6000 | ⚠️ |
| **GRPO 结果** | **72.7%** | 论文 Table 1 | **72.8% ±3.6%** | 论文 Table 2 | **10.16%** | 目标 **~70%** | — |

### 来源标注说明
- **论文**: Self-Guide 论文 (2604.03098) 明确写的
- **代码**: verl-agent `run_alfworld.sh` 中明确设定的
- **论文 E.1**: GiGPO 论文 (2505.10978) Appendix E.1 明确写的
- **默认配置**: verl-agent `ppo_trainer.yaml` 默认值
- **推断¹**: Self-Guide 使用 verl-agent 框架 → 参数与 GiGPO GRPO baseline 的 `run_alfworld.sh` 一致
- **推断²**: Self-Guide 未披露 → 取 verl-agent 框架默认值
- **推断³**: GiGPO 论文 E.2 明确说 ALFWorld history=2，Self-Guide 同框架同环境

---

## 2. exp027 vs 目标 recipe 的关键差异（按影响排序）

| # | 差异项 | exp027 | exp028c 目标 | 倍数 | 影响 |
|---|--------|--------|-------------|------|------|
| 1 | SFT 起点 | SFT checkpoint (6.25%) | Instruct cold-start | — | 🔴 极高 |
| 2 | Invalid action penalty | 0 (binary) | -0.1 | ∞ | 🔴 极高 |
| 3 | Mini-batch size | 32 | 256 | 8× | 🔴 高 |
| 4 | 总训练步数 | 50 | 100 | 2× | 🟡 中高 |
| 5 | LR | 5e-7 | 1e-6 | 2× | 🟡 中 |
| 6 | KL coef | 0.005 | 0.01 | 2× | 🟡 中 |
| 7 | Env groups | 8 | 16 | 2× | 🟡 中 |
| 8 | Group size | 16 | 8 | 0.5× | 🟡 中 |
| 9 | Entropy coef | 0.01 | 0.001 | 0.1× | 🟢 低 |
| 10 | History length | 5 | 2 | 0.4× | 🟢 低 |
| 11 | Loss agg | seq-mean-token-mean | token-mean | — | 🟢 低 |

---

## 3. 不确定项

| 项目 | 状态 | 置信度 | 推断依据 |
|------|------|--------|---------|
| Self-Guide LR | 推断 1e-6 | 🟡 高 | 使用 verl-agent 框架，GiGPO paper E.1 明确 ALFWorld actor LR=1e-6 |
| Self-Guide mini-batch | 推断 256 | 🟡 高 | 同上 |
| Self-Guide KL coef | 推断 0.01 | 🟡 高 | 同上 |
| Self-Guide group_size | 推断 8 | 🟡 高 | 同上 |
| Self-Guide env_groups | 推断 16 | 🟡 高 | 同上 |
| Self-Guide gamma | 推断 0.95 | 🟡 高 | GiGPO paper E.1 明确 γ=0.95 for ALFWorld |
| Self-Guide invalid_action_penalty | 推断 -0.1 | 🟡 高 | verl-agent run script 默认启用 |
| Self-Guide history_length | 推断 2 | 🟡 高 | GiGPO paper E.2 明确 ALFWorld+WebShop history=2 |
| Self-Guide reward normalization | 推断 mean_std_norm | 🟠 中 | verl-agent 可能有 adv_norm 但未确认 |
| Self-Guide max_prompt 4096 vs GiGPO 2048 | 已确认不同 | 🟢 确定 | Self-Guide 论文明确 4096，GiGPO 论文/代码明确 2048 |
| Self-Guide max_response 1024 vs GiGPO 512 | 已确认不同 | 🟢 确定 | 同上 |
| Self-Guide 硬件 | 完全未知 | 🔴 低 | 论文未披露 |
| Self-Guide 代码仓库 | 未找到 | — | 论文未提供 GitHub link |
| Qwen3-1.7B 零样本 ALFWorld success | 未测 | — | 需要 exp028c 前验证 |

---

## 4. 硬件适配说明

### 4.1 硬件对比

| | GiGPO (参考) | 我们 (exp028c) |
|--|-------------|---------------|
| GPU 型号 | H100 80GB | RTX PRO 6000 48GB |
| GPU 数量 | 2 | 2 |
| 总 VRAM | 160 GB | 96 GB |
| VRAM 差距 | — | **-40%** |
| 互联 | NVLink | PCIe (推测) |

### 4.2 需要调整的参数

**可能需要调整：**

1. **`gpu_memory_utilization`**: GiGPO 用 0.6 (在 80GB 上 = 48GB)。我们 48GB × 0.6 = 28.8GB 可能不够。
   - 建议：先试 0.6，如果 OOM 则升到 0.7-0.8
   - Qwen3-1.7B 较小，0.6 可能够用

2. **`max_prompt_length` 和 `max_response_length`**: Self-Guide 用 4096/1024，GiGPO 用 2048/512。
   - 更长的 sequence → 更多 VRAM
   - 建议：先用 GiGPO 的 2048/512（硬件友好），如果 success rate < 60% 再尝试 4096/1024
   - 理由：GiGPO 用 2048/512 在 Qwen2.5-1.5B 上也达到了 72.8%

3. **`env_groups=16`**: 16 个并行环境 × 8 rollouts = 128 trajectories 需要同时推理。
   - 在 2×48GB 上推 Qwen3-1.7B 应该没问题
   - 如果 OOM：降到 env_groups=12 + group_size=8 = 96 rollouts

**无需调整：**
- `ppo_mini_batch_size=256`: 这是梯度累积的 batch，不影响 VRAM
- `tensor_model_parallel_size=2`: Qwen3-1.7B 足够小，TP=2 可用
- `ref param_offload=True`: 已开启，节省 VRAM

### 4.3 模型差异

Self-Guide 用 Qwen3-1.7B，GiGPO 用 Qwen2.5-1.5B-Instruct。两者不同：
- Qwen3-1.7B: 更新架构，思维链能力更强（带 `<think>` tag）
- Qwen2.5-1.5B: GiGPO 验证过的模型，结果可复现
- 建议 exp028c 用 **Qwen3-1.7B**（与 Self-Guide 一致，且是我们项目的目标模型）

---

## 5. 建议 exp028c 完整配置

```yaml
# === exp028c: Self-Guide recipe alignment ===

# Model
model_path: Qwen/Qwen3-1.7B  # 原版 Instruct, 不用 SFT checkpoint

# Optimization
actor:
  optim:
    lr: 1e-6
    weight_decay: 0.01
  ppo_mini_batch_size: 256
  ppo_micro_batch_size_per_gpu: 32
  ppo_epochs: 1
  clip_ratio: 0.2
  max_grad_norm: 1.0
  entropy_coeff: 0.001
  use_kl_loss: True
  kl_loss_coef: 0.01
  kl_loss_type: low_var_kl
  enable_gradient_checkpointing: True
  fsdp_config:
    param_offload: False
    optimizer_offload: False

# Reference model
ref:
  fsdp_config:
    param_offload: True

# Rollout
rollout:
  tensor_model_parallel_size: 2
  gpu_memory_utilization: 0.6    # 如 OOM 升到 0.7
  temperature: 1.0               # rollout 用 1.0
  val_kwargs:
    temperature: 0.4
    do_sample: True

# Data
data:
  max_prompt_length: 4096        # Self-Guide 值; 如 VRAM 不够降到 2048
  max_response_length: 1024      # Self-Guide 值; 如 VRAM 不够降到 512

# Environment
env:
  max_steps: 50
  group_size: 8
  train:
    env_groups: 16               # 16 unique tasks per step
  val:
    env_groups: 128              # 128 episodes per eval

# Training
trainer:
  total_training_steps: 100
  test_freq: 5
  save_freq: 5                   # 每 5 步存 checkpoint
  val_before_train: True

# Algorithm
algorithm:
  adv_estimator: grpo
  use_kl_in_reward: False
  gamma: 0.95

# Agent
agent:
  context_window_mode: step_independent
  step_independent_history_length: 2
  loss_agg_mode: token-mean

# Reward
reward:
  success_reward: 10.0
  failure_reward: 0.0
  invalid_action_penalty_coef: 0.1

# Hardware
hardware:
  n_gpus_per_node: 2
  nnodes: 1
  # Constraint C001: cuda:0, cuda:1 only
```

### 与 exp027 的 diff 汇总

```diff
- model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
+ model_path: Qwen/Qwen3-1.7B

- lr: 5e-7
+ lr: 1e-6

- ppo_mini_batch_size: 32
+ ppo_mini_batch_size: 256

- kl_loss_coef: 0.005
+ kl_loss_coef: 0.01

- entropy_coeff: 0.01
+ entropy_coeff: 0.001

- total_training_steps: 50
+ total_training_steps: 100

- env_groups_train: 8
+ env_groups_train: 16

- group_size: 16
+ group_size: 8

- invalid_action_penalty: 0 (binary)
+ invalid_action_penalty_coef: 0.1

- step_independent_history_length: 5
+ step_independent_history_length: 2

- loss_agg_mode: seq-mean-token-mean
+ loss_agg_mode: token-mean

- val_episodes: 16
+ val_episodes: 128
```

---

## 6. 预期效果

| 指标 | exp027 | exp028c 预期 | 依据 |
|------|--------|-------------|------|
| Success rate | 10.16% | **60-75%** | Self-Guide Qwen3-1.7B GRPO=72.7% |
| 训练时间 | ~6h (50 steps) | ~12h (100 steps) | 线性外推，env_groups 翻倍可能增加 rollout 时间 |
| GPU 内存 | 稳定 | 需监控 | 4096 prompt + 16 env_groups 可能更吃内存 |

### 风险点
1. **Qwen3-1.7B 零样本能力未验证**: 如果零样本 success < 5%，cold start 可能不如预期
2. **VRAM**: 4096 prompt length + env_groups=16 可能 OOM → 准备 fallback 到 2048/512
3. **框架差异**: 我们用 RAGEN 而非 verl-agent，实现细节可能有差异（loss agg、advantage 计算等）

---

## 7. 数据来源

- Self-Guide: [arXiv 2604.03098](https://arxiv.org/abs/2604.03098) — 论文 §4.1, Appendix A, Table 1
- GiGPO: [arXiv 2505.10978](https://arxiv.org/abs/2505.10978) — 论文 Appendix E.1, E.2
- verl-agent 代码: [GitHub langfengQ/verl-agent](https://github.com/langfengQ/verl-agent) — `examples/grpo_trainer/run_alfworld.sh`, `verl/trainer/config/ppo_trainer.yaml`
- exp027 数据: `recipe_gap_analysis.md`, checkpoint JSON files
