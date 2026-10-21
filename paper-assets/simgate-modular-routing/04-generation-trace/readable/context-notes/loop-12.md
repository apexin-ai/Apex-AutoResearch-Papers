# director / loop_12.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_12.md`
- **Structured JSON:** [`fc8e697e0014ffb47b40.json`](../../sessions/fc/fc8e697e0014ffb47b40.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_messages
updated: '2026-05-21T01:23:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westb-13313 的 cuda:0 / cuda:1（2× RTX 5090）。D129 已决策释放，**无需新 GPU 实验**
- westd-18266 SSH key 未配通（public key 已发用户，未确认添加），**不要尝试连接**
- 论文 CI 方法已统一为 **non-clustered episode-level bootstrap (B=10,000)**。任何新增 CI 必须用同一方法，禁止混入 cluster bootstrap
- Gemma CI 是 [79.5, 98.4]（episode-level），不是 [68.8, 100.0]（cluster，已全文清除）。如果在 registry/manifest 中看到 68.8 是历史残留，论文中已修正
- EMNLP 2026 ARR DDL **2026-05-25**，主文严格 ≤8 页

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313（SSH host: `autodl-simgate`，Port 13313）
- 工作目录：/root/autodl-tmp/simgate-modular-routing/
- Python：conda base 环境（/root/miniconda3/bin/python）
- 模型：/root/autodl-tmp/.hf_cache/ 下 Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Gemma-2-9B-it
- 数据：/root/autodl-tmp/simgate-modular-routing/ 下各模型的 episodes.jsonl
- 论文源码：本地 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/
- 活跃进程：无（全部实验完成，GPU 空闲）
- Cron：无活跃 cron

### 3. 📊 当前状态
刚完成 CI 方法统一（episode-level bootstrap 全文一致）+ 三模型 sensitivity analysis（排除零死亡 task 后 DAF ≥97%）。

- Registry: 0 RUNNING / 0 PREPARING。53 成功 / 30 阴性 / 17 失败 / 21 killed
- 论文编译通过：17 页，0 errors，主文 ≤8 页
- **内部审稿已提交**（apr_20260521T004926_35g5），审批卡在 A 群等用户选择审稿模式
- **等待用户确认** ARR 提交。用户尚未回复"是否启动 ARR 提交流程"
- Agent 空闲，Reviewer 即将 RESET

### 4. 📋 待办
- 用户选择审稿模式（continue/fresh）→ 内部审稿自动启动 → 收到审稿报告后按 review-report-action skill 处理
- 用户确认提交 → 最终格式/引用/数据一致性检查 → ARR 提交
- 内部审稿发现需要补实验 → 评估是否重新开 GPU（westb-13313 可重开）
- 4 个预存 undefined ref（NLP checklist 中引用 sec:experiments）→ 低优先级，提交前修复

### 5. 🎯 战略上下文
- **核心结论**：Death avoidance accounts for 88-90% of routing signal across three architecturally distinct model families (Qwen/Llama/Gemma)。排除零死亡 task 后 ≥97%。Framework-centric pivot (D126/D127) 是关键 framing 决策。
- **决策链**：D126 framework-centric pivot → D127 paper_framing 更新 → D128 extended-task-validation → D129 释放 GPU
- **易错点**：
  - 不要把 cluster bootstrap CI 混进论文（68.8 vs 79.5 for Gemma，差别很大）
  - experiments.tex L23 的 "DAF to 96.8%" 是 LOTO 分析的 Pearson r 值 (0.9698)，不是 DAF——Agent 已确认无冲突
  - 论文 page 26 附近 Qwen CI 写的是 [81.1, 99.0]，cross_model_bootstrap_cis.json 里是 [81.3, 99.1]——0.2pp 差异来自不同脚本运行，论文统一用 [81.1, 99.0]
  - Rebuttal drafts 已更新到最新 CI 值和 sensitivity 数据，不需要再改
  - 用户之前说"先不提交"（等实验完成），现在实验全部完成但用户尚未确认提交——不要主动提交，等用户确认


---
