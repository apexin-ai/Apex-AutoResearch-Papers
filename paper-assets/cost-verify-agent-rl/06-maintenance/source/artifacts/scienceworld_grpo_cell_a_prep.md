# ScienceWorld GRPO Cell A — Preparation Report

> Date: 2026-05-20 | Server: bjb1-17606 (2× RTX PRO 6000 96GB) | Priority: P1

## 目标

在 ScienceWorld 上复现 ALFWorld Cell A 的 collapse pattern：step-level reward + sliding window (h=2) 导致 sign misattribution → 训练崩溃。对应 paper_framing.md Reviewer Attack Surface #5（Single environment）。

## 就绪状态

| 项目 | 状态 | 说明 |
|------|------|------|
| ScienceWorld env 代码 | ✅ 就绪 | `ragen/env/scienceworld/{env.py,config.py,__init__.py}` 已实现 |
| env 注册 | ✅ 就绪 | `ragen/env/__init__.py` 已注册 `scienceworld` type |
| SFT checkpoint | ✅ 就绪 | `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface` (Qwen3-1.7B) |
| Java runtime | ✅ 就绪 | eval_v2 正在用 scienceworld JVM 运行 |
| scienceworld package | ✅ 就绪 | 已安装在 conda base 环境 |
| 磁盘空间 | ⚠️ 61GB 可用 | 需 ~15-20GB for checkpoints，足够 |
| envs.yaml ScienceWorld 条目 | ❌ 需创建 | 需添加 `ScienceWorldSG` tag |
| GRPO config yaml | ❌ 需创建 | `_scienceworld_cell_a_grpo.yaml` |
| 代码修改 | ✅ 无需 | 现有代码已完整支持 |

## 需要创建的文件

### 1. envs.yaml 追加 ScienceWorld 条目

在 `/root/cost-verify-agent-rl/RAGEN/config/envs.yaml` 末尾追加：

```yaml
  # --- ScienceWorld ---
  ScienceWorldSG:
    env_type: scienceworld
    max_actions_per_traj: 100
    parallel_friendly: false
    max_workers: 1
    env_instruction: |
      You are a science student performing experiments in a virtual science lab.
      Complete the given task by navigating rooms and interacting with objects.

      Your reasoning MUST be enclosed within <think> </think> tags.
      After the closing </think> tag, wrap your chosen action in <answer> </answer> tags.
      The action must be from the admissible actions list.
      Do NOT output anything after the </answer> tag.

      Example: <think>I need to boil water. I should go to the kitchen first.</think><answer>open door to kitchen</answer>
    max_tokens: 512
    env_config:
      task_names: "boil,melt,freeze,change-the-state-of-matter-of,use-thermometer,measure-melting-point-known-substance,measure-melting-point-unknown-substance,power-component,power-component-renewable-vs-nonrenewable-energy,test-conductivity,test-conductivity-of-unknown-substances,find-living-thing,find-non-living-thing,find-plant,find-animal,grow-plant,grow-fruit,chemistry-mix,chemistry-mix-paint-secondary-color,chemistry-mix-paint-tertiary-color,lifespan-longest-lived,lifespan-shortest-lived,lifespan-longest-lived-then-shortest-lived,identify-life-stages-1,identify-life-stages-2,inclined-plane-determine-angle,inclined-plane-friction-named-surfaces,inclined-plane-friction-unnamed-surfaces,mendelian-genetics-known-plant,mendelian-genetics-unknown-plant"
      score: 10.0
      max_steps: 100
      max_valid_actions: 50
      eval_split: "dev"
```

**设计决策：**
- `env_instruction` 基于 SFT 训练的 system prompt，但改用 `<answer>` tags 以匹配 RAGEN ctx_manager 的标准格式（RAGEN 有 Qwen3 bare-text fallback parser，两种格式都能解析）
- `task_names` 包含全部 30 个 ScienceWorld 任务（从 `tasks.json` 提取的完整列表）
- `score: 10.0` 与 ALFWorld 一致（reward = final_score/100 × 10）
- `max_steps: 100` 是 ScienceWorld 标准
- `parallel_friendly: false` + `max_workers: 1`：ScienceWorld JVM singleton 约束
- `eval_split: "dev"`：val 使用 dev split（与 eval_v2 一致）

