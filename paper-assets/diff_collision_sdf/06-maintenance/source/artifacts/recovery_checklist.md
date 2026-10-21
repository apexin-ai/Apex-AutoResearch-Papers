# Server Recovery Execution Checklist

Generated: 2026-05-30
Target: 6/1 恢复后零调试立即执行
Servers: westd-35807 (4× GPU), westd-45947 (2× GPU)

---

## Phase 0: 连接验证（两台服务器各执行一次）

### 0.1 SSH 连接测试

```bash
# westd-35807
ssh westd-35807 "echo 'OK: westd-35807 connected' && uptime"

# westd-45947
ssh westd-45947 "echo 'OK: westd-45947 connected' && uptime"
```

**如果连接失败**: AutoDL 重启后端口可能变化。去 AutoDL 控制台查新端口，更新 `~/.ssh/config`。

### 0.2 GPU 健康检查

```bash
ssh westd-35807 "nvidia-smi --query-gpu=name,memory.total,memory.used,temperature.gpu --format=csv,noheader"
ssh westd-45947 "nvidia-smi --query-gpu=name,memory.total,memory.used,temperature.gpu --format=csv,noheader"
```

预期: RTX PRO 6000 (96GB) × 4 (35807) / × 2 (45947), 温度 < 85°C, memory.used 接近 0。

### 0.3 PyTorch CUDA 验证

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')
\""
```

同理对 westd-45947 执行。

### 0.4 磁盘空间确认

```bash
ssh westd-35807 "df -h /root/autodl-tmp && du -sh /root/autodl-tmp/checkpoints /root/autodl-tmp/eval_results /root/colliforce-vla/data 2>/dev/null"
ssh westd-45947 "df -h /root/autodl-tmp && du -sh /root/autodl-tmp/checkpoints /root/autodl-tmp/eval_results /root/colliforce-vla/data 2>/dev/null"
```

**红线**: /root/autodl-tmp 可用空间 < 20GB 则需先清理再跑实验。westd-45947 上次磁盘满 (250G/250G) 需特别关注。

### 0.5 Conda 环境 + 项目代码验证

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  which python && python --version && \
  cd /root/colliforce-vla && git log --oneline -3 && \
  python -c 'import robosuite; print(f\"robosuite={robosuite.__version__}\")' && \
  python -c 'from libero.libero.benchmark import get_benchmark; print(\"LIBERO OK\")'"
```

同理对 westd-45947 执行。如 git log 落后则需 `git pull`。

---

## Phase 1: D049 #1 — Pi0.5 Baseline +2 Seeds (最高优先)

**目标**: 给当前仅 1 seed 的 Pi0.5 baseline 追加 2 个 eval seed，验证 Claim 1 基准稳定性。
**Server**: westd-35807 (有 4 GPU，可并行 2 eval)
**预计耗时**: ~2.5h per eval seed, 并行跑 ~2.5h 总计
**GPU 占用**: cuda:0, cuda:1

### 1.1 参考: 已有 baseline eval 命令 (eval_pi05_baseline_reeval_disp)

```bash
# 已完成的 baseline eval (CAR=28.5%, TSR=71.5%):
# server: westd-45947, GPU: cuda:1
# python scripts/eval_safelibero.py \
#   --default_policy --config_name pi05_libero --suite safelibero_object \
#   --pi05 --seed 0 --gpu 1 --n_episodes 200
```

### 1.2 Eval Seed 42 (cuda:0)

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/colliforce-vla && \
  export WANDB_MODE=disabled && export MUJOCO_GL=egl && \
  nohup python scripts/eval_safelibero.py \
    --default_policy \
    --config_name pi05_libero \
    --suite safelibero_object \
    --pi05 \
    --seed 42 \
    --gpu 0 \
    --n_episodes 200 \
    --save_dir /root/autodl-tmp/eval_results \
    > /root/runs/diff_collision_sdf/eval_pi05_baseline_seed42.log 2>&1 &
  echo \$!"
