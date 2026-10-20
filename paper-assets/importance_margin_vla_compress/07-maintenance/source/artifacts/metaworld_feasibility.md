# MetaWorld Benchmark 可行性报告

**日期**: 2026-05-24

## 1. MetaWorld 概述

MetaWorld 是 Farama Foundation 维护的机器人操作 benchmark，基于 MuJoCo 仿真，包含 50 个 Sawyer 机械臂桌面操作任务。

| 属性 | 值 |
|------|-----|
| 版本 | 3.0.0 (2025-06-14) |
| Python | >= 3.10 |
| 任务数 | 50 |
| 机器人 | Sawyer arm |
| 动作空间 | Box(-1, 1, (4,)) — dx, dy, dz, gripper |
| 观测 | 480x480 RGB (corner2 camera) + 4D state (EEF pos + gripper) |
| Metrics | Success rate (info["success"]) |
| 每 episode 最大步数 | 500 |

### 难度分组
- **Easy** (28 tasks): button-press, door-open, drawer, faucet, handle, window 等
- **Medium** (11 tasks): basketball, bin-picking, box-close, hammer, soccer 等
- **Hard** (6 tasks): assembly, pick-place, push, pick-out-of-hole 等
- **Very Hard** (5 tasks): shelf-place, disassemble, stick-pull/push, pick-place-wall

### 与 LIBERO 对比

| 维度 | LIBERO | MetaWorld |
|------|--------|-----------|
| 仿真器 | MuJoCo (robosuite) | MuJoCo |
| 机器人 | Franka Panda | Sawyer |
| 摄像头 | 2 (agentview + wrist) | 1 (corner2) |
| 动作维度 | 7D (6D EEF + gripper) | 4D (3D EEF delta + gripper) |
| 状态维度 | 8D (pos + axis-angle + gripper_qpos) | 4D (EEF pos + gripper) |
| 图像分辨率 | 256x256 | 480x480 |
| 任务数 | 10-90 per suite | 50 |
| 语言指令 | 长指令 (task-specific) | 短描述 (task-level) |
| 评估标准 | done flag | info["success"] |

## 2. 安装状态

已安装在 **westd-27271** 服务器：
- MetaWorld 3.0.0, Python 3.12.3 (conda base), MuJoCo 3.8.1
- EGL rendering 正常
- LeRobot MetaWorld 集成可用 (`lerobot/envs/metaworld.py`)

验证结果：
```
Obs pixels: (480, 480, 3), dtype=uint8
Obs state: (4,), values=[0.005, 0.601, 0.195, 1.0]
Action space: Box(-1.0, 1.0, (4,), float32)
```

## 3. VLA 在 MetaWorld 上的已有结果

### OpenVLA
OpenVLA 论文没有 MetaWorld 实验。只用了 LIBERO (仿真) 和 real-world (WidowX, Google Robot)。

### SmolVLA (论文结果)
SmolVLA 论文 (HuggingFace, 2025) 在 MetaWorld MT50 上的结果：

| Model | Easy | Medium | Hard | Very Hard | Average |
|-------|------|--------|------|-----------|---------|
| SmolVLA 0.45B | 82.5% | 41.8% | 45.0% | 60.0% | 57.3% |
| SmolVLA 2.25B | 87.1% | 51.8% | 70.0% | 64.0% | 68.2% |

- 训练：100k steps, batch 64, 只训练 action expert, VLM frozen
- 数据：`lerobot/metaworld_mt50` (2500 episodes, 50 per task)
- 评估：10 trials per task

### π0.5
π0.5 没有公开的 MetaWorld 实验或 checkpoint。需要自行 fine-tune。

### Token Pruning on MetaWorld
无已有工作。Compressor-VLA 用 LIBERO，EfficientVLA 用 SIMPLER，GridS 用 LIBERO。MetaWorld 上的 token pruning 实验将是新颖贡献。

## 4. 可用 Checkpoint

| Checkpoint | 来源 | 验证状态 |
|-----------|------|---------|
| `jadechoghari/smolvla_metaworld` | 社区 (HuggingFace) | 未验证 |
| `lerobot/smolvla_base` | 官方 base | 需 fine-tune |
| 自行训练 | `lerobot/metaworld_mt50` | 需 ~100k steps |

