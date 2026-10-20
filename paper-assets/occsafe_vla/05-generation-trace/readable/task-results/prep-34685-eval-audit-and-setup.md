# prep 34685 eval audit and setup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_34685_eval_audit_and_setup_20260527T152831_result.json`
- **Structured JSON:** [`71143c24072f9f13a0d6.json`](../../sessions/71/71143c24072f9f13a0d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。汇报如下：

---

## 1. 34685 Checkpoint 审查结果

**34685 上没有可立即 eval 的 checkpoint。** 所有有数据的 checkpoint 均已 eval 完毕：

| Checkpoint | Size | Eval Status | TSR | CAR |
|---|---|---|---|---|
| cutoff_25k_s1_v2 | 30G | DONE | 0.940 | 0.788 |
| detach_bn_v2_s0 | 15G | DONE | 0.870 | 0.774 |
| detach_bn_v2_s1 | 15G | DONE | 0.926 | 0.736 |
| detach_bn_v2_s2 | 15G | DONE | 0.914 | 0.762 |
| detach_ln_s3 | 30G | DONE | 0.886 | 0.802 |
| full_occ_bn_v2_s1 | 15G | DONE | 0.854 | 0.654 |
| vanilla_v2_s1 | 30G | DONE | 0.908 | 0.748 |
| vanilla_v2_s2 | 30G | DONE | 0.844 | 0.720 |
| **mvp_occ_s4** | 30G | **刚完成 (22:52 UTC)** | **0.910** | **0.754** |
| detach_ln_v2_s2 | 4KB | 训练中 (cuda:0) | — | — |
| full_occ_ln_v2_s0c | 4KB | 空目录 | — | — |

## 2. 紧急发现

- **mvp_occ_s4_eval 已完成**，34685:cuda:3 已释放。结果: TSR=0.910, CAR=0.754，保存在 `/root/occsafe_vla/artifacts/safelibero_libero_spatial_20260527_220945.json`
- **full_occ_ln_v2_s1c_r2 和 full_occ_ln_v2_s2_r2 不存在** — 10894 上无 log、无 checkpoint、无进程、无 exit file。Registry 标记 RUNNING 但实际从未启动。
- **10894 cuda:0/1 也空闲**（不是在跑 _r2 训练）
- **34685 当前: cuda:0 训练中, cuda:1/2/3 全空闲**

## 3. 10894 Eval 环境 — 就绪

- evaluate_safelibero.py ✅
- conda env occsafe (libero + mujoco + robosuite) ✅
- libero_spatial 数据集 (10 tasks) ✅ `/root/autodl-tmp/libero_datasets/libero_spatial/`
- 10894 上有两个 **完整但未 eval 的 checkpoint**:
  - `full_occ_ln_v2_s1c` (45G, 有 50k checkpoint)
  - `full_occ_ln_v2_s2` (45G, 有 50k checkpoint)

## 4. 可立即执行的 Eval 命令（10894）

**full_occ_ln_v2_s1c_eval (cuda:0):**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl python3 vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c--50000_chkpt \
  --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

**full_occ_ln_v2_s2_eval (cuda:1):**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl python3 vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2--50000_chkpt \
  --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

## 5. 34685 cuda:1/2/3 利用建议

34685 所有本地 checkpoint 已 eval，无法直接跑新 eval。选项：

1. **SCP 10894 上的 checkpoint 到 34685 跑 eval**（每个 ~15GB，但不如直接在 10894 本地 eval 高效）
2. **在 34685 启动新训练任务**（需要 Director 指定实验）
3. **上报 Director 决策** — _r2 实验从未启动，10894:cuda:0/1 和 34685:cuda:1/2/3 共 5 张卡空闲，需要重新分配任务

建议优先在 **10894:cuda:0/1 立即启动 full_occ_ln_v2_s1c_eval 和 full_occ_ln_v2_s2_eval**，同时等 Director 对 34685 空闲卡下达新指令。

---
