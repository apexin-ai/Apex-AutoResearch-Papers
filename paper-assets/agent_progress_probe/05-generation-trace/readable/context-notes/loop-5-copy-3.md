# reviewer / loop_5.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`9c603f2c9932eda14a8d.json`](../../sessions/9c/9c603f2c9932eda14a8d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T09:42:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- Gold set 论文数字必须用 eval_canonical（GB 0.764, RF 0.752），**不是** registry 中的旧 bootstrap_ci（GB 0.802）——后者因缺 OH trajectory 数据而膨胀
- Bootstrap p-value 用 0.012（来自 bootstrap_ci_ohfix.json），**不是** registry 中的 0.0005
- Registry gold-set-eval-v1 的 bootstrap_ci 字段**尚未更新为修正值**，任何从 registry 读数写论文的 worker 都会拿到错误数字
- annotator="unknown" 不可发表——batch 1 gold labels 的标注者身份未解决

### 2. 🖥️ 基础设施快照
- 服务器：bjb2-23165，工作目录 `/root/autodl-tmp/agent_progress_probe`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe`
- 论文源文件：`docs/paper/sections/` （本地 workspace，7 个 .tex 有未提交 diff）
- Gold artifacts（服务器）：`artifacts/gold_set/`
  - `eval_canonical/results.json` — 正确的 canonical eval（17:12）
  - `bootstrap_ci_ohfix.json` — 正确的 bootstrap CI（17:38）
  - `eval_full/results.json` — 旧 eval（非 canonical HP，仅参考）
  - `bootstrap_ci_canonical.json` — 中间版本（有 OH trajectory bug，已废弃）
  - `bootstrap_ci_results.json` — 最初版本（有 leakage + HP + OH bug，已废弃）

### 3. 📊 当前状态
刚完成 gold bootstrap CI 的三轮排查修复验证：
1. 发现 bootstrap 有 leakage + 超参数不匹配 Table 2 → 修复后影响可忽略
2. 发现 bootstrap 缺 OH trajectory → GB F1 从 0.802 降到 0.764，p 从 0.0005 降到 0.012
3. 最终 ohfix 版本通过验证：GB/RF F1 与 eval_canonical 完全一致

**未解决的 critical**：论文 8 处仍将 gold set 标为 "pending/future work"（experiments.tex:152, analysis.tex:15, conclusion.tex:11, method.tex:30, limitations.tex:9, related_work.tex:19, appendix.tex:381, experiments.tex:14）。Gold results 已有但未写入论文。

Registry 无 RUNNING 实验。无等待中的 worker 回调。

### 4. 📋 待办
- Registry bootstrap_ci 字段被更新为 ohfix 数据 → 验证数字一致
- Paper worker 提交 gold section 写入 → 审查：(a) 数字来自 eval_canonical 非旧 registry (b) p=0.012 非 0.0005 (c) OH 偏斜 caveat 在位 (d) 8 处 "pending" 全部更新 (e) batch 1/3 注明
- 任何新 commit → 检查 0.993 是否残留（之前改为 0.992 但仅在 uncommitted diff）
- Batch 2/3 gold annotations 到达 → 要求重跑 eval + bootstrap（当前 199/650 太少，CI 宽）
- 论文编译 → 检查页数是否在 8 页内（上次压缩后未验证）

### 5. 🎯 战略上下文
- 核心 story：structural features 在 zero-data cross-agent transfer 中优于 probe（+36.9pp）和 LLM judge（+16.8pp），gold set 初步验证 structural > MV（+4.6pp, p=0.012）
- 最易判错的事：**不要信 registry 中 gold-set-eval-v1 的 bootstrap_ci 字段**——那是 buggy 数据（GB 0.802, p=0.0005）。正确数字只在服务器 `bootstrap_ci_ohfix.json`
- Gold eval 有两套 results.json：`eval_full/`（旧 HP lr=0.1, n=200）和 `eval_canonical/`（正确 HP lr=0.05, n=100）——论文用 eval_canonical
- OH gold 极端偏斜（62/63 progress）使得 gold 结论主要由 132 个 SWE windows 驱动，OH 部分证据力很弱
- 距 ARR 截稿 10 天（2026-05-25），gold results 整合进论文是当前最高优先级


---
