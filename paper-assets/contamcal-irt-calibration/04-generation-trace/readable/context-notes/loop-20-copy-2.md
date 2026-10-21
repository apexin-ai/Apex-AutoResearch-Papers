# agent / loop_20.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`9f9e7e49dde51aae46d6.json`](../../sessions/9f/9f9e7e49dde51aae46d6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-17T21:53:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cqa1-21977 的 cuda:0~cuda:5（共 6 张 4090D），不得使用其他服务器或设备号
- 论文已完稿通过 10 项检查，距 EMNLP 2026 ARR May 25 仅 8 天，**禁止未经 Director 批准修改 paper 文件**
- Llama d100 数据有 position bias (A-rate=82.8%)，IRT pooling 必须排除该条件
- 0.5B 模型已从 MMLU domain IRT 中排除（D127），不要重新加入
- DeepSeek MC 数据已从 IRT pooling 中排除（D128）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 `/root/contamcal-irt-calibration/`
- Python：`/root/miniconda3/bin/python`（通过 `source /root/miniconda3/bin/activate` 激活）
- 实验代码：`/root/contamcal-irt-calibration/exp006/`（IRT），`/root/contamcal-irt-calibration/exp002/`（signals）
- 论文本地路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/`
- 磁盘：`/autodl-pub` 96% 已用（343G 可用）⚠️，`/autodl-pub/data` 65% 已用（1.5T 可用）
- 活跃进程：无（6 张 GPU 全空闲）
- Cron：0 个活跃

### 3. 📊 当前状态
**刚做完**：Session 20 初始化 + j16 诊断 Worker 结果处理 + 3 个 stale RUNNING 实验清理 + 向 Director 汇报

**Registry**：0 RUNNING, 13 PREPARING（历史遗留 superseded 实验，非活跃），~255 DONE

**等待中**：
- Worker 回调：`worker_ops_rrf_vs_s1only_ablation_20260517T174924`（CPU，turn 12，分析 RRF vs s1-only ablation 代码/数据）
- Director 决策：(a) 是否用 `--pooled_only` 重跑 j16 pooled fit；(b) Round 4 审稿结果（apr_20260517T171959_uwoy，待用户审批）
- 用户确认后提交 ARR

### 4. 📋 待办
- `worker_ops_rrf_vs_s1only_ablation` 回调到达 → 读取结果，整合到项目知识文件，汇报 Director
- Director 决定重跑 j16 pooled → spawn Worker 用 `--pooled_only` 参数在 cqa1-21977 跑（~6-10 分钟）
- Round 4 审稿结果返回 → 按反馈修正论文（需 Director 批准每处改动）
- 用户确认提交 → 按流程提交 ARR
- 6 GPU 全空闲 → 如 Director 无新实验指令，可清理 13 个 PREPARING 历史实验

### 5. 🎯 战略上下文
- **核心结论**：IRT calibration decomposition 是 primary contribution，但 D134 pivot 到 **null finding framing**——SFT 污染聚合效应仅 ~0.6-0.7pp，raw accuracy 全面胜出所有校正方法。IRT 价值在 diagnostic（γ 存在性检验 + domain 异质性），非 calibration improvement
- **D129 是关键 pivot**：从 γ-centric 转向 Direction A（IRT calibration primary），全文已 reframe
- **易错点**：`exp_006_cross_family_irt_j16`（J=16，failed）和 `exp006_cross_family_pooled_irt`（v5，success）是不同实验。v5 已充分支撑论文 cross-family claim（D131），j16 是扩展实验。不要因 j16 失败认为 cross-family 证据缺失
- **j16 domain fits 已有有价值数据**：3/8 domain 显著负向 γ（Social Sciences -1.09, Humanities -0.95, Other -0.88），暗示 Qwen RRF signals 标记的是跨家族更难的 items（非更容易），与 Llama 不共享 Qwen 特定污染一致。但 6/8 domain PPP>0.95 有模型 misspecification 问题
- **三层贡献**：(1) Null finding: raw accuracy beats all corrections (2) Decomposition: θ ability + γ diagnostic + RRF item filtering (3) Exploratory: domain heterogeneity + identifiability boundary


---
