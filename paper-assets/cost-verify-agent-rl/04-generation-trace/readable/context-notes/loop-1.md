# director / loop_1.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`9806a1906394875cb536.json`](../../sessions/98/9806a1906394875cb536.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T21:43:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1 @ bjb1-17606（constraint C001，共享服务器有其他项目残留）
- 模型必须是 Qwen3-1.7B **base**（不是 Instruct）——Self-Guide 论文证明 base 可行，之前误判为需要 Instruct 已纠正（D002 作废）
- RAGEN 框架必须启用 prompt 截断（max_prompt_length=4096），否则 50-turn ALFWorld 必崩（已连崩 3 次：exp_001/exp_002 均因此失败）
- 训练配置必须匹配 Self-Guide 论文：128 traj/step（env_groups=16 × group_size=8）、100 steps、response_length=1024、max_turn=50

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-17606 (connect.bjb1.seetacloud.com:17606)，account: root
- GPU：2× RTX PRO 6000 Blackwell 94GB，CUDA 12.8，Driver 590.44.01
- 工作目录：/root/cost-verify-agent-rl/RAGEN/
- Python：/root/miniconda3/bin/python (conda base)，PyTorch 2.10.0+cu128
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-1.7B/ (symlink /root/cost-verify-agent-rl/models/Qwen3-1.7B)
- ALFWorld 数据：/root/autodl-tmp/alfworld/（ALFWORLD_DATA 需在启动时 export）
- 活跃进程：exp003 (PID 157852, tmux=exp003, cuda:0+1)，100 步训练，刚启动
- Phase B 代码：/root/cost-verify-agent-rl/RAGEN/ragen/biavr/（4 模块，61 tests passed）
- wandb 未配置，console-only 日志：~/runs/cost-verify-agent-rl/

### 3. 📊 当前状态
exp003（Phase A: always-on self-guidance baseline）刚启动正式训练，100 GRPO steps，预估 ~2.5 天。初始 validation 显示 invalid_action=73.75%（vs 之前 96%），配置方向正确。

Registry 状态：
- exp003: RUNNING（Phase A baseline，100 steps）
- exp_001, exp_001b, exp_002: DONE/failed（prompt 长度崩溃 + bootstrap 失败）
- 4 个 dry-run 僵尸条目（PREPARING），需清理

Phase B 代码（biavr 模块）已完成并集成到 RAGEN 流水线，但 a_pre greedy forward pass 未接 vLLM engine（可用纯 budget penalty 模式先跑）。

Reviewer 警告：exp003 未设 RAY_DISABLE_DASHBOARD_AGENT=1，可能复现 Ray dashboard_agent 崩溃。

### 4. 📋 待办
- exp003 完成 step 1-2 无崩溃 → prompt 截断确认有效，放心等 step 20 eval（~12h）
- exp003 Ray dashboard_agent 崩溃 → 加 RAY_DISABLE_DASHBOARD_AGENT=1 重启
- exp003 step 20 eval success ≥ 10% → bootstrap 已解决，继续跑完 100 步
- exp003 step 20 eval success = 0% 且 advantages ≈ 0 → kill，重新诊断（但根据初始 invalid_action 74% 改善，大概率不会）
- exp003 完成 100 步 → gate check：PASS ≥ 76%（Self-Guide 报 81.3%），FAIL < 60%
- Phase A PASS → 用 checkpoint 启动 Phase B（B-IAVR selective verification，β=0.3）
- Phase A FAIL → 诊断原因，可能需要调参或换框架

### 5. 🎯 战略上下文
- 项目核心：B-IAVR 用行为信号（action 是否因 self-guidance 改变）训练 agent 选择性验证。MVP 分两阶段：Phase A 复现 Self-Guide baseline → Phase B 验证 B-IAVR
- D001: MVP 选 ALFWorld + Qwen3-1.7B 单环境验证
- D002: 全量微调（非 LoRA）——但这是基于"匹配 Self-Guide"的判断，Self-Guide 论文调研确认 base model + GRPO 直接训练可行
- **最大风险**：impact 偏低（reviewer 3/5），10-17% token reduction 实际省量有限。Research 阶段需想办法提升
- **易踩的坑**：(1) 不要再试换 Instruct 模型——已证明 base + 大 batch 是正确路径；(2) RAGEN 和 verl-agent 有框架差异（prompt 格式、截断机制、reward 结构），不能假设 Self-Guide 配置直接搬过来就能用；(3) exp003 step 耗时未校准（128 traj 比之前 16 traj 慢很多），2.5 天是粗估
- 目标会议：EMNLP 2026（ARR）/ AAAI 2027 / ICLR 2027


---
