# director / loop_2.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`8535048a5af6e3f96209.json`](../../sessions/85/8535048a5af6e3f96209.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T23:25:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-39279 的 cuda:0 和 cuda:1，共 2 张 RTX PRO 6000 96GB。不可用其他服务器或设备号
- plan_003 消歧已确认 Interpretation B（penalty effect）—— 论文中**不可再声称 "STA 检测 reward hacking"**，只能用观察性表述（D006/D008）
- 50/50 STA 权重已证实有害（prove_rate 退化至 baseline 以下）—— 任何新 exec+STA 实验必须用 plan_005 确定的最优权重，不可用 0.5/0.5
- Dream 审稿明确禁止的措辞：不可说 "Pareto-improving"（prove rate 差异不显著）、不可说 "dense+automatic"（ISR 对 unproved=0，改用 "conditionally dense"）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，SSH connect.westd.seetacloud.com:39279，account root
- 工作目录：/root/solver-trace-ablation
- Python 环境：未确认（Agent 之前做过环境探测但 handoff 缺细节，需 SSH 验证）
- 数据：FOL 数据在 data/proofwriter_fol_*.jsonl；**Prolog 数据不存在**（Reviewer WARNING，阻塞 plan_006）
- GPU 健康数据：stale（get_gpu_health 返回 "no data yet"），需 Agent SSH 确认实际状态
- 活跃进程：plan005-sta-low-s42 应在 cuda:1 上 RUNNING（registry 状态），但已超 3h 未确认实际进程状态

### 3. 📊 当前状态
**我刚做完**：
- Dream dream_20260513T215750 完整分析（best 4/6 Borderline Reject, median 3/6 Weak Reject）
- paper_framing.md 更新：story 从 "STA detects hacking" 转向 "STA as structural metric + proper integration"
- experiment_plan.yaml 新增 plan_013-016（random baseline / downstream validation / curriculum ablation / longer training），plan_006 升级 3 seeds
- ROADMAP 更新，D008 决策记录
- 给 Agent 发了 plan_001 诊断指令（但 Agent 空闲 180min 未响应，触发本次 RESET）

**Registry**：
- RUNNING: plan005-sta-low-s42（STA weight=0.1，cuda:1）—— 实际进程状态未知，需确认
- DONE(failed): plan001-exec-only-s42, -r2, -r3 —— 连续 3 次失败，根因未诊断
- DONE(success): plan003-eval-exec-only-r5（prove_rate=0.32, proved_only_ISR=0.6423）
- 其余 12 个 DONE（4 success, 3 negative, 9 failed，详见 registry）

**等待中**：无。Agent 被 RESET，新 session 需重新派任务。

### 4. 📋 待办
- Agent RESET 完成 → 立即派指令：(1) 确认 plan_005 进程是否还活着 (2) 诊断 plan_001 连续 3 次失败根因 (3) cuda:0 空闲则立即修复 plan_001 并重跑
- plan_005 完成(success) → 分析最优权重 → 用该权重配置 plan_002 和 Prolog exec+STA config → 启动 plan_002
- plan_005 完成(failed) → 诊断失败原因，同时考虑 bonus mode (r = exec × (1 + 0.3 × ISR)) 作为替代
- plan_001 成功 + plan_005 成功 → 有两个 checkpoint，启动 plan_003 正式对比 + plan_013 random baseline + plan_014 downstream validation
- Kill Criteria #1：plan_005 所有权重配比均 exec+STA < exec-only → story 退化为 "STA as monitoring only"
- Kill Criteria #4：plan_001 exec-only 500步 3-seed mean prove_rate < 25% AND slope ≤ 0 → GRPO pipeline 本身有问题
- Prolog 数据准备是非 GPU 任务，可在任何时候并行铺开（Reviewer 已标 WARNING）

### 5. 🎯 战略上下文
- **决策链**：D001(MVP方案) → D002(调整) → D003(fast_isr无效) → D004(exec-sta退化) → D005(因果归因待验证) → D006(hacking claim降级) → D008(Dream确认5个结构性问题+消歧B confirmed)
- **核心结论**：STA 作为度量有效（ISR 区分力 0.6423 vs GT 0.56），作为 reward 需要低权重集成。论文 story 是 "principled structural metric via LOO ablation + calibrated reward integration"，不是 "novel algorithm"
- **最易判断错的事**：plan_003 的 proved_only_ISR=0.6423 是 exec-only checkpoint 的，不是 exec+STA 的。这证明 exec-only 模型天然结构良好，STA reward 是在惩罚而非纠正。不要误读为 "STA 训练提升了 ISR"
- **容易踩的坑**：(1) plan_001 连续失败可能是脚本 bug 或环境问题，不是实验设计问题——先查日志再重跑 (2) Reviewer 报告 Prolog config 仍用 50/50 权重——不要直接用来跑实验 (3) GPU 健康数据 stale，plan_005 可能已完成或已挂，第一件事确认进程状态
- **DDL**：EMNLP ARR 2026-05-25，剩 12 天。Dream median=Weak Reject，需要 random baseline + downstream validation + 3-seed secondary 才有望提到 Weak Accept


---
