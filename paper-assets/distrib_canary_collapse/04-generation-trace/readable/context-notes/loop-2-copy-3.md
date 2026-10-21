# reviewer / loop_2.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`96deb68fdcc060743196.json`](../../sessions/96/96deb68fdcc060743196.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-14T14:51:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名已从 `autodl-rtx6000` 变更为 `westd-19828`，registry 中旧实验仍引用旧名，但 SSH 只能连 `westd-19828`
- 无 constraints.yaml / gpu_ids 白名单定义，当前 rep_42 用 cuda:0、rep_43 用 cuda:1、rep_44 用 cuda:0（nohup 方式，非 tmux）——如果后续定义了 gpu_ids 约束需立即核对
- MAUVE 已被分析脚本自动降级为 supplementary（floor_effect，Gen 0 ≈ 0.034），**不计入 MVP pass/fail verdict**。不要把 MAUVE 相关 pair 结果当作有效证据
- effective_rank 被标记为 **inconclusive**（seed 42 slope +0.81，seed 43 slope -1.90，方向不一致），其 pair 结果**不计入 verdict**

### 2. 🖥️ 基础设施快照
- 服务器：`westd-19828(root)`，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base 环境），PyTorch 2.10.0+cu128
- GPU：2× NVIDIA RTX PRO 6000 Blackwell 96GB
- 数据：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/`（5000 samples）
- HF cache：`/root/autodl-tmp/.hf_cache`，mirror `https://hf-mirror.com`
- 模型：`EleutherAI/pythia-410m`（从 HF cache 加载）
- 活跃进程：rep_44 训练（PID 30678，**nohup 方式非 tmux**，CUDA_VISIBLE_DEVICES=0），日志 `~/runs/distrib_canary_collapse/mvp_v4_rep44.log`
- 无 W&B 配置，不检查 W&B
- 分析产出：`results/mvp/analysis/`（analysis_summary.json, metric_trends.png, cross_correlation.png, lead_time_table.csv）
- 评估标准文档：本地 `artifacts/mvp_evaluation_criteria.md`

### 3. 📊 当前状态
**我刚完成的审查：**
- rep_42 和 rep_43 全部完成（gen_0–gen_10），分析已运行，verdict = **STRONG PASS**
- 2 个 canary family（token_entropy、ece）各有 ≥1 SIGNIFICANT LEAD pair（against distinct_1/2/3）
- rep_44 刚启动（21:35 server time），仅有 config.json，在 GPU 0 上跑
- **GPU 1 完全空闲**（0% util, 0 MB）——rep_44 只用了 GPU 0

**我已提交给 Director 的报告（~08:36 UTC）：**
- MAUVE 基线病态低（warning）
- collapse 过快（warning）
- effective_rank 反直觉上升（warning）
- 以上两个 warning 已被 analyze_mvp.py 的评估标准正确处理（MAUVE 降级、eff_rank inconclusive）

**未提交的新发现（本轮）：**
- STRONG PASS verdict 的独立核实——尚未提交，需要下一个"我"完成
- rep_44 进程用 nohup 而非 tmux 提交，registry 仍是 PREPARING 状态未更新

### 4. 📋 待办（条件触发式）
- **立即**：独立核实 STRONG PASS verdict，重点检查：(a) 分析只用了 2 个 seed（rep_42/43），MVP 要求 3/3 seeds 一致，rep_44 未完成时 verdict 不成立；(b) token_entropy→perplexity 是 WEAK LEAD（seed 42 p=0.12 > 0.10），不是 SIGNIFICANT；(c) ece→perplexity 的 lag 方向不一致（seed 42 lag=+5，seed 43 也未见），是 NO LEAD → 提交核实报告给 Director
- rep_44 完成 → 核实 3/3 一致性，重新评估 verdict（可能从 STRONG PASS 降级）
- rep_44 完成 → 检查 GPU 1 是否仍空闲，若是则标 warning（资源浪费）
- Director 决策 MVP pass/fail 后 → 审查 Phase 2 计划是否与 MVP 证据匹配

### 5. 🎯 战略上下文
- **项目核心**：D001 定义 MVP 假设（canary 领先 downstream ≥1 gen），D004 修正过拟合参数。目标 AAAI 2027（~Aug 2026 DDL）
- **MVP 初步结论看起来正面**：token_entropy 和 ECE 对 distinct-n 有显著 lead（lag=-1），但对 perplexity 的 lead 较弱或方向不一致
- **最容易判断错的事**：当前 analysis_summary.json 报 STRONG PASS，但**只基于 2 个 seed**（rep_44 未完成）。MVP 评估标准（mvp_evaluation_criteria.md §2）要求 3/3 seeds 全部 peak_lag < 0 且显著。**2/3 seed 的 STRONG PASS 不是真正的 STRONG PASS**——必须等 rep_44 跑完重新分析
- **容易踩的坑**：ece→perplexity pair 在 seed 42 的 peak_lag=+5（反向！canary 滞后于 downstream），这使得 ece 对 perplexity 无法成为 lead pair。如果 rep_44 的 ece→distinct_n 不一致，ece family 可能整体降级
- **文献竞争**：chen2025scales 已报告 ECE 领先 accuracy（但无 Granger causality），如果 ece 在我们的实验中不稳健，方法论壁垒（cross-correlation 框架本身）成为唯一 novelty 支柱


---
