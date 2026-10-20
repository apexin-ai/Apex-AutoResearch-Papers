# reviewer / loop_4.md

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`65a807725707256c8973.json`](../../sessions/65/65a807725707256c8973.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T04:21:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `bjb2-23165`，项目代码在 `/root/autodl-tmp/agent_progress_probe`
- 特征重叠消融只有 **11/19 split** 有实验支撑（registry: feature-overlap-ablation + feature-overlap-lf-only），**14/16 split 没有实验支撑**——之前 Paper Agent 曾擅自改成 14/16 被我打回，若再出现立即 CRITICAL
- OH 数据存在双轨：150,652 windows / 20.9% stag（全量 JSONL）vs 143,057 / 21.4%（embedding subset）。论文中必须区分使用场景，不能混用
- error overlap canonical 数字是 192/8,643 = 2.22%（不是旧的 31/0.36%，旧数字来自错误配置的 GB）

### 2. 🖥️ 基础设施快照
- 服务器：`bjb2-23165`，工作目录 `/root/autodl-tmp/agent_progress_probe`
- 我是 Reviewer，只有只读权限（ssh_read_only / registry / Read / Grep），无法直接 SSH 探查进程状态
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/`
- 论文源码：`docs/paper/sections/*.tex`，main entry `docs/paper/main.tex`
- 活跃进程（上次已知）：Claude CoT 实验 ~44% (800/1824)；LLM structured-input ~49% (900/1824)——两者均在服务器上运行，可能已完成

### 3. 📊 当前状态
**刚做完**：7 项修正验证报告已 post 给 Director（全部 PASS + 2 个 WARNING：Appendix A.7 模型名 "Claude 3.5 Sonnet" 应为 "Claude Sonnet 4.6"；GPT-5.5 "partial" 应改为 "parse failure"）。

**刚收到未处理**：Director 的 Round 3 审稿 Action Matrix 审查请求（6 个具体问题）——我已读完 method.tex 但因 context 断裂尚未回复。这是当前最高优先级任务。

**Registry 关键状态**（上次已知）：
- cross-agent-structural: DONE (GB conf≥2=0.9919)
- feature-overlap-ablation / feature-overlap-lf-only: DONE (11/19 verified)
- instance-isolation-canonical: DONE (all Δ<0.1pp)
- llm-judge-strengthened: DONE (Claude few-shot 0.751, GPT-5.5 0.746)
- Claude CoT / LLM structured-input: 可能仍 RUNNING

### 4. 📋 待办
- **立即**：回复 Director 的 Round 3 Action Matrix 审查（6 个问题），需要先读 registry 确认 CoT/structured-input 最新状态
- Claude CoT 完成 → 若 F1 > 0.751 → "best LLM" 基准和 21.6pp claim 需更新，立即 post Director
- Claude CoT 完成 → 若 F1 ≤ 0.751 → 确认 Appendix A.7 无需改动
- Gold set 标注启动 → 核查标注协议（每窗口 2-3 分钟 × 150 窗口 ≈ 5-8h，需确认 inter-annotator agreement 设计）
- MF-3 scope matching worker 完成 → 验证 structural GB 在 6,122 probe test split 上的 F1，评估 36.9pp claim 是否需要修正
- 页面压缩后 → 审查压缩版是否丢失关键证据

### 5. 🎯 战略上下文
- **审稿结果**：weak reject (R1: 2.5, R2: 2.5)。4 个 must-fix：页面超限、gold set 缺失、scope mixing、circularity 缺口
- **核心风险**：gold set 是全文可信度的关键路径——没有 human annotation，所有 claims 都建立在 silver labels 上，reviewers 已明确指出这一点
- **易错判断**：
  1. 21.6pp claim（0.967 cross-agent GB vs 0.751 in-domain LLM）是**跨 scope 比较**——reviewers 已标记为 overclaiming，MF-3 的 matched-scope 计算可能显著改变这个数字
  2. 11 vs 30 features 的差异（0.977 vs 0.967）虽然叙事好看（"fewer features generalize better"），但没有统计检验——reviewer 要求 paired bootstrap
  3. SF-5 不加新 LF 是**有风险的决策**——reviewer 明确要求 5-6 LFs minimum，仅 scope 收窄可能不够，需要看 Director 怎么 frame
  4. Findings track vs Main track 定位——reviewer 建议 Findings，但这是 Director/用户决策，我只评估证据是否支撑


---
