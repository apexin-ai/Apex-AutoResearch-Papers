# LeRobot 官方 Eval 调研报告

## 1. LeRobot v0.5.1 官方 eval 流程

### 关键路径
- `lerobot/rl/eval_policy.py` — RL eval loop（简单循环）
- `lerobot/envs/factory.py` — env 创建
- `lerobot/envs/utils.py::preprocess_observation()` — obs 预处理
- `lerobot/policies/smolvla/modeling_smolvla.py::select_action()` — action 推理
- `lerobot/policies/smolvla/processor_smolvla.py` — preprocessor/postprocessor pipeline

### 官方 obs 处理流程
1. `preprocess_observation(obs)`:
   - `pixels["top"]` → `observation.images.top`: HWC uint8 → CHW float32 [0,1]
   - `agent_pos` → `observation.state`: float tensor
2. `policy._prepare_batch(batch)`:
   - 如果 `adapt_to_pi_aloha=True`，翻转 joints [1,2,8,9]，gripper 线性→角度转换
   - SmolVLA base: `adapt_to_pi_aloha=False`，不做任何转换
3. `policy.prepare_images(batch)`:
   - 如果 5D 取 `[:, -1, :]`
   - `resize_with_pad` 到 512x512
   - **[0,1] → [-1,1]** (SigLIP 要求)
4. `policy.prepare_state(batch)`: pad 到 max_state_dim=32

### 官方 action 处理
1. `_get_action_chunk()`:
   - 调 `model.sample_actions()` (flow matching ODE)
   - 截断到 `action_feature.shape[0]` 维
   - 如果 `adapt_to_pi_aloha=True`，调 `_pi_aloha_encode_actions()`
2. `select_action()`:
   - 用 deque 管理 action queue (maxlen=n_action_steps=50)
   - queue 空时才调 `_get_action_chunk()`
   - 每步 pop 一个 action

### Normalization
- SmolVLA config: STATE=MEAN_STD, ACTION=MEAN_STD, VISUAL=IDENTITY
- **但这只在 processor pipeline 中使用（新 v0.5 API）**
- 直接调 `select_action` / `forward` **不会做 normalization**
- 我们的训练代码直接调 `policy.forward(batch)` → 不经过 processor → 数据在原始空间
- 因此 eval 也不需要 normalize/unnormalize ✅

## 2. 我们的 eval_success_rate.py 与官方的差异

| 项目 | LeRobot 官方 | 我们的 eval_success_rate.py | 是否有影响 |
|------|-------------|---------------------------|-----------|
| obs 图像处理 | preprocess_observation → [0,1] CHW | 手动 permute+/255.0 | ✅ 一致 |
| state 处理 | float tensor, 无 norm | float tensor, 无 norm | ✅ 一致 |
| 图像 key | observation.images.top | observation.images.top | ✅ 一致 |
| language tokens | tokenizer + \n | tokenizer + \n | ✅ 一致 |
| action chunk | select_action queue (一步一步) | 整块执行 action_horizon=50 | ⚠️ 微小差异，但 n_action_steps=50=chunk_size，等价 |
| action clip | 官方不 clip | np.clip(-1, 1) | ⚠️ 微小差异，数据中有 16.6% actions |a|>1 |
| adapt_to_pi_aloha | False (smolvla_base config) | 未实现 | ✅ 不影响（config 为 False）|
| normalization | 不经过 processor → 无 | 无 | ✅ 一致 |
| prepare_images | policy 内部调，resize+pad 到 512x512 | 通过 predict_actions 调 policy.prepare_images | ✅ 一致 |

**结论：eval pipeline 没有遗漏关键步骤。**

## 3. 已知 Reference Success Rate

| 模型 | 任务 | Success Rate | 来源 |
|------|------|-------------|------|
| ACT (LeRobot) | aloha_sim_insertion | ~20% (50 ep eval) | lerobot/act_aloha_sim_insertion_human model card |
| ACT (原论文) | aloha_sim_insertion | ~50% | ACT paper |
| SmolVLA base (pretrained) | aloha_sim_insertion | 0% | 预期—未在此任务训练 |
| SmolVLA (LIBERO) | LIBERO avg | 87.3% | SmolVLA paper |
| SmolVLA (社区报告) | aloha_sim_insertion | 训练不收敛 | GitHub issue #2700 |

**关键发现：SmolVLA 在 aloha_sim_insertion 上的 finetune 是已知困难的。** GitHub 上有用户报告相同问题。

## 4. 0% Success Rate 的根因（已在 sim_rollout_diagnosis.md 中诊断）

### 主因：LoRA fine-tuning 导致 flow matching mode collapse

| Model | Action std | Image sensitivity |
|-------|-----------|-------------------|
| Pretrained (no LoRA) | 0.104 | 0.149 |
| LoRA fine-tuned | 0.006 | 0.024 |

- ODE 推理从任意噪声收敛到同一个固定点（~dataset mean action）
- LoRA alpha/rank=2.0 的 scaling 破坏了预训练模型的 global flow structure
- 训练 loss 低（0.0187）但推理失败：forward() 看到 GT action 附近的 x_t，sample_actions() 从纯噪声开始

### 次要因素（已排除）
- ✅ env 截断问题已修复（max_episode_steps 显式传入）
- ✅ obs/action 格式正确
- ✅ checkpoint 加载正确
- ✅ LoRA 权重确实被应用

## 5. 推荐方向

1. **降低 LoRA scaling**: alpha=16 的 baseline_v6 也是 0%，说明问题不止 alpha/rank ratio
2. **换训练方式**: flow matching 对 LoRA 敏感，考虑：
   - Full fine-tuning（至少 action expert 部分）
   - 使用 generation-aware training（训练时也跑 ODE）
   - 使用更少的 ODE steps（num_steps=5-10）减轻 collapse
3. **换 baseline**: 用 ACT 作为 aloha_sim_insertion 的 baseline，SmolVLA finetune 在此任务上是 known hard problem
4. **换任务**: 如果必须用 SmolVLA，考虑 LIBERO benchmark（官方已验证 87% success）
