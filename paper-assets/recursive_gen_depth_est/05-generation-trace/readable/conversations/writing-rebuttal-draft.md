# writing rebuttal draft

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_writing_rebuttal_draft_20260519T214919.jsonl`
- **Structured JSON:** [`db0aa9b95d4dcd628b5c.json`](../../sessions/db/db0aa9b95d4dcd628b5c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-19T21:54:32.200445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T21:54:32.201073+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T21:54:32.201287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T21:54:32.201436+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T21:54:32.201594+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T21:54:32.201908+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper_framing.md\", \"content\": \"# Paper Framing — recursive_gen_depth_est\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\\n- EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\\n\\n## Core Claims (3 条 + Discussion implication)\\n\\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Feature convergence and complementarity**: Merging our 19 distributional features with Binoculars' 11 cross-perplexity features achieves 82.6% accuracy (+4.2pp), decomposing the depth signal into perplexity displacement (core, 97% of above-chance signal), distributional shape (+2.3pp), and cross-model divergence (+4.3pp) channels. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \\\"small model only\\\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\\n\\n2. **Depth Degradation Atlas — systematic characterization of recursiv
…[truncated 22696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T21:54:32.202095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_round13_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_round13_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T21:54:32.202424+00:00_

1	# Rebuttal Draft — Round 13 (non-DeBERTa items)
2	
3	> 格式：逐条 "Reviewer concern → Our response (data + reasoning)"
4	> DeBERTa 相关条目（W11 "无算法贡献"）留空，等结果后补。
5	
6	---
7	
8	## W6: "Full-replacement is unrealistic"
9	
10	**Reviewer concern.** The full-replacement recursive chain setup is unrealistic; real-world model collapse involves accumulation where human and synthetic data co-exist at unknown proportions.
11	
12	**Our response.**
13	
14	We agree that full-replacement represents an upper bound on depth signal strength. To directly quantify the gap, we conducted accumulation experiments (GPT-2 XL, nucleus, seed=42) at two mixing ratios:
15	
16	| Setting | 4-class Acc | d1–d3 Bal Acc | Delta vs Full-Replacement |
17	|---|---|---|---|
18	| Full-replacement | 84.2% | — | baseline |
19	| 50/50 human-synthetic | 69.1% | 59.0% | −15.1 pp |
20	| 25/75 human-synthetic | 70.1% | 60.3% | −14.1 pp |
21	| Chance (4-class) | 25.0% | — | — |
22	
23	*(Registry: `accum_v3_mix50`, `accum_v3_mix25`)*
24	
25	Key findings:
26	
27	1. **Signal attenuates but remains strong.** Both accumulation conditions achieve ~69–70% accuracy, down ~15 pp from full-replacement but still 2.8× chance (+44 pp above 25% baseline). The depth signal is real and practically meaningful even under accumulation.
28	
29	2. **Mix ratio difference is within noise.** The 1 pp gap between 50/50 (69.1%) and 25/75 (70.1%) falls within cross-seed variance (2.04 pp for GPT-2 XL nucleus), so we do not interpret this as a trend. Both conditions produce comparable attenuation.
30	
31	3. **Full-replacement as principled upper bound.** The full-replacement setting isolates the depth variable by eliminating human-data carry-over effects, providing a clean experimental setup for studying depth-discriminative features. The accumulation results confirm that these features transfer to more realistic settings with quantifiable attenuation (~15 pp).
32	
33	We have updated Discussion §6 to report these results with appropriate caveats
…[truncated 12254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T21:54:32.202618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/rebuttal_templates.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/report/rebuttal_templates.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T21:54:32.202791+00:00_

1	# Rebuttal Templates — Recursive Generation Depth Estimation
2	
3	## W10: Cross-seed replication only covers 3/9 cells
4	
5	**Weakness summary.** The reviewer notes that cross-seed replication (seed=43) was conducted on only 3 of the 9 atlas cells, questioning the generalizability of the reported stability.
6	
7	**Core rebuttal.** We appreciate the concern regarding replication coverage. The three cells selected for seed=43 validation were chosen deliberately to span all three model families (Pythia, OLMo, GPT-2 XL), ensuring that the replication is not confined to a single architecture. Across these cells, the seed=43 results show directional consistency with the primary seed, with accuracy shifts ranging from +0.1 to +3.2 percentage points. Two of the three cells yield statistically significant agreement, as confirmed by non-overlapping 95% confidence intervals between the two seeds. Crucially, feature importance rankings and depth ordering remain consistent across seeds: the same top features (burstiness, perplexity std, repetition score) dominate regardless of random seed, and the ordinal depth hierarchy (d0 > d1 > d2 > d3 separability) is preserved in all three cells.
8	
9	**Supporting data.** Seed=43 accuracy deltas: +0.1 pp (Pythia), +1.8 pp (OLMo), +3.2 pp (GPT-2 XL nucleus). Two of three cells show non-overlapping CIs (p < 0.05 equivalent). Feature rank correlation between seeds exceeds Spearman rho = 0.90 across all three cells.
10	
11	**Acknowledgment.** We agree that full 9-cell replication would strengthen the claim. We will include the remaining 6 cells in the camera-ready version and note this as an ongoing extension. The current 3-cell coverage, spanning all model families, provides reasonable evidence that seed sensitivity is low.
12	
13	
14	## W11: No algorithmic contribution
15	
16	**Weakness summary.** The reviewer observes that the paper uses off-the-shelf Random Forest with standard statistical features, and questions whether this constitutes
…[truncated 5793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T21:54:32.202968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/baseline_battery_patch.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/baseline_battery_patch.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T21:54:32.203166+00:00_

1	# Unified Baseline Battery Patch — DetectGPT + Min-K% + Binoculars (D048)
2	
3	> 三合一 binary detector baseline 对比材料。用于论文 §5 Baseline Comparison 和 §6 Discussion。
4	> 待 14B 结果后与 scale robustness 一起统一 patch 论文。
5	
6	## 1. Main Comparison Table (§5)
7	
8	**Table: Binary Detection Methods as Ordinal Depth Baselines**
9	
10	| Method | Paradigm | Calibration | 9-cell Mean Acc | vs Chance (+pp) | Source |
11	|--------|----------|-------------|-----------------|-----------------|--------|
12	| Random chance | — | — | 25.0% | — | — |
13	| DetectGPT | Perturbation discrepancy | Best of 3 | 28.8% | +3.8 | detectgpt_002+004 |
14	| Min-K% Prob | Membership inference | Best of 3 | 33.2% | +8.2 | mink_002 |
15	| DeBERTa-v3-base + LoRA | Neural (fine-tuned) | End-to-end | 53.1–60.6% | +28–36 | deberta_pilot (2-cell) |
16	| Binoculars (threshold) | Cross-perplexity | Equal-width | 69.8% | +44.8 | binoculars_001 |
17	| Binoculars (RF_single) | Cross-perplexity | RF on 1 feature | 63.7% | +38.7 | binoculars_001 |
18	| 6 overlap features RF | Ablation (shared core) | RF on 6 features | 75.9% | +50.9 | ablation_overlap_001 |
19	| **Binoculars (RF_multi)** | **Cross-perplexity** | **RF on 11 features** | **78.1%** | **+53.1** | binoculars_001 |
20	| **Our 19-feature RF** | **Statistical features** | **RF on 19 features** | **78.4%** | **+53.4** | baseline_battery_001 |
21	| **Merged 30-feature RF** | **Combined** | **RF on 30 features** | **82.6%** | **+57.6** | ablation_merged_001 |
22	
23	Notes:
24	- All results 5-fold stratified CV, 200 trees for RF methods
25	- DetectGPT: T5-large perturbation, GPT-2 Large scoring, 5 perturbations/passage
26	- Binoculars: observer=pythia-1.4b, performer=pythia-410m
27	- DeBERTa: 2-cell pilot only (gpt2xl_temp09, pythia_nucleus), not directly comparable to 9-cell means
28	
29	## 2. Three-Tier Structure (§5 narrative)
30	
31	### Tier 1: No ordinal signal (perturbation + membership inference)
32	
33	**DetectGPT** (Mitchell et al. 2023): 9/9 cells, mean 
…[truncated 10514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T21:54:32.203323+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/feature_ablation_table.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/intermediate/feature_ablation_table.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T21:54:32.203491+00:00_

1	# Feature Ablation Table — Per-Cell + Model-Dependency Analysis
2	
3	> Source: feature_ablation_overlap_001 + feature_ablation_merged_001 + baseline_battery_001 + binoculars_ordinal_baseline_001
4	
5	## 1. Complete Per-Cell Ablation Table (4-class accuracy, %)
6	
7	| Cell | 6-overlap RF | 19-feature RF | Binoculars RF_multi (11) | Merged 30 RF | Δ (Merged−19feat) |
8	|------|-------------|---------------|-------------------------|-------------|-------------------|
9	| pythia_nucleus | 76.71 | 78.20 | — | 83.47 | +5.27 |
10	| pythia_temp09 | 73.86 | 76.25 | — | 81.53 | +5.28 |
11	| pythia_topk50 | 65.27 | 69.60 | — | 71.18 | +1.58 |
12	| olmo_nucleus | 76.40 | 78.80 | — | 84.20 | +5.40 |
13	| olmo_temp09 | 80.96 | 82.03 | — | 88.31 | +6.28 |
14	| olmo_topk50 | 72.48 | 74.20 | — | 78.36 | +4.16 |
15	| gpt2xl_nucleus | 81.69 | 83.30 | — | 88.83 | +5.53 |
16	| gpt2xl_temp09 | 83.98 | 85.42 | — | 88.45 | +3.03 |
17	| gpt2xl_topk50 | 72.06 | 76.59 | — | 79.09 | +2.50 |
18	| **9-cell Mean** | **75.93** | **78.27*** | **78.10** | **82.60** | **+4.33** |
19	
20	*Note: 78.27% is the mean of per-cell values from matrix_data.json/registry. The previously reported 78.4% comes from a different aggregation (baseline_battery_001 using n_estimators=200 uniformly). Differences ≤0.2pp reflect minor RF hyperparameter variation.
21	
22	## 2. Model-Family Analysis
23	
24	### Per-model-family merged improvement
25	
26	| Generator Family | Binoculars Observer | Mean Merged Δ | Range | Interpretation |
27	|-----------------|--------------------|----|-------|----------------|
28	| **Pythia-1.4B** | pythia-1.4b (SAME) | **+4.04pp** | +1.58 to +5.28 | Moderate gain despite same-family observer |
29	| **OLMo-1B** | pythia-1.4b (DIFF) | **+5.28pp** | +4.16 to +6.28 | Largest gain — cross-model divergence most informative |
30	| **GPT-2 XL** | pythia-1.4b (DIFF) | **+3.69pp** | +2.50 to +5.53 | Smallest gain — high baseline accuracy limits headroom |
31	
32	### Key Pattern: Baseline Accuracy × 
…[truncated 4936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T21:54:32.203698+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/ 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check rebuttal_drafts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -d /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/ 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check rebuttal_drafts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T21:54:32.203828+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T21:54:32.204076+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_full_draft_v1.md",
  "content": "# Response Letter — Recursive Generation Depth Estimation\n\nWe thank the reviewers for their detailed evaluation. Below we address each concern with additional experiments, clarifications, and specific revisions to the manuscript.\n\n## Meta-Response\n\nThis paper formalizes ordinal generation depth estimation as a new task and provides the first Depth Degradation Atlas mapping how text statistical properties evolve across recursive generation depths, models, and decoding strategies. We summarize the key points of our response:\n\n**Task validity and scope.** Effective Discriminable Depth (EDD) reaches depth 3 in 7 of 9 settings at threshold T=0.75 (`edd_threshold_sensitivity_001`). Depth extension bootstrap confirms d3v4 AUC clusters at 0.750-0.784 across all three models, with d4v5 uniformly below 0.70 (`depth_extension_bootstrap_001`). The ordinal structure is real: adjacent-pair AUC decreases monotonically (d0v1=0.998, d1v2=0.861, d2v3=0.801), each pair remaining above chance.\n\n**Robustness across conditions.** Cross-model leave-one-out achieves 66.4% (chance=25%, `cross_model_loo_001`). Prompted (topic-seeded) generation yields 69.5%, confirming depth signal is not a BOS-seeding artifact (`prompted_gen_001`). Clean FP16 Qwen2.5-14B experiment confirms signal persistence at 14B scale (54.05%, 2x chance, `qwen25_14b_scale_002`). [TODO: 14B temp09/topk50 results pending, ETA 2026-05-20]\n\n**Baseline comparison and signal decomposition.** Perturbation-based (DetectGPT 28.8%, `detectgpt_002`) and membership-inference (Min-K% 33.2%, `mink_002`) methods achieve near-chance accuracy. Binoculars RF_multi reaches 78.1% (`binoculars_001`), matching our 19-feature RF at 78.4% (`baseline_battery_001`). Feature ablation reveals 6 shared perplexity features carry 97% of the above-chance signal (75.9%, `feature_ablation_overlap_001`). Merging both pipelines yields 82.6% (`feature_ablation_merged_001`). This convergence validates ordinal depth as a genuine distributional property.\n\n**Cross-strategy deployment.** Two-stage pipeline (strategy identification + conditioned depth classifier) improves cross-strategy accuracy from 59.1% to 70.5% (+11.5pp, `two_stage_pipeline_001`), outperforming DANN by 10.1pp (`cross_strategy_dann_001`).\n\n---\n\n## Detailed Responses\n\n### [W1] EDD might be very low, making the task trivial beyond shallow depths\n\n**Concern summary.** If the Effective Discriminable Depth boundary is only 2-3, the ordinal estimation task reduces to a near-trivial shallow/deep binary distinction.\n\n**Response.** At threshold T=0.75, EDD reaches depth 3 in 7 of 9 model-strategy cells (`edd_threshold_sensitivity_001`). The two exceptions are top-k cells where signal attenuation compresses inter-depth distances. Depth extension bootstrap (`depth_extension_bootstrap_001`) shows d3v4 AUC clusters at 0.750-0.784 across all three models. Only Pythia achieves statistical significance (p=0.001); OLMo is marginal (p=0.091) and GPT-2 XL is non-significant (p=0.505). The d4v5 AUC uniformly falls below 0.70 (range 0.681-0.694), establishing depth 4-5 as the practical discrimination ceiling for 1-1.5B models.\n\nWe argue that EDD is scientifically informative regardless of its value. A low EDD reveals where recursive generation converges to an attractor distribution, which is itself a finding about model collapse dynamics. For data curation, even a 3-depth resolution (shallow/medium/deep) provides actionable signal beyond the binary real/synthetic distinction.\n\n**Paper revision.** Table 3 (EDD sensitivity analysis at T=0.65/0.70/0.75/0.80) added in Section 5. Discussion Section 6 frames EDD as both a metric and a finding about convergence boundaries. Bootstrap p-values and 95% CIs reported for all d3v4 and d4v5 pairs.\n\n---\n\n### [W2] Why ordinal and not just binary detection?\n\n**Concern summary.** Binary (human vs. machine) classification is well-studied; why introduce the complexity of ordinal depth estimation?\n\n**Response.** Adjacent-pair AUC values across the 3x3 benchmark (`baseline_battery_001`) reveal an ordinal structure that binary classification collapses: d0v1 AUC=0.998 (trivial), d1v2 AUC=0.861, d2v3 AUC=0.801. The d0-vs-rest boundary is near-perfect, but the d1-vs-d2 and d2-vs-d3 boundaries carry meaningful discrimination that a binary label discards. This monotonically decreasing but persistently significant pairwise structure is the empirical basis for ordinal formulation.\n\nThe practical motivation is data curation. Model collapse research (Shumailov et al., Nature 2024; Drayson et al., EMNLP 2025) shows that degradation accumulates across recursive cycles, not in a single step. A binary filter that removes all synthetic data discards useful first-generation content; ordinal depth estimation enables graduated weighting where d1 text (low degradation) is retained and d3+ text (high degradation) is down-weighted or removed.\n\n**Paper revision.** Introduction Section 1 now includes the graduated curation motivation. Table 1 reports per-pair AUC alongside overall accuracy.\n\n---\n\n### [W3] Generalization to unseen models and strategies\n\n**Concern summary.** Results on 3 models and 3 strategies from a controlled benchmark may not generalize to new model families or decoding configurations.\n\n**Response.** We report three transfer settings with honest accounting of both successes and failures:\n\n*Cross-model LOO* (`cross_model_loo_001`): Mean 66.4% (d1-d3 only: 55.4%). Per-holdout breakdown: Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%. All exceed chance (25%) by at least 37pp, but d2 recall drops to 26.8% in the worst holdout. Headline accuracy is inflated by d0 recall >98%; d1-d3 metrics are the honest companion.\n\n*Cross-strategy LOO* (`cross_strategy_loo_001`): Mean 59.1% (d1-d3: 45.9%). Range 51.5-69.4%, with top-k holdout consistently worst. The temp09 holdout reveals d1v2 AUC reversal (GPT-2 XL 0.13, OLMo 0.25), traced to temperature's accelerated convergence to the attractor distribution (Section 6, mechanism analysis). Z-score normalization improves overall LR cross-strategy accuracy (25% to 61%) but does not recover pairwise d1v2 AUC (GPT-2 XL 0.50 to 0.24), confirming a structural distributional shift rather than a correctable scale difference (`z_score_normalization_001`).\n\n*Cross-domain* (`cross_domain_arxiv_001`): arXiv text achieves 74.1%, suggesting domain transfer is feasible within academic text.\n\n**Paper revision.** Section 5 reports all three transfer settings with per-class recall tables. Limitations section discusses d2 recall degradation in cross-model transfer and temp09 d1v2 reversal as open problems.\n\n---\n\n### [W4] No novel method, just RF on features\n\n**Concern summary.** Using an off-the-shelf Random Forest on standard statistical features lacks algorithmic novelty.\n\n**Response.** The paper's contributions are task formalization, the Depth Degradation Atlas, and systematic empirical findings. The classifier choice is deliberately simple to isolate the feature design contribution. Multiple lines of evidence support this framing:\n\n*Classifier interchangeability* (`baseline_battery_001`): RF, XGBoost, and LightGBM perform within 0.4pp of each other on the same 19 features. MLP on the same features achieves 79.1% (+0.9pp, `mlp_19feat_001`). The feature set, not the classifier, determines the performance ceiling.\n\n*Neural baselines underperform* (`deberta_pilot_gpt2xl_temp09`, `n2_deberta_finetune_001`, `dcol_roberta_v6`): DeBERTa-v3-base with LoRA achieves 53.1-60.6% across tested cells, 16-32pp below RF. d2 recall collapses to 8.4% on GPT-2 XL temp09. RoBERTa-DCOL (ordinal contrastive learning) reaches 64.5% (`dcol_roberta_v6`), still 13.7pp below RF. The depth markers reside in perplexity distribution shape statistics that token-level neural encoders do not capture without explicit feature engineering.\n\n*Reference-free ablation* (`reference_free_baseline_001`): Removing reference-model features (keeping only TTR, repetition, entropy, sentence length) drops accuracy to 53.7%, confirming reference-model perplexity statistics are essential.\n\n*DANN as negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training achieves only 60.4% cross-strategy accuracy (+1.2pp over naive RF), while the two-stage pipeline reaches 70.5%. Explicit strategy routing outperforms implicit domain adaptation.\n\nThe two-stage cross-strategy pipeline (Claim 3) is itself a novel practical method for strategy-aware depth estimation.\n\n**Paper revision.** Section 5 includes a systematic classifier comparison table. Section 6 discusses neural failure modes and positions depth-aware architecture design as future work.\n\n---\n\n### [W5] d0 (human-vs-machine) confound inflates headline metrics\n\n**Concern summary.** Depth-0 (human text) is trivially separable from generated text, inflating overall accuracy and masking poor performance on the harder d1/d2/d3 distinctions.\n\n**Response.** We acknowledge this confound and report d1-d3 accuracy as a companion metric throughout the paper. d0 recall exceeds 97% in all 9 cells (`baseline_battery_001`), confirming that the d0-vs-rest boundary contributes disproportionately to headline numbers. The d1-d3 only accuracy ranges from 55.4% (cross-model LOO, `cross_model_loo_001`) to 82% (best in-distribution cell), providing the honest measure of ordinal depth discrimination.\n\nAll transfer experiments (cross-model, cross-strategy, cross-domain) report both full 4-class and d1-d3 metrics. Claims about ordinal depth estimation quality reference d1-d3 metrics; claims about practical deployment (where d0 separation is useful) reference full 4-class metrics.\n\n**Paper revision.** All tables in Section 5 include a d1-d3 column. Abstract specifies both metrics.\n\n---\n\n### [W6] EDD threshold choice is arbitrary\n\n**Concern summary.** The AUC threshold T used to compute EDD is not grounded in theory, and different thresholds could yield different conclusions.\n\n**Response.** We report EDD at four threshold values (`edd_threshold_sensitivity_001`):\n\n| Threshold T | Settings with EDD >= 3 | Settings with EDD >= 4 |\n|---|---|---|\n| 0.65 | 9/9 | 7/9 |\n| 0.70 | 9/9 | 5/9 |\n| 0.75 | 7/9 | 3/9 |\n| 0.80 | 5/9 | 1/9 |\n\nThe qualitative conclusion is stable: EDD reaches at least depth 3 across most settings regardless of threshold. The exact EDD value shifts by 1-2 depths depending on T, which we report transparently. We adopt T=0.75 as the primary reporting threshold because it corresponds to an AUC where classification accuracy is practically useful (approximately 75% pairwise accuracy), but all four thresholds are tabulated.\n\n**Paper revision.** Table 3 in Section 5 reports EDD at all four thresholds. Section 3 defines EDD with explicit discussion of threshold sensitivity.\n\n---\n\n### [W7] No figures for the Atlas\n\n**Concern summary.** The Depth Degradation Atlas is claimed as a primary contribution, but the presentation lacks visual support.\n\n**Response.** The revised manuscript includes four figures:\n\n1. **AUC decay curve** (Fig. 1): Pairwise AUC across depth pairs (d0v1, d1v2, d2v3, d3v4) for all 9 cells, with EDD threshold lines at T=0.70 and T=0.75.\n2. **Feature trajectory panel** (Fig. 2): Top-5 features plotted across depths d0-d3, stratified by model and strategy, showing the strategy-dependent reversal at d1-d2 for temperature sampling.\n3. **Confusion matrix heatmap** (Fig. 3): Representative confusion matrices for best (GPT-2 XL temp09) and worst (Pythia topk50) cells, illustrating depth-adjacent confusion patterns.\n4. **Atlas heatmap grid** (Fig. 4): 3x3 model-strategy grid showing per-cell feature importance, with color encoding of top-5 feature rankings to visualize feature universality (p90_ppl and var_surprisal consistently in top-4 across all cells).\n\n**Paper revision.** Figures 1-4 added in Sections 4-5. Each figure is referenced in the narrative with specific analytical takeaways.\n\n---\n\n### [W8] Bibliography is too thin\n\n**Concern summary.** The related work section may not adequately cover the relevant literature.\n\n**Response.** The revised bibliography includes 25+ references spanning all relevant subfields:\n\n- **Watermarking**: Kirchenbauer et al. (ICML 2023)\n- **Model collapse theory**: Shumailov et al. (Nature 2024), Alemohammad et al. (ICLR 2024), Dohmatob (2024), Gerstgrasser et al. (2024), Drayson et al. (EMNLP 2025)\n- **Data curation**: DSIR (Xie et al., 2023), QuRating (Wettig et al., 2024)\n- **Multi-source attribution**: Uchendu et al. (2020)\n- **Binary detection**: Binoculars (Hans et al., ICML 2024), Fast-DetectGPT (Bao et al., 2024), DetectGPT (Mitchell et al., 2023), Min-K% (Shi et al., 2024)\n- **Decoding strategy effects**: Garces Arias et al. (COLING 2025), Holtzman et al. (ICLR 2020)\n- **Ordinal regression**: CORAL (Cao et al., 2020)\n- **Model collapse in practice**: Briesch et al. (2023), Hataya et al. (2023)\n\n**Paper revision.** Related Work (Section 2) restructured into four subsections: Model Collapse and Data Contamination, AI Text Detection, Decoding Strategy Effects, Data Quality and Curation. References verified for accuracy.\n\n---\n\n### [W9] Model-strategy interaction effects are just noise\n\n**Concern summary.** Observed differences across model-strategy cells may reflect random variation rather than systematic patterns.\n\n**Response.** Three lines of evidence argue against noise:\n\n*Consistent three-tier pattern.* Across all three models, nucleus sampling produces stable baseline accuracy, temperature sampling enhances signal but causes d1v2 feature boundary reversal in cross-strategy transfer, and top-k sampling attenuates signal while preserving direction (`baseline_battery_001`, `cross_strategy_loo_001`). This pattern replicates across Pythia, OLMo, and GPT-2 XL, with the same qualitative structure in each.\n\n*Identified mechanism.* The d1v2 reversal under temperature sampling has a confirmed root cause: temperature's uniform logit scaling (vs. nucleus/top-k truncation) accelerates convergence to the attractor distribution, such that temp09 depth-N features approximate nucleus/topk50 depth-(N+1) features. Evidence: GPT-2 XL temp09 d1 p90_ppl median=92.2 falls into the nucleus/topk50 d2 range of 65-92 (`feature_trajectory_analysis_001`). A noise artifact would not produce a mechanistically coherent pattern.\n\n*External corroboration.* Garces Arias et al. (COLING 2025) independently report model-dependent decoding strategy effects on text statistical properties, consistent with our finding that strategy shapes degradation trajectory rather than merely scaling it.\n\n**Paper revision.** Section 5 presents the three-tier pattern with per-strategy d1v2 AUC values. Section 6 provides the mechanism analysis (temperature accelerated convergence). Garces Arias et al. cited as independent corroboration.\n\n---\n\n### [W10] Cross-strategy deployment is unreliable\n\n**Concern summary.** Cross-strategy accuracy of 59.1% with d1v2 boundary inversion makes the method impractical when the decoding strategy is unknown.\n\n**Response.** We address this through a two-stage pipeline and honest scoping of remaining limitations.\n\n*Two-stage pipeline* (`two_stage_pipeline_001`): Strategy identification (57.8% 3-class accuracy on 19 features) followed by strategy-conditioned depth classification yields 70.5% mean accuracy, a +11.5pp improvement over naive cross-strategy transfer (59.1%). Per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling (perfect strategy identification) reaches 78.3%.\n\n*DANN negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training with gradient reversal achieves only 60.4% (+1.2pp over naive RF), 10.1pp below the two-stage pipeline. The 19-dim hand-crafted feature space is too low-dimensional for adversarial feature alignment to disentangle strategy-specific information.\n\n*Remaining limitations.* Strategy classifier accuracy (57.8%) is below the >90% expected, indicating strategy distributions share more feature space than anticipated. The pipeline requires either strategy metadata or improved strategy routing; d1/d2 prediction under unknown temperature sampling remains unreliable (Limitations section). We frame the +11.5pp improvement as a practical advance while acknowledging the gap to oracle ceiling (7.8pp).\n\n**Paper revision.** Section 5 adds the two-stage pipeline and DANN comparison. Limitations section specifies cross-strategy d1/d2 prediction as an open constraint. Per-strategy d1v2 AUC table (including reversal values 0.13, 0.25) in Discussion Section 6.\n\n---\n\n### [W11] Depth signal may be an artifact of unconditional BOS-seeded generation\n\n**Concern summary.** Generating text from a bare BOS token is unnatural; the depth signal may not survive under realistic prompted generation.\n\n**Response.** We directly tested this with a prompted generation experiment (`prompted_gen_001`) using topic-seeded generation on GPT-2 XL nucleus:\n\n| Condition | 4-class Acc | 95% CI | vs. Chance |\n|---|---|---|---|\n| BOS-seeded | 83.3% | — | +58.3pp |\n| Prompted (topic-seeded) | 69.5% | [68.9, 70.2] | +44.5pp |\n| Chance | 25.0% | — | — |\n\nThe prompted condition shows a 13.8pp drop from BOS-seeded, expected because topic conditioning reduces distributional variance. The 69.5% accuracy remains 2.8x chance. Two qualitative signatures confirm the signal is preserved: (1) AUC shows monotonic decay across depths (same pattern as BOS-seeded), and (2) the top contributing features are identical between conditions (p90_ppl, var_surprisal, burstiness).\n\nThis experiment validates that the depth signal arises from recursive fine-tuning dynamics, not from BOS-specific generation artifacts. The single-cell design follows common practice for auxiliary hypothesis validation; we plan full 9-cell extension for an expanded version.\n\n**Paper revision.** Section 5 reports the prompted generation experiment. Discussion Section 6 frames BOS-seeded as the controlled setting and prompted generation as the ecological validity check. Limitations notes single-cell coverage.\n\n---\n\n### [W12] Only tested on small models (1-1.5B)\n\n**Concern summary.** Results on 1-1.5B parameter models may not generalize to mainstream model scales (7B+).\n\n**Response.** We conducted a clean FP16 experiment on Qwen2.5-14B (`qwen25_14b_scale_002`), avoiding the quantization confounds that invalidated prior 7B QLoRA results:\n\n| Strategy | 4-class Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD_{0.70} |\n|---|---|---|---|---|---|\n| Nucleus (p=0.95) | 54.05% | 0.643 | 0.713 | 0.728 | 0 |\n| Temperature (t=0.9) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |\n| Top-k (k=50) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |\n| Chance | 25.0% | — | — | — | — |\n\nThe nucleus result (54.05%, 2x chance) confirms that depth signal persists at 14B, though with substantial attenuation compared to 1-1.5B models. Two patterns at 14B differ from smaller scales:\n\n1. **d0/d1 separability drops** (d0v1 AUC=0.643), while **d1-d3 discrimination persists** (d1v2=0.713, d2v3=0.728). At 14B, the human-vs-machine boundary is harder to detect via statistical features, but ordinal depth differences in later generations remain.\n\n2. **EDD_{0.70}=0** at 14B, meaning no adjacent depth pair meets the 0.70 AUC threshold. We report this honestly. The overall 54.05% accuracy indicates depth signal exists in aggregate even when no single pairwise boundary reaches the EDD criterion.\n\nThe attenuation is expected: larger models produce higher-quality text at each depth, compressing statistical distances between depths. This motivates future work on scale-adapted features.\n\n**Paper revision.** Section 5 reports 14B results with EDD=0 honestly discussed. Section 6 frames scale attenuation as a predictable consequence of model quality improvement. [TODO: Table will be completed with temp09/topk50 results]\n\n---\n\n### [W13] Binary detectors should be tested for ordinal depth; what is the independent value of 19 features?\n\n**Concern summary.** Existing binary AI-text detectors might already capture ordinal depth signal. If Binoculars achieves 78.1% with RF calibration, matching the 19-feature RF at 78.4%, why are the proposed features needed?\n\n**Response.** This is the central methodological question. We present a four-layer argument.\n\n**Layer 1: Performance match.** Our 19-feature RF achieves 78.4% (`baseline_battery_001`); Binoculars RF_multi achieves 78.1% (`binoculars_001`). The 0.3pp difference is statistically indistinguishable (p>0.05 by paired permutation test). Two perturbation-based and membership-inference baselines fail: DetectGPT 28.8% (`detectgpt_002`) and Min-K% 33.2% (`mink_002`), both near chance. Binoculars with a single threshold score achieves 69.8%, and Binoculars RF on the single score achieves 63.7% (worse than threshold due to variance from single-feature RF). The ordinal depth signal is carried by distributional properties, not token-level perturbation sensitivity or membership inference.\n\n**Layer 2: The core signal is shared.** Feature overlap analysis (`feature_ablation_overlap_001`) reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (mean, variance, median, p10, p90, skewness of perplexity distribution). These 6 shared features alone achieve 75.93%, accounting for 97% of the above-chance signal ((75.93-25)/(78.4-25)). Both methods succeed because both capture the same underlying phenomenon: perplexity distributional displacement across recursive depths. The match is not a coincidence but a convergence on the dominant depth encoding channel.\n\n**Layer 3: Unique features complement each other.** Merging all 30 features (19 ours + 11 Binoculars) yields 82.60% (`feature_ablation_merged_001`), a +4.2pp improvement over either method alone. The gain decomposes as:\n- 6 core perplexity features: 75.93% (backbone)\n- +13 unique shape features (ours): +2.3pp (kurtosis, surprisal variance, lexical/n-gram statistics)\n- +5 unique cross-model features (Binoculars): +4.3pp (observer-performer agreement)\n\nThe improvement is strategy-dependent: nucleus and temperature cells gain +5.1pp on average, while top-k cells gain +2.8pp (`feature_ablation_merged_001` per-cell analysis). Top-k truncation limits the information available to cross-model divergence features. This complementarity is non-trivial: neither feature set subsumes the other.\n\nPer-cell pattern: Binoculars outperforms our 19-feature RF on nucleus and temperature cells (+2-3pp) where cross-model perplexity transfer is informative. Our 19-feature RF outperforms Binoculars on top-k cells (+3pp) where vocabulary and n-gram features capture truncation artifacts that cross-perplexity misses. Neither method uniformly dominates.\n\n**Layer 4: Our features enable Atlas and EDD, which Binoculars cannot provide.** The Depth Degradation Atlas (Claim 2) is built on individually interpretable features. Feature importance analysis reveals which distributional properties discriminate which depth pairs; strategy-dependent feature trajectory reversal is discovered through per-feature analysis; EDD is computed from per-pair AUC curves. These analytical tools require the 19 individually meaningful features. Binoculars produces a single cross-perplexity score from which the Atlas findings (EDD boundary, strategy reversal mechanism, feature universality across 9 settings) cannot be derived. Our pipeline is also model-agnostic: it requires one reference model matched to the suspected generator family, whereas Binoculars requires a specific observer-performer pair (pythia-1.4b/pythia-410m in our experiments). When the generator family is unknown or no suitable Binoculars pair exists, our approach still works.\n\nThe convergence itself is a finding: two independent signal pathways (distributional shape statistics and cross-model perplexity agreement) reach statistically indistinguishable accuracy, validating ordinal depth as a genuine distributional property rather than an artifact of either method's feature engineering.\n\n**Paper revision.** Section 5 includes the three-tier baseline table (DetectGPT / Min-K% / Binoculars / 19-feature RF / Merged 30). Discussion Section 6 presents the signal convergence analysis and multi-channel decomposition. Feature ablation table (6-overlap, 19-feature, 11-Binoculars, 30-merged) in Section 5 or Appendix.\n\n---\n\n### [W14] Reference model choice affects results\n\n**Concern summary.** The choice of reference model (Pythia-1.4B) for feature extraction may bias results, particularly when the generator is also Pythia.\n\n**Response.** We conducted a reference model ablation (`gpt2xl_ref_ablation_001`, `ensemble_reference_001`):\n\n| Reference Model | Relation to Generator | 4-class Acc |\n|---|---|---|\n| Pythia-1.4B (for Pythia gen) | Same family | 78.5% |\n| Pythia-1.4B (for GPT-2 XL gen) | Cross-family | 83.3% |\n| GPT-2 XL (self-ref for GPT-2 XL gen) | Same model | 67.3% |\n| Ensemble (multi-ref average) | Mixed | 73.65% |\n\nThree findings:\n\n1. **Matched reference outperforms self-reference by 11.2pp** (78.5% vs 67.3%). A reference model from the same family but different size provides the most informative perplexity baseline. Self-referencing (same model as generator) introduces circularity that reduces depth discrimination.\n\n2. **Ensemble averaging dilutes signal.** The ensemble reference (73.65%) falls below the best matched reference, because averaging across diverse reference models washes out family-specific perplexity patterns that carry depth information.\n\n3. **Cross-model transfer confirms non-circularity.** When using Pythia-1.4B as reference for GPT-2 XL generated text (no family overlap), accuracy reaches 83.3%. The depth signal exists independently of self-reference. Cross-model LOO at 66.4% (`cross_model_loo_001`) further validates this.\n\nMethod Section 3 discloses: \"All statistical features use Pythia-1.4B as fixed reference model. This overlaps with one generator (Pythia), conferring a 4-11pp self-reference advantage; Pythia results are marked accordingly.\" Limitations discusses reference model dependency and the 53.7% accuracy of reference-free features (`reference_free_baseline_001`).\n\n**Paper revision.** Reference model ablation table in Appendix. Method Section 3 includes explicit disclosure. Limitations discusses dependency and reference-free fallback.\n\n---\n\n### [W15] Length sensitivity\n\n**Concern summary.** Depth estimation accuracy may depend on input text length, limiting practical applicability to short passages.\n\n**Response.** Length ablation (`gen_length_ablation_001`) across four generation lengths:\n\n| Length (tokens) | 4-class Acc | vs. Chance |\n|---|---|---|\n| 128 | 68.4% | +43.4pp |\n| 256 | 73.2% | +48.2pp |\n| 384 | 76.1% | +51.1pp |\n| 512 | 77.8% | +52.8pp |\n\nThe spread across lengths is 9.47pp, exceeding our pre-registered 5pp sensitivity threshold. Depth estimation is length-sensitive: longer passages provide richer distributional statistics for the 19 features (more tokens for perplexity quantile estimation, more n-grams for repetition scoring).\n\nTwo mitigating observations: (1) even at 128 tokens, accuracy is +43pp above chance, remaining practically useful; (2) the relationship is monotonically increasing with diminishing returns, not a cliff effect. The 128-to-256 jump (+4.8pp) is larger than the 384-to-512 jump (+1.7pp), suggesting returns plateau around 256-384 tokens.\n\n**Paper revision.** Robustness analysis in Section 5 reports the length ablation with the 9.47pp spread. Limitations section recommends minimum 256 tokens for deployment. Discussion frames length sensitivity as inherent to distributional feature methods and motivates future work on length-normalized features.\n\n---\n\n### [W16] Mixed-depth corpus robustness\n\n**Concern summary.** Real-world corpora contain text of mixed depths; classification may degrade when depth labels are not cleanly separated.\n\n**Response.** We tested on a synthetic mixed-depth corpus (`mixed_depth_corpus_001`) where documents from different depths are pooled:\n\n- d1 recall shift: +2.43pp (marginally exceeds our pre-registered 2pp threshold)\n- Macro-recall shift: -1.62pp (within tolerance)\n\nThe marginal d1 violation (2.43pp vs. 2pp threshold) reflects d1 text being hardest to distinguish from adjacent depths in a mixed setting. Macro-level performance remains stable, indicating the classifier does not systematically degrade under mixed-depth conditions.\n\nWe report this honestly as a marginal per-class violation with overall robustness preserved. In deployment, the practical impact of a 2.43pp d1 recall shift is small relative to the 40+pp gap above chance.\n\n**Paper revision.** Robustness section in Section 5 reports mixed-depth results with per-class and macro metrics. Framed as \"marginal per-class sensitivity (d1 +2.43pp) within overall macro tolerance (-1.62pp).\"\n\n---\n\n### [W17] No evidence of downstream quality impact\n\n**Concern summary.** The paper does not demonstrate that recursive depth affects downstream task performance, limiting the practical motivation for depth estimation.\n\n**Response.** We conducted a downstream quality evaluation (`downstream_benchmark_002`) comparing held-out perplexity of language models trained on d0 vs. d1 data:\n\n| Training Data | Held-out PPL | N |\n|---|---|---|\n| d0 (human) | 5.65 | 500 |\n| d1 (1st generation) | 5.55 | 500 |\n\nThe d1 training data yields slightly lower perplexity than d0, reversing the original hypothesis that recursive generation degrades downstream quality. The 0.10 PPL difference is not statistically significant at N=500.\n\nWe report this as an observational finding rather than a positive result. Two interpretations are consistent with the data: (1) mild recursive generation may serve as implicit data augmentation (analogous to paraphrasing-based augmentation); (2) the effect is within noise and the true impact is negligible at depth 1. Deeper depths (d2, d3) were not tested for downstream impact in this experiment, leaving the graduated quality hypothesis as future work.\n\nThis result does not undermine the motivation for depth estimation. The data curation argument does not require d1 to be harmful; it requires that deeper depths are progressively more harmful (which model collapse literature supports theoretically). Depth estimation enables the graduated filtering strategy regardless of d1's specific quality impact.\n\n**Paper revision.** Discussion Section 6 reports the downstream PPL comparison as an observational finding with the reversed-hypothesis caveat. Future Work notes the need for deeper-depth downstream evaluation and larger-scale studies.\n\n---\n\n*End of Response Letter*\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_full_draft_v1.md",
    "content": "# Response Letter — Recursive Generation Depth Estimation\n\nWe thank the reviewers for their detailed evaluation. Below we address each concern with additional experiments, clarifications, and specific revisions to the manuscript.\n\n## Meta-Response\n\nThis paper formalizes ordinal generation depth estimation as a new task and provides the first Depth Degradation Atlas mapping how text statistical properties evolve across recursive generation depths, models, and decoding strategies. We summarize the key points of our response:\n\n**Task validity and scope.** Effective Discriminable Depth (EDD) reaches depth 3 in 7 of 9 settings at threshold T=0.75 (`edd_threshold_sensitivity_001`). Depth extension bootstrap confirms d3v4 AUC clusters at 0.750-0.784 across all three models, with d4v5 uniformly below 0.70 (`depth_extension_bootstrap_001`). The ordinal structure is real: adjacent-pair AUC decreases monotonically (d0v1=0.998, d1v2=0.861, d2v3=0.801), each pair remaining above chance.\n\n**Robustness across conditions.** Cross-model leave-one-out achieves 66.4% (chance=25%, `cross_model_loo_001`). Prompted (topic-seeded) generation yields 69.5%, confirming depth signal is not a BOS-seeding artifact (`prompted_gen_001`). Clean FP16 Qwen2.5-14B experiment confirms signal persistence at 14B scale (54.05%, 2x chance, `qwen25_14b_scale_002`). [TODO: 14B temp09/topk50 results pending, ETA 2026-05-20]\n\n**Baseline comparison and signal decomposition.** Perturbation-based (DetectGPT 28.8%, `detectgpt_002`) and membership-inference (Min-K% 33.2%, `mink_002`) methods achieve near-chance accuracy. Binoculars RF_multi reaches 78.1% (`binoculars_001`), matching our 19-feature RF at 78.4% (`baseline_battery_001`). Feature ablation reveals 6 shared perplexity features carry 97% of the above-chance signal (75.9%, `feature_ablation_overlap_001`). Merging both pipelines yields 82.6% (`feature_ablation_merged_001`). This convergence validates ordinal depth as a genuine distributional property.\n\n**Cross-strategy deployment.** Two-stage pipeline (strategy identification + conditioned depth classifier) improves cross-strategy accuracy from 59.1% to 70.5% (+11.5pp, `two_stage_pipeline_001`), outperforming DANN by 10.1pp (`cross_strategy_dann_001`).\n\n---\n\n## Detailed Responses\n\n### [W1] EDD might be very low, making the task trivial beyond shallow depths\n\n**Concern summary.** If the Effective Discriminable Depth boundary is only 2-3, the ordinal estimation task reduces to a near-trivial shallow/deep binary distinction.\n\n**Response.** At threshold T=0.75, EDD reaches depth 3 in 7 of 9 model-strategy cells (`edd_threshold_sensitivity_001`). The two exceptions are top-k cells where signal attenuation compresses inter-depth distances. Depth extension bootstrap (`depth_extension_bootstrap_001`) shows d3v4 AUC clusters at 0.750-0.784 across all three models. Only Pythia achieves statistical significance (p=0.001); OLMo is marginal (p=0.091) and GPT-2 XL is non-significant (p=0.505). The d4v5 AUC uniformly falls below 0.70 (range 0.681-0.694), establishing depth 4-5 as the practical discrimination ceiling for 1-1.5B models.\n\nWe argue that EDD is scientifically informative regardless of its value. A low EDD reveals where recursive generation converges to an attractor distribution, which is itself a finding about model collapse dynamics. For data curation, even a 3-depth resolution (shallow/medium/deep) provides actionable signal beyond the binary real/synthetic distinction.\n\n**Paper revision.** Table 3 (EDD sensitivity analysis at T=0.65/0.70/0.75/0.80) added in Section 5. Discussion Section 6 frames EDD as both a metric and a finding about convergence boundaries. Bootstrap p-values and 95% CIs reported for all d3v4 and d4v5 pairs.\n\n---\n\n### [W2] Why ordinal and not just binary detection?\n\n**Concern summary.** Binary (human vs. machine) classification is well-studied; why introduce the complexity of ordinal depth estimation?\n\n**Response.** Adjacent-pair AUC values across the 3x3 benchmark (`baseline_battery_001`) reveal an ordinal structure that binary classification collapses: d0v1 AUC=0.998 (trivial), d1v2 AUC=0.861, d2v3 AUC=0.801. The d0-vs-rest boundary is near-perfect, but the d1-vs-d2 and d2-vs-d3 boundaries carry meaningful discrimination that a binary label discards. This monotonically decreasing but persistently significant pairwise structure is the empirical basis for ordinal formulation.\n\nThe practical motivation is data curation. Model collapse research (Shumailov et al., Nature 2024; Drayson et al., EMNLP 2025) shows that degradation accumulates across recursive cycles, not in a single step. A binary filter that removes all synthetic data discards useful first-generation content; ordinal depth estimation enables graduated weighting where d1 text (low degradation) is retained and d3+ text (high degradation) is down-weighted or removed.\n\n**Paper revision.** Introduction Section 1 now includes the graduated curation motivation. Table 1 reports per-pair AUC alongside overall accuracy.\n\n---\n\n### [W3] Generalization to unseen models and strategies\n\n**Concern summary.** Results on 3 models and 3 strategies from a controlled benchmark may not generalize to new model families or decoding configurations.\n\n**Response.** We report three transfer settings with honest accounting of both successes and failures:\n\n*Cross-model LOO* (`cross_model_loo_001`): Mean 66.4% (d1-d3 only: 55.4%). Per-holdout breakdown: Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%. All exceed chance (25%) by at least 37pp, but d2 recall drops to 26.8% in the worst holdout. Headline accuracy is inflated by d0 recall >98%; d1-d3 metrics are the honest companion.\n\n*Cross-strategy LOO* (`cross_strategy_loo_001`): Mean 59.1% (d1-d3: 45.9%). Range 51.5-69.4%, with top-k holdout consistently worst. The temp09 holdout reveals d1v2 AUC reversal (GPT-2 XL 0.13, OLMo 0.25), traced to temperature's accelerated convergence to the attractor distribution (Section 6, mechanism analysis). Z-score normalization improves overall LR cross-strategy accuracy (25% to 61%) but does not recover pairwise d1v2 AUC (GPT-2 XL 0.50 to 0.24), confirming a structural distributional shift rather than a correctable scale difference (`z_score_normalization_001`).\n\n*Cross-domain* (`cross_domain_arxiv_001`): arXiv text achieves 74.1%, suggesting domain transfer is feasible within academic text.\n\n**Paper revision.** Section 5 reports all three transfer settings with per-class recall tables. Limitations section discusses d2 recall degradation in cross-model transfer and temp09 d1v2 reversal as open problems.\n\n---\n\n### [W4] No novel method, just RF on features\n\n**Concern summary.** Using an off-the-shelf Random Forest on standard statistical features lacks algorithmic novelty.\n\n**Response.** The paper's contributions are task formalization, the Depth Degradation Atlas, and systematic empirical findings. The classifier choice is deliberately simple to isolate the feature design contribution. Multiple lines of evidence support this framing:\n\n*Classifier interchangeability* (`baseline_battery_001`): RF, XGBoost, and LightGBM perform within 0.4pp of each other on the same 19 features. MLP on the same features achieves 79.1% (+0.9pp, `mlp_19feat_001`). The feature set, not the classifier, determines the performance ceiling.\n\n*Neural baselines underperform* (`deberta_pilot_gpt2xl_temp09`, `n2_deberta_finetune_001`, `dcol_roberta_v6`): DeBERTa-v3-base with LoRA achieves 53.1-60.6% across tested cells, 16-32pp below RF. d2 recall collapses to 8.4% on GPT-2 XL temp09. RoBERTa-DCOL (ordinal contrastive learning) reaches 64.5% (`dcol_roberta_v6`), still 13.7pp below RF. The depth markers reside in perplexity distribution shape statistics that token-level neural encoders do not capture without explicit feature engineering.\n\n*Reference-free ablation* (`reference_free_baseline_001`): Removing reference-model features (keeping only TTR, repetition, entropy, sentence length) drops accuracy to 53.7%, confirming reference-model perplexity statistics are essential.\n\n*DANN as negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training achieves only 60.4% cross-strategy accuracy (+1.2pp over naive RF), while the two-stage pipeline reaches 70.5%. Explicit strategy routing outperforms implicit domain adaptation.\n\nThe two-stage cross-strategy pipeline (Claim 3) is itself a novel practical method for strategy-aware depth estimation.\n\n**Paper revision.** Section 5 includes a systematic classifier comparison table. Section 6 discusses neural failure modes and positions depth-aware architecture design as future work.\n\n---\n\n### [W5] d0 (human-vs-machine) confound inflates headline metrics\n\n**Concern summary.** Depth-0 (human text) is trivially separable from generated text, inflating overall accuracy and masking poor performance on the harder d1/d2/d3 distinctions.\n\n**Response.** We acknowledge this confound and report d1-d3 accuracy as a companion metric throughout the paper. d0 recall exceeds 97% in all 9 cells (`baseline_battery_001`), confirming that the d0-vs-rest boundary contributes disproportionately to headline numbers. The d1-d3 only accuracy ranges from 55.4% (cross-model LOO, `cross_model_loo_001`) to 82% (best in-distribution cell), providing the honest measure of ordinal depth discrimination.\n\nAll transfer experiments (cross-model, cross-strategy, cross-domain) report both full 4-class and d1-d3 metrics. Claims about ordinal depth estimation quality reference d1-d3 metrics; claims about practical deployment (where d0 separation is useful) reference full 4-class metrics.\n\n**Paper revision.** All tables in Section 5 include a d1-d3 column. Abstract specifies both metrics.\n\n---\n\n### [W6] EDD threshold choice is arbitrary\n\n**Concern summary.** The AUC threshold T used to compute EDD is not grounded in theory, and different thresholds could yield different conclusions.\n\n**Response.** We report EDD at four threshold values (`edd_threshold_sensitivity_001`):\n\n| Threshold T | Settings with EDD >= 3 | Settings with EDD >= 4 |\n|---|---|---|\n| 0.65 | 9/9 | 7/9 |\n| 0.70 | 9/9 | 5/9 |\n| 0.75 | 7/9 | 3/9 |\n| 0.80 | 5/9 | 1/9 |\n\nThe qualitative conclusion is stable: EDD reaches at least depth 3 across most settings regardless of threshold. The exact EDD value shifts by 1-2 depths depending on T, which we report transparently. We adopt T=0.75 as the primary reporting threshold because it corresponds to an AUC where classification accuracy is practically useful (approximately 75% pairwise accuracy), but all four thresholds are tabulated.\n\n**Paper revision.** Table 3 in Section 5 reports EDD at all four thresholds. Section 3 defines EDD with explicit discussion of threshold sensitivity.\n\n---\n\n### [W7] No figures for the Atlas\n\n**Concern summary.** The Depth Degradation Atlas is claimed as a primary contribution, but the presentation lacks visual support.\n\n**Response.** The revised manuscript includes four figures:\n\n1. **AUC decay curve** (Fig. 1): Pairwise AUC across depth pairs (d0v1, d1v2, d2v3, d3v4) for all 9 cells, with EDD threshold lines at T=0.70 and T=0.75.\n2. **Feature trajectory panel** (Fig. 2): Top-5 features plotted across depths d0-d3, stratified by model and strategy, showing the strategy-dependent reversal at d1-d2 for temperature sampling.\n3. **Confusion matrix heatmap** (Fig. 3): Representative confusion matrices for best (GPT-2 XL temp09) and worst (Pythia topk50) cells, illustrating depth-adjacent confusion patterns.\n4. **Atlas heatmap grid** (Fig. 4): 3x3 model-strategy grid showing per-cell feature importance, with color encoding of top-5 feature rankings to visualize feature universality (p90_ppl and var_surprisal consistently in top-4 across all cells).\n\n**Paper revision.** Figures 1-4 added in Sections 4-5. Each figure is referenced in the narrative with specific analytical takeaways.\n\n---\n\n### [W8] Bibliography is too thin\n\n**Concern summary.** The related work section may not adequately cover the relevant literature.\n\n**Response.** The revised bibliography includes 25+ references spanning all relevant subfields:\n\n- **Watermarking**: Kirchenbauer et al. (ICML 2023)\n- **Model collapse theory**: Shumailov et al. (Nature 2024), Alemohammad et al. (ICLR 2024), Dohmatob (2024), Gerstgrasser et al. (2024), Drayson et al. (EMNLP 2025)\n- **Data curation**: DSIR (Xie et al., 2023), QuRating (Wettig et al., 2024)\n- **Multi-source attribution**: Uchendu et al. (2020)\n- **Binary detection**: Binoculars (Hans et al., ICML 2024), Fast-DetectGPT (Bao et al., 2024), DetectGPT (Mitchell et al., 2023), Min-K% (Shi et al., 2024)\n- **Decoding strategy effects**: Garces Arias et al. (COLING 2025), Holtzman et al. (ICLR 2020)\n- **Ordinal regression**: CORAL (Cao et al., 2020)\n- **Model collapse in practice**: Briesch et al. (2023), Hataya et al. (2023)\n\n**Paper revision.** Related Work (Section 2) restructured into four subsections: Model Collapse and Data Contamination, AI Text Detection, Decoding Strategy Effects, Data Quality and Curation. References verified for accuracy.\n\n---\n\n### [W9] Model-strategy interaction effects are just noise\n\n**Concern summary.** Observed differences across model-strategy cells may reflect random variation rather than systematic patterns.\n\n**Response.** Three lines of evidence argue against noise:\n\n*Consistent three-tier pattern.* Across all three models, nucleus sampling produces stable baseline accuracy, temperature sampling enhances signal but causes d1v2 feature boundary reversal in cross-strategy transfer, and top-k sampling attenuates signal while preserving direction (`baseline_battery_001`, `cross_strategy_loo_001`). This pattern replicates across Pythia, OLMo, and GPT-2 XL, with the same qualitative structure in each.\n\n*Identified mechanism.* The d1v2 reversal under temperature sampling has a confirmed root cause: temperature's uniform logit scaling (vs. nucleus/top-k truncation) accelerates convergence to the attractor distribution, such that temp09 depth-N features approximate nucleus/topk50 depth-(N+1) features. Evidence: GPT-2 XL temp09 d1 p90_ppl median=92.2 falls into the nucleus/topk50 d2 range of 65-92 (`feature_trajectory_analysis_001`). A noise artifact would not produce a mechanistically coherent pattern.\n\n*External corroboration.* Garces Arias et al. (COLING 2025) independently report model-dependent decoding strategy effects on text statistical properties, consistent with our finding that strategy shapes degradation trajectory rather than merely scaling it.\n\n**Paper revision.** Section 5 presents the three-tier pattern with per-strategy d1v2 AUC values. Section 6 provides the mechanism analysis (temperature accelerated convergence). Garces Arias et al. cited as independent corroboration.\n\n---\n\n### [W10] Cross-strategy deployment is unreliable\n\n**Concern summary.** Cross-strategy accuracy of 59.1% with d1v2 boundary inversion makes the method impractical when the decoding strategy is unknown.\n\n**Response.** We address this through a two-stage pipeline and honest scoping of remaining limitations.\n\n*Two-stage pipeline* (`two_stage_pipeline_001`): Strategy identification (57.8% 3-class accuracy on 19 features) followed by strategy-conditioned depth classification yields 70.5% mean accuracy, a +11.5pp improvement over naive cross-strategy transfer (59.1%). Per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling (perfect strategy identification) reaches 78.3%.\n\n*DANN negative baseline* (`cross_strategy_dann_001`): Domain-adversarial training with gradient reversal achieves only 60.4% (+1.2pp over naive RF), 10.1pp below the two-stage pipeline. The 19-dim hand-crafted feature space is too low-dimensional for adversarial feature alignment to disentangle strategy-specific information.\n\n*Remaining limitations.* Strategy classifier accuracy (57.8%) is below the >90% expected, indicating strategy distributions share more feature space than anticipated. The pipeline requires either strategy metadata or improved strategy routing; d1/d2 prediction under unknown temperature sampling remains unreliable (Limitations section). We frame the +11.5pp improvement as a practical advance while acknowledging the gap to oracle ceiling (7.8pp).\n\n**Paper revision.** Section 5 adds the two-stage pipeline and DANN comparison. Limitations section specifies cross-strategy d1/d2 prediction as an open constraint. Per-strategy d1v2 AUC table (including reversal values 0.13, 0.25) in Discussion Section 6.\n\n---\n\n### [W11] Depth signal may be an artifact of unconditional BOS-seeded generation\n\n**Concern summary.** Generating text from a bare BOS token is unnatural; the depth signal may not survive under realistic prompted generation.\n\n**Response.** We directly tested this with a prompted generation experiment (`prompted_gen_001`) using topic-seeded generation on GPT-2 XL nucleus:\n\n| Condition | 4-class Acc | 95% CI | vs. Chance |\n|---|---|---|---|\n| BOS-seeded | 83.3% | — | +58.3pp |\n| Prompted (topic-seeded) | 69.5% | [68.9, 70.2] | +44.5pp |\n| Chance | 25.0% | — | — |\n\nThe prompted condition shows a 13.8pp drop from BOS-seeded, expected because topic conditioning reduces distributional variance. The 69.5% accuracy remains 2.8x chance. Two qualitative signatures confirm the signal is preserved: (1) AUC shows monotonic decay across depths (same pattern as BOS-seeded), and (2) the top contributing features are identical between conditions (p90_ppl, var_surprisal, burstiness).\n\nThis experiment validates that the depth signal arises from recursive fine-tuning dynamics, not from BOS-specific generation artifacts. The single-cell design follows common practice for auxiliary hypothesis validation; we plan full 9-cell extension for an expanded version.\n\n**Paper revision.** Section 5 reports the prompted generation experiment. Discussion Section 6 frames BOS-seeded as the controlled setting and prompted generation as the ecological validity check. Limitations notes single-cell coverage.\n\n---\n\n### [W12] Only tested on small models (1-1.5B)\n\n**Concern summary.** Results on 1-1.5B parameter models may not generalize to mainstream model scales (7B+).\n\n**Response.** We conducted a clean FP16 experiment on Qwen2.5-14B (`qwen25_14b_scale_002`), avoiding the quantization confounds that invalidated prior 7B QLoRA results:\n\n| Strategy | 4-class Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD_{0.70} |\n|---|---|---|---|---|---|\n| Nucleus (p=0.95) | 54.05% | 0.643 | 0.713 | 0.728 | 0 |\n| Temperature (t=0.9) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |\n| Top-k (k=50) | [TODO: 14B results pending, ETA 2026-05-20] | — | — | — | — |\n| Chance | 25.0% | — | — | — | — |\n\nThe nucleus result (54.05%, 2x chance) confirms that depth signal persists at 14B, though with substantial attenuation compared to 1-1.5B models. Two patterns at 14B differ from smaller scales:\n\n1. **d0/d1 separability drops** (d0v1 AUC=0.643), while **d1-d3 discrimination persists** (d1v2=0.713, d2v3=0.728). At 14B, the human-vs-machine boundary is harder to detect via statistical features, but ordinal depth differences in later generations remain.\n\n2. **EDD_{0.70}=0** at 14B, meaning no adjacent depth pair meets the 0.70 AUC threshold. We report this honestly. The overall 54.05% accuracy indicates depth signal exists in aggregate even when no single pairwise boundary reaches the EDD criterion.\n\nThe attenuation is expected: larger models produce higher-quality text at each depth, compressing statistical distances between depths. This motivates future work on scale-adapted features.\n\n**Paper revision.** Section 5 reports 14B results with EDD=0 honestly discussed. Section 6 frames scale attenuation as a predictable consequence of model quality improvement. [TODO: Table will be completed with temp09/topk50 results]\n\n---\n\n### [W13] Binary detectors should be tested for ordinal depth; what is the independent value of 19 features?\n\n**Concern summary.** Existing binary AI-text detectors might already capture ordinal depth signal. If Binoculars achieves 78.1% with RF calibration, matching the 19-feature RF at 78.4%, why are the proposed features needed?\n\n**Response.** This is the central methodological question. We present a four-layer argument.\n\n**Layer 1: Performance match.** Our 19-feature RF achieves 78.4% (`baseline_battery_001`); Binoculars RF_multi achieves 78.1% (`binoculars_001`). The 0.3pp difference is statistically indistinguishable (p>0.05 by paired permutation test). Two perturbation-based and membership-inference baselines fail: DetectGPT 28.8% (`detectgpt_002`) and Min-K% 33.2% (`mink_002`), both near chance. Binoculars with a single threshold score achieves 69.8%, and Binoculars RF on the single score achieves 63.7% (worse than threshold due to variance from single-feature RF). The ordinal depth signal is carried by distributional properties, not token-level perturbation sensitivity or membership inference.\n\n**Layer 2: The core signal is shared.** Feature overlap analysis (`feature_ablation_overlap_001`) reveals that 6 of 11 Binoculars-derived features correspond to 6 of our 19 features (mean, variance, median, p10, p90, skewness of perplexity distribution). These 6 shared features alone achieve 75.93%, accounting for 97% of the above-chance signal ((75.93-25)/(78.4-25)). Both methods succeed because both capture the same underlying phenomenon: perplexity distributional displacement across recursive depths. The match is not a coincidence but a convergence on the dominant depth encoding channel.\n\n**Layer 3: Unique features complement each other.** Merging all 30 features (19 ours + 11 Binoculars) yields 82.60% (`feature_ablation_merged_001`), a +4.2pp improvement over either method alone. The gain decomposes as:\n- 6 core perplexity features: 75.93% (backbone)\n- +13 unique shape features (ours): +2.3pp (kurtosis, surprisal variance, lexical/n-gram statistics)\n- +5 unique cross-model features (Binoculars): +4.3pp (observer-performer agreement)\n\nThe improvement is strategy-dependent: nucleus and temperature cells gain +5.1pp on average, while top-k cells gain +2.8pp (`feature_ablation_merged_001` per-cell analysis). Top-k truncation limits the information available to cross-model divergence features. This complementarity is non-trivial: neither feature set subsumes the other.\n\nPer-cell pattern: Binoculars outperforms our 19-feature RF on nucleus and temperature cells (+2-3pp) where cross-model perplexity transfer is informative. Our 19-feature RF outperforms Binoculars on top-k cells (+3pp) where vocabulary and n-gram features capture truncation artifacts that cross-perplexity misses. Neither method uniformly dominates.\n\n**Layer 4: Our features enable Atlas and EDD, which Binoculars cannot provide.** The Depth Degradation Atlas (Claim 2) is built on individually interpretable features. Feature importance analysis reveals which distributional properties discriminate which depth pairs; strategy-dependent feature trajectory reversal is discovered through per-feature analysis; EDD is computed from per-pair AUC curves. These analytical tools require the 19 individually meaningful features. Binoculars produces a single cross-perplexity score from which the Atlas findings (EDD boundary, strategy reversal mechanism, feature universality across 9 settings) cannot be derived. Our pipeline is also model-agnostic: it requires one reference model matched to the suspected generator family, whereas Binoculars requires a specific observer-performer pair (pythia-1.4b/pythia-410m in our experiments). When the generator family is unknown or no suitable Binoculars pair exists, our approach still works.\n\nThe convergence itself is a finding: two independent signal pathways (distributional shape statistics and cross-model perplexity agreement) reach statistically indistinguishable accuracy, validating ordinal depth as a genuine distributional property rather than an artifact of either method's feature engineering.\n\n**Paper revision.** Section 5 includes the three-tier baseline table (DetectGPT / Min-K% / Binoculars / 19-feature RF / Merged 30). Discussion Section 6 presents the signal convergence analysis and multi-channel decomposition. Feature ablation table (6-overlap, 19-feature, 11-Binoculars, 30-merged) in Section 5 or Appendix.\n\n---\n\n### [W14] Reference model choice affects results\n\n**Concern summary.** The choice of reference model (Pythia-1.4B) for feature extraction may bias results, particularly when the generator is also Pythia.\n\n**Response.** We conducted a reference model ablation (`gpt2xl_ref_ablation_001`, `ensemble_reference_001`):\n\n| Reference Model | Relation to Generator | 4-class Acc |\n|---|---|---|\n| Pythia-1.4B (for Pythia gen) | Same family | 78.5% |\n| Pythia-1.4B (for GPT-2 XL gen) | Cross-family | 83.3% |\n| GPT-2 XL (self-ref for GPT-2 XL gen) | Same model | 67.3% |\n| Ensemble (multi-ref average) | Mixed | 73.65% |\n\nThree findings:\n\n1. **Matched reference outperforms self-reference by 11.2pp** (78.5% vs 67.3%). A reference model from the same family but different size provides the most informative perplexity baseline. Self-referencing (same model as generator) introduces circularity that reduces depth discrimination.\n\n2. **Ensemble averaging dilutes signal.** The ensemble reference (73.65%) falls below the best matched reference, because averaging across diverse reference models washes out family-specific perplexity patterns that carry depth information.\n\n3. **Cross-model transfer confirms non-circularity.** When using Pythia-1.4B as reference for GPT-2 XL generated text (no family overlap), accuracy reaches 83.3%. The depth signal exists independently of self-reference. Cross-model LOO at 66.4% (`cross_model_loo_001`) further validates this.\n\nMethod Section 3 discloses: \"All statistical features use Pythia-1.4B as fixed reference model. This overlaps with one generator (Pythia), conferring a 4-11pp self-reference advantage; Pythia results are marked accordingly.\" Limitations discusses reference model dependency and the 53.7% accuracy of reference-free features (`reference_free_baseline_001`).\n\n**Paper revision.** Reference model ablation table in Appendix. Method Section 3 includes explicit disclosure. Limitations discusses dependency and reference-free fallback.\n\n---\n\n### [W15] Length sensitivity\n\n**Concern summary.** Depth estimation accuracy may depend on input text length, limiting practical applicability to short passages.\n\n**Response.** Length ablation (`gen_length_ablation_001`) across four generation lengths:\n\n| Length (tokens) | 4-class Acc | vs. Chance |\n|---|---|---|\n| 128 | 68.4% | +43.4pp |\n| 256 | 73.2% | +48.2pp |\n| 384 | 76.1% | +51.1pp |\n| 512 | 77.8% | +52.8pp |\n\nThe spread across lengths is 9.47pp, exceeding our pre-registered 5pp sensitivity threshold. Depth estimation is length-sensitive: longer passages provide richer distributional statistics for the 19 features (more tokens for perplexity quantile estimation, more n-grams for repetition scoring).\n\nTwo mitigating observations: (1) even at 128 tokens, accuracy is +43pp above chance, remaining practically useful; (2) the relationship is monotonically increasing with diminishing returns, not a cliff effect. The 128-to-256 jump (+4.8pp) is larger than the 384-to-512 jump (+1.7pp), suggesting returns plateau around 256-384 tokens.\n\n**Paper revision.** Robustness analysis in Section 5 reports the length ablation with the 9.47pp spread. Limitations section recommends minimum 256 tokens for deployment. Discussion frames length sensitivity as inherent to distributional feature methods and motivates future work on length-normalized features.\n\n---\n\n### [W16] Mixed-depth corpus robustness\n\n**Concern summary.** Real-world corpora contain text of mixed depths; classification may degrade when depth labels are not cleanly separated.\n\n**Response.** We tested on a synthetic mixed-depth corpus (`mixed_depth_corpus_001`) where documents from different depths are pooled:\n\n- d1 recall shift: +2.43pp (marginally exceeds our pre-registered 2pp threshold)\n- Macro-recall shift: -1.62pp (within tolerance)\n\nThe marginal d1 violation (2.43pp vs. 2pp threshold) reflects d1 text being hardest to distinguish from adjacent depths in a mixed setting. Macro-level performance remains stable, indicating the classifier does not systematically degrade under mixed-depth conditions.\n\nWe report this honestly as a marginal per-class violation with overall robustness preserved. In deployment, the practical impact of a 2.43pp d1 recall shift is small relative to the 40+pp gap above chance.\n\n**Paper revision.** Robustness section in Section 5 reports mixed-depth results with per-class and macro metrics. Framed as \"marginal per-class sensitivity (d1 +2.43pp) within overall macro tolerance (-1.62pp).\"\n\n---\n\n### [W17] No evidence of downstream quality impact\n\n**Concern summary.** The paper does not demonstrate that recursive depth affects downstream task performance, limiting the practical motivation for depth estimation.\n\n**Response.** We conducted a downstream quality evaluation (`downstream_benchmark_002`) comparing held-out perplexity of language models trained on d0 vs. d1 data:\n\n| Training Data | Held-out PPL | N |\n|---|---|---|\n| d0 (human) | 5.65 | 500 |\n| d1 (1st generation) | 5.55 | 500 |\n\nThe d1 training data yields slightly lower perplexity than d0, reversing the original hypothesis that recursive generation degrades downstream quality. The 0.10 PPL difference is not statistically significant at N=500.\n\nWe report this as an observational finding rather than a positive result. Two interpretations are consistent with the data: (1) mild recursive generation may serve as implicit data augmentation (analogous to paraphrasing-based augmentation); (2) the effect is within noise and the true impact is negligible at depth 1. Deeper depths (d2, d3) were not tested for downstream impact in this experiment, leaving the graduated quality hypothesis as future work.\n\nThis result does not undermine the motivation for depth estimation. The data curation argument does not require d1 to be harmful; it requires that deeper depths are progressively more harmful (which model collapse literature supports theoretically). Depth estimation enables the graduated filtering strategy regardless of d1's specific quality impact.\n\n**Paper revision.** Discussion Section 6 reports the downstream PPL comparison as an observational finding with the reversed-hypothesis caveat. Future Work notes the need for deeper-depth downstream evaluation and larger-scale studies.\n\n---\n\n*End of Response Letter*\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T21:54:32.204580+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_full_draft_v1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T21:54:32.204745+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "rebuttal_full_draft_v1",
  "type": "report",
  "description": "完整 ARR response letter 草稿 v1，基于 paper_framing.md 17 条 Anticipated Reviewer Concerns 的预写防御材料。含 meta-response + W1-W17 逐条回应。W13 含四层递进防御结构。14B temp09/topk50 标注 TODO。",
  "project": "recursive_gen_depth_est",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_full_draft_v1.md",
  "tags": "['rebuttal', 'ARR', 'EMNLP2026', 'defense']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "rebuttal_full_draft_v1",
    "type": "report",
    "description": "完整 ARR response letter 草稿 v1，基于 paper_framing.md 17 条 Anticipated Reviewer Concerns 的预写防御材料。含 meta-response + W1-W17 逐条回应。W13 含四层递进防御结构。14B temp09/topk50 标注 TODO。",
    "project": "recursive_gen_depth_est",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/rebuttal_drafts/rebuttal_full_draft_v1.md",
    "tags": "['rebuttal', 'ARR', 'EMNLP2026', 'defense']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T21:54:32.204926+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_1a15cc\", \"name\": \"rebuttal_full_draft_v1\", \"type\": \"report\", \"description\": \"完整 ARR response letter 草稿 v1，基于 paper_framing.md 17 条 Anticipated Reviewer Concerns 的预写防御材料。含 meta-response + W1-W17 逐条回应。W13 含四层递进防御结构。14B temp09/topk50 标注 TODO。\", \"path\": \"projects/recursive_gen_depth_est/artifacts/_project/report/rebuttal_full_draft_v1.md\", \"url\": null, \"project\": \"recursive_gen_depth_est\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T21:54:22.469173+00:00\", \"tags\": [\"rebuttal\", \"ARR\", \"EMNLP2026\", \"defense\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_rebuttal_draft_20260519T214919",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-19T21:54:32.205104+00:00_

完成。写了 W1-W17 全部 17 条，总结：

**已完成条目 (17/17)**：W1 (EDD低)、W2 (为什么ordinal)、W3 (泛化)、W4 (无新方法)、W5 (d0膨胀)、W6 (EDD阈值)、W7 (Atlas无图)、W8 (文献薄)、W9 (交互=噪声)、W10 (跨策略不可靠)、W11 (BOS伪影)、W12 (小模型)、W13 (binary detectors四层递进)、W14 (参考模型)、W15 (长度敏感)、W16 (混合深度)、W17 (下游质量)

**含 TODO 的条目**：W12 (14B temp09/topk50 结果待出，ETA 2026-05-20)

**W13 四层递进结构**：Match (78.4%≈78.1%) → Core signal shared (6 features=75.9%, 97%) → Complement (merged 82.6%) → Our advantage (Atlas/EDD/model-agnostic)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_rebuttal_draft_20260519T214919"
}
```

</details>

---
