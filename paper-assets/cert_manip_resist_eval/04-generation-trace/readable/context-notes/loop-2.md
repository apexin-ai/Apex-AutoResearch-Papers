# director / loop_2.md

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`06a4cbd5421d82a6fa37.json`](../../sessions/06/06a4cbd5421d82a6fa37.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-25T06:02:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 只有 seetacloud-rtx6000 的 cuda:0（单卡）
- 论文主文严格 ≤8 页（EMNLP 2026），Limitations 不计入。当前刚好卡在 8 页边界，任何正文增加都可能溢出
- Abstract ≤200 words（当前 ~154 words）
- 结论已被极限压缩到 2 行，不能再扩展（之前 Paper Agent 扩展导致溢出，被反复修剪）
- Table 2 定义已从 results.tex 移到 methodology.tex（§4.2 后），Table 1 从 methodology.tex 移到 threat_model.tex 末尾——这是布局优化，不要移回去

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-rtx6000，GPU cuda:0
- 论文目录：`projects/cert_manip_resist_eval/docs/paper/`（本地 workspace）
- 代码目录（远程）：需从 project config 确认 `execution.project_path`
- r1w2-fp16-baseline 实验在远程服务器运行中（FP16 vs AWQ 对比）
- 无活跃 W&B / cron 任务

### 3. 📊 当前状态
刚完成：
- R5 审稿全部修复整合到论文（fractional logit 9/12 flat 修正、β_std 轨迹、quant dummy、API-only power、Bayesian entropy、K_eff framing 降级、scope qualifier、OpenRouter footnote）
- 图表布局重排（Table 2 → p5, Table 1 → p4，解决 p3-5 纯文本墙问题）
- R6 审稿已提交（apr_20260524T194848_a22r，pending 用户审批，推荐 continue 模式）
- PDF 已上传给用户（main_layout_rebalanced.pdf）

Registry: `r1w2-fp16-baseline` RUNNING（Qwen2.5-14B/32B AWQ vs FP16 accuracy 对比，验证量化是否引入 <2pp 精度下降）。上一轮已派 Agent 去 SSH 检查状态，Agent 已处理完但未返回明确结果。

等待中：用户审批 R6 审稿模式（continue/fresh）；FP16 实验完成回调。

### 4. 📋 待办
- R6 审稿卡片被用户审批 → 等待 Review Director 出报告，收到后按 `review-report-action` skill 处理
- FP16 baseline 完成 → 分析 AWQ vs FP16 accuracy diff，<2pp 则 R1-W2 resolved，≥2pp 则需调整论文 claim
- 用户反馈第 3 页仍无图 → 可考虑画 Related Work positioning 概念图（PaperBanana），但非必须
- Agent idle 且无待办 → 可派去检查 FP16 进度或准备下一批实验

### 5. 🎯 战略上下文
核心 narrative 已从"K_eff 是独立预测变量"降级为"predictor shift 的系统性记录 + confound 本身作为发现"。这是 3 轮审稿后的根本性重新定位。

关键数据点：
- Predictor shift 是 method-dependent：bootstrap 支持 (4→7→8)，fractional logit 不支持 (9→9→9 flat)，quant dummy 下减弱 (6→6→4)
- Diversity-capability confound r=0.70-0.81，69% 条件下 Cinelli-Hazlett 失败
- API-only 子集 predictor shift 消失（K_eff 2-3/12 vs η_max 8/12），但 power 不足（MDE>0.897）

易错点：
- 不要试图恢复 K_eff 的因果解释——copula 被 97-100% 拒绝，"有效独立通道数"语义已放弃，只保留 motivating analogy
- 不要扩展结论——当前 2 行是页面预算极限
- R5 的 fractional logit 数字是 9/12 at ALL K（不是 4/12→9/12→9/12），之前论文里写错过，已全部修正
- review_issues.yaml 已更新到 R5 修复状态，R4-W4 和 R2-W6 标记为 resolved


---
