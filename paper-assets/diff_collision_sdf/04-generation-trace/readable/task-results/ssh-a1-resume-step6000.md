# ssh a1 resume step6000

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a1_resume_step6000_20260520T071817_result.json`
- **Structured JSON:** [`f16306e7d80f6d258320.json`](../../sessions/f1/f16306e7d80f6d258320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**A1 恢复训练已成功启动**
- **PID**: 181881 | **tmux**: `a1_sdf_spatial_bowl_s0_v3`
- **GPU**: cuda:3（13.4GB VRAM 占用中）
- **Step**: 从 6001 正确接续，当前 ~6072，loss ~0.27
- **Phase 2 已激活**: lr=2.33e-05，LoRA 已解冻
- **save_interval**: 2000（原 500）
- **Registry**: RUNNING | **Cron**: 已注册（120s 轮询）

排障过程中修复了 3 个问题：
1. tmux 未安装 → 已装
2. wandb API key 缺失 → 设 `WANDB_MODE=disabled`（与其他实验一致）
3. conda env 错误（`base` 缺依赖）→ 改用 `libero` 环境 + `source /etc/network_turbo` 启用网络代理

---
