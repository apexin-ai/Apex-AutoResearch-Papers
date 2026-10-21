# reviewer / loop_4.md

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`252ab23323e6a030c8d3.json`](../../sessions/25/252ab23323e6a030c8d3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-23T19:44:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是理论+数值验证论文（无GPU训练），所有实验是本地CPU Python脚本，不涉及GPU设备号约束
- 论文 ε 数值必须与 JSON 结果文件严格一致——已发生两次不一致（0.008→0.02, 0.004→0.005），审稿人可机械核查
- e2e_demo 使用对称 C₀（diagonal=0.7, off-diag=0.15），恰好是 Theorem 2 精确成立的特殊情况——appendix 已加 caveat（commit 8c847dc），但若有人改 demo 参数必须同步更新
- 97.3% 是 **非比例效应下的符号保持率**，不是"满足比例效应条件的比例"——method.tex 已修正（commit 2f15106），不可回退

### 2. 🖥️ 基础设施快照
- 服务器：home-1x5090(sonny)，远程代码根 `/home/sonny/causal_annot_error_attrib`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- 论文源：`docs/paper/`（main.tex 入口），LaTeX 本地编译
- 关键结果文件（本地 `artifacts/` 下）：`adversarial_monotonicity_results.json`、`k3_symmetric_verify_results.json`、`e2e_demo_results.json`、`symmetry_deviation_results.json`、`exp_proportional_real_matrices_results.json`
- 无 W&B、无训练进程、无 cron、无活跃 PID

### 3. 📊 当前状态
本 session 完成 8 次 worker 审查（MF-1a/1b, MF-2, SF-2 ×2, MF-1a rerun N=1000, W4 symmetry, R20 data traceability），全部已 post to Director。

最新 commit：`04a84ad`（ε 0.004→0.005 修复）。R20 W1-W9 修复已全部落地（commits f3a1f4b → 04a84ad）。

**最后一条审查报告**发现 Remark rem:symmetry 两处小错未修：
- "8 VAST configurations" → 实际 10 个
- "median d_rel=0.31" → 实际 0.330

Registry 无 RUNNING/PREPARING 实验。等待 Paper Agent 修正上述两处数据后可能触发新一轮章节审查。

### 4. 📋 待办
- Paper Agent 提交 rem:symmetry 修正（8→10, 0.31→0.33）→ 核实 appendix_proofs.tex 对应行
- Paper Agent 提交全文章节审查请求 → 按模式 B 逐维度审查，使用 paper-quality-lessons.skill.md + reviewer-audit-checklist §7，返回维度评分模板
- DDL 2026-05-25 前若有新 commit → 重点检查：abstract ≤200 words、正文 ≤8 页、Limitations 在正文不在 appendix、无重复 Limitations section
- 若 Director 转发 Framing 调整提案 → Read negative-framing-review.skill.md，四维度审查

### 5. 🎯 战略上下文
**核心结论链**：K≥3 打破二分类 attenuation guarantee → 7 拓扑分 safe/fragile → ASV 量化脆弱性 → FWL invariance 证明 4 类拓扑校正无效 → Algorithm 1 路由

**Theorem-Conjecture 边界是最敏感攻击面**：Theorem 1（K=2）和 Theorem 2（K=3 symmetric + proportional）都是精确结果；Conjecture 1（general K≥3, ε<0.02）靠 646K 数值曲线支撑。论文已加"From proofs to numerical evidence"过渡段（commit f3a1f4b），但审稿人仍可能攻击 Conjecture 缺乏解析证明。

**易判断错的点**：
1. 不要混淆 "proportional effects 比例" 和 "sign preservation 比例" — 前者是 prop_in_01=85%，后者是 sign_pres=97.3%
2. K=3 经验矩阵全部严重非对称（d_rel 0.29-0.38），Theorem 2 理论价值 > 实用价值
3. e2e demo 的 IV 结果（-139%）是 PPI++ 误用于 IV，不是 MC-SIMEX 结果 — 论文措辞 "topology-agnostic IV correction" 是指无视拓扑盲目用 PPI++


---
