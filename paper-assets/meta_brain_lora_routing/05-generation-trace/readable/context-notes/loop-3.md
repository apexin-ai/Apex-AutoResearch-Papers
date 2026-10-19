# agent / loop_3.md

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`bfdd02a8ace38652437f.json`](../../sessions/bf/bfdd02a8ace38652437f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-16T20:40:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34142 的 cuda:0, cuda:1, cuda:2, cuda:3（共 4 张 RTX PRO 6000 96GB）
- Base checkpoint 已切换为 pi05_libero（D010），不再用 pi0_base
- v2 系列训练用的是 LIBERO 标准 demo 数据（D008 决策），不是 π₀ rollout
- Router 架构锁定：PaliGemma layer 6, first-token pooling（D006）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34142，4× RTX PRO 6000 96GB
- 工作目录：未在本 session 内 SSH 确认（上一轮 Worker 操作的）
- Python/conda：需 Worker SSH 探查确认（大概率 conda base 或 venv）
- 模型路径：checkpoints 在 `/root/autodl-tmp/checkpoints/` 下（physical 确认路径 `/root/autodl-tmp/checkpoints/v2_lora_physical_r16/v2lora_physical_r16/final`）
- Phase 1 checkpoints：`/root/meta_brain_lora_routing/checkpoints/lora_{visual,physical,universal_r16,universal_r48}/final`
- 活跃进程：无（4 GPU 全空闲）
- Cron：reconcile 返回 0 个活跃 cron

### 3. 📊 当前状态
刚收到 CRON 回调：v2_lora_spatial_r16 进程异常退出。

**已完成的动作**：
- Session-start 初始化（registry + reconcile + report + roadmap）
- 派 Worker `worker_diagnose_v2_lora_failed_20260516T155337` SSH 诊断两个失败实验
- 向 Director 汇报了 4 GPU 空闲 + 2/4 失败的状态

**Registry 关键状态**：
- v2_lora_visual_r16: DONE/success (loss 0.7035)
- v2_lora_physical_r16: DONE/success (loss 0.6776)
- v2_lora_spatial_r16: DONE/failed (EXIT_CODE=129, SIGHUP)
- v2_lora_universal_r16: DONE/failed (EXIT_CODE=143, SIGTERM)
- phase_b5_activation_collection: PREPARING
- eval_no_routing: PREPARING
- phase1_lora_spatial: ALLOCATED (遗留，可能已过时)

**等待中**：
- Worker 诊断回调（查 log + dmesg + tmux，确认失败根因）

### 4. 📋 待办
- 诊断 Worker 回调到达 → 根据根因决定：若 OOM 则调参重跑；若误杀/tmux 断开则直接重跑（优先从 checkpoint 恢复）
- 重跑确认后 → 立即在 4 GPU 上重启 spatial + universal 训练
- 4 路 v2 全部 success 后 → 进入 Phase 1 assembly + eval（plan_003），组装 routing pipeline 做 LIBERO eval
- rank-48 universal (plan_013) 还未跑 v2 版本，需要排期

### 5. 🎯 战略上下文
- 项目目标：CoRL 2026（Abstract DDL 2026-05-26，仅剩 10 天）
- 核心方向：Perturbation-Adaptive LoRA Routing——从 π₀ 内部激活诊断扰动类型，路由到专用 LoRA expert
- D010 是关键转折：从 pi0_base 切到 pi05_libero，所有 v2 训练基于此
- v2 的 loss（0.67-0.70）远高于 phase1（0.01），这是正常的——v2 用真实 demo 数据而非 rollout，任务难度不同
- 易错点：phase1 系列实验和 v2 系列不能直接比 loss，它们的数据分布完全不同
- 两个成功实验证明代码和配置没问题，失败大概率是外部因素（tmux/OOM），重跑成功率高


---