```

### 1.3 Eval Seed 99 (cuda:1)

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/colliforce-vla && \
  export WANDB_MODE=disabled && export MUJOCO_GL=egl && \
  nohup python scripts/eval_safelibero.py \
    --default_policy \
    --config_name pi05_libero \
    --suite safelibero_object \
    --pi05 \
    --seed 99 \
    --gpu 1 \
    --n_episodes 200 \
    --save_dir /root/autodl-tmp/eval_results \
    > /root/runs/diff_collision_sdf/eval_pi05_baseline_seed99.log 2>&1 &
  echo \$!"
```

### 1.4 预期输出路径

```
/root/autodl-tmp/eval_results/eval_safelibero_object_all_levelII_default_seed42.json
/root/autodl-tmp/eval_results/eval_safelibero_object_all_levelII_default_seed99.json
```

### 1.5 完成后提取指标

```bash
ssh westd-35807 "python3 -c \"
import json
for seed in [42, 99]:
    path = f'/root/autodl-tmp/eval_results/eval_safelibero_object_all_levelII_default_seed{seed}.json'
    try:
        with open(path) as f:
            data = json.load(f)
        results = data['results']
        tsr = sum(r['TSR'] for r in results) / len(results)
        car = sum(r['CAR'] for r in results) / len(results)
        print(f'Seed {seed}: CAR={car*100:.1f}%, TSR={tsr*100:.1f}%')
    except Exception as e:
        print(f'Seed {seed}: ERROR - {e}')
\""
```

### 1.6 汇报格式

```
Pi0.5 Baseline (3 seeds): CAR=X.X%±Y.Y%, TSR=X.X%±Y.Y%
  seed0:  CAR=28.5%, TSR=71.5%  (existing)
  seed42: CAR=__._%, TSR=__.__%
  seed99: CAR=__._%, TSR=__.__%
```

---

## Phase 2: D049 #2 — Demo Collision-Free 标注 (CPU-only, 10min)

**目标**: 标注 200 demos 的 collision-free/containing 状态，确定自然 cf rate。
**Server**: westd-35807 或 westd-45947 (任一台, CPU-only 不占 GPU)
**预计耗时**: ~5-10 分钟

### 2.1 Sync 标注脚本到服务器

```bash
# 本地路径
LOCAL_SCRIPT="/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/scripts/demo_collision_label.py"

# 复制到服务器
scp $LOCAL_SCRIPT westd-35807:/root/colliforce-vla/scripts/demo_collision_label.py
```

### 2.2 执行标注

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/colliforce-vla && \
  export MUJOCO_GL=egl && \
  python scripts/demo_collision_label.py \
    --suite safelibero_object \
    --safety_level II \
    --output_dir /root/autodl-tmp/demo_labels"
```

### 2.3 预期输出路径

```
/root/autodl-tmp/demo_labels/collision_labels_safelibero_object_levelII.json
/root/autodl-tmp/demo_labels/collision_label_summary_safelibero_object_levelII.json
```

### 2.4 提取关键数据

```bash
ssh westd-35807 "python3 -c \"
import json
with open('/root/autodl-tmp/demo_labels/collision_label_summary_safelibero_object_levelII.json') as f:
    data = json.load(f)
print(f'Overall CF rate: {data[\"overall_cf_rate\"]*100:.1f}%')
print(f'Total demos: {data[\"total_demos\"]}')
print()
for t in data['per_task']:
    print(f'Task {t[\"task_id\"]} ({t[\"task_name\"]}):')
    print(f'  CF: {t[\"n_cf\"]}/{t[\"n_cf\"]+t[\"n_cc\"]} ({t[\"cf_rate\"]*100:.1f}%)')
    print(f'  CF indices: {t[\"cf_episode_indices\"]}')
