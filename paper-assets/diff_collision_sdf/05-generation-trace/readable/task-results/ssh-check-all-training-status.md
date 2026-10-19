# ssh check all training status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_training_status_20260520T081906_result.json`
- **Structured JSON:** [`d1adbc46907135a098ba.json`](../../sessions/d1/d1adbc46907135a098ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

| 服务器 | GPU | 实验 | Step/Total | Loss | Speed(s/it) | VRAM | 进程状态 |
|--------|-----|------|-----------|------|-------------|------|---------|
| westd-35807 | cuda:0 | baseline_spatial_bowl_s0_v2 | 9576/30000 (32%) | 0.0116 | ~3.5 | 37.4/95.6 GB | ✅ 运行 9h44m |
| westd-35807 | cuda:1 | baseline_spatial_bowl_s1_v2 | 9859/30000 (33%) | 0.0109 | ~3.5 | 37.4/95.6 GB | ✅ 运行 9h56m |
| westd-35807 | cuda:2 | baseline_object_pudding_s0_v2 | 9928/30000 (33%) | 0.0093 | ~3.5 | 37.4/95.6 GB | ✅ 运行 9h55m |
| westd-35807 | cuda:3 | a1_sdf_spatial_bowl_s0_v3 | 6800/30000 (23%) | 0.2371 | ~3.5 | 13.1/95.6 GB | ⚠️ **异常** |
| westd-45947 | cuda:0 | a3_gradient_spatial_bowl_s0 | 56/30000 (0.2%) | 0.2799 | ~11-16 | 16.5/95.6 GB | ✅ 刚启动 19m |
| westd-45947 | cuda:1 | a3_gradient_object_pudding_s0 | 2558/30000 (8.5%) | 0.2140 | ~11-16 | 16.5/95.6 GB | ✅ 从ckpt恢复 19m |

### 磁盘使用
- **westd-35807**: 144G/350G (42%)
- **westd-45947**: 22G/250G (9%)

### 关键发现

1. **3 个 baseline 正常运行**，进度 ~32-33%，loss 已降到 0.01 左右，速度稳定 ~3.5s/it

2. **a1_sdf_spatial_bowl_s0_v3 异常** — PID 181881 的 CPU=0%、RSS=3.5KB，基本是死进程。GPU 3 利用率 0%，VRAM 仅 13GB（远低于 baseline 的 37GB）。日志停在 step 6800，loss 仍在 0.24 高位。**该实验很可能已崩溃/退出，需要排查重启。**

3. **westd-45947 两个 a3_gradient 实验刚启动约 19 分钟**。a3_gradient_object_pudding_s0 从 step 2500 的 checkpoint 恢复（当前 2558），a3_gradient_spatial_bowl_s0 从头开始（当前 step 56）。速度 ~11-16 s/it，比 baseline 慢约 3-4 倍（梯度方法计算量更大）。按此速度完成 30K 步需约 **4-6 天**。

---