### 2. GRPO Cell A 配置文件

创建 `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_a_grpo.yaml`：

```yaml
# ScienceWorld Cell A: step-level reward + sliding window (h=2)
# 对标 ALFWorld hsweep_h2，预期 collapse
# 控制变量：仅改 environment 和 model_path，其余参数与 ALFWorld Cell A 完全一致

defaults:
  - base

hydra:
  searchpath:
    - pkg://verl.trainer.config

model_path: /root/autodl-tmp/checkpoints/scienceworld_sft/huggingface

system:
  CUDA_VISIBLE_DEVICES: "0,1"

micro_batch_size_per_gpu: 1
ppo_mini_batch_size: 16

trainer:
  project_name: cost-verify-agent-rl
  experiment_name: scienceworld-cell-a-h2
  total_training_steps: 15
  n_gpus_per_node: 2
  val_before_train: True
  test_freq: 5
  save_freq: 5
  local_log_dir: "/root/autodl-tmp/checkpoints/scienceworld-cell-a/"
  default_local_dir: "/root/autodl-tmp/checkpoints/scienceworld-cell-a/"
  logger: ['console', 'wandb']
  max_actor_ckpt_to_keep: 10
  resume_mode: "disable"

actor_rollout_ref:
  model:
    override_config:
      attn_implementation: sdpa
  actor:
    fsdp_config:
      optimizer_offload: True
    use_ref: True
    use_torch_compile: False
    use_kl_loss: True
    kl_loss_coef: 0.01
    kl_loss_type: low_var_kl
    entropy_coeff: 0.001
    clip_ratio_low: 0.2
    clip_ratio_high: 0.28
    loss_agg_mode: "token-mean"
    grad_clip: 1.0
    ppo_max_token_len_per_gpu: 65536
    optim:
      lr: 1e-6
  ref:
    use_torch_compile: False
    log_prob_max_token_len_per_gpu: 65536
  rollout:
    response_length: 512
    gpu_memory_utilization: 0.35
    enable_chunked_prefill: true
    max_model_len: 20480
    temperature: 1.0
    max_num_batched_tokens: 20480
    enforce_eager: True
    val_kwargs:
      do_sample: True
      temperature: 0.4

algorithm:
  adv_estimator: grpo
  gamma: 0.95
  high_level_gamma: 0.95
  norm_adv_by_std_in_grpo: True

agent_proxy:
  context_window_mode: "step_independent"
  max_context_window: -1
  step_independent_history_length: 2
  max_turn: 100
  max_actions_per_turn: 1
  max_prompt_length: 16384
  use_turn_scores: True

collapse_detection:
  multi_turn_enabled: false

es_manager:
  format_penalty: 0
  train:
    env_groups: 16
    group_size: 8
    env_configs:
      tags: ["ScienceWorldSG"]
      n_groups: [16]
  val:
    env_groups: 32
    group_size: 1
    env_configs:
      tags: ["ScienceWorldSG"]
      n_groups: [32]
```

**与 ALFWorld Cell A (hsweep_h2) 的差异：**

| 参数 | ALFWorld Cell A | ScienceWorld Cell A | 原因 |
|------|-----------------|---------------------|------|
| model_path | qwen3_exp021_ragen_sft_v4 | scienceworld_sft/huggingface | 不同环境的 SFT 模型 |
| experiment_name | hsweep-h2 | scienceworld-cell-a-h2 | — |
| max_turn | 50 | 100 | ScienceWorld 标准 max_steps=100 |
| response_length | 1024 | 512 | ScienceWorld 动作更短，512 足够 |
| env tags | AlfworldSG | ScienceWorldSG | — |
| local_log_dir | hsweep-h2/ | scienceworld-cell-a/ | — |

