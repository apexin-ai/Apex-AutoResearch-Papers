# H-Sweep 实验配置分析 & 多 Seed 方案

## 1. 原始 H-Sweep 完整训练配置

### 共同配置 (所有 h 值)
```yaml
model: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4  # Qwen3-1.7B SFT
algorithm: GRPO
gamma: 0.95
high_level_gamma: 0.95
norm_adv_by_std_in_grpo: True

# Training
total_training_steps: 15
n_gpus_per_node: 2
CUDA_VISIBLE_DEVICES: "0,1"
micro_batch_size_per_gpu: 1
ppo_mini_batch_size: 16

# Actor
lr: 1e-6
optimizer: AdamW (betas: [0.9, 0.999])
kl_loss_type: low_var_kl
kl_loss_coef: 0.01
clip_ratio: [0.2, 0.28]
entropy_coeff: 0.001
loss_agg_mode: token-mean
grad_clip: 1.0
ppo_max_token_len_per_gpu: 65536
use_ref: True
attn_implementation: sdpa

# Rollout (vLLM)
response_length: 1024
gpu_memory_utilization: 0.35
max_model_len: 20480
temperature: 1.0 (train) / 0.4 (val)
max_num_batched_tokens: 20480

# Agent
max_turn: 50
max_actions_per_turn: 1
max_prompt_length: 16384
use_turn_scores: True

# Env
train: 16 env_groups × 8 group_size = 128 episodes/step (K=8)
val: 32 env_groups × 1 group_size = 32 episodes/eval (ID set, AlfworldSG)
format_penalty: 0

# Eval & Checkpoint
test_freq: 5 (eval at step 0, 5, 10, 15)
save_freq: 5
val_before_train: True
logger: [console, wandb]
resume_mode: disable

# Seed
train_seed = SEED * 10000  (seed1→10000, seed2→20000, ...)
```

### 各 h 值差异配置

| 配置项 | h=2 | h=5 | h=10 | h=20 | full |
|--------|-----|-----|------|------|------|
| context_window_mode | step_independent | step_independent | step_independent | step_independent | **full** |
| step_independent_history_length | 2 | 5 | 10 | 20 | 2 (无效) |
| optimizer_offload | True | True | True | **False** ⚠️ | True |
| val_before_train | True | True | True | **false** | True |
| max_actor_ckpt_to_keep | 10 | 10 | 10 | **3** | 10 |

> ⚠️ h=20 的 optimizer_offload=False 是异常值，导致 step 1 update_actor 花了 15139s（4.2h）。建议多 seed 重跑时统一改为 True。

### 启动命令
```bash
cd /root/cost-verify-agent-rl/RAGEN
python train.py --config-name _alfworld_hsweep_h{VALUE} \
    seed.train={SEED*10000} \
    trainer.experiment_name="hsweep-h{VALUE}-seed{SEED}"
```

自动链式启动脚本: `scripts/launch_hsweep.sh <h_value> <seed>`
序列: `2:1 → 2:2 → 10:1 → 5:1 → 20:1 → full:1 → 2:3 → ...`

---

## 2. 每个 h 值的训练时间

### 实测数据 (bjb1, 2× RTX PRO 6000 96GB)

| 实验 | 完成步数 | 总时间 | 平均 step 时间 | 平均 tokens/step | 吞吐量 | 状态 |
|------|---------|--------|---------------|-----------------|--------|------|
| h=2 seed1 | 15/15 | 36127s (**10.0h**) | ~2035s | ~4.4M | 1075 tok/s | ✅ 完成 |
| h=2 seed2 | 15/15 | 43689s (**12.1h**) | ~2800s | ~4.1M | 647 tok/s | ✅ 完成 |
| h=5 seed1 | 0/15 | — | — | — | — | ❌ SIGTERM 初始化时 |
| h=10 seed1 | 0/15 | — | — | — | — | ❌ SIGTERM step0 val |
| h=20 seed1 | ~5/15 | 54968s (**15.3h**) 到 step5 | ~6h (step1), ~7137s (step5) | ~7.7M | 559 tok/s | ⚠️ 部分完成, offload=False |
| full seed1 | 0/15 | — | — | — | — | ❌ Config error |

### 估算（15 steps, 2× RTX PRO 6000, optimizer_offload=True）

基于 response_length 比例和 tokens/step 关系推算：

| h 值 | 平均 response_length | 预估 tokens/step | 预估单次训练时间 | GPU-hours (2 GPU) |
|------|---------------------|-----------------|----------------|-------------------|
| **h=2** | ~687 | ~4.2M | **10-12h** | 20-24 |
| **h=5** | ~800 (估) | ~5.0M | **12-14h** | 24-28 |
| **h=10** | ~950 (估) | ~5.8M | **15-18h** | 30-36 |
| **h=20** | ~1346 | ~7.8M | **20-25h** | 40-50 |
| **full** | ~2000+ (估) | ~10M+ | **28-35h+** | 56-70+ |

