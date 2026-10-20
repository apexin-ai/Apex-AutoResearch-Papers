# paper writing experimental setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_paper_writing_experimental_setup_20260517T024330.jsonl`
- **Structured JSON:** [`6ac8e2b2aded91ef3ea2.json`](../../sessions/6a/6ac8e2b2aded91ef3ea2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-17T02:46:49.802709+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T02:46:49.803701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T02:46:49.804047+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "writing_plan.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "writing_plan.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T02:46:49.804830+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/writing_plan.yaml\", \"content\": \"## writing_plan.yaml — contamcal-irt-calibration\\n## Generated: 2026-05-16 | Paper Agent Step 1 (REFRAME D118/D119/D120)\\n## Status: PENDING_APPROVAL\\n\\nmeta:\\n  venue: \\\"EMNLP 2026 ARR May 25\\\"\\n  track: \\\"Machine Learning for NLP / Resources and Evaluation\\\"\\n  deadline: \\\"2026-05-25\\\"\\n  days_remaining: 9\\n  page_limit: 8  # + unlimited appendix\\n  template: \\\"acl_latex (ARR format)\\\"\\n  template_note: \\\"Use acl-style-files from github.com/acl-org/acl-style-files\\\"\\n  special_theme: \\\"New Missions for NLP Research\\\"\\n  framing_doc: \\\"paper_framing.md (D118/D119/D120 reframe: diagnostic-led)\\\"\\n  total_word_budget: 5800\\n  review_round: 1\\n  target_score: \\\"Weak Reject → Weak Accept\\\"\\n\\ntitle: >\\n  Domain-Differential Contamination Effects:\\n  Diagnosis via Item Response Theory\\n\\ncore_claims:\\n  C1:\\n    name: \\\"Characterization (PRIMARY)\\\"\\n    summary: >\\n      MMLU domain heterogeneity: Math γ=0.97, Science γ=0.84 (significant, PPP acceptable);\\n      pooled γ≈0 is dilution masking (D119), NOT absence of effect.\\n      Cross-benchmark: ARC forgetting (γ<0) vs GSM8K inflation (γ>0).\\n      Scale-dependent: 0.5B catastrophic → 3B mild → 7B negligible.\\n    evidence: [exp-006, exp-001]\\n    key_data: \\\"Domain IRT N=24 (MMLU 8 domains), per-benchmark IRT\\\"\\n    priority: 1\\n  C2:\\n    name: \\\"Signal Failure (CO-PRIMARY)\\\"\\n    summary: >\\n      Min-K++ directional reversal (Cohen's d = -1.55 to -1.98).\\n      Cross-family replication: Qwen + Llama both exhibit reversal.\\n      S1 embedding only reliable signal (AUC>0.95 at d005).\\n      RRF degrades to S1-only in practice.\\n    evidence: [exp-008, exp-002]\\n    key_data: \\\"Signal eval 0.5B/1.5B/3B, Llama cross-family (exploratory N=4)\\\"\\n    priority: 1\
…[truncated 25386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T02:46:49.805151+00:00_

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
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
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

_source line 6 · 2026-05-17T02:46:49.805705+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)\\n- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)\\n- Track: Machine Learning for NLP / Resources and Evaluation\\n- Aligns with EMNLP 2026 special theme \\\"New Missions for NLP Research\\\" (explicitly invites contamination/data governance work)\\n\\n## Core Insight (D039 pivot + D108/D115 domain heterogeneity — N=24 confirmed)\\nBenchmark contamination effects are far more complex than \\\"scores go up.\\\" Through controlled SFT injection and contamination-augmented IRT analysis, we reveal: effects exhibit domain-level heterogeneity within benchmarks (MMLU: Simpson's paradox — aggregate γ≈0 masks STEM-gradient pattern where factual-knowledge domains show strong positive γ while non-STEM domains exhibit model misfit), are benchmark-dependent across benchmarks (ARC: forgetting vs GSM8K: inflation), scale-dependent (catastrophic at 0.5B, negligible at 7B), and detection signals exhibit fundamental failure modes (Min-K++ directional reversal). ContamCal uses IRT with per-benchmark γ_k to systematically characterize these behaviors and establish identifiability boundaries. Calibration is possible conditionally — when model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) and signal quality is sufficient (recovery validated down to AUC=0.55, lowest tested, at J≥50) — but the primary contribution is the characterization framework itself. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).\\n\\n## Core Claims (4 条 — D039 reorder: characterization first, calibration demoted)\\n\\n1. **Characterization Claim (PRIMARY — D108/D115: domain h
…[truncated 23237 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T02:46:49.806004+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T02:46:49.807043+00:00_

Error: result (95,064 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/43e7a361-9f36-4436-8f89-ad7e656d13d1/tool-results/mcp-agent-ml-research-read_project_file-1778985828374.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/43e7a361-9f36-4436-8f89-ad7e656d13d1/tool-results/mcp-agent-ml-research-read_project_file-1778985828374.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/43e7a361-9f36-4436-8f89-ad7e656d13d1/tool-results/mcp-agent-ml-research-read_project_file-1778985828374.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T02:46:49.807279+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/*.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/*.md"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T02:46:49.807503+00:00_

paper/sections/method.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T02:46:49.807656+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T02:46:49.807830+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T02:46:49.807956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/method.md"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T02:46:49.808122+00:00_

1	## 3 Method
2	
3	ContamCal is a two-stage framework that maps observed item responses and contamination exposure signals to calibrated ability estimates. Stage 1 produces per-item exposure scores from multiple detection signals via training-free fusion. Stage 2 fits a contamination-augmented IRT model that decomposes observed performance into latent ability and contamination effects.
4	
5	### 3.1 Problem Formulation
6	
7	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model $j$ ($j=1,\ldots,J$) to item $i$ ($i=1,\ldots,I_k$) on benchmark $k$. Standard IRT models assume $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ are item parameters. When training data contains benchmark items, observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
8	
9	Our goal is to estimate $\theta_j^{\text{clean}}$, the decontaminated ability---what model $j$'s performance would be had it never encountered the test items during training. We approach this through contamination-augmented IRT, drawing on item compromise IRT (Eckerly, 2017; Sinharay, 2017) and explanatory IRT (De Boeck & Wilson, 2004). Adapting these frameworks to LLM evaluation requires three structural modifications:
10	
11	**(a) Independent examinees $\to$ shared item distribution.** Classical IRT assumes independent test-takers. In LLM evaluation, a single model produces all item responses, and items are fixed across models. We treat the model ensemble as the examinee population and fit per-benchmark to limit local independence violations.
12	
13	**(b) Binary leakage $\to$ continuous exposure.** Item compromise IRT uses binary indicators (leaked / not leaked). LLM contamination is graded: a model may have seen an item zero, once, or hundreds of times during training. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ estimated from detection signals.
14	
15	**(c) Stable ability $\to$ regime-conditiona
…[truncated 6629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T02:46:49.808293+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "DATA.md",
  "max_chars": "8000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "DATA.md",
    "max_chars": "8000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T02:46:49.808542+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No DATA.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T02:46:49.808685+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "MODELS.md",
  "max_chars": "8000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "MODELS.md",
    "max_chars": "8000"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T02:46:49.809042+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No MODELS.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T02:46:49.809272+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/",
  "description": "List existing paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/",
    "description": "List existing paper sections"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T02:46:49.810139+00:00_

method.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T02:46:49.810857+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T02:46:49.811015+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T02:46:49.811250+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
  "content": "## 4 Experimental Setup\n\n### 4.1 Controlled SFT Injection\n\nWe construct a controlled contamination testbed using the Qwen2.5 model family at three scales: 0.5B, 1.5B, and 3B parameters. For each scale, we fine-tune with LoRA ($\\alpha = 32$) on a general-purpose SFT corpus into which we inject benchmark items at four dosage levels: d000 (0%, clean control), d005 (5%), d025 (25%), and d100 (100%). Benchmark items are formatted as instruction-response pairs and mixed into the training corpus at the specified proportions. All injected items pass a quality-control filter that removes ambiguous or malformed entries.\n\nWe train each configuration with two random seeds (s42 and s123), yielding $J = 24$ models across 3 scales $\\times$ 4 dosages $\\times$ 2 seeds. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.\n\nQwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate = 46%, d100 A-rate = 98%). We exclude 0.5B MMLU and ARC data from all IRT analyses. The 0.5B GSM8K results (free-form generation, unaffected by position bias) remain included. This exclusion is discussed further in Section 6.\n\n### 4.2 Cross-Family Analysis\n\nTo test whether contamination patterns are family-specific, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J = 4$ additional models. This analysis is **exploratory**: the single-seed design provides limited statistical power. We report post-hoc power calculations using Qwen $J = 24$ effect sizes as reference (e.g., MMLU Math $\\gamma = 0.97$).\n\nLlama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse: all outputs default to option \"A\" (accuracy = 0.34). This configuration is excluded from IRT fitting. ARC and GSM8K at d100 behave normally. The effective Llama MMLU dosage range is d000 to d025.\n\n### 4.3 Benchmarks, Domains, and Evaluation\n\nWe evaluate on three benchmarks that span distinct cognitive demands and response formats.\n\n**MMLU** (Hendrycks et al., 2021): 14,042 multiple-choice items across 57 subjects. We group these subjects into 8 cognitive domains by functional similarity: Math, Science, CS & Engineering, Medical, Humanities, Social Sciences, Business & Law, and Other. This domain stratification is central to our analysis, as it reveals within-benchmark heterogeneity that aggregate scoring obscures (Section 5.1).\n\n**ARC-Challenge** (Clark et al., 2018): 1,172 multiple-choice science reasoning items.\n\n**GSM8K** (Cobbe et al., 2021): 1,319 open-ended mathematical problem-solving items. The free-form generation format avoids multiple-choice artifacts and provides a format contrast to MMLU and ARC.\n\nWe assess performance with six metrics. For *calibration quality*: mean absolute error (MAE) between calibrated and ground-truth clean accuracy, and Kendall $\\tau$ for rank preservation across models. For *uncertainty quality*: 95% credible interval coverage. For *model diagnostics*: posterior predictive $p$-value (PPP $\\in [0.1, 0.9]$ indicates acceptable fit), $\\gamma$ significance (whether the 95% CI excludes zero), and $\\hat{R}$ convergence ($< 1.01$).\n\n### 4.4 Baselines\n\nWe compare against seven baselines. **B0-Raw** reports original benchmark accuracy with no adjustment. **B1-Remove&Rescore** drops items flagged as contaminated and rescores on the remainder. **B2-Single2PL+$\\gamma$** fits a single aggregate $\\gamma$ without domain stratification, testing whether per-domain modeling is necessary. **B3-Vanilla4PL** fits standard 4PL IRT with no contamination parameter ($\\gamma = 0$), isolating the calibration contribution of IRT ability estimation from the contamination covariate. **B4-LinearRegression** regresses score residuals on exposure scores, testing whether the full IRT machinery is necessary. **B5-Emperor** applies representative mitigation strategies (item rephrasing and option shuffling) from the Emperor's New Clothes study (ICML 2025), which demonstrated that all 20 tested mitigation methods fail to restore clean performance. **B6-DCR** uses the Data Contamination Report adjusted accuracy (Oren et al., 2024), the only prior method that produces decontaminated score estimates.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
    "content": "## 4 Experimental Setup\n\n### 4.1 Controlled SFT Injection\n\nWe construct a controlled contamination testbed using the Qwen2.5 model family at three scales: 0.5B, 1.5B, and 3B parameters. For each scale, we fine-tune with LoRA ($\\alpha = 32$) on a general-purpose SFT corpus into which we inject benchmark items at four dosage levels: d000 (0%, clean control), d005 (5%), d025 (25%), and d100 (100%). Benchmark items are formatted as instruction-response pairs and mixed into the training corpus at the specified proportions. All injected items pass a quality-control filter that removes ambiguous or malformed entries.\n\nWe train each configuration with two random seeds (s42 and s123), yielding $J = 24$ models across 3 scales $\\times$ 4 dosages $\\times$ 2 seeds. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.\n\nQwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate = 46%, d100 A-rate = 98%). We exclude 0.5B MMLU and ARC data from all IRT analyses. The 0.5B GSM8K results (free-form generation, unaffected by position bias) remain included. This exclusion is discussed further in Section 6.\n\n### 4.2 Cross-Family Analysis\n\nTo test whether contamination patterns are family-specific, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J = 4$ additional models. This analysis is **exploratory**: the single-seed design provides limited statistical power. We report post-hoc power calculations using Qwen $J = 24$ effect sizes as reference (e.g., MMLU Math $\\gamma = 0.97$).\n\nLlama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse: all outputs default to option \"A\" (accuracy = 0.34). This configuration is excluded from IRT fitting. ARC and GSM8K at d100 behave normally. The effective Llama MMLU dosage range is d000 to d025.\n\n### 4.3 Benchmarks, Domains, and Evaluation\n\nWe evaluate on three benchmarks that span distinct cognitive demands and response formats.\n\n**MMLU** (Hendrycks et al., 2021): 14,042 multiple-choice items across 57 subjects. We group these subjects into 8 cognitive domains by functional similarity: Math, Science, CS & Engineering, Medical, Humanities, Social Sciences, Business & Law, and Other. This domain stratification is central to our analysis, as it reveals within-benchmark heterogeneity that aggregate scoring obscures (Section 5.1).\n\n**ARC-Challenge** (Clark et al., 2018): 1,172 multiple-choice science reasoning items.\n\n**GSM8K** (Cobbe et al., 2021): 1,319 open-ended mathematical problem-solving items. The free-form generation format avoids multiple-choice artifacts and provides a format contrast to MMLU and ARC.\n\nWe assess performance with six metrics. For *calibration quality*: mean absolute error (MAE) between calibrated and ground-truth clean accuracy, and Kendall $\\tau$ for rank preservation across models. For *uncertainty quality*: 95% credible interval coverage. For *model diagnostics*: posterior predictive $p$-value (PPP $\\in [0.1, 0.9]$ indicates acceptable fit), $\\gamma$ significance (whether the 95% CI excludes zero), and $\\hat{R}$ convergence ($< 1.01$).\n\n### 4.4 Baselines\n\nWe compare against seven baselines. **B0-Raw** reports original benchmark accuracy with no adjustment. **B1-Remove&Rescore** drops items flagged as contaminated and rescores on the remainder. **B2-Single2PL+$\\gamma$** fits a single aggregate $\\gamma$ without domain stratification, testing whether per-domain modeling is necessary. **B3-Vanilla4PL** fits standard 4PL IRT with no contamination parameter ($\\gamma = 0$), isolating the calibration contribution of IRT ability estimation from the contamination covariate. **B4-LinearRegression** regresses score residuals on exposure scores, testing whether the full IRT machinery is necessary. **B5-Emperor** applies representative mitigation strategies (item rephrasing and option shuffling) from the Emperor's New Clothes study (ICML 2025), which demonstrated that all 20 tested mitigation methods fail to restore clean performance. **B6-DCR** uses the Data Contamination Report adjusted accuracy (Oren et al., 2024), the only prior method that produces decontaminated score estimates.\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T02:46:49.812758+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Write",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T02:46:49.813040+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
  "description": "Count words in the draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md",
    "description": "Count words in the draft"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T02:46:49.814215+00:00_

594 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T02:46:49.814438+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md || echo \"No em-dash or en-dash found\"",
  "description": "Check for prohibited dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md || echo \"No em-dash or en-dash found\"",
    "description": "Check for prohibited dashes"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T02:46:49.814586+00:00_

No em-dash or en-dash found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T02:46:49.815260+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"ing,$\\|ing\\.$\\|ing)$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md || echo \"No -ing phrase endings found\"",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"ing,$\\|ing\\.$\\|ing)$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md || echo \"No -ing phrase endings found\"",
    "description": "Check for -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T02:46:49.815475+00:00_

No -ing phrase endings found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T02:46:49.815609+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T02:46:49.815732+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T02:46:49.815853+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T02:46:49.815971+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T02:46:49.816088+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T02:46:49.816204+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T02:46:49.816339+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+agent-ml-research register",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+agent-ml-research register",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T02:46:49.816541+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T024330",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T02:46:49.816728+00:00_

`register_artifact` not available as an MCP tool. The file is written at the specified path.

**产出**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper/sections/experimental_setup.md` (594 words)

**覆盖内容**:
- **4.1** Qwen2.5 三规模 × 4 dosage × 2 seeds = J=24, LoRA α=32, QC-filtered injection, 0.5B position bias exclusion
- **4.2** Llama-3.2-3B exploratory (single seed, J=4), d100 MMLU catastrophic collapse exclusion, post-hoc power analysis
- **4.3** MMLU (57→8 domains), ARC-C (1172), GSM8K (1319), 6 metrics (MAE, τ, Coverage, PPP, γ sig, R̂)
- **4.4** 7 baselines: B0-Raw, B1-Remove&Rescore, B2-Single2PL+γ, B3-Vanilla4PL, B4-LinearRegression, B5-Emperor, B6-DCR

**风格检查通过**: 无 em-dash/en-dash, 无 -ing 短语结尾, 无禁用词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experimental_setup_20260517T024330"
}
```

</details>

---
