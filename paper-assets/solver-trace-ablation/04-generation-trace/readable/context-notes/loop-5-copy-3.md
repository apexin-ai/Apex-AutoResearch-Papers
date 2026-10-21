# reviewer / loop_5.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`608112015ff5c5f3c02d.json`](../../sessions/60/608112015ff5c5f3c02d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T16:25:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1，越界即 critical（C002）
- 所有 Python 进程（含 eval/fix）必须显式 `CUDA_VISIBLE_DEVICES`（C005，2026-05-14 事故）
- 跨 seed ISR 对比只能用 eval_sta.py full STA 结果，禁止引用训练日志 ISR（C004）
- 训练数据必须统一用 `data/train_500_seed42.jsonl`（C001）
- ISR 论文讨论须区分 exec-only low ISR（冗余编码）vs exec+STA high ISR（Goodhart gaming）（C006）
- Claim 2 已定论为 pure negative（D051-D054）：premise-count-matched 后 ISR vs Random = 1.02x，不可再声称 ISR 有结构优势

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 输出目录：`/root/autodl-tmp/outputs/`
- GPU：2 × NVIDIA RTX PRO 6000 Blackwell 96GB
- 活跃进程（截至 handoff 时刻）：
  - PID 858391: plan018-random-b01-s43-r2 训练中（cuda:0，86GB 占用）
  - PID 889385: plan006-prolog-exec-s44 eval_sta.py 运行中（由 run_evals_seq.sh PID 881797 调起）
  - tmux session: `plan006-prolog-exec-s44`
- ⚠️ PID 889385 eval_sta.py 由 run_evals_seq.sh 启动，**未见显式 CUDA_VISIBLE_DEVICES 设置**——可能违反 C005，下一轮需核实

### 3. 📊 当前状态
我刚完成 D046-D054 的一系列 Claim 2 审查（genuine ISR 2.4x 差异 → premise-count-matched 后归零 1.02x），确认 ISR-as-reward pure negative。

- **RUNNING**: plan018-additive-random-b01-s43-r2（Random β=0.1 s43 控制组，cuda:0 训练中）
- **RUNNING/EVAL**: plan006-prolog-exec-s44（训练完成，checkpoint-500 eval_sta.py 正在跑）
- **DONE(negative)**: plan006-prolog-exec-s43-r3（warmup=0.0 对齐 s42，结论 negative）
- **PREPARING**: plan006-prolog-sta-s43, plan006-prolog-sta-s44（等 GPU）

### 4. 📋 待办（条件触发式）
- plan006-prolog-exec-s44 eval 完成 → 核对 eval_results.json 与 s42 模式一致性（PR/ISR/hacking mode），检查 ground fact enumeration 是否复现 → 3-seed Prolog exec-only 统计出齐
- plan018-random-b01-s43-r2 训练完成 → eval_sta.py → 与 plan002-b01-s43（ISR β=0.1 s43）对比 H7/conclusion embedding 比例
- plan006-prolog-sta-s43/s44 获批启动 → 核实 GPU 分配和 CUDA_VISIBLE_DEVICES
- 3-seed 全部出齐 → 审查 Table 1 + Table 2 定稿数字与 registry 一致性
- Agent 提交论文章节 → 对照 D051-D054 确认 Claim 2 措辞为 pure negative（禁止重新 inflate）

### 5. 🎯 战略上下文
- **核心叙事**：ISR/STA 作为 GRPO neurosymbolic formalizer 的诊断工具 + Goodhart's Law 案例研究
- **三条 Claims**：(1) ISR 崩塌轨迹检测 reward hacking (2) ISR-as-reward 全 β 全 seed Goodhart（pure negative）(3) 跨逻辑泛化（FOL+Prolog）
- **决策链要点**：D020 ISR-as-reward 全面失败转诊断定位 → D033/D035 Goodhart 主线 → D041 β=0.1 sweet spot 被推翻 → D051-D054 premise-count-matched 归零，Claim 2 定论 pure negative
- **最易判断错的事**：
  - Claim 2 已经历 6 次 framing 变更（D046-D054），**不要**被早期决策（D033 sweet spot/D049 双面性）迷惑——最终定论在 D051-D054
  - H7 strict 定义（exact normalized match）是权威口径（D044），旧分析用 partial match 会高估 hacking
  - plan013（convex random）和 plan017（additive random）公式结构不同（D027），不可简化为 additive vs convex 对照
  - conclusion embedding ~70% 是 GRPO 通用行为（D047），不是 ISR 特有——审稿人可能攻击这一点


---
