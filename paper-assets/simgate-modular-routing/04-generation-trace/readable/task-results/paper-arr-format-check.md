# paper arr format check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_arr-format-check_20260521T123525_result.json`
- **Structured JSON:** [`309efb9fe2d280963ef0.json`](../../sessions/30/309efb9fe2d280963ef0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All files read. Now compiling the full compliance report.

---

## 检查 1: 匿名化验证
**结果**: PASS (0 critical issues, 1 minor suggestion)

- `\usepackage[review]{acl}` — 正确启用 review 模式 (`main.tex:3`)
- `\author{Anonymous}` — 正确 (`main.tex:22`)
- 无真实作者姓名、机构名、个人 URL、email、GitHub 链接
- 无 Acknowledgments 部分 ✓
- 无 "we previously showed" / "our prior work" 等自引暗示 ✓
- 图表 caption 和表格注释中无泄露 ✓
- "Code and data will be released upon acceptance" (`main.tex:54`) — 标准匿名措辞 ✓

### Minor suggestion
1. **[main.tex]** 无 `\hypersetup{pdfauthor={}}` 显式清空 PDF metadata。`[review]` 模式通常会处理，但显式设置更安全 → 建议在 preamble 加 `\hypersetup{pdfauthor={},pdftitle={}}`

---

## 检查 2: Supplementary Materials 打包清单
**结果**: 2 items missing

### 应打包内容清单

**核心代码 (`src/`, 27+ files):**
- `src/episode_level_collection.py`, `src/counterfactual_labeling.py`, `src/death_decomposition.py` — 数据收集与分析核心
- `src/death_aware_labeling.py`, `src/analysis.py`, `src/action_divergence_analysis.py` — 分析模块
- `src/llm_agent.py`, `src/scienceworld_utils.py`, `src/code_sandbox.py` — Agent 与环境接口
- `src/router_sft_train.py`, `src/router_sft_eval.py`, `src/eval_end_to_end.py`, `src/eval_implicit_router.py` — Router 训练与评估
- `src/training/` (5 files): `format_implicit_data.py`, `data_loader.py`, `implicit_router_sft.py`, `router_sft.py`, `__init__.py`
- `src/analysis/` (2 files): `death_decomposition.py`, `rule_based_routing.py`
- `src/evaluation/` (2 files): `prompt_routing_eval.py`, `ablation_comparison.py`
- `src/ablation_*.py` (4 files), `src/plot_death_decomposition.py`, `src/routing_pattern_analysis.py`
- `src/analyze_math_pilot.py`, `src/alfworld_counterfactual.py`, `src/analyze_alfworld_llama.py`, `src/analyze_gemma_scienceworld.py`, `src/compute_cross_model_cis.py`

**脚本 (`scripts/`, 8 files):**
- `scripts/plan008_v2_router_size.py`, `scripts/eval_retrained_seeds.py`, `scripts/leave_one_tasktype_out.py`
- `scripts/matched_daf_comparison.py`, `scripts/w1_cluster_bootstrap.py`
- `scripts/crafter/` (3 files)

**图表生成脚本 (`docs/paper/figures/`):**
- `gen_pipeline.py`, `gen_fig1.py`, `gen_fig2.py`, `gen_signal_reversal.py`

**附录已在 main PDF 中** — 不需单独打包 ✓

### Missing (需创建)
1. **`requirements.txt`** — 项目根目录无依赖声明文件
2. **`README.md`** — 项目根目录无说明文件（ARR supplementary 建议包含代码使用说明）

---

## 检查 3: Submission Form 字段预填
**结果**: 已提取

### Paper Title
> Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld

### Abstract (纯文本)
> LLM agent routing—deciding when to rely on internal reasoning versus external tool use—is typically addressed by training routers directly, without first understanding what mechanistic signal drives the routing preference. This absence of diagnostic methods risks building routers atop confounded or trivial signal. We propose an episode-level counterfactual framework that compares pure-strategy outcomes (internal-only vs. deterministic-only) to decompose routing signal into its mechanistic components before any router is constructed. Applying this framework to ScienceWorld (11 task types, 245 episodes), we find that 78.9% of non-tie routing labels arise from death asymmetry—the internal strategy triggers catastrophic failure while the deterministic strategy survives. This finding is penalty-independent: a derived score-weighted measure, the Death Avoidance Factor, reaches 88–90% across three model families (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), confirming convergence on a single dominant mechanism. Cross-environment probes on MATH and ALFWorld diagnose qualitatively different routing mechanisms—no extractable signal and information asymmetry, respectively—demonstrating the framework's generality. A ~50-episode diagnostic pilot suffices to identify the dominant routing mechanism in a new environment, enabling informed build-vs-buy decisions before expensive router training.

### Keywords (7)
1. counterfactual analysis
2. LLM agent routing
3. tool use
4. catastrophic failure avoidance
5. diagnostic framework
6. interactive environments
7. computation strategies

### Recommended Track
**Primary: Interpretability and Analysis of Models for NLP**
- 论文核心贡献是诊断性框架（分解 routing signal 的机制来源），本质是分析/可解释性工作

**Secondary: NLP Applications** 或 **Large Language Models**
- 应用场景是 LLM agent 在交互式环境中的 routing

### Dual Submission
否

---

## 检查 4: Camera-ready 级 Typo 扫描
**结果**: 1 systematic issue, 3 minor issues

### Issue 1 (Systematic): `\cite` 应为 `\citep` — ~25 处

在 natbib 中，`\cite` = `\citet`，渲染为 "Author (Year)"。当模式为 `SystemName \cite{key}` 时，输出为 "SystemName Author et al. (Year)"——冗余。应改为 `SystemName \citep{key}` → "SystemName (Author et al., Year)"。

**introduction.tex:**
- `L4`: `ScienceWorld \cite{scienceworld-2022}` → `\citep`
- `L6`: `Toolformer \cite{toolformer-2023}` → `\citep`
- `L6`: `ART \cite{art-2023}` → `\citep`
- `L6`: `Chameleon \cite{chameleon-2023}` → `\citep`
- `L6`: `\cite{cogrouter-2026,ares-2026}` → `\citep`
- `L6`: `\cite{mtrouter-2026}` → `\citep`
- `L6`: `\cite{budget-aware-routing-2026}` → `\citep`
- `L10`: `ReAct \cite{react-2023}` → `\citep`

**method.tex:**
- `L9`: `ReAct~\cite{react-2023}` → `\citep`
- `L29`: `ScienceWorld \cite{scienceworld-2022}` → `\citep`

**related_work.tex (最密集):**
- `L5`: `Toolformer \cite{toolformer-2023}` → `\citep`
- `L5`: `ToolACE \cite{toolace-2025}` → `\citep`
- `L7`: `ToolkenGPT \cite{toolkengpt-2023}` → `\citep`
- `L8`: `ART \cite{art-2023}` → `\citep`
- `L8`: `Chameleon \cite{chameleon-2023}` → `\citep`
- `L9`: `ReTool \cite{retool-2025}` → `\citep`
- `L13`: `CogRouter \cite{cogrouter-2026}` → `\citep`
- `L13`: `ARES \cite{ares-2026}` → `\citep`
- `L13`: `Mixture-of-Recursions \cite{mixture-of-recursions-2025}` → `\citep`
- `L13`: `MTRouter \cite{mtrouter-2026}` → `\citep`
- `L21`: `ScienceWorld \cite{scienceworld-2022}`, `ALFWorld \cite{alfworld-2021}`, `AgentBench \cite{agentbench-2024}`, `ReAct \cite{react-2023}`, `Reflexion \cite{reflexion-2023}`, `LATS \cite{lats-2024}` — 全部应改为 `\citep`

**main.tex:**
- `L53`: `ScienceWorld \cite{scienceworld-2022}` → `\citep`

注意：同一论文中已有正确的 `\citep` 用法（如 `experiments.tex:80` `MATH Level~4--5~\citep{math-2021}`），确认是不一致而非故意选择。

### Issue 2 (Minor): 数字格式

- 所有大数字已正确使用 `{,}` 分隔（如 `2{,}040`, `10{,}000`）✓
- 百分号全部使用 `\%` ✓
- 小数点前均有前导零（`0.3` 非 `.3`）✓
- `pp`（percentage points）全文统一使用 `~pp` ✓

### Issue 3 (Minor): 标点与排版

- 连字符/en-dash/em-dash 使用正确 ✓（`7--8B` 数字范围，复合词用 `-`）
- `vs.\` 正确防止句末双空格 ✓
- `cf.\` 同上 ✓
- Figure/Table/Appendix/Section 引用大写一致 ✓
- `\S\ref{}` (§) 和 `Section` 混用 — 无严重问题，全文以 `\S` 为主
- 引号使用 LaTeX 标准 ``` ``...'' ``` ✓

### Issue 4 (Minor): 拼写与术语一致性

- 无明显拼写错误
- "death rate" (名词) vs "death-rate" (定语) — 用法正确 ✓
- "task type" (名词) vs "task-type" (定语) — 用法正确 ✓
- "episode-level", "step-level" — 一致使用连字符做定语 ✓
- "always-deterministic" — 一致 ✓

---

## 总结

### Critical Issues (必须修复)
无。

### High Priority (强烈建议修复)
1. **`\cite` → `\citep`** (~25 处): 系统性引用格式不一致。Reviewer 可能标记为 formatting issue。修复方法：全局替换 `SystemName \cite{` 模式为 `SystemName \citep{`，保留少数确实用作句子主语的 `\citet`（如 `\citet{budget-aware-routing-2026}` 在 `related_work.tex:15` 已正确）。

### Medium Priority (建议修复)
2. **创建 `requirements.txt`** — supplementary 打包需要
3. **创建 `README.md`** — supplementary 打包需要（简要说明代码结构、运行方式、依赖）

### Low Priority (可选)
4. **`\hypersetup{pdfauthor={}}`** — 显式清空 PDF metadata（可能已由 `[review]` 处理）

---
