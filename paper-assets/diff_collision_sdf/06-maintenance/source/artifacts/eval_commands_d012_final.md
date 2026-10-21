# D012 Final Eval Pipeline (30K) — 命令模板

## 概述

- **模型**: Pi0.5+A1 SDF (6个模型 = 2 lambda × 3 seed)
- **评估基准**: SafeLIBERO Object (safelibero_object, Level II, 4 tasks × 50 episodes = 200 episodes/model)
- **Checkpoint**: step `30000` (训练终点，每 2000 步保存，30000 是 save_interval 的整数倍)
- **输出**: JSON 文件含 TSR/CAR/frozen_rate/per-episode displacement metrics

## 训练进度 (截至 2026-05-24 12:30 UTC)

| 模型 | 服务器 | 当前 step | 预计完成 (UTC) |
|------|--------|-----------|----------------|
| s0_l005 | westd-45947 | 25533/30000 (85%) | ~18:00 |
| s0_l01  | westd-45947 | ~25530/30000 | ~18:00 |
| s1_l005 | westd-35807 | 23122/30000 (77%) | ~21:20 |
| s1_l01  | westd-35807 | ~23100/30000 | ~21:20 |
| s2_l005 | westd-35807 | 23078/30000 (77%) | ~21:25 |
| s2_l01  | westd-35807 | ~23070/30000 | ~21:25 |

> **注**: s1/s2 训练历史——磁盘满崩溃于 step ~7999 (M036)，从 step 6000 checkpoint 恢复；后在 step ~11280 因 Phase 2 transition fix 再次重启。

## 服务器分配

| 模型 | 服务器 | GPU | Port | Checkpoint 路径 |
|------|--------|-----|------|-----------------|
| s0_l005 | westd-45947 | cuda:0 | 8000 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000/` |
| s0_l01  | westd-45947 | cuda:1 | 8001 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000/` |
| s1_l005 | westd-35807 | cuda:0 | 8000 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000/` |
| s1_l01  | westd-35807 | cuda:1 | 8001 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/30000/` |
| s2_l005 | westd-35807 | cuda:2 | 8002 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/30000/` |
| s2_l01  | westd-35807 | cuda:3 | 8003 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/30000/` |

## 公共环境设置

```bash
# 每个 tmux 窗口都需执行
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla
```

## 启动前检查

```bash
# 确认 checkpoint 30000 已生成
ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000/
# 确认输出目录存在
mkdir -p /root/autodl-tmp/eval_results/d012_final
```

---

## westd-45947 命令（2 个模型, 预计 ~18:00 UTC 可启动）

### 创建 tmux session

```bash
tmux new-session -d -s eval_d012_final
tmux new-window -t eval_d012_final -n s0_l005
tmux new-window -t eval_d012_final -n s0_l01
```

### Model: s0_l005 (tmux window: s0_l005)

```bash
# === 环境 ===
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

# === Step 1: 启动 serve_policy (GPU 0, Port 8000) ===
CUDA_VISIBLE_DEVICES=0 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000 \
    --port 8000 &
SERVE_PID=$!

# 等待 serve_policy 就绪（通常 30-60s）
sleep 60

# === Step 2: 运行 eval ===
python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8000 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s0_l005.json

# === Step 3: 清理 ===
kill $SERVE_PID
echo "s0_l005 final eval complete"
```

### Model: s0_l01 (tmux window: s0_l01)

```bash
# === 环境 ===
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

# === Step 1: 启动 serve_policy (GPU 1, Port 8001) ===
CUDA_VISIBLE_DEVICES=1 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000 \
    --port 8001 &
SERVE_PID=$!

sleep 60

# === Step 2: 运行 eval ===
python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8001 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s0_l01.json

# === Step 3: 清理 ===
kill $SERVE_PID
echo "s0_l01 final eval complete"
```

---

## westd-35807 命令（4 个模型, 预计 ~21:30 UTC 可启动）

### 创建 tmux session

```bash
tmux new-session -d -s eval_d012_final
tmux new-window -t eval_d012_final -n s1_l005
tmux new-window -t eval_d012_final -n s1_l01
tmux new-window -t eval_d012_final -n s2_l005
tmux new-window -t eval_d012_final -n s2_l01
```

### Model: s1_l005 (tmux window: s1_l005)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

CUDA_VISIBLE_DEVICES=0 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/30000 \
    --port 8000 &
SERVE_PID=$!
sleep 60

python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8000 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s1_l005.json

kill $SERVE_PID
echo "s1_l005 final eval complete"
```

### Model: s1_l01 (tmux window: s1_l01)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

CUDA_VISIBLE_DEVICES=1 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/30000 \
    --port 8001 &
SERVE_PID=$!
sleep 60

python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8001 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s1_l01.json

kill $SERVE_PID
echo "s1_l01 final eval complete"
```

