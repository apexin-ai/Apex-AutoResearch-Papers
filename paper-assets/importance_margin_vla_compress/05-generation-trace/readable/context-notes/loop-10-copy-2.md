# agent / loop_10.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`a2f74de1a8634e84d9d7.json`](../../sessions/a2/a2f74de1a8634e84d9d7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-21T02:46:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 14 张：westd-27271:0/1, cqa1-33015:0/1/2/3, westd-41074:0/1/2/3, westd-38929:0/1/2/3。白名单外的 GPU 即使 Director 指令也必须 push back
- westd-27271 用 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不存在 .venv
- 所有 AutoDL 服务器 pip/HF 操作前必须 `source /etc/network_turbo` + 设 SSL 证书环境变量
- CoRL 2026 deadline：abstract May 26（5 天），paper May 29（8 天）—— 时间极紧，每张空闲 GPU 都是浪费

### 2. 🖥️ 基础设施快照
- **westd-27271**: 工作目录 `/root/autodl-tmp/importance_margin_vla_compress/`，Python `/root/miniconda3/bin/python`，conda base。HF cache `/root/autodl-tmp/.hf_cache`。磁盘 root ~819G/879G free，/autodl-pub 5.3T/7.3T free
- **westd-41074**: 同上路径结构。M=96 PID 68539 (cuda:2)，M=64 PID 68852 (cuda:3)。cuda:1 有未识别 PID 125816 待清理
- **cqa1-33015**: 4 卡全空闲。/autodl-pub 仅 395G/7T free (95% used) ⚠️，/autodl-pub/data 1.5T/4T free
- **westd-38929**: 4 卡空闲（X-VLA eval sweep Batch 1 已完成，Batch 2 状态不明）。磁盘 root 645G/879G free
- **活跃 cron**: train_openvla_sc_m96_seed42_v3, train_openvla_sc_m64_seed42_v3（均 westd-41074）
- **Worker**: `worker_ops_c4ext-eval-cqa1-retry_20260520T102758`（running），`worker_diagnose_train_openvla_sc_m32_vtconly_seed42_20260520T104406`（刚派出）

### 3. 📊 当前状态
**刚做完**：诊断 train_openvla_sc_m32_vtconly_seed42 失败原因 = 磁盘写入失败 @ step 20000 checkpoint save。已更新 registry、发飞书卡片、汇报 Director、派 Worker 修复重启。

**RUNNING**:
- `train_openvla_sc_m96_seed42_v3` (westd-41074:2) — OpenVLA VTC M=96, step ~2000+
- `train_openvla_sc_m64_seed42_v3` (westd-41074:3) — OpenVLA VTC M=64, step ~2450+

**等待回调**:
- Worker `diagnose:train_openvla_sc_m32_vtconly_seed42` — 检查 westd-27271 磁盘 + 清理 + resume M=32 训练
- Worker `ops:c4ext-eval-cqa1-retry` — C4-ext 20K eval 重试（cqa1 上）
- westd-38929 X-VLA Batch 2 状态未知（Batch 1 k=0.7 接近完成时 ROADMAP 记录的）

**⚠️ 严重问题**：14 张 GPU 仅 2 张在跑，12 张空闲 = 失职。westd-38929 4 卡和 cqa1 4 卡状态需要立即确认并分配任务。

### 4. 📋 待办（条件触发式）
- M=32 修复 Worker 回调 → 确认 resume 成功，更新 registry RUNNING + spec
- C4-ext eval Worker 回调 → 读结果，成功则填 C4-ext 数据点，失败则再诊断
- M=96/M=64 cron 完成回调 → 按 on-experiment-done 流程分析 + eval
- westd-38929 X-VLA Batch 2 状态确认 → 如果没在跑，立即重启 sweep (k=0.5/0.3/0.2/0.1)
- **主动**: 12 张空闲 GPU 必须填满——P0 确认 westd-38929 X-VLA 状态，P1 cqa1 分配 C4-ext eval 或其他待执行实验，P2 westd-41074:0/1 和 westd-27271:0 分配任务
- Director 决策后 → 如批准新实验方向，立即并行铺开

### 5. 🎯 战略上下文
**核心叙事**: Vision connector 架构决定 VLA token 可压缩性。3 类 taxonomy: linear (immune) → MLP (graded) → pixel-shuffle (catastrophic)。Diagnose-then-Compress 框架: Entropy+CV 复合诊断 (D104) + VTR 通用压缩。

**Claims 进度**: C1-C4 ✅, C4-ext 🟡 (最关键 pending: OpenVLA M-sweep + 20K eval), Diagnostic ✅ (X-VLA CV 还差一个数据点)

**关键决策链**: D104 解决了 D103 的诊断指标问题（entropy 单独不够，需 +CV）; D105 确认 SmolVLA M-curve 平坦; D106 X-VLA k=0.7 出现 task-specific 崩塌但暂不改 C3a

**易错点**:
- M=96/M=64 的 v3 版本是从 orphan PID retrack 的，不是从 step 0 重跑——检查 step 进度时注意
- cqa1 磁盘 /autodl-pub 95% used，提交实验前必须检查空间
- westd-41074:1 有不明 PID 125816，清理前先确认不是其他项目的进程
- M=32 失败是磁盘问题不是训练问题——resume 后预期正常收敛，不需要改超参


---
