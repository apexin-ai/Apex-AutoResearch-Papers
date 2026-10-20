# prep gradient analysis v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_gradient-analysis-v2_20260527T104315_result.json`
- **Structured JSON:** [`14e0756a0db68c9dabff.json`](../../sessions/14/14e0756a0db68c9dabff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run passed. Now I have all the information. Here's the complete report:

---

## v2 梯度分析准备报告

### 1. 脚本状态

| 项目 | 状态 |
|------|------|
| 脚本路径 | `/root/occsafe_vla/openvla-oft/scripts/v2_gradient_analysis.py` |
| **westd-10894** | ✅ 存在，dry-run 通过 |
| **westd-34685** | ❌ **不存在，需要同步** |
| 额外依赖 | 无（与 finetune.py 相同环境） |

**需要操作**: git pull 或 scp 将脚本同步到 34685。

### 2. Checkpoint 清单

#### westd-34685（~13:00 UTC GPU 释放后可用）

| 条件 | Checkpoint 路径 | Step | 状态 |
|------|----------------|------|------|
| **full_occ_bn** | `.../full_occ_bn_v2_s1/.../--50000_chkpt` | 50000 | ✅ 完整 |
| **detach_bn** | `.../detach_bn_v2_s0/.../--50000_chkpt` | 50000 | ✅ 完整 |
| **vanilla** | `.../vanilla_v2_s1/.../--50000_chkpt` | 50000 | ✅ 完整 |
| **detach_ln** | `.../detach_ln_v2_s1/.../--40000_chkpt` | 40000 | ⚠️ 训练中，~13:00 应有 50000 |

#### westd-10894

| 条件 | Checkpoint 路径 | Step | 状态 |
|------|----------------|------|------|
| **full_occ_ln** | `.../full_occ_ln_v2_s1c/.../--30000_chkpt` | 30000 | ⏳ 训练中，50000 ETA ~22:50 UTC |

**关键缺口**: `full_occ_ln` 没有已完成的 v2 50000 checkpoint。最早 ~22:50 UTC 才有（在 10894 上）。

### 3. 现有梯度分析结果

10894 上 `/root/autodl-tmp/analysis/gradient_same_seed/` (May 25) 存在旧结果，但使用的是 **v1 checkpoint**（如 `vanilla_retrain_s0`）——正是 D056/D057 推翻的那批。需要全部用 v2 checkpoint 重新跑。

### 4. 运行命令模板

在 34685 上，激活环境后：
```bash
cd /root/occsafe_vla/openvla-oft
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe
```

**4 条并行（34685, ~13:00 GPU 释放后）：**

```bash
# Cell 1: Full OCC BN
nohup python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt \
  --condition_name full_occ_bn --num_samples 100 --device cuda:0 \
  > /tmp/grad_full_occ_bn.log 2>&1 &

# Cell 3: Detach BN
nohup python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0--50000_chkpt \
  --condition_name detach_bn --num_samples 100 --device cuda:1 \
  > /tmp/grad_detach_bn.log 2>&1 &

# Vanilla
nohup python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt \
  --condition_name vanilla --num_samples 100 --device cuda:2 \
  > /tmp/grad_vanilla.log 2>&1 &

# Cell 4: Detach LN (确认 50000 checkpoint 存在后)
nohup python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1--50000_chkpt \
  --condition_name detach_ln --num_samples 100 --device cuda:3 \
  > /tmp/grad_detach_ln.log 2>&1 &
```

**第 5 条（10894, ~22:50 GPU 释放后）：**
```bash
# Cell 2: Full OCC LN
nohup python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt \
  --condition_name full_occ_ln --num_samples 100 --device cuda:0 \
  > /tmp/grad_full_occ_ln.log 2>&1 &
```

### 5. 运行时间预估

| 阶段 | 耗时 |
|------|------|
| 模型加载（per condition） | ~60-90s |
| 梯度计算（100 samples） | ~30-60s |
| **单条件总计** | ~2-3 min |
| **34685 4 条并行** | ~3-5 min |
| **10894 第 5 条** | ~3-5 min |

**总计**: 34685 上 ~5 min（13:00 开始，13:05 完成），10894 上 ~5 min（22:50 开始，22:55 完成）。

### 6. 前置操作清单

1. ⚠️ **同步脚本到 34685**：`scp` 或 `git pull`
2. ⚠️ **确认 detach_ln_v2_s1 50000 checkpoint** 在 ~13:00 时已保存
3. ⚠️ **full_occ_ln 需等到 ~22:50 UTC**（或用 30000 intermediate，但不推荐——不同 step 的梯度特征不可比）

---
