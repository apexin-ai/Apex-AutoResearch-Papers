# agent / loop_19.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`be436d507a578e6c82ef.json`](../../sessions/be/be436d507a578e6c82ef.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-17T17:48:55+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cqa1-21977 的 cuda:0~cuda:5（共 6 张 4090D），不得使用其他服务器或设备号
- 论文已完稿通过 10 项检查，距 EMNLP 2026 ARR May 25 仅 8 天，**禁止未经 Director 批准修改 paper 文件**
- Llama d100 数据已确认有 position bias (A-rate=82.8%)，IRT pooling 必须排除该条件
- 0.5B 模型已从 MMLU domain IRT 中排除（D127 决策），不要重新加入
- DeepSeek MC 数据已从 IRT pooling 中排除（D128 决策）

### 2. 🖥️ 基础设施快照
- 服务器: cqa1-21977，工作目录 `/root/contamcal-irt-calibration/`
- Python: `/root/miniconda3/bin/python`（通过 `source /root/miniconda3/bin/activate` 激活）
- 实验代码: `/root/contamcal-irt-calibration/exp006/`（IRT 相关），`/root/contamcal-irt-calibration/exp002/`（signals）等
- 论文本地路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/`
- 磁盘: `/autodl-pub` 已用 96%（343G 可用）⚠️，`/autodl-pub/data` 65% 已用（1.5T 可用）
- 活跃进程: 无（全部 6 张 GPU 空闲）
- Cron: reconcile 结果为 0 个活跃 cron

### 3. 📊 当前状态
**刚做完**: Session 初始化 + 收到 `exp_006_cross_family_irt_j16` 失败回调
**正在做**: 已派 Worker `worker_diagnose_exp_006_cross_family_irt_j16_20260517T134702` SSH 诊断失败根因（进程死亡 5 次无 W&B/sentinel）

Registry 概况:
- RUNNING: 0
- PREPARING: 23（多为历史遗留的 superseded 实验，非活跃）
- DONE: 250（success 177, negative 7, failed 54, killed 12）

**等待中**:
- Worker 回调: `worker_diagnose_exp_006_cross_family_irt_j16_20260517T134702`（诊断完成后需分析根因 → 更新 registry → 汇报 Director）
- Director 决策: 论文待提交 Review Director 正式审稿，然后等用户确认后提交 ARR

### 4. 📋 待办
- 诊断 Worker 回调到达 → 分析根因，更新 registry failure_reason，汇报 Director（附资源行，6 GPU 全空闲）
- 如果根因可修 → 建议 Director 是否重跑 cross-family IRT（但注意论文已完稿，cross-family 已有 v5 结果支撑 D131 决策）
- Director 确认论文提交 → 按流程提交 Review Director 审稿
- 6 张 GPU 全空闲 = 失职 → 诊断完后向 Director 请示是否有新实验需求，或可清理 23 个 PREPARING 状态的历史实验

### 5. 🎯 战略上下文
- **核心结论**: IRT calibration decomposition 是 primary contribution（θ 估计 53% MAE 减少，vanilla 2PL ≈ ContamCal）。RRF 3-signal 为 secondary，domain γ heterogeneity 为 exploratory（J=13 underpowered，仅 Social_Sciences γ=-0.57 显著）
- **D129 是关键 pivot**: Framing 从 γ-centric 转向 Direction A（IRT calibration primary），全文已按此 reframe
- **D131**: Cross-family v5 结果已确认 IRT calibration 跨家族有效，这是论文的 robustness claim
- **易错点**: `exp_006_cross_family_irt_j16`（J=16，本次失败的）和 `exp006_cross_family_pooled_irt`（v5，已成功）是不同实验。v5 已经支撑了论文的 cross-family claim，j16 是后续扩展。不要因为 j16 失败就认为 cross-family 证据缺失
- **论文状态**: 10 项检查全 PASS，7 页正文 + 2 页 ref + 2 页附录 = 11 页，0 critical warnings。距投稿 8 天，主要等 Director 审稿确认


---
