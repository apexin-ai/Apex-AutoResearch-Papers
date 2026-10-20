# director / loop_3.md

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`fa9d8edaefcffbb53ebd.json`](../../sessions/fa/fa9d8edaefcffbb53ebd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T21:18:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 autodl-rtx6000pro:cuda:0（单卡项目，gpu_ids=[0]）
- 代码路径 /root/autodl-tmp/crdd，模型/数据不能放根分区
- MVP 阶段不能启动完整研究规划、不能调 dream_simulate、不能写 paper_framing.md
- Pipeline 进程用 nohup 后台跑，不要在 SSH session 前台阻塞

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtx6000pro (connect.westd.seetacloud.com) + westd-32608
- 工作目录：/root/autodl-tmp/crdd
- Python：conda base 环境 /root/miniconda3/bin/python
- HF_HOME：/root/autodl-tmp/.hf_cache
- 活跃进程：PID 47964（v4 pipeline，应已完成 204/204 样本）
- 无 wandb 配置，无 tmux session

### 3. 📊 当前状态
- v4 pipeline (mvp_pipeline_004) 跑 204 样本，3小时前在 127/204（62.3%），按速率应已完成
- 我刚派 Agent 去确认 pipeline 完成 + 跑 evaluate_mvp.py + repair_only.py（消息已入队，Agent 刚重置待启动）
- Registry: mvp_pipeline_004 ANALYZING(success), mvp_baseline_001 DONE(success), 其余 negative/killed
- 126 样本子集已 5/5 PASS（C1 35.9%, C2 88.1%, C3/C4/C5 均过阈值），等 204 全量确认

### 4. 📋 待办
- Agent 汇报 204 样本 evaluate_mvp.py 结果 → 5/5 PASS 则 complete_mvp() 进 research 阶段
- 204 样本某指标 FAIL → 分析失败样本分布，决定是调 pipeline 还是放宽阈值
- complete_mvp 后 → 立即启动 post-mvp-kickoff skill（paper_framing.md → experiment_plan.yaml → dream_simulate → ROADMAP）
- repair_only.py 结果 → 记录修复成功率作为论文 claim 支撑数据

### 5. 🎯 战略上下文
- 核心假设：不同表征空间（token/logit/attention）的 disagreement 可以诊断模型错误类型
- MVP 验证的是 pipeline 可行性：能否自动检测 disagreement 并生成有意义的诊断
- 126 样本已 5/5 PASS 是强正信号，204 全量大概率通过
- 易错：evaluate_mvp.py 是权威评估脚本，不要自己手算指标替代它
- 决策链：D001-D008 见 decisions.yaml，关键转折是 v3→v4 引入 truncation detection + thinking-off retry 解决了截断问题


---
