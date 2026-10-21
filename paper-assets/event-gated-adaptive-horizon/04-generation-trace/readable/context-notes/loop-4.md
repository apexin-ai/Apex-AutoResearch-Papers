# director / loop_4.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`8d1629a0480418d50f4e.json`](../../sessions/8d/8d1629a0480418d50f4e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T12:03:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（2×RTX PRO 6000）。绝不在其他卡上启动实验
- 008d 和 009e 是同一 seed (seed=1)，不是独立观测。崩溃率统计中只算一个。论文中 trained dt_emb collapse rate = 1/2 (50%)，不是 2/3
- exp_006 的 dt_emb 分类尚未确认——Table 1/2 标 "---" 但 threshold report 归为 "trained"。Agent 正在核实，结果出来前不要修改 88.9% accuracy 数字
- plan_017 submit 脚本必须有 `--gate_subsample_max_dt 1`，否则 subsample 仍 ON = 重复 008d（已被 Reviewer 抓过两次）
- plan_015B 的 dt_emb freeze 必须在 `_train` 入口重新 freeze（DreamerV3 的 `RequiresGrad` 上下文管理器会覆盖）——代码已处理，但改代码时注意
- NVE 字段统一用 normalized（除以 baseline v/e），不是 raw v/e ratio

### 2. 🖥️ 基础设施快照
- 服务器：通过 SSH host 连接（具体 host 见 `list_ssh_hosts`），工作目录 `/root/event-gated-adaptive-horizon/`
- Python：conda base 环境（aml-train 镜像），`/root/miniconda3/bin/python`
- 本地项目路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文源码：`docs/paper/` (main.tex + sections/*.tex)
- 图表权威目录：`artifacts/figures/paper/`（fig1-fig6，旧 `artifacts/paper_figures/` 已 archive）
- 活跃进程：
  - cuda:0: exp_009d_baseline_walker_s0 (seed=0, 500K, 刚启动 ~19h)
  - cuda:1: exp_015b_frozen_dt_emb (freeze dt_emb, 105K, ~5h, 刚启动)

### 3. 📊 当前状态
**刚做完**：009e 完成分析 (CIVO confirmed, eval=131@105K)、kill 009d (seed=1 duplicate) 并用 seed=0 重新提交、plan_015B 启动在 cuda:1、Paper Agent Step 5 Round 2 审稿修正进行中（评分从 4→6/10）

**RUNNING 实验**：
- exp_009d_baseline_walker_s0 (cuda:0, seed=0, 500K) — 第三个独立 baseline seed
- exp_015b_frozen_dt_emb (cuda:1, 105K) — 2×2 矩阵关键格：dt_emb training 是否是 CIVO 必要条件

**等待中**：
- Agent 回复：exp_006 dt_emb 配置核实结果
- Paper Agent：Round 2 修正中（3 warnings: analysis 009e 描述、006 dt_emb 标注、fig2 caption 限定）
- 015B 完成 cron → 提交 plan_017 (subsample OFF + trained dt_emb) 到 cuda:1

### 4. 📋 待办
- exp_006 dt_emb 核实结果返回 → 如果 trained: Table 1/2 改为 "trained"，88.9% 不变；如果非 trained: 重算准确率，"100% specificity" 需修正
- 015B 完成 → 分析结果（预期不崩溃 = dt_emb training 是必要条件）→ 立即提交 plan_017 到 cuda:1
- plan_017 完成 → 2×2 矩阵闭合，log decision，通知 Paper Agent patch Results
- 009d (seed=0) 完成 → 更新 baseline 为 3 seeds，Paper Agent 更新 Methodology "3 seeds"
- 009d 完成后 cuda:0 → plan_020 (Cheetah baseline, 3 seeds) 代码已准备好
- Paper Agent Round 2 修正完成 → 送 Round 3 审稿，目标 ≥7/10
- Fig3 和 Fig6 仍为 Draft 状态（需纳入 009e + D040 dual pathway 数据）

### 5. 🎯 战略上下文
- **核心因果链**：trained dt_embedding → CIVO (conditioning-induced value overestimation) → collapse。C2 是最强 claim。
- **关键决策链**：D033 (008e_v3 dt_emb 实际是 trained) → D038 (C6 falsified) → D039 (机制辨析) → D040 (C6 PARTIALLY FALSIFIED, multiple vulnerability pathways) → D041 (plan_015 redesign: detach 是 no-op, 改为 freeze)
- **论文定位**：diagnostic analysis paper，不是 method paper。发现问题+定位根因+展示多条脆弱路径。TAWM 对比是关键差异化（MPC 成功 vs imagination 失败）
- **三种 post-CIVO 结局**：full collapse (008d s0) / oscillatory degradation (009e s1) / self-correction (009b s2)。同配置不同 seed → systemic vulnerability
- **最容易判断错的事**：(1) 008d/009e 不是独立观测，是同 seed 延续；(2) plan_017 的 subsample OFF 需要 `--gate_subsample_max_dt 1` 不是 0；(3) "4/4 separating power" 只在 factorial grid 内成立，全样本是 88.9% (8/9)；(4) 008e_v3_s2 崩溃不是经典 CIVO（eval-driven vs value-driven），论文标签应为 "late-onset collapse" 不是 "non-CIVO"
- **CoRL DDL 2026-05-29，剩 14 天**。Walker Walk 数据基本完整，Cheetah 跨环境验证是 P0 但还没开始


---
