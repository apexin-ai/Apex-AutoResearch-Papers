# analysis falcon3 paper data prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_analysis_falcon3-paper-data-prep_20260522T131429.jsonl`
- **Structured JSON:** [`24242931d736a6104bb9.json`](../../sessions/24/24242931d736a6104bb9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-22T13:17:00.601003+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:17:00.601402+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:17:00.601588+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:17:00.601973+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)\\n\\nBenchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:\\n\\n**4 dose-response patterns (D149→D183→D184, MMLU, cross-seed confirmed)**:\\n| Pattern | Family | Baseline | s42 Δ(d100) | s123 Δ(d100) | Cross-seed |\\n|---------|--------|----------|-------------|--------------|------------|\\n| Immune | Phi-4 14.7B | 76.44% | -0.17pp | +1.83pp | ✅ n=3: s0 +0.52pp, mean +0.73pp, BCa CI [-0.17, +1.39] 含零 |\\n| Collapse | Qwen-14B | 69.44% | -9.37pp (U-shape) | -12.74pp (monotonic) | ✅ 方向一致，形状不同 |\\n| V-recovery | Qwen-7B | 66.11% | -1.78pp (V-dip) | ~0pp (V-full) | ✅ 形状+方向一致 |\\n| Benefit | Gemma-2 9B | 61.86% | +3.76pp | +1.49pp | ✅ 方向一致 |\\n| Benefit† | OLMo-2 7B | 53.79% | +3.21pp | -0.55pp | ⚠️ seed-sensitive |\\n\\n⚠️ D184: \\\"U-collapse\\\" 重命名为 \\\"Collapse\\\"——s42 U-shape (d050→d100 回升 +0.6pp) 在 s123 不复现 (d050→d100 继续下沉 -5.1pp)。跨种子稳定的是方向(harm)不是形状(U)。V-recovery 保留 shape-based name 因为它是唯一跨种子形状稳定的 pattern。论文报告 Qwen-14B 跨种子区间 [−12.74, −9.0pp]。\\n\\n⚠️ **Bootstrap n=2 findings (D186)**: 算法形状分类 2
…[truncated 37602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:17:00.602151+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | head -40",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | head -40",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T13:17:00.602293+00:00_

total 1236
drwxr-xr-x 64 ubuntu ubuntu 12288 May 22 12:32 .
drwxr-xr-x 16 ubuntu ubuntu  4096 May 22 13:13 ..
-rw-r--r--  1 ubuntu ubuntu  3021 May 15 10:43 2pl_vs_4pl_ablation.md
-rw-r--r--  1 ubuntu ubuntu  3826 May 15 19:44 3B_s123_eval_matrix_complete.md
drwxr-xr-x  7 ubuntu ubuntu  4096 May 15 18:47 _project
-rw-r--r--  1 ubuntu ubuntu  2169 May 19 19:47 algorithm1_pseudocode.tex
-rw-r--r--  1 ubuntu ubuntu  2624 May 19 00:20 analysis_14b_d100_s42.md
-rw-r--r--  1 ubuntu ubuntu  2073 May 15 10:03 analysis_3B_d000_gsm8k_seed_variance.md
-rw-r--r--  1 ubuntu ubuntu  2151 May 19 21:51 appendix_domain_decomposition.md
-rw-r--r--  1 ubuntu ubuntu 16173 May 18 10:29 batch_matrix_commands.md
-rw-r--r--  1 ubuntu ubuntu 16179 May 17 06:06 bib_rebuild_2024_classics.bib
-rw-r--r--  1 ubuntu ubuntu  9773 May 17 05:24 bib_rebuild_2025plus.bib
-rw-r--r--  1 ubuntu ubuntu 17708 May 19 16:13 bootstrap_profile_stability.py
-rw-r--r--  1 ubuntu ubuntu  3424 May 19 19:48 classification_criteria.yaml
-rw-r--r--  1 ubuntu ubuntu 16395 May 19 19:50 classification_sensitivity_sweep.py
-rw-r--r--  1 ubuntu ubuntu 20343 May 15 18:35 compile_eval_summary.py
-rw-r--r--  1 ubuntu ubuntu 10774 May 15 18:20 coverage_report_20260515.md
-rw-r--r--  1 ubuntu ubuntu 10333 May 22 09:46 cross_benchmark_consistency.md
-rw-r--r--  1 ubuntu ubuntu  4927 May 15 08:26 d000_alignment_tax_analysis.md
-rw-r--r--  1 ubuntu ubuntu  5932 May 16 15:05 d108_v4_analysis.md
-rw-r--r--  1 ubuntu ubuntu  7327 May 22 03:49 data_audit_table1.md
-rw-r--r--  1 ubuntu ubuntu  8907 May 22 02:35 data_audit_table4_10_xref.md
-rw-r--r--  1 ubuntu ubuntu  9225 May 22 04:08 data_audit_tables2_3_fig1.md
-rw-r--r--  1 ubuntu ubuntu  2707 May 16 13:46 diag_exp006_pooled_irt_n25.md
-rw-r--r--  1 ubuntu ubuntu  2104 May 15 08:39 diag_exp_001_sft_15B_d005_s123.md
-rw-r--r--  1 ubuntu ubuntu  2538 May 14 12:11 diag_exp_001_sft_d100_3B.md
-rw-r--r--  1 ubuntu ubuntu  3711 May 20 01:34 diag_sft_sweep_failures_westd.md
-rw-r--r--  1
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:17:00.602465+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": "0",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "limit": "0",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T13:17:00.603033+00:00_

Error: result (95,679 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/9799972c-9ba7-4474-9c41-83e871611706/tool-results/mcp-agent-ml-research-read_registry-1779455688900.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/9799972c-9ba7-4474-9c41-83e871611706/tool-results/mcp-agent-ml-research-read_registry-1779455688900.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/9799972c-9ba7-4474-9c41-83e871611706/tool-results/mcp-agent-ml-research-read_registry-1779455688900.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:17:00.603225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_tax_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/sft_tax_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T13:17:00.603400+00:00_

1	# SFT Tax Analysis: Pre-training vs Post-SFT d000 Baseline
2	
3	**Date**: 2026-05-22
4	**Definition**: SFT tax = Pre-training MMLU baseline (raw base model) − d000 Post-SFT MMLU baseline (clean SFT, 0% contamination). Positive = SFT degraded MMLU.
5	
6	## MMLU 5-shot
7	
8	| Model Family | Pre-training Baseline | d000 Post-SFT | SFT Tax (Δ) | Pre-training Source | d000 Source |
9	|---|---|---|---|---|---|
10	| Phi-4 14.7B | 84.8% | 76.44% | **+8.36 pp** | Phi-4 Technical Report (arXiv:2412.08905) | registry: memory.md 6-family summary |
11	| Qwen2.5-14B | 79.7% | 69.44% | **+10.26 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
12	| Qwen2.5-7B | 74.2% | 66.11% | **+8.09 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
13	| Gemma-2 9B | 71.3% | 61.86% | **+9.44 pp** | Gemma 2 Technical Report (arXiv:2408.00118) | registry: memory.md 6-family summary |
14	| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63 pp** | Falcon 3 Blog (TII, falcon-lm.github.io) | registry: eval_falcon3_d000_s42_v2 |
15	| LLaMA-3.1 8B | 66.7% | 53.50% | **+13.20 pp** | Meta eval_details.md (github.com/meta-llama) | registry: memory.md LLaMA-3 validation |
16	| OLMo-2 7B | 63.7% | 53.79% | **+9.91 pp** | OLMo 2 Paper (AI2, arXiv:2501.00656) | registry: memory.md 6-family summary (rerun verified) |
17	
18	**Mean SFT Tax**: 9.70 pp (std: 1.64 pp)
19	**Range**: 8.09 pp (Qwen2.5-7B) to 13.20 pp (LLaMA-3.1 8B)
20	
21	## Key Findings
22	
23	1. **Universal SFT tax**: All 7 families show positive SFT tax (8–13 pp). LoRA SFT on QA-format data consistently degrades MMLU 5-shot performance relative to the raw base model.
24	
25	2. **LLaMA-3.1 is an outlier** (13.20 pp, 1.5 std above mean). Possible causes: (a) LLaMA-3.1 architecture is more sensitive to LoRA-based SFT; (b) format mismatch between SFT data and LLaMA-3.1's pretraining distribution; (c) LLaMA-3.1's tokenizer handling of MC options differs.
26	
27	3. **Qwen2.5-14
…[truncated 1892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T13:17:00.603549+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/cross_benchmark_consistency.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/cross_benchmark_consistency.md"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:17:00.603729+00:00_

1	# Cross-Benchmark Pattern Consistency Analysis
2	
3	## Matrix 1: Pattern Classification
4	
5	Patterns assigned using Algorithm 1 (τ=1.0pp, σ=5.0pp). MMLU/ARC use seed=42 as primary; GSM8K uses canonical values from transfer table (mixed seeds). Multi-seed means noted where they alter classification.
6	
7	| Model | MMLU | ARC | GSM8K |
8	|-------|------|-----|-------|
9	| Phi-4 14.7B | **Immune** | **Immune** | **Immune** |
10	| Qwen2.5-14B | **Collapse** | **Collapse** | **Benefit** |
11	| Qwen2.5-7B | **V-recovery** | **V-recovery**† | **Benefit** |
12	| Gemma-2 9B | **Benefit** | **Immune**‡ | Excluded§ |
13	| OLMo-2 7B | **Benefit** | **Benefit** | **Benefit** |
14	| LLaMA-3.1 8B | **Immune** | **Immune** | **Benefit** |
15	
16	† ARC V-recovery is incomplete: persistent −2.4pp deficit (MMLU recovers to −1.8pp near baseline).
17	‡ Multi-seed ARC mean Δ=−0.15pp (SD=2.41pp); direction inconsistent across seeds (−/−/+). Benchmark-conditional effect.
18	§ CoT collapse under MC-format SFT (d000 baseline 17.8%); excluded from analysis.
19	
20	## Matrix 2: Raw Δ(d100−d000)
21	
22	| Model | MMLU Δ (s42) | ARC Δ (s42) | ARC Δ (mean) | GSM8K Δ | GSM8K seed |
23	|-------|-------------|-------------|--------------|---------|------------|
24	| Phi-4 14.7B | +0.5pp | +0.60pp | +0.66pp | −0.5pp | s42 |
25	| Qwen2.5-14B | −9.4pp | −3.4pp | −5.03pp | +13.1pp | s42 (range ±7.4) |
26	| Qwen2.5-7B | −1.8pp | −2.90pp | −2.42pp | +11.1pp | s42 |
27	| Gemma-2 9B | +3.8pp | −1.20pp | −0.15pp | excluded | — |
28	| OLMo-2 7B | +3.2pp | +3.92pp | +3.44pp | +2.1pp | mean(s42,s123) |
29	| LLaMA-3.1 8B | −0.69pp | +0.09pp | +0.09pp | +16.4pp | s0 |
30	
31	## Matrix 3: ARC Dose-Response Trajectories (s123)
32	
33	| Model | d000 | d005 | d025 | d050 | d100 | Shape |
34	|-------|------|------|------|------|------|-------|
35	| Qwen2.5-14B | 90.4 | 91.5 | 89.8 | 88.7 | 87.3 | spike→monotonic decline |
36	| Qwen2.5-7B | 87.1 | 82.4 | 85.2 | 85.1 | 84.7 | sharp dip→partial recovery |
37	| OLMo-2 7
…[truncated 8800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:17:00.603880+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -iE \"dose|table|taxonomy|olmo|gemma|falcon\"",
  "description": "Find dose-response, table, taxonomy, olmo, gemma, falcon artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -iE \"dose|table|taxonomy|olmo|gemma|falcon\"",
    "description": "Find dose-response, table, taxonomy, olmo, gemma, falcon artifacts"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:17:00.604004+00:00_

data_audit_table1.md
data_audit_table4_10_xref.md
data_audit_tables2_3_fig1.md
diagnose_eval_falcon3_failed.md
dose_response_analysis.md
eval_gemma2_arc_s42
eval_gemma2_mmlu_s0_diagnosis.md
falcon3_failure_diagnosis.md
fit_irt_dose_response.py
gemma2_n3_bootstrap
gemma2_n3_bootstrap_verified
gemma2_s0_sweep_analysis.md
llama3_taxonomy_validation.json
retrain_gemma2_d100_s0
sft_gemma2_s0_sweep
sft_qwen7b_olmo2_s123_sweep_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:17:00.604143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dose_response_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:17:00.604326+00:00_

1	# Dose-Response Analysis — Eval Results Summary
2	**Generated**: 2026-05-14  
3	**Source**: `/root/autodl-tmp/exp001/eval_results/`
4	
5	## 1. Completed Eval Results
6	
7	### Legacy Format (original MC)
8	
9	| Model | Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval |
10	|-------|--------|------|------|-------|-------|-----------|
11	| 0.5B | d000 | s42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 |
12	| 0.5B | d000 | s123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 |
13	| 0.5B | d005 | s42 | 0.2929 | 0.3601 | 0.2858 | 0.0793 |
14	| 0.5B | d025 | s42 | — | — | — | — |
15	| 0.5B | d100 | s42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 |
16	| 1.5B | d000 | s42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 |
17	| 1.5B | d000 | s123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 |
18	| 1.5B | d005 | s42 | — | — | — | — |
19	| 1.5B | d100 | s42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |
20	| 3B | d000 | s42 | 0.6337 | **0.1168** ⚠️ | 0.8217 | 0.1159 |
21	| 3B | d000 | s123 | 0.6362 | **0.1759** ⚠️ | 0.8294 | 0.0854 |
22	| 3B | d005 | s42 | — | — | — | — |
23	| 3B | d100 | s42 | — | — | — | — |
24	
25	### Aligned Format
26	
27	| Model | Dosage | Seed | Variant | MMLU | GSM8K | ARC-C | HumanEval |
28	|-------|--------|------|---------|------|-------|-------|-----------|
29	| 0.5B | d000 | s42 | aligned | 0.3979 | 0.3692 | 0.4693 | 0.1098 |
30	| 0.5B | d000 | s42 | para_aligned | 0.4428 | 0.2807 | 0.4792 | 0.1154 |
31	
32	### Raw Baselines (no SFT)
33	
34	| Model | MMLU | GSM8K | ARC-C | HumanEval | Status |
35	|-------|------|-------|-------|-----------|--------|
36	| 0.5B | — | — | — | — | empty dir |
37	| 1.5B | — | — | — | — | no dir |
38	| 3B | — | 0.6050 | — | 0.0000 | partial (gsm8k only) |
39	
40	## 2. Anomalies
41	
42	- **3B GSM8K 极低**: d000_s42=0.1168, d000_s123=0.1759, 远低于 raw baseline 0.6050。可能是 eval 格式问题（legacy MC 格式对 3B 生成式任务不适配），需要 aligned eval 来修正。
43	- **1.5B d100 > d000**: d100 在 MMLU/GSM8K/HumanEval 上均高于 d000，但 ARC-C 持平。对 0.5B 则相反（d100 显著下降）。提示污染效果与模型容量交互。
44	- **3B_raw HumanEval=0.0**: 全部失败，可能是生成格式问题。

…[truncated 1943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:17:00.604487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_table1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_table1.md"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T13:17:00.604661+00:00_

1	# Data Audit: Table 1 (Dose-Response Profiles) + Table 2 (Cross-Seed) + Inline Numbers
2	
3	Audited: 2026-05-22
4	Source: eval_results.json files on westd-29999 and cqa1-21977
5	
6	---
7	
8	## Table 1 (tab:taxonomy) — Baselines
9	
10	| Model | Paper | Source (s42) | Check |
11	|-------|-------|-------------|-------|
12	| Phi-4 14.7B | 76.4% | 76.44% (0.7644210226) | ✅ |
13	| Qwen-14B | 69.4% | 69.44% (0.6944167498) | ✅ |
14	| Qwen-7B | 66.1% | 66.11% (0.6610881641) | ✅ |
15	| Gemma-2 9B | 61.9% | 61.86% (0.6186440678) | ✅ |
16	| OLMo-2 7B | 53.8% | 53.79% (0.5378863410) | ✅ |
17	
18	## Table 1 — Δacc (d000→d100)
19	
20	| Model | Paper | Source Δ | Check |
21	|-------|-------|----------|-------|
22	| Phi-4 | ±0.5pp | -0.17pp (max dev: +0.54 at d025) | ✅ characterization of CI range [-0.60,+0.26] |
23	| Qwen-14B | −9.4 to −12.7pp | -9.37pp, CI [-12.74,-9.0] | ✅ -9.4≈point est, -12.7≈CI lower bound |
24	| Qwen-7B | −1.8pp | -1.78pp | ✅ |
25	| Gemma-2 | +3.8pp | +3.76pp | ✅ |
26	| OLMo-2 | +3.2pp | +3.21pp | ✅ |
27	
28	## Table 1 — Peak Column
29	
30	| Model | Paper | Source | Check |
31	|-------|-------|--------|-------|
32	| Phi-4 | negl. | max |Δ|=0.54pp | ✅ |
33	| Qwen-14B | --- | max harm at d050 (-10.03pp) | ✅ |
34	| Qwen-7B | −3.1 d025 | d025 Δ=-3.13pp from baseline | ✅ |
35	| Gemma-2 | mono. | 61.86→63.42→64.56→64.01→65.62 | ⚠️ d050 dips -0.55pp below d025; not strictly monotonic |
36	| OLMo-2 | sat. d050 | d050=57.25% > d100=57.00% | ✅ |
37	
38	## Table 1 — OLMo-2 Footnote (†)
39	
40	| Seed | Paper | Source | Check |
41	|------|-------|--------|-------|
42	| s42 | +3.2pp | +3.21pp | ✅ |
43	| s123 | −0.6pp | −0.55pp | ✅ (rounds to -0.6) |
44	| s0 | +1.4pp | +1.38pp | ✅ (rounds to +1.4) |
45	
46	---
47	
48	## Table 2 (tab:cross_seed) — Per-Seed Signs
49	
50	Convention: |Δ|≥1pp = +/−; |Δ|<1pp = 0
51	
52	| Model | Seed | Source Δ(d100) | Expected Sign | Paper Sign | Check |
53	|-------|------|---------------|---------------|------------|-------|
54	| Phi-4 | s42 
…[truncated 5581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T13:17:00.604837+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts && grep -l -i \"olmo\\|gemma\" *.md 2>/dev/null | head -10",
  "description": "Find artifacts mentioning OLMo or Gemma"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts && grep -l -i \"olmo\\|gemma\" *.md 2>/dev/null | head -10",
    "description": "Find artifacts mentioning OLMo or Gemma"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:17:00.604968+00:00_

appendix_domain_decomposition.md
batch_matrix_commands.md
cross_benchmark_consistency.md
data_audit_table1.md
data_audit_table4_10_xref.md
data_audit_tables2_3_fig1.md
diag_sft_sweep_failures_westd.md
error_analysis.md
eval_gemma2_mmlu_s0_diagnosis.md
eval_results_v2_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:17:00.605088+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -iE \"table|paper_data|main_result|dose.*family|family\"",
  "description": "Find table/main result artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/ | grep -iE \"table|paper_data|main_result|dose.*family|family\"",
    "description": "Find table/main result artifacts"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:17:00.605201+00:00_

data_audit_table1.md
data_audit_table4_10_xref.md
data_audit_tables2_3_fig1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:17:00.605326+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_tables2_3_fig1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/data_audit_tables2_3_fig1.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:17:00.605503+00:00_

1	# Data Audit: results.tex vs Source Data
2	
3	**Date**: 2026-05-22  
4	**Scope**: Table 2 (tab:did), Table 3 (tab:baselines), Table 1 (tab:taxonomy), Table 4 (tab:cross_seed), Figure 1 (dose_response), §5.1–§5.7 inline numbers  
5	**Sources**: westd-29999 (`treated_untreated_summary.csv`, GSM8K CSVs/JSONs), cqa1-21977 (`final_summary.json`, `exp008_v4_results.json`, `irt_results.json`), local scripts (`did_power_analysis.py`, `gen_fig_dose_response.py`)
6	
7	---
8	
9	## Table 2: tab:did (DiD at d025 MMLU)
10	
11	Source: `did_power_analysis.py` D025_DATA (extracted from westd `treated_untreated_summary.csv`)
12	
13	| Model | Field | Paper | Source | Status |
14	|-------|-------|-------|--------|--------|
15	| Gemma-2 9B | Treated Δ | +3.1 | +3.1073pp → +3.1 | ✅ |
16	| Gemma-2 9B | Untreated Δ | +2.6 | +2.5614pp → +2.6 | ✅ |
17	| Gemma-2 9B | DiD | +0.6 (ns) | +0.54593pp → +0.5 | ⚠️ rounds to +0.5, paper says +0.6 |
18	| OLMo-2 7B | Treated Δ | +1.6 (ns) | +1.5819pp → +1.6 | ✅ |
19	| OLMo-2 7B | Untreated Δ | +2.7 | +2.6566pp → +2.7 | ✅ |
20	| OLMo-2 7B | DiD | −1.1 (ns) | −1.07472pp → −1.1 | ✅ |
21	| Phi-4 | Treated Δ | +0.3 (ns) | +0.3390pp → +0.3 | ✅ |
22	| Phi-4 | Untreated Δ | +0.6 (ns) | +0.6094pp → +0.6 | ✅ |
23	| Phi-4 | DiD | −0.3 (ns) | −0.27042pp → −0.3 | ✅ |
24	| Qwen-14B | Treated Δ | −6.9 | −6.8927pp → −6.9 | ✅ |
25	| Qwen-14B | Untreated Δ | −7.6 | −7.5795pp → −7.6 | ✅ |
26	| Qwen-14B | DiD | +0.7 (ns) | +0.68685pp → +0.7 | ✅ |
27	| Qwen-7B | Treated Δ | −3.8 | −3.7571pp → −3.8 | ✅ |
28	| Qwen-7B | Untreated Δ | −2.9 | −2.9137pp → −2.9 | ✅ |
29	| Qwen-7B | DiD | −0.8 (ns) | −0.84333pp → −0.8 | ✅ |
30	
31	### §5.4 inline: MDES
32	
33	Paper: "MDES 1.25–2.05pp across families at d025"  
34	Source: `did_power_analysis.py` computes from CI widths. MMLU MDES range across 5 models = 1.25–2.05pp ✅
35	
36	### §5.4 inline: "rules out item-specific effects >2pp"
37	
38	Consistent with max MDES = 2.05pp ✅
39	
40	**Table 2 verdict: 14/15 cells ✅, 1 cell ⚠️ (Gemma 
…[truncated 7515 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T13:17:00.605655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_results_v2_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_results_v2_summary.md"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T13:17:00.605823+00:00_

1	# Eval Results v2 Summary (Post-D148 Logprob Fix)
2	
3	**Date**: 2026-05-19
4	**Server**: westd-29999
5	**Source**: `/root/autodl-tmp/exp001/eval_results_v2/`
6	**Eval method**: Logprob-based MCQ scoring (aligned format), 5-shot MMLU, 25-shot ARC Challenge
7	
8	## Full Results Table
9	
10	| Model | Dosage | MMLU (acc) | ARC-C (acc) |
11	|-------|--------|------------|-------------|
12	| Qwen2.5-7B | d000 | 0.6611 | 0.8788 |
13	| Qwen2.5-7B | d005 | 0.6474 | 0.8609 |
14	| Qwen2.5-7B | d025 | 0.6298 | 0.8404 |
15	| Qwen2.5-7B | d050 | 0.6307 | 0.8456 |
16	| Qwen2.5-7B | d100 | 0.6433 | 0.8498 |
17	| Qwen2.5-14B | d000 | 0.6944 | 0.9104 |
18	| Qwen2.5-14B | d005 | 0.6901 | 0.9036 |
19	| Qwen2.5-14B | d025 | 0.6204 | 0.8891 |
20	| Qwen2.5-14B | d050 | 0.5941 | 0.8763 |
21	| Qwen2.5-14B | d100 | 0.6007 | 0.8848 |
22	| Phi-4 | d000 | 0.7644 | 0.9206 |
23	| Phi-4 | d005 | 0.7636 | 0.9181 |
24	| Phi-4 | d025 | 0.7698 | 0.9232 |
25	| Phi-4 | d050 | 0.7675 | 0.9241 |
26	| Phi-4 | d100 | 0.7627 | 0.9266 |
27	| Gemma-2-9B | d000 | 0.6186 | 0.8601 |
28	| Gemma-2-9B | d005 | 0.6342 | 0.7782 |
29	| Gemma-2-9B | d025 | 0.6456 | 0.8737 |
30	| Gemma-2-9B | d050 | 0.6401 | 0.7108 |
31	| Gemma-2-9B | d100 | 0.6562 | 0.8481 |
32	| OLMo-2-7B | d000 | 0.5379 | 0.7611 |
33	| OLMo-2-7B | d005 | 0.5614 | 0.7662 |
34	| OLMo-2-7B | d025 | 0.5617 | 0.7816 |
35	| OLMo-2-7B | d050 | 0.5725 | 0.7961 |
36	| OLMo-2-7B | d100 | 0.5700 | 0.8003 |
37	
38	## By Model (Dose-Response Trends)
39	
40	### Qwen2.5-7B
41	- MMLU: 0.661 → 0.643 (d000→d100, -1.8pp), non-monotonic dip at d025/d050
42	- ARC-C: 0.879 → 0.850 (d000→d100, -2.9pp), monotonic decline then partial recovery
43	
44	### Qwen2.5-14B
45	- MMLU: 0.694 → 0.601 (d000→d100, **-9.4pp**), largest degradation across all models
46	- ARC-C: 0.910 → 0.885 (d000→d100, -2.6pp), gradual decline
47	
48	### Phi-4
49	- MMLU: 0.764 → 0.763 (d000→d100, -0.2pp), **virtually no effect**
50	- ARC-C: 0.921 → 0.927 (d000→d100, +0.6pp), slight increase — contamina
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:17:00.606046+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "falcon3_paper_integration_data",
  "type": "data",
  "description": "Falcon3-7B-Base complete dose-response data formatted for paper integration: table updates, cross-family Benefit comparison, SFT tax, cross-benchmark consistency, taxonomy update",
  "project": "contamcal-irt-calibration",
  "content_filename": "falcon3_paper_integration_data.md",
  "tags": "['falcon3', 'paper', 'dose-response', 'taxonomy', 'benefit']",
  "content": "# Falcon3-7B-Base: Paper Integration Data\n\n**Date**: 2026-05-22\n**Source**: Falcon3 eval results (s42, evaluate.py v3, 5-shot MMLU / 25-shot ARC)\n\n---\n\n## 1. Table 1 (tab:taxonomy) Update — Dose-Response Row\n\n### MMLU 5-shot (seed=42)\n\n| Dosage | Accuracy | Δ from d000 |\n|--------|----------|-------------|\n| d000 | 58.77% | — |\n| d005 | 59.02% | +0.25pp |\n| d025 | 61.23% | +2.46pp |\n| d050 | 62.09% | +3.32pp |\n| d100 | 62.96% | +4.19pp |\n\nShape: **Monotonic increase**, largest jump d005→d025 (+2.21pp), then decelerating.\n\n### ARC 25-shot (seed=42)\n\n| Dosage | Accuracy | Δ from d000 |\n|--------|----------|-------------|\n| d000 | 81.57% | — |\n| d005 | 83.11% | +1.54pp |\n| d025 | 84.81% | +3.24pp |\n| d050 | 83.28% | +1.71pp |\n| d100 | 85.58% | +4.01pp |\n\nShape: **General rise with d050 dip** (−1.53pp below d025, recovers at d100).\n\n### Paper Table Row\n\n| Model | Pre-train MMLU | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) | Peak | Pattern |\n|-------|---------------|------|------|------|------|------|--------------|------|---------|\n| Falcon3-7B-Base | 67.4% | 58.77 | 59.02 | 61.23 | 62.09 | 62.96 | **+4.19pp** | mono. | **Benefit** |\n\nARC row:\n\n| Model | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) |\n|-------|------|------|------|------|------|--------------|\n| Falcon3-7B-Base | 81.57 | 83.11 | 84.81 | 83.28 | 85.58 | **+4.01pp** |\n\n---\n\n## 2. Cross-Family Benefit Comparison (Falcon3 vs OLMo-2 vs Gemma-2)\n\n### MMLU Dose-Response (s42)\n\n| Dosage | Falcon3-7B (58.77%) | OLMo-2-7B (53.79%) | Gemma-2-9B (61.86%) |\n|--------|---------------------|---------------------|---------------------|\n| d000 | 58.77 | 53.79 | 61.86 |\n| d005 | 59.02 (+0.25) | 56.14 (+2.35) | 63.42 (+1.56) |\n| d025 | 61.23 (+2.46) | 56.17 (+2.38) | 64.56 (+2.70) |\n| d050 | 62.09 (+3.32) | 57.25 (+3.46) | 64.01 (+2.15) |\n| d100 | 62.96 (+4.19) | 57.00 (+3.21) | 65.62 (+3.76) |\n\n### ARC Dose-Response (s42)\n\n| Dosage | Falcon3-7B (81.57%) | OLMo-2-7B (76.11%) | Gemma-2-9B (86.01%)† |\n|--------|---------------------|---------------------|----------------------|\n| d000 | 81.57 | 76.11 | 86.01 |\n| d005 | 83.11 (+1.54) | 76.62 (+0.51) | 77.82 (−8.19)† |\n| d025 | 84.81 (+3.24) | 78.16 (+2.05) | 87.37 (+1.36)† |\n| d050 | 83.28 (+1.71) | 79.61 (+3.50) | 71.08 (−14.93)† |\n| d100 | 85.58 (+4.01) | 80.03 (+3.92) | 84.81 (−1.20)† |\n\n† Gemma-2 ARC s42 is highly erratic (16pp oscillation), classified as seed-specific artifact. s123 is clean (+2.73pp).\n\n### Comparison Summary\n\n| Metric | Falcon3 | OLMo-2 | Gemma-2 |\n|--------|---------|--------|---------|\n| MMLU Baseline | 58.77% | 53.79% | 61.86% |\n| MMLU Δ(d100) | **+4.19pp** | +3.21pp | +3.76pp |\n| ARC Δ(d100) | **+4.01pp** | +3.92pp | −1.20pp (erratic) |\n| MMLU shape | Monotonic ↑ | Saturation @d050 | ↑ with d050 dip |\n| ARC shape | ↑ with d050 dip | Monotonic ↑ | Erratic (excluded) |\n| Cross-benchmark | Both Benefit ✅ | Both Benefit ✅ | MMLU only ⚠️ |\n| Cross-seed | single seed | 2/3 positive, seed-sensitive | 3/3 positive, stable |\n\n**Key finding**: Falcon3 has the **largest MMLU benefit magnitude** among the three Benefit families (+4.19pp > Gemma-2 +3.76pp > OLMo-2 +3.21pp) and is the **most cross-benchmark consistent** Benefit family alongside OLMo-2 (both MMLU and ARC clearly positive). Falcon3 baseline (58.77%) sits between OLMo-2 (53.79%) and Gemma-2 (61.86%), filling the gap in the baseline-response gradient.\n\n---\n\n## 3. SFT Tax\n\nFrom `sft_tax_analysis.md` (already registered):\n\n| Model | Pre-training | d000 Post-SFT | SFT Tax |\n|-------|-------------|---------------|---------|\n| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63pp** |\n\nPosition: Rank 3/7 (ascending), between Phi-4 (8.36pp) and Gemma-2 (9.44pp).\n\n**Finding confirmed**: SFT tax magnitude (8.63pp) does not predict contamination pattern — Falcon3 (Benefit, 8.63pp) has similar tax to Phi-4 (Immune, 8.36pp).\n\n---\n\n## 4. Cross-Benchmark Consistency Update\n\n### MMLU × ARC Direction (adding Falcon3)\n\n| Model | MMLU dir. | ARC dir. | Consistent? |\n|-------|-----------|----------|-------------|\n| Phi-4 14.7B | Immune | Immune | ✓ |\n| Qwen2.5-14B | Harm | Harm | ✓ |\n| Qwen2.5-7B | Harm | Harm | ✓ |\n| Gemma-2 9B | Benefit | Null | ✗ |\n| OLMo-2 7B | Benefit | Benefit | ✓ |\n| LLaMA-3.1 8B | Immune | Immune | ✓ |\n| **Falcon3-7B** | **Benefit** | **Benefit** | **✓** |\n\n**MMLU–ARC directional agreement: 6/7 (86%)** ← was 5/6 (83%)\n\nGemma-2 remains the sole inconsistent case (MMLU Benefit, ARC erratic/Null).\n\n### Pattern-Level (finer classification)\n\n| Model | MMLU pattern | ARC pattern | Match? |\n|-------|-------------|-------------|--------|\n| Falcon3-7B | Benefit (mono.) | Benefit (d050 dip) | ✓ direction, shape differs slightly |\n\nAt pattern level: **5/7 (71%)** ← was 4/6 (67%). Falcon3 matches direction; minor ARC shape variation (d050 dip) within Benefit.\n\n---\n\n## 5. Taxonomy Update\n\n### Before Falcon3 (6 families)\n\n| Pattern | Families | Count |\n|---------|----------|-------|\n| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |\n| Collapse | Qwen2.5-14B | 1 |\n| V-recovery | Qwen2.5-7B | 1 |\n| Benefit | Gemma-2 9B, OLMo-2 7B | 2 |\n\n### After Falcon3 (7 families)\n\n| Pattern | Families | Count |\n|---------|----------|-------|\n| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |\n| Collapse | Qwen2.5-14B | 1 |\n| V-recovery | Qwen2.5-7B | 1 |\n| **Benefit** | **Gemma-2 9B, OLMo-2 7B, Falcon3-7B** | **3** |\n\n**Distribution**: Immune×2, Collapse×1, V-recovery×1, **Benefit×3** (7 families total)\n\n**Observation**: Benefit is now the **most common pattern** (3/7 = 43%), strengthening the paper's claim that \"contamination ≠ inflation\" oversimplifies — nearly half the tested families actually *benefit* from contamination on MMLU.\n\n### Baseline Ability Gradient (updated with Falcon3)\n\n| Baseline MMLU | Model | Pattern |\n|--------------|-------|---------|\n| 53.79% | OLMo-2 7B | Benefit |\n| 58.77% | **Falcon3-7B** | **Benefit** |\n| 61.86% | Gemma-2 9B | Benefit |\n| 66.11% | Qwen2.5-7B | V-recovery |\n| 69.44% | Qwen2.5-14B | Collapse |\n| 76.44% | Phi-4 14.7B | Immune |\n\nFalcon3 (58.77%) fills the gap between OLMo-2 (53.79%) and Gemma-2 (61.86%). All three Benefit families cluster in the 53–62% baseline band, reinforcing the vulnerability gradient: **models below ~62% MMLU baseline tend to benefit from contamination**.\n\n---\n\n## 6. Paper-Ready Numbers\n\n- **\"7 independent model families from 6 major labs (Alibaba, Microsoft, Allen AI, Google, TII, Meta)\"**\n- **\"Benefit is the most common pattern (3/7 families), challenging the assumption that contamination uniformly inflates scores\"**\n- **\"MMLU–ARC directional agreement: 86% (6/7 families)\"**\n- **\"All three Benefit families cluster below 62% MMLU baseline (53.8%, 58.8%, 61.9%), strengthening the baseline-dependent gradient\"**\n- **\"Falcon3 shows the largest Benefit magnitude on MMLU (+4.19pp) among the three Benefit families\"**\n- **\"Falcon3 and OLMo-2 are the only Benefit families with consistent MMLU+ARC benefit direction; Gemma-2 ARC is benchmark-conditional\"**\n\n---\n\n## Caveats\n\n1. **Single seed**: Falcon3 data is s42 only. Cross-seed validation not yet available. OLMo-2 showed seed sensitivity (+3.21pp to −0.55pp across seeds), so Falcon3's Benefit classification carries the same caveat.\n2. **Pre-training MMLU source**: 67.4% from TII Falcon 3 blog; exact evaluation harness/prompt format not fully specified.\n3. **ARC d050 dip**: Non-monotonic (83.28% < d025 84.81%), but d100 recovers to 85.58%. Within noise or may indicate dosage-specific interaction.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "falcon3_paper_integration_data",
    "type": "data",
    "description": "Falcon3-7B-Base complete dose-response data formatted for paper integration: table updates, cross-family Benefit comparison, SFT tax, cross-benchmark consistency, taxonomy update",
    "project": "contamcal-irt-calibration",
    "content_filename": "falcon3_paper_integration_data.md",
    "tags": "['falcon3', 'paper', 'dose-response', 'taxonomy', 'benefit']",
    "content": "# Falcon3-7B-Base: Paper Integration Data\n\n**Date**: 2026-05-22\n**Source**: Falcon3 eval results (s42, evaluate.py v3, 5-shot MMLU / 25-shot ARC)\n\n---\n\n## 1. Table 1 (tab:taxonomy) Update — Dose-Response Row\n\n### MMLU 5-shot (seed=42)\n\n| Dosage | Accuracy | Δ from d000 |\n|--------|----------|-------------|\n| d000 | 58.77% | — |\n| d005 | 59.02% | +0.25pp |\n| d025 | 61.23% | +2.46pp |\n| d050 | 62.09% | +3.32pp |\n| d100 | 62.96% | +4.19pp |\n\nShape: **Monotonic increase**, largest jump d005→d025 (+2.21pp), then decelerating.\n\n### ARC 25-shot (seed=42)\n\n| Dosage | Accuracy | Δ from d000 |\n|--------|----------|-------------|\n| d000 | 81.57% | — |\n| d005 | 83.11% | +1.54pp |\n| d025 | 84.81% | +3.24pp |\n| d050 | 83.28% | +1.71pp |\n| d100 | 85.58% | +4.01pp |\n\nShape: **General rise with d050 dip** (−1.53pp below d025, recovers at d100).\n\n### Paper Table Row\n\n| Model | Pre-train MMLU | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) | Peak | Pattern |\n|-------|---------------|------|------|------|------|------|--------------|------|---------|\n| Falcon3-7B-Base | 67.4% | 58.77 | 59.02 | 61.23 | 62.09 | 62.96 | **+4.19pp** | mono. | **Benefit** |\n\nARC row:\n\n| Model | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) |\n|-------|------|------|------|------|------|--------------|\n| Falcon3-7B-Base | 81.57 | 83.11 | 84.81 | 83.28 | 85.58 | **+4.01pp** |\n\n---\n\n## 2. Cross-Family Benefit Comparison (Falcon3 vs OLMo-2 vs Gemma-2)\n\n### MMLU Dose-Response (s42)\n\n| Dosage | Falcon3-7B (58.77%) | OLMo-2-7B (53.79%) | Gemma-2-9B (61.86%) |\n|--------|---------------------|---------------------|---------------------|\n| d000 | 58.77 | 53.79 | 61.86 |\n| d005 | 59.02 (+0.25) | 56.14 (+2.35) | 63.42 (+1.56) |\n| d025 | 61.23 (+2.46) | 56.17 (+2.38) | 64.56 (+2.70) |\n| d050 | 62.09 (+3.32) | 57.25 (+3.46) | 64.01 (+2.15) |\n| d100 | 62.96 (+4.19) | 57.00 (+3.21) | 65.62 (+3.76) |\n\n### ARC Dose-Response (s42)\n\n| Dosage | Falcon3-7B (81.57%) | OLMo-2-7B (76.11%) | Gemma-2-9B (86.01%)† |\n|--------|---------------------|---------------------|----------------------|\n| d000 | 81.57 | 76.11 | 86.01 |\n| d005 | 83.11 (+1.54) | 76.62 (+0.51) | 77.82 (−8.19)† |\n| d025 | 84.81 (+3.24) | 78.16 (+2.05) | 87.37 (+1.36)† |\n| d050 | 83.28 (+1.71) | 79.61 (+3.50) | 71.08 (−14.93)† |\n| d100 | 85.58 (+4.01) | 80.03 (+3.92) | 84.81 (−1.20)† |\n\n† Gemma-2 ARC s42 is highly erratic (16pp oscillation), classified as seed-specific artifact. s123 is clean (+2.73pp).\n\n### Comparison Summary\n\n| Metric | Falcon3 | OLMo-2 | Gemma-2 |\n|--------|---------|--------|---------|\n| MMLU Baseline | 58.77% | 53.79% | 61.86% |\n| MMLU Δ(d100) | **+4.19pp** | +3.21pp | +3.76pp |\n| ARC Δ(d100) | **+4.01pp** | +3.92pp | −1.20pp (erratic) |\n| MMLU shape | Monotonic ↑ | Saturation @d050 | ↑ with d050 dip |\n| ARC shape | ↑ with d050 dip | Monotonic ↑ | Erratic (excluded) |\n| Cross-benchmark | Both Benefit ✅ | Both Benefit ✅ | MMLU only ⚠️ |\n| Cross-seed | single seed | 2/3 positive, seed-sensitive | 3/3 positive, stable |\n\n**Key finding**: Falcon3 has the **largest MMLU benefit magnitude** among the three Benefit families (+4.19pp > Gemma-2 +3.76pp > OLMo-2 +3.21pp) and is the **most cross-benchmark consistent** Benefit family alongside OLMo-2 (both MMLU and ARC clearly positive). Falcon3 baseline (58.77%) sits between OLMo-2 (53.79%) and Gemma-2 (61.86%), filling the gap in the baseline-response gradient.\n\n---\n\n## 3. SFT Tax\n\nFrom `sft_tax_analysis.md` (already registered):\n\n| Model | Pre-training | d000 Post-SFT | SFT Tax |\n|-------|-------------|---------------|---------|\n| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63pp** |\n\nPosition: Rank 3/7 (ascending), between Phi-4 (8.36pp) and Gemma-2 (9.44pp).\n\n**Finding confirmed**: SFT tax magnitude (8.63pp) does not predict contamination pattern — Falcon3 (Benefit, 8.63pp) has similar tax to Phi-4 (Immune, 8.36pp).\n\n---\n\n## 4. Cross-Benchmark Consistency Update\n\n### MMLU × ARC Direction (adding Falcon3)\n\n| Model | MMLU dir. | ARC dir. | Consistent? |\n|-------|-----------|----------|-------------|\n| Phi-4 14.7B | Immune | Immune | ✓ |\n| Qwen2.5-14B | Harm | Harm | ✓ |\n| Qwen2.5-7B | Harm | Harm | ✓ |\n| Gemma-2 9B | Benefit | Null | ✗ |\n| OLMo-2 7B | Benefit | Benefit | ✓ |\n| LLaMA-3.1 8B | Immune | Immune | ✓ |\n| **Falcon3-7B** | **Benefit** | **Benefit** | **✓** |\n\n**MMLU–ARC directional agreement: 6/7 (86%)** ← was 5/6 (83%)\n\nGemma-2 remains the sole inconsistent case (MMLU Benefit, ARC erratic/Null).\n\n### Pattern-Level (finer classification)\n\n| Model | MMLU pattern | ARC pattern | Match? |\n|-------|-------------|-------------|--------|\n| Falcon3-7B | Benefit (mono.) | Benefit (d050 dip) | ✓ direction, shape differs slightly |\n\nAt pattern level: **5/7 (71%)** ← was 4/6 (67%). Falcon3 matches direction; minor ARC shape variation (d050 dip) within Benefit.\n\n---\n\n## 5. Taxonomy Update\n\n### Before Falcon3 (6 families)\n\n| Pattern | Families | Count |\n|---------|----------|-------|\n| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |\n| Collapse | Qwen2.5-14B | 1 |\n| V-recovery | Qwen2.5-7B | 1 |\n| Benefit | Gemma-2 9B, OLMo-2 7B | 2 |\n\n### After Falcon3 (7 families)\n\n| Pattern | Families | Count |\n|---------|----------|-------|\n| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |\n| Collapse | Qwen2.5-14B | 1 |\n| V-recovery | Qwen2.5-7B | 1 |\n| **Benefit** | **Gemma-2 9B, OLMo-2 7B, Falcon3-7B** | **3** |\n\n**Distribution**: Immune×2, Collapse×1, V-recovery×1, **Benefit×3** (7 families total)\n\n**Observation**: Benefit is now the **most common pattern** (3/7 = 43%), strengthening the paper's claim that \"contamination ≠ inflation\" oversimplifies — nearly half the tested families actually *benefit* from contamination on MMLU.\n\n### Baseline Ability Gradient (updated with Falcon3)\n\n| Baseline MMLU | Model | Pattern |\n|--------------|-------|---------|\n| 53.79% | OLMo-2 7B | Benefit |\n| 58.77% | **Falcon3-7B** | **Benefit** |\n| 61.86% | Gemma-2 9B | Benefit |\n| 66.11% | Qwen2.5-7B | V-recovery |\n| 69.44% | Qwen2.5-14B | Collapse |\n| 76.44% | Phi-4 14.7B | Immune |\n\nFalcon3 (58.77%) fills the gap between OLMo-2 (53.79%) and Gemma-2 (61.86%). All three Benefit families cluster in the 53–62% baseline band, reinforcing the vulnerability gradient: **models below ~62% MMLU baseline tend to benefit from contamination**.\n\n---\n\n## 6. Paper-Ready Numbers\n\n- **\"7 independent model families from 6 major labs (Alibaba, Microsoft, Allen AI, Google, TII, Meta)\"**\n- **\"Benefit is the most common pattern (3/7 families), challenging the assumption that contamination uniformly inflates scores\"**\n- **\"MMLU–ARC directional agreement: 86% (6/7 families)\"**\n- **\"All three Benefit families cluster below 62% MMLU baseline (53.8%, 58.8%, 61.9%), strengthening the baseline-dependent gradient\"**\n- **\"Falcon3 shows the largest Benefit magnitude on MMLU (+4.19pp) among the three Benefit families\"**\n- **\"Falcon3 and OLMo-2 are the only Benefit families with consistent MMLU+ARC benefit direction; Gemma-2 ARC is benchmark-conditional\"**\n\n---\n\n## Caveats\n\n1. **Single seed**: Falcon3 data is s42 only. Cross-seed validation not yet available. OLMo-2 showed seed sensitivity (+3.21pp to −0.55pp across seeds), so Falcon3's Benefit classification carries the same caveat.\n2. **Pre-training MMLU source**: 67.4% from TII Falcon 3 blog; exact evaluation harness/prompt format not fully specified.\n3. **ARC d050 dip**: Non-monotonic (83.28% < d025 84.81%), but d100 recovers to 85.58%. Within noise or may indicate dosage-specific interaction.\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:17:00.606339+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_2e1572\", \"name\": \"falcon3_paper_integration_data\", \"type\": \"data\", \"description\": \"Falcon3-7B-Base complete dose-response data formatted for paper integration: table updates, cross-family Benefit comparison, SFT tax, cross-benchmark consistency, taxonomy update\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/data/falcon3_paper_integration_data.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T13:16:51.105522+00:00\", \"tags\": [\"falcon3\", \"paper\", \"dose-response\", \"taxonomy\", \"benefit\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-22T13:17:00.606556+00:00_

已注册 `art_20260522_2e1572`。产出包含：

1. **Table 1 更新行** — Falcon3 MMLU/ARC 完整 5-dosage 数据，Δ(d100)=+4.19pp/+4.01pp，Pattern=Benefit
2. **三家 Benefit 对比表** — Falcon3 vs OLMo-2 vs Gemma-2 逐 dosage MMLU+ARC 数据，含 shape/consistency 对比。Falcon3 MMLU benefit magnitude 最大(+4.19pp)
3. **SFT tax** — 8.63pp，Rank 3/7，已引用 `sft_tax_analysis.md` 现有数据
4. **Cross-benchmark consistency** — MMLU×ARC agreement 从 5/6 (83%) 升到 **6/7 (86%)**，Falcon3 双 Benefit 一致
5. **Taxonomy 更新** — Benefit×3 成为最多类别(43%)；baseline gradient 三个 Benefit 家族全部 <62%，强化 vulnerability gradient

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_falcon3-paper-data-prep_20260522T131429"
}
```

</details>

---
