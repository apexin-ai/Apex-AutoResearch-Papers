# MVP-1 Baseline Eval 方案

## 评测目标
建立 SmolVLA 预训练模型在 LIBERO 标称 + LIBERO-Plus 4 维视觉扰动下的 baseline 成绩。

## 评测矩阵

### 标称评测（LIBERO standard）

| Suite | 任务数 | Episodes/task | 总 Episodes |
|-------|--------|---------------|-------------|
| libero_spatial | 10 | 50 | 500 |
| libero_object | 10 | 50 | 500 |
| libero_goal | 10 | 50 | 500 |
| libero_10 (Long) | 10 | 50 | 500 |
| **合计** | **40** | | **2,000** |

### 扰动评测（LIBERO-Plus, 4 维纯视觉扰动）

MVP 只评 4 维视觉扰动（排除物体布局 O、语言指令 R、机器人初态）：

| 维度 | 子维度 | 参数范围 | 说明 |
|------|--------|----------|------|
| **Camera (C)** | C1 距离缩放 | 1.01x - 2.00x | 沿光轴缩放 |
| | C2 球坐标位移 | Δθ/Δφ 15-75° | 方位角+仰角 |
| | C3 朝向扰动 | yaw/pitch/roll 2-10° | |
| **Lighting (L)** | L1 漫射颜色 | RGB 通道调整 | |
| | L2 方向 | 平行光方向变化 | |
| | L3 镜面强度 | 反射表面高光 | |
| | L4 阴影 | on/off | |
| **Texture (B)** | B1 场景纹理 | 950 张纹理池 | XML 替换 |
| | B2 表面纹理 | 桌面/地板 | |
| **Noise (N)** | N1 运动模糊 | r=5-35, σ=2-20 | |
| | N2 高斯模糊 | σ=1-10 | |
| | N3 缩放模糊 | [1, 1.11-1.56] | |
| | N4 雾 | α=0.5-5.0, β=1.3-3.0 | |
| | N5 毛玻璃模糊 | σ=0.5-2.5, δ=1-5 | |

共 14 个子维度。LIBERO-Plus 使用 L1-L5 难度分层，MVP 默认跑全部难度。

每个 suite × 扰动维度组合：50 episodes/task × 10 tasks = 500 episodes/suite
4 suites × 4 维度 × 500 = **8,000 episodes**（扰动部分）

**总计：2,000（标称） + 8,000（扰动） = 10,000 episodes**

## GPU 分工

### 方案 A：按标称/扰动分（推荐，简单）
| GPU | 任务 | 预估时间 |
|-----|------|----------|
| cuda:0 | 标称 LIBERO 全 4 suites (2,000 ep) | ~4-6h |
| cuda:1 | LIBERO-Plus 全 4 suites × 4 维扰动 (8,000 ep) | ~16-24h |

**问题**：cuda:1 负载远大于 cuda:0。

### 方案 B：按 suite 分（推荐，负载均衡）
| GPU | 任务 | 预估时间 |
|-----|------|----------|
| cuda:0 | spatial + object：标称 1,000 ep + 扰动 4,000 ep | ~10-14h |
| cuda:1 | goal + long：标称 1,000 ep + 扰动 4,000 ep | ~10-14h |

**推荐方案 B**，两张卡负载均衡。

## 执行命令

### cuda:0（spatial + object）
```bash
# 环境前缀（根据 detect_image 结果调整）
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export MUJOCO_GL=egl && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \

# 标称
CUDA_VISIBLE_DEVICES=0 lerobot-eval \
  --policy.path=lerobot/smolvla_base \
  --env.type=libero \
  --env.task=libero_spatial,libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=50 \
  --env.max_parallel_tasks=1 \
  --output_dir=/root/acib/results/baseline_standard_gpu0 \
  2>&1 | tee /root/acib/logs/baseline_standard_gpu0.log

# 扰动
CUDA_VISIBLE_DEVICES=0 lerobot-eval \
  --policy.path=lerobot/smolvla_base \
  --env.type=libero_plus \
  --env.task=libero_spatial,libero_object \
  --eval.batch_size=1 \
  --eval.n_episodes=50 \
  --env.max_parallel_tasks=1 \
  --output_dir=/root/acib/results/baseline_perturbed_gpu0 \
  2>&1 | tee /root/acib/logs/baseline_perturbed_gpu0.log
```

### cuda:1（goal + long）
```bash
# 标称
CUDA_VISIBLE_DEVICES=1 lerobot-eval \
  --policy.path=lerobot/smolvla_base \
  --env.type=libero \
  --env.task=libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=50 \
  --env.max_parallel_tasks=1 \
  --output_dir=/root/acib/results/baseline_standard_gpu1 \
  2>&1 | tee /root/acib/logs/baseline_standard_gpu1.log

# 扰动
CUDA_VISIBLE_DEVICES=1 lerobot-eval \
  --policy.path=lerobot/smolvla_base \
  --env.type=libero_plus \
  --env.task=libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=50 \
  --env.max_parallel_tasks=1 \
  --output_dir=/root/acib/results/baseline_perturbed_gpu1 \
  2>&1 | tee /root/acib/logs/baseline_perturbed_gpu1.log
```

## 输出格式

lerobot-eval 输出 JSON：
```json
{
  "suite_name": {
    "task_0": {"success_rate": 0.XX, "n_episodes": 50},
    "task_1": {...},
    ...
    "avg_success_rate": 0.XX
  }
}
```

## 结果收集

eval 完成后需要汇总的指标：
1. **Per-suite 标称 success rate**（4 个数字）
2. **Per-suite × per-perturbation-dimension success rate**（4×4=16 个数字）
3. **Robustness gap** = 标称 SR - 扰动 SR（越大说明越脆弱，ACIB 要缩小这个 gap）
4. **Per-difficulty (L1-L5) success rate**（如果 LIBERO-Plus 输出支持）

这些数字构成 MVP-2 ACIB-S 的 baseline 对照。
