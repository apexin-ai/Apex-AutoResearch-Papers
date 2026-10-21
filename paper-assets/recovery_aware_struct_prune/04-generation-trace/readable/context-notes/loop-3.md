# director / loop_3.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`785f9b94ec02e8bd51ca.json`](../../sessions/78/785f9b94ec02e8bd51ca.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T17:33:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-23072 的 cuda:0 和 cuda:1（2× RTX PRO 6000 96G），约束 C001
- 模型/数据/checkpoint 必须放 `/root/autodl-tmp/`，根分区只有 ~30G
- grpo_standard_20 不能手动杀——让 RewardDesertCallback 自然触发是实验证据（D006 决策）
- MLP 总参数量相等（395,232）已被 Reviewer 逐层验证，不要质疑这个结论

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com)，用户 root
- 工作目录：`/root/recovery_aware_struct_prune`
- 模型路径：`/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`（base）
- 剪枝模型：`/root/autodl-tmp/pruned_{rasp,standard}_{20,25}/`（4 个）
- GRPO 输出：`/root/autodl-tmp/recovered_{rasp,standard}_20/`
- 活跃进程：
  - GPU 0: grpo_rasp_20 (PID 221271), 62.9GB VRAM, 95% util
  - GPU 1: grpo_standard_20 (PID 221911), 13.3GB VRAM, 94% util
- Cron 监控：120s 轮询，进程退出自动回调 Agent
- 磁盘：autodl-tmp 剩余 ~190GB（Qwen3.5-9B 已删）
- W&B / Git：未配置

### 3. 📊 当前状态
GRPO 双 GPU 恢复对比正在运行（MVP 关键路径）：
- mvp_rasp_pipeline_v4 (PREPARING in registry)：20% sparsity，RASP 29% vs Standard 1% post-prune accuracy
- grpo_rasp_20 on cuda:0：29% 起点，GRPO 学习信号充足，预计 6-9h（~明早凌晨）
- grpo_standard_20 on cuda:1：1% 起点，RewardDesertCallback 预计 1-2h 内触发

等待中：
- Cron 回调：grpo_standard_20 RewardDesertCallback 触发 → Agent 自动派 Worker 跑 25% eval 串行链
- Cron 回调：grpo_rasp_20 完成 → Agent 回调，MVP 判定

25% eval 缺失：standard_25 在 72/100 处死亡，rasp_25 从未启动。等 GPU 1 释放后补跑。

### 4. 📋 待办
- grpo_standard_20 RewardDesertCallback 触发 → 记录触发 step/reward/loss → GPU 1 跑 standard_25 + rasp_25 eval 串行链（~30min）→ 收集 threshold effect 数据
- grpo_rasp_20 完成 → 读 post-recovery accuracy → 与 post-prune 29% 对比 → MVP pass/fail 判定
- MVP pass（recovery 显著提升）→ complete_mvp() → 进入 research 阶段 → 写 paper_framing.md + experiment_plan.yaml → dream_simulate
- MVP fail（recovery 无显著提升）→ 评估 Contingency（pivot 到 benchmark 交互研究）
- 25% eval 完成 → 与 20% 数据对比，分析 sparsity threshold effect

### 5. 🎯 战略上下文
- 项目核心：RASP 用 CKA functional overlap 指导结构化剪枝，保护 RLVR 可恢复性
- 决策链：D001(MLP-only ok) → D002(GRPO 无信号，需 SFT warmup) → D003(暂缓 SFT，先审计代码) → D004(min_keep_mlp=4 bug 修复) → D005(35% 太激进，降到 20%/25%) → D006(20% Scenario B 确认，GRPO 双 GPU 启动)
- **Scenario B 是最强叙事**：RASP 不仅预测 recoverability，pruning 本身就保护推理能力（29% vs 1%，同等参数量）。如果 GRPO 进一步拉大差距，paper 更强；如果 Standard GRPO 完全失败（RewardDesertCallback），这本身就是最强证据
- 易错点：v3 被标记为 negative 但假设未被 falsify——35% 对蒸馏模型太激进，不是方法问题。不要因为 v1-v3 失败而对 RASP 假设失去信心
- 目标会议：EMNLP 2026 ARR May 25（距今 11 天）
- 新颖性已验证：无竞品做 pruning×RLVR recovery 交互研究，核心 gap 成立


---
