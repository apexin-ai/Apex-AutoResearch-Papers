# ops westd35807 training env prep and launch

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd35807_training_env_prep_and_launch_20260523T000711_result.json`
- **Structured JSON:** [`e14db555f15138e3edb7.json`](../../sessions/e1/e14db555f15138e3edb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个训练成功运行，loss 正常下降。汇报如下：

---

### 环境检查结果

| # | 检查项 | 状态 | 备注 |
|---|--------|------|------|
| 1 | train_a1_sdf_aux_pi05.py | ✅ | 已存在 |
| 2 | SDF GT 数据 | ✅ | `/root/colliforce-vla/data/sdf_gt_object_chocolate.npz` |
| 3 | object_pudding demo 数据 | ✅ | 已存在 |
| 4 | Pi0.5 PyTorch checkpoint | ✅ **修复** | JAX→PyTorch 转换完成（6.8GB） |
| 5 | lora_utils.py _dtype 修复 | ✅ | 已修复 |
| 6 | norm_stats q01/q99 | ✅ **修复** | 原值为 null，从 westd-45947 复制完整版 |
| 7 | openpi 环境 | ✅ | libero conda env + sys.path 导入正常 |

### 多 seed eval 结果
- **Seed 1**: TSR=76.0% (152/200), CAR=25.0% (50/200), avg_disp=0.1530
- **Seed 2**: TSR=75.0% (150/200), CAR=27.5% (55/200), avg_disp=0.1323
- serve_policy 已 kill，GPU 已释放

### 4 个训练启动状态

| tmux session | Seed | λ_sdf | GPU | PID | 前 3 步 loss |
|---|---|---|---|---|---|
| train_pi05_a1_obj_s1_l005 | 1 | 0.005 | cuda:0 | 291398 | 0.145 → 0.140 → 0.147 |
| train_pi05_a1_obj_s1_l01 | 1 | 0.01 | cuda:1 | 291473 | 0.145 → 0.140 → 0.147 |
| train_pi05_a1_obj_s2_l005 | 2 | 0.005 | cuda:2 | 291611 | 0.149 → 0.150 → 0.150 |
| train_pi05_a1_obj_s2_l01 | 2 | 0.01 | cuda:3 | 292370 | 0.150 → 0.151 → 0.151 |

### GPU 显存
每张 GPU 占用约 **19GB / 97.9GB**（19.4%），余量充裕。

### 训练速度
~1.3s/it（warmup 后），预计总训练时长约 **11 小时**。

### 修复操作
1. **Pi0.5 权重转换**：westd-35807 只有 JAX/OCDBT 格式，运行 `convert_jax_model_to_pytorch.py` 生成 model.safetensors
2. **norm_stats.json**：原文件 q01/q99 均为 null，首次启动全部崩溃（`ValueError: quantile stats must be provided`），从 westd-45947 复制完整版后重启成功

---
