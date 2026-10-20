# director / loop_1.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`c5fb66d716b0a760af25.json`](../../sessions/c5/c5fb66d716b0a760af25.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T18:33:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（westb-13313 双卡 RTX 5090 32GB）
- plan-011 的 `src/rule_based_keywords.json` 已 pre-register，实验开始后禁止修改（防 p-hacking）
- episode_level_collection.py 的 labeling 逻辑：death episodes (-100) 自动判负，不做 class weighting（D010/D011 决策）
- 1-step counterfactual labeling 已废弃（tie rate 98.2%），不要回退到 per-step forking 方案
- CogRouter/ITP-R 数据引自论文，不自行复现——对比仅做 context reference

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python 环境：需 SSH 确认（aml-train 镜像，大概率 conda base）
- 关键脚本：
  - `src/signal_prescreening.py` — plan-001a 预筛（GPU0 正在跑）
  - `src/phase1_signal.py` — MVP 信号检测
  - `src/episode_level_collection.py` — Plan C 数据收集（已完成，待 dry-run 确认）
  - `src/router_sft_train.py` — plan-002 router SFT（Worker 编写中）
  - `src/rule_based_routing.py` — plan-011 rule-based baseline（Worker 编写中）
  - `src/rule_based_keywords.json` — pre-registered keyword list
- 活跃进程：GPU0 预筛 + GPU1 boil v3（均通过 ssh_execute 启动，非 submit_training_job）
- W&B / Git：未配置

### 3. 📊 当前状态
**刚做完**：paper_framing.md v3 更新（C2 重构为 failure trajectory predictor，Plan C 绕开 oracle circularity），experiment_plan.yaml v4（Plan C labeling），ROADMAP v7。

**Registry 状态**：
- research-prescreening-gpu0: RUNNING — 25 task types 信号预筛，5/25 完成
- research-boil-v3-gpu1: ANALYZING — boil v3 rerun，12/20 episodes 完成，~30min 剩余
- research-cf-pilot-gpu1: PENDING (killed) — K=10 pilot 已取消

**Agent 最后汇报**：GPU 双卡满载，3 个 CPU Worker 在写 router_sft_train.py / rule_based_routing.py / GPU状态检查。boil v3 中间结果各 mode 均大幅优于 MVP（v3 代码效果显著）。

**等待中**：Agent 处理 RESET，新 session 需接收上述状态继续。

### 4. 📋 待办
- boil v3 完成（~30min）→ 分析最终结果（vs MVP 对比表）→ GPU1 加入预筛分担剩余 tasks
- GPU0 预筛完成（~8h total）→ 筛出 signal-positive tasks → 双卡启动 plan-001b（Plan C episode-level collection）
- plan-001b 完成 → plan-002 (router SFT, cuda:0) + plan-004 (explicit vs implicit, cuda:1) 双卡并行
- plan-003 完成 → plan-011 (rule-based baseline) + plan-012 (death decomposition) 分析
- router_sft_train.py / rule_based_routing.py Worker 完成 → dry-run 验证
- plan-001b 完成后立即统计 label 分布——如果 det labels > 85%，在论文中诚实报告
- C1 "selective > unconditional" 关键指标：plan-003 的 simulator invocation ratio（用 60% simulator calls 达到 90% always-det 效果 = selective routing 的实用价值）

### 5. 🎯 战略上下文
**决策链**：D005(MVP PASS) → D008(1-step tie rate 98.2%, labeling 失败) → D010(Plan C episode-level labeling 采用) → D011(C2 重构为 failure trajectory predictor)

**核心 story 演进**：从 "per-step routing decision" 转向 "catastrophic trajectory risk prediction"。Plan C 的三个优势：(1) 绕开 oracle circularity（Dream worst 核心攻击）；(2) safety-aware framing ↔ episode-level labeling 天然匹配；(3) router-as-failure-predictor 比 step-level router 更有 novelty。

**易错点**：
- 不要回退到 per-step labeling 或 K-step forking——已证明不可行/太贵
- plan-001a 的 step-level data 已确认可复用（observation + action + score 都有），plan-001b 只需补 15 episodes/task（001a 已有 5 ep）
- boil v3 registry 状态显示 ANALYZING（不是 RUNNING），因为用了 ssh_execute 而非 submit_training_job，cron 检测到 wrapper PID exit 误标了
- Dream 审稿：best 4/6, median 3/6, worst 2/6——容错率低，C1 依赖 plan-003 结果
- DDL: 2026-05-25（剩 12 天），关键路径 ~2.3 天实验 + ~3 天写作


---
