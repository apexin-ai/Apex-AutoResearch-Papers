# reviewer / loop_16.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`eb92d6cbbd8f01b45c8d.json`](../../sessions/eb/eb92d6cbbd8f01b45c8d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-17T06:41:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-5 全部属于本项目（6× RTX 4090D, cqa1-21977）
- MMLU domain IRT 正在重跑（D127: J=13，排除 0.5B）— 新结果出来前论文中 γ 数字全部 pending，不可引用旧 J=21 结果作为最终数据
- Paper 声明必须与实际一致：如果 rerun 后 Math γ 不再显著，不可保留 "γ=+0.97" claim
- Bib 中 `lalor2024irt` 已被替换为 EACL tutorial 数据（fabricated entry 已清除），不可恢复旧版

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，代码根目录 `/root/contamcal-irt-calibration`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 论文目录：`artifacts/paper_draft/`（main.tex + 8 section files + references.bib）
- IRT 结果目录：`/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/`（旧 J=21），rerun 结果路径待确认
- Stan model：`/root/contamcal-irt-calibration/stan_models/contam_irt_2pl_gamma.stan`（scalar γ per domain fit）
- 活跃进程（截至 06:26 UTC）：GPU 0-5 全占（eval PID 943337/943406/943479/935048 + signals PID 946440/947036）
- 无 wandb 配置

### 3. 📊 当前状态
**刚完成**：Paper Agent Step 5 Round 2 评审（score 4/10，3 CRITICALs 仍在）+ 确认 0.5B position bias 混淆后建议 rerun

**正在进行**：
- D127: MMLU domain IRT J=13 rerun（CPU Stan MCMC，~1-4h，blocking）
- D126: Paper Agent reversal patch（恢复 "exclude 0.5B" + 等 J=13 数字）
- Exp-009: Instruct 模型 eval + signals（GPU 0-5 全占）

**等待**：
- J=13 rerun 完成 → 需要审查新 γ 值是否仍显著
- Step 5 Round 3 提交（依赖 J=13 + reversal patch 完成）

### 4. 📋 待办
- J=13 rerun 完成 → 审查 Math/Science γ 是否仍 CI excludes zero + PPP acceptable；如果 Math γ 大幅下降或变 non-sig → 立即 post critical 给 Director 要求 framing 调整
- Step 5 Round 3 提交 → 用 §5.3 模板评分；重点验证 simulation 条件已统一（12 vs 20）+ J 数字全文一致
- Exp-009 完成 → 审查 Instruct 模型结果是否合理（特别关注 DeepSeek below-random 问题是否已解决）
- 最终提交前 → reference-audit skill 做全面引用验证

### 5. 🎯 战略上下文
**核心结论链**：D118→D119→D121→D127 = 从 "Simpson's Paradox" 退到 "Dilution Masking"，从 J=24 退到 J=13。每次退步都是数据诚实性驱动。

**最容易判断错的事**：
1. 不要看到 J=13 的 γ 变 non-significant 就认为论文完了——value decomposition（IRT calibration 本身有效）仍然成立，只是 C1 "domain-differential diagnosis" 需要降级
2. 论文有两个独立贡献轴：(a) calibration via IRT, (b) diagnosis via γ。即使 γ 弱化，(a) 仍可作为 primary contribution
3. `results_mmlu_domain_gamma_n24` 目录名含 "n24" 但实际数据是 J=21（含 0.5B）或 J=13（排除后）——不要被目录名误导
4. Cross-family 结果全 non-sig 是已知事实，不是 bug——论文已降级为 "calibration robustness" claim
5. Simulation 条件：Method 写 12/120，Results 写 20/200——Agent 至今未修，Round 3 必须再检


---
