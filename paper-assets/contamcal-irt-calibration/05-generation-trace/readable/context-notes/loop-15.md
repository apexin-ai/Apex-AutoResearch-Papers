# director / loop_15.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_15.md`
- **Structured JSON:** [`cf6c010fbe2ce2118ab9.json`](../../sessions/cf/cf6c010fbe2ce2118ab9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_messages
updated: '2026-05-17T06:41:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-5 on cqa1-21977，共 6× RTX 4090D，全部归本项目
- 0.5B 模型已被排除出 MMLU/ARC domain IRT（D127），不可再 include
- J=13 (1.5B×8 + 3B×5) 是当前 IRT 模型池，J=21/J=24 均为过时数字
- Paper Agent 已完成 D126 reversal patch，不要再派 D126 相关指令
- Step 5 Round 3 不可在 J=13 rerun 结果出来前启动

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-21977 (connect.cqa1.seetacloud.com)，6× RTX 4090D
- 工作目录: /root/contamcal-irt-calibration
- Stan MCMC: CPU-only，通过 tmux 运行 (session name 待 Agent 确认)
- 模型 checkpoints: /root/contamcal-irt-calibration/ 下各 exp 子目录
- 活跃进程: 
  - Worker `compute:mmlu_domain_irt_no05b` — Stan MCMC J=13 rerun (CPU, tmux)
  - Worker `exp009_recovery` — GPU 0-3 eval + GPU 4-5 s4 signals
- 无 W&B / 无 Git remote 配置

### 3. 📊 当前状态
刚完成: Session 恢复后重发 D127 rerun 指令 + Paper Agent D126 reversal patch（已确认完成）。

RUNNING/活跃:
- `mmlu_domain_irt_no05b`: J=13 Stan MCMC 8 domains + pooled（CPU, ~1-4h，blocking）
- `exp009_recovery`: GPU 0-3 Instruct eval (3B/0.5B/1.5B MMLU + DeepSeek GSM8K), GPU 4-5 s4 signals

等待中:
- J=13 rerun γ 结果回报（Agent 汇报触发）
- exp-009 eval 完成后 → s1_embedding signals 阶段

### 4. 📋 待办
- Agent 汇报 J=13 γ 结果 → Math γ 仍显著(>0.5, p<0.05): 确认 Claim 1 更强，通知 Paper Agent 更新 γ 数值 + J=13 全文替换，启动 Step 5 Round 3
- Agent 汇报 J=13 γ 结果 → Math γ 不显著: framing 调整决策（降级 C1 anchor domain 或换 Science 为主 domain），通知 Paper Agent reframe
- exp-009 eval 完成 → 派 s1_embedding signals（需 GPU），完成后 IRT fitting → data patch 入论文
- Step 5 收敛到 6+/10 → 启动 final reference-audit + 编译验证 + 10 项检查
- Paper Agent 报告"建议提交审稿" → submit_paper_to_review

### 5. 🎯 战略上下文
- 核心 claim: Domain-level γ heterogeneity reveals contamination effects masked by pooled analysis（Math γ >> Science γ）
- D127 是关键转折: 排除 0.5B 消除了 position bias confound（A-rate 46%→98% 与 dosage 共线）。如果 γ_Math 在 J=13 下仍显著，这反而让 claim 更 robust（"即使排除有 confound 的模型也成立"）
- 易错点: 不要把 D108 报告的 N=24 γ 数值当作最终数值——那些含 0.5B，已作废
- Step 5 Round 2 score 4/10 的 3 个 CRITICAL: (1) 0.5B confound 未解决 (2) simulation 条件不一致 (3) bib 问题。其中 (1) 正在通过 J=13 rerun 解决，(2)(3) Paper Agent 已修复
- DDL: EMNLP 2026 ARR May 25，T-8 天
- Cross-family γ 已降级为 "calibration robustness" 弱 claim (D124)，不再是主推论点


---