\""
```

### 2.5 汇报格式

```
Demo Collision Labeling Complete:
  Overall: X/200 collision-free (XX.X%)
  Per-task:
    Task 0 (orange_juice):    XX/50 CF (XX.X%)
    Task 1 (chocolate_pudding): XX/50 CF (XX.X%)
    Task 2 (milk):            XX/50 CF (XX.X%)
    Task 3 (bbq_sauce):       XX/50 CF (XX.X%)

推荐分层网格: L0=XX%, L1=25%, L2=50%, L3=75%, L4=100%
(如果自然 cf rate > 80%，需调整分层点位)
```

---

## Phase 3: D049 #3-6 前置准备检查

### 3.1 代码/脚本部署状态

| 脚本 | 本地路径 | 服务器状态 | 需要 Sync |
|------|---------|-----------|----------|
| demo_collision_label.py | artifacts/scripts/ | ❌ 未部署 | ✅ Phase 2.1 中 sync |
| robocasa_eval.py | artifacts/scripts/ | ❌ 未部署 | 待 Phase 4 |
| robocasa_finetune_config.py | artifacts/scripts/ | ❌ 未部署 | 待 Phase 4 |
| eval_safelibero.py | supplementary/code/eval/ | ✅ 已在服务器 | — |
| train_pi05_lora_baseline.py | supplementary/code/training/ | ✅ 已在服务器 | — |
| train_a1_sdf_aux_pi05.py | supplementary/code/training/ | ✅ 已在服务器 | — |

### 3.2 数据/模型依赖

| 依赖 | 路径 | 服务器 | 状态 |
|------|------|--------|------|
| Pi0.5 pretrained weights | /root/autodl-tmp/openpi_weights/pi05_libero/ | 两台 | ✅ 已有 |
| SafeLIBERO demo HDF5 | /root/colliforce-vla/data/ | 两台 | ✅ 已有 |
| SDF ground truth | /root/colliforce-vla/data/sdf_gt_object_chocolate.npz | 两台 | ✅ 已有 |
| LoRA checkpoints (s0-s2) | /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/ | 两台 | ✅ 已有 |
| LeRobot dataset (safelibero_object) | /root/colliforce-vla/data/safelibero_object/ | 两台 | ✅ 已有 |
| RoboCasa package | — | 两台 | ❌ 需安装 |
| RoboCasa demo data | — | — | ❌ 需下载 |
| OpenVLA model weights | — | — | ❌ 需重新下载 (之前损坏) |

### 3.3 Demo Curation Training (plan_018, 756 GPU-hrs) 前置

标注完成后需要:
1. 根据实际 cf rate 确定 5 个 curation levels
2. 为每个 level 创建 curated dataset (HF push 或本地 episode index filter)
3. 每个 level × 3 seeds × 30K steps = 18 training runs

```bash
# 批量 sync 脚本到服务器
scp artifacts/scripts/demo_collision_label.py westd-35807:/root/colliforce-vla/scripts/
scp artifacts/scripts/robocasa_eval.py westd-35807:/root/colliforce-vla/scripts/
scp artifacts/scripts/robocasa_finetune_config.py westd-35807:/root/colliforce-vla/scripts/
```

### 3.4 Seed3 λ=0.1 重启 (plan 在 registry 中已有)

```bash
# westd-45947:cuda:0 — SDF λ=0.1 seed3
ssh westd-45947 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/colliforce-vla && \
  python scripts/train_a1_sdf_aux_pi05.py \
    --scene object_pudding \
    --seed 3 \
    --gpu 0 \
    --lambda_sdf 0.1 \
    --num_train_steps 30000 \
    --exp_name a1_sdf_pi05_object_pudding_seed3_l01_high"
```

**注意**: westd-45947 上次因磁盘满 crash。执行前必须确认 `/root/autodl-tmp` 可用空间 > 50GB。如不足：
```bash
# 清理已确认不需要的 checkpoint (failed/killed 实验)
ssh westd-45947 "du -sh /root/autodl-tmp/checkpoints/*/  | sort -rh | head -10"
```

### 3.5 RoboCasa 环境搭建 (plan_020, 需 Director 批准后执行)

```bash
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  source /etc/network_turbo && \
  pip install robocasa robosuite && \
  python -c 'import robocasa; print(f\"robocasa={robocasa.__version__}\")'"
