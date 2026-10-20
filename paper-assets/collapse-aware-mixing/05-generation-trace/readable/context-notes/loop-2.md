# director / loop_2.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`26b9860ea070c3bac3d8.json`](../../sessions/26/26b9860ea070c3bac3d8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-12T18:25:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只用项目配置 `execution.gpu_ids` 白名单内的卡，当前只分配了 1 张（需 `get_project_status` 确认具体 device）
- v5 pipeline 正在跑，不能中断/重启/改参数——等它自然跑完
- 90M tokens_per_generation vs ROADMAP 100M 的差异已确认不影响 MVP 判定，不要因此重跑
- analyze_g0.py holdout 路径已批准修复（改为 `load_dataset("wikitext", "wikitext-103-raw-v1", split="test")`），确认修复已落地再用

### 2. 🖥️ 基础设施快照
- 需要 `get_project_status` + `list_ssh_hosts` 确认服务器名和路径（我的 session 没有直接 SSH 过，都是通过 Agent 操作）
- v5 实验在远程服务器跑，Agent 持有具体 PID/tmux 信息——新 Agent session 启动后让它 `check-training-status` 获取
- 项目本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/`

### 3. 📊 当前状态
- **mvp_pilot_v5** RUNNING：3 代 pipeline（G0→G1→G2），G0 训练完成，G0 评估进行到 6/11 checkpoint 时最后汇报，剩余 G0 评估 + G1 训练评估 + G2 训练评估，总剩余约 5-6h（从上次汇报算起，已过约 3h）
- **analyze_g0.py 修复**：已派 CPU Worker 修 holdout 路径默认值，状态未回报（Agent idle 触发 reset 前未收到完成回调）
- 无等待中的 Cron / Director 决策

### 4. 📋 待办
- v5 pipeline 全部完成 → Agent 汇报结果 → 用 analyze_g0.py 跑 G0 分析 → 综合 3 代数据判断 MVP GO/NO-GO
- MVP 通过（collapse-aware mixing 在多代训练中显示出信号）→ `complete_mvp()` → 进入 research 阶段 → 按 `post-mvp-kickoff` skill 写 paper_framing.md + experiment_plan.yaml + dream_simulate
- MVP 失败 → 分析失败原因，决定 pivot 方向或调整假设重试
- analyze_g0.py 修复完成回调 → 确认改动正确（`load_dataset` 方式），无需进一步操作

### 5. 🎯 战略上下文
- 项目处于 **MVP 验证阶段**，核心假设：collapse-aware mixing 策略能在多代模型蒸馏/合成数据训练中缓解 model collapse
- 之前 v1-v4 都有各种问题（具体见 ROADMAP 和 report.md），v5 是当前 MVP 验证轮次
- paper_framing.md 和 experiment_plan.yaml 都还没创建（MVP 阶段不写），MVP 通过后才启动
- 易错点：不要在 MVP 完成前启动完整研究规划或调 dream_simulate（前置文件不存在会失败）
- 易错点：v5 跑的是 90M tokens/代不是 100M，分析结果时注意这个差异


---
