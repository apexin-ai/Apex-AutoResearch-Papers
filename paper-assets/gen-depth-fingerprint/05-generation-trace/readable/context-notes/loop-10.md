# agent / loop_10.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`343dad49ca64444ea770.json`](../../sessions/34/343dad49ca64444ea770.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-16T04:40:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 cuda:0-3（4× RTX 5090）。禁止使用任何其他设备
- Primary metric 是 **binary LOGO F1=0.723**（gen-1 vs gen-2+，排除 gen-0 leakage），不是 3-class F1
- Scope 限定 **base models only**——instruct 模型 depth signal 被长度伪影主导（D019 已撤回 instruct narrative）
- plan-004 downstream 是 **negative 结果**（D023/D029），Contribution #3 已降级为 supplementary analysis，不要把它当正面证据写
- paraphrastic 数据中 rp=1.3 会制造 feature reversal artifact，任何涉及 plan-006 数据的分析必须先按 rp 值过滤

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-5090**，账号 root，工作目录 `/root/gen-depth-fingerprint`
- Python：预置镜像 `aml-train`，用 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），**不是 venv**
- 数据：`/root/gen-depth-fingerprint/data/features_all_models.csv`（27529 条，6 generators × 5 depths）
- 活跃进程：**无**。0 个 running worker，0 个 active cron，4/4 GPU 空闲
- W&B / HF cache：按 AutoDL 规范在 `/root/autodl-tmp/` 下

### 3. 📊 当前状态
**Round 3 审稿处理中**，Overall 3.0 / Findings acceptance。DDL: **2026-05-25**（剩 9 天）。

刚完成的事：
- D029/D030 决策已落地：framing 大幅重写为 "base-model recursive generation controlled study"
- review-exp-a-baseline-ensemble (DONE/success)：4-det+surface ensemble F1=0.805，7-feature F1=0.789，baseline 对比完成
- 论文已 fit 到 8 页（downstream table 移入 appendix，related work 压缩）

Registry 状态：所有实验 DONE（成功 44 / 负向 4 / 失败 8）。**无 RUNNING/PREPARING 实验**。

等待中：
- **Paper Agent 应在执行 ROADMAP 中的 Day 1-2 Critical 任务**（N1 framing 重写、N2a bootstrap CI、N2b downstream 移除、N3 Table 1 改造）——但当前 0 worker running，需要确认 Paper Agent 是否已完成或需要重新派发
- report.md 列出 plan-004-prep / plan-001-restore / mvp-001 系列为"准备中"，这些是历史残留，Round 3 不需要新实验

### 4. 📋 待办（条件触发式）
- **立即**：确认 Paper Agent 进度——N1/N2a/N2b/N3 是否已完成。若未完成 → spawn worker 执行 ROADMAP Day 1-2 Critical 任务
- N1+N2b 完成 → spawn worker 执行 Day 2-3 Warning 任务（W1-W6, D1b）
- Day 2-3 完成 → spawn worker 执行 Day 4-5 Minor+Polish（M1-M6, MR, M7）
- 全部修改完成 → spawn review_reviewer worker 做内部审查（Day 6-7）
- N2a bootstrap CI 需要 GPU（<1h）→ submit_on_allocated 跑 bootstrap 脚本
- 所有论文修改完成 → reference-audit + paper-visual-review → 最终编译提交

### 5. 🎯 战略上下文
- **核心结论链**：递归 LLM 生成链展现 differential depth response（central-tendency 漂移 + shape 稳态）。7-feature ensemble 跨 6 generators / 3 families / 3 prompt types 验证。binary LOGO F1=0.723（leak-free）
- **D029 是转折点**：Round 3 审稿要求把 framing 从 "web-crawled provenance" 收窄到 "base-model controlled study"。这意味着 abstract/intro/discussion 全部需要重写，不是小修
- **最容易判断错的事**：plan-004 downstream 是 negative，但论文中仍保留为 supplementary analysis（不是 contribution）。不要试图"救"它或重新跑——D023/D029 已决定降级处理
- **Claim 证据状态**：Claim 1 (depth discriminability) ✅ | Claim 2 (differential depth response) ✅ | Claim 3 (downstream) ⬇️降级为 supplementary
- **时间风险**：9 天内完成 framing 重写 + 全部 minor fixes + 内部审查 + 提交。论文已 8 页，改动空间有限。优先级：N1 framing > N2/N3 统计 > W 系列 > M 系列


---