```

RoboCasa 需要下载 kitchen assets (~2GB), 首次 import 时自动下载。

---

## Phase 4: 故障处理

### 4.1 SSH 连接超时

```
错误: ssh: connect to host XXX port XXXXX: Connection refused
```

**原因**: AutoDL 实例重启后端口变化。
**处理**:
1. 登录 AutoDL 控制台 (autodl.com)
2. 找到实例，查看新 SSH 端口
3. 更新 `~/.ssh/config` 中对应 Host 的 Port
4. 重试连接

### 4.2 GPU 异常

```
错误: CUDA error: out of memory / CUDA driver version is insufficient
```

**处理**:
```bash
# 检查是否有残留进程
ssh westd-35807 "nvidia-smi | grep python"

# 如有残留，kill 掉
ssh westd-35807 "nvidia-smi --query-compute-apps=pid --format=csv,noheader | xargs -I{} kill -9 {}"

# 如果 CUDA driver 报错，需要重启实例
```

### 4.3 磁盘满

```
错误: OSError: [Errno 28] No space left on device
```

**westd-45947 高风险** (上次 250G/250G 满盘)

**安全清理顺序**:
```bash
# 1. 检查空间分布
ssh westd-45947 "du -sh /root/autodl-tmp/*/ 2>/dev/null | sort -rh | head -20"

# 2. 清理 pip cache
ssh westd-45947 "pip cache purge"

# 3. 清理 HF cache (大模型缓存)
ssh westd-45947 "du -sh /root/autodl-tmp/.hf_cache/ 2>/dev/null"

# 4. 清理 failed 实验的 checkpoint (逐个确认)
# ⚠️ 只删 conclusion=failed/killed 且无 parent 依赖的 checkpoint
# ⚠️ 禁止删除 conclusion=success 的 checkpoint
```

**禁止操作**:
- `rm -rf /root/autodl-tmp/checkpoints/` (会删除所有 checkpoint)
- 删除 success 实验的 checkpoint/log
- 删除其他项目的文件
- 大规模清理 (>50GB) 前未经 Director 批准

### 4.4 LeRobot Dataset API 不兼容

上次 seed3 训练因 LeRobot API 变化失败 (`torch.stack() received HF Column`)。

**已知 fix** (4 patches, 已在 westd-45947 验证):
```bash
# 检查 patch 是否已应用
ssh westd-35807 "grep -c 'PATCHED' /root/miniconda3/lib/python*/site-packages/lerobot/common/datasets/lerobot_dataset.py 2>/dev/null || echo 'NO_PATCH'"
```

如未 patch，需重新应用。Patch 内容在 train_pi05_lora_baseline_s3 的 registry notes 中。

### 4.5 Eval 脚本 Rotation Bug

确认使用的 eval 脚本包含 180° 相机旋转修复:
```bash
ssh westd-35807 "grep -c 'rotate\|flip\|180' /root/colliforce-vla/scripts/eval_safelibero.py"
```

如果输出 0，需要 sync 修复版本。

---

## 执行时间线

| 时间 | 操作 | Server | GPU |
|------|------|--------|-----|
| T+0 | Phase 0: 连接验证 (两台) | both | — |
| T+5min | Phase 2: Demo 标注 (CPU) | 35807 | — |
| T+5min | Phase 1: Baseline eval seed42+99 (并行) | 35807 | cuda:0,1 |
| T+15min | Phase 2 完成, 汇报 cf rate | — | — |
| T+15min | Phase 3: Sync 脚本到服务器 | both | — |
| T+2.5h | Phase 1 完成, 汇报 3-seed baseline | — | — |
| T+2.5h | 服务器就绪, 等 Director 决策下一步 | — | — |

**Phase 1 和 Phase 2 可同时启动** — eval 用 cuda:0,1, 标注用 CPU, 互不干扰。
