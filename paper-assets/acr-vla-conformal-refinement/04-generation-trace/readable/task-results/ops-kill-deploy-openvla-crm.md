# ops kill deploy openvla crm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-deploy-openvla-crm_20260520T212816_result.json`
- **Structured JSON:** [`a07d5cecca8d6f7a8e9f.json`](../../sessions/a0/a07d5cecca8d6f7a8e9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CPU 656%，进程在活跃运行中（LIBERO MuJoCo 环境初始化中，不产生日志输出）。进程健康。

---

## 报告

### 1. Kill 确认
- **PID 803103**（bash wrapper 803098）— `norm=0.2 seed54` on cuda:5
- 已 kill，GPU 5 内存从 1989 MiB → 1 MiB

### 2. OpenVLA CRM eval 部署
- **PID 842052**（bash wrapper 842046），cuda:5
- GPU 5 VRAM: **15,663 MiB** / 24,564 MiB
- 注意：原始命令缺少 `--obs_dim 4096`，导致 CRM checkpoint 维度不匹配（checkpoint input_dim=4102 vs 默认 966）。已修正为 `--obs_dim 4096` 重新启动

### 3. 启动日志
- OpenVLA 7B 加载成功（14.1GB GPU mem）
- CRM 加载成功（1,117,702 params, max_correction_norm=0.2）
- 10 LIBERO-Object tasks loaded
- TF/MuJoCo 环境初始化中，CPU 656% 活跃

### 4. Registry 更新
- `eval-obs-only-object-norm02-seed54`: status=DONE, conclusion=killed
- `eval-openvla-crm-object-seed42`: status=RUNNING, spec 已注册

---
