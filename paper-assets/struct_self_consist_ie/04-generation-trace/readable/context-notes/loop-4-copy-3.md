# reviewer / loop_4.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`7d6d45d31a80421e5e90.json`](../../sessions/7d/7d6d45d31a80421e5e90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-14T21:46:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：autodl-5090 的 cuda:0/1/2/3（`execution.gpu_ids`）。当前全部空闲，无活跃训练进程。
- `voting_conf` 信号存在两套不同实现：主 pipeline（`analyze_*.py`）取所有 entity 的 mean(count/N)；bootstrap（`run_bootstrap_loo.py`）只取 majority (>n/2) entity。**bootstrap 的 voting_conf CI 不适用于论文报告的 ρ 值**——已报 Director CRITICAL，尚未确认是否修复。在修复前，论文中 voting_conf 的 CI/显著性结论不可信。
- Qwen SciERC 3-seed 数据中 EM 和 voting_conf 仅有硬编码值（从 `all_signals_report.json` 提取），不在 `bootstrap_ci_summary.json` 中——如果论文需要这两个信号的 bootstrap CI，需要补跑。

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090(root)`，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型 checkpoints：`checkpoints/qwen3-8b-scierc-merged-v2`、`checkpoints/qwen3-8b-conll2003-merged`、`checkpoints/llama3.1-8b-scierc-merged`、`checkpoints/llama3.1-8b-conll2003-merged`
- 数据集：`data/scierc/processed_data`（551 实例）、`data/conll2003`（3453 实例）
- 图表输出：`artifacts/figures/`（3 PDF+3 PNG，05:40 更新），旧版在 `figures/paper/`（仅 heatmap）
- 活跃进程：无（全部 GPU 实验已完成，Writing 阶段）
- Bootstrap 结果：`output/bootstrap_ci_nscaling/results.json`（含 LLaMA_CoNLL）、`output/bootstrap_ci_summary.json`（统一汇总）

### 3. 📊 当前状态
刚完成三轮 worker 审查：
1. **paper_figures_core_3figures**（status=failed）：图表实际已生成，failure 是后续步骤问题。已报 info。
2. **llama_conll_nscaling_bootstrap**（status=done）：数据一致性通过（SJ/FK/logprob 匹配），但发现 voting_conf 实现不一致（CRITICAL 已报）。N-scaling actual CI 跨零（方向性正，p~0.95），paired CI 显著。
3. **fix_heatmap_3seed_p0_v2**（status=done）：修复了我之前报告的 `*0.95` fallback + 数据源混用问题。验证 PASS。

Registry 中 PREPARING 状态的实验（exp008_re_n16 等 7 个）均为历史残留，不再有活跃任务。
Writing 阶段：Paper Agent 在做 Step 4 章节写作，method.tex 有 3 个 CRITICAL 待修正，related_work 和 discussion 未完成。

### 4. 📋 待办
- Director 回复 voting_conf bootstrap CRITICAL → 如果决定修 bootstrap 代码，审查修复后的 CI 值；如果决定论文中不报 voting_conf CI，确认 experiments.tex 中无此 claim
- Paper Agent 提交 method.tex CRITICAL 修正（FK/EM/SJ 公式）→ 审查修正后公式是否与代码实现一致（源码在 `code/consistency.py`、`code/analyze_*.py`）
- Paper Agent 提交 related_work / discussion → 按 §5 章节审查维度审查
- 如果收到 `paper_agent_request_review` → 使用 §5.3 评分模板返回维度评分
- bootstrap_ci_summary.json 更新后 → 验证 Qwen SciERC EM/voting_conf 是否补全

### 5. 🎯 战略上下文
- **核心结论**：structural consistency (SJ + voting_conf) > logprob 作为 IE 质量估计器，跨 2 模型 × 2 数据集 × 3 seed 一致成立。但存在 correlation-selection gap（ρ 高不代表 selection F1 高）。
- **最易判断错的事**：
  1. 不要把 `run_bootstrap_loo.py` 的 voting_conf CI 当作论文 ρ 值的 CI——信号定义不同（majority filter vs 全 entity mean）。这是目前唯一未解决的 CRITICAL。
  2. N-scaling 的 actual（unpaired）分析 CI 跨零，但 paired 分析显著。论文中如果 claim "statistically significant N-scaling"，必须明确是 paired 分析。
  3. RE 结构信号系统性弱于 NER 是 task 本质属性（D041），不是 bug。
  4. WNUT-17 已放弃（D043/D045），报告为 Claim 3（capability boundary）证据。
- **DDL**：ARR May 2026-05-25，距今 11 天。全部 GPU 实验完成，瓶颈在论文写作迭代。


---