### Model: s2_l005 (tmux window: s2_l005)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

CUDA_VISIBLE_DEVICES=2 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/30000 \
    --port 8002 &
SERVE_PID=$!
sleep 60

python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8002 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s2_l005.json

kill $SERVE_PID
echo "s2_l005 final eval complete"
```

### Model: s2_l01 (tmux window: s2_l01)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla

CUDA_VISIBLE_DEVICES=3 python /root/colliforce-vla/openpi/scripts/serve_policy.py \
    --env libero \
    --policy:checkpoint \
    --policy.config pi05_libero \
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/30000 \
    --port 8003 &
SERVE_PID=$!
sleep 60

python scripts/eval_pi05_safelibero.py \
    --host 0.0.0.0 \
    --port 8003 \
    --suite safelibero_object \
    --safety_level II \
    --n_episodes 50 \
    --max_steps 300 \
    --replan_steps 5 \
    --seed 7 \
    --save_dir /root/autodl-tmp/eval_results/d012_final \
    --output_path /root/autodl-tmp/eval_results/d012_final/eval_d012_final_s2_l01.json

kill $SERVE_PID
echo "s2_l01 final eval complete"
```

---

## 输出文件

所有结果保存在各服务器的 `/root/autodl-tmp/eval_results/d012_final/`:

| 文件 | 模型 | 服务器 |
|------|------|--------|
| `eval_d012_final_s0_l005.json` | seed=0, λ=0.005 | westd-45947 |
| `eval_d012_final_s0_l01.json`  | seed=0, λ=0.01  | westd-45947 |
| `eval_d012_final_s1_l005.json` | seed=1, λ=0.005 | westd-35807 |
| `eval_d012_final_s1_l01.json`  | seed=1, λ=0.01  | westd-35807 |
| `eval_d012_final_s2_l005.json` | seed=2, λ=0.005 | westd-35807 |
| `eval_d012_final_s2_l01.json`  | seed=2, λ=0.01  | westd-35807 |

## 修订后执行序列

```
westd-45947 s0 训练完成 (~18:00 UTC)
  → 创建输出目录 + 确认 checkpoint 30000 存在
  → 启动 serve_policy s0_l005 (port 8000) + s0_l01 (port 8001)
  → 并行 eval 两个模型 (~30 min, GPU 不再与训练共存)
  → eval 完成 (~18:40 UTC)
  → kill serve_policy，释放 GPU
  → 启动 LoRA baseline 训练 (2 seeds)

westd-35807 s1/s2 训练完成 (~21:30 UTC)
  → 确认 checkpoint 30000 存在 (注意之前磁盘满问题，先 df -h 确认空间足够)
  → 4 个 GPU 各启动一个 serve_policy
  → 并行 eval 4 个模型 (~30 min)
  → eval 完成 (~22:00 UTC)
```

## 时间预估

- serve_policy 启动: ~30-60s
- 每个 eval: ~200 episodes × ~8s/ep ≈ 27 min (训练完成后 GPU 独占，可能更快)
- westd-45947: 2 个 eval 并行 → ~30 min
- westd-35807: 4 个 eval 并行 → ~30 min

## 注意事项

1. **磁盘空间**: westd-35807 之前因磁盘满导致 s1/s2 训练崩溃。启动 eval 前先 `df -h /root/autodl-tmp/` 确认空间充足。当前 75GB/225GB 可用，eval JSON 文件很小 (~150KB/个)，不是问题。
2. **训练崩溃恢复**: s1/s2 磁盘满崩溃于 step ~7999 (M036)，从 step 6000 恢复；后在 step ~11280 因 Phase 2 fix 再次重启。checkpoint 保留策略只保留最近 2 个 + best。确认 30000 生成后旧 checkpoint 会被清理。
6. **s2_l01 SDF loss 异常**: s2_l01 的 SDF loss 持续偏高（~0.067 vs 其他 run ~0.033，约 2x），从 step 7K 到 23K 完全平坦无收敛。30K eval 时需特别关注该 run 的 CAR/TSR 是否偏离其他 seed，以判断是否为 outlier 需排除。
3. **Mid-eval 状态**: s0 的 mid-eval (step 10K) JSON 在 westd-45947 的 `d012_mid10k/` 目录。s1/s2 无 mid-eval 结果（训练在 mid-eval 前崩溃）。
4. **端口冲突**: 确保训练进程已完全退出再启动 serve_policy，否则 GPU 显存不够。
5. **结果收集**: 6 个 JSON 分布在两台服务器上，需要 scp 汇总到一处后用分析脚本统一处理。