推荐：先用 `jadechoghari/smolvla_metaworld` 验证，不行再自训。

## 5. Pruning 适配方案

### 已完成
- `eval_smolvla_pruning_metaworld.py` (490 行，已验证 env 部分)
  - 支持 baseline / l2norm_prune / random_prune / attention_prune
  - 支持按难度组或具体 task 名选择
  - 复用 LIBERO 版本的 pruning hooks (connector forward hook)
  - 适配 MetaWorld obs 格式 (单摄像头 + 4D state)

### 代码改动点 (vs LIBERO 版本)
1. **环境创建**: `metaworld.MT1` 替代 `LiberoEnv`
2. **Obs 转换**: 单摄像头 pixels + raw_obs[:4] 替代双摄像头 + 8D state
3. **动作维度**: 4D 替代 7D
4. **任务迭代**: difficulty group 解析替代 LIBERO suite
5. **成功判定**: `info["success"]` 替代 `done` flag

### 无需修改的部分
- Pruning hooks (connector 层面，与 env 无关)
- predict_actions 接口
- Wilson CI 统计

## 6. 建议实验方案

### Phase 1: Baseline 验证 (预计 1-2h GPU)
```bash
python eval_smolvla_pruning_metaworld.py \
    --pretrained_dir /path/to/smolvla_metaworld \
    --task reach-v3,push-v3,pick-place-v3 \
    --mode baseline --num_episodes 10
```

### Phase 2: Pruning Sweep (预计 6-8h GPU)
```bash
TASKS="reach-v3,button-press-v3,drawer-open-v3,push-v3,pick-place-v3,assembly-v3,coffee-pull-v3,hammer-v3,shelf-place-v3,window-open-v3"
for k in 0.9 0.7 0.5 0.3; do
    python eval_smolvla_pruning_metaworld.py \
        --pretrained_dir /path/to/ckpt \
        --task $TASKS --mode l2norm_prune --k_ratio $k --num_episodes 10
done
```

### Phase 3: 全量对比 (预计 12-16h GPU)
- 50 tasks x 10 episodes x {baseline, k=0.7, k=0.5, k=0.3}

### 建议 Tasks (10 个, 覆盖所有难度)

| Task | 难度 | 描述 |
|------|------|------|
| reach-v3 | Easy | 到达目标位置 |
| button-press-v3 | Easy | 按按钮 |
| drawer-open-v3 | Easy | 开抽屉 |
| window-open-v3 | Easy | 开窗户 |
| coffee-pull-v3 | Medium | 从咖啡机拉杯子 |
| hammer-v3 | Medium | 锤钉子 |
| push-v3 | Hard | 推物体到目标 |
| pick-place-v3 | Hard | 抓取放置 |
| assembly-v3 | Hard | 组装螺母到螺栓 |
| shelf-place-v3 | Very Hard | 放置到架子上 |

### 预计 GPU 时间
- 每 task x 10 episodes: ~5-8 min (SmolVLA 0.45B)
- 10 tasks x 4 k_ratios: ~4-6h
- 50 tasks x 4 k_ratios: ~20-30h

## 7. π0.5 可行性评估

### 可行但需要前置工作
1. **Fine-tune π0.5 on MetaWorld**: 需要数据集适配 + 训练 (100k steps, ~10h GPU)
2. **Obs 格式差异**: π0.5 用 2 cameras (LIBERO), MetaWorld 只有 1 camera
3. **Action 维度**: π0.5 LIBERO 用 7D action, MetaWorld 用 4D

### 建议策略
- **短期**: 用 SmolVLA 做 MetaWorld 实验，已有 checkpoint 和集成
- **长期**: 如需 π0.5 结果，需要 ~1 周 (fine-tune + debug)

## 8. 结论

MetaWorld 作为第三个 benchmark **可行且低成本**：
- 环境已搭建，渲染正常
- eval 脚本已写好，pruning hooks 已适配
- SmolVLA 有现成 MetaWorld checkpoint
- 无已有 MetaWorld token pruning 工作 → 新颖性
- π0.5 需额外 fine-tune 工作
- 需下载 `jadechoghari/smolvla_metaworld` checkpoint 验证

**下一步**: 下载 MetaWorld checkpoint → 跑 3 task baseline → 确认 pipeline 端到端通过 → 启动 pruning sweep。
