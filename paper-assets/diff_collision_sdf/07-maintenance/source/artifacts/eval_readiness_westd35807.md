# D012 Eval 就绪状态报告 — westd-35807

**检查时间**: 2026-05-23 ~10:30 UTC

## 检查结果

### 1. 项目代码目录
✅ `/root/colliforce-vla` — 代码已同步

### 2. Eval 脚本
✅ `scripts/eval_pi05_safelibero.py` (358行) — 存在且包含基础 metric
- ✅ CAR (Collision Avoidance Rate)
- ✅ TSR (Task Success Rate)
- ✅ avg_max_displacement (障碍物最大位移均值)
- ❌ **robot_total_displacement** — 缺失
- ❌ **min_ee_obstacle_distance** — 缺失
- ❌ **is_frozen / frozen_rate** — 缺失
- ❌ **pass/fail gate (CAR≥33% + TSR≥50%)** — 缺失

**结论**: eval 脚本缺少 D012 增强 metric，需要同步修复后再 eval。

### 3. 测试数据
✅ `/root/autodl-tmp/colliforce_data/safelibero_object/` — 存在
- `data/chunk-000/` 含 9 个 parquet 文件
- SafeLIBERO benchmark 代码: `/root/colliforce-vla/vlsa-aegis/safelibero/` ✅

### 4. Pi0.5 Base Checkpoint
✅ `/root/autodl-tmp/openpi_weights/pi05_libero/model.safetensors` (~6.7GB)
- config.json 同目录 ✅

### 5. 训练 Checkpoint 目录
⏳ 训练进行中，4 个目录已创建但尚无 checkpoint 文件：
```
/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/
├── a1_sdf_pi05_object_pudding_seed1_l005/  (wandb: 7nylrrzs) — 仅 wandb_id.txt
├── a1_sdf_pi05_object_pudding_seed1_l01/   — 仅 wandb_id.txt
├── a1_sdf_pi05_object_pudding_seed2_l005/  — 仅 wandb_id.txt
└── a1_sdf_pi05_object_pudding_seed2_l01/   (wandb: 6ygjfx6b) — 仅 wandb_id.txt
```
Lambda 后缀 `_l005` / `_l01` 已区分，无冲突 ✅

### 6. GPU 状态
✅ 4x NVIDIA RTX PRO 6000 (96GB)，全部在训练中
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 100% | 19055/97887 MiB |
| 1 | 55% | 19055/97887 MiB |
| 2 | 100% | 19055/97887 MiB |
| 3 | 100% | 19055/97887 MiB |

### 7. Eval 依赖
- ✅ `openpi_client` — conda base 和 libero env 均已安装
- ✅ `serve_policy.py` — `/root/colliforce-vla/vlsa-aegis/scripts/serve_policy.py`
- ⚠️ `libero` — 仅在 `libero` conda env 中 (`/root/miniconda3/envs/libero`)，**不在 base env**
- ✅ 磁盘空间: 112GB 可用 (/root/autodl-tmp)

## 缺失项 & 修复建议

| # | 问题 | 优先级 | 修复方案 |
|---|------|--------|----------|
| 1 | eval 脚本缺少增强 metric | **P0** | 下一个 worker 同步修复 eval_pi05_safelibero.py，添加 robot_total_displacement, min_ee_obstacle_distance, is_frozen/frozen_rate, pass/fail gate |
| 2 | checkpoint 文件尚未生成 | 等待 | 训练完成后自动生成，预计 ~11:00 UTC |
| 3 | libero 不在 base env | 低 | eval 时用 `conda activate libero` 即可 |

## Eval 执行命令模板

训练完成后，对每个 checkpoint 执行以下两步：

```bash
# 环境准备
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero
cd /root/colliforce-vla

# === 对每个 checkpoint 重复 ===
# 变量定义（替换为实际值）
CKPT_DIR="/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l005/<step>"
GPU_SERVE=0

# Step 1: 启动 serve_policy.py（tmux session）
tmux new-session -d -s serve
tmux send-keys -t serve "source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && cd /root/colliforce-vla && CUDA_VISIBLE_DEVICES=${GPU_SERVE} python vlsa-aegis/scripts/serve_policy.py checkpoint --config pi05_libero --dir ${CKPT_DIR}" Enter

# Step 2: 等待服务就绪后运行 eval
tmux new-session -d -s eval
tmux send-keys -t eval "source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && cd /root/colliforce-vla && python scripts/eval_pi05_safelibero.py --suite safelibero_object --safety_level I --n_episodes 50 --seed 7 --save_dir /root/autodl-tmp/eval_results" Enter
```

**4 个 checkpoint 路径**（`<step>` 待训练完成后确认）:
1. `a1_sdf_pi05_object_pudding_seed1_l005/<step>`
2. `a1_sdf_pi05_object_pudding_seed1_l01/<step>`
3. `a1_sdf_pi05_object_pudding_seed2_l005/<step>`
4. `a1_sdf_pi05_object_pudding_seed2_l01/<step>`

## 结论

**基础设施就绪，但 eval 脚本需要增强。** P0 阻塞项是 eval_pi05_safelibero.py 缺少 D012 要求的增强 metric（frozen 检测、pass/fail gate 等），需下一个 worker 修复后方可执行有效 eval。
