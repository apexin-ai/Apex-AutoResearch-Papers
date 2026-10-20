# agent / loop_11.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`132eabd0376da8ba54c5.json`](../../sessions/13/132eabd0376da8ba54c5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T12:40:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 已按 D056 全部释放，当前 gpu_ids 为空。**未经 Director 重新分配前禁止启动任何 GPU 实验**
- 论文已提交 fresh review（`apr_20260515T104409_t4pu`），**review 结果回来前不动 paper 文件**，除非 Director 明确指示
- Llama cross-model expansion 已被 D056 明确叫停，**不要再尝试扩展 Llama 实验**（D054/D055/D056 决策链）
- Bib 引用键已从 `toolformer-2024`/`chameleon-2024` 修正为 `toolformer-2023`/`chameleon-2023`，改动涉及 references.bib + introduction.tex + related_work.tex，**不要回退**

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，2× RTX 5090，当前无活跃进程
- 本地论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`
- 编译命令：`cd docs/paper && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex ... && pdflatex ...`
- Figure 生成 venv：`/tmp/fig_venv/bin/python`（matplotlib 已装，PEP 668 系统不能直接 pip）
- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/`
- 活跃进程：无。Cron：0 个活跃。Worker：0 个。

### 3. 📊 当前状态
刚完成 D056 跟进清理并已向 Director 汇报：
- Registry：6 个残留 PREPARING 实验全部清理到 DONE（3 success, 3 killed）
- Bib：2 个 citation key 年份错误修复，编译验证通过（0 undefined citations）
- Provenance：C139/C220/C223 deprecated，C118 值修正 96.2%→96.3%
- Registry 中 0 个 RUNNING/PREPARING 实验
- 无等待中的 Worker 回调或 Cron
- 等待：fresh review 结果（预计 5/17-19 返回）

### 4. 📋 待办
- Fresh review 结果返回 → 按 action protocol 处理：spawn worker 逐条分析审稿意见 → 分类 blocker/nice-to-have → 向 Director 汇报修改方案
- Director 重新分配 GPU → 可跑额外加强实验（routing pattern 分析已产出 death timing 分布洞察，可考虑写入论文）
- Director 指示修改论文 → 按 red-section skill 规范操作，写前必须读 skill
- 5/23-24 终稿阶段 → reference-audit + paper-visual-review + 最终编译检查

### 5. 🎯 战略上下文
- 核心结论：ScienceWorld 上 ~90% routing signal 来自 death avoidance（DAF=90.41% at P=100, r=0.97 across 11 tasks）
- 论文定位：EMNLP 2026 ARR Long Paper (8p+refs)，DDL 5/25
- 证据包完整：core decomposition + correlation + penalty sensitivity + router diagnostic + MATH negative contrast + Llama cross-model pilot + labeling quality audit
- 决策链关键节点：D050（升级 long paper）→ D054/D055（Llama pilot 方向一致，不扩展）→ D056（停全部实验，清理，释放 GPU 等 review）
- 易错点：plan-005-routing-patterns 的 death timing 分布（internal mid-game 69.5% vs deterministic late-game 70%）是新洞察但**尚未写入论文**，review 结果回来后可作为加强材料
- 易错点：MATH 结果是 directional reversal (+4.3pp) 但 **不显著**（p=0.079），论文措辞是 "directional" 不是 "significant"，不要误改


---
