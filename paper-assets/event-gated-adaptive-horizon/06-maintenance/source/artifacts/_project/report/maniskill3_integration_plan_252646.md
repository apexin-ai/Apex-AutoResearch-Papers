# ManiSkill3 + DreamerV3 集成方案

> 日期: 2026-05-16 | 项目: event-gated-adaptive-horizon | 服务器: bjb1-45299

## 1. ManiSkill3 概述 + 选定任务

### 1.1 ManiSkill3 简介

ManiSkill3 是基于 SAPIEN 物理引擎的 GPU 并行机器人仿真平台，提供标准 Gymnasium 接口。支持 state/rgbd/pointcloud 三种观测模式，GPU 并行可达 30,000+ FPS。

- PyPI 包名: `mani-skill`
- 依赖: SAPIEN 3.x + Vulkan (渲染)
- API: `gymnasium.make("TaskName-v1", obs_mode="state")`

### 1.2 选定任务

| Task | obs_dim (state) | act_dim | reward | 默认 max_steps | temporal abstraction 价值 |
|------|----------------|---------|--------|---------------|--------------------------|
| **PickCube-v1** | 42 | 8 | dense | 50 (用 200) | reach→grasp→lift→place 4阶段，阶段切换点天然适合 event gate 触发 |
| **StackCube-v1** | 48 | 8 | dense | 50 (用 200) | 5阶段 (reach A→grasp→lift→move to B→stack)，transport 阶段可用大 dt，精确对齐需小 dt |
| **PegInsertionSide-v1** | 43 | 8 | dense | 50 (用 200) | 精密插入任务，approach 与 insertion 阶段动力学差异极大，event gate 可学习在接近孔洞时切换到细粒度控制 |

所有任务 action space 均为 `Box(-1, 1, (8,))`：pd_joint_delta_pos 控制 (7 关节 + 1 gripper)。

**选择理由**:
- 任务复杂度适中 (500K steps 内可训练)
- 天然多阶段结构，展示 temporal abstraction 效果
- CoRL robotics 社区标准 benchmark
- 与 DMC locomotion 形成互补 (locomotion + manipulation)

## 2. 服务器环境现状

### 2.1 硬件

| 项目 | 状态 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell (98GB each) |
| Vulkan ICD | ✅ `/usr/share/vulkan/icd.d/nvidia_icd.json` 存在 |
| Python | conda base (`/root/miniconda3`) |
| PyTorch | 2.4.1 |

### 2.2 软件依赖

| 依赖 | 状态 |
|------|------|
| mani-skill | ❌ **未安装** (`import mani_skill` → ModuleNotFoundError) |
| gymnasium | 需确认版本 (ManiSkill3 要求 ==0.29.1) |
| gym (legacy) | 0.22.0 (DreamerV3 wrapper 使用) |
| SAPIEN | 随 mani-skill 自动安装 |

### 2.3 代码集成现状

| 组件 | 状态 | 位置 |
|------|------|------|
| ManiSkill wrapper | ✅ 已完成 | `envs/maniskill.py` |
| dreamer.py make_env | ✅ 已集成 | `dreamer.py` L198 `elif suite == "maniskill":` |
| configs.yaml preset | ✅ 已有 `maniskill_state` | `configs.yaml` (仅 PickCube-v1) |
| CUDA_VISIBLE_DEVICES workaround | ✅ 已实现 | `envs/maniskill.py` (`os.environ.pop`) |
| mani-skill 安装 | ❌ 未安装 | — |
| StackCube/PegInsertion 配置 | ❌ 缺失 | — |
| Event-gate + ManiSkill 实验 | ❌ 未开始 | — |

## 3. DreamerV3 代码适配清单

### 3.1 已完成的适配 (无需修改)

**`envs/maniskill.py`** — 完整的 DreamerV3 兼容 wrapper:
- `_flatten_obs()`: 将 ManiSkill3 torch.Tensor/dict obs 转为 flat numpy vector
- `_build_obs()`: 输出包含 `is_first`, `is_terminal`, `state` (和可选 `image`) 的 dict
- `step()` / `reset()`: 兼容 DreamerV3 的 `(obs, reward, done, info)` 接口
- `action_repeat` 支持
- `observation_space` / `action_space`: 返回 `gym.spaces` (非 gymnasium.spaces)
- CUDA_VISIBLE_DEVICES 自动移除 + 设备翻译

**`dreamer.py`** L198-207 — `make_env` 中的 maniskill 分支:
```python
elif suite == "maniskill":
    import envs.maniskill as maniskill
    env = maniskill.ManiSkill(
        task, config.action_repeat, config.size,
        obs_mode="state", max_episode_steps=config.time_limit,
        seed=config.seed + id,
    )
    env = wrappers.NormalizeActions(env)
```

