# research paper outline prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_paper-outline-prep_20260515T044605.jsonl`
- **Structured JSON:** [`e5833aa4f53421f42399.json`](../../sessions/e5/e5833aa4f53421f42399.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-15T04:48:57.397344+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T04:48:57.397674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T04:48:57.397859+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T04:48:57.398082+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2) — D021: 撤销 D011，重新瞄准 CoRL 2026\\n- ~~ICLR 2027~~ — 不再是首要目标\\n\\n## Core Insight\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode \\\"which action dimensions are uncertain and how they co-vary\\\" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.\\n\\n> ⚠️ **Pending ablation confirmation**: \\\"fundamentally richer\\\" 措辞依赖 Scenario A (perdof > obs_only)。如果 Scenario B/C，Core Insight 需调整为 \\\"uncertainty-conditioned learned correction\\\" 或 \\\"observation-conditioned residual correction\\\"。见备选策略。\\n\\n## Core Claims (2 条，均可证伪) — D022: Claim 3 SRPO stacking 因 CoRL 时间限制移除\\n1. **Learned correction conditioned on uncertainty features significantly improves VLA robustness**: CRM（轻量 MLP）以 uncertainty 特征为条件输入，在 argmin 样本选择基础上进一步校正动作，显著优于纯选择方法。\\n   - **主 claim (硬证据)**: CRM correction 相比 argmin-only selection 有独立增量 (+9.6pp interim)\\n   - **子 claim (待确认)**: Per-DOF conformal features (40D) 作为 conditioning 比 obs-only / scalar 更优\\n   - 验证: MVP (✅ done) + spatial 4-way ablation (perdof vs obs_only vs scalar_unc vs argmin_only, RUNNING) + object benchmark\\n   - Kill criterion (主 claim): CRM correction vs argmin-only < 3pp across both benchmarks → correction 无价值\\n   - Kill criterion (子 claim): obs_only eval >= perdof eval → per-DOF features 无额外价值，启用备选 framing\\n\\n2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆
…[truncated 7634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T04:48:57.398248+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T04:48:57.398475+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-15 03:08 UTC | 更新原因: D023 drop Claim 2, D024 kill v4-default-r3, D025 suspend D019 conclusion, spatial mid-results update\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~11 天。\\n\\n## 当前进展\\n- **阶段**: Phase 2c — Spatial 4-way Ablation (等全 10 task) + Object 4-way 并行铺开\\n- **MVP**: PASS\\n- **Claim 2 (ACI/COC) 已放弃 (D023)**: ACI 需 expert_action，test-time 不可用，11 天内重设计风险过高。CoRL 论文聚焦单 Claim (CRM correction)\\n- **D019 \\\"52.5%\\\" 已失效 (D025)**: perdof 实际 42%@5/10 tasks，仅 +4.5pp over argmin (噪声水平)。obs_only 57.5%@4 tasks 暂时领先。**必须等全 10 task 完成再做 framing 裁决**\\n- **Baselines 锁定**: spatial 30% (K=1), VLA-mean 31% (K=10), object 13% (K=1)\\n\\n## Spatial Eval 进行中（bjb1-18228）\\n\\n| 实验 | Mode | Tasks | 当前 SR | ETA |\\n|------|------|-------|---------|-----|\\n| obs-only-r2 | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ~7h |\\n| v4-small (perdof) | acr_vla, norm=0.1 | 5/10 | 42.0% | ~6h |\\n| argmin-only | reconvla | 8/10 | 37.5% | ~2h |\\n| v4-scalar | crm_scalar, norm=0.1 | 2/10 | 80%* (easy tasks only) | ~6h |\\n\\n## Object Eval 进行中（bjb1-32546, 6/6 GPU 满载）\\n\\n| GPU | 实验 | Mode | 状态 |\\n|-----|------|------|------|\\n| cuda:0 | reconvla-object | reconvla, K=10 | RUNNING (no results yet) |\\n| cuda:1 | acr-object-v4-perdof | crm_perdof, norm=0.1 | RUNNING |\\n| cuda:2 | acr-object-v4-obs-only | crm_obs_only, norm=0.1 | RUNNING |\\n| cuda:3 | acr-object-v4-scalar | crm_scalar, norm=0.1 | RUNNING |\\n| cuda:4 | vla-only-object | vla_only, K=1 | RUNNING (unregistered) |\\n| cuda:5 | vla-mean-object | vla_only mean, K=10 | RUNNING (unregistered) |\\n\\n
…[truncated 2989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T04:48:57.398642+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T04:48:57.399185+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    auth
…[truncated 31298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T04:48:57.399427+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T04:48:57.399568+00:00_

_project
ablation_eval_commands.md
competitive_analysis_20260515.md
competitor_analysis.md
correction_degradation_literature.md
crm-train-v2-k5
crm_bug_audit.md
diag-eval-v6-batch-failure.md
dream_reports
eval-reconvla-spatial-v1-diag.md
fix_plan_code_sketch.md
lerobot-pipeline-alignment.md
libero-smolvla-env-report.md
manifest.yaml
method_section_draft.tex
mvp-point-reaching
object_eval_commands.md
pipeline-dimension-verification.md
precompute-k5
precompute-k5-analysis.md
reconvla-comparison-report.md
report_eval_progress.md
report_running_status.md
smolvla-libero-finetune-survey.md
smolvla_wrapper_fixed.py
spatial_comparison_template.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T04:48:57.399723+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
  "content": "# Spatial Ablation Analysis & Paper Narrative Preparation\n\n> 生成时间: 2026-05-15 | 状态: 分析备忘录（等待全 10 task 完成后裁决）\n\n## 1. 当前数据快照\n\n### Spatial Benchmark（ROADMAP 2026-05-15 03:08 UTC）\n\n| 实验 | Mode | Tasks 完成 | 当前 SR | 来源 |\n|------|------|-----------|---------|------|\n| VLA baseline (K=1) | vla_only | locked | **30%** | ROADMAP baselines |\n| VLA-mean (K=10) | vla_only mean | locked | **31%** | ROADMAP baselines |\n| argmin-only | reconvla | 8/10 | **37.5%** | ROADMAP spatial eval |\n| perdof CRM | acr_vla, norm=0.1 | 5/10 | **42.0%** | ROADMAP spatial eval (v4-small) |\n| obs_only CRM | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ROADMAP spatial eval (obs-only-r2) |\n| scalar CRM | crm_scalar, norm=0.1 | 2/10 | **80%*** | ROADMAP spatial eval (*easy tasks only) |\n\n**注意**: 任务描述中的数字（perdof 42.9%, obs_only 40.0%, scalar 56.7%@3 tasks）与 ROADMAP 不一致。以 ROADMAP 为准，但两者均为中间结果，任何中间排序均可能在剩余 tasks 翻转。\n\n### 关键增量\n\n| 对比 | 增量 | 统计可信度 |\n|------|------|-----------|\n| CRM (any) vs argmin-only | +4.5pp (perdof) 至 +20pp (obs_only) | 低: 4-5/10 tasks |\n| argmin-only vs VLA baseline | +7.5pp | 中: 8/10 tasks |\n| 全 pipeline vs VLA baseline | +12pp (perdof) 至 +27.5pp (obs_only) | 低: 不同 task counts |\n\n### 数据可靠性警告\n- **obs_only** 仅 4/10 tasks，当前领先可能因 task selection bias 翻转\n- **scalar** 仅 2/10 tasks 且均为 easy tasks，80% 完全不可信\n- **perdof** 5/10 tasks，D025 已将 D019 \"52.5%\" claim 标记为失效\n- 所有 CRM variant 排序必须等全 10 tasks 完成\n\n---\n\n## 2. 三种 Narrative 分析\n\n### Scenario A: perdof > obs_only（per-DOF story）\n\n**触发条件**: 全 10 task 后 perdof SR > obs_only SR 且差 ≥5pp\n\n**可能性评估**: **低**。当前 obs_only (57.5%@4) 大幅领先 perdof (42.0%@5)。需要剩余 tasks 中 obs_only 大幅下滑且 perdof 追上。训练 loss 也支持 obs_only（val_loss 0.0165 vs perdof 0.0358，见 D020）。\n\n**Narrative**: \"Per-DOF conformal features encode dimension-specific uncertainty that observation features cannot capture. Despite worse training loss, conformal features' epistemic signal proves critical under distribution shift in closed-loop deployment.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | 开门见山：scalar UQ 丢失维度信息 → per-DOF conformal features 是解决方案。Problem 聚焦 \"information loss in scalar aggregation\" |\n| **Method** | CGS multivariate CP + per-DOF interval extraction 是核心技术贡献。CRM 架构强调 40D conformal feature vector 的设计。Magnitude control 作为工程发现 |\n| **Results** | 主表: 4-way ablation 展示 perdof > obs_only > scalar ≈ argmin。亮点故事: \"training loss 预测翻转\" (obs_only lower loss but worse eval) = compelling evidence for epistemic value |\n| **Discussion** | 强调 conformal features 在 distribution shift 下的 epistemic value 与 in-distribution training loss 的 divergence。与 ReconVLA scalar CP 对比突出信息增益 |\n\n**风险**: 如果 perdof 仅略优于 obs_only (3-5pp)，统计显著性不足，narrative 说服力弱。\n\n---\n\n### Scenario B: perdof ≈ obs_only ≈ scalar（correction-is-key story）\n\n**触发条件**: 全 10 task 后三种 CRM variant 两两差 <5pp\n\n**可能性评估**: **中**。如果 obs_only 在剩余 tasks 下滑，三者可能收敛到 40-50% 区间。\n\n**Narrative**: \"Learned uncertainty-conditioned correction (sample-then-refine) significantly outperforms pure sample selection. The correction mechanism is the contribution, not the specific feature representation.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem: 现有方法止步于 sample selection (ReconVLA) 或需 RL 训练 (SC-VLA)。Gap: 缺少 lightweight learned correction。Our angle: CRM 作为 plug-and-play correction module |\n| **Method** | CRM 架构设计 + magnitude control 是核心贡献。Per-DOF features 作为 \"one valid feature set\" 呈现，不强调其必要性。重点放在 correction mechanism 设计原则（bounded residual, norm control） |\n| **Results** | 主表: CRM (any variant) vs argmin-only 的增量。Feature ablation 作为次要表 \"CRM is robust to feature choice\"。Magnitude control study (norm sensitivity) 升级为独立 contribution |\n| **Discussion** | \"Correction > selection\" 作为主要 takeaway。与 residual policy learning 文献 (Silver 2018, PLD, TRANSIC) 建立联系。Per-DOF 保留用于 online monitoring (future work) |\n\n**优势**: 这是最稳健的 narrative——只要 CRM vs argmin-only ≥5pp 即可成立。不依赖特定 feature variant 排序。\n**风险**: Contribution novelty 降低——\"learned correction helps\" 不够新颖。需要用 magnitude control discovery 和 CoRL 实验规模补偿。\n\n---\n\n### Scenario C: obs_only > perdof（simpler-is-better / observation-conditioned story）\n\n**触发条件**: 全 10 task 后 obs_only SR > perdof SR 且差 ≥5pp\n\n**可能性评估**: **较高**。当前数据 (57.5% vs 42.0%) + 训练 loss (0.0165 vs 0.0358) 均支持此方向。D025 已预警此趋势。\n\n**Narrative**: \"Observation-conditioned learned residual correction is the key contribution. Conformal features provide no additional value as CRM input over observation features, but remain valuable for sample selection quality and coverage monitoring.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem 保持不变（VLA robustness gap）。Gap: 缺少 inference-time learned correction。Our angle: lightweight observation-conditioned residual correction，不需要额外 UQ features |\n| **Method** | CRM 架构 + magnitude control 是核心。CGS/conformal 降为 \"sample selection module\" 的理论基础，不再是 CRM feature。需要解释 per-DOF features 的 negative result |\n| **Results** | 主表: obs_only CRM vs argmin-only vs baselines。Feature ablation 如实呈现——conformal features 不优于 observation features 作为 honest negative result。Per-DOF 在 sample selection 中的角色仍可报告 |\n| **Discussion** | 解释可能原因: (1) 观测特征已隐含编码 uncertainty 信息 (2) conformal 特征在小 K 下噪声大 (3) CRM 容量足以从观测中学到校正方向。将 per-DOF 定位为 \"future direction: larger K + better calibration\" |\n\n**Core Insight 需重写**: \"Lightweight learned residual correction on selected VLA samples significantly improves robustness. The correction module only needs observation features; structured uncertainty features are not required.\"\n\n**优势**: 实际上简化了 method 和 story——不需要解释复杂的 multivariate CP 管线作为 CRM 输入。\n**风险**: (1) 论文标题 \"ACR-VLA\" 中 \"conformal\" 角色弱化；(2) 与 A2C2 (Sendai 2025) 的差异化缩小——都变成了 \"observation-conditioned residual correction\"；(3) Reviewer 可能质疑 \"你们做了这么复杂的 CP pipeline 结果没用？\"\n\n**子情况 C1**: scalar > perdof 但 scalar < obs_only → conformal feature 形式无关紧要，进一步支持 \"correction mechanism is key\" narrative（hybrid of B+C）\n\n---\n\n## 3. 待完成实验及其对 Narrative 选择的影响\n\n| 实验 | 当前状态 | ETA | 对 narrative 的影响 |\n|------|---------|-----|-------------------|\n| **Spatial 全 10 task** (bjb1-18228) | 4-8/10 tasks | ~6-9h | **决定性**: 全部排序确认后才能选择 A/B/C |\n| **Object benchmark 全 10 task** (bjb1-32546) | 刚开始 | ~数小时 after spatial | **验证性**: cross-benchmark consistency。如果 spatial B 但 object A → narrative 困难 |\n| **Magnitude sweep** (norm ∈ {0.03, 0.05, 0.2, 0.3}) | 未开始 | 待 bjb2-28827 部署 | **补充性**: 强化 magnitude control contribution (所有 scenario 均可用) |\n| **K sensitivity sweep** (K=5,10,15,20) | 未开始 | 待 GPU 释放 | **补充性**: 回应 Reviewer Q1 (K=10 covariance reliability) |\n| **Fisher exact test** | 需全 10 task 数据 | post-eval | **统计性**: 判断增量是否 p<0.05 |\n\n**裁决所需最低数据**: Spatial 全 10 task + Object 全 10 task。两个 benchmark 均显示 CRM vs argmin ≥5pp (p<0.05) 才能安全 claim。\n\n---\n\n## 4. CoRL 8 页单 Claim 论文结构建议\n\n### 推荐结构（CoRL 2026, 8 pages + references）\n\n| 章节 | 页数 | 内容 |\n|------|------|------|\n| **Abstract** | — | 一句 problem, 一句 method (sample-then-refine + CRM), 一句 headline result |\n| **1. Introduction** | 1.0 | Problem (VLA robustness gap) → Existing approaches (selection/RL/MLLM) → Gap (no lightweight learned correction with statistical grounding) → Contribution (CRM + magnitude control + empirical findings) |\n| **2. Related Work** | 0.75 | (a) VLA robustness: training-time (RobustVLA, DiG-Flow, SRPO, ACoT) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) (b) CP in robotics (c) Residual policy learning |\n| **3. Method** | 2.0 | 3.1 Multi-sample inference + CGS (0.5p) → 3.2 Conformal sample selection (0.5p) → 3.3 CRM architecture + feature variants (0.5p) → 3.4 Magnitude control (0.5p) |\n| **4. Experiments** | 2.5 | 4.1 Setup: LIBERO-Plus spatial+object, SmolVLA backbone, baselines (0.5p) → 4.2 Main results: headline table (0.5p) → 4.3 Feature ablation: 4-way comparison (0.5p) → 4.4 Magnitude sensitivity study (0.5p) → 4.5 Analysis: per-task breakdown, failure modes (0.5p) |\n| **5. Discussion & Limitations** | 0.75 | Sim-only, K=10 overhead, feature choice insights, future directions |\n| **6. Conclusion** | 0.25 | 2-3 sentences |\n| **References** | ~1.5 (不计入) | ~30-35 refs |\n\n### 单 Claim 论文的关键策略\n\n1. **Claim 必须够强**: \"CRM correction ≥5pp over argmin-only on BOTH benchmarks\" 是最低门槛。单 claim 论文缺乏 \"至少有一个 claim 成立\" 的安全网。\n\n2. **Ablation 表做得像 multi-claim**: 4-way feature ablation + magnitude sweep + K sensitivity = 3 个独立分析维度。即使只有一个 claim，实验深度可以补偿。\n\n3. **Magnitude control 升级为独立 contribution**: norm=1.42 → 0% vs norm=0.1 → 42-57.5% 的发现是 novel empirical insight（来源: D019）。这在所有 scenario 下都成立，可作为论文的 \"second punch\"。\n\n4. **Negative result 如实呈现**: 如果 per-DOF 不优于 obs_only (Scenario B/C)，Table 中如实展示比隐藏更好——Reviewer 会欣赏 thorough ablation。\n\n5. **与 ReconVLA 的对比是必须的** (paper_framing.md Reviewer Q6)。argmin-only baseline 已经是 ReconVLA 的近似（conformal selection without correction），但需要在论文中明确声明这一对应关系。\n\n### 各 Scenario 下的标题候选\n\n| Scenario | 标题方向 |\n|----------|---------|\n| A (perdof wins) | \"ACR-VLA: Dimension-Selective Action Correction via Per-DOF Conformal Features\" |\n| B (all similar) | \"Sample-then-Refine: Uncertainty-Conditioned Learned Correction for Robust VLA Deployment\" |\n| C (obs_only wins) | \"Learned Residual Correction Improves VLA Robustness: A Conformal Selection + Observation-Conditioned Refinement Pipeline\" |\n\n---\n\n## 5. 决策依赖与时间线\n\n```\nMay 15 (NOW)\n  ├── Spatial eval running (ETA ~6-9h)\n  ├── Object eval running (ETA ~hours after spatial)\n  └── This memo prepared\n\nMay 16 (Day 2)\n  ├── Spatial 全 10 task 完成 → 初步排序\n  ├── Object 初步结果\n  └── ★ Narrative 初步选择 (A/B/C)\n\nMay 17-19 (Day 3-5)\n  ├── Object 全 10 task 完成\n  ├── Fisher exact test on both benchmarks\n  ├── Magnitude sweep (if GPU available)\n  └── ★ Narrative 最终锁定 + paper_framing.md 更新\n\nMay 20-24 (Day 6-10)\n  ├── Paper writing (8 pages)\n  ├── Figures: main results table, ablation, magnitude curve\n  └── Per-task breakdown analysis\n\nMay 25-26 (Day 11-12)\n  ├── Abstract 提交 (May 26 DDL)\n  └── Continue full paper for Jun 2 DDL\n```\n\n---\n\n## 6. Scenario-Specific 风险矩阵\n\n| 风险 | Scenario A | Scenario B | Scenario C |\n|------|-----------|-----------|-----------|\n| Novelty 挑战 | 低 (per-DOF is novel) | 中 (correction alone less novel) | 中-高 (需与 A2C2 差异化) |\n| Statistical power | 需 perdof-obs_only ≥5pp | 只需 CRM-argmin ≥5pp | 需 obs_only-argmin ≥5pp |\n| Reviewer \"so what?\" | 低 | 中 (加 magnitude control) | 中 (conformal pipeline \"wasted\"?) |\n| 论文完成复杂度 | 高 (需解释 loss-eval 反直觉) | 低 (最直白) | 中 (需优雅处理 negative result) |\n| Title/branding 一致性 | 最佳 (ACR = conformal features) | 可接受 | 差 (ACR 中 conformal 角色弱化) |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
    "content": "# Spatial Ablation Analysis & Paper Narrative Preparation\n\n> 生成时间: 2026-05-15 | 状态: 分析备忘录（等待全 10 task 完成后裁决）\n\n## 1. 当前数据快照\n\n### Spatial Benchmark（ROADMAP 2026-05-15 03:08 UTC）\n\n| 实验 | Mode | Tasks 完成 | 当前 SR | 来源 |\n|------|------|-----------|---------|------|\n| VLA baseline (K=1) | vla_only | locked | **30%** | ROADMAP baselines |\n| VLA-mean (K=10) | vla_only mean | locked | **31%** | ROADMAP baselines |\n| argmin-only | reconvla | 8/10 | **37.5%** | ROADMAP spatial eval |\n| perdof CRM | acr_vla, norm=0.1 | 5/10 | **42.0%** | ROADMAP spatial eval (v4-small) |\n| obs_only CRM | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ROADMAP spatial eval (obs-only-r2) |\n| scalar CRM | crm_scalar, norm=0.1 | 2/10 | **80%*** | ROADMAP spatial eval (*easy tasks only) |\n\n**注意**: 任务描述中的数字（perdof 42.9%, obs_only 40.0%, scalar 56.7%@3 tasks）与 ROADMAP 不一致。以 ROADMAP 为准，但两者均为中间结果，任何中间排序均可能在剩余 tasks 翻转。\n\n### 关键增量\n\n| 对比 | 增量 | 统计可信度 |\n|------|------|-----------|\n| CRM (any) vs argmin-only | +4.5pp (perdof) 至 +20pp (obs_only) | 低: 4-5/10 tasks |\n| argmin-only vs VLA baseline | +7.5pp | 中: 8/10 tasks |\n| 全 pipeline vs VLA baseline | +12pp (perdof) 至 +27.5pp (obs_only) | 低: 不同 task counts |\n\n### 数据可靠性警告\n- **obs_only** 仅 4/10 tasks，当前领先可能因 task selection bias 翻转\n- **scalar** 仅 2/10 tasks 且均为 easy tasks，80% 完全不可信\n- **perdof** 5/10 tasks，D025 已将 D019 \"52.5%\" claim 标记为失效\n- 所有 CRM variant 排序必须等全 10 tasks 完成\n\n---\n\n## 2. 三种 Narrative 分析\n\n### Scenario A: perdof > obs_only（per-DOF story）\n\n**触发条件**: 全 10 task 后 perdof SR > obs_only SR 且差 ≥5pp\n\n**可能性评估**: **低**。当前 obs_only (57.5%@4) 大幅领先 perdof (42.0%@5)。需要剩余 tasks 中 obs_only 大幅下滑且 perdof 追上。训练 loss 也支持 obs_only（val_loss 0.0165 vs perdof 0.0358，见 D020）。\n\n**Narrative**: \"Per-DOF conformal features encode dimension-specific uncertainty that observation features cannot capture. Despite worse training loss, conformal features' epistemic signal proves critical under distribution shift in closed-loop deployment.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | 开门见山：scalar UQ 丢失维度信息 → per-DOF conformal features 是解决方案。Problem 聚焦 \"information loss in scalar aggregation\" |\n| **Method** | CGS multivariate CP + per-DOF interval extraction 是核心技术贡献。CRM 架构强调 40D conformal feature vector 的设计。Magnitude control 作为工程发现 |\n| **Results** | 主表: 4-way ablation 展示 perdof > obs_only > scalar ≈ argmin。亮点故事: \"training loss 预测翻转\" (obs_only lower loss but worse eval) = compelling evidence for epistemic value |\n| **Discussion** | 强调 conformal features 在 distribution shift 下的 epistemic value 与 in-distribution training loss 的 divergence。与 ReconVLA scalar CP 对比突出信息增益 |\n\n**风险**: 如果 perdof 仅略优于 obs_only (3-5pp)，统计显著性不足，narrative 说服力弱。\n\n---\n\n### Scenario B: perdof ≈ obs_only ≈ scalar（correction-is-key story）\n\n**触发条件**: 全 10 task 后三种 CRM variant 两两差 <5pp\n\n**可能性评估**: **中**。如果 obs_only 在剩余 tasks 下滑，三者可能收敛到 40-50% 区间。\n\n**Narrative**: \"Learned uncertainty-conditioned correction (sample-then-refine) significantly outperforms pure sample selection. The correction mechanism is the contribution, not the specific feature representation.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem: 现有方法止步于 sample selection (ReconVLA) 或需 RL 训练 (SC-VLA)。Gap: 缺少 lightweight learned correction。Our angle: CRM 作为 plug-and-play correction module |\n| **Method** | CRM 架构设计 + magnitude control 是核心贡献。Per-DOF features 作为 \"one valid feature set\" 呈现，不强调其必要性。重点放在 correction mechanism 设计原则（bounded residual, norm control） |\n| **Results** | 主表: CRM (any variant) vs argmin-only 的增量。Feature ablation 作为次要表 \"CRM is robust to feature choice\"。Magnitude control study (norm sensitivity) 升级为独立 contribution |\n| **Discussion** | \"Correction > selection\" 作为主要 takeaway。与 residual policy learning 文献 (Silver 2018, PLD, TRANSIC) 建立联系。Per-DOF 保留用于 online monitoring (future work) |\n\n**优势**: 这是最稳健的 narrative——只要 CRM vs argmin-only ≥5pp 即可成立。不依赖特定 feature variant 排序。\n**风险**: Contribution novelty 降低——\"learned correction helps\" 不够新颖。需要用 magnitude control discovery 和 CoRL 实验规模补偿。\n\n---\n\n### Scenario C: obs_only > perdof（simpler-is-better / observation-conditioned story）\n\n**触发条件**: 全 10 task 后 obs_only SR > perdof SR 且差 ≥5pp\n\n**可能性评估**: **较高**。当前数据 (57.5% vs 42.0%) + 训练 loss (0.0165 vs 0.0358) 均支持此方向。D025 已预警此趋势。\n\n**Narrative**: \"Observation-conditioned learned residual correction is the key contribution. Conformal features provide no additional value as CRM input over observation features, but remain valuable for sample selection quality and coverage monitoring.\"\n\n**各章节影响**:\n\n| 章节 | 内容重点 |\n|------|---------|\n| **Intro** | Problem 保持不变（VLA robustness gap）。Gap: 缺少 inference-time learned correction。Our angle: lightweight observation-conditioned residual correction，不需要额外 UQ features |\n| **Method** | CRM 架构 + magnitude control 是核心。CGS/conformal 降为 \"sample selection module\" 的理论基础，不再是 CRM feature。需要解释 per-DOF features 的 negative result |\n| **Results** | 主表: obs_only CRM vs argmin-only vs baselines。Feature ablation 如实呈现——conformal features 不优于 observation features 作为 honest negative result。Per-DOF 在 sample selection 中的角色仍可报告 |\n| **Discussion** | 解释可能原因: (1) 观测特征已隐含编码 uncertainty 信息 (2) conformal 特征在小 K 下噪声大 (3) CRM 容量足以从观测中学到校正方向。将 per-DOF 定位为 \"future direction: larger K + better calibration\" |\n\n**Core Insight 需重写**: \"Lightweight learned residual correction on selected VLA samples significantly improves robustness. The correction module only needs observation features; structured uncertainty features are not required.\"\n\n**优势**: 实际上简化了 method 和 story——不需要解释复杂的 multivariate CP 管线作为 CRM 输入。\n**风险**: (1) 论文标题 \"ACR-VLA\" 中 \"conformal\" 角色弱化；(2) 与 A2C2 (Sendai 2025) 的差异化缩小——都变成了 \"observation-conditioned residual correction\"；(3) Reviewer 可能质疑 \"你们做了这么复杂的 CP pipeline 结果没用？\"\n\n**子情况 C1**: scalar > perdof 但 scalar < obs_only → conformal feature 形式无关紧要，进一步支持 \"correction mechanism is key\" narrative（hybrid of B+C）\n\n---\n\n## 3. 待完成实验及其对 Narrative 选择的影响\n\n| 实验 | 当前状态 | ETA | 对 narrative 的影响 |\n|------|---------|-----|-------------------|\n| **Spatial 全 10 task** (bjb1-18228) | 4-8/10 tasks | ~6-9h | **决定性**: 全部排序确认后才能选择 A/B/C |\n| **Object benchmark 全 10 task** (bjb1-32546) | 刚开始 | ~数小时 after spatial | **验证性**: cross-benchmark consistency。如果 spatial B 但 object A → narrative 困难 |\n| **Magnitude sweep** (norm ∈ {0.03, 0.05, 0.2, 0.3}) | 未开始 | 待 bjb2-28827 部署 | **补充性**: 强化 magnitude control contribution (所有 scenario 均可用) |\n| **K sensitivity sweep** (K=5,10,15,20) | 未开始 | 待 GPU 释放 | **补充性**: 回应 Reviewer Q1 (K=10 covariance reliability) |\n| **Fisher exact test** | 需全 10 task 数据 | post-eval | **统计性**: 判断增量是否 p<0.05 |\n\n**裁决所需最低数据**: Spatial 全 10 task + Object 全 10 task。两个 benchmark 均显示 CRM vs argmin ≥5pp (p<0.05) 才能安全 claim。\n\n---\n\n## 4. CoRL 8 页单 Claim 论文结构建议\n\n### 推荐结构（CoRL 2026, 8 pages + references）\n\n| 章节 | 页数 | 内容 |\n|------|------|------|\n| **Abstract** | — | 一句 problem, 一句 method (sample-then-refine + CRM), 一句 headline result |\n| **1. Introduction** | 1.0 | Problem (VLA robustness gap) → Existing approaches (selection/RL/MLLM) → Gap (no lightweight learned correction with statistical grounding) → Contribution (CRM + magnitude control + empirical findings) |\n| **2. Related Work** | 0.75 | (a) VLA robustness: training-time (RobustVLA, DiG-Flow, SRPO, ACoT) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) (b) CP in robotics (c) Residual policy learning |\n| **3. Method** | 2.0 | 3.1 Multi-sample inference + CGS (0.5p) → 3.2 Conformal sample selection (0.5p) → 3.3 CRM architecture + feature variants (0.5p) → 3.4 Magnitude control (0.5p) |\n| **4. Experiments** | 2.5 | 4.1 Setup: LIBERO-Plus spatial+object, SmolVLA backbone, baselines (0.5p) → 4.2 Main results: headline table (0.5p) → 4.3 Feature ablation: 4-way comparison (0.5p) → 4.4 Magnitude sensitivity study (0.5p) → 4.5 Analysis: per-task breakdown, failure modes (0.5p) |\n| **5. Discussion & Limitations** | 0.75 | Sim-only, K=10 overhead, feature choice insights, future directions |\n| **6. Conclusion** | 0.25 | 2-3 sentences |\n| **References** | ~1.5 (不计入) | ~30-35 refs |\n\n### 单 Claim 论文的关键策略\n\n1. **Claim 必须够强**: \"CRM correction ≥5pp over argmin-only on BOTH benchmarks\" 是最低门槛。单 claim 论文缺乏 \"至少有一个 claim 成立\" 的安全网。\n\n2. **Ablation 表做得像 multi-claim**: 4-way feature ablation + magnitude sweep + K sensitivity = 3 个独立分析维度。即使只有一个 claim，实验深度可以补偿。\n\n3. **Magnitude control 升级为独立 contribution**: norm=1.42 → 0% vs norm=0.1 → 42-57.5% 的发现是 novel empirical insight（来源: D019）。这在所有 scenario 下都成立，可作为论文的 \"second punch\"。\n\n4. **Negative result 如实呈现**: 如果 per-DOF 不优于 obs_only (Scenario B/C)，Table 中如实展示比隐藏更好——Reviewer 会欣赏 thorough ablation。\n\n5. **与 ReconVLA 的对比是必须的** (paper_framing.md Reviewer Q6)。argmin-only baseline 已经是 ReconVLA 的近似（conformal selection without correction），但需要在论文中明确声明这一对应关系。\n\n### 各 Scenario 下的标题候选\n\n| Scenario | 标题方向 |\n|----------|---------|\n| A (perdof wins) | \"ACR-VLA: Dimension-Selective Action Correction via Per-DOF Conformal Features\" |\n| B (all similar) | \"Sample-then-Refine: Uncertainty-Conditioned Learned Correction for Robust VLA Deployment\" |\n| C (obs_only wins) | \"Learned Residual Correction Improves VLA Robustness: A Conformal Selection + Observation-Conditioned Refinement Pipeline\" |\n\n---\n\n## 5. 决策依赖与时间线\n\n```\nMay 15 (NOW)\n  ├── Spatial eval running (ETA ~6-9h)\n  ├── Object eval running (ETA ~hours after spatial)\n  └── This memo prepared\n\nMay 16 (Day 2)\n  ├── Spatial 全 10 task 完成 → 初步排序\n  ├── Object 初步结果\n  └── ★ Narrative 初步选择 (A/B/C)\n\nMay 17-19 (Day 3-5)\n  ├── Object 全 10 task 完成\n  ├── Fisher exact test on both benchmarks\n  ├── Magnitude sweep (if GPU available)\n  └── ★ Narrative 最终锁定 + paper_framing.md 更新\n\nMay 20-24 (Day 6-10)\n  ├── Paper writing (8 pages)\n  ├── Figures: main results table, ablation, magnitude curve\n  └── Per-task breakdown analysis\n\nMay 25-26 (Day 11-12)\n  ├── Abstract 提交 (May 26 DDL)\n  └── Continue full paper for Jun 2 DDL\n```\n\n---\n\n## 6. Scenario-Specific 风险矩阵\n\n| 风险 | Scenario A | Scenario B | Scenario C |\n|------|-----------|-----------|-----------|\n| Novelty 挑战 | 低 (per-DOF is novel) | 中 (correction alone less novel) | 中-高 (需与 A2C2 差异化) |\n| Statistical power | 需 perdof-obs_only ≥5pp | 只需 CRM-argmin ≥5pp | 需 obs_only-argmin ≥5pp |\n| Reviewer \"so what?\" | 低 | 中 (加 magnitude control) | 中 (conformal pipeline \"wasted\"?) |\n| 论文完成复杂度 | 高 (需解释 loss-eval 反直觉) | 低 (最直白) | 中 (需优雅处理 negative result) |\n| Title/branding 一致性 | 最佳 (ACR = conformal features) | 可接受 | 差 (ACR 中 conformal 角色弱化) |\n"
  }
}
````

</details>

---

### Tool result

_source line 12 · 2026-05-15T04:48:57.399993+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T04:48:57.400127+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "spatial_analysis_prep",
  "type": "report",
  "description": "CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
  "tags": "['corl2026', 'paper-framing', 'spatial-ablation', 'narrative-analysis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "spatial_analysis_prep",
    "type": "report",
    "description": "CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议",
    "project": "acr-vla-conformal-refinement",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/spatial_analysis_prep.md",
    "tags": "['corl2026', 'paper-framing', 'spatial-ablation', 'narrative-analysis']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T04:48:57.400300+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_b9f79e\", \"name\": \"spatial_analysis_prep\", \"type\": \"report\", \"description\": \"CoRL 2026 论文 narrative 分析备忘录: 基于 spatial benchmark 中间结果的三种 Scenario (A/B/C) 分析、各章节影响、待完成实验清单、8页单claim论文结构建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/spatial_analysis_prep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T04:48:41.627375+00:00\", \"tags\": [\"corl2026\", \"paper-framing\", \"spatial-ablation\", \"narrative-analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-outline-prep_20260515T044605",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-15T04:48:57.400478+00:00_

备忘录已写入 `artifacts/spatial_analysis_prep.md` 并注册（art_20260515_b9f79e）。

核心发现：

- **当前数据倾向 Scenario C**（obs_only 57.5% > perdof 42.0%），但 obs_only 仅 4/10 tasks，排序可能翻转
- **Scenario B 是最稳健的 fallback**——只要 CRM vs argmin-only ≥5pp 即可支撑，不依赖 variant 排序
- **Magnitude control (norm=1.42→0% vs norm=0.1→42-57.5%)** 在所有 scenario 下都是独立 contribution，建议升级为论文 "second punch"
- **裁决最低数据**: spatial + object 均完成全 10 tasks + Fisher exact test p<0.05
- 预计 May 16 spatial 完成后可初步选择 narrative，May 17-19 锁定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper-outline-prep_20260515T044605"
}
```

</details>

---
