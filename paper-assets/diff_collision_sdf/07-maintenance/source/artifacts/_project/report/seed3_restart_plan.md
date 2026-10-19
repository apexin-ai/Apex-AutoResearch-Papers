# Seed3 Restart Plan

> 编写时间: 2026-05-29 | 两台服务器因 AutoDL 实例不可达而中断

---

## Server: westd-35807

### Experiment: train_pi05_lora_baseline_s3_v2

- **Status**: DONE (failed) — SSH check failed 5x, port 35807 不可达
- **Parent**: train_pi05_lora_baseline_s3 (v1 因 LeRobot API 不兼容在 step 0 崩溃)
- **v2 进度**: 启动后确认到 step 8，loss ~0.10-0.15，速度 ~1.5s/it，预计 ~12.5h 完成 30K steps。之后 SSH 断连，实际进度未知
- **Last checkpoint**: 未知。v2 可能已跑完（12.5h 足够），也可能因服务器关机中断。需上线后检查
- **Checkpoint 路径**: 预计 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed3/`（参考 seed0-2 的命名规律）
- **训练目标**: LoRA baseline (no SDF) seed3, object_pudding, 30K steps — 第 4 个 seed 提升统计显著性

#### LeRobot Patch（重启后必须验证）

v2 启动前已在 westd-35807 上打了 4 处 patch（移植自 westd-45947）。**AutoDL 重启后 patch 应仍在**（文件在 conda env 里），但必须验证：

| 位置 | 修改内容 |
|------|---------|
| `lerobot_dataset.py:508-509` | `torch.stack(hf_dataset["timestamp"])` → `np.array(to_dict()["timestamp"])` |
| `lerobot_dataset.py:511` | `check_timestamps_sync` 用 try/except 包裹（object_pudding timestamp 不符合严格校验） |
| `utils.py:272` | `hf_transform_to_torch` 增加 `dict` + `"bytes"` 类型处理（图像以 bytes dict 存储） |
| `lerobot_dataset.py:698` | `_query_hf_dataset` 整个方法重写，处理多种数据类型 |

Patch 文件路径: `/root/miniconda3/lib/python3.*/site-packages/lerobot/common/datasets/`

#### Resume Strategy

```
如果 checkpoint 存在且 step >= 30000:
  → 训练已完成，直接收集结果
如果 checkpoint 存在但 step < 30000:
  → 从 checkpoint resume（需确认脚本是否支持 --resume）
如果无 checkpoint:
  → 从头重跑（patch 已在，直接启动）
```

#### Restart Commands

```bash
# Step 1: 确认 SSH 端口（AutoDL 重启后端口可能变）
# 去 AutoDL 控制台查新端口，更新 ~/.ssh/config 中 westd-35807 的 Port

# Step 2: 检查环境
ssh westd-35807 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\""
ssh westd-35807 "nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv,noheader"
ssh westd-35807 "df -h /root/autodl-tmp"

# Step 3: 验证 LeRobot patch 是否还在
ssh westd-35807 "grep -n 'to_dict' /root/miniconda3/lib/python3.*/site-packages/lerobot/common/datasets/lerobot_dataset.py | head -5"

# Step 4: 检查 checkpoint
ssh westd-35807 "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed3/ 2>/dev/null || echo 'NO_CHECKPOINT'"
# 也检查 /tmp 日志
ssh westd-35807 "tail -20 /tmp/train_lora_s3_restart.log 2>/dev/null || echo 'LOG_GONE'"

# Step 5: 启动训练（如需从头或 resume）
# 用 tmux 启动，避免 SSH 超时
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/colliforce-vla
export WANDB_MODE=disabled
tmux new-session -d -s lora_s3 'python scripts/train_pi05_lora_baseline.py --scene object_pudding --seed 3 --gpu 0 --batch_size 32 --num_train_steps 30000'
```

---

## Server: westd-45947

### Experiment: train_pi05_a1_obj_s3_l01_v2

- **Status**: DONE (failed) — SSH check failed 5x, port 45947 不可达
- **Parent**: train_pi05_a1_obj_s3_l01 (v1 在 step 2000 因磁盘满崩溃)
- **v1 已确认保存**: step 2000 checkpoint ✅
- **v2 进度**: 从 step 2000 resume 后 SSH 断连，实际进度未知。磁盘清理后曾释放 47.6GB
- **Checkpoint 路径**: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed3_l01/` (断连前 11G)
- **训练目标**: SDF auxiliary loss (λ=0.01) seed3, object_pudding, 30K steps — 第 4 个 seed

#### 磁盘状况（断连前快照）

