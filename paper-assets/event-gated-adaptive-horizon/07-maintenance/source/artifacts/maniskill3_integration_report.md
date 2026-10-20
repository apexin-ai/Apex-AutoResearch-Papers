# ManiSkill3 + DreamerV3 集成调研报告

## 1. ManiSkill3 概况

- **版本**: 3.0.1 (PyPI: `mani-skill`)
- **安装**: `pip install mani-skill` (SAPIEN 作为依赖自动安装)
- **底层**: SAPIEN 物理引擎 + Vulkan 渲染
- **API**: 标准 Gymnasium 接口 (`gymnasium.make()`)
- **特色**: GPU 并行仿真 (可达 30,000+ FPS)，支持 state/rgbd/pointcloud 多种 obs 模式

### 安装步骤 (bjb1-45299)

```bash
# 1. 安装 Vulkan 依赖
apt-get install -y libvulkan1 vulkan-tools mesa-vulkan-drivers

# 2. 创建 NVIDIA Vulkan ICD 配置 (服务器上缺失)
cat > /usr/share/vulkan/icd.d/nvidia_icd.json << 'EOF'
{
    "file_format_version": "1.0.0",
    "ICD": {
        "library_path": "libGLX_nvidia.so.0",
        "api_version": "1.3.0"
    }
}
EOF

# 3. 安装 ManiSkill3
pip install mani-skill
```

### 注意事项

- **CUDA_VISIBLE_DEVICES 限制会导致 SAPIEN 崩溃**：ManiSkill3/SAPIEN 内部用 Vulkan 初始化 GPU 设备，如果 CUDA_VISIBLE_DEVICES 过度限制会导致 segfault。state-based 模式不需要 GPU 渲染但 SAPIEN 初始化时仍尝试探测 CUDA。
- **headless 可用**：state-based obs (`render_mode=None`) 在 headless 服务器上正常运行，不需要 X display。
- **visual obs 需要 Vulkan**：rgbd/rgb obs 需要 Vulkan 正确配置。已在 bjb1-45299 上验证 Vulkan 检测到 4 个 GPU。

## 2. Obs / Action Space 详情

### State-based (obs_mode="state")

所有 task action space 均为 `Box(-1, 1, (8,))` (pd_joint_delta_pos 控制模式, 7 关节 + 1 gripper)。

| Task | obs dim | obs 组成 (state_dict) | reward 类型 | info keys |
|------|---------|----------------------|------------|-----------|
| PickCube-v1 | 42 | qpos(9) + qvel(9) + is_grasped(1) + tcp_pose(7) + goal_pos(3) + obj_pose(7) + tcp_to_obj_pos(3) + obj_to_goal_pos(3) | dense | success, is_obj_placed, is_robot_static, is_grasped |
| StackCube-v1 | 48 | qpos(9) + qvel(9) + tcp_pose(7) + cubeA_pose(7) + cubeB_pose(7) + tcp_to_cubeA_pos(3) + tcp_to_cubeB_pos(3) + cubeA_to_cubeB_pos(3) | dense | is_cubeA_grasped, is_cubeA_on_cubeB, is_cubeA_static, success |
| PegInsertionSide-v1 | 43 | qpos(9) + qvel(9) + tcp_pose(7) + peg/hole poses + relative positions | dense | success, peg_head_pos_at_hole |
| PushCube-v1 | 35 | qpos(9) + qvel(9) + task-specific states | dense | success |
| LiftPegUpright-v1 | 32 | qpos(9) + qvel(9) + task-specific states | dense | success |

### RGBD (obs_mode="rgbd")

PickCube-v1 示例:
```
agent:
  qpos: (9,)
  qvel: (9,)
extra:
  is_grasped: (1,)
  tcp_pose: (7,)
  goal_pos: (3,)
sensor_data:
  base_camera:
    rgb: (128, 128, 3)  # uint8
    depth: (128, 128, 1) # float32
```

### State-based vs Visual 切换

```python
# State-based (快速验证用)
env = gymnasium.make("PickCube-v1", obs_mode="state")

# Visual (需要 Vulkan)
env = gymnasium.make("PickCube-v1", obs_mode="rgbd", render_mode="rgb_array")
```

## 3. 已有 DreamerV3 + ManiSkill 集成情况