Wrapper 链: `ManiSkill → NormalizeActions → TimeLimit → SelectAction → UUID` — 已验证兼容。

**`models.py`** — EventGate + WorldModel:
- `EventGate` (`networks.py:336`): Gumbel-softmax 选择 dt ∈ {1,...,max_dt}，支持 curriculum annealing
- `RSSM` (`networks.py:17`): 支持 `max_dt` 和 `dt_embed_dim` 参数
- Event gate 机制与环境无关，对 ManiSkill 自动生效

### 3.2 需要新增的适配

#### 3.2.1 `configs.yaml` — 添加多任务配置

```yaml
# StackCube state-based
maniskill_stackcube:
  task: maniskill_StackCube-v1
  steps: 5e5
  action_repeat: 1
  envs: 1
  train_ratio: 512
  time_limit: 200
  video_pred_log: false
  encoder: {mlp_keys: '.*', cnn_keys: '$^'}
  decoder: {mlp_keys: '.*', cnn_keys: '$^'}

# PegInsertionSide state-based
maniskill_peg:
  task: maniskill_PegInsertionSide-v1
  steps: 5e5
  action_repeat: 1
  envs: 1
  train_ratio: 512
  time_limit: 200
  video_pred_log: false
  encoder: {mlp_keys: '.*', cnn_keys: '$^'}
  decoder: {mlp_keys: '.*', cnn_keys: '$^'}
```

**文件**: `configs.yaml` — 在 `maniskill_state` section 后追加。

#### 3.2.2 启动命令模板

```bash
# 进入环境
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/event-gated-adaptive-horizon

# Baseline (无 event gate)
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
  python dreamer.py --configs maniskill_state \
  --task maniskill_PickCube-v1 \
  --logdir ./logdir/maniskill_pickcube_baseline_s1

# Event-gated
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
  python dreamer.py --configs maniskill_state \
  --task maniskill_PickCube-v1 \
  --gate_enabled true --gate_max_dt 8 \
  --logdir ./logdir/maniskill_pickcube_gated_s1
```

**注意**: 不要设置 `CUDA_VISIBLE_DEVICES`，SAPIEN 会 segfault。

### 3.3 无需修改的理由

| 潜在顾虑 | 判断 |
|----------|------|
| Reward scale | ManiSkill3 dense reward ∈ [0, ~5]，DreamerV3 使用 symlog_disc reward head，自动适配 |
| Action space | ManiSkill3 action 已是 [-1,1]^8，`NormalizeActions` wrapper 正确处理 |
| Episode length | `time_limit: 200` 通过 `TimeLimit` wrapper 控制，默认 50 太短 |
| State obs 维度 | 42-48 维，`mlp_keys: '.*'` 匹配 `state` key，encoder/decoder MLP 自动适配 |
| Event gate 兼容性 | Gate 作用于 RSSM latent space，与 obs 来源无关 |

## 4. 安装步骤

### 4.1 安装 ManiSkill3

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo  # AutoDL 代理加速

# 安装 ManiSkill3 (自动安装 SAPIEN + gymnasium)
pip install mani-skill

# 验证
python -c "import mani_skill; print(mani_skill.__version__)"
python -c "
import gymnasium
import mani_skill.envs
env = gymnasium.make('PickCube-v1', obs_mode='state', render_backend='cpu')
obs, _ = env.reset()
print(f'obs shape: {obs.shape}, action space: {env.action_space}')
env.close()
print('ManiSkill3 验证通过')
"
```

### 4.2 Gymnasium 版本冲突风险

ManiSkill3 依赖 `gymnasium==0.29.1`。当前 DreamerV3 用 `gym==0.22.0`。两者共存无问题 (gymnasium 和 gym 是不同包)，wrapper 内部使用 gymnasium 创建 env，外部暴露 gym.spaces 给 DreamerV3。

### 4.3 完整 make_env 测试

```bash
cd /root/autodl-tmp/event-gated-adaptive-horizon
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl \
  python -c "
