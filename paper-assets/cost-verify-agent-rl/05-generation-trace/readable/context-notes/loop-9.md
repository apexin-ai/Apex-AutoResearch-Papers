# director / loop_9.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`d9939e8a68b50db19138.json`](../../sessions/d9/d9939e8a68b50db19138.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-15T20:17:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 bjb1-17606 的 cuda:0 + cuda:1（2× RTX PRO 6000 Blackwell 98GB），不得使用其他设备
- exp027 正在训练中（PID 789790），任何操作不得中断该进程
- exp027 早停条件（D041）：step 10 train success ≤ 12% → 终止
- MVP 判定以 val success 为准（不是 train success），阈值 20%（D037）
- paper_framing.md claim 强度标注为 "target: X"（当前零证据，不得标为已建立）

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606，工作目录 `/root/runs/cost-verify-agent-rl/`
- 代码仓库：`/root/autodl-tmp/verl-agent/`（RAGEN 框架）
- Python：conda base `/root/miniconda3/bin/python`
- 模型：Qwen3-1.7B（路径在 exp027 config 中）
- W&B：run y7jiibqk（metrics 有延迟但最终到达，非丢失）
- exp027 活跃进程：PID 789790，tmux session `exp027_stable_grpo`，双卡满载
- Ray worker stdout（唯一实时指标源）：`/root/autodl-tmp/tmp/ray/session_2026-05-15_22-33-13_032304_789790/logs/worker-...-793046.out`
- 主日志 `/root/runs/cost-verify-agent-rl/exp027_stable_grpo.log` 在计算密集期停更，不可靠
- eval_checkpoint.py 已修复格式对齐（Reviewer PASS），可用于 step 5 checkpoint 评估

### 3. 📊 当前状态
**刚完成**：D041（Plan D 升级）、D042/D043（recipe gap 诊断优先级最高）、experiment_plan.yaml（21 个实验，标准路径）、paper_framing.md（3 claims, cost-efficiency story）、method_draft.md 骨架、ARES 调研、GiGPO 可行性评估、literature_map 引用修正

**RUNNING**：exp027_stable_grpo — step 3 完成（绿区：success=10.16%, KL=0.248），step 4 预计 ~04:15 UTC，step 5 val 预计 ~05:30 UTC，step 10 val 预计 ~16:00 UTC 05/16

**活跃 Worker**：
- GiGPO 代码集成 Worker（SSH，从 verl-agent 移植 4 函数到 RAGEN）
- Recipe Gap 诊断 Worker（SSH+Web，6 维度对比 exp027 vs GiGPO/Self-Guide 论文）

**等待中**：两个 Worker 回调 + exp027 step 4/5 cron 回调

### 4. 📋 待办
- Recipe Gap Worker 回调 → 分析根因（SFT 起点？训练迭代数定义？环境配置？），决定是修 recipe 还是换算法
- GiGPO Worker 回调 → Reviewer 审查集成代码质量，准备 exp028 config
- exp027 step 5 val 出结果 → 如 val ≥ 20% → complete_mvp()；如 10-20% → 继续到 step 10；如 < 10% → 评估是否提前终止
- exp027 step 10 train ≤ 12% → 终止 exp027，启动 exp028（GiGPO 或 recipe-fixed GRPO）
- step 5 val 后 → 评估 GPU 扩容需求（最小论文 534 GPU-h，当前 2 卡需 114 天），向 Manager 申请
- Method draft 低优先级修正：confirmatory → "prior work suggests..."，Self-Guide 节标 "proposed extension"

### 5. 🎯 战略上下文
**决策链**：D037（MVP 阈值 20%）→ D039（cost-efficiency framing）→ D040（三层 KL 判定框架）→ D041（sparse reward 是瓶颈，Plan D GiGPO 升级）→ D042/D043（recipe gap 62pp 才是根本问题）

**核心发现**：参考论文 GRPO baseline 72-73%，我们 10%。差距在 recipe 不在算法。GiGPO 有增量价值但不解决根因。Recipe gap 诊断结果将决定下一步是调 recipe（可能最简单）还是换算法（可能不够）。

**最容易判断错的事**：
- 不要因为 GiGPO "+13pp" 就期望从 10% 跳到 23%——那个 +13pp 是 72.8% 基础上的，不能外推
- exp027 train success 35.94%@step1 是 exploration spike 不是学习成果，真实水平在 ~10%
- cost-efficiency story 前提是 baseline ≥ 50%，即使 MVP 20% pass 也距论文门槛很远
- pass@16 从 100%→62.5%→50% 持续下滑，如跌破 50% 进黄区
- ARES 对比必须用 SFT+GRPO 全流程（不是 SFT-only），否则审稿人攻击公平性


---