- **没有找到现成的 DreamerV3 + ManiSkill3 集成代码/教程/repo**
- 存在一个 [Gymnasium envs with DreamerV3 的 gist](https://gist.github.com/qxcv/e8641342c102c2aa714c9caeca724101)，但是是 Minigrid 示例，不涉及 ManiSkill
- [tongzhoumu/ManiSkill_Baselines](https://github.com/tongzhoumu/ManiSkill_Baselines) 提供了 PPO/SAC 等 baseline，但无 DreamerV3
- ManiSkill3 官方文档列出了 PPO (StableBaselines3/CleanRL) 的设置指南

## 4. Rendering 要求和限制

| 需求 | 状态 (bjb1-45299) |
|------|-------------------|
| Vulkan ICD | 手动创建了 nvidia_icd.json |
| libvulkan1 | 已安装 |
| EGL (10_nvidia.json) | 已存在 |
| NVIDIA Driver | 595.58.03 (支持 Vulkan 1.4.329) |
| GPU | 4x NVIDIA RTX PRO 6000 Blackwell (98GB each) |
| Headless state-based | 可用 |
| Headless visual | 需要验证 (需避开 CUDA_VISIBLE_DEVICES 问题) |

## 5. 推荐 Tasks 及理由

### Task 1: PickCube-v1

| 属性 | 值 |
|------|-----|
| obs dim (state) | 42 |
| action dim | 8 |
| reward | dense (距离+抓取+放置 shaping) |
| 默认 episode length | 50 steps (可配置) |
| **选择理由** | 最经典的 manipulation benchmark，涉及 reach → grasp → lift → place 4 个阶段，天然适合时间抽象研究。event gate 可以学习在阶段转换时触发（如接触物体、开始抬升），不同阶段的最优 dt 不同（approach 需要精细控制 → dt 小，lift 阶段可以粗粒度 → dt 大）。 |

### Task 2: StackCube-v1

| 属性 | 值 |
|------|-----|
| obs dim (state) | 48 |
| action dim | 8 |
| reward | dense (多阶段 shaping) |
| 默认 episode length | 50 steps (可配置) |
| **选择理由** | 在 PickCube 基础上增加了放置精度要求（stack A on B），阶段更多：reach A → grasp A → lift A → move to B → place A on B。时间层级结构更丰富，对 adaptive horizon 的需求更强：transport 阶段动作模式固定可用大 dt，精确对齐阶段需要小 dt。同时 StackCube 有更长的 horizon 和更稀疏的最终成功信号，对 world model 的长期预测能力是更好的测试。 |

## 6. Wrapper 代码

已实现 `envs/maniskill.py`，完成与 DreamerV3 env 接口的适配：
- 将 ManiSkill3 torch.Tensor obs 转为 numpy (去除 batch dim)
- 输出 `is_first`, `is_terminal` 标记
- 支持 action_repeat
- 兼容现有 wrappers (NormalizeActions, TimeLimit, SelectAction, UUID)
- **集成测试已通过**

### dreamer.py 集成 diff (待应用)

```python
# 在 make_env 函数中添加:
elif suite == "maniskill":
    import envs.maniskill as maniskill
    env = maniskill.ManiSkill(
        task, config.action_repeat, config.size,
        obs_mode="state", max_episode_steps=config.time_limit,
        seed=config.seed + id,
    )
    env = wrappers.NormalizeActions(env)
```

### configs.yaml 新增配置

```yaml
maniskill_state:
  task: maniskill_PickCube-v1
  steps: 5e5
  action_repeat: 1
  envs: 1
  train_ratio: 512
  time_limit: 200
  video_pred_log: false
  encoder: {mlp_keys: '.*', cnn_keys: '$^'}
  decoder: {mlp_keys: '.*', cnn_keys: '$^'}
```

## 7. 后续步骤

1. 将 `envs/maniskill.py` 和 dreamer.py 修改合入代码
2. 添加 maniskill_state 配置到 configs.yaml
3. 先跑 PickCube-v1 baseline (无 event gate) 验证学习曲线
4. 再开启 event gate 对比
5. 如需 visual obs，验证 Vulkan headless rendering 在不限制 CUDA_VISIBLE_DEVICES 时的稳定性
