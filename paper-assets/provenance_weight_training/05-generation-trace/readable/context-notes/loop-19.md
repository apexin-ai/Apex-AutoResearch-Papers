# director / loop_19.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_19.md`
- **Structured JSON:** [`a0b1a0fe3fca99143ae4.json`](../../sessions/a0/a0b1a0fe3fca99143ae4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_messages
updated: '2026-05-25T03:15:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-41312 的 cuda:0/1/2/3，共 4 张 RTX PRO 6000 96GB。不得使用其他服务器或 GPU
- PaperBanana 必须用 `--vlm-model gemini-2.5-pro`，不能用默认 gemini-2.0-flash（已废弃 404）
- DDL：**EMNLP 2026 ARR May 25**（今天）。所有决策以提交为最高优先级
- 用户明确要求不允许放弃 PaperBanana 概念图，已充值 Google API 配额

### 2. 🖥️ 基础设施快照
- 服务器：westd-41312 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/provenance_weight_training
- Python：aml-train 镜像，conda base 环境（/root/miniconda3/bin/python）
- 磁盘：/autodl-pub 5.3T/7.3T (24%)
- 活跃进程：
  - detect_remove_q07_seed42_r2: cuda:1, PID 987903, ~8% 进度, ETA ~02:30 UTC
  - detect_remove_q05_seed42: cuda:2, ~41% 进度
  - detect_remove_q03_seed42: cuda:3, ~16% 进度
  - cuda:0: 空闲待命，eval 命令已预备好
- D&R eval 脚本已准备：训练完成后零延迟启动 holdout+owt+wiki 三项 eval

### 3. 📊 当前状态
本轮完成：
- N=5 seeds 统计显著性已解决：p_BH=0.011 < 0.05 ✓（核心瓶颈已清除）
- random_subset_epoch_seed42 registry 已更正为 success（Δ≈-0.005 vs uniform，epoch 效应中性）
- contamination_20 eval 完成：holdout=17.348, owt=18.056, wiki=15.105，结论 negative
- PaperBanana 风格标定完成，10 组 PDF+PNG 已用校准 rcParams 重新生成（Reviewer PASS）
- matplotlib 图表全部统一配色（蓝=adaptive, 橙=D&R/ESS, 灰=uniform）

RUNNING：detect_remove_q03/q05/q07_seed42（D&R 阈值扫描三组）
等待：D&R 训练完成 → eval → 结果写入论文

Paper Agent 已在更新 N=5 统计量到论文中。

### 4. 📋 待办
- q05 训练完成（最快，~41%）→ 在原 GPU 或 cuda:0 跑 eval（holdout+owt+wiki）→ registry 更新
- q03 训练完成 → 同上 eval
- q07 训练完成（最慢，ETA ~02:30 UTC）→ 同上 eval
- 全部 D&R eval 完成 → 汇总 D&R 阈值扫描数据（q01/q03/q05/q07 的 PPL 对比）→ 派 Paper Agent 更新论文 D&R 分析章节
- Paper Agent 完成 N=5 更新 + D&R 更新 → 提交审稿 / 最终提交
- PaperBanana 概念图：风格标定已完成但最终概念图未渲染（只完成 planning 阶段）。如需最终渲染需再触发一次，注意 planning.json 有数据幻觉，必须从 CSV 读数据

### 5. 🎯 战略上下文
- 论文定位：Analysis paper "When, why, and how does detect-and-reweight work?"
- 四大贡献：(1) Epoch confound >95% (2) Detector requirements: calibration+discrimination (3) Mechanism: minimum intervention > maximization (4) Adaptive b* tool
- 审稿历史：R8:2.5 → R9:3.0 → R10:3.0 → R12:3.0 → R13:3.0。核心瓶颈（N=3 BH 不显著）已解决
- D&R q>0.1 的 wiki_ppl=28.22 异常高但已接受（仅保留 15% 数据，欠拟合预期）。checkpoint 在旧服务器 westd-30476
- 易错点：PaperBanana planning.json 包含 LLM 幻觉数据（虚构 b=10/20/30），最终渲染绝不能从 planning.json 取数据，必须直接读 CSV/registry
- 决策 D130：Round 13 响应策略 = 补 N=5 seeds + random-subset baseline + 论文更新


---
