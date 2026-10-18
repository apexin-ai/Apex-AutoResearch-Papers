# agent / loop_9.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`a43a63fec5c69520c1f2.json`](../../sessions/a4/a43a63fec5c69520c1f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-18T00:56:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-27271:cuda:0,1 + cqa1-33015:cuda:0,1,2,3（共 6 张）
- cqa1 磁盘 /autodl-pub 已用 95%（375GB 剩余），提交实验前必须预检空间
- westd 是 48GB RTX PRO 6000，OpenVLA 7B 只能在 westd 跑（需 ~40GB VRAM）
- SmolVLA 实验用 cqa1（24GB RTX 4090）
- libero_fullft_batch64 系列已被 Director 永久 kill（D066），不再重启

### 2. 🖥️ 基础设施快照
- **cqa1-33015**: 工作目录 ~/runs/importance_margin_vla_compress/，4× RTX 4090 24GB
- **westd-27271**: 工作目录 ~/runs/importance_margin_vla_compress/，2× RTX PRO 6000 48GB
- 预置镜像：`aml-train`（两台都是，连接后 `detect_image` 确认）
- SmolVLA checkpoint: cqa1 上 checkpoints/ 目录（100K Full FT seed=42 是主 baseline）
- LIBERO 数据: cqa1 上已有（具体路径需 Worker SSH 确认）
- W&B: 项目 importance_margin_vla_compress（离线 run 为主）
- 活跃 Worker: 
  - worker_ops_download_pi05: 下载 Pi0.5 模型
  - worker_ops_westd_cleanup_and_download: westd 清理+下载

### 3. 📊 当前状态
刚处理 libero_fullft_batch64_v2 的 cron 退出回调，确认是 D066 intentional kill（SIGKILL）。Registry 已更新为 DONE(killed)。

- **RUNNING**: 无（6 张 GPU 全部空闲）
- **PREPARING**: sanity_acis_prune, eval_random_prune_baseline, eval_k07_bypass, plan_005_formal_bound, eval_sim_success_rate, imm_two_stage_v9（均为历史残留，不再执行）
- **等待中**: 2 个 CPU Worker 在下载 Pi0.5 模型和清理 westd，完成后应有回调
- **libero_full_ft_baseline**: ANALYZING 状态，SR 数据已全（object=36%, spatial=48%, goal=63%, overall=49%），可关闭

### 4. 📋 待办
- Pi0.5 下载 Worker 完成回调 → 确认模型就位 → 向 Director 汇报可开始 Pi0.5 跨模型验证
- westd cleanup Worker 完成回调 → 确认空间 → 为 OpenVLA 7B 实验准备环境
- Director 给出 smart compression 方案设计决策 → spawn Worker 实现代码 + 训练
- OpenVLA 环境就绪 → naive pruning cliff-edge 验证（跨模型）
- libero_full_ft_baseline 可关为 DONE(success)（数据完备，只是状态未更新）

### 5. 🎯 战略上下文
- **D066 方向调整**：从 pure negative results 扩展为"跨模型 cliff-edge 验证 + smart token compression"
- **核心已证实结论**：SmolVLA 对 vision token pruning 零容忍（k=0.9 仍 0% SR），无论 ACIS/random/true-removal/merge 全部 0%。这是 motivation，不是终点。
- **新方向三条腿**：(1) OpenVLA/Pi0 跨模型验证 cliff-edge 是否普遍 (2) smart compression（Q-Former/Perceiver/VLA-IAP style，不硬删 token）(3) 论文 framing 待 smart compression 结果定
- **关键对照**: VLA-IAP (2026-03) 在 OpenVLA 上 97.8% SR + 1.54x 加速（用 geometric prior + dynamic scheduling）
- **DDL**: CoRL 2026 Abstract May 26 / Paper May 29（距今 8/11 天）
- **易错点**: 
  - Stage2 IMM 训练会摧毁 expert weights（bypass SR=0%），这条路已死，不要再试
  - 之前 eval_stage1_only 44.8% SR 是假阳性（pruning bug 未执行），修复后 0%
  - westd-27271 曾经断联过，提交长实验前确认服务器稳定性


---