**保持一致的参数（控制变量）：**
- context_window_mode: step_independent, h=2
- algorithm: GRPO, gamma=0.95
- lr: 1e-6, kl_loss_coef: 0.01
- clip_ratio: 0.2-0.28, entropy_coeff: 0.001
- train: 16 groups × 8 = 128 episodes, val: 32 groups × 1 = 32 episodes
- total_training_steps: 15
- format_penalty: 0

## 训练命令

```bash
cd /root/cost-verify-agent-rl/RAGEN
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=0,1 python train.py --config-name _scienceworld_cell_a_grpo 2>&1 | tee /root/autodl-tmp/checkpoints/scienceworld-cell-a/train.log
```

## 预估资源需求

- **GPU**: 2× RTX PRO 6000 96GB — 充足（1.7B 模型 + step_independent h=2 窗口很小）
- **显存**: 预估 <40GB/卡（ALFWorld Cell A 1.7B 在同配置下 ~30GB/卡）
- **磁盘**: ~15-20GB for checkpoints（15 steps × ~1GB/ckpt + optimizer）
- **训练时长**: 预估 8-15h（ScienceWorld 100 步 episodes 比 ALFWorld 50 步更长，且 JVM 有额外开销）
- **瓶颈**: Rollout 时间（128 sequential ScienceWorld episodes × 100 max steps + JVM overhead）

## 提交前 Pre-flight Checklist (C002)

- [ ] 确认入口点：`python train.py --config-name _scienceworld_cell_a_grpo`（与 ALFWorld 实验一致的 train.py 入口）
- [ ] `df -h` 检查磁盘：当前 61GB 可用，需 ~20GB
- [ ] 验证 config 参数与框架版本兼容
- [ ] 确认 checkpoint 路径存在：`/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface`
- [ ] 确认 envs.yaml 中 ScienceWorldSG 条目已添加
- [ ] 确认 Java runtime 可用（`java -version`）
- [ ] dry-run 验证（短 1-2 step 训练确认不 crash）

## 风险与注意事项

1. **SFT prompt format mismatch**: SFT 训练用 bare-text action（`</think>action`），RAGEN 用 `<answer>` tags。RAGEN 有 fallback parser 可以处理两种格式，但模型生成可能偏向 bare-text → format_rate 可能低于 ALFWorld。Cell A 实验目的是展示 collapse，format mismatch 不影响核心结论。

2. **JVM 开销**: ScienceWorld 每个 env 实例需要 JVM。128 个 env 实例意味着 128 个 JVM 进程。可能需要监控内存。如果 OOM，降低 train env_groups 到 8 (64 episodes)。

3. **ScienceWorld reward 是连续的**: `reward = final_score/100 * 10`，range [-10, +10]。与 ALFWorld binary reward (0 or 10) 不同。GRPO group normalization 仍然适用，sign misattribution 机制仍然成立。

4. **Episode 长度**: 100 max steps vs ALFWorld 50 steps。Rollout 更慢，但 step_independent h=2 的训练样本大小不变。

5. **eval_v2 还在跑**: 当前 bjb1 GPU 被 eval_v2 占用。需等其完成（预计还需 ~10h）后才能启动。在等待期间可以先在 CPU 上做 dry-run 验证 config 正确性。

## ScienceWorld vs ALFWorld 环境对比

| 维度 | ALFWorld | ScienceWorld |
|------|----------|--------------|
| 环境类型 | 家庭任务（pick, clean, heat...）| 科学实验（boil, grow, measure...）|
| 任务数 | 6 types | 30 types |
| 最大步数 | 50 | 100 |
| 动作空间 | admissible actions | admissible actions (更大) |
| Reward | binary (0/10) | continuous (-10 to +10) |
| Backend | Python (TWC) | Java (JVM via py4j) |
| SFT baseline | ~28% (in-dist) | ~30.8% (dev, eval_v2 partial) |
| 模型 | Qwen3-1.7B (ALFWorld SFT) | Qwen3-1.7B (ScienceWorld SFT) |