> h=20 和 full 的估算不确定性较大，因为长序列的 attention 计算非线性增长。

---

## 3. GPU 状态

### bjb1-17606
```
GPU 0: NVIDIA RTX PRO 6000 Blackwell Server Edition, 96GB
       Status: IDLE (0 MiB used), 27°C, P8
       Driver: 590.44.01, CUDA 13.1
```

> ⚠️ **关键问题：nvidia-smi 只显示 1 张 GPU (cuda:0)**，但所有 h-sweep 配置均要求 `n_gpus_per_node: 2` 和 `CUDA_VISIBLE_DEVICES: "0,1"`。
> 需要确认 cuda:1 是否被其他用户占用、被 `CUDA_VISIBLE_DEVICES` 过滤、或已被释放。
> 若只有 1 GPU，需要修改配置降为单 GPU 模式。

### 磁盘
```
/root/autodl-tmp: 250GB total, 154GB used, 97GB available (62%)
```
每个 h-sweep checkpoint ~3-5GB (save_freq=5, 3个checkpoint)，8 组实验需要 ~24-40GB，可用空间充足。

---

## 4. 评测方式

### 训练中 eval (inline)
- **ID set**: 32 tasks (AlfworldSG), 32 env_groups × 1 group_size
- 频率: 每 5 步 (step 0, 5, 10, 15)
- 温度: 0.4 (do_sample=True)
- 自动记录到 wandb

### 训练后 OOD eval (separate)
- **OOD set**: 134 tasks (AlfworldSG_OOD), 134 env_groups × 1 group_size
- 通过 `_alfworld_hsweep_h2_seed2_reeval_ood.yaml` 类似配置
- 需要为每个 checkpoint 创建单独的 reeval config
- 使用 `resume_mode: resume_path` 加载 checkpoint

---

## 5. 多 Seed 方案建议

### 时间预算分析

假设 30h 墙钟时间限制，bjb1 当前只有 1 GPU（需确认）：

**如果 2 GPU 可用：**
| 方案 | 组合 | 串行总时间 | 可行性 |
|------|------|-----------|--------|
| A: 4h × 2seeds | h=2,5,10,20 × seed2,3 = 8 runs | ~114-138h | ❌ 远超 30h |
| B: 3h × 2seeds | h=2,5,10 × seed2,3 = 6 runs | ~74-88h | ❌ 超 30h |
| C: 4h × 1seed | h=2,5,10,20 × seed2 = 4 runs | ~57-69h | ❌ 超 30h |
| D: 2h × 2seeds | h=2,5 × seed2,3 = 4 runs | ~44-52h | ❌ 超 30h |
| E: 关键点 | h=2,5 × seed2 = 2 runs | ~22-26h | ✅ 刚好 |
| F: 最小集 | h=2 × seed3 + h=5 × seed2 = 2 runs | ~22-26h | ✅ |

**如果 westd-47453 也可用 (4× RTX PRO 6000)：**

| 服务器 | 分配 | 时间 |
|--------|------|------|
| bjb1 (2 GPU, 串行) | h=2×seed2 + h=2×seed3 | ~22h |
| westd (4 GPU, 可并行 2 组 2-GPU runs) | h=5×s2 + h=10×s2 \|\| h=5×s3 + h=10×s3 | ~18h per pair |

→ 两台服务器并行可在 ~22-25h 完成 h=2,5,10 × 2 seeds = 6 runs

### 推荐方案

**方案 1（最可行 — 仅 bjb1, 2GPU确认后）:**
- 跑 h=2 seed2,3 + h=5 seed2 = 3 runs ≈ 34-38h
- 已有数据: h=2 seed1,2 已完成
- 新增: h=2 seed3 + h=5 seed2 = 2 runs ≈ 22-26h ✅

**方案 2（推荐 — bjb1 + westd 双机并行）:**
- bjb1: h=2 × seed3 → h=5 × seed2 → h=5 × seed3 (串行, ~36h)
- westd: h=10 × seed2 → h=10 × seed3 → h=20 × seed2 (串行, ~55h)
- 总墙钟: ~55h, 可覆盖 h=2,5,10,20 各 2-3 seeds

**方案 3（精简版 — 只要关键对比）:**
- 只跑 h=5 seed1,2 (threshold 附近最关键的点)
- ~24-28h, 可在 30h 内完成
- 结合已有 h=2 seed1,2 数据，验证 cliff 位置

### 前置问题（需确认）

1. **bjb1 到底有几张 GPU?** nvidia-smi 只显示 1 张，配置需要 2 张
2. **westd-47453 是否可用?** 4 GPU 机器可以显著加速
3. **h=20 的 optimizer_offload 是否改为 True?** 原配置 False 导致 step 1 极慢
4. **已有的 h=2 seed1,2 数据是否可用?** 还是需要全部重跑？
5. **需要 OOD eval 吗?** 还是只需要 32-task ID eval？
