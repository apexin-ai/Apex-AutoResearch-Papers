# research smolvla libero gap deep dive

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla_libero_gap_deep_dive_20260517T001826_result.json`
- **Structured JSON:** [`c529f296c89275fe310f.json`](../../sessions/c5/c529f296c89275fe310f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the information needed. Here's the complete analysis:

---

## === 差异分析 ===

| 对比项 | 我们 | SmolVLA 官方 | 差异影响 |
|--------|------|-------------|----------|
| **Batch size** | **4** | **64** | **极高 (16x)** |
| 总样本量 (steps×batch) | 400K | 6.4M | 极高 (16x) |
| 训练步数 | 100K | 100K | 无 |
| 学习率 | 1e-4 | 1e-4 | 无 |
| LR scheduler | cosine | cosine | 无 |
| **Warmup steps** | **1000** | **100** | 低 |
| Decay LR (eta_min) | 2.5e-6 | 2.5e-6 | 无 |
| Optimizer | AdamW β=(0.9,0.95) | AdamW β=(0.9,0.95) | 无 |
| Weight decay | 1e-10 | 1e-10 | 无 |
| Gradient clipping | 10.0 | 10.0 | 无 |
| 图像分辨率 (env render) | 256×256 | 256×256 | 无 |
| 模型内部 resize | 512×512 | 512×512 | 无 |
| Action normalization | MEAN_STD | MEAN_STD | 无 (训练时) |
| State normalization | MEAN_STD | MEAN_STD | 无 (训练时) |
| n_action_steps (eval) | 50 | 50 | 无 |
| 训练模式 | train_expert_only | train_expert_only | 无 |
| 可训练参数 | ~100M | ~100M | 无 |
| Eval episodes/task | 50 | 10 | 无 (更严格) |
| Max steps (Object) | 280 | 280 | 无 |
| 数据集 | HuggingFaceVLA/libero | HuggingFaceVLA/libero | 无 |
| **Eval 归一化处理** | **可能缺 unnormalize** | **lerobot-eval 内置处理** | **中等** |

## === 87.3% 引用来源 ===

- **论文**: [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/html/2506.01844v1)
- **87.3% = 4 个 suite 的平均值** (不是 5 个):
  - Spatial: 90%
  - Object: **96%**
  - Goal: 92%
  - Long (libero_10): 71%
- 评估协议: 10 episodes per task × 10 tasks/suite = 100 episodes/suite
- 模型大小: 0.45B (SmolVLA-base)

对比我们 Object suite: **44.8% (seed=42) / 51.0% (seed=0)** vs 官方 **96%** — 差距 45-51 个百分点。

## === Gap 根因排序 ===

### 1. [最关键] Batch Size: 4 vs 64 (16x 差距)

这是**决定性差异**。

- 我们: 4 × 100K = **400K 样本**
- 官方: 64 × 100K = **6.4M 样本**
- 16x 数据曝光差距，对 10 个 task 并行学习是致命的
- Per-task 分布: 我们每个 task 仅 ~40K 样本，不足以收敛
- 证据: 你的结果中容易 task (cream cheese: 74%, bbq sauce: 68-74%) 部分收敛，难 task (alphabet soup: 2-4%) 完全失败 — 典型的欠训练模式
- GitHub issue [#3287](https://github.com/huggingface/lerobot/issues/3287) 也怀疑官方可能用了多 GPU (4×64=256 effective batch)，但未获官方回复

### 2. [中等] 可能的 Eval 归一化 Bug

你的 eval 脚本 `predict_actions()` 直接调用 `policy.model.sample_actions()`，绕过了 `SmolVLAPolicy` 的 `normalize_inputs()` / `unnormalize_outputs()` 方法。

- 训练时 LeRobotDataset 返回归一化后的 state/action
- Eval 时 `obs_to_batch()` 传入 RAW state（未归一化）
- 模型输出归一化后的 action，直接 clip 到 [-1,1] 使用（未反归一化）
- LIBERO action 本身在 [-1,1]，所以 MEAN_STD 偏移不大，部分 task 仍能工作
- 但对精度要求高的 task（如 alphabet soup），归一化偏移足以导致抓取失败

### 3. [低] Warmup Steps: 1000 vs 100

多浪费 900 步在极低 LR，影响不大但略微减少有效训练量。

### 4. [确认非问题] 其他项

- 图像分辨率: 都是 256→512 (model internal resize)，一致
- Action space, control mode, max_steps: 一致
- train_expert_only: 一致
- n_action_steps=50: 一致 (SmolVLA 默认执行完整 chunk)

## === 建议修复 ===

**优先级 1: Batch Size → 64**
```yaml
training:
  batch_size: 64        # 从 4 改为 64
  # 单 GPU VRAM 不够就用 gradient accumulation:
  # batch_size: 8
  # gradient_accumulation_steps: 8  # effective batch = 64
```

如果单 GPU (24GB) 放不下 batch=64:
- SmolVLA expert-only ~100M params + 2张 256×256 图 → 估计 batch=8~16 可行
- 用 `gradient_accumulation_steps` 补到 effective 64

**优先级 2: 修复 Eval 归一化**
```python
# 替换 predict_actions() 为:
@torch.no_grad()
def predict_actions(policy, batch: dict) -> torch.Tensor:
    # 使用 policy 层级接口，自动处理 normalize/unnormalize
    actions = policy.select_action(batch)
    return actions
```

或者手动加归一化:
```python
# 在 obs_to_batch 中对 state 做 normalize
state_mean = policy.config.normalization_mapping["observation.state"].mean
state_std = policy.config.normalization_mapping["observation.state"].std
state_normalized = (state - state_mean) / state_std

# 对 model output 做 unnormalize
action_mean = policy.config.normalization_mapping["action"].mean
action_std = policy.config.normalization_mapping["action"].std
action_raw = action_normalized * action_std + action_mean
```

**优先级 3: Warmup → 100**
```yaml
training:
  warmup_steps: 100     # 从 1000 改为 100
```

**快速验证建议**: 先只改 batch_size=64 (或 grad_accum 到 effective 64)，保持 100K steps，观察是否能到 80%+。如果 VRAM 限制只能到 batch=16，那需要 400K steps 才能达到同样的总样本量。

Sources:
- [SmolVLA Paper (arxiv)](https://arxiv.org/html/2506.01844v1)
- [GitHub Issue #3287 - Replication Inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [GitHub Issue #2294 - LIBERO Config Discrepancy](https://github.com/huggingface/lerobot/issues/2294)
- [LeRobot LIBERO Docs](https://huggingface.co/docs/lerobot/libero)
- [SmolVLA HuggingFace Docs](https://huggingface.co/docs/lerobot/en/smolvla)
- [smolvla_base config.json](https://huggingface.co/lerobot/smolvla_base/blob/04d96c1f9167360280aaa54de31418f824d1ef48/config.json)

---
