# agent / loop_18.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`b0812559c580f37c0d0d.json`](../../sessions/b0/b0812559c580f37c0d0d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-17T09:35:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 cuda:0, cuda:1（只有这两张，config里写的 autodl-simgate:cuda:0/1）
- 论文目标：EMNLP 2026 Findings，DDL 2026-05-25（剩 8 天）
- Round 11 最终审稿已提交 pending，论文不动除非 Director 明确指示
- 4B router e2e 实验是 capacity scaling 证据链的最后一环——结论直接影响 paper framing（若 negative 则强化 "analytical framework > learned routing at all scales" narrative）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，account: root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- 日志目录：~/runs/simgate-modular-routing/
- GPU：2× RTX 5090
- W&B：无专用 wandb section in config（但实验有 W&B data）
- 活跃进程：math-extension-n800 (PID 565371, cuda:1, cron 监控中)
- plan-008-v4-4b-e2e：进程已退出，状态 ANALYZING，日志 ~/runs/simgate-modular-routing/plan-008-v4-4b-e2e.log

### 3. 📊 当前状态
- **刚发生**：plan-008-v4-4b-e2e cron 回调到达（进程正常退出，W&B data available）
- **已派 Worker**：`worker_analysis_plan-008-v4-4b-e2e_20260517T041811` 正在 SSH 读日志 + 抓指标，尚未返回
- **RUNNING**：math-extension-n800（cuda:1，MATH Level 4-5 N=800 统计验证）
- **ANALYZING**：plan-008-v4-4b-e2e（等 Worker 回调后判定 conclusion）
- **cuda:0 空闲**（plan-008-v4-4b-e2e 已跑完释放）

### 4. 📋 待办
- Worker `worker_analysis_plan-008-v4-4b-e2e` 回调 → 读 metrics → 判定 conclusion（大概率 negative，对标 always-det=-9.47）→ update_registry → 刷新 report.md → 向 Director 汇报（含推导链）
- 若 negative → 不默默跑下一个实验，按 on-experiment-done negative 流程汇报 Director（这是 capacity scaling 的 final data point，论文已有 framing 预期它 negative）
- math-extension-n800 cron 回调 → 同样分析流程（验证 MATH 环境中 internal vs code-interpreter 无优势）
- 两个实验都完成后 → 向 Director 汇报全部 capacity + cross-domain 证据链是否完整，是否支撑 R11 提交

### 5. 🎯 战略上下文
- 核心结论：DAF 78.9% routing labels 由 death asymmetry 驱动（penalty-independent）。论文定位 Findings track（case study 而非 main contribution）
- plan-008-v4-4b-e2e 的上下文：之前 1.7B router e2e = -10.70（worse than always-det -9.47）。4B router episode-level accuracy=59%（略高于 1.7B 的 58.1%），如果 e2e 仍 ≤ always-det，则确认 "learned routing fails at all tested scales"
- D101 决策链：Findings reframe 已完成，R11 已提交。这两个实验（4b-e2e + math-extension）是补充证据，不改变论文 core framing
- 易错点：不要因为 4B e2e negative 就建议 pivot 或改 framing——论文 narrative 已经预期并 embrace 这个结论（"analytical framework dominates learned routing"）。正确做法是将数据录入 paper 作为 capacity scaling 补充证据


---
