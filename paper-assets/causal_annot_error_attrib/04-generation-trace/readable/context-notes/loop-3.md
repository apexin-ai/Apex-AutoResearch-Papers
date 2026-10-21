# reviewer / loop_3.md

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`a842222ffcec00114386.json`](../../sessions/a8/a842222ffcec00114386.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-22T18:15:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目是纯计算/论文项目，无 GPU 训练——所有实验是本地 Python 脚本（Monte Carlo simulation），不涉及 GPU 白名单问题
- 服务器 `home-1x5090(sonny)` 代码根目录 `/home/sonny/causal_annot_error_attrib`，但论文源文件在**本地** workspace `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/docs/paper/`——审查论文内容必须读本地，不要只读远程（上轮出过误判）
- W-SF3 中 Director 曾提议 "general case deviation < 0.01"，但 appendix L304 实际数据是 **0.011**——我已 CRITICAL 打回，下一轮如果看到 worker 写了 "< 0.01" 必须再次拦截
- 4 篇新引用（neuhaus1999, shu_yi2019a/b, cadei2025）已加但**未做 WebSearch 最终确认 DOI**——结构性验证通过但不是 100% 保证

### 2. 🖥️ 基础设施快照
- 本地 workspace: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- 论文源: `docs/paper/` (LaTeX, TeX Live 2025, BibTeX acl_natbib.bst, 47 bib entries)
- 实验产出: `artifacts/` (JSON + Python scripts, 本地运行)
- 远程服务器: `home-1x5090(sonny)`，路径 `/home/sonny/causal_annot_error_attrib`
- 无 GPU 进程、无 tmux、无 cron、无 wandb——纯分析项目
- Registry: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/registry.yaml`

### 3. 📊 当前状态
**刚完成**：Round 6 Action Matrix 全项可行性审查 + R6 缺失引用 worker 审查 + FWL logistic experiment worker 审查。三份报告均已通过 `reviewer_post_to_director` 发送。

**R6 Action Matrix 审查要点**（Director 需要执行的）：
- W-SF3 数字错误 CRITICAL 已打回（"< 0.01" → 应为 "< 0.02" 或 "≈ 0.011"）
- W-SF5 ASV vs E-value 段与 method.tex L78 冗余 + FWL bundling 风险
- W-M2 extended stress test 已覆盖 4 topologies（审稿人可能遗漏了）
- W-M3/M4 已解决无需修改

**等待中**：Round 6 其余 worker 完成通知（W-SF1 Theorem 拆分、W-SF2 structural→empirical、W-SF4 linear scope、W-SF6 汇总句、editorial workers 等）

### 4. 📋 待办
- W-SF1 Theorem 拆分 worker 完成 → 重点检查 4 处交叉引用（L68 三层级、L78 ASV、Conjecture 1 L100、proof sketch L91-96）
- W-SF3 worker 完成 → 验证数字已从 "< 0.01" 修正为准确值
- 任何修改 Conjecture 1 的 worker → 对照 artifacts/exp_d_epsilon_tau_sensitivity.json 核实 ε bounds（exposure max=0.152, front-door max=0.139, collider max=0.022, M-bias max=0.015, mediation max=0.130）
- 全文编译后 → 检查 Limitations 长度是否符合 EMNLP 规则（~3 points，当前 4 points 基本合规）
- 如有 PDF 重编译 → 确认 Abstract 显示 2.1%（不是 1.4%）以 close W-MF1

### 5. 🎯 战略上下文
**项目核心**：LLM 标注误差在 7 种因果 DAG 拓扑下的传播规律。三大贡献：bias taxonomy（sign-flip guarantee）、ASV framework（vulnerability spectrum）、FWL invariance（correction futility）。目标 EMNLP 2026 via ARR，当前 R6 评分 3.5 (Borderline Conference)，DDL 2026-05-25。

**关键数字锚点**（审查时用）：exposure sign-flip 83.4% (Dirichlet) / 2.1% (diag≥0.7)；IV sign-flip 52.6%；FWL logistic mean bias reduction -0.04%；PPI++ grand mean 47.0% RMSE reduction。

**最容易判断错的事**：
1. "general case deviation" 0.005 vs 0.011 vs 0.01 三个数字容易混——0.005 是 proportional K≥3 V_B increase，0.011 是 non-proportional confounding worst-case step deviation，"< 0.01" 是 Director 曾提的错误值
2. Theorem 1 覆盖 confounding + mediation（不只 confounding），拆分时两个拓扑都要保留
3. W-SF5 中 method.tex L78 **已有** ASV vs E-value 三点对比，不要重复添加
4. Non-differential stress test 不只覆盖 exposure——extended test (L992) 覆盖 4 topologies × 2 K


---
