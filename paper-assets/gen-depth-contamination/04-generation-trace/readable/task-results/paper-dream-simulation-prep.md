# paper dream simulation prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_dream-simulation-prep_20260519T044614_result.json`
- **Structured JSON:** [`a48df51b3c4f037f2440.json`](../../sessions/a4/a48df51b3c4f037f2440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the checklist report.

---

## Dream Simulation 前置检查报告

### 1. paper_framing.md 完整性

| 检查项 | 状态 | 说明 |
|--------|------|------|
| C1' 实验支撑 | **部分缺失** | C1'(a) 列 7/8 configs，但 LaTeX 正文/abstract 报 8/9（含 Qwen-14B）。paper_framing 缺 Qwen-14B 数据行 |
| C1' Code domain | **待更新** | paper_framing 明确标注 "LLaMA/Mistral/Qwen-7B Code 结果待更新"，对应 3 个 RUNNING 实验 |
| C3 实验支撑 | **需重审** | exp_026_arxiv_filtering=DONE/negative, exp_025_pythia_filtering=DONE/negative。paper_framing C3 仅 claim web text binary filtering 优势，但 "K* determines filtering granularity" 的隐含预测（arXiv K*=3 应 graduated 更优）被否定，reviewer 会追问 |
| Story Spine 最新结果 | **基本完整** | retrain K*=7 跨模型、Code Qwen K*=2、4 域阶梯均已包含 |
| Anticipated Concerns | **覆盖 Pythia Code K*=1** | Concern #5 明确讨论，框架为 domain ceiling + competence |
| C3 negative results | **未覆盖** | Concerns 列表无条目讨论 arXiv filtering negative / Pythia filtering negative |

### 2. experiment_plan.yaml 覆盖率

| 检查项 | 状态 | 说明 |
|--------|------|------|
| P0 实验完成度 | **全部 DONE 或 RUNNING** | 无 P0 仍为 planned |
| exp-028 不一致 | **确认** | plan 中 `registry_id: null`，但 registry 中 `exp_028_power_curve` 和 `exp_028_subsampling_power` 均 DONE/success。需更新 plan |
| exp-009 链接 | **注意** | plan 链接 `exp_009_dose_50pct` (DONE/failed)，但 v3 版本 (10%/30%/50%) 均存在于 registry。plan 未更新 |
| exp-014 | **未执行** | P2，registry_id=null，naturalistic validation 未做（可接受，P2 优先级） |
| RUNNING 实验 (4) | `exp_code_llama8b`, `exp_code_mistral7b`, `exp_code_qwen7b`, `exp_32b_c4` |
| PREPARING (2) | `exp_olmo_retrain_v2`, `exp_008_retrain_chain` |

### 3. LaTeX 文件状态

| 文件 | 状态 | 问题 |
|------|------|------|
| **main.tex abstract** | **数字不一致** | Abstract 写 "8/9 model configurations"，paper_framing C1'(a) 写 "7/8"。根源：abstract 含 Qwen-14B，paper_framing 表格缺 Qwen-14B |
| **experiments_c1.tex** | **Code 段落已写** | 引用 `tab:code_crossmodel_kstar`，正文写 "Qwen K*=2, Pythia borderline K*=1"，但 domain_kstar 表中 3 个模型 Code 列为 "---" |
| **code_crossmodel_table.tex** | **3/5 TBD** | Qwen-7B, LLaMA-8B, Mistral-7B 全部 TBD，caption 标注 "remaining models pending completion" |

### 4. Dream Simulation 更新清单

#### Critical Blockers（必须在 dream 前完成）

1. **paper_framing C1'(a) 补 Qwen-14B 数据行**，对齐 abstract 的 8/9 统计
2. **添加 Anticipated Concern：arXiv filtering negative result**。Reviewer 必问："If K* determines optimal filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)？" 需要预备 defense（e.g., 训练数据量不足以体现 graduated 优势、LoRA capacity constraint、arXiv 占比低导致 downstream metric 不敏感）
3. **exp-028 registry_id 更新**：plan 中填入 `exp_028_power_curve`

#### Nice-to-Have（dream 后可补）

1. Code 3 模型 RUNNING 实验完成后更新 `code_crossmodel_table.tex`（去掉 TBD）和 `domain_kstar` 表
2. exp-009 plan registry_id 更新为最终 v3 版本
3. paper_framing Story Spine 中 Code domain 描述从 "Qwen-1.5B confirmed" 扩展为包含 3+ 模型结果

#### 预测 Dream Reviewer 主要 Weakness

1. **C3 可证伪性弱**：paper claim "K* determines filtering granularity"，但 arXiv K*=3 时 graduated filtering 并未优于 binary（exp-026 negative），Pythia filtering 也 negative（exp-025）。C3 的 evidence 仅限 Qwen + C4 web text，泛化性不足
2. **Code domain 数据不完整**：5 模型表格 3 个 TBD，domain hierarchy claim (C4≥Code≥Wiki) 仅基于 2 个模型
3. **C3 effect size 小**：MMLU 30% ratio p=0.074 不显著，paper_framing 已标注 defensive framing，但 reviewer 可能仍认为 practical impact 不足
4. **Model family imbalance**：Limitations 已承认 Qwen 占 5/9 configs，reviewer 可能 push back
5. **θ=0.60 敏感性**：多个 boundary case CI 距 θ 极近（Qwen-cont +0.2pp, LLaMA +0.3pp），reviewer 可能质疑 K*=2 判定的 robustness

---
