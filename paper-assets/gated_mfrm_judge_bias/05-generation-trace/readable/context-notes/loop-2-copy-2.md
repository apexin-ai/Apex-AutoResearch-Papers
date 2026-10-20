# agent / loop_2.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`e7548d6970b69e54741f.json`](../../sessions/e7/e7548d6970b69e54741f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-23T21:36:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx6000-4x cuda:0/1/2/3 + autodl-8gpu cuda:0/1/2/3，共 8 张。用白名单外的 GPU 必须 push back Director
- exp-004 状态是 ALLOCATED/success（registry 遗留态），实际已完成，不要重新提交
- exp-001 被误标 failure_reason（startup recovery 假失败），实际 success，registry 需修正但不影响数据
- Stage 2 exposure estimation 默认权重 75/25（reference-anchoring / cross-model-agreement），exp-013 正在验证这个配置——结果出来前不要改权重
- 论文已 14 页（8 正文 + 6 Appendix），Round 3 审稿等用户审批，未审批前不动 paper 文件

### 2. 🖥️ 基础设施快照
- **rtx6000-4x**: 工作目录 /root/gated_mfrm_judge_bias/，Python /root/miniconda3/bin/python3，conda base 环境
  - 数据：exp001/results/（9 judge 判断数据）、exp002/results/exposure_scores.csv
  - 模型输出：exp003/output_003b/（G-MFRM InferenceData joint_gmfrm_idata.nc）
  - exp-013 代码：/root/gated_mfrm_judge_bias/exp013/run_exp013.py
  - exp-013 日志：~/runs/gated_mfrm_judge_bias/exp-013.log
- **autodl-8gpu**: 同结构 /root/gated_mfrm_judge_bias/，exp-006/exp-w7-ablation/exp-008 结果在此
- 活跃进程：exp-001 可能仍有残留进程 PID 525427（reconcile 显示 still running，需确认是否是 Llama 收集的尾巴）
- **Worker 在跑**：worker_analysis_exp-013_20260523T052624（分析 exp-013 结果，等回调）

### 3. 📊 当前状态
收到 exp-013 cron 回调（进程正常退出，ANALYZING）。已 spawn Worker 分析结果，等 Worker 回调。

Registry 状态：
- **ANALYZING**: exp-013（Stage 2 权重敏感性，4 种权重配置 x G-MFRM MCMC）
- **ALLOCATED**: exp-004（遗留态，实际已完成 success）
- **DONE**: 其余 13 个实验（10 success / 3 negative）
- **RUNNING**: 无（所有 8 张 GPU 空闲）

等待中：
- Worker 回调：worker_analysis_exp-013 → 拿到 metrics 后更新 registry + 汇报 Director
- Director 决策：Round 3 审稿模式审批
- exp-001 PID 525427 状态待确认

### 4. 📋 待办
- Worker exp-013 分析回调到达 → 读 metrics → update_registry(conclusion/metrics/checkpoint_path) → 判断 R1-W6 open issue 是否关闭 → 汇报 Director（带 [资源] 行）
- exp-013 conclusion=success（τ 变化 < 0.02）→ R1-W6 resolved，ROADMAP 更新，论文 Appendix 可补充权重敏感性表
- exp-013 conclusion=negative（τ 变化 ≥ 0.02）→ 需要重新评估 75/25 默认配置，汇报 Director 决策
- 所有 8 张 GPU 空闲 → 汇报 Director 时必须提出 GPU 利用建议（是否有新实验要铺、或 Round 3 审稿后可能需要补实验）
- exp-001 PID 525427 确认 → 如已结束则清理 cron

### 5. 🎯 战略上下文
- 项目核心：G-MFRM joint calibration 同时建模 judge bias + benchmark contamination，用 OVB 理论框架讲 story
- 关键结果链：mvp_001(neg) → mvp_002(neg/convergence) → mvp_003(success, NCP fix) → exp-003(neg/horseshoe) → exp-003b(success, τ=0.857 +7.1pp, HalfNormal prior) → 下游验证全部 success
- 论文 story 重心已从 Claim 3 (ranking improvement) 转移到 Claim 1+2（OVB 理论 + contamination detection），因为 Bootstrap Δτ CI 包含 0（D022）
- exp-013 对应 ROADMAP 的 R1-W6 open issue（低优先级），如果 success 则 25 个 review issues 只剩 R1-MT（Murphy-Topel CI width）1 个 open
- 易错点：不要把 exp-004 当作待提交实验——它虽然状态显示 ALLOCATED 但 conclusion=success，是 registry 历史遗留
- 易错点：exp-003 和 exp-003b 是同一个实验的两次跑，exp-003 horseshoe prior 收敛失败(negative)，exp-003b HalfNormal prior 修复后 success，引用结果时用 exp-003b


---