import sys; sys.path.insert(0, '.')
import envs.maniskill as ms
env = ms.ManiSkill('PickCube-v1', action_repeat=1, obs_mode='state', max_episode_steps=200)
obs = env.reset()
print('obs keys:', list(obs.keys()))
print('state shape:', obs['state'].shape)
print('action space:', env.action_space)
obs, r, d, info = env.step(env.action_space.sample())
print(f'step OK, reward={r:.4f}, done={d}')
env.close()
print('Full pipeline test passed')
"
```

## 5. 实验设计建议

### 5.1 实验矩阵

| 实验 ID | Task | Gate | Config | Seeds | 目标 |
|---------|------|------|--------|-------|------|
| MS-001a | PickCube-v1 | off (baseline) | maniskill_state | 0,1,2 | Baseline 学习曲线 |
| MS-001b | PickCube-v1 | on (gate_max_dt=8) | maniskill_state + gate | 0,1,2 | Event-gate 效果 |
| MS-001c | PickCube-v1 | fixed dt=2 | maniskill_state + fixed | 0,1,2 | Fixed frame-skip 对照 |
| MS-002a | StackCube-v1 | off | maniskill_stackcube | 0,1,2 | |
| MS-002b | StackCube-v1 | on | maniskill_stackcube + gate | 0,1,2 | |
| MS-003a | PegInsertionSide-v1 | off | maniskill_peg | 0,1,2 | |
| MS-003b | PegInsertionSide-v1 | on | maniskill_peg + gate | 0,1,2 | |

### 5.2 Event-Gate 配置

ManiSkill manipulation 任务与 DMC locomotion 的关键差异：
- **阶段性更强**: approach/grasp/transport/place 各阶段动力学截然不同
- **接触事件**: 抓取/碰撞瞬间是天然的 event boundary
- **精度需求变化大**: 粗略移动 vs 精确插入

推荐 gate 参数 (可基于 PickCube-v1 初步调参后统一)：

```yaml
gate_enabled: true
gate_max_dt: 8          # manipulation 阶段差异大，8 级够用
gate_tau_init: 5.0
gate_tau_final: 0.5
gate_tau_anneal_steps: 100000  # 500K steps / 5 = 100K annealing
gate_loss_weight: 1.0
gate_curriculum_phase1: 25000
gate_curriculum_phase2: 75000
```

### 5.3 指标

| 指标 | 含义 |
|------|------|
| eval/success_rate | 主指标：任务成功率 |
| eval/episode_reward | 累积 reward |
| train/gate_dt_mean | event gate 选择的平均 dt |
| train/gate_entropy | gate 分布熵 (应从高到低收敛) |
| train/model_loss | world model 预测损失 |

### 5.4 预期假设

- **PickCube**: event gate 学习在 grasp 和 lift 阶段切换 dt，baseline 对比预期 10-20% success rate 提升
- **StackCube**: 多阶段结构更适合 adaptive horizon，效果差距应更显著
- **PegInsertionSide**: 精密操作阶段需要小 dt，event gate 的自适应选择应优于固定 dt

## 6. 预估工作量和时间线

### 6.1 任务分解

| 步骤 | 工作 | 时间 |
|------|------|------|
| 1. 安装 | `pip install mani-skill` + 验证 | 15 min |
| 2. 配置 | 添加 StackCube/PegInsertion configs | 10 min |
| 3. Baseline 验证 | PickCube-v1 baseline 单 seed 跑通 | ~2 hr (500K steps) |
| 4. 全矩阵实验 | 3 tasks × 3 configs × 3 seeds = 27 runs | 3-5 天 (可并行) |
| 5. 分析 | 收集指标、画图、写 analysis | 0.5 天 |

### 6.2 训练时间估算

单 GPU state-based 训练 (envs=1, 500K steps):
- DMC walker_walk 参考: ~45 min/500K steps
- ManiSkill state-based 预计类似 (state obs, 无渲染开销)
- 估算: **1-2 hr/run** (保守，含 SAPIEN 初始化和可能的 overhead)

2 GPU 并行: 可同时跑 2 个实验 (一个 GPU 一个)，但注意 SAPIEN 的 CUDA_VISIBLE_DEVICES 限制。

### 6.3 风险

| 风险 | 概率 | 缓解 |
|------|------|------|
| gymnasium/gym 版本冲突 | 低 | 两个包共存，wrapper 隔离 |
| SAPIEN GPU 内存占用过大 | 低 | state-based 仅 ~118 MiB |
| ManiSkill3 reward 太 dense 导致 gate 退化为 dt=1 | 中 | 可调 reward scale 或 gate_loss_weight |
| training 不收敛 | 中 | 先验证 baseline，确认 DreamerV3 在 ManiSkill 上能学习 |

## 附录: 关键文件索引

| 文件 | 作用 |
|------|------|
| `envs/maniskill.py` | ManiSkill3 → DreamerV3 wrapper |
| `dreamer.py` L198 | `make_env` maniskill 分支 |
| `configs.yaml` `maniskill_state` | PickCube 默认配置 |
| `networks.py:336` EventGate | event gate (Gumbel-softmax) |
| `networks.py:17` RSSM | 世界模型 (支持 dt embedding) |
| `models.py` WorldModel | 集成 EventGate + variable-dt |
