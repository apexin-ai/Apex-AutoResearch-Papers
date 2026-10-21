# reviewer / loop_3.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`38d750d76fb31dbf1b12.json`](../../sessions/38/38d750d76fb31dbf1b12.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T19:09:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 训练，全部是 API 实验 + 论文写作。无 cuda 设备约束。
- 论文正文严格 8 页（EMNLP 2026 long paper），当前恰好卡在 8 页边界，任何文本增加必须编译验证。
- Mitigation 数据有 v1 (plan_011, 5-model unpaired) 和 v2 (plan_016, GPT-5.4 matched-pair) 两套，绝不能混为同一实验引用。v1 数据：overall -6.6pp/-8.5pp（加权/unweighted），auth_scope -18.0pp。v2 数据：generic +1.3pp，auth_scope -12pp (p=0.07)，incompleteness +14pp。
- Cross-domain 分析有两个 Worker 产出矛盾结果：Worker 1 (p=0.187, rates ~41%) vs Worker 2 (p=0.007, rates ~50%)。**Worker 1 与论文主表一致，应采用 Worker 1**。论文当前已采用 Worker 1 数据（interaction p=0.19, type ρ=0.26）。
- 3 个 Anonymous bib 条目 (arXiv:2505.12543, 2604.02022, 2602.03100) 暂可接受，camera-ready 前必须更新实际作者。

### 2. 🖥️ 基础设施快照
- 服务器：localhost (ubuntu)，纯本地工作
- 工作目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/`
- 论文源码：`docs/paper/sections/*.tex`，主文件 `docs/paper/main.tex`
- 分析产出：`artifacts/` 下各子目录（full_study/analysis/, mitigation_study/, perturbation_extended/ 等）
- 关键数据文件：
  - `artifacts/full_study/analysis/clause_variance_decomposition.json` — 方差分解（ICC=0.386 ambiguous, 0.189 full）
  - `artifacts/analysis_type_mechanism_mapping_summary.md` — MI/NMI 数据
  - `artifacts/analysis_cross_domain_mitigation_summary.md` — Worker 1 cross-domain（可信）
  - `artifacts/analysis_cross_domain_summary.md` — Worker 2 cross-domain（不可信，rates 偏高）
- SOPBench 代码：`artifacts/sopbench/`，已完成 routing 配置，3/5 模型已跑完
- 无活跃进程、无 tmux、无 cron

### 3. 📊 当前状态
R17 fresh review 回来 3.5（vs R16 continue review 4.0）。两个新 must-fix 待处理：

**W-N1 [MF]**："30×" MI ratio 未归一化。已验证 NMI 数据存在：NMI ratio = 0.2316/0.0138 = 16.78 ≈ 17×。全文 30× → 17× 是纯文本替换。

**W-N2 [MF]**：22.4% LPM 方差分解 df 膨胀。审稿人 "null ~10%" 估算正确（294 df / 2996 obs）。Director 计划跑 permutation test (1000×) + GLMM 补充。我预判 permutation p << 0.001（因为 ICC=0.386 是真实信号）。**这个 permutation test 是当前最高优先级的新计算任务。**

Registry 全部 DONE（17 个实验），无 RUNNING。
等待 Director 分配 Worker 执行 W-N1/W-N2 修改 + permutation test。

### 4. 📋 待办
- W-N2 permutation worker 完成 → 核实 p-value 和 null distribution 统计量，验证论文中的表述是否准确引用
- W-N1 文本替换 worker 完成 → grep 确认全文无残留 "30×"，验证 NMI 数字与 `analysis_type_mechanism_mapping_summary.md` 一致
- SOPBench 5/5 模型完成 → 审查是否值得加入 appendix 作为 cross-benchmark replication（如果 Δ 显著）
- 如果 permutation 结果 p > 0.05（极低概率）→ fallback 策略：用 ICC=0.386 (ambiguous condition) 替代 22.4% 作为主论据，不受 df 批评
- 最终提交前 → 编译验证 8 页限制，全文一致性扫描（数字、术语、cross-ref）

### 5. 🎯 战略上下文
**核心叙事**：Policy ambiguity is nocuous for LLM agents (+34pp, conditional OR=15.1)。Clause wording dominates variance (22.4%), not type (0.4%) or model (1.0%)。Taxonomy 价值在于诊断 failure mechanism（NMI 17×），不在于预测 violation rate → "diagnostic taxonomy"。

**审稿历程**：R14→R15 从 "risk gradient" 转向 "intervention-design framework" → R16 降级为 "diagnostic taxonomy"（reviewer 认为 "framework" overclaim）→ R17 要求 NMI 归一化 + LPM df 验证。每次降级都是正确的——不要试图回升措辞强度。

**最容易判断错的事**：
1. 不要混淆两个 ρ=0.90：一个是 LLaMA replication (plan_013, C2 rank)，另一个是 cross-judge sans auth_scope (C2 rates)。前者在 appendix model expansion，后者在 §5.2 和 limitations。
2. 不要把 -8.5pp (v1 unweighted model mean of type-specific) 和 -6.6pp (v1 weighted aggregate) 混淆——两者都是 plan_011 的合法数字，计算方式不同。
3. §7 Discussion L11 "reverses across formulations (−3.3 vs. +14 pp)" 仍混合 v1/v2 数据，但 "across formulations" 措辞已足够诚实，不需要再改。
4. DDL 是 2026-05-25（ARR May cycle）。距今约 3 天。所有修改都是文本/计算级别，无新 API 实验。


---
