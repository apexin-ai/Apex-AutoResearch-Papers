# D012 Eval Pipeline — 命令模板

## 概述

- **模型**: Pi0.5+A1 SDF (6个模型 = 2 lambda × 3 seed)
- **评估基准**: SafeLIBERO Object (safelibero_object, Level II, 4 tasks × 50 episodes = 200 episodes/model)
- **流程**: 先启动 `serve_policy.py` (占GPU加载模型), 再运行 `eval_pi05_safelibero.py` (连接websocket)
- **输出**: JSON 文件含 TSR/CAR/frozen_rate/per-episode displacement metrics

## 服务器分配

| 模型 | 服务器 | GPU | Port | Checkpoint 目录 |
|------|--------|-----|------|-----------------|
| s0_l005 | westd-45947 | cuda:0 | 8000 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/<STEP>/` |
| s0_l01  | westd-45947 | cuda:1 | 8001 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/<STEP>/` |
| s1_l005 | westd-35807 | cuda:0 | 8000 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/<STEP>/` |
| s1_l01  | westd-35807 | cuda:1 | 8001 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/<STEP>/` |
| s2_l005 | westd-35807 | cuda:2 | 8002 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/<STEP>/` |
| s2_l01  | westd-35807 | cuda:3 | 8003 | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/<STEP>/` |

> **`<STEP>`**: 训练完成后替换为实际 step（如 `best`、`6000`、`8000`）。查看可用 step:
> `ls /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/`

## 公共环境设置

```bash
# 每个 tmux 窗口都需执行
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export JAX_PLATFORMS=cpu
export PYTHONPATH=/root/colliforce-vla/openpi/src:$PYTHONPATH
cd /root/colliforce-vla
```

## westd-45947 命令（2 个模型）

### 创建 tmux session

```bash
tmux new-session -d -s eval_d012
tmux new-window -t eval_d012 -n s0_l005
tmux new-window -t eval_d012 -n s0_l01
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s0_l005.json

# === Step 3: 清理 ===
kill $SERVE_PID
echo "s0_l005 eval complete"
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s0_l01.json

# === Step 3: 清理 ===
kill $SERVE_PID
echo "s0_l01 eval complete"
```

## westd-35807 命令（4 个模型）

### 创建 tmux session

```bash
tmux new-session -d -s eval_d012
tmux new-window -t eval_d012 -n s1_l005
tmux new-window -t eval_d012 -n s1_l01
tmux new-window -t eval_d012 -n s2_l005
tmux new-window -t eval_d012 -n s2_l01
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s1_l005.json

kill $SERVE_PID
echo "s1_l005 eval complete"
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l01/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s1_l01.json

kill $SERVE_PID
echo "s1_l01 eval complete"
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l005/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s2_l005.json

kill $SERVE_PID
echo "s2_l005 eval complete"
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
    --policy.dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed2_l01/<STEP> \
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
    --save_dir /root/autodl-tmp/eval_results/d012 \
    --output_path /root/autodl-tmp/eval_results/d012/eval_d012_s2_l01.json

kill $SERVE_PID
echo "s2_l01 eval complete"
```

## 输出文件

所有结果保存在 `/root/autodl-tmp/eval_results/d012/`:

| 文件 | 模型 |
|------|------|
| `eval_d012_s0_l005.json` | seed=0, λ=0.005 |
| `eval_d012_s0_l01.json`  | seed=0, λ=0.01  |
| `eval_d012_s1_l005.json` | seed=1, λ=0.005 |
| `eval_d012_s1_l01.json`  | seed=1, λ=0.01  |
| `eval_d012_s2_l005.json` | seed=2, λ=0.005 |
| `eval_d012_s2_l01.json`  | seed=2, λ=0.01  |

## 时间预估

- serve_policy 启动: ~30-60s (模型加载到GPU)
- 每个 eval: ~200 episodes × ~8s/ep ≈ 27 min
- 所有 6 个 eval 并行: ~30 min 总时长

## 注意事项

1. **训练完成后**: 先用 `ls` 确认最终 checkpoint step，替换 `<STEP>` 为 `best` 或具体 step 号
2. **端口冲突**: 确保同一服务器上每个 serve_policy 用不同端口
3. **baseline_frozen_rate**: 当前 baseline eval (v11) 无 frozen_rate 数据，D012 eval 暂不设此参数
4. **eval 结果收集**: 6 个 JSON 文件写完后，用 `analyze_d012_results.py` 统一分析
