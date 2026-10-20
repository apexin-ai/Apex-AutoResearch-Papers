# Action Prediction Probe 设计

## HDF5 数据格式

### 原始 LIBERO 数据 (`/root/autodl-tmp/vla-ssd/data/libero/libero_10/{TASK}_demo.hdf5`)

```
data/demo_X/actions:      (T, 7) float64   — 连续 action
data/demo_X/obs/ee_pos:   (T, 3) float64   — end-effector position
data/demo_X/obs/ee_ori:   (T, 3) float64   — end-effector orientation
data/demo_X/obs/gripper_states: (T, 2) float64
```

**Action 7-dim 含义**：

| Dim | 含义 | 典型范围 | Std |
|-----|------|---------|-----|
| 0-2 | EE position delta (x,y,z) | [-0.94, 0.94] | 0.26-0.43 |
| 3-5 | EE orientation delta (roll,pitch,yaw) | [-0.34, 0.38] | 0.03-0.10 |
| 6   | Gripper command | {-1, 1} | binary: -1=close, 1=open |

- 50 demos/task, ~220-290 steps/demo, ~13k total steps/task
- 10 tasks × 50 demos = 500 trajectories total

### Feature HDF5

| Source | Path | Key | Shape | Layers | Dim |
|--------|------|-----|-------|--------|-----|
| VLA trained | `features/trained/{TASK}.h5` | `demo_X/last_preaction` | (T, 33, 4096) | 33 | 4096 |
| VLA untrained | `features/untrained/{TASK}.h5` | `demo_X/last_preaction` | (T, 33, 4096) | 33 | 4096 |
| DINO-V2 | `features/dinov2/{TASK}.h5` | `traj_X/cls_token` | (T, 1024) | 1 | 1024 |

### Feature-Action 对齐

- **T 完全一致**：feature h5 的 T == LIBERO action 的 T（已验证 demo_0/1/5/49）
- **文件名映射**：feature `{TASK}.h5` → LIBERO `{TASK}_demo.hdf5`
- **Demo key 映射**：VLA 用 `demo_X`，DINO 用 `traj_X`，index 对应 LIBERO 的 `demo_X`

## Probe 架构

### 目标任务

给定 timestep t 的 hidden state h_t，预测 **next action** a_{t+1}。

为什么选 a_{t+1} 而非 a_t：
- a_t 是当前帧正在执行的动作，与当前视觉状态高度相关（手臂正在往某个方向移动，视觉上能看出来）
- a_{t+1} 需要"理解接下来该做什么"——更需要 task goal + progress 的知识
- 每条 trajectory 产出 T-1 个样本（丢弃最后一帧的 h_T）

### 模型

```python
class ActionMLPProbe(nn.Module):
    def __init__(self, in_dim, out_dim=7, hidden_dim=256):
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim),
        )
    def forward(self, x):
        return self.net(x)  # (N, 7)
```

与现有 MLPProbe 一致的 2-layer 架构，唯一区别：output_dim=7 而非 squeeze to scalar。

### Action 标准化

Position dims (0-2) std ~0.3 vs orientation dims (3-5) std ~0.05，差 6 倍。如果直接 MSE，loss 被 position 主导。

策略：**per-dim standardization on training set**。
- 训练前计算 train set 所有 action 的 per-dim mean 和 std
- z-score normalize：z = (a - mean) / (std + 1e-8)
- 模型预测 z，evaluation 时 denormalize 回原始空间再算 R²
- Gripper dim (6) 也做 standardization（虽然是 binary，但 z-score 不会破坏信息）

### Loss

MSE on standardized 7-dim action vector：

```
loss = MSE(pred_z, target_z)  # shape (N, 7) → scalar
```

### Evaluation Metrics

1. **Per-dim R²**：对每个 action dimension 单独计算 R²，展示哪些维度更容易预测
2. **Overall R²**：7-dim flatten 后计算
3. **Per-task mean R²**：按 task 分组计算 R²，取均值（与 temporal distance 的 per_task_mean_rho 对应）
4. **Gripper accuracy**：dim 6 的预测 threshold 0 后计算 binary accuracy
5. **MSE (raw)**：denormalize 后的原始空间 MSE

核心对比指标：**per-task mean R² 的 Δ(trained VLA − untrained VLA)**

## 实验矩阵

| Model | Layers | Hidden Dim | 预期 action R² |
|-------|--------|------------|---------------|
| Trained VLA | 33 (sweep all) | 4096 | 高（训练目标直接相关） |
| Untrained VLA | 33 (sweep all) | 4096 | 低（随机权重无策略知识） |
| DINO-V2 | 1 | 1024 | 低-中（有视觉信息但无策略） |

### 预期结果

- **如果 VLA 训练教会了策略知识**：trained VLA 的 R² 应显著高于 untrained VLA 和 DINO-V2
- **与 temporal distance 对比**：temporal distance 被 vision encoder 主导（DINO 也能做），但 action prediction 应该不会——纯视觉无法推断出要往哪个方向移动多远
- **Layer-wise pattern**：action 信息预计集中在 LLM 深层（靠近 action token 输出层），而非浅层视觉编码层

### 关键假设检验

若 DINO-V2 也能不错地预测 action → 说明 action 与视觉状态高度相关（例如手臂位置基本决定下一步动作的方向），此时需进一步分析：
- 哪些 action dims DINO 也能预测（可能是 gripper status，视觉可判断）
- 哪些 dims 只有 trained VLA 才行（可能是精确的 position/orientation deltas）

## 代码改动估算

### 新增 (~150-200 行)

1. **`ActionMLPProbe` class** (~10 行)：7-dim output 的 MLP
2. **`load_actions()` function** (~30 行)：
   - 根据 traj_metas 的 task name 映射到 LIBERO hdf5 路径
   - 处理 DINO `traj_X` → LIBERO `demo_X` 的 key 映射
   - 返回 per-trajectory action arrays
3. **`run_action_prediction()` runner** (~80 行)：
   - Load features + actions
   - Build shifted pairs (h_t → a_{t+1})，每条 traj 产出 T-1 样本
   - Per-dim standardization
   - Per-layer loop：train + eval
   - 计算 per-dim R²、per-task R²、gripper accuracy
4. **`train_multi_output_regression_probe()`** (~30 行)：
   - MSE on (N, 7) output
   - Early stopping（复用现有 pattern）
   - 返回 per-dim R² + overall R² + gripper acc

### 修改现有代码 (~20 行)

1. `parse_args()`：
   - `choices` 加 `"action_prediction"`
   - 加 `--data_dir` 参数（LIBERO 数据路径）
2. `main()`：
   - `runners` dict 加 `action_prediction=run_action_prediction`
3. `save_results()`：
   - 加 `action_prediction` 的 fields（per_dim_r2, overall_r2, gripper_acc 等）

### 可完全复用

- `scan_features()` / `split_by_task()` / `load_layer_features()` / `parse_layers()` — 不改动
- 训练循环的 early stopping + best_state 保存 pattern
- Results I/O 框架（per-layer JSON + summary CSV）

### 运行命令

```bash
# Trained VLA
python train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained/ \
  --probe_type action_prediction \
  --aggregation last_preaction

# Untrained VLA
python train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ \
  --probe_type action_prediction \
  --aggregation last_preaction

# DINO-V2
python train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/dinov2/ \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/dinov2/ \
  --probe_type action_prediction \
  --aggregation last_preaction
```

预估每个 model 全层 sweep 运行时间：~5-10 分钟（VLA 33 层，每层 ~50 epoch MLP 训练）。
