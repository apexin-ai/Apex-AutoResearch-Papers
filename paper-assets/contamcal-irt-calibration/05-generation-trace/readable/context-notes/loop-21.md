# agent / loop_21.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`ed842fafb913b7cce0c4.json`](../../sessions/ed/ed842fafb913b7cce0c4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-18T01:55:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 的 cuda:0~cuda:5（共 6 张 4090D），不得使用其他服务器或设备号
- 论文已完稿通过 10 项检查，距 EMNLP 2026 ARR May 25 仅 7 天，**禁止未经 Director 批准修改 paper 文件**
- Llama d100 数据有 position bias (A-rate=82.8%)，IRT pooling 必须排除该条件
- 0.5B 模型已从 MMLU domain IRT 中排除（D127），不要重新加入
- DeepSeek MC 数据已从 IRT pooling 中排除（D128）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 `/root/contamcal-irt-calibration/`
- Python：`/root/miniconda3/bin/python`（通过 `source /root/miniconda3/bin/activate` 激活）
- 实验代码：`/root/contamcal-irt-calibration/exp006/`（IRT），`/root/contamcal-irt-calibration/exp002/`（signals）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/`
- 磁盘：`/autodl-pub` 96% 已用（343G 可用），`/autodl-pub/data` 65% 已用（1.5T 可用）
- 活跃进程：无（6 张 GPU 全空闲）
- Cron：0 个活跃

### 3. 📊 当前状态
Session 21 初始化完成，向 Director 汇报了空闲状态。项目处于 **等待 Round 5 审稿结果** 阶段。

- Registry：0 RUNNING，23 PREPARING（全部 conclusion=killed，历史 superseded 实验，非活跃）
- 最近完成的 Worker：`worker_review_bib-completeness`（21:42 UTC）、`worker_review_narrative-verify`（21:39 UTC）
- Round 5 review 已提交：`apr_20260517T195445_dcf9`（continue mode）
- 无等待中的 Worker 回调 / Cron / Director 决策（RRF ablation worker 已在前几轮处理完毕）

### 4. 📋 待办
- Round 5 审稿结果返回 → 读取反馈，按 on-experiment-done skill 分叉处理（纯文本修改需 Director 批准）
- Director 指示提交 ARR → 按流程执行最终提交
- Director 分配新任务 → 按指令执行（6 GPU 空闲可用）
- 如长期无指令 → 可清理 23 个 killed PREPARING 实验（低优先级，不影响功能）

### 5. 🎯 战略上下文
- **核心结论**：IRT calibration decomposition 是 primary contribution，但 D134 pivot 到 **null finding framing**——SFT 污染聚合效应仅 ~0.6-0.7pp，raw accuracy 全面胜出所有校正方法。IRT 价值在 diagnostic（γ 存在性检验 + domain 异质性），非 calibration improvement
- **三层贡献**：(1) Null finding: raw accuracy beats all corrections (2) Decomposition: θ ability + γ diagnostic + RRF item filtering (3) Exploratory: domain heterogeneity + identifiability boundary
- **易错点**：`exp_006_cross_family_irt_j16`（J=16，failed）和 `exp006_cross_family_pooled_irt`（v5，success）是不同实验。v5 已充分支撑论文 cross-family claim（D131），j16 是扩展实验，不要因 j16 失败认为 cross-family 证据缺失
- **D135 Action Matrix 全部完成**：Round 4 所有 issue 已修复，Round 5 是 continue mode review。论文 0 errors, 0 undefined citations, 14 pages
- **距 deadline 7 天**：除非审稿有 critical issue，论文基本定稿。任何修改需 Director 批准


---