```
/root/autodl-tmp/ 总计 250G，100% 满（清理后有 47.6GB 可用，可能已被 v2 训练消耗）

大项:
  checkpoints/                           206G
    a1_sdf_pi05_object_pudding/          139G  ← 含 11 个子目录
      seed0_l005                          15G
      seed0_l01                           15G
      seed0_l1                           7.2G
      seed1_l005                         7.1G
      seed1_l01                          7.1G
      seed2_l005                         7.1G
      seed2_l1                            22G
      seed3_l01                           11G  ← 当前实验
      lora_baseline_seed0                 15G
      lora_baseline_seed1                 15G
      lora_baseline_seed2                 22G
    a3_grad_refine_object_pudding/        22G
    a3_grad_refine_spatial_bowl/          22G
    baseline_object_pudding/             6.6G
    baseline_object_pudding_eval/         19G
  openpi_weights/                         32G  ← 模型权重，不可删
  colliforce_data/                       1.3G
```

#### 磁盘清理计划

**安全删除候选**（需确认相关实验已完成评估）:

| 目标 | 大小 | 理由 |
|------|------|------|
| `baseline_object_pudding_eval/` | 19G | eval 产生的临时 checkpoint 副本，结果已在 eval_results/ |
| `a3_grad_refine_object_pudding/` | 22G | A3 实验如已完成，中间 checkpoint 可清 |
| `a3_grad_refine_spatial_bowl/` | 22G | 同上 |
| `seed0_l1/` + `seed2_l1/` | 29G | λ=1.0 配置，如非论文所需可清 |
| 旧 seed 的非 best checkpoint | ~20-40G | 保留 best + final，清除中间 step |

**预估可释放**: 50-90G（保守 50G）

**不可删除**:
- `openpi_weights/` (32G) — 基础模型权重
- `colliforce_data/` (1.3G) — 训练数据
- `seed3_l01/` — 当前实验 checkpoint
- 论文中使用到的 seed0-2 的 best checkpoint

#### Resume Strategy

```
如果 checkpoint step >= 30000:
  → 训练已完成，收集结果
如果 checkpoint step > 2000:
  → v2 有进展，继续 resume
如果 checkpoint step == 2000:
  → v2 未执行或崩溃，检查磁盘后 resume
先清理磁盘，确保至少 50G 可用再启动
```

#### Restart Commands

```bash
# Step 1: 确认 SSH 端口
# 去 AutoDL 控制台查新端口，更新 ~/.ssh/config 中 westd-45947 的 Port

# Step 2: 检查环境
ssh westd-45947 "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\""
ssh westd-45947 "nvidia-smi --query-gpu=name,memory.total,memory.used --format=csv,noheader"
ssh westd-45947 "df -h /root/autodl-tmp"

# Step 3: 检查 checkpoint
ssh westd-45947 "ls -la /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed3_l01/"
ssh westd-45947 "tail -20 /tmp/train_sdf_s3_l01_resume.log 2>/dev/null || echo 'LOG_GONE'"

# Step 4: 磁盘清理（根据实际情况选择）
# ⚠️ 删除前确认这些实验已完成评估
ssh westd-45947 "rm -rf /root/autodl-tmp/checkpoints/baseline_object_pudding_eval/"      # 释放 19G
ssh westd-45947 "rm -rf /root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/"     # 释放 22G
ssh westd-45947 "rm -rf /root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/"       # 释放 22G
ssh westd-45947 "df -h /root/autodl-tmp"  # 确认释放效果

# Step 5: 启动训练
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/colliforce-vla
export WANDB_MODE=disabled
tmux new-session -d -s sdf_s3 'python scripts/train_a1_sdf_aux_pi05.py --scene object_pudding --seed 3 --lambda_sdf 0.01 --gpu 0 --batch_size 32 --num_train_steps 30000 --lambda_ee 0.01 --lr 2.5e-5 --save_interval 2000 --resume'
```

---

## 恢复后第一步操作清单

1. **确认 SSH 端口** — 去 AutoDL 控制台查两台服务器新端口，更新 `~/.ssh/config`
2. **ssh_read_only 检查环境** — Python、conda、GPU、磁盘空间
3. **检查 checkpoint 完整性** — 确认文件未损坏、记录最新 step
4. **确认训练数据和模型权重仍在**:
   - westd-35807: `/root/colliforce-vla/` 代码 + SafeLIBERO 数据
   - westd-45947: `/root/autodl-tmp/openpi_weights/` + `/root/autodl-tmp/colliforce_data/`
5. **验证 LeRobot patch** (westd-35807) — grep 确认 4 处 patch 未被覆盖
6. **磁盘清理** (westd-45947) — 确保 ≥50G 可用
7. **启动训练** — 用 tmux，不用 submit_training_job（避免 timeout 问题）
8. **注册实验到 registry** — 创建 v3 条目记录 resume

## 已知风险

| 风险 | 影响 | 应对 |
|------|------|------|
| AutoDL 实例数据丢失 | 需从头搭建环境+重跑 | 检查 /root/autodl-tmp 数据完整性 |
| 端口变更后 ssh_config 未更新 | 所有 SSH 操作失败 | 优先更新 config |
| LeRobot patch 被 conda update 覆盖 | 训练 step 0 崩溃 | 启动前 grep 验证 |
| 磁盘仍满 (westd-45947) | 训练写 checkpoint 时崩溃 | 先清理再启动 |
| v2 实际已跑完但 SSH 断连导致 registry 标 failed | 不需要重跑 | 先检查 checkpoint |
