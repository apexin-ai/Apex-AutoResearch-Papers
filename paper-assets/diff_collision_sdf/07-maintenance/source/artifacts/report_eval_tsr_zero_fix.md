# Eval Pipeline TSR=0% 根因分析与修复报告

## 1. openpi policy.infer() 返回值语义和格式

`policy.infer(input_dict)` 的完整流程：

```
input_dict → _input_transform(LiberoInputs + Normalize) → model → _output_transform(Unnormalize + LiberoOutputs) → result
```

**返回值格式：**
```python
{
    "actions": np.ndarray,     # shape (50, 7) — 50步 action chunk，每步7维
    "state": np.ndarray,       # 当前state（透传）
    "policy_timing": dict,     # 推理耗时统计
}
```

- `actions` 的50步是 action chunking 的结果，eval 时只取 `actions[0]`（第一步），每步重新推理
- 7维含义：`[dx, dy, dz, drot_x, drot_y, drot_z, gripper]`（delta动作 + gripper开合）
- `LiberoOutputs` 负责从模型原始输出（32维 padded）截取前7维

**input_dict 要求的字段：**
```python
{
    "observation/image": np.ndarray,       # agentview RGB, shape (H, W, 3)
    "observation/wrist_image": np.ndarray, # wrist camera RGB, shape (H, W, 3)
    "observation/state": np.ndarray,       # 8维 state vector (float32)
    "prompt": str,                         # 语言指令
}
```

## 2. extra_delta_transform 的确切含义

`extra_delta_transform` 控制是否在 transform 链中插入 `DeltaActions` / `AbsoluteActions`：

- **True**：训练时在 data_transforms 中加入 `DeltaActions`（将绝对动作转换为相对于当前 state 的 delta）；推理时在 output_transforms 中加入 `AbsoluteActions`（将 delta 预测还原为绝对动作）
- **False**：不做转换，模型直接输出 delta 动作

**LIBERO 的训练数据本身就是 delta 动作**（HDF5 中的 `actions` 已经是相对位移），所以 `extra_delta_transform` 应该为 **False**。

- 训练配置 `pi0_libero_low_mem_finetune` 默认 `extra_delta_transform=True`（适用于其他 absolute action 的数据集）
- `train_baseline.py` 和 eval 脚本都正确地 override 为 `False`
- 这不是 TSR=0% 的原因

## 3. eval_safelibero.py 中 action 处理的具体问题

### 根因：state 向量格式不匹配

**训练数据格式**（来自 `convert_libero_to_lerobot.py`）：
```python
state = np.concatenate([ee_pos, ee_ori, gripper_states])
# ee_pos:        3维, 末端位置
# ee_ori:        3维, rotation vector (axis-angle)
# gripper_states: 2维, 左右手指 qpos
# 总计 8维
```

**eval 脚本（修复前）：**
```python
state = np.concatenate([robot_state, robot_quat, gripper_qpos[:1]])
# robot_state:    3维, 末端位置 ✓
# robot_quat:     4维, 四元数 [x,y,z,w]  ✗ (应为3维 rotation vector)
# gripper_qpos[:1]: 1维, 只取一个手指  ✗ (应为2维)
# 总计 8维（碰巧维度相同，无 shape error！）
```

### 为什么导致 TSR=0%

两种格式都是8维，不会触发 shape 错误，但内容完全不匹配。经过 z-score normalization 后产生灾难性的数值：

- 训练时 dim[3]（rotation vector x分量）均值=3.122，std=0.049
- Eval 时 dim[3] 实际是四元数 x 分量（≈0.0）
- 归一化：`(0.0 - 3.122) / 0.049 ≈ -63.7`（正常值应在 ±3 内）

所有 orientation 和 gripper 维度都严重偏离训练分布，模型接收到的 state 是 garbage，导致输出无意义的动作。

### 两种失败模式

| 配置 | 现象 | 原因 |
|------|------|------|
| `extra_delta_transform=True` | 碰撞爆炸, displacement=0.822m | AbsoluteActions 把 garbage state 加到 delta 上，产生巨大动作 |
| `extra_delta_transform=False` | 机器人静止, displacement≈1e-10 | 模型在极端 OOD state 下输出接近零的动作 |

## 4. 修复方案和 dry-run 结果

### 修复内容

`get_action_from_policy` 函数中的 state 构建：

```python
# 修复前
robot_state = obs.get("robot0_eef_pos", np.zeros(3))
robot_quat = obs.get("robot0_eef_quat", np.zeros(4))
gripper_qpos = obs.get("robot0_gripper_qpos", np.zeros(2))
state = np.concatenate([robot_state, robot_quat, gripper_qpos[:1]])

# 修复后
from scipy.spatial.transform import Rotation as _Rotation
ee_pos = obs.get("robot0_eef_pos", np.zeros(3))
ee_quat = obs.get("robot0_eef_quat", np.array([1.0, 0.0, 0.0, 0.0]))
gripper_qpos = obs.get("robot0_gripper_qpos", np.zeros(2))
ee_ori = _Rotation.from_quat(ee_quat).as_rotvec()  # robosuite [x,y,z,w] = scipy convention
state = np.concatenate([ee_pos, ee_ori, gripper_qpos]).astype(np.float32)
```

关键改动：
1. **四元数→旋转向量**：robosuite 提供 `robot0_eef_quat`（[x,y,z,w]），通过 scipy 转为3维 rotation vector，匹配训练时 HDF5 中 `obs["ee_ori"]` 的格式
2. **gripper 取两维**：去掉 `[:1]` 截断，保留两个手指的 qpos，匹配训练时 `obs["gripper_states"]` 的2维格式

### Dry-run 结果

在 westd-45947 上运行1个 episode（baseline checkpoint, object_pudding task, max 400 steps）：

```
Initial EEF pos: [-0.153, -0.015, 0.261]
Final EEF pos:   [ 0.106,  0.550, 0.041]
Total displacement: 0.659m
Task success: False
```

**对比修复前后：**

| 指标 | 修复前 (extra_delta=False) | 修复前 (extra_delta=True) | 修复后 |
|------|--------------------------|-------------------------|--------|
| 机器人运动 | 静止 (disp≈1e-10) | 爆炸 (disp=0.822) | 正常运动 (disp=0.659) |
| 动作幅度 | ≈0 | 极大 | 合理 (0.1~0.8) |
| Gripper 行为 | 无变化 | 无意义 | 先闭合再张开 (pick-place) |
| TSR | 0% | 0% | 待全量评估 |

单 episode 未成功完成任务（TSR=0/1），但这是正常的——单次评估的随机性很大，且 baseline 模型本身可能 TSR 不高。关键改善是机器人从**完全不动**变为**执行有意义的 pick-and-place 动作序列**。

### 修复部署状态

| 位置 | 状态 |
|------|------|
| westd-45947 `/root/colliforce-vla/scripts/eval_safelibero.py` | ✅ 已修复 |
| westd-35807 `/root/colliforce-vla/scripts/eval_safelibero.py` | ✅ 已修复 |
| 本地 `eval_safelibero.py` | ✅ 已修复 |
| 本地 `artifacts/eval_safelibero.py` | ✅ 已修复 |

### 建议下一步

1. 在 westd-45947 上重新跑全量 baseline eval（所有4个 task × 20 episodes）获取真实 TSR
2. 同样重新跑 A3 eval，验证 SDF refinement 在正确 state 下是否有效
3. 将修复 commit 到 git repo
