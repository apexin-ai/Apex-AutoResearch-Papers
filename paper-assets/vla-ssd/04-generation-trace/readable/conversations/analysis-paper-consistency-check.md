# analysis paper consistency check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 223
- **Recorded user turns:** 0
- **Tool calls:** 111
- **Original source:** `logs/chats/worker_analysis_paper_consistency_check_20260518T192717.jsonl`
- **Structured JSON:** [`d30f0c446d2500b09270.json`](../../sessions/d3/d30f0c446d2500b09270.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

223 recorded events

### Tool call

_source line 1 · 2026-05-18T19:33:45.187205+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T19:33:45.187724+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:33:45.188009+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:33:45.188224+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:33:45.188411+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:33:45.188591+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T19:33:45.188811+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T19:33:45.189034+00:00_

docs/paper/corl_example.tex
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/median/paper.tex
artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
artifacts/dream_reports/dream_20260516T011810/best/paper.tex
artifacts/dream_reports/dream_20260516T011810/median/paper.tex
artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method_a6c062.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/introduction_fccb56.tex
docs/paper-a-plus-backup/abstract.tex
docs/paper-a-plus-backup/appendix.tex
docs/paper-a-plus-backup/conclusion.tex
docs/paper-a-plus-backup/corl_example.tex
docs/paper-a-plus-backup/discussion.tex
docs/paper-a-plus-backup/experiments.tex
docs/paper-a-plus-backup/introduction.tex
docs/paper-a-plus-backup/main.tex
docs/paper-a-plus-backup/method.tex
docs/paper-a-plus-backup/related_work.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T19:33:45.189235+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T19:33:45.190271+00:00_

Error: result (157,911 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T19:33:45.190604+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T19:33:45.190818+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T19:33:45.191097+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Numerical consistency check",
  "prompt": "You are checking numerical consistency between a paper's .tex files and an experiment registry.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Registry data location\nThe registry JSON is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed. Use jq or python to probe and extract.\n\n## Task\n1. Read ALL .tex files and extract every quantitative number: Cohen's d values, R² values, MSE, p-values, percentages, ratios, counts, etc. Note the file and line number for each.\n\n2. Extract relevant metrics from the registry. Use bash with jq or python to parse the registry file. The key metrics to find:\n   - Cohen's d: L1 instruction 24h ablation = 0.651, control 8h = 0.41\n   - Dose-response: d=0.482(top4) → 0.639(top32)\n   - Counterfactual: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n   - Attention decomposition: instruction-dominant 62.4% vs control 44.9%\n   - Per-dim MAE ratios: translation 3-5x, rotation 1.9-2.6x\n   - Per-task R²: L1 10/10 positive, L8 8/10, L13 5/10\n   - Per-head bootstrap: instruction d=0.027, control d=0.051, p=0.0018\n   - CV permutation: p=0.016\n   - Random subset ablation: dominant Δ=0.042, random mean Δ=0.077, z=-2.73, p=0.003\n   - Specificity control: bottom-24 d=0.565 vs top-24 d=0.65 (ratio 1.15)\n   - Trained probe peak: L9 R²=0.643, untrained peak L1 R²=0.547\n   - Linear probe: trained peak L13 R²=0.596, untrained peak L1 R²=0.492\n\n3. Cross-validate: for each number in the paper, check if it matches the registry. Report mismatches.\n\n## Output format\nReturn a markdown table:\n```\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n```\nStatus should be: ✅ 匹配, ❌ 不匹配, ⚠️ 未找到registry记录\n\nAlso return a summary count of matches, mismatches, and unverified numbers."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "tool_args": {
    "description": "Numerical consistency check",
    "prompt": "You are checking numerical consistency between a paper's .tex files and an experiment registry.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Registry data location\nThe registry JSON is at: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/mcp-agent-ml-research-read_registry-1779132458658.txt\n\nThe file is JSON with schema: {result: string}. The `result` field is itself a JSON string that needs to be parsed. Use jq or python to probe and extract.\n\n## Task\n1. Read ALL .tex files and extract every quantitative number: Cohen's d values, R² values, MSE, p-values, percentages, ratios, counts, etc. Note the file and line number for each.\n\n2. Extract relevant metrics from the registry. Use bash with jq or python to parse the registry file. The key metrics to find:\n   - Cohen's d: L1 instruction 24h ablation = 0.651, control 8h = 0.41\n   - Dose-response: d=0.482(top4) → 0.639(top32)\n   - Counterfactual: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625\n   - Attention decomposition: instruction-dominant 62.4% vs control 44.9%\n   - Per-dim MAE ratios: translation 3-5x, rotation 1.9-2.6x\n   - Per-task R²: L1 10/10 positive, L8 8/10, L13 5/10\n   - Per-head bootstrap: instruction d=0.027, control d=0.051, p=0.0018\n   - CV permutation: p=0.016\n   - Random subset ablation: dominant Δ=0.042, random mean Δ=0.077, z=-2.73, p=0.003\n   - Specificity control: bottom-24 d=0.565 vs top-24 d=0.65 (ratio 1.15)\n   - Trained probe peak: L9 R²=0.643, untrained peak L1 R²=0.547\n   - Linear probe: trained peak L13 R²=0.596, untrained peak L1 R²=0.492\n\n3. Cross-validate: for each number in the paper, check if it matches the registry. Report mismatches.\n\n## Output format\nReturn a markdown table:\n```\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n```\nStatus should be: ✅ 匹配, ❌ 不匹配, ⚠️ 未找到registry记录\n\nAlso return a summary count of matches, mismatches, and unverified numbers."
  }
}
````

</details>

---

### Tool call

_source line 14 · 2026-05-18T19:33:45.191482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T19:33:45.191692+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T19:33:45.191898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T19:33:45.192129+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T19:33:45.192353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T19:33:45.192564+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T19:33:45.192768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T19:33:45.192998+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T19:33:45.193218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T19:33:45.193493+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confir
…[truncated 9617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T19:33:45.193724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T19:33:45.193944+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraph
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T19:33:45.194163+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T19:33:45.194346+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T19:33:45.194540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T19:33:45.194905+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 38972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T19:33:45.195167+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T19:33:45.195359+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T19:33:45.195561+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(json.dumps(result, indent=2))\n\" 2>&1 | head -500",
  "description": "Parse registry JSON file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nprint(json.dumps(result, indent=2))\n\" 2>&1 | head -500",
    "description": "Parse registry JSON file"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T19:33:45.195894+00:00_

{
  "success": true,
  "data": {
    "experiments": {
      "specificity_control_action": {
        "status": "DONE",
        "retry_count": 0,
        "created_at": "2026-05-18T18:28:45.197Z",
        "updated_at": "2026-05-18T18:45:03.767Z",
        "hypothesis": "Bottom-24 non-instruction heads should cause significantly less action shift (d << 0.65) than top-24 instruction-dominant heads when ablated, confirming that instruction-action coupling is specific to identified heads rather than a general property of any 24 heads.",
        "parent": "action_trajectory_control",
        "spec": {
          "command": "source /root/miniconda3/bin/activate base && cd /root/vla-ssd && MUJOCO_GL=egl python -u scripts/specificity_control_action.py",
          "server": "westd-19183",
          "data_path": "/root/autodl-tmp/vla-ssd/data/libero/libero_goal",
          "data_count": 1500,
          "model_name": "openvla-7b",
          "seed": 42,
          "checkpoint_source": "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b",
          "eval_data": "libero_goal 3 tasks x 10 demos x 50 timesteps",
          "checkpoint_path": "N/A",
          "log_path": "/root/autodl-tmp/vla-ssd/results/specificity_control_action.log"
        },
        "conclusion": "negative",
        "notes": "Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.",
        "metrics": {
          "cohens_d": 0.565,
          "paired_mse": 0.034,
          "token_divergence": 0.598,
          "kl_divergence": 4.166,
          "top24_d": 0.65,
          "bottom24_d": 0.565,
          "ratio": 1.15,
          "per_task_d": {
            "cabinet": 0.405,
            "bowl": 0.628,
            "plate": 0.659
         
…[truncated 23926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T19:33:45.196174+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Wording consistency check",
  "prompt": "You are checking wording consistency in a paper that recently shifted its narrative from \"instruction-specific\" to \"graded distributed routing\".\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Task\nRead ALL .tex files and search for:\n\n### A. Problematic residual strong claims (mark each with file:line)\n1. \"uniquely responsible\"\n2. \"exclusively\"\n3. \"solely driven\"\n4. \"only instruction heads\"\n5. \"specific to instruction heads\" (check context - may be OK with qualifier)\n6. \"instruction-specific\" (in non-probe context, needs checking)\n7. Any wording that implies trajectory-level specificity has been confirmed\n8. Any other overly strong causal claims that don't fit \"graded distributed routing\"\n\n### B. AI writing style markers (mark each with file:line)\n1. \"—\" (em-dash, U+2014) - ALL instances must be flagged\n2. \" – \" (explanatory en-dash, U+2013, with spaces) - flag all except number ranges like \"2020–2024\"\n3. \"-ing,\" pattern (participial phrases ending sentences) - flag instances like \"..., demonstrating the...\" / \"..., highlighting the...\"\n4. Excessive \"Furthermore\" / \"Moreover\" / \"Additionally\" sequences\n5. \"It is worth noting\" / \"Notably, ...\"\n6. \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\"\n7. \"a myriad of\" / \"a plethora of\"\n\n### C. Confirm new narrative keywords exist\nSearch for presence of:\n1. \"graded\" or \"distributed\" (in routing/processing context)\n2. Qualifiers: \"primarily\", \"preferentially\", \"predominantly\", etc.\n\n## Output format\nReturn a markdown table for issues:\n```\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n```\n\nProblem types: \"残留强claim\", \"em-dash\", \"en-dash\", \"AI写作-ing\", \"AI写作过渡词\", \"AI写作用词\"\n\nAlso confirm which new narrative keywords were found and where.\n\nReturn a summary count of issues by type."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "tool_args": {
    "description": "Wording consistency check",
    "prompt": "You are checking wording consistency in a paper that recently shifted its narrative from \"instruction-specific\" to \"graded distributed routing\".\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\n## Task\nRead ALL .tex files and search for:\n\n### A. Problematic residual strong claims (mark each with file:line)\n1. \"uniquely responsible\"\n2. \"exclusively\"\n3. \"solely driven\"\n4. \"only instruction heads\"\n5. \"specific to instruction heads\" (check context - may be OK with qualifier)\n6. \"instruction-specific\" (in non-probe context, needs checking)\n7. Any wording that implies trajectory-level specificity has been confirmed\n8. Any other overly strong causal claims that don't fit \"graded distributed routing\"\n\n### B. AI writing style markers (mark each with file:line)\n1. \"—\" (em-dash, U+2014) - ALL instances must be flagged\n2. \" – \" (explanatory en-dash, U+2013, with spaces) - flag all except number ranges like \"2020–2024\"\n3. \"-ing,\" pattern (participial phrases ending sentences) - flag instances like \"..., demonstrating the...\" / \"..., highlighting the...\"\n4. Excessive \"Furthermore\" / \"Moreover\" / \"Additionally\" sequences\n5. \"It is worth noting\" / \"Notably, ...\"\n6. \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\"\n7. \"a myriad of\" / \"a plethora of\"\n\n### C. Confirm new narrative keywords exist\nSearch for presence of:\n1. \"graded\" or \"distributed\" (in routing/processing context)\n2. Qualifiers: \"primarily\", \"preferentially\", \"predominantly\", etc.\n\n## Output format\nReturn a markdown table for issues:\n```\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n```\n\nProblem types: \"残留强claim\", \"em-dash\", \"en-dash\", \"AI写作-ing\", \"AI写作过渡词\", \"AI写作用词\"\n\nAlso confirm which new narrative keywords were found and where.\n\nReturn a summary count of issues by type."
  }
}
````

</details>

---

### Tool call

_source line 35 · 2026-05-18T19:33:45.196560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print experiments with metrics\nfor name, exp in result.get('experiments', {}).items():\n    if 'metrics' in exp:\n        print(f'=== {name} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print()\n    elif 'notes' in exp:\n        print(f'=== {name} (notes only) ===')\n        print(exp.get('notes', ''))\n        print()\n\" 2>&1 | tail -300",
  "description": "Extract all metrics from registry experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print experiments with metrics\nfor name, exp in result.get('experiments', {}).items():\n    if 'metrics' in exp:\n        print(f'=== {name} ===')\n        print(json.dumps(exp.get('metrics', {}), indent=2))\n        print()\n    elif 'notes' in exp:\n        print(f'=== {name} (notes only) ===')\n        print(exp.get('notes', ''))\n        print()\n\" 2>&1 | tail -300",
    "description": "Extract all metrics from registry experiments"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T19:33:45.196793+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T19:33:45.197006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T19:33:45.197207+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T19:33:45.197433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T19:33:45.197646+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T19:33:45.197866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T19:33:45.198133+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T19:33:45.198376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T19:33:45.198639+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T19:33:45.198888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T19:33:45.199209+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confir
…[truncated 9617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T19:33:45.199466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T19:33:45.199688+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraph
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T19:33:45.199951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T19:33:45.200164+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T19:33:45.200383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T19:33:45.200594+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T19:33:45.200807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T19:33:45.201244+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 38972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T19:33:45.201536+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Cross-reference integrity check",
  "prompt": "You are checking cross-reference integrity in a LaTeX paper.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\nThe .bib file is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib\n\n## Task\n1. **Labels and refs**: \n   - Extract ALL \\label{...} from all .tex files (note file:line for each)\n   - Extract ALL \\ref{...}, \\eqref{...}, \\autoref{...}, \\cref{...}, \\Cref{...} from all .tex files\n   - Find orphan labels (defined but never referenced)\n   - Find dangling refs (referenced but never defined)\n\n2. **Citations**:\n   - Extract ALL \\cite{...}, \\citep{...}, \\citet{...}, \\citealp{...} etc. from all .tex files\n   - Extract ALL bib entry keys from references.bib\n   - Find missing citations (cited in tex but not in bib)\n   - Find unused bib entries (in bib but never cited) - just count these, don't list all\n\n3. **Other checks**:\n   - Check for duplicate labels\n   - Check for common issues like \\ref without preceding ~ (should be ~\\ref for non-breaking space)\n\n## Output format\nReturn:\n```\n## 交叉引用检查\n\n### 孤立 \\label (defined but never referenced)\n- file:line - \\label{xxx}\n...\n\n### 悬空 \\ref (referenced but never defined)\n- file:line - \\ref{xxx}\n...\n\n### 缺失 \\cite (cited but not in .bib)\n- file:line - \\cite{xxx}\n...\n\n### 未使用 bib 条目\nN entries in .bib are never cited.\n\n### 其他问题\n- duplicate labels, missing ~\\ref, etc.\n```\n\nReturn a summary count."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "tool_args": {
    "description": "Cross-reference integrity check",
    "prompt": "You are checking cross-reference integrity in a LaTeX paper.\n\n## Paper files location\nAll .tex files are in: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nFiles: main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, appendix.tex\n\nThe .bib file is: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib\n\n## Task\n1. **Labels and refs**: \n   - Extract ALL \\label{...} from all .tex files (note file:line for each)\n   - Extract ALL \\ref{...}, \\eqref{...}, \\autoref{...}, \\cref{...}, \\Cref{...} from all .tex files\n   - Find orphan labels (defined but never referenced)\n   - Find dangling refs (referenced but never defined)\n\n2. **Citations**:\n   - Extract ALL \\cite{...}, \\citep{...}, \\citet{...}, \\citealp{...} etc. from all .tex files\n   - Extract ALL bib entry keys from references.bib\n   - Find missing citations (cited in tex but not in bib)\n   - Find unused bib entries (in bib but never cited) - just count these, don't list all\n\n3. **Other checks**:\n   - Check for duplicate labels\n   - Check for common issues like \\ref without preceding ~ (should be ~\\ref for non-breaking space)\n\n## Output format\nReturn:\n```\n## 交叉引用检查\n\n### 孤立 \\label (defined but never referenced)\n- file:line - \\label{xxx}\n...\n\n### 悬空 \\ref (referenced but never defined)\n- file:line - \\ref{xxx}\n...\n\n### 缺失 \\cite (cited but not in .bib)\n- file:line - \\cite{xxx}\n...\n\n### 未使用 bib 条目\nN entries in .bib are never cited.\n\n### 其他问题\n- duplicate labels, missing ~\\ref, etc.\n```\n\nReturn a summary count."
  }
}
````

</details>

---

### Tool call

_source line 56 · 2026-05-18T19:33:45.201960+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print all experiment names and their metrics/notes\nfor name, exp in result.get('experiments', {}).items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    if metrics or notes:\n        print(f'--- {name} ---')\n        if metrics:\n            print('METRICS:', json.dumps(metrics, indent=2, default=str))\n        if notes:\n            print('NOTES:', notes)\n        print()\n\" 2>&1",
  "description": "Extract all experiment metrics and notes from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\n# Print all experiment names and their metrics/notes\nfor name, exp in result.get('experiments', {}).items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    if metrics or notes:\n        print(f'--- {name} ---')\n        if metrics:\n            print('METRICS:', json.dumps(metrics, indent=2, default=str))\n        if notes:\n            print('NOTES:', notes)\n        print()\n\" 2>&1",
    "description": "Extract all experiment metrics and notes from registry"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T19:33:45.202198+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-18T19:33:45.202398+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "uniquely responsible",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "uniquely responsible",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-18T19:33:45.202608+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-18T19:33:45.202810+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exclusively",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exclusively",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-18T19:33:45.203036+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-18T19:33:45.203233+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "solely driven",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "solely driven",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T19:33:45.203423+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T19:33:45.203612+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "only instruction heads",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "only instruction heads",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T19:33:45.203797+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T19:33:45.204003+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-18T19:33:45.204194+00:00_

docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-18T19:33:45.204397+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-18T19:33:45.204599+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-18T19:33:45.204789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-18T19:33:45.204978+00:00_

1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).
5	Second, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
6	Convergent causal evidence from seven independent analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation.
7	Third, under RSA and action probes, vision encoder representations show a middle-layer peak, but this pattern is metric-dependent (CKA diverges).
8	Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-18T19:33:45.205164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-18T19:33:45.205360+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, R
…[truncated 2206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-18T19:33:45.205570+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T19:33:45.205753+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "LaTeX compilation check",
  "prompt": "You are checking if a LaTeX paper compiles successfully.\n\n## Paper files location\nThe paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nMain file: main.tex\n\n## Task\n1. First, read main.tex to understand the document structure and what packages/files it includes.\n\n2. Check if there's a Makefile in the paper directory.\n\n3. Try to compile the paper locally. Try in this order:\n   a. `latexmk -pdf main.tex` (if latexmk is available)\n   b. `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n   c. If neither works, check what's available with `which latexmk pdflatex xelatex lualatex`\n\n4. If local compilation tools aren't available, check on the remote server:\n   - SSH command: `ssh connect.westd.seetacloud.com`\n   - The paper might also be at /root/vla-ssd/docs/paper/ on the server\n   - Check if LaTeX tools are available there\n\n5. Report ALL warnings and errors from compilation. Focus especially on:\n   - Undefined references\n   - Missing citations\n   - Missing packages\n   - Overfull/underfull hbox warnings (just count, don't list all)\n   - Any other errors\n\n## Output format\nReturn:\n```\n## 编译结果\n\n### 编译环境\n- Tool used: ...\n- Location: local / remote\n\n### Errors (N)\n- ...\n\n### Warnings (N)\n- Undefined references: N\n- Missing citations: N\n- Overfull hbox: N\n- Underfull hbox: N\n- Other: N\n\n### 详细 warning 列表\n(list non-trivial warnings)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "tool_args": {
    "description": "LaTeX compilation check",
    "prompt": "You are checking if a LaTeX paper compiles successfully.\n\n## Paper files location\nThe paper is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/\nMain file: main.tex\n\n## Task\n1. First, read main.tex to understand the document structure and what packages/files it includes.\n\n2. Check if there's a Makefile in the paper directory.\n\n3. Try to compile the paper locally. Try in this order:\n   a. `latexmk -pdf main.tex` (if latexmk is available)\n   b. `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`\n   c. If neither works, check what's available with `which latexmk pdflatex xelatex lualatex`\n\n4. If local compilation tools aren't available, check on the remote server:\n   - SSH command: `ssh connect.westd.seetacloud.com`\n   - The paper might also be at /root/vla-ssd/docs/paper/ on the server\n   - Check if LaTeX tools are available there\n\n5. Report ALL warnings and errors from compilation. Focus especially on:\n   - Undefined references\n   - Missing citations\n   - Missing packages\n   - Overfull/underfull hbox warnings (just count, don't list all)\n   - Any other errors\n\n## Output format\nReturn:\n```\n## 编译结果\n\n### 编译环境\n- Tool used: ...\n- Location: local / remote\n\n### Errors (N)\n- ...\n\n### Warnings (N)\n- Undefined references: N\n- Missing citations: N\n- Overfull hbox: N\n- Underfull hbox: N\n- Other: N\n\n### 详细 warning 列表\n(list non-trivial warnings)\n```"
  }
}
````

</details>

---

### Tool call

_source line 76 · 2026-05-18T19:33:45.205997+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "specific to instruction",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "specific to instruction",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-18T19:33:45.206221+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	We test this assumption at the representational level through per-layer, per-token-type decomposition.
8	
9	\paragraph{Mechanistic interpretability in transformers.}
10	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
11	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
12	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
13	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
14	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
15	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
16	Our Layer-1 attention head analysis ext
…[truncated 3052 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-18T19:33:45.206596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-18T19:33:45.206814+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\nkeys = list(result.keys())\nprint(\"Top-level keys:\", keys)\nfor k in keys:\n    v = result[k]\n    if isinstance(v, dict):\n        print(f\"\\n{k} has {len(v)} entries: {list(v.keys())[:20]}\")\n    else:\n        print(f\"\\n{k}: {type(v).__name__} = {str(v)[:200]}\")\nPYEOF",
  "description": "Inspect registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\ndata = json.loads(raw)\nresult_str = data['result']\nresult = json.loads(result_str)\nkeys = list(result.keys())\nprint(\"Top-level keys:\", keys)\nfor k in keys:\n    v = result[k]\n    if isinstance(v, dict):\n        print(f\"\\n{k} has {len(v)} entries: {list(v.keys())[:20]}\")\n    else:\n        print(f\"\\n{k}: {type(v).__name__} = {str(v)[:200]}\")\nPYEOF",
    "description": "Inspect registry structure"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T19:33:45.207022+00:00_

docs/paper/appendix.tex:87:To evaluate whether the ablation effect in \S\ref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacement).
docs/paper/appendix.tex:671:To test whether ablation effects are specific to instruction-dominant heads, we compare ablating the top-24 heads (highest instruction attention fraction, i.e., the instruction-dominant group) against the bottom-24 heads (lowest instruction attention fraction).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-18T19:33:45.207189+00:00_

Top-level keys: ['success', 'data', 'error', 'metadata']

success: bool = True

data has 4 entries: ['experiments', 'count', 'total', 'baseline']

error: NoneType = None

metadata has 1 entries: ['elapsed_seconds']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-18T19:33:45.207397+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}).
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24
…[truncated 3943 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T19:33:45.207616+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-18T19:33:45.207840+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations; all patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
13	
14	%------------------------------------------------------------------
15	\subsection{Framework Validation: Token-Level Specialization}
16	\label{sec:token_specialization}
17	
18	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
19	
20	\paragraph{Image tokens are instruction-blind (expected).}
21	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
22	Both linear and MLP probes confir
…[truncated 9617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T19:33:45.208075+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-18T19:33:45.208586+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "instruction-specific",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "instruction-specific",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-18T19:33:45.208764+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-18T19:33:45.208968+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "—",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-18T19:33:45.209172+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Convergent causal evidence from seven independent analyses supports a functional role for L1 instruction-dominant heads in instruction-conditioned action generation:
8	(1)~three-condition attention gradient ($0 \to 9 \to 24$ instruction-dominant heads);
9	(2)~$R^2$ ablation gradient confined to L1 ($+0.059$ at L1, $\approx 0$ at L13);
10	(3)~trajectory divergence under L1 ablation ($d = 0.65$, $72.3\%$ token divergence);
11	(4)~dose-response curve across 8 conditions ($d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response});
12	(5)~counterfactual instruction analysis across 4 perturbation types ($d = 0.63$--$0.97$; Table~\ref{tab:counterfactual});
13	(6)~per-head bootstrap CIs confirming coordinated routing ($p = 0.002$);
14	and~(7)~CV permutation test ($p = 0.016$).
15	
16	\paragraph{Mechanistic interpretation.}
17	The dose-response curve reveals a concentrated routing core with steep rise through 12 heads and diminishing returns beyond 20; individual control heads produce stronger effects than instruction heads ($d = 0.051$ vs.\ $0.027$), yet 24 instruction heads collectively generate a larger perturbation ($d = 0.65$ vs.\ $0.41$).
18	Bottom-24 head ablation produces comparable but lower disruption ($d = 0.57$ vs.\ $0.65$; Table~\ref{tab:specificity_control}); instruction-attention fraction predicts contribution magnitude, with stronger token-level specificity (KL ratio $1.56\times$) compressed by the 7-D action bottleneck.
19	The counterfactual ordering (empty $>$ wrong $>$ paraph
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-18T19:33:45.209401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-18T19:33:45.209763+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
5	Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
6	The framework generalizes to any decoder-only VLA with a frozen vision encoder; multi-model validation and closed-loop evaluation are natural next steps.
7	Code and representations will be released upon acceptance.
8	
9	\paragraph{Use of Generative AI.}
10	Generative AI tools (Claude, GPT-4) assisted with code implementation and manuscript editing; all scientific content was produced by the authors.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T19:33:45.209959+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-18T19:33:45.210150+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": " – ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-18T19:33:45.210339+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-18T19:33:45.210523+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T19:33:45.210696+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-18T19:33:45.210974+00:00_

1	% === VLA / Architecture ===
2	
3	@article{kim2024_openvla,
4	  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},
5	  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},
6	  journal   = {arXiv preprint arXiv:2406.09246},
7	  year      = {2024},
8	}
9	
10	@article{karamcheti2024,
11	  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},
12	  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},
13	  journal   = {arXiv preprint arXiv:2402.07865},
14	  year      = {2024},
15	}
16	
17	@article{brohan2023_rt2,
18	  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
19	  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
20	  journal   = {arXiv preprint arXiv:2307.15818},
21	  year      = {2023},
22	}
23	
24	% === Benchmark ===
25	
26	@inproceedings{liu2023_libero,
27	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
28	  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
29	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
30	  year      = {2023},
31	}
32	
33	% === Representation Analysis Methods ===
34	
35	@article{kriegeskorte2008,
36	  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},
37	  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Ban
…[truncated 16770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-18T19:33:45.211391+00:00_

1	\appendix
2	
3	\section{Supplementary Material}
4	\label{sec:appendix}
5	
6	\subsection{CKA Analysis Method}
7	\label{sec:cka_appendix}
8	
9	We employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA as a complementary perspective.
10	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
11	
12	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
13	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
14	
15	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
16	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality.
17	
18	\subsection{Metric Sensitivity: RSA versus CKA}
19	\label{sec:metric_sensitivity_appendix}
20	
21	Linear CKA~\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\ref{fig:metric_comparison}).
22	RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).
23	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties.
24	
25	At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
26	RSA captures ran
…[truncated 38972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T19:33:45.211626+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing,",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing,",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-18T19:33:45.211812+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-18T19:33:45.212007+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-18T19:33:45.212197+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "Makefile",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "Makefile",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-18T19:33:45.212376+00:00_

docs/paper/main.bbl:9:  Choromanski, Ding, Driess, Dubey, Finn, et~al.]{brohan2023_rt2}
docs/paper/main.bbl:11:  T.~Ding, D.~Driess, A.~Dubey, C.~Finn, et~al.
docs/paper/main.bbl:31:\bibitem[H{\"a}on et~al.(2025)H{\"a}on, Stocking, Chuang, and Tomlin]{haon2025}
docs/paper/main.bbl:32:B.~H{\"a}on, K.~C. Stocking, I.~Chuang, and C.~J. Tomlin.
docs/paper/main.bbl:87:  Nair, Pertsch, Shi, Tanner, Vuong, Walling, Wang, and
docs/paper/main.bbl:92:  A.~Walling, H.~Wang, and U.~Zhilinsky.
docs/paper/main.bbl:148:\bibitem[Bills et~al.(2023)Bills, Cammarata, Mossing, Tillman, Gao, Goh,
docs/paper/main.bbl:150:S.~Bills, N.~Cammarata, D.~Mossing, H.~Tillman, L.~Gao, G.~Goh, I.~Sutskever,
docs/paper/main.bbl:181:  lifting, the rest can be pruned.
docs/paper/appendix.tex:199:A potential concern with the three-condition comparison (\S\ref{sec:model_data}) is that the pretrained Llama-2 backbone never encountered projected visual tokens during pretraining, so its representations of such input could be degenerate.
docs/paper/appendix.tex:204:These diagnostics indicate that the pretrained LLM produces structured, full-rank representations of visual input despite never encountering projected visual tokens during pretraining, supporting the validity of the three-condition comparison.
docs/paper/introduction.tex:6:Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
docs/paper/references.bib:19:  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
docs/paper/references.bib:93:  author    = {H{\"a}on, Bear and Stocking, Kaylene C. and Chuang, Ian and Tomlin, Claire J.},
docs/paper/references.bib:207:  author    = {Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D.},
docs/paper/references.bib
…[truncated 1681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-18T19:33:45.212568+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-18T19:33:45.212742+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Furthermore|Moreover|Additionally",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Furthermore|Moreover|Additionally",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-18T19:33:45.212937+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-18T19:33:45.213114+00:00_

docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discussion.tex
docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-18T19:33:45.213287+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-18T19:33:45.213464+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-18T19:33:45.213618+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-18T19:33:45.213788+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "It is worth noting|Notably",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "It is worth noting|Notably",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T19:33:45.213974+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T19:33:45.214178+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\nouter = json.loads(raw)\nresult = json.loads(outer['result'])\ndata = result['data']\n\n# Print all experiments with their metrics and notes\nfor name, exp in data['experiments'].items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    print(f'=== {name} ===')\n    if metrics:\n        print('METRICS:', json.dumps(metrics, indent=2, default=str))\n    if notes:\n        print('NOTES:', notes)\n    print()\nPYEOF",
  "description": "Extract all experiment data from nested registry JSON"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results && python3 << 'PYEOF'\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779132458658.txt') as f:\n    raw = f.read()\nouter = json.loads(raw)\nresult = json.loads(outer['result'])\ndata = result['data']\n\n# Print all experiments with their metrics and notes\nfor name, exp in data['experiments'].items():\n    metrics = exp.get('metrics', {})\n    notes = exp.get('notes', '')\n    print(f'=== {name} ===')\n    if metrics:\n        print('METRICS:', json.dumps(metrics, indent=2, default=str))\n    if notes:\n        print('NOTES:', notes)\n    print()\nPYEOF",
    "description": "Extract all experiment data from nested registry JSON"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-18T19:33:45.214391+00:00_

&lt;persisted-output>
Output too large (53.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt

Preview (first 2KB):
=== specificity_control_action ===
METRICS: {
  "cohens_d": 0.565,
  "paired_mse": 0.034,
  "token_divergence": 0.598,
  "kl_divergence": 4.166,
  "top24_d": 0.65,
  "bottom24_d": 0.565,
  "ratio": 1.15,
  "per_task_d": {
    "cabinet": 0.405,
    "bowl": 0.628,
    "plate": 0.659
  }
}
NOTES: Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.

=== counterfactual_instruction ===
NOTES: 4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim.

=== attention_decomposition ===
NOTES: B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json

=== action_metrics_extended ===
...
&lt;/persisted-output>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-18T19:33:45.214641+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "delve|leverage|utilize|facilitate",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "delve|leverage|utilize|facilitate",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-18T19:33:45.214846+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-18T19:33:45.215078+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "a myriad of|a plethora of",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "a myriad of|a plethora of",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-18T19:33:45.215273+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-18T19:33:45.215474+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "graded|distributed",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "graded|distributed",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-18T19:33:45.215687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/2e136dbf-061a-4249-b788-cde9bf2a0739/tool-results/bgt1o9lo8.txt"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-18T19:33:45.216419+00:00_

1	=== specificity_control_action ===
2	METRICS: {
3	  "cohens_d": 0.565,
4	  "paired_mse": 0.034,
5	  "token_divergence": 0.598,
6	  "kl_divergence": 4.166,
7	  "top24_d": 0.65,
8	  "bottom24_d": 0.565,
9	  "ratio": 1.15,
10	  "per_task_d": {
11	    "cabinet": 0.405,
12	    "bowl": 0.628,
13	    "plate": 0.659
14	  }
15	}
16	NOTES: Bottom-24 d=0.565 vs Top-24 d=0.65 (ratio 1.15). Specificity NOT confirmed: ablating non-instruction heads causes nearly as much action shift as instruction heads. Per-task: cabinet d=0.405, bowl d=0.628, plate d=0.659. Only cabinet shows clear specificity gap. Control-8 d=0.41 for reference. Paired MSE=0.034 (p=1.86e-92), token_div=0.598, KL=4.166.
17	
18	=== counterfactual_instruction ===
19	NOTES: 4 counterfactual conditions vs correct baseline. Cohen's d: empty=0.968, wrong=0.844, paraphrased=0.697, shuffled=0.625. All d>0.5. Graduated response confirms instruction content sensitivity. Surprise: paraphrased > shuffled (model depends on surface form, not just semantics). Supports C2 claim.
20	
21	=== attention_decomposition ===
22	NOTES: B2: Instruction-dominant heads allocate 62.4% attention to instruction tokens vs 44.9% for control heads (+17.5pp delta). Training shifts attention from vision to instruction for both groups (instr-dom: 11.5%->62.4%, control: 12.3%->44.9%), but the shift is larger for instruction-dominant heads (+50.9pp vs +32.6pp). B3: Per-task R2 shows consistent ablation effect at L1 (10/10 tasks positive, mean delta +0.0586) that vanishes by L13 (5/10 positive, mean delta -0.0002). Task variability is substantial (CV=0.22 at L1). Results saved: attention_decomposition.json and per_task_r2_distribution.json
23	
24	=== action_metrics_extended ===
25	NOTES: Per-dim MAE extracted from existing JSONs. Instruction 24h causes 1.9-5.1x larger shifts than control 8h. Translation dims most affected (dx=5.1x, dy=4.3x, dz=3.1x), rotation moderate (roll=2.6x, pitch=2.2x, yaw=1.9x), gripper=2.1x. Cosine similarity NOT computable
…[truncated 60976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-18T19:33:45.216698+00:00_

docs/paper/appendix.tex:219:Untrained deep layers collapse entirely under the linear probe (L25: $R^2 = -0.298$); MLP nonlinearity partially rescues these degraded representations.
docs/paper/appendix.tex:676:\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times$, KL ratio $1.56\times$), consistent with graded, attention-ordered contribution to routing.}
docs/paper/main.aux:310:\@writefile{lot}{\contentsline {table}{\numberline {21}{\ignorespaces Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times $, KL ratio $1.56\times $), consistent with graded, attention-ordered contribution to routing.}}{26}{table.21}\protected@file@percent }
docs/paper/main.aux:311:\newlabel{tab:specificity_control}{{21}{26}{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom-24 L1 heads (ranked by instruction attention fraction). Top-24 produces disproportionately larger effects ($d$ ratio $1.15\times $, KL ratio $1.56\times $), consistent with graded, attention-ordered contribution to routing}{table.21}{}}
docs/paper/corlabbrvnat.bst:17:%% This program can be redistributed and/or modified under the terms
docs/paper/method.tex:4:We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-18T19:33:45.216943+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.sty",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.sty",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-18T19:33:45.217168+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "primarily|preferentially|predominantly",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "primarily|preferentially|predominantly",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T19:33:45.217368+00:00_

docs/paper/conclusion.tex:4:We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
docs/paper/appendix.tex:432:This asymmetry confirms that training primarily reshapes how the readout token integrates information rather than altering the visual representations carried by image tokens.
docs/paper/introduction.tex:23:[Omitted long matching line]
docs/paper/discussion.tex:5:VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-18T19:33:45.217573+00:00_

docs/paper/corl_2026.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-18T19:33:45.217765+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which latexmk pdflatex xelatex lualatex bibtex 2>&1",
  "description": "Check available LaTeX tools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "which latexmk pdflatex xelatex lualatex bibtex 2>&1",
    "description": "Check available LaTeX tools"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T19:33:45.217977+00:00_

Exit code 1
/usr/bin/latexmk
/usr/bin/pdflatex
/usr/bin/lualatex
/usr/bin/bibtex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-18T19:33:45.218189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/corl_example.tex"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-18T19:33:45.218429+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Use this for the initial submission.
4	% \usepackage[final]{corl_2026} % Uncomment for the camera-ready ``final'' version.
5	% \usepackage[preprint]{corl_2026} % Uncomment for pre-prints (e.g., arxiv); This is like ``final'', but will remove the CORL footnote.
6	
7	\title{Formatting Instructions for CoRL 2026 Camera-Ready}
8	
9	% The \author macro works with any number of authors. There are two
10	% commands used to separate the names and addresses of multiple
11	% authors: \And and \AND.
12	%
13	% Using \And between authors leaves it to LaTeX to determine where to
14	% break the lines. Using \AND forces a line break at that point. So,
15	% if LaTeX puts 3 of 4 authors names on the first line, and the last
16	% on the second line, try using \AND instead of \And before the third
17	% author name.
18	
19	% NOTE: authors will be visible only in the camera-ready and preprint versions (i.e., when using the option 'final' or 'preprint'). 
20	% 	For the initial submission the authors will be anonymized.
21	
22	\author{
23	  Jane E.~Doe\\
24	  Department of Electrical Engineering and Computer Sciences\\
25	  University of California Berkeley 
26	  United States\\
27	  \texttt{janedoe@berkeley.edu} \\
28	  %% examples of more authors
29	  %% \And
30	  %% Coauthor \\
31	  %% Affiliation \\
32	  %% Address \\
33	  %% \texttt{email} \\
34	  %% \AND
35	  %% Coauthor \\
36	  %% Affiliation \\
37	  %% Address \\
38	  %% \texttt{email} \\
39	  %% \And
40	  %% Coauthor \\
41	  %% Affiliation \\
42	  %% Address \\
43	  %% \texttt{email} \\
44	  %% \And
45	  %% Coauthor \\
46	  %% Affiliation \\
47	  %% Address \\
48	  %% \texttt{email} \\
49	}
50	
51	
52	\begin{document}
53	\maketitle
54	
55	%===============================================================================
56	
57	\begin{abstract}
58	    The purpose of this document is to provide both the basic paper template and submission guidelines. Abstracts should be a single 
…[truncated 6129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-18T19:33:45.218694+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1",
  "description": "Compile LaTeX paper with latexmk",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1",
    "description": "Compile LaTeX paper with latexmk",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-18T19:33:45.218914+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "exclusive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "exclusive",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-18T19:33:45.219123+00:00_

docs/paper/related_work.tex:29:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-18T19:33:45.219373+00:00_

Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  introduction.tex
Category 'changed_user':
  introduction.tex

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -recorder  "main.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo)) (./corl_2026.sty
(/usr/share/texlive/texmf-dist/tex/latex/lineno/lineno.sty
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/graphics/color.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/
…[truncated 9715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-18T19:33:45.219610+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "sole ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "sole ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-18T19:33:45.219819+00:00_

docs/paper/related_work.tex:25:Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
docs/paper/experiments.tex:26:The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
docs/paper/abstract.tex:4:First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-18T19:33:45.220051+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "only.*responsible|responsible.*only",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "only.*responsible|responsible.*only",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-18T19:33:45.220236+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-18T19:33:45.220433+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "trajectory.level specificity|trajectory specificity",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "trajectory.level specificity|trajectory specificity",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-18T19:33:45.220633+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n '\\\\label{' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\label definitions from tex files with line numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n '\\\\label{' \"$f\" 2>/dev/null; done",
    "description": "Extract all \\label definitions from tex files with line numbers"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-18T19:33:45.220822+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-18T19:33:45.221043+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing\\.",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-18T19:33:45.221255+00:00_

=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
2:\label{sec:introduction}
=== related_work.tex ===
1:\section{Related Work}\label{sec:related_work}
=== method.tex ===
2:\label{sec:method}
8:\label{sec:model_data}
17:\label{sec:repr_extraction}
31:\label{sec:cross_instruction_probes}
39:\label{sec:attention_analysis}
46:\label{sec:rsa}
55:\label{sec:probes}
=== experiments.tex ===
2:\label{sec:experiments}
5:\label{sec:setup}
16:\label{sec:token_specialization}
31:\label{tab:dense_routing_main}
49:\label{sec:learned_routing}
85:\label{tab:routing_gradient}
102:\label{fig:attention_profile}
107:\label{sec:nonmonotonic}
126:\label{tab:rsa_overview}
150:\label{fig:layer_curves}
=== discussion.tex ===
2:\label{sec:discussion}
=== conclusion.tex ===
2:\label{sec:conclusion}
=== appendix.tex ===
4:\label{sec:appendix}
7:\label{sec:cka_appendix}
19:\label{sec:metric_sensitivity_appendix}
33:\label{fig:metric_comparison}
37:\label{sec:branch_split_appendix}
45:\label{sec:rsa_bar_appendix}
53:\label{fig:rsa_bar}
57:\label{sec:rsa_perlayer_appendix}
63:\label{fig:rsa_perlayer_curve}
67:\label{sec:action_r2_threecond}
81:\label{fig:action_r2_threecond}
85:\label{sec:random_subset_ablation}
95:\label{fig:random_subset_ablation}
99:\label{sec:action_trajectory}
115:\label{tab:perhead_bootstrap}
138:\label{fig:dose_response}
144:\label{tab:dose_response}
165:\label{tab:counterfactual}
184:\label{tab:action_shift_perdim}
197:\label{sec:ood_diagnostics}
210:\label{fig:ood_diagnostics}
214:\label{sec:linear_probe}
227:\label{fig:linear_vs_mlp}
231:\label{sec:probe_bars_appendix}
239:\label{fig:probe_bars}
243:\label{sec:instruction_invariance_appendix}
252:\label{fig:factorial}
256:\label{sec:additional_rsa}
262:\label{sec:cross_benchmark_appendix}
279:\label{fig:cross_benchmark}
283:\label{sec:spatial_cross_instruction}
292:\label{tab:spatial_cross_instruction}
307:\label{sec:robustness_appendix}
310:\label{sec:metric_invariance}
317:\label{tab:metric_invariance}
332
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-18T19:33:45.221503+00:00_

docs/paper/related_work.tex:16:Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:114:\caption{Per-head bootstrap analysis of L1 ablation effects. Instruction heads are individually weaker but collectively stronger, consistent with coordinated routing.}
docs/paper/appendix.tex:267:The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
docs/paper/appendix.tex:273:This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.
docs/paper/appendix.tex:550:\caption{Instruction-dominant heads and text attention fraction at four sampled layers (subset of the 32-layer profile in Figure~\ref{fig:attention_profile}). VLA-trained shows entry-exit concentration (L1, L31); Llama-2 base peaks at mid-depth (L16); untrained shows no instruction routing. Head counts from the 32-layer bulk extraction may differ slightly from dedicated per-layer analyses (Table~\ref{tab:routing_gradient}) due to threshold boundary effects.}
docs/paper/appendix.tex:676:\caption{Specificity control: trajectory disruption from ablating top-24 vs.\ bottom
…[truncated 223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-18T19:33:45.221738+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\ref, \\eqref, \\autoref, \\cref, \\Cref from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
    "description": "Extract all \\ref, \\eqref, \\autoref, \\cref, \\Cref from tex files"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-18T19:33:45.221978+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (demonstrating|highlighting|showcasing|indicating|suggesting|confirming|showing|revealing|establishing|underscoring)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (demonstrating|highlighting|showcasing|indicating|suggesting|confirming|showing|revealing|establishing|underscoring)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-18T19:33:45.222203+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"^!\" main.log",
  "description": "Count errors in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"^!\" main.log",
    "description": "Count errors in log"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-18T19:33:45.222418+00:00_

docs/paper/related_work.tex:29:We extend this to VLAs, showing that image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
docs/paper/conclusion.tex:4:We present a systematic framework for token-level analysis of VLA representations, revealing that VLA fine-tuning primarily reorganizes instruction routing from mid-depth to entry-exit rather than reshaping visual geometry.
docs/paper/discussion.tex:20:The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
docs/paper/appendix.tex:25:At the per-layer level, linear CKA between image\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.
docs/paper/appendix.tex:47:Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:110:The 24 instruction heads nonetheless produce a larger aggregate perturbation ($d = 0.65$ vs.\ $0.41$), confirming collective coordination rather than individual strength.
docs/paper/appendix.tex:238:\caption{Functional probe $R^2$ for action prediction (best layer per source). Trained readout ($R^2{=}0.678$, L13) and trained image\_mean ($0.655$, L8) exceed the projector baseline ($0.630$), confirming the inverted-U extends to functional capacity.}
docs/paper/appendix.tex:246:Instruction invariance holds across all conditions: maximum $|\Delta| < 0.006$, confirming that action geometry is visually grounded and not modulated by language instructions.
docs/paper/appendix.tex:251:\caption{\textbf{(a)}~Trained vs.\ untrained image\_mean RSA profiles. Traini
…[truncated 2231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-18T19:33:45.222975+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-18T19:33:45.223215+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "the primary",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "the primary",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-18T19:33:45.223427+00:00_

=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
20:\ref{sec:cka_appendix}
=== related_work.tex ===
=== method.tex ===
64:\ref{sec:cka_appendix}
64:\ref{sec:nonmonotonic}
=== experiments.tex ===
8:\ref{sec:repr_extraction}
9:\ref{sec:model_data}
10:\ref{sec:rsa}
11:\ref{sec:probes}
12:\ref{sec:linear_probe}
18:\ref{sec:cross_instruction_probes}
21:\ref{tab:dense_routing_main}
22:\ref{sec:instruction_invariance_appendix}
25:\ref{sec:loocv}
26:\ref{sec:qa_probe}
26:\ref{sec:cross_benchmark_appendix}
30:\ref{sec:dense_routing}
52:\ref{tab:routing_gradient}
52:\ref{fig:attention_profile}
55:\ref{fig:attention_profile}
57:\ref{sec:threshold_sensitivity}
60:\ref{fig:probe_conditions_appendix}
61:\ref{sec:training_effect_summary}
61:\ref{sec:action_r2_threecond}
65:\ref{tab:rsa_overview}
66:\ref{sec:random_subset_ablation}
68:\ref{sec:repr_extraction}
68:\ref{tab:per_task_r2}
71:\ref{tab:attention_decomp}
71:\ref{tab:per_dim_mae}
71:\ref{sec:action_trajectory}
74:\ref{fig:dose_response}
74:\ref{sec:action_trajectory}
78:\ref{tab:counterfactual}
80:\ref{sec:action_trajectory}
84:\ref{tab:dense_routing_main}
101:\ref{fig:probe_conditions_appendix}
110:\ref{tab:rsa_overview}
111:\ref{sec:cka_appendix}
114:\ref{fig:layer_curves}
114:\ref{sec:seed_sensitivity}
115:\ref{tab:rsa_overview}
116:\ref{sec:cka_appendix}
119:\ref{tab:training_effects}
121:\ref{sec:cross_benchmark_appendix}
125:\ref{sec:cka_appendix}
141:\ref{sec:seed_sensitivity}
=== discussion.tex ===
11:\ref{fig:dose_response}
12:\ref{tab:counterfactual}
18:\ref{tab:specificity_control}
28:\ref{sec:ood_diagnostics}
28:\ref{sec:cka_appendix}
=== conclusion.tex ===
=== appendix.tex ===
21:\ref{fig:metric_comparison}
47:\ref{fig:rsa_bar}
47:\ref{tab:rsa_overview}
69:\ref{fig:action_r2_threecond}
87:\ref{sec:learned_routing}
101:\ref{tab:action_shift_perdim}
108:\ref{tab:perhead_bootstrap}
131:\ref{tab:dose_response}
131:\ref{fig:dose_response}
199:\ref{sec:model_data}
233:\ref{fig:probe_bars}
245:\ref{fig:
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-18T19:33:45.223661+00:00_

docs/paper/conclusion.tex:5:Convergent causal evidence from seven independent analyses supports L1 as the primary routing hub.
docs/paper/abstract.tex:8:Training effects concentrate at the readout token (probe $R^2$ $+0.069$, instruction attention $+46$pp) rather than visual geometry ($\Delta\rho \leq 0.017$, non-significant); instruction routing reorganization is the primary learned contribution of fine-tuning in the model studied.
docs/paper/introduction.tex:21:Training yields non-significant geometric gain ($\Delta\rho = 0.017$, $3\%$) but substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$), consistent with routing reorganization as the primary learned contribution.
docs/paper/introduction.tex:23:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-18T19:33:45.223871+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"undefined\" main.log 2>&1",
  "description": "Check undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"undefined\" main.log 2>&1",
    "description": "Check undefined references"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-18T19:33:45.224334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
  "description": "Extract all \\cite variants from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do echo \"=== $f ===\" && grep -n -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null; done",
    "description": "Extract all \\cite variants from tex files"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-18T19:33:45.224530+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-18T19:33:45.224731+00:00_

=== main.tex ===
=== abstract.tex ===
=== introduction.tex ===
5:\cite{brohan2023_rt2,kim2024_openvla}
8:\cite{grant2026}
8:\cite{haon2025}
12:\cite{kim2024_openvla,karamcheti2024}
12:\cite{zhai2023_siglip,oquab2024_dinov2}
12:\cite{touvron2023_llama2}
13:\cite{oquab2024_dinov2}
13:\cite{radford2021_clip}
14:\cite{kriegeskorte2008}
14:\cite{alain2017}
=== related_work.tex ===
4:\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}
11:\cite{elhage2021}
12:\cite{olsson2022}
13:\cite{wang2023_ioi}
13:\cite{conmy2023}
14:\cite{meng2022_rome}
14:\cite{belrose2023_tunedlens}
14:\cite{bills2023language,templeton2024scaling}
15:\cite{clark2019}
15:\cite{vig2019}
15:\cite{voita2019}
19:\cite{grant2026,hou2026,fei2025}
20:\cite{haon2025}
21:\cite{swann2026,buurmeijer2026}
21:\cite{lu2025,molinari2025}
22:\cite{fang2025}
24:\cite{grant2026}
28:\cite{dosovitskiy2021}
28:\cite{darcet2024}
28:\cite{geva2021}
28:\cite{tenney2019}
28:\cite{nostalgebraist2020}
28:\cite{neo2025}
32:\cite{kriegeskorte2008}
32:\cite{raghu2017}
32:\cite{morcos2018}
32:\cite{kornblith2019}
32:\cite{raghu2021}
33:\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022}
=== method.tex ===
10:\cite{kim2024_openvla,karamcheti2024}
10:\cite{zhai2023_siglip,oquab2024_dinov2}
10:\cite{touvron2023_llama2}
11:\cite{padalkar2023_oxe}
11:\cite{liu2023_libero}
23:\cite{oquab2024_dinov2}
24:\cite{radford2021_clip}
48:\cite{kriegeskorte2008}
51:\cite{nili2014toolbox}
58:\cite{alain2017}
63:\cite{kornblith2019}
=== experiments.tex ===
7:\cite{kim2024_openvla,karamcheti2024}
7:\cite{liu2023_libero}
8:\cite{oquab2024_dinov2}
8:\cite{radford2021_clip}
=== discussion.tex ===
6:\cite{grant2026}
28:\cite{brohan2023_rt2,black2024_pi0}
=== conclusion.tex ===
=== appendix.tex ===
9:\cite{kornblith2019}
21:\cite{kornblith2019}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-18T19:33:45.224971+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"missing\" main.log 2>&1",
  "description": "Check missing citations/files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -i \"missing\" main.log 2>&1",
    "description": "Check missing citations/files"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-18T19:33:45.225166+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-18T19:33:45.225351+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Overfull\" main.log",
  "description": "Count overfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Overfull\" main.log",
    "description": "Count overfull warnings"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-18T19:33:45.225539+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-18T19:33:45.225723+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull\" main.log",
  "description": "Count underfull warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull\" main.log",
    "description": "Count underfull warnings"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-18T19:33:45.225895+00:00_

10

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-18T19:33:45.226130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Warning\" main.log",
  "description": "Count all warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Warning\" main.log",
    "description": "Count all warnings"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-18T19:33:45.226332+00:00_

20

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-18T19:33:45.226541+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": ", (confirming|indicating|suggesting|consistent with) ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": ", (confirming|indicating|suggesting|consistent with) ",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-18T19:33:45.226756+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Warning\" main.log | sort | uniq -c | sort -rn",
  "description": "Categorize warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Warning\" main.log | sort | uniq -c | sort -rn",
    "description": "Categorize warnings"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-18T19:33:45.227004+00:00_

docs/paper/experiments.tex:80:L1 ablation ($d = 0.65$) falls between shuffled and paraphrased, consistent with removal of instruction signal rather than injection of noise (Appendix~\ref{sec:action_trajectory}).
docs/paper/discussion.tex:19:The counterfactual ordering (empty $>$ wrong $>$ paraphrased $>$ shuffled) follows semantic distance, with L1 ablation falling between shuffled and paraphrased, consistent with signal removal rather than noise injection.
docs/paper/discussion.tex:20:The non-trivial paraphrasing effect ($d = 0.70$) likely reflects sensitivity to exact token sequences; shuffled instructions ($d = 0.63$) produce less disruption, suggesting partial recovery from preserved vocabulary.
docs/paper/appendix.tex:47:Figure~\ref{fig:rsa_bar} shows RSA with the action space across all representation sources, confirming the ordering reported in Table~\ref{tab:rsa_overview}.
docs/paper/appendix.tex:62:\caption{Per-layer RSA ($\rho$) for trained and untrained models at image\_mean and readout (last\_preaction) positions. The trained model shows an inverted-U peaking at L12 for both positions; the untrained model shows monotonic decline. After L12, readout and image\_mean diverge: readout $\rho$ declines gradually ($0.628 \to 0.584$) while image\_mean $\rho$ drops sharply ($0.628 \to 0.422$), consistent with task-specific conditioning at the readout position.}
docs/paper/appendix.tex:71:The trained model peaks at L9 ($R^2 = 0.643 \pm 0.014$), consistent with progressive specialization for action-relevant feature integration.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:94:\caption{$R^2$ increase from ablating 24/32 L1 heads. Gray bars: 10 random subsets; red line: dominant-24 heads ($+0.042$). Random subsets yield larger gains (mean $+0.077 \pm 0.013$; $z = -2.73$, $p = 0.003$), consistent with routing-first specializati
…[truncated 5264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-18T19:33:45.229215+00:00_

     17 LaTeX Warning: `h' float specifier changed to `ht'.
      3 Package hyperref Warning: Token not allowed in a PDF string (Unicode):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-18T19:33:45.229460+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Overfull\" main.log",
  "description": "List overfull details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Overfull\" main.log",
    "description": "List overfull details"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-18T19:33:45.229657+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-18T19:33:45.229868+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ing\\.\\s*$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ing\\.\\s*$",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-18T19:33:45.230153+00:00_

docs/paper/related_work.tex:16:Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
docs/paper/appendix.tex:72:Llama-2 base shows a steady decline (L0: $0.645 \to$ L32: $0.551$, std $0.003$--$0.035$), indicating stable but unspecialized processing.
docs/paper/appendix.tex:267:The inverted-U profile replicates on LIBERO-Spatial: trained image\_mean RSA peaks at L14 ($\rho = 0.691$) and $R^2$ at L13 ($0.696$), with peaks shifting ${\sim}2$ layers deeper than LIBERO-Goal (RSA L12, $R^2$ L8--L10), consistent with increased task difficulty requiring deeper processing.
docs/paper/appendix.tex:273:This suggests that peak convergence is benchmark-specific rather than a general consequence of training.
docs/paper/appendix.tex:461:Both pretrained and VLA-trained models sustain $100\%$ through L31; only random initialization shows progressive decay ($82\%$ at L31), indicating that deep-layer stability derives from structured pretrained weights rather than task-specific fine-tuning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-18T19:33:45.230390+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL LABELS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed \"s/\\\\\\\\label{//;s/}//\" | while read lbl; do echo \"$lbl\"; done; done | sort -u",
  "description": "Extract all unique label keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL LABELS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed \"s/\\\\\\\\label{//;s/}//\" | while read lbl; do echo \"$lbl\"; done; done | sort -u",
    "description": "Extract all unique label keys"
  }
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-18T19:33:45.231377+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "the sole|the only",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "tool_args": {
    "pattern": "the sole|the only",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-18T19:33:45.231574+00:00_

docs/paper/related_work.tex:25:Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
docs/paper/experiments.tex:26:The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
docs/paper/abstract.tex:4:First, our framework validates architecture-expected token specialization: image tokens are instruction-blind while the readout token serves as the sole multimodal convergence point ($100\%$ instruction classification from L1, cross-validated).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-18T19:33:45.231767+00:00_

=== ALL LABELS ===
fig:action_r2_threecond
fig:attention_appendix
fig:attention_profile
fig:cross_benchmark
fig:dose_response
fig:factorial
fig:layer_curves
fig:linear_vs_mlp
fig:metric_comparison
fig:multilayer_attention
fig:ood_diagnostics
fig:probe_bars
fig:probe_conditions_appendix
fig:random_subset_ablation
fig:rsa_bar
fig:rsa_perlayer_curve
sec:action_r2_threecond
sec:action_trajectory
sec:additional_rsa
sec:appendix
sec:attention_analysis
sec:attention_decomp
sec:attention_pattern
sec:branch_split_appendix
sec:cka_appendix
sec:conclusion
sec:cross_benchmark_appendix
sec:cross_instruction_probes
sec:demo_sensitivity
sec:dense_routing
sec:discussion
sec:experiments
sec:instruction_invariance_appendix
sec:introduction
sec:learned_routing
sec:linear_probe
sec:loocv
sec:method
sec:metric_invariance
sec:metric_sensitivity_appendix
sec:model_data
sec:multilayer_attention
sec:nonmonotonic
sec:ood_diagnostics
sec:per_dim_mae
sec:per_task_r2
sec:perdof
sec:permutation
sec:probe_bars_appendix
sec:probe_profiles
sec:probes
sec:qa_probe
sec:random_subset_ablation
sec:related_work
sec:repr_extraction
sec:robustness_appendix
sec:routing_appendix
sec:rsa
sec:rsa_bar_appendix
sec:rsa_perlayer_appendix
sec:seed_sensitivity
sec:setup
sec:spatial_cross_instruction
sec:specificity_control
sec:threshold_sensitivity
sec:token_specialization
sec:training_effect_summary
sec:training_effects_appendix
tab:action_shift_perdim
tab:attention_decomp
tab:counterfactual
tab:demo_sensitivity
tab:dense_routing
tab:dense_routing_main
tab:dose_response
tab:metric_invariance
tab:multilayer_attention
tab:per_dim_mae
tab:per_task_r2
tab:perhead_bootstrap
tab:qa_probe
tab:routing_gradient
tab:rsa_overview
tab:seed_sensitivity
tab:spatial_cross_instruction
tab:specificity_control
tab:threshold_sensitivity
tab:training_effect_summary
tab:training_effects

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-18T19:33:45.231999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL REFS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//' ; done | sort -u",
  "description": "Extract all unique ref keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL REFS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//' ; done | sort -u",
    "description": "Extract all unique ref keys"
  }
}
```

</details>

---

### Tool call

_source line 178 · 2026-05-18T19:33:45.232216+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Underfull\" main.log",
  "description": "List underfull details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep \"Underfull\" main.log",
    "description": "List underfull details"
  }
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-18T19:33:45.232411+00:00_

Underfull \vbox (badness 3396) has occurred while \output is active []
Underfull \vbox (badness 1960) has occurred while \output is active []
Underfull \hbox (badness 1173) in paragraph at lines 159--166
Underfull \hbox (badness 10000) in paragraph at lines 262--268
Underfull \hbox (badness 10000) in paragraph at lines 262--268
Underfull \vbox (badness 2042) has occurred while \output is active []
Underfull \vbox (badness 6063) has occurred while \output is active []
Underfull \vbox (badness 4254) has occurred while \output is active []
Underfull \vbox (badness 1917) has occurred while \output is active []
Underfull \vbox (badness 10000) has occurred while \output is active []

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-18T19:33:45.232751+00:00_

=== ALL REFS ===
fig:action_r2_threecond
fig:attention_appendix
fig:attention_profile
fig:cross_benchmark
fig:dose_response
fig:factorial
fig:layer_curves
fig:metric_comparison
fig:probe_bars
fig:probe_conditions_appendix
fig:rsa_bar
sec:action_r2_threecond
sec:action_trajectory
sec:cka_appendix
sec:cross_benchmark_appendix
sec:cross_instruction_probes
sec:dense_routing
sec:instruction_invariance_appendix
sec:learned_routing
sec:linear_probe
sec:loocv
sec:model_data
sec:nonmonotonic
sec:ood_diagnostics
sec:probes
sec:qa_probe
sec:random_subset_ablation
sec:repr_extraction
sec:rsa
sec:seed_sensitivity
sec:threshold_sensitivity
sec:training_effect_summary
tab:action_shift_perdim
tab:attention_decomp
tab:counterfactual
tab:demo_sensitivity
tab:dense_routing
tab:dense_routing_main
tab:dose_response
tab:metric_invariance
tab:multilayer_attention
tab:per_dim_mae
tab:per_task_r2
tab:perhead_bootstrap
tab:qa_probe
tab:routing_gradient
tab:rsa_overview
tab:seed_sensitivity
tab:spatial_cross_instruction
tab:specificity_control
tab:threshold_sensitivity
tab:training_effect_summary
tab:training_effects

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-18T19:33:45.233004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull \\\\\\\\hbox\" main.log && grep -c \"Underfull \\\\\\\\vbox\" main.log",
  "description": "Count underfull hbox vs vbox"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"Underfull \\\\\\\\hbox\" main.log && grep -c \"Underfull \\\\\\\\vbox\" main.log",
    "description": "Count underfull hbox vs vbox"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-18T19:33:45.233199+00:00_

3
7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-18T19:33:45.233398+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL CITE KEYS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL CITE KEYS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u",
    "description": "Extract all unique citation keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-18T19:33:45.233617+00:00_

=== ALL CITE KEYS ===
alain2017
belinkov2022
belrose2023_tunedlens
bills2023language
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hewitt2019control
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
liu2023_libero
lu2025
meng2022_rome
molinari2025
morcos2018
neo2025
nili2014toolbox
nostalgebraist2020
olsson2022
oquab2024_dinov2
padalkar2023_oxe
radford2021_clip
raghu2017
raghu2021
swann2026
templeton2024scaling
tenney2019
touvron2023_llama2
vig2019
voita2019
wang2023_ioi
zhai2023_siglip

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-18T19:33:45.233822+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL BIB KEYS ===\" && grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
  "description": "Extract all bib entry keys from references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ALL BIB KEYS ===\" && grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
    "description": "Extract all bib entry keys from references.bib"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-18T19:33:45.234031+00:00_

=== ALL BIB KEYS ===
alain2017
belinkov2022
belrose2023_tunedlens
bills2023language
black2024_pi0
brohan2023_rt2
buurmeijer2026
clark2019
conmy2023
darcet2024
dosovitskiy2021
elhage2021
fang2025
fei2025
geva2021
grant2026
haon2025
hewitt2019
hewitt2019control
hou2026
karamcheti2024
kim2024_openvla
kornblith2019
kriegeskorte2008
liu2023_libero
lu2025
meng2022_rome
molinari2025
morcos2018
neo2025
nili2014toolbox
nostalgebraist2020
olsson2022
oquab2024_dinov2
padalkar2023_oxe
radford2021_clip
raghu2017
raghu2021
swann2026
templeton2024scaling
tenney2019
touvron2023_llama2
vig2019
voita2019
wang2023_ioi
zhai2023_siglip

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-18T19:33:45.234232+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"hyperref Warning\" main.log",
  "description": "Count hyperref warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && grep -c \"hyperref Warning\" main.log",
    "description": "Count hyperref warnings"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-18T19:33:45.234404+00:00_

3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-18T19:33:45.234592+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ORPHAN LABELS (defined but never referenced) ===\" && comm -23 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//'; done | sort -u) <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u)",
  "description": "Find orphan labels (defined but never referenced)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ORPHAN LABELS (defined but never referenced) ===\" && comm -23 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//'; done | sort -u) <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u)",
    "description": "Find orphan labels (defined but never referenced)"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-18T19:33:45.234767+00:00_

=== ORPHAN LABELS (defined but never referenced) ===
fig:linear_vs_mlp
fig:multilayer_attention
fig:ood_diagnostics
fig:random_subset_ablation
fig:rsa_perlayer_curve
sec:additional_rsa
sec:appendix
sec:attention_analysis
sec:attention_decomp
sec:attention_pattern
sec:branch_split_appendix
sec:conclusion
sec:demo_sensitivity
sec:discussion
sec:experiments
sec:introduction
sec:method
sec:metric_invariance
sec:metric_sensitivity_appendix
sec:multilayer_attention
sec:per_dim_mae
sec:per_task_r2
sec:perdof
sec:permutation
sec:probe_bars_appendix
sec:probe_profiles
sec:related_work
sec:robustness_appendix
sec:routing_appendix
sec:rsa_bar_appendix
sec:rsa_perlayer_appendix
sec:setup
sec:spatial_cross_instruction
sec:specificity_control
sec:token_specialization
sec:training_effects_appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-18T19:33:45.234984+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== DANGLING REFS (referenced but never defined) ===\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//'; done | sort -u) <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u)",
  "description": "Find dangling refs (referenced but never defined)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== DANGLING REFS (referenced but never defined) ===\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//'; done | sort -u) <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u)",
    "description": "Find dangling refs (referenced but never defined)"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-18T19:33:45.235182+00:00_

=== DANGLING REFS (referenced but never defined) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-18T19:33:45.235381+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING CITES (cited but not in bib) ===\" && comm -23 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u)",
  "description": "Find missing citations (cited but not in bib)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING CITES (cited but not in bib) ===\" && comm -23 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u)",
    "description": "Find missing citations (cited but not in bib)"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-18T19:33:45.235564+00:00_

=== MISSING CITES (cited but not in bib) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-18T19:33:45.235759+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== UNUSED BIB ENTRIES (in bib but never cited) ===\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) && echo \"---\" && echo \"Count:\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) | wc -l",
  "description": "Find unused bib entries (in bib but never cited)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== UNUSED BIB ENTRIES (in bib but never cited) ===\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) && echo \"---\" && echo \"Count:\" && comm -13 <(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u) <(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) | wc -l",
    "description": "Find unused bib entries (in bib but never cited)"
  }
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-18T19:33:45.236020+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\n# Build the cross-validation table\n\n# Registry reference values (extracted from registry above)\nregistry = {\n    # action_trajectory_analysis\n    \"L1 instruction 24h ablation Cohen's d\": 0.651,\n    \"L1 instruction 24h token divergence\": 0.723,\n    \"L1 instruction 24h KL\": 5.079,\n    \"L1 instruction 24h gripper shift\": 0.2907,\n    \n    # action_trajectory_control  \n    \"control 8h Cohen's d\": 0.41,\n    \"control 8h token divergence\": 0.293,\n    \"control 8h gripper shift\": 0.1407,  # registry: 0.1407\n    \"control 8h KL\": 1.69,\n    \n    # dose_response_curve\n    \"dose top4 d\": 0.482,\n    \"dose top32 d\": 0.639,\n    \n    # counterfactual\n    \"counterfactual empty d\": 0.968,\n    \"counterfactual wrong d\": 0.844,\n    \"counterfactual paraphrased d\": 0.697,\n    \"counterfactual shuffled d\": 0.625,\n    \n    # attention_decomposition\n    \"instruction-dominant attention\": 0.624,  # 62.4%\n    \"control attention\": 0.449,  # 44.9%\n    \"per-task R2 L1 10/10 positive\": True,\n    \"per-task R2 L1 mean delta\": 0.0586,\n    \"per-task R2 L13 5/10 positive\": True,\n    \n    # per-head bootstrap\n    \"per-head instruction d\": 0.0271,\n    \"per-head control d\": 0.0514,\n    \"per-head p\": 0.0018,\n    \n    # CV permutation\n    \"cv_exact_paired_p\": 0.0156,\n    \"per_dim_cv_instruction\": 1.3,\n    \"per_dim_cv_control\": 2.74,\n    \n    # random subset ablation\n    \"random_subset baseline_r2\": 0.517,\n    \"random_subset dominant_24_delta\": 0.042,\n    \"random_subset random_24_mean_delta\": 0.077,\n    \"random_subset random_24_std_delta\": 0.013,\n    \"random_subset z_score\": -2.73,\n    \"random_subset p_value\": 0.003,\n    \n    # specificity control\n    \"specificity top24 d\": 0.65,\n    \"specificity bottom24 d\": 0.565,\n    \"specificity ratio\": 1.15,\n    \"specificity KL top24\": 6.50,  # from paper table\n    \"specificity KL bottom24\": 4.166,  # registry: 4.166\n    \n    # trained probe peak (threecond_multiseed_r2_v2)\n    \"trained peak layer\": 9,\n    \"trained peak R2\": 0.643,\n    \"trained peak std\": 0.014,\n    \"L0 baseline R2\": 0.645,\n    \"L0 baseline std\": 0.008,\n    \"untrained peak R2 (excl L32)\": 0.547,\n    \n    # linear probe (linear_probe_last_preaction)\n    \"linear trained peak layer\": 13,\n    \"linear trained peak R2\": 0.596,\n    \"linear untrained peak layer\": 1,\n    \"linear untrained peak R2\": 0.492,\n    \n    # plan_011_fulllayer_r2\n    \"trained image_mean peak layer\": 8,\n    \"trained image_mean peak R2\": 0.6553,\n    \"trained readout peak layer\": 13,\n    \"trained readout peak R2\": 0.6779,\n    \"untrained image_mean peak R2\": 0.6403,\n    \"untrained readout peak R2\": 0.6093,\n    \"best-vs-best image_mean delta\": 0.0149,\n    \"best-vs-best readout delta\": 0.0686,\n    \n    # d041_method_b_rsa\n    \"RSA trained image_mean peak\": 0.6282,\n    \"RSA trained readout peak\": 0.6425,\n    \"RSA untrained image_mean peak\": 0.6117,\n    \"RSA untrained readout peak\": 0.6262,\n    \"RSA DINOv2 cls\": 0.6915,  # registry: 0.6915\n    \"RSA CLIP\": 0.557,\n    \"RSA best-vs-best delta\": 0.017,\n    \n    # ablation_50demos_main\n    \"ablation baseline L1\": 0.5567,\n    \"ablation all24 L1\": 0.6153,\n    \"ablation all24_vs_baseline L1 delta\": 0.0585,\n    \n    # seed robustness\n    \"seed peak R2 mean\": 0.6546,\n    \"seed peak R2 std\": 0.0022,\n    \n    # per-dim MAE ratios\n    \"per-dim dx ratio\": 5.09,  # 5.1x\n    \"per-dim dy ratio\": 4.26,  # 4.3x\n    \"per-dim dz ratio\": 3.14,  # 3.1x\n    \"per-dim roll ratio\": 2.62,  # 2.6x\n    \"per-dim pitch ratio\": 2.21,  # 2.2x\n    \"per-dim yaw ratio\": 1.90,  # 1.9x\n    \n    # llama2_base_control\n    \"llama2base L1 heads\": 9,\n    \"trained L1 heads\": 25,  # note: registry says 25, paper says 24\n    \"untrained L1 heads\": 0,\n    \"trained L1 text attn\": 0.577,\n    \"untrained L1 text attn\": 0.117,\n    \"llama2base L1 text attn\": 0.365,\n    \"trained L1 probe acc\": 0.996,\n    \"llama2base L1 probe acc\": 0.802,\n    \"untrained L31 probe acc\": 0.82,\n    \n    # branch split\n    \"dinov2 branch rsa\": 0.619,\n    \"siglip branch rsa\": 0.621,\n    \"fused rsa\": 0.634,\n    \"projector rsa\": 0.615,\n    \n    # QA probe\n    \"QA trained L20 acc\": 0.8632,\n    \"QA dino acc\": 0.8272,\n    \n    # demo sensitivity\n    \"demo_25 rsa peak rho\": 0.6059,  # registry: 0.6059\n    \"demo_25 rsa profile corr\": 0.9696,\n    \"demo_25 r2 peak\": 0.6088,\n    \"demo_25 r2 profile corr\": 0.8189,\n    \n    # LIBERO-Spatial\n    \"spatial RSA trained img peak layer\": 14,\n    \"spatial RSA trained img peak\": 0.6911,\n    \"spatial R2 trained img peak layer\": 13,\n    \"spatial R2 trained img peak\": 0.6963,\n    \"spatial bootstrap delta\": 0.023,\n    \n    # CKA\n    \"linear CKA untrained\": 0.0894,\n    \"linear CKA trained\": 0.0834,\n    \"linear CKA projector\": 0.0809,\n    \"linear CKA dino\": 0.0664,\n    \"RDM CKA trained\": 0.2599,\n    \"RDM CKA projector\": 0.2568,\n    \"RDM CKA untrained\": 0.2464,\n    \"RDM CKA dino\": 0.2408,\n}\n\nprint(\"Registry data loaded successfully. Key values extracted.\")\nPYEOF",
  "description": "Organize registry metrics for comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\n# Build the cross-validation table\n\n# Registry reference values (extracted from registry above)\nregistry = {\n    # action_trajectory_analysis\n    \"L1 instruction 24h ablation Cohen's d\": 0.651,\n    \"L1 instruction 24h token divergence\": 0.723,\n    \"L1 instruction 24h KL\": 5.079,\n    \"L1 instruction 24h gripper shift\": 0.2907,\n    \n    # action_trajectory_control  \n    \"control 8h Cohen's d\": 0.41,\n    \"control 8h token divergence\": 0.293,\n    \"control 8h gripper shift\": 0.1407,  # registry: 0.1407\n    \"control 8h KL\": 1.69,\n    \n    # dose_response_curve\n    \"dose top4 d\": 0.482,\n    \"dose top32 d\": 0.639,\n    \n    # counterfactual\n    \"counterfactual empty d\": 0.968,\n    \"counterfactual wrong d\": 0.844,\n    \"counterfactual paraphrased d\": 0.697,\n    \"counterfactual shuffled d\": 0.625,\n    \n    # attention_decomposition\n    \"instruction-dominant attention\": 0.624,  # 62.4%\n    \"control attention\": 0.449,  # 44.9%\n    \"per-task R2 L1 10/10 positive\": True,\n    \"per-task R2 L1 mean delta\": 0.0586,\n    \"per-task R2 L13 5/10 positive\": True,\n    \n    # per-head bootstrap\n    \"per-head instruction d\": 0.0271,\n    \"per-head control d\": 0.0514,\n    \"per-head p\": 0.0018,\n    \n    # CV permutation\n    \"cv_exact_paired_p\": 0.0156,\n    \"per_dim_cv_instruction\": 1.3,\n    \"per_dim_cv_control\": 2.74,\n    \n    # random subset ablation\n    \"random_subset baseline_r2\": 0.517,\n    \"random_subset dominant_24_delta\": 0.042,\n    \"random_subset random_24_mean_delta\": 0.077,\n    \"random_subset random_24_std_delta\": 0.013,\n    \"random_subset z_score\": -2.73,\n    \"random_subset p_value\": 0.003,\n    \n    # specificity control\n    \"specificity top24 d\": 0.65,\n    \"specificity bottom24 d\": 0.565,\n    \"specificity ratio\": 1.15,\n    \"specificity KL top24\": 6.50,  # from paper table\n    \"specificity KL bottom24\": 4.166,  # registry: 4.166\n    \n    # trained probe peak (threecond_multiseed_r2_v2)\n    \"trained peak layer\": 9,\n    \"trained peak R2\": 0.643,\n    \"trained peak std\": 0.014,\n    \"L0 baseline R2\": 0.645,\n    \"L0 baseline std\": 0.008,\n    \"untrained peak R2 (excl L32)\": 0.547,\n    \n    # linear probe (linear_probe_last_preaction)\n    \"linear trained peak layer\": 13,\n    \"linear trained peak R2\": 0.596,\n    \"linear untrained peak layer\": 1,\n    \"linear untrained peak R2\": 0.492,\n    \n    # plan_011_fulllayer_r2\n    \"trained image_mean peak layer\": 8,\n    \"trained image_mean peak R2\": 0.6553,\n    \"trained readout peak layer\": 13,\n    \"trained readout peak R2\": 0.6779,\n    \"untrained image_mean peak R2\": 0.6403,\n    \"untrained readout peak R2\": 0.6093,\n    \"best-vs-best image_mean delta\": 0.0149,\n    \"best-vs-best readout delta\": 0.0686,\n    \n    # d041_method_b_rsa\n    \"RSA trained image_mean peak\": 0.6282,\n    \"RSA trained readout peak\": 0.6425,\n    \"RSA untrained image_mean peak\": 0.6117,\n    \"RSA untrained readout peak\": 0.6262,\n    \"RSA DINOv2 cls\": 0.6915,  # registry: 0.6915\n    \"RSA CLIP\": 0.557,\n    \"RSA best-vs-best delta\": 0.017,\n    \n    # ablation_50demos_main\n    \"ablation baseline L1\": 0.5567,\n    \"ablation all24 L1\": 0.6153,\n    \"ablation all24_vs_baseline L1 delta\": 0.0585,\n    \n    # seed robustness\n    \"seed peak R2 mean\": 0.6546,\n    \"seed peak R2 std\": 0.0022,\n    \n    # per-dim MAE ratios\n    \"per-dim dx ratio\": 5.09,  # 5.1x\n    \"per-dim dy ratio\": 4.26,  # 4.3x\n    \"per-dim dz ratio\": 3.14,  # 3.1x\n    \"per-dim roll ratio\": 2.62,  # 2.6x\n    \"per-dim pitch ratio\": 2.21,  # 2.2x\n    \"per-dim yaw ratio\": 1.90,  # 1.9x\n    \n    # llama2_base_control\n    \"llama2base L1 heads\": 9,\n    \"trained L1 heads\": 25,  # note: registry says 25, paper says 24\n    \"untrained L1 heads\": 0,\n    \"trained L1 text attn\": 0.577,\n    \"untrained L1 text attn\": 0.117,\n    \"llama2base L1 text attn\": 0.365,\n    \"trained L1 probe acc\": 0.996,\n    \"llama2base L1 probe acc\": 0.802,\n    \"untrained L31 probe acc\": 0.82,\n    \n    # branch split\n    \"dinov2 branch rsa\": 0.619,\n    \"siglip branch rsa\": 0.621,\n    \"fused rsa\": 0.634,\n    \"projector rsa\": 0.615,\n    \n    # QA probe\n    \"QA trained L20 acc\": 0.8632,\n    \"QA dino acc\": 0.8272,\n    \n    # demo sensitivity\n    \"demo_25 rsa peak rho\": 0.6059,  # registry: 0.6059\n    \"demo_25 rsa profile corr\": 0.9696,\n    \"demo_25 r2 peak\": 0.6088,\n    \"demo_25 r2 profile corr\": 0.8189,\n    \n    # LIBERO-Spatial\n    \"spatial RSA trained img peak layer\": 14,\n    \"spatial RSA trained img peak\": 0.6911,\n    \"spatial R2 trained img peak layer\": 13,\n    \"spatial R2 trained img peak\": 0.6963,\n    \"spatial bootstrap delta\": 0.023,\n    \n    # CKA\n    \"linear CKA untrained\": 0.0894,\n    \"linear CKA trained\": 0.0834,\n    \"linear CKA projector\": 0.0809,\n    \"linear CKA dino\": 0.0664,\n    \"RDM CKA trained\": 0.2599,\n    \"RDM CKA projector\": 0.2568,\n    \"RDM CKA untrained\": 0.2464,\n    \"RDM CKA dino\": 0.2408,\n}\n\nprint(\"Registry data loaded successfully. Key values extracted.\")\nPYEOF",
    "description": "Organize registry metrics for comparison"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-18T19:33:45.236292+00:00_

Registry data loaded successfully. Key values extracted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-18T19:33:45.236474+00:00_

=== UNUSED BIB ENTRIES (in bib but never cited) ===
---
Count:
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-18T19:33:45.236677+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== DUPLICATE LABELS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed \"s/\\\\\\\\label{//;s/}//\" | while read lbl; do echo \"$lbl $f\"; done; done | sort | uniq -D -f0 | awk '{print $1}' | sort -u",
  "description": "Check for duplicate labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== DUPLICATE LABELS ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed \"s/\\\\\\\\label{//;s/}//\" | while read lbl; do echo \"$lbl $f\"; done; done | sort | uniq -D -f0 | awk '{print $1}' | sort -u",
    "description": "Check for duplicate labels"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-18T19:33:45.237150+00:00_

## 编译结果

### 编译环境
- Tool used: `latexmk -pdf` (pdfTeX 3.141592653, TeX Live 2025)
- Location: local (`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/`)
- Output: `main.pdf` (26 pages, 555 KB)

### Errors (0)
无编译错误，PDF 成功生成。

### Warnings (30)
- Undefined references: 0
- Missing citations: 0
- Overfull hbox: 0
- Underfull hbox: 3
- Underfull vbox: 7
- Float specifier changed (`h` -> `ht`): 17
- Hyperref token warnings: 3

### 详细 warning 列表

**Float specifier warnings (17)**
共 17 处 `[h]` 被 LaTeX 自动改为 `[ht]`，均在 `appendix.tex` 中。建议将这些 float 的 specifier 从 `[h]` 改为 `[ht]` 或 `[htbp]` 以消除警告。

**Underfull hbox (3)**
- `main.bbl` lines 159-166: badness 1173, bibliography entry 中 URL 断行导致
- `main.bbl` lines 262-268: badness 10000 (x2), bibliography entry "nostalgebraist. interpreting GPT: the logit lens" 的 URL 断行问题

这 3 个 underfull hbox 均发生在 references 的 URL 断行处，是 BibTeX 排版 URL 时的常见问题，可通过在 bib 条目中使用 `\url{}` 包裹或调整 `\sloppy` 设置缓解。

**Underfull vbox (7)**
- 分布在第 1, 5, 13, 16, 17, 23, 24 页附近
- badness 范围 1917 - 10000
- 主要由浮动体（figures/tables）的页面分布造成，属于排版调优问题，不影响正确性

**Hyperref warnings (3)**
- `appendix.tex` line 638: section 标题中包含数学公式 (`$R^2$`)，hyperref 无法将其编码为 PDF 书签字符串
- 修复：使用 `\texorpdfstring{$R^2$}{R2}` 替代
agentId: a5857206b887a1a30 (use SendMessage with to: 'a5857206b887a1a30' to continue this agent)
&lt;usage>total_tokens: 25643
tool_uses: 18
duration_ms: 47973&lt;/usage>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "elapsed_ms": 31
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-18T19:33:45.237379+00:00_

=== DUPLICATE LABELS ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-18T19:33:45.237653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING ~ BEFORE \\\\ref ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -n '[^~]\\\\ref{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
  "description": "Check for \\ref without preceding ~ (non-breaking space)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING ~ BEFORE \\\\ref ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -n '[^~]\\\\ref{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
    "description": "Check for \\ref without preceding ~ (non-breaking space)"
  }
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-18T19:33:45.237856+00:00_

=== MISSING ~ BEFORE \ref ===
method.tex:64:We report both in Appendix~ref{sec:cka_appendix}; the divergence between metrics (Sref{sec:nonmonotonic}) confirms neither alone fully characterizes representational structure.
experiments.tex:8:Representations are extracted from six sources spanning the VLA pipeline (Sref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image_mean and readout tokens at each of 32 layers, DINOv2~cite{oquab2024_dinov2} (texttt{cls_token}/texttt{patch_mean}), CLIP~cite{radford2021_clip} (texttt{patch_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
experiments.tex:9:Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (Sref{sec:model_data}).
experiments.tex:10:RSA computes Spearman $rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (Sref{sec:rsa}).
experiments.tex:11:MLP probes (input $to$ 256 $to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (Sref{sec:probes}).
experiments.tex:18:As a sanity check on the experimental framework, we train cross-instruction probes (Sref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
experiments.tex:68:In the original extraction pipeline (Sref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs. no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $Delta approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~ref{tab:per_task_r2}).
appendix.tex:87:To evaluate whether the ablation effect in Sref{sec:learned_routing} is specific to instruction-dominant heads, we compare dominant-head ablation against 10 random subsets of 24/32 L1 heads (each subset drawn without replacemen
…[truncated 611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-18T19:33:45.238127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING ~ BEFORE \\\\ref (excluding \\\\S\\\\ref and already ~\\\\ref) ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -nP '(?&lt;!~)(?&lt;!\\\\S)\\\\ref\\{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
  "description": "Check for \\ref without preceding ~ or \\S (refined check)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== MISSING ~ BEFORE \\\\ref (excluding \\\\S\\\\ref and already ~\\\\ref) ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -nP '(?&lt;!~)(?&lt;!\\\\S)\\\\ref\\{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
    "description": "Check for \\ref without preceding ~ or \\S (refined check)"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-18T19:33:45.238323+00:00_

=== MISSING ~ BEFORE \ref (excluding \S\ref and already ~\ref) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-18T19:33:45.238526+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== SPACE BEFORE \\\\ref (should be ~) ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -nP ' \\\\ref\\{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
  "description": "Check for space before \\ref that should be ~"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== SPACE BEFORE \\\\ref (should be ~) ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -nP ' \\\\ref\\{' \"$f\" 2>/dev/null | grep -v '^\\s*%' | while read line; do echo \"$f:$line\"; done; done",
    "description": "Check for space before \\ref that should be ~"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-18T19:33:45.239056+00:00_

=== SPACE BEFORE \ref (should be ~) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-18T19:33:45.239377+00:00_

Now I have all the data needed. Let me compile the complete analysis.

Here is the full audit.

---

## A. Problematic Residual Strong Claims

| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |
|---|---|---|---|
| related_work.tex:29 | "the readout token serves as the **exclusive** multimodal hub" | 残留强claim | 改为 "the **primary** multimodal hub" |
| abstract.tex:4 | "the readout token serves as the **sole** multimodal convergence point" | 残留强claim | 改为 "the **primary** multimodal convergence point"（"sole" 是绝对声明，除非有理论证明不可能存在其他路径） |
| related_work.tex:25 | "identify the readout token as the **sole** multimodal integration site" | 残留强claim | 同上，改为 "primary" |
| experiments.tex:26 | "The readout is thus the **sole** locus of multimodal integration" | 残留强claim | 同上，改为 "primary" |

**注**：以下搜索项 **未找到** 任何匹配：
- "uniquely responsible" — 无
- "exclusively" — 无
- "solely driven" — 无
- "only instruction heads" — 无
- "instruction-specific" — 无

"specific to instruction-dominant heads" 出现在 appendix.tex:87 和 appendix.tex:671，但上下文是描述实验设计（"evaluate whether the ablation effect is specific to instruction-dominant heads"），属于合理的实验问题表述，**无需修改**。

"the primary" 出现 4 次（abstract.tex:8, introduction.tex:21, introduction.tex:23, conclusion.tex:5），用法均为 "the primary routing hub" / "the primary learned contribution"，搭配 "primarily" 限定词，**与新叙事一致，无需修改**。

---

## B. AI Writing Style Markers

### B1. Em-dash (U+2014 "—") 和 En-dash (U+2013 " – ")

**零匹配。** 全部 .tex 文件中无 em-dash 和解释性 en-dash。LaTeX `--` 语法（如 `L0--L1`, `0.63--0.97`）是数字范围的标准 TeX 写法，不是 AI 标志。

### B2. -ing 分词短语结尾句子

| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |
|---|---|---|---|
| related_work.tex:16 | "...we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning." | AI写作-ing | 此处 "fine-tuning" 作为名词用法，可接受，**无需修改** |
| conclusion.tex:4 | "...revealing that VLA fine-tuning primarily reorganizes..." | AI写作-ing | "revealing that" 是典型 -ing 分词引导结果从句。改为 "...VLA representations. The analysis
…[truncated 2977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "elapsed_ms": 43
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-18T19:33:45.239648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ORPHAN LABELS WITH LOCATION ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -n '\\\\label{' \"$f\" 2>/dev/null | while IFS= read -r line; do lnum=$(echo \"$line\" | cut -d: -f1); lbl=$(echo \"$line\" | grep -oP '\\\\label\\{[^}]+\\}' | sed 's/\\\\label{//;s/}//'); echo \"$f:$lnum:$lbl\"; done; done | while IFS=: read -r file lnum lbl; do is_ref=0; for f2 in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do if grep -qP \"\\\\\\\\(ref|eqref|autoref|cref|Cref)\\{$lbl\\}\" \"$f2\" 2>/dev/null; then is_ref=1; break; fi; done; if [ \"$is_ref\" = \"0\" ]; then echo \"- $file:$lnum - \\\\label{$lbl}\"; fi; done",
  "description": "Get orphan labels with file:line details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"=== ORPHAN LABELS WITH LOCATION ===\" && for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -n '\\\\label{' \"$f\" 2>/dev/null | while IFS= read -r line; do lnum=$(echo \"$line\" | cut -d: -f1); lbl=$(echo \"$line\" | grep -oP '\\\\label\\{[^}]+\\}' | sed 's/\\\\label{//;s/}//'); echo \"$f:$lnum:$lbl\"; done; done | while IFS=: read -r file lnum lbl; do is_ref=0; for f2 in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do if grep -qP \"\\\\\\\\(ref|eqref|autoref|cref|Cref)\\{$lbl\\}\" \"$f2\" 2>/dev/null; then is_ref=1; break; fi; done; if [ \"$is_ref\" = \"0\" ]; then echo \"- $file:$lnum - \\\\label{$lbl}\"; fi; done",
    "description": "Get orphan labels with file:line details"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-18T19:33:45.239871+00:00_

=== ORPHAN LABELS WITH LOCATION ===
- introduction.tex:2 - \label{sec:introduction}
- related_work.tex:1 - \label{sec:related_work}
- method.tex:2 - \label{sec:method}
- method.tex:39 - \label{sec:attention_analysis}
- experiments.tex:2 - \label{sec:experiments}
- experiments.tex:5 - \label{sec:setup}
- experiments.tex:16 - \label{sec:token_specialization}
- discussion.tex:2 - \label{sec:discussion}
- conclusion.tex:2 - \label{sec:conclusion}
- appendix.tex:4 - \label{sec:appendix}
- appendix.tex:19 - \label{sec:metric_sensitivity_appendix}
- appendix.tex:37 - \label{sec:branch_split_appendix}
- appendix.tex:45 - \label{sec:rsa_bar_appendix}
- appendix.tex:57 - \label{sec:rsa_perlayer_appendix}
- appendix.tex:63 - \label{fig:rsa_perlayer_curve}
- appendix.tex:95 - \label{fig:random_subset_ablation}
- appendix.tex:210 - \label{fig:ood_diagnostics}
- appendix.tex:227 - \label{fig:linear_vs_mlp}
- appendix.tex:231 - \label{sec:probe_bars_appendix}
- appendix.tex:256 - \label{sec:additional_rsa}
- appendix.tex:283 - \label{sec:spatial_cross_instruction}
- appendix.tex:307 - \label{sec:robustness_appendix}
- appendix.tex:310 - \label{sec:metric_invariance}
- appendix.tex:332 - \label{sec:perdof}
- appendix.tex:338 - \label{sec:permutation}
- appendix.tex:371 - \label{sec:demo_sensitivity}
- appendix.tex:398 - \label{sec:training_effects_appendix}
- appendix.tex:454 - \label{sec:routing_appendix}
- appendix.tex:513 - \label{sec:probe_profiles}
- appendix.tex:523 - \label{sec:attention_pattern}
- appendix.tex:536 - \label{sec:multilayer_attention}
- appendix.tex:545 - \label{fig:multilayer_attention}
- appendix.tex:592 - \label{sec:attention_decomp}
- appendix.tex:614 - \label{sec:per_dim_mae}
- appendix.tex:639 - \label{sec:per_task_r2}
- appendix.tex:669 - \label{sec:specificity_control}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-18T19:33:45.240143+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"Total labels: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null; done | wc -l)\" && echo \"Unique labels: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//' ; done | sort -u | wc -l)\" && echo \"Unique refs: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u | wc -l)\" && echo \"Unique cite keys: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u | wc -l)\" && echo \"Unique bib keys: $(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u | wc -l)\"",
  "description": "Get summary counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && echo \"Total labels: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null; done | wc -l)\" && echo \"Unique labels: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\label\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\label{//;s/}//' ; done | sort -u | wc -l)\" && echo \"Unique refs: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\(ref|eqref|autoref|cref|Cref)\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/.*{//;s/}//'; done | sort -u | wc -l)\" && echo \"Unique cite keys: $(for f in main.tex abstract.tex introduction.tex related_work.tex method.tex experiments.tex discussion.tex conclusion.tex appendix.tex; do grep -oP '\\\\cite[a-z]*\\{[^}]+\\}' \"$f\" 2>/dev/null | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//'; done | sort -u | wc -l)\" && echo \"Unique bib keys: $(grep -oP '^@\\w+\\{([^,]+),' references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u | wc -l)\"",
    "description": "Get summary counts"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-18T19:33:45.240524+00:00_

Total labels: 89
Unique labels: 89
Unique refs: 53
Unique cite keys: 46
Unique bib keys: 46

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-18T19:33:45.240818+00:00_

## 交叉引用检查

### 孤立 \label (defined but never referenced)

**主文 section labels (9 个, 正常):** 主文的 section/subsection labels 通常不需要 `\ref`，而是通过文档结构组织，属于预期行为:
- introduction.tex:2 - `\label{sec:introduction}`
- related_work.tex:1 - `\label{sec:related_work}`
- method.tex:2 - `\label{sec:method}`
- method.tex:39 - `\label{sec:attention_analysis}`
- experiments.tex:2 - `\label{sec:experiments}`
- experiments.tex:5 - `\label{sec:setup}`
- experiments.tex:16 - `\label{sec:token_specialization}`
- discussion.tex:2 - `\label{sec:discussion}`
- conclusion.tex:2 - `\label{sec:conclusion}`

**附录 section labels (18 个, 部分值得关注):** 附录的 subsection labels 未被正文或附录其他位置引用:
- appendix.tex:4 - `\label{sec:appendix}`
- appendix.tex:19 - `\label{sec:metric_sensitivity_appendix}`
- appendix.tex:37 - `\label{sec:branch_split_appendix}`
- appendix.tex:45 - `\label{sec:rsa_bar_appendix}`
- appendix.tex:57 - `\label{sec:rsa_perlayer_appendix}`
- appendix.tex:231 - `\label{sec:probe_bars_appendix}`
- appendix.tex:256 - `\label{sec:additional_rsa}`
- appendix.tex:283 - `\label{sec:spatial_cross_instruction}`
- appendix.tex:307 - `\label{sec:robustness_appendix}`
- appendix.tex:310 - `\label{sec:metric_invariance}`
- appendix.tex:332 - `\label{sec:perdof}`
- appendix.tex:338 - `\label{sec:permutation}`
- appendix.tex:371 - `\label{sec:demo_sensitivity}`
- appendix.tex:398 - `\label{sec:training_effects_appendix}`
- appendix.tex:454 - `\label{sec:routing_appendix}`
- appendix.tex:513 - `\label{sec:probe_profiles}`
- appendix.tex:523 - `\label{sec:attention_pattern}`
- appendix.tex:536 - `\label{sec:multilayer_attention}`
- appendix.tex:592 - `\label{sec:attention_decomp}`
- appendix.tex:614 - `\label{sec:per_dim_mae}`
- appendix.tex:639 - `\label{sec:per_task_r2}`
- appendix.tex:669 - `\label{sec:specificity_control}`

**附录 figure labels (5 个, 值得关注):** 这些图定义了 label 但从未被引用:
- appendix.tex:63 - `\label{fig:rsa_perlayer_curve}`
- appendix.tex:95 - `\label{fig:random_subset_ablation}`
- appendix.tex:210 - `
…[truncated 1243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "elapsed_ms": 39
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-18T19:33:45.241248+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\n# Comprehensive cross-validation\n\nrows = []\n\ndef add(file, line, paper_val, registry_val, status):\n    rows.append((f\"{file}:{line}\", paper_val, registry_val, status))\n\n# ===== ABSTRACT (abstract.tex) =====\n# Line 4: 100% instruction classification\nadd(\"abstract.tex\", 4, \"100%\", \"100% (lg_gc_trained L1+)\", \"✅ 匹配\")\n\n# Line 6: d=0.48→0.64 dose-response\nadd(\"abstract.tex\", 6, \"d=0.48→0.64\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配 (rounded)\")\n\n# Line 6: d=0.63--0.97 counterfactual\nadd(\"abstract.tex\", 6, \"d=0.63--0.97\", \"d=0.625--0.968 (counterfactual_instruction)\", \"✅ 匹配 (rounded)\")\n\n# Line 8: R² +0.069\nadd(\"abstract.tex\", 8, \"R² +0.069\", \"+0.0686 (plan_011_fulllayer_r2)\", \"✅ 匹配 (rounded)\")\n\n# Line 8: +46pp attention\nadd(\"abstract.tex\", 8, \"+46pp attention\", \"57.7%-11.7%=46.0pp (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 8: Δρ ≤ 0.017\nadd(\"abstract.tex\", 8, \"Δρ ≤ 0.017\", \"+0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# ===== INTRODUCTION (introduction.tex) =====\n# Line 17: 100% cross-validated\nadd(\"introduction.tex\", 17, \"100%\", \"100% (lg_gc_trained)\", \"✅ 匹配\")\n\n# Line 18: L9--L16: 15--22 heads (Llama-2 base mid-depth)\nadd(\"introduction.tex\", 18, \"L9--L16: 15--22 heads\", \"Qualitative (multilayer_attention table)\", \"⚠️ 未找到registry记录\")\n\n# Line 18: L0--L1: 21--24 heads, L31: 18 heads\nadd(\"introduction.tex\", 18, \"L0--L1: 21--24 heads, L31: 18\", \"L1: 24/32 (llama2_base_control, but 25 in registry)\", \"❌ 不匹配 (registry=25 vs paper=24)\")\n\n# Line 19: d=0.48→0.64\nadd(\"introduction.tex\", 19, \"d=0.48→0.64\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配 (rounded)\")\n\n# Line 19: d=0.63--0.97\nadd(\"introduction.tex\", 19, \"d=0.63--0.97\", \"d=0.625--0.968 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# Line 20: R² at L8--L14, RSA at L12\nadd(\"introduction.tex\", 20, \"R² peak L8--L14\", \"R² peak L8 image_mean, L13 readout (plan_011)\", \"✅ 匹配\")\nadd(\"introduction.tex\", 20, \"RSA peak L12\", \"L12 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 21: Δρ = 0.017, 3%\nadd(\"introduction.tex\", 21, \"Δρ = 0.017\", \"+0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 21: R² Δ = +0.069, p < 0.0001\nadd(\"introduction.tex\", 21, \"R² Δ = +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# ===== EXPERIMENTS (experiments.tex) =====\n# Line 12: N = 63,228 observations\nadd(\"experiments.tex\", 12, \"N = 63,228\", \"lg_dino_extract: total_frames=63728\", \"❌ 不匹配 (63228 vs 63728)\")\n\n# Line 21: 10% image_mean\nadd(\"experiments.tex\", 21, \"10% image_mean chance\", \"10% (lg_gc_trained L0, cross_inst)\", \"✅ 匹配\")\n\n# Line 22: DINOv2 10%\nadd(\"experiments.tex\", 22, \"DINOv2 10%\", \"DINOv2 at chance (consistent)\", \"✅ 匹配\")\n\n# Line 25: 100% L1-L31 trained readout, 82% untrained L31\nadd(\"experiments.tex\", 25, \"100% L1-L31 trained\", \"100% (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 25, \"82% untrained L31\", \"0.82 (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 26: QA 86.3% vs 82.7%\nadd(\"experiments.tex\", 26, \"86.3% QA trained\", \"86.32% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 26, \"82.7% DINOv2 QA\", \"82.72% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\n\n# Table tab:dense_routing_main (lines 37-42)\nadd(\"experiments.tex\", 37, \"L0: 10.0% / 10.0% / 10.0%\", \"Consistent with lg_gc data\", \"✅ 匹配\")\nadd(\"experiments.tex\", 38, \"L1: 100.0% / 100.0% / 10.0%\", \"llama2_base_control: trained=1.0, untrained=1.0\", \"✅ 匹配\")\nadd(\"experiments.tex\", 40, \"L8: 100.0% / 95.5% / 10.0%\", \"llama2_base_control: untrained L8=0.986\", \"❌ 不匹配 (paper=95.5% vs registry=98.6%)\")\nadd(\"experiments.tex\", 41, \"L16: 100.0% / 91.1% / 10.0%\", \"llama2_base_control: untrained L16=0.92\", \"❌ 不匹配 (paper=91.1% vs registry=92.0%)\")\nadd(\"experiments.tex\", 42, \"L31: 100.0% / 82.0% / 10.0%\", \"llama2_base_control: untrained L31=0.82\", \"✅ 匹配\")\n\n# Line 52: 0/32, 9/32, 24/32 heads; 11.7%, 36.5%, 57.7%\nadd(\"experiments.tex\", 52, \"untrained 0/32 (11.7%)\", \"0 heads, 0.117 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 52, \"Llama-2 9/32 (36.5%)\", \"9 heads, 0.365 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 52, \"VLA 24/32 (57.7%)\", \"25 heads, 0.577 (llama2_base_control)\", \"❌ 不匹配 (heads: paper=24 vs registry=25)\")\n\n# Line 60: 99.6% VLA at L1, 80.2% Llama-2 at L1\nadd(\"experiments.tex\", 60, \"VLA 99.6% at L1\", \"0.996 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 60, \"Llama-2 80.2% at L1\", \"0.802 (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 61: R² +0.069, attention +46pp, Δ ≤ 1.7%\nadd(\"experiments.tex\", 61, \"R² +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 61, \"+46pp attention\", \"46.0pp (57.7%-11.7%)\", \"✅ 匹配\")\n\n# Line 65: +0.042 (baseline 0.517)\nadd(\"experiments.tex\", 65, \"+0.042 (baseline 0.517)\", \"0.042 / 0.517 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Line 66: +0.077 ± 0.013, z=-2.73, p=0.003\nadd(\"experiments.tex\", 66, \"+0.077 ± 0.013\", \"0.077 ± 0.013 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 66, \"z=-2.73, p=0.003\", \"-2.73, 0.003 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Line 68: +0.059 L1, +0.018 L8, ~0 L13\nadd(\"experiments.tex\", 68, \"+0.059 L1 ablation\", \"0.0585 (ablation_50demos_main)\", \"✅ 匹配 (rounded)\")\n\n# Line 71: 72.3% d=0.65, d=0.41 (29.3%), 0.291 vs <0.034\nadd(\"experiments.tex\", 71, \"72.3% token div, d=0.65\", \"0.723, 0.651 (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 71, \"d=0.41 (29.3%)\", \"0.41, 0.293 (action_trajectory_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 71, \"gripper 0.291 vs <0.034\", \"0.2907 vs 0.0339 max rotation (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Line 74: d=0.482→0.639\nadd(\"experiments.tex\", 74, \"d=0.482→0.639\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配\")\n\n# Line 78: empty 0.968, wrong 0.844, paraphrased 0.697, shuffled 0.625\nadd(\"experiments.tex\", 78, \"empty d=0.968\", \"0.968 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"wrong d=0.844\", \"0.844 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"paraphrased d=0.697\", \"0.697 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"shuffled d=0.625\", \"0.625 (counterfactual)\", \"✅ 匹配\")\n\n# Line 80: L1 ablation d=0.65\nadd(\"experiments.tex\", 80, \"L1 ablation d=0.65\", \"0.651 (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Table routing_gradient (lines 91-93)\nadd(\"experiments.tex\", 91, \"VLA: 24/32, 57.7%, 99.6%, 100%\", \"Registry: 25/32 heads\", \"❌ 不匹配 (heads: 24 vs 25)\")\nadd(\"experiments.tex\", 92, \"Llama-2: 9/32, 36.5%, 80.2%, 100%\", \"Registry: 9/32, 0.365, 0.802, 1.0\", \"✅ 匹配\")\nadd(\"experiments.tex\", 93, \"Untrained: 0/32, 11.7%, 100%, 82%\", \"Registry: 0/32, 0.117, 1.0, 0.82\", \"✅ 匹配\")\n\n# Line 111: DINOv2 ρ=0.692, VLA peak 0.628 at L12, CLIP 0.557\nadd(\"experiments.tex\", 111, \"DINOv2 ρ=0.692\", \"0.6915 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 111, \"VLA peak 0.628 at L12\", \"0.6282 at L12 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 111, \"CLIP 0.557\", \"0.557 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 114: 0.655 ± 0.002 (seed sensitivity)\nadd(\"experiments.tex\", 114, \"0.655 ± 0.002\", \"0.6546 ± 0.0022 (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\n\n# Line 115: readout R²=0.678 (L13), Δ=0.048 from projector\nadd(\"experiments.tex\", 115, \"readout R²=0.678 at L13\", \"0.6779 at L13 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 115, \"Δ=0.048 from projector\", \"0.6779 - 0.6298 = 0.0481 (plan_011 vs plan_012)\", \"✅ 匹配 (rounded)\")\n\n# Line 119: Δρ=0.017, 3%\nadd(\"experiments.tex\", 119, \"Δρ=0.017, 3%\", \"0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 120: readout R² +0.069, p<0.0001, CI [0.047,0.090]\nadd(\"experiments.tex\", 120, \"readout R² +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 120, \"image_mean +0.015, p=0.006\", \"+0.0149, p=0.006 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# Table rsa_overview (lines 132-143)\nadd(\"experiments.tex\", 132, \"DINOv2 cls RSA=0.692, R²=0.634\", \"RSA=0.6915, R²=0.6343 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 133, \"VLA readout RSA=0.643, R²=0.678\", \"RSA=0.6425, R²=0.6779 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 134, \"Fused DinoSigLIP RSA=0.634\", \"0.634 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 135, \"VLA img_mean RSA=0.628, R²=0.655\", \"RSA=0.6282, R²=0.6553 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 136, \"Projector RSA=0.615, R²=0.630\", \"RSA=0.615, R²=0.6298 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 137, \"Untrained img_mean RSA=0.612, R²=0.640\", \"RSA=0.6117, R²=0.6403 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 138, \"Untrained readout RSA=0.626, R²=0.609\", \"RSA=0.6262, R²=0.6093 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 139, \"CLIP RSA=0.557, R²=0.587\", \"RSA=0.557, R²=0.5866 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\n\n# Figure layer_curves (line 149): L0 0.612 → L12 0.628 → L32 0.422\nadd(\"experiments.tex\", 149, \"L0 0.612→L12 0.628→L32 0.422\", \"L0=0.6117, L12=0.6282 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\n\n# ===== DISCUSSION (discussion.tex) =====\n# Line 5: R² +0.069, +46pp, Δ ≤ 1.7%\nadd(\"discussion.tex\", 5, \"R² +0.069, +46pp\", \"Consistent with above\", \"✅ 匹配\")\n\n# Line 6: ρ=0.692, R²=0.678 vs 0.634\nadd(\"discussion.tex\", 6, \"ρ=0.692, R²=0.678 vs 0.634\", \"0.6915, 0.6779 vs 0.6343\", \"✅ 匹配 (rounded)\")\n\n# Line 8: 0→9→24 heads\nadd(\"discussion.tex\", 8, \"0→9→24 heads\", \"Registry: 0, 9, 25 heads\", \"❌ 不匹配 (VLA heads: 24 vs 25)\")\n\n# Line 9: +0.059 L1, ~0 L13\nadd(\"discussion.tex\", 9, \"+0.059 at L1\", \"0.0585 (ablation_50demos_main)\", \"✅ 匹配 (rounded)\")\n\n# Line 10: d=0.65, 72.3%\nadd(\"discussion.tex\", 10, \"d=0.65, 72.3%\", \"0.651, 0.723\", \"✅ 匹配 (rounded)\")\n\n# Line 11: d=0.48→0.64\nadd(\"discussion.tex\", 11, \"d=0.48→0.64\", \"0.482→0.639\", \"✅ 匹配 (rounded)\")\n\n# Line 12: d=0.63--0.97\nadd(\"discussion.tex\", 12, \"d=0.63--0.97\", \"0.625--0.968\", \"✅ 匹配 (rounded)\")\n\n# Line 13: p=0.002 bootstrap CIs\nadd(\"discussion.tex\", 13, \"p=0.002\", \"p=0.0018 (action_trajectory_cpu_analysis)\", \"❌ 不匹配 (0.002 vs 0.0018)\")\n\n# Line 14: p=0.016 CV permutation\nadd(\"discussion.tex\", 14, \"p=0.016\", \"cv_exact_paired_p=0.0156 (permutation_test_I2)\", \"✅ 匹配 (rounded)\")\n\n# Line 17: d=0.051 vs 0.027\nadd(\"discussion.tex\", 17, \"d=0.051 vs 0.027\", \"0.0514 vs 0.0271 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Line 18: d=0.57 vs 0.65 (bottom-24 vs top-24)\nadd(\"discussion.tex\", 18, \"d=0.57 vs 0.65\", \"0.565 vs 0.65 (specificity_control)\", \"❌ 不匹配 (paper=0.57 vs registry=0.565)\")\n\n# Line 18: KL ratio 1.56x\nadd(\"discussion.tex\", 18, \"KL ratio 1.56×\", \"6.50/4.166 = 1.56 (specificity_control)\", \"✅ 匹配\")\n\n# Line 20: d=0.70 paraphrased\nadd(\"discussion.tex\", 20, \"d=0.70 paraphrased\", \"0.697 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# Line 20: d=0.63 shuffled\nadd(\"discussion.tex\", 20, \"d=0.63 shuffled\", \"0.625 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# ===== APPENDIX (appendix.tex) =====\n# CKA values (lines 21-22)\nadd(\"appendix.tex\", 21, \"Linear CKA: untrained=0.089, trained=0.083, proj=0.081, DINOv2=0.066\", \n    \"0.0894, 0.0834, 0.0809, 0.0664 (plan_009_cka)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 22, \"RDM CKA: trained=0.260, proj=0.257, untrained=0.246, DINOv2=0.241\",\n    \"0.2599, 0.2568, 0.2464, 0.2408 (plan_009_cka)\", \"✅ 匹配 (rounded)\")\n\n# Line 25: linear CKA L0=0.081, L32=0.098\nadd(\"appendix.tex\", 25, \"linear CKA L0=0.081→L32=0.098\", \"L0=0.0809 (plan_009_cka, projector)\", \"⚠️ 未找到registry记录 (per-layer CKA)\")\n\n# Branch split (lines 40-42)\nadd(\"appendix.tex\", 40, \"DINOv2 branch ρ=0.619, SigLIP ρ=0.621\", \"0.619, 0.621 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 41, \"Fused ρ=0.634\", \"0.634 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 42, \"Projector ρ=0.615, Δ=0.019\", \"0.615 (plan_013). 0.634-0.615=0.019\", \"✅ 匹配\")\n\n# DINOv2 patch_mean (line 258)\nadd(\"appendix.tex\", 258, \"DINOv2 patch_mean ρ=0.631\", \"0.6307 (d041_method_b_rsa dino_patch_mean)\", \"✅ 匹配 (rounded)\")\n\n# Untrained readout peak L1 ρ=0.626 (line 259)\nadd(\"appendix.tex\", 259, \"Untrained readout peak L1 ρ=0.626\", \"0.6262 at L1 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\n\n# LIBERO-Spatial (lines 267-268)\nadd(\"appendix.tex\", 267, \"Spatial RSA peak L14 ρ=0.691, R² L13 0.696\", \"L14: 0.6911, L13: 0.6963 (plan_010)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 268, \"Spatial Δ=+0.023, p<0.001\", \"0.023, p=0.001 (plan_010_libero_spatial)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 268, \"Goal Δ=+0.017\", \"0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Spatial cross-instruction (line 287): 75.4% L31\nadd(\"appendix.tex\", 287, \"untrained 75.4% L31 Spatial\", \"0.754 L31 (cross_inst_spatial_trained)\", \"✅ 匹配\")\n\n# Three-condition R² (lines 70-72)\nadd(\"appendix.tex\", 70, \"L0 R²=0.645±0.008\", \"0.645±0.008 (threecond_multiseed_v2)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 71, \"Trained peak L9 R²=0.643±0.014\", \"L9, 0.643±0.014 (threecond_multiseed_v2)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 72, \"Llama-2 base L0:0.645→L32:0.551\", \"L0=0.645 (threecond). L32=0.551 from notes\", \"✅ 匹配\")\n\n# Random subset ablation (lines 88-89)\nadd(\"appendix.tex\", 88, \"+0.042 (baseline 0.517)\", \"0.042, 0.517 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 88, \"+0.077 ± 0.013\", \"0.077±0.013 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 89, \"z=-2.73, p=0.003\", \"-2.73, 0.003 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Per-task Cohen's d (line 105): 0.43, 0.69, 0.70, 0.70, 0.73 (mean 0.65)\nadd(\"appendix.tex\", 105, \"Per-task d: 0.43-0.73, mean 0.65\", \"range [0.433, 0.729] (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Token-level KL (line 106): 5.08 instruction, 1.69 control\nadd(\"appendix.tex\", 106, \"KL instruction=5.08, control=1.69\", \"5.079, 1.69 (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Per-head bootstrap (lines 109-110)\nadd(\"appendix.tex\", 109, \"control d=0.051, instruction d=0.027, p=0.0018\", \"0.0514, 0.0271, 0.0018 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Per-head bootstrap table (lines 121-124)\nadd(\"appendix.tex\", 121, \"Instruction: 24 heads, collective d=0.65, per-head d=0.027 [0.026,0.029]\",\n    \"24h, 0.65, 0.0271 [0.0258,0.0285] (cpu_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 122, \"Control: 8 heads, collective d=0.41, per-head d=0.051 [0.048,0.055]\",\n    \"8h, 0.41, 0.0514 [0.0478,0.0551] (cpu_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 124, \"Difference 0.024, p=0.0018\", \"0.0244, 0.0018 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# CV permutation (line 129): CV=1.30 vs 2.74, p=0.016\nadd(\"appendix.tex\", 129, \"CV=1.30 vs 2.74, p=0.016\", \"1.3, 2.74, 0.0156 (permutation_test_I2)\", \"✅ 匹配 (rounded)\")\n\n# Dose-response table (lines 150-158)\nadd(\"appendix.tex\", 150, \"4 heads: d=0.482 [0.449,0.511]\", \"0.482 (dose_response_curve)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 151, \"8 heads: d=0.508\", \"dose_response_curve notes\", \"⚠️ 未找到registry记录 (only endpoints in registry)\")\nadd(\"appendix.tex\", 157, \"32 heads: d=0.639 [0.603,0.671]\", \"0.639 (dose_response_curve)\", \"✅ 匹配\")\n\n# Counterfactual table (lines 171-177)\nadd(\"appendix.tex\", 171, \"Empty: d=0.968, 90.7%\", \"0.968 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 172, \"Wrong: d=0.844, 89.5%\", \"0.844 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 173, \"Paraphrased: d=0.697, 82.6%\", \"0.697 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 174, \"Shuffled: d=0.625, 85.7%\", \"0.625 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 176, \"L1 ablation: d=0.650, 72.3%\", \"0.651, 0.723 (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Action shift per dim table (lines 191-193)\nadd(\"appendix.tex\", 191, \"Instruction gripper=0.291\", \"0.2907 (action_trajectory)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 192, \"Control gripper=0.141\", \"0.1407 (action_trajectory_control)\", \"✅ 匹配 (rounded)\")\n\n# Attention decomposition table (lines 605-608)\nadd(\"appendix.tex\", 605, \"Instruction-dom: 62.4% instr, 18.8% vision, 18.8% BOS\", \"62.4% (attention_decomposition)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 606, \"Control: 44.9% instr, 27.1% vision, 28.0% BOS\", \"44.9% (attention_decomposition)\", \"✅ 匹配\")\n\n# Per-dim MAE ratios table (lines 627-633)\nadd(\"appendix.tex\", 627, \"dx ratio 5.09×\", \"5.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 628, \"dy ratio 4.26×\", \"4.3x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 629, \"dz ratio 3.14×\", \"3.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 630, \"roll ratio 2.62×\", \"2.6x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 631, \"pitch ratio 2.21×\", \"2.2x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 632, \"yaw ratio 1.90×\", \"1.9x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 633, \"gripper ratio 2.07×\", \"2.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\n\n# Specificity control table (lines 683-684)\nadd(\"appendix.tex\", 683, \"Top-24 d=0.650, KL=6.50\", \"0.65 (specificity_control)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 684, \"Bottom-24 d=0.565, KL=4.17, ratio 1.15×/1.56×\", \"0.565, 4.166, 1.15/1.56 (specificity_control)\", \"✅ 匹配 (rounded)\")\n\n# Linear probe (lines 217-220)\nadd(\"appendix.tex\", 217, \"Linear trained img_mean peak L14, R²=0.565\", \"L13 for readout (linear_probe_last_preaction). No image_mean linear probe in registry.\", \"⚠️ 未找到registry记录 (linear image_mean)\")\nadd(\"appendix.tex\", 217, \"Linear untrained peak L0, R²=0.517\", \"No linear image_mean untrained in registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 220, \"Linear readout peak L13, R²=0.596\", \"L13, 0.596 (linear_probe_last_preaction)\", \"✅ 匹配\")\n\n# Training effects table (lines 411-422)\nadd(\"appendix.tex\", 412, \"RSA best-vs-best +0.017, n.s.\", \"0.017, n.s. (d041_method_b_rsa)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 414, \"RSA same-layer L12 +0.079, p<0.0001\", \"0.079, p=0.0001 (d041_method_b_rsa)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 419, \"R² best-vs-best img_mean +0.015, p=0.006\", \"0.0149, p=0.006 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 421, \"R² best-vs-best readout +0.069, p<0.0001\", \"0.0686, p=0.0001 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# Training effect summary table (lines 443-448)\nadd(\"appendix.tex\", 443, \"RSA peak img_mean 0.628 (L12) vs 0.612 (L0), +0.017\", \"0.6282 vs 0.6117, +0.017 (d041)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 444, \"R² peak img_mean 0.655 (L8) vs 0.640 (L0), +0.015\", \"0.6553 vs 0.6403, +0.015 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 445, \"R² peak readout 0.678 (L13) vs 0.609 (L32), +0.069\", \"0.6779 vs 0.6093, +0.069 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 448, \"Progress classification 86.3% (L20) vs 85.3% (L4)\", \"86.32 L20 trained, 85.3 from notes (qa_probe)\", \"✅ 匹配 (rounded)\")\n\n# QA probe table (lines 505-508)\nadd(\"appendix.tex\", 505, \"Trained last_preaction L20: 86.3%\", \"86.32% L20 (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 507, \"DINOv2 cls: 82.7%\", \"82.72% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\n\n# Seed sensitivity table (lines 359-365)\nadd(\"appendix.tex\", \"359-364\", \"Seeds 0-42: peaks L9/L16/L9/L10/L9, R²=0.654-0.656\", \n    \"peaks [9,16,9,10,9], R²=[0.6534,0.6549,0.6529,0.6531,0.6587] (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 365, \"Mean±std: 10.6±2.7, 0.655±0.002\", \"10.6±2.73, 0.6546±0.0022 (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\n\n# Demo sensitivity table (lines 387-395)\nadd(\"appendix.tex\", 388, \"RSA peak ρ 50demos=0.628, 25demos=0.606, -3.6%\", \n    \"0.6282, 0.6059 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 390, \"R² peak 50demos=0.659, 25demos=0.609, -7.6%\", \n    \"0.6587, 0.6088 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 391, \"RSA profile r=0.970\", \"0.9696 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 392, \"R² profile r=0.819\", \"0.8189 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\n\n# OOD diagnostics (line 201-203)\nadd(\"appendix.tex\", 201, \"Llama-2 activation 16.5→90.2, VLA 16.5→51.7\", \"No exact registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 202, \"Cosine sim decreases to ~0.28 at L25\", \"No exact registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 203, \"PC variance 0.59--0.74\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Permutation test (line 340): ρ=0.42--0.63, null max 0.08--0.10\nadd(\"appendix.tex\", 340, \"Observed ρ 0.42--0.63, null max 0.08--0.10\", \"No exact values in registry\", \"⚠️ 未找到registry记录\")\n\n# Per-DOF RSA (line 334): xyz peak L13 ρ=0.193, rotation L12 ρ=0.175, gripper L13 ρ=0.106\nadd(\"appendix.tex\", 334, \"xyz L13 ρ=0.193, rotation L12 ρ=0.175, gripper L13 ρ=0.106\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Metric invariance (line 312): Pearson r > 0.989\nadd(\"appendix.tex\", 312, \"Profile r > 0.989\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Spatial cross-instruction table (lines 298-301)\nadd(\"appendix.tex\", 298, \"Spatial trained L1=98.9%, L4-L31=100%\", \"L1=0.989, L4+=1.0 (cross_inst_spatial)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 299, \"Spatial untrained L1=99.5%, L31=75.4%\", \"L1=0.995, L31=0.754 (cross_inst_spatial)\", \"✅ 匹配\")\n\n# Print results\nmatch = sum(1 for r in rows if r[3].startswith(\"✅\"))\nmismatch = sum(1 for r in rows if r[3].startswith(\"❌\"))\nunverified = sum(1 for r in rows if r[3].startswith(\"⚠️\"))\n\nprint(f\"\\n## Summary\")\nprint(f\"- ✅ 匹配: {match}\")\nprint(f\"- ❌ 不匹配: {mismatch}\")\nprint(f\"- ⚠️ 未找到registry记录: {unverified}\")\nprint(f\"- Total: {len(rows)}\")\nprint()\n\n# Print mismatches first\nprint(\"## MISMATCHES\")\nfor r in rows:\n    if r[3].startswith(\"❌\"):\n        print(f\"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |\")\nprint()\n\nprint(\"## FULL TABLE\")\nprint(\"| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\")\nprint(\"|---|---|---|---|\")\nfor r in rows:\n    print(f\"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |\")\n\nPYEOF",
  "description": "Build comprehensive cross-validation table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\n# Comprehensive cross-validation\n\nrows = []\n\ndef add(file, line, paper_val, registry_val, status):\n    rows.append((f\"{file}:{line}\", paper_val, registry_val, status))\n\n# ===== ABSTRACT (abstract.tex) =====\n# Line 4: 100% instruction classification\nadd(\"abstract.tex\", 4, \"100%\", \"100% (lg_gc_trained L1+)\", \"✅ 匹配\")\n\n# Line 6: d=0.48→0.64 dose-response\nadd(\"abstract.tex\", 6, \"d=0.48→0.64\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配 (rounded)\")\n\n# Line 6: d=0.63--0.97 counterfactual\nadd(\"abstract.tex\", 6, \"d=0.63--0.97\", \"d=0.625--0.968 (counterfactual_instruction)\", \"✅ 匹配 (rounded)\")\n\n# Line 8: R² +0.069\nadd(\"abstract.tex\", 8, \"R² +0.069\", \"+0.0686 (plan_011_fulllayer_r2)\", \"✅ 匹配 (rounded)\")\n\n# Line 8: +46pp attention\nadd(\"abstract.tex\", 8, \"+46pp attention\", \"57.7%-11.7%=46.0pp (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 8: Δρ ≤ 0.017\nadd(\"abstract.tex\", 8, \"Δρ ≤ 0.017\", \"+0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# ===== INTRODUCTION (introduction.tex) =====\n# Line 17: 100% cross-validated\nadd(\"introduction.tex\", 17, \"100%\", \"100% (lg_gc_trained)\", \"✅ 匹配\")\n\n# Line 18: L9--L16: 15--22 heads (Llama-2 base mid-depth)\nadd(\"introduction.tex\", 18, \"L9--L16: 15--22 heads\", \"Qualitative (multilayer_attention table)\", \"⚠️ 未找到registry记录\")\n\n# Line 18: L0--L1: 21--24 heads, L31: 18 heads\nadd(\"introduction.tex\", 18, \"L0--L1: 21--24 heads, L31: 18\", \"L1: 24/32 (llama2_base_control, but 25 in registry)\", \"❌ 不匹配 (registry=25 vs paper=24)\")\n\n# Line 19: d=0.48→0.64\nadd(\"introduction.tex\", 19, \"d=0.48→0.64\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配 (rounded)\")\n\n# Line 19: d=0.63--0.97\nadd(\"introduction.tex\", 19, \"d=0.63--0.97\", \"d=0.625--0.968 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# Line 20: R² at L8--L14, RSA at L12\nadd(\"introduction.tex\", 20, \"R² peak L8--L14\", \"R² peak L8 image_mean, L13 readout (plan_011)\", \"✅ 匹配\")\nadd(\"introduction.tex\", 20, \"RSA peak L12\", \"L12 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 21: Δρ = 0.017, 3%\nadd(\"introduction.tex\", 21, \"Δρ = 0.017\", \"+0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 21: R² Δ = +0.069, p < 0.0001\nadd(\"introduction.tex\", 21, \"R² Δ = +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# ===== EXPERIMENTS (experiments.tex) =====\n# Line 12: N = 63,228 observations\nadd(\"experiments.tex\", 12, \"N = 63,228\", \"lg_dino_extract: total_frames=63728\", \"❌ 不匹配 (63228 vs 63728)\")\n\n# Line 21: 10% image_mean\nadd(\"experiments.tex\", 21, \"10% image_mean chance\", \"10% (lg_gc_trained L0, cross_inst)\", \"✅ 匹配\")\n\n# Line 22: DINOv2 10%\nadd(\"experiments.tex\", 22, \"DINOv2 10%\", \"DINOv2 at chance (consistent)\", \"✅ 匹配\")\n\n# Line 25: 100% L1-L31 trained readout, 82% untrained L31\nadd(\"experiments.tex\", 25, \"100% L1-L31 trained\", \"100% (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 25, \"82% untrained L31\", \"0.82 (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 26: QA 86.3% vs 82.7%\nadd(\"experiments.tex\", 26, \"86.3% QA trained\", \"86.32% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 26, \"82.7% DINOv2 QA\", \"82.72% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\n\n# Table tab:dense_routing_main (lines 37-42)\nadd(\"experiments.tex\", 37, \"L0: 10.0% / 10.0% / 10.0%\", \"Consistent with lg_gc data\", \"✅ 匹配\")\nadd(\"experiments.tex\", 38, \"L1: 100.0% / 100.0% / 10.0%\", \"llama2_base_control: trained=1.0, untrained=1.0\", \"✅ 匹配\")\nadd(\"experiments.tex\", 40, \"L8: 100.0% / 95.5% / 10.0%\", \"llama2_base_control: untrained L8=0.986\", \"❌ 不匹配 (paper=95.5% vs registry=98.6%)\")\nadd(\"experiments.tex\", 41, \"L16: 100.0% / 91.1% / 10.0%\", \"llama2_base_control: untrained L16=0.92\", \"❌ 不匹配 (paper=91.1% vs registry=92.0%)\")\nadd(\"experiments.tex\", 42, \"L31: 100.0% / 82.0% / 10.0%\", \"llama2_base_control: untrained L31=0.82\", \"✅ 匹配\")\n\n# Line 52: 0/32, 9/32, 24/32 heads; 11.7%, 36.5%, 57.7%\nadd(\"experiments.tex\", 52, \"untrained 0/32 (11.7%)\", \"0 heads, 0.117 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 52, \"Llama-2 9/32 (36.5%)\", \"9 heads, 0.365 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 52, \"VLA 24/32 (57.7%)\", \"25 heads, 0.577 (llama2_base_control)\", \"❌ 不匹配 (heads: paper=24 vs registry=25)\")\n\n# Line 60: 99.6% VLA at L1, 80.2% Llama-2 at L1\nadd(\"experiments.tex\", 60, \"VLA 99.6% at L1\", \"0.996 (llama2_base_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 60, \"Llama-2 80.2% at L1\", \"0.802 (llama2_base_control)\", \"✅ 匹配\")\n\n# Line 61: R² +0.069, attention +46pp, Δ ≤ 1.7%\nadd(\"experiments.tex\", 61, \"R² +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 61, \"+46pp attention\", \"46.0pp (57.7%-11.7%)\", \"✅ 匹配\")\n\n# Line 65: +0.042 (baseline 0.517)\nadd(\"experiments.tex\", 65, \"+0.042 (baseline 0.517)\", \"0.042 / 0.517 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Line 66: +0.077 ± 0.013, z=-2.73, p=0.003\nadd(\"experiments.tex\", 66, \"+0.077 ± 0.013\", \"0.077 ± 0.013 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 66, \"z=-2.73, p=0.003\", \"-2.73, 0.003 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Line 68: +0.059 L1, +0.018 L8, ~0 L13\nadd(\"experiments.tex\", 68, \"+0.059 L1 ablation\", \"0.0585 (ablation_50demos_main)\", \"✅ 匹配 (rounded)\")\n\n# Line 71: 72.3% d=0.65, d=0.41 (29.3%), 0.291 vs <0.034\nadd(\"experiments.tex\", 71, \"72.3% token div, d=0.65\", \"0.723, 0.651 (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 71, \"d=0.41 (29.3%)\", \"0.41, 0.293 (action_trajectory_control)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 71, \"gripper 0.291 vs <0.034\", \"0.2907 vs 0.0339 max rotation (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Line 74: d=0.482→0.639\nadd(\"experiments.tex\", 74, \"d=0.482→0.639\", \"d=0.482→0.639 (dose_response_curve)\", \"✅ 匹配\")\n\n# Line 78: empty 0.968, wrong 0.844, paraphrased 0.697, shuffled 0.625\nadd(\"experiments.tex\", 78, \"empty d=0.968\", \"0.968 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"wrong d=0.844\", \"0.844 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"paraphrased d=0.697\", \"0.697 (counterfactual)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 78, \"shuffled d=0.625\", \"0.625 (counterfactual)\", \"✅ 匹配\")\n\n# Line 80: L1 ablation d=0.65\nadd(\"experiments.tex\", 80, \"L1 ablation d=0.65\", \"0.651 (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Table routing_gradient (lines 91-93)\nadd(\"experiments.tex\", 91, \"VLA: 24/32, 57.7%, 99.6%, 100%\", \"Registry: 25/32 heads\", \"❌ 不匹配 (heads: 24 vs 25)\")\nadd(\"experiments.tex\", 92, \"Llama-2: 9/32, 36.5%, 80.2%, 100%\", \"Registry: 9/32, 0.365, 0.802, 1.0\", \"✅ 匹配\")\nadd(\"experiments.tex\", 93, \"Untrained: 0/32, 11.7%, 100%, 82%\", \"Registry: 0/32, 0.117, 1.0, 0.82\", \"✅ 匹配\")\n\n# Line 111: DINOv2 ρ=0.692, VLA peak 0.628 at L12, CLIP 0.557\nadd(\"experiments.tex\", 111, \"DINOv2 ρ=0.692\", \"0.6915 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 111, \"VLA peak 0.628 at L12\", \"0.6282 at L12 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 111, \"CLIP 0.557\", \"0.557 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 114: 0.655 ± 0.002 (seed sensitivity)\nadd(\"experiments.tex\", 114, \"0.655 ± 0.002\", \"0.6546 ± 0.0022 (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\n\n# Line 115: readout R²=0.678 (L13), Δ=0.048 from projector\nadd(\"experiments.tex\", 115, \"readout R²=0.678 at L13\", \"0.6779 at L13 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 115, \"Δ=0.048 from projector\", \"0.6779 - 0.6298 = 0.0481 (plan_011 vs plan_012)\", \"✅ 匹配 (rounded)\")\n\n# Line 119: Δρ=0.017, 3%\nadd(\"experiments.tex\", 119, \"Δρ=0.017, 3%\", \"0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Line 120: readout R² +0.069, p<0.0001, CI [0.047,0.090]\nadd(\"experiments.tex\", 120, \"readout R² +0.069\", \"+0.0686 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 120, \"image_mean +0.015, p=0.006\", \"+0.0149, p=0.006 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# Table rsa_overview (lines 132-143)\nadd(\"experiments.tex\", 132, \"DINOv2 cls RSA=0.692, R²=0.634\", \"RSA=0.6915, R²=0.6343 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 133, \"VLA readout RSA=0.643, R²=0.678\", \"RSA=0.6425, R²=0.6779 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 134, \"Fused DinoSigLIP RSA=0.634\", \"0.634 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"experiments.tex\", 135, \"VLA img_mean RSA=0.628, R²=0.655\", \"RSA=0.6282, R²=0.6553 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 136, \"Projector RSA=0.615, R²=0.630\", \"RSA=0.615, R²=0.6298 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 137, \"Untrained img_mean RSA=0.612, R²=0.640\", \"RSA=0.6117, R²=0.6403 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 138, \"Untrained readout RSA=0.626, R²=0.609\", \"RSA=0.6262, R²=0.6093 (d041/plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"experiments.tex\", 139, \"CLIP RSA=0.557, R²=0.587\", \"RSA=0.557, R²=0.5866 (d041/plan_012)\", \"✅ 匹配 (rounded)\")\n\n# Figure layer_curves (line 149): L0 0.612 → L12 0.628 → L32 0.422\nadd(\"experiments.tex\", 149, \"L0 0.612→L12 0.628→L32 0.422\", \"L0=0.6117, L12=0.6282 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\n\n# ===== DISCUSSION (discussion.tex) =====\n# Line 5: R² +0.069, +46pp, Δ ≤ 1.7%\nadd(\"discussion.tex\", 5, \"R² +0.069, +46pp\", \"Consistent with above\", \"✅ 匹配\")\n\n# Line 6: ρ=0.692, R²=0.678 vs 0.634\nadd(\"discussion.tex\", 6, \"ρ=0.692, R²=0.678 vs 0.634\", \"0.6915, 0.6779 vs 0.6343\", \"✅ 匹配 (rounded)\")\n\n# Line 8: 0→9→24 heads\nadd(\"discussion.tex\", 8, \"0→9→24 heads\", \"Registry: 0, 9, 25 heads\", \"❌ 不匹配 (VLA heads: 24 vs 25)\")\n\n# Line 9: +0.059 L1, ~0 L13\nadd(\"discussion.tex\", 9, \"+0.059 at L1\", \"0.0585 (ablation_50demos_main)\", \"✅ 匹配 (rounded)\")\n\n# Line 10: d=0.65, 72.3%\nadd(\"discussion.tex\", 10, \"d=0.65, 72.3%\", \"0.651, 0.723\", \"✅ 匹配 (rounded)\")\n\n# Line 11: d=0.48→0.64\nadd(\"discussion.tex\", 11, \"d=0.48→0.64\", \"0.482→0.639\", \"✅ 匹配 (rounded)\")\n\n# Line 12: d=0.63--0.97\nadd(\"discussion.tex\", 12, \"d=0.63--0.97\", \"0.625--0.968\", \"✅ 匹配 (rounded)\")\n\n# Line 13: p=0.002 bootstrap CIs\nadd(\"discussion.tex\", 13, \"p=0.002\", \"p=0.0018 (action_trajectory_cpu_analysis)\", \"❌ 不匹配 (0.002 vs 0.0018)\")\n\n# Line 14: p=0.016 CV permutation\nadd(\"discussion.tex\", 14, \"p=0.016\", \"cv_exact_paired_p=0.0156 (permutation_test_I2)\", \"✅ 匹配 (rounded)\")\n\n# Line 17: d=0.051 vs 0.027\nadd(\"discussion.tex\", 17, \"d=0.051 vs 0.027\", \"0.0514 vs 0.0271 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Line 18: d=0.57 vs 0.65 (bottom-24 vs top-24)\nadd(\"discussion.tex\", 18, \"d=0.57 vs 0.65\", \"0.565 vs 0.65 (specificity_control)\", \"❌ 不匹配 (paper=0.57 vs registry=0.565)\")\n\n# Line 18: KL ratio 1.56x\nadd(\"discussion.tex\", 18, \"KL ratio 1.56×\", \"6.50/4.166 = 1.56 (specificity_control)\", \"✅ 匹配\")\n\n# Line 20: d=0.70 paraphrased\nadd(\"discussion.tex\", 20, \"d=0.70 paraphrased\", \"0.697 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# Line 20: d=0.63 shuffled\nadd(\"discussion.tex\", 20, \"d=0.63 shuffled\", \"0.625 (counterfactual)\", \"✅ 匹配 (rounded)\")\n\n# ===== APPENDIX (appendix.tex) =====\n# CKA values (lines 21-22)\nadd(\"appendix.tex\", 21, \"Linear CKA: untrained=0.089, trained=0.083, proj=0.081, DINOv2=0.066\", \n    \"0.0894, 0.0834, 0.0809, 0.0664 (plan_009_cka)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 22, \"RDM CKA: trained=0.260, proj=0.257, untrained=0.246, DINOv2=0.241\",\n    \"0.2599, 0.2568, 0.2464, 0.2408 (plan_009_cka)\", \"✅ 匹配 (rounded)\")\n\n# Line 25: linear CKA L0=0.081, L32=0.098\nadd(\"appendix.tex\", 25, \"linear CKA L0=0.081→L32=0.098\", \"L0=0.0809 (plan_009_cka, projector)\", \"⚠️ 未找到registry记录 (per-layer CKA)\")\n\n# Branch split (lines 40-42)\nadd(\"appendix.tex\", 40, \"DINOv2 branch ρ=0.619, SigLIP ρ=0.621\", \"0.619, 0.621 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 41, \"Fused ρ=0.634\", \"0.634 (plan_013_branch_split)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 42, \"Projector ρ=0.615, Δ=0.019\", \"0.615 (plan_013). 0.634-0.615=0.019\", \"✅ 匹配\")\n\n# DINOv2 patch_mean (line 258)\nadd(\"appendix.tex\", 258, \"DINOv2 patch_mean ρ=0.631\", \"0.6307 (d041_method_b_rsa dino_patch_mean)\", \"✅ 匹配 (rounded)\")\n\n# Untrained readout peak L1 ρ=0.626 (line 259)\nadd(\"appendix.tex\", 259, \"Untrained readout peak L1 ρ=0.626\", \"0.6262 at L1 (d041_method_b_rsa)\", \"✅ 匹配 (rounded)\")\n\n# LIBERO-Spatial (lines 267-268)\nadd(\"appendix.tex\", 267, \"Spatial RSA peak L14 ρ=0.691, R² L13 0.696\", \"L14: 0.6911, L13: 0.6963 (plan_010)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 268, \"Spatial Δ=+0.023, p<0.001\", \"0.023, p=0.001 (plan_010_libero_spatial)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 268, \"Goal Δ=+0.017\", \"0.017 (d041_method_b_rsa)\", \"✅ 匹配\")\n\n# Spatial cross-instruction (line 287): 75.4% L31\nadd(\"appendix.tex\", 287, \"untrained 75.4% L31 Spatial\", \"0.754 L31 (cross_inst_spatial_trained)\", \"✅ 匹配\")\n\n# Three-condition R² (lines 70-72)\nadd(\"appendix.tex\", 70, \"L0 R²=0.645±0.008\", \"0.645±0.008 (threecond_multiseed_v2)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 71, \"Trained peak L9 R²=0.643±0.014\", \"L9, 0.643±0.014 (threecond_multiseed_v2)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 72, \"Llama-2 base L0:0.645→L32:0.551\", \"L0=0.645 (threecond). L32=0.551 from notes\", \"✅ 匹配\")\n\n# Random subset ablation (lines 88-89)\nadd(\"appendix.tex\", 88, \"+0.042 (baseline 0.517)\", \"0.042, 0.517 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 88, \"+0.077 ± 0.013\", \"0.077±0.013 (random_subset_ablation)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 89, \"z=-2.73, p=0.003\", \"-2.73, 0.003 (random_subset_ablation)\", \"✅ 匹配\")\n\n# Per-task Cohen's d (line 105): 0.43, 0.69, 0.70, 0.70, 0.73 (mean 0.65)\nadd(\"appendix.tex\", 105, \"Per-task d: 0.43-0.73, mean 0.65\", \"range [0.433, 0.729] (action_trajectory_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Token-level KL (line 106): 5.08 instruction, 1.69 control\nadd(\"appendix.tex\", 106, \"KL instruction=5.08, control=1.69\", \"5.079, 1.69 (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Per-head bootstrap (lines 109-110)\nadd(\"appendix.tex\", 109, \"control d=0.051, instruction d=0.027, p=0.0018\", \"0.0514, 0.0271, 0.0018 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# Per-head bootstrap table (lines 121-124)\nadd(\"appendix.tex\", 121, \"Instruction: 24 heads, collective d=0.65, per-head d=0.027 [0.026,0.029]\",\n    \"24h, 0.65, 0.0271 [0.0258,0.0285] (cpu_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 122, \"Control: 8 heads, collective d=0.41, per-head d=0.051 [0.048,0.055]\",\n    \"8h, 0.41, 0.0514 [0.0478,0.0551] (cpu_analysis)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 124, \"Difference 0.024, p=0.0018\", \"0.0244, 0.0018 (cpu_analysis)\", \"✅ 匹配 (rounded)\")\n\n# CV permutation (line 129): CV=1.30 vs 2.74, p=0.016\nadd(\"appendix.tex\", 129, \"CV=1.30 vs 2.74, p=0.016\", \"1.3, 2.74, 0.0156 (permutation_test_I2)\", \"✅ 匹配 (rounded)\")\n\n# Dose-response table (lines 150-158)\nadd(\"appendix.tex\", 150, \"4 heads: d=0.482 [0.449,0.511]\", \"0.482 (dose_response_curve)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 151, \"8 heads: d=0.508\", \"dose_response_curve notes\", \"⚠️ 未找到registry记录 (only endpoints in registry)\")\nadd(\"appendix.tex\", 157, \"32 heads: d=0.639 [0.603,0.671]\", \"0.639 (dose_response_curve)\", \"✅ 匹配\")\n\n# Counterfactual table (lines 171-177)\nadd(\"appendix.tex\", 171, \"Empty: d=0.968, 90.7%\", \"0.968 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 172, \"Wrong: d=0.844, 89.5%\", \"0.844 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 173, \"Paraphrased: d=0.697, 82.6%\", \"0.697 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 174, \"Shuffled: d=0.625, 85.7%\", \"0.625 (counterfactual)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 176, \"L1 ablation: d=0.650, 72.3%\", \"0.651, 0.723 (action_trajectory)\", \"✅ 匹配 (rounded)\")\n\n# Action shift per dim table (lines 191-193)\nadd(\"appendix.tex\", 191, \"Instruction gripper=0.291\", \"0.2907 (action_trajectory)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 192, \"Control gripper=0.141\", \"0.1407 (action_trajectory_control)\", \"✅ 匹配 (rounded)\")\n\n# Attention decomposition table (lines 605-608)\nadd(\"appendix.tex\", 605, \"Instruction-dom: 62.4% instr, 18.8% vision, 18.8% BOS\", \"62.4% (attention_decomposition)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 606, \"Control: 44.9% instr, 27.1% vision, 28.0% BOS\", \"44.9% (attention_decomposition)\", \"✅ 匹配\")\n\n# Per-dim MAE ratios table (lines 627-633)\nadd(\"appendix.tex\", 627, \"dx ratio 5.09×\", \"5.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 628, \"dy ratio 4.26×\", \"4.3x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 629, \"dz ratio 3.14×\", \"3.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 630, \"roll ratio 2.62×\", \"2.6x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 631, \"pitch ratio 2.21×\", \"2.2x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 632, \"yaw ratio 1.90×\", \"1.9x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 633, \"gripper ratio 2.07×\", \"2.1x (action_metrics_extended)\", \"✅ 匹配 (rounded)\")\n\n# Specificity control table (lines 683-684)\nadd(\"appendix.tex\", 683, \"Top-24 d=0.650, KL=6.50\", \"0.65 (specificity_control)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 684, \"Bottom-24 d=0.565, KL=4.17, ratio 1.15×/1.56×\", \"0.565, 4.166, 1.15/1.56 (specificity_control)\", \"✅ 匹配 (rounded)\")\n\n# Linear probe (lines 217-220)\nadd(\"appendix.tex\", 217, \"Linear trained img_mean peak L14, R²=0.565\", \"L13 for readout (linear_probe_last_preaction). No image_mean linear probe in registry.\", \"⚠️ 未找到registry记录 (linear image_mean)\")\nadd(\"appendix.tex\", 217, \"Linear untrained peak L0, R²=0.517\", \"No linear image_mean untrained in registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 220, \"Linear readout peak L13, R²=0.596\", \"L13, 0.596 (linear_probe_last_preaction)\", \"✅ 匹配\")\n\n# Training effects table (lines 411-422)\nadd(\"appendix.tex\", 412, \"RSA best-vs-best +0.017, n.s.\", \"0.017, n.s. (d041_method_b_rsa)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 414, \"RSA same-layer L12 +0.079, p<0.0001\", \"0.079, p=0.0001 (d041_method_b_rsa)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 419, \"R² best-vs-best img_mean +0.015, p=0.006\", \"0.0149, p=0.006 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 421, \"R² best-vs-best readout +0.069, p<0.0001\", \"0.0686, p=0.0001 (plan_011)\", \"✅ 匹配 (rounded)\")\n\n# Training effect summary table (lines 443-448)\nadd(\"appendix.tex\", 443, \"RSA peak img_mean 0.628 (L12) vs 0.612 (L0), +0.017\", \"0.6282 vs 0.6117, +0.017 (d041)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 444, \"R² peak img_mean 0.655 (L8) vs 0.640 (L0), +0.015\", \"0.6553 vs 0.6403, +0.015 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 445, \"R² peak readout 0.678 (L13) vs 0.609 (L32), +0.069\", \"0.6779 vs 0.6093, +0.069 (plan_011)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 448, \"Progress classification 86.3% (L20) vs 85.3% (L4)\", \"86.32 L20 trained, 85.3 from notes (qa_probe)\", \"✅ 匹配 (rounded)\")\n\n# QA probe table (lines 505-508)\nadd(\"appendix.tex\", 505, \"Trained last_preaction L20: 86.3%\", \"86.32% L20 (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 507, \"DINOv2 cls: 82.7%\", \"82.72% (qa_probe_classification)\", \"✅ 匹配 (rounded)\")\n\n# Seed sensitivity table (lines 359-365)\nadd(\"appendix.tex\", \"359-364\", \"Seeds 0-42: peaks L9/L16/L9/L10/L9, R²=0.654-0.656\", \n    \"peaks [9,16,9,10,9], R²=[0.6534,0.6549,0.6529,0.6531,0.6587] (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 365, \"Mean±std: 10.6±2.7, 0.655±0.002\", \"10.6±2.73, 0.6546±0.0022 (ablation_p1_seed)\", \"✅ 匹配 (rounded)\")\n\n# Demo sensitivity table (lines 387-395)\nadd(\"appendix.tex\", 388, \"RSA peak ρ 50demos=0.628, 25demos=0.606, -3.6%\", \n    \"0.6282, 0.6059 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 390, \"R² peak 50demos=0.659, 25demos=0.609, -7.6%\", \n    \"0.6587, 0.6088 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 391, \"RSA profile r=0.970\", \"0.9696 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\nadd(\"appendix.tex\", 392, \"R² profile r=0.819\", \"0.8189 (ablation_p2_demo_sensitivity_v2)\", \"✅ 匹配 (rounded)\")\n\n# OOD diagnostics (line 201-203)\nadd(\"appendix.tex\", 201, \"Llama-2 activation 16.5→90.2, VLA 16.5→51.7\", \"No exact registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 202, \"Cosine sim decreases to ~0.28 at L25\", \"No exact registry\", \"⚠️ 未找到registry记录\")\nadd(\"appendix.tex\", 203, \"PC variance 0.59--0.74\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Permutation test (line 340): ρ=0.42--0.63, null max 0.08--0.10\nadd(\"appendix.tex\", 340, \"Observed ρ 0.42--0.63, null max 0.08--0.10\", \"No exact values in registry\", \"⚠️ 未找到registry记录\")\n\n# Per-DOF RSA (line 334): xyz peak L13 ρ=0.193, rotation L12 ρ=0.175, gripper L13 ρ=0.106\nadd(\"appendix.tex\", 334, \"xyz L13 ρ=0.193, rotation L12 ρ=0.175, gripper L13 ρ=0.106\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Metric invariance (line 312): Pearson r > 0.989\nadd(\"appendix.tex\", 312, \"Profile r > 0.989\", \"No exact registry\", \"⚠️ 未找到registry记录\")\n\n# Spatial cross-instruction table (lines 298-301)\nadd(\"appendix.tex\", 298, \"Spatial trained L1=98.9%, L4-L31=100%\", \"L1=0.989, L4+=1.0 (cross_inst_spatial)\", \"✅ 匹配\")\nadd(\"appendix.tex\", 299, \"Spatial untrained L1=99.5%, L31=75.4%\", \"L1=0.995, L31=0.754 (cross_inst_spatial)\", \"✅ 匹配\")\n\n# Print results\nmatch = sum(1 for r in rows if r[3].startswith(\"✅\"))\nmismatch = sum(1 for r in rows if r[3].startswith(\"❌\"))\nunverified = sum(1 for r in rows if r[3].startswith(\"⚠️\"))\n\nprint(f\"\\n## Summary\")\nprint(f\"- ✅ 匹配: {match}\")\nprint(f\"- ❌ 不匹配: {mismatch}\")\nprint(f\"- ⚠️ 未找到registry记录: {unverified}\")\nprint(f\"- Total: {len(rows)}\")\nprint()\n\n# Print mismatches first\nprint(\"## MISMATCHES\")\nfor r in rows:\n    if r[3].startswith(\"❌\"):\n        print(f\"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |\")\nprint()\n\nprint(\"## FULL TABLE\")\nprint(\"| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\")\nprint(\"|---|---|---|---|\")\nfor r in rows:\n    print(f\"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |\")\n\nPYEOF",
    "description": "Build comprehensive cross-validation table"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-18T19:33:45.241898+00:00_

## Summary
- ✅ 匹配: 135
- ❌ 不匹配: 9
- ⚠️ 未找到registry记录: 11
- Total: 155

## MISMATCHES
| introduction.tex:18 | L0--L1: 21--24 heads, L31: 18 | L1: 24/32 (llama2_base_control, but 25 in registry) | ❌ 不匹配 (registry=25 vs paper=24) |
| experiments.tex:12 | N = 63,228 | lg_dino_extract: total_frames=63728 | ❌ 不匹配 (63228 vs 63728) |
| experiments.tex:40 | L8: 100.0% / 95.5% / 10.0% | llama2_base_control: untrained L8=0.986 | ❌ 不匹配 (paper=95.5% vs registry=98.6%) |
| experiments.tex:41 | L16: 100.0% / 91.1% / 10.0% | llama2_base_control: untrained L16=0.92 | ❌ 不匹配 (paper=91.1% vs registry=92.0%) |
| experiments.tex:52 | VLA 24/32 (57.7%) | 25 heads, 0.577 (llama2_base_control) | ❌ 不匹配 (heads: paper=24 vs registry=25) |
| experiments.tex:91 | VLA: 24/32, 57.7%, 99.6%, 100% | Registry: 25/32 heads | ❌ 不匹配 (heads: 24 vs 25) |
| discussion.tex:8 | 0→9→24 heads | Registry: 0, 9, 25 heads | ❌ 不匹配 (VLA heads: 24 vs 25) |
| discussion.tex:13 | p=0.002 | p=0.0018 (action_trajectory_cpu_analysis) | ❌ 不匹配 (0.002 vs 0.0018) |
| discussion.tex:18 | d=0.57 vs 0.65 | 0.565 vs 0.65 (specificity_control) | ❌ 不匹配 (paper=0.57 vs registry=0.565) |

## FULL TABLE
| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |
|---|---|---|---|
| abstract.tex:4 | 100% | 100% (lg_gc_trained L1+) | ✅ 匹配 |
| abstract.tex:6 | d=0.48→0.64 | d=0.482→0.639 (dose_response_curve) | ✅ 匹配 (rounded) |
| abstract.tex:6 | d=0.63--0.97 | d=0.625--0.968 (counterfactual_instruction) | ✅ 匹配 (rounded) |
| abstract.tex:8 | R² +0.069 | +0.0686 (plan_011_fulllayer_r2) | ✅ 匹配 (rounded) |
| abstract.tex:8 | +46pp attention | 57.7%-11.7%=46.0pp (llama2_base_control) | ✅ 匹配 |
| abstract.tex:8 | Δρ ≤ 0.017 | +0.017 (d041_method_b_rsa) | ✅ 匹配 |
| introduction.tex:17 | 100% | 100% (lg_gc_trained) | ✅ 匹配 |
| introduction.tex:18 | L9--L16: 15--22 heads | Qualitative (multilayer_attention table) | ⚠️ 未找到registry记录 |
| introduction.tex:18 | L0--L1: 21--24 heads, L31: 18 | L1: 24/32 (llama2_base_control, but 25 in registry) | ❌ 不匹配 (registry=25 vs
…[truncated 14744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-18T19:33:45.242305+00:00_

Here is the complete cross-validation report.

---

## Summary

| 状态 | 数量 |
|---|---|
| ✅ 匹配 | 135 |
| ❌ 不匹配 | 9 |
| ⚠️ 未找到registry记录 | 11 |
| **Total** | **155** |

---

## Mismatches requiring attention

| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |
|---|---|---|---|
| introduction.tex:18 | L0--L1: 21--24 heads, L31: 18 | L1: 24/32 (llama2_base_control, but registry `l1_heads_gt50pct.trained` = **25**) | ❌ 不匹配 (registry=25 vs paper=24) |
| experiments.tex:12 | N = 63,228 | lg_dino_extract: total_frames = **63728** | ❌ 不匹配 (63228 vs 63728) |
| experiments.tex:40 | L8 untrained readout: 95.5% | llama2_base_control: `dense_probe_L8_acc` untrained = **0.986** (98.6%) | ❌ 不匹配 (95.5% vs 98.6%) |
| experiments.tex:41 | L16 untrained readout: 91.1% | llama2_base_control: `dense_probe_L16_acc` untrained = **0.920** (92.0%) | ❌ 不匹配 (91.1% vs 92.0%) |
| experiments.tex:52 | VLA 24/32 heads (57.7%) | llama2_base_control: `l1_heads_gt50pct.trained` = **25** | ❌ 不匹配 (24 vs 25) |
| experiments.tex:91 | VLA: 24/32 heads | Same as above, registry says **25/32** | ❌ 不匹配 (24 vs 25) |
| discussion.tex:8 | 0 -> 9 -> 24 heads | Registry: 0, 9, **25** | ❌ 不匹配 (24 vs 25) |
| discussion.tex:13 | p = 0.002 (bootstrap CIs) | `task_paired_t.p` = **0.0018** | ❌ 不匹配 (0.002 vs 0.0018, incorrect rounding) |
| discussion.tex:18 | bottom-24 d = 0.57 | specificity_control: `bottom24_d` = **0.565** | ❌ 不匹配 (0.57 vs 0.565, should be 0.57 rounds from 0.565 which is actually 0.57 at 2 sig figs -- borderline) |

### Analysis of mismatches

1. **VLA L1 instruction-dominant heads: 24 vs 25** (appears 4 times across introduction.tex, experiments.tex, discussion.tex). The registry `llama2_base_control` records `l1_heads_gt50pct.trained = 25`. The paper consistently says 24/32. This is a systematic discrepancy likely due to the 50% threshold being borderline for one head. The appendix threshold sensitivity table (appendix.tex line 583) also says 24 at 50%, so this may reflect different extraction runs or slig
…[truncated 2036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Agent",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-18T19:33:45.242635+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-18T19:33:45.242859+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-18T19:33:45.244157+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/paper_consistency_report.md",
  "content": "# 论文全文一致性检查报告\n\n检查时间: 2026-05-18\n论文路径: `docs/paper/`\n\n## 1. 数值一致性\n\n**总计: 155 个数值, 135 匹配, 9 不匹配, 11 未找到 registry 记录**\n\n### 不匹配项\n\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n| introduction.tex:18 | L1: 24 heads | `l1_heads_gt50pct.trained` = **25** | ❌ 不匹配 |\n| experiments.tex:12 | N = 63,228 | `lg_dino_extract.total_frames` = **63,728** | ❌ 不匹配 |\n| experiments.tex:40 | L8 untrained readout: 95.5% | `dense_probe_L8_acc` untrained = **98.6%** | ❌ 不匹配 |\n| experiments.tex:41 | L16 untrained readout: 91.1% | `dense_probe_L16_acc` untrained = **92.0%** | ❌ 不匹配 |\n| experiments.tex:52 | VLA 24/32 heads (57.7%) | registry = **25/32** | ❌ 不匹配 |\n| experiments.tex:91 | VLA: 24/32 heads | registry = **25/32** | ❌ 不匹配 |\n| discussion.tex:8 | 0 → 9 → 24 heads | registry = 0, 9, **25** | ❌ 不匹配 |\n| discussion.tex:13 | p = 0.002 (bootstrap CIs) | `task_paired_t.p` = **0.0018** | ❌ 不匹配 (rounding imprecise) |\n| discussion.tex:18 | bottom-24 d = 0.57 | `bottom24_d` = **0.565** | ❌ 不匹配 (borderline rounding) |\n\n### 分析\n\n1. **L1 heads 24 vs 25** — 系统性问题，出现 4 次 (introduction, experiments×2, discussion)。需确认 50% 阈值下的正确 head 数量并全文统一。\n2. **N = 63,228 vs 63,728** — 500 帧差异，需核实数据提取记录。\n3. **Untrained readout L8/L16** — 论文 95.5%/91.1% vs registry 98.6%/92.0%。可能来自不同 probe run，appendix Table `tab:dense_routing` 与正文一致 (95.5%)，但与 registry 不一致。需确认哪个是最终结果。\n4. **p = 0.002 vs 0.0018** — 精度损失。建议用准确值 0.0018 或写 \"p < 0.002\"。\n5. **bottom-24 d = 0.57 vs 0.565** — 四舍五入边界。appendix 用 0.565，discussion 用 0.57。建议统一精度。\n\n### 未找到 registry 记录 (11 项)\n\n主要来自 appendix 中的 robustness 分析 (OOD diagnostics, permutation tests, per-DOF RSA, metric invariance) 和 Llama-2 base mid-depth attention profile，可能是本地计算未录入 registry。\n\n---\n\n## 2. 措辞问题\n\n**总计: 8 处需修改**\n\n### 残留强 claim (4 处)\n\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n| abstract.tex:4 | \"the readout token serves as the **sole** multimodal convergence point\" | 残留强claim | → \"the **primary** multimodal convergence point\" |\n| related_work.tex:25 | \"identify the readout token as the **sole** multimodal integration site\" | 残留强claim | → \"the **primary** multimodal integration site\" |\n| related_work.tex:29 | \"the readout token serves as the **exclusive** multimodal hub\" | 残留强claim | → \"the **primary** multimodal hub\" |\n| experiments.tex:26 | \"The readout is thus the **sole** locus of multimodal integration\" | 残留强claim | → \"the **primary** locus of multimodal integration\" |\n\n### AI 写作标志 — -ing 分词句尾 (4 处)\n\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n| conclusion.tex:4 | \"...revealing that VLA fine-tuning primarily reorganizes...\" | AI写作-ing | 拆为两句: \"...VLA representations. The analysis reveals that...\" |\n| appendix.tex:72 | \"...indicating stable but unspecialized processing.\" | AI写作-ing | → \"). This indicates stable but unspecialized processing.\" |\n| appendix.tex:461 | \"...indicating that deep-layer stability derives from...\" | AI写作-ing | → \"; this indicates that deep-layer stability...\" |\n| appendix.tex:620 | \"...indicating instruction-dominant heads have disproportionate influence...\" | AI写作-ing | → \"; instruction-dominant heads thus have disproportionate...\" |\n\n### 已清理确认 (无问题)\n\n- em-dash (—): **0** 处\n- 解释性 en-dash ( – ): **0** 处\n- \"Furthermore\"/\"Moreover\"/\"Additionally\" 序列: **0** 处\n- \"It is worth noting\"/\"Notably\": **0** 处\n- 黑名单用词 (delve/leverage/utilize/facilitate/myriad/plethora): **0** 处\n- \"uniquely responsible\"/\"exclusively\"/\"solely driven\"/\"only instruction heads\": **0** 处\n\n### 新叙事关键词确认\n\n| 关键词 | 出现位置 |\n|---|---|\n| \"graded\" | appendix.tex:676 (\"graded, attention-ordered contribution to routing\") |\n| \"distributed\" | method.tex:4 (\"how action-relevant structure is distributed across a VLA\") |\n| \"primarily\" | conclusion.tex:4, discussion.tex:5, appendix.tex:432 |\n| \"the primary\" | abstract.tex:8, introduction.tex:21, introduction.tex:23, conclusion.tex:5 |\n\n**注**: \"preferentially\" 和 \"predominantly\" 未出现，当前叙事依赖 \"primarily\"/\"the primary\"，用词略单一。\n\n---\n\n## 3. 交叉引用\n\n**总 labels: 89 | 总 unique refs: 53 | 总 bib 条目: 46**\n\n### 孤立 \\label (defined but never referenced)\n\n**附录 figure labels (5 个, 应修复):**\n- appendix.tex:63 — `\\label{fig:rsa_perlayer_curve}`\n- appendix.tex:95 — `\\label{fig:random_subset_ablation}`\n- appendix.tex:210 — `\\label{fig:ood_diagnostics}`\n- appendix.tex:227 — `\\label{fig:linear_vs_mlp}`\n- appendix.tex:545 — `\\label{fig:multilayer_attention}`\n\n**附录 section labels (22 个):** 附录 subsection labels 未被引用，部分可能需要在正文添加 \"see Appendix~\\ref{...}\" 引用。\n\n**主文 section labels (9 个):** section labels 未被 `\\ref` 引用属正常行为。\n\n### 悬空 \\ref (referenced but never defined)\n无。\n\n### 缺失 \\cite (cited but not in .bib)\n无。\n\n### 未使用 bib 条目\n0 条。全部 46 个 bib 条目均被引用。\n\n### 其他问题\n- 重复 labels: 无\n- 缺失 `~\\ref`: 无 (全部使用了非断空格)\n\n---\n\n## 4. 编译结果\n\n### 编译环境\n- Tool: `latexmk -pdf` (pdfTeX 3.141592653, TeX Live 2025)\n- Location: local\n- Output: `main.pdf` (26 pages, 555 KB)\n\n### Errors: 0\n\n### Warnings: 30\n\n| 类型 | 数量 | 说明 |\n|---|---|---|\n| Float specifier `[h]` → `[ht]` | 17 | 全在 appendix.tex，改为 `[htbp]` 即可消除 |\n| Underfull hbox | 3 | bibliography URL 断行，可用 `\\url{}` 缓解 |\n| Underfull vbox | 7 | 浮动体页面分布导致，排版调优问题 |\n| Hyperref token | 3 | appendix.tex:638 section 标题含 `$R^2$`，用 `\\texorpdfstring{$R^2$}{R2}` 修复 |\n\n---\n\n## 总结\n\n| 检查项 | 问题数 | 严重程度 |\n|---|---|---|\n| 数值不匹配 | **9** 处 | 🔴 高 (其中 L1 heads 24→25 出现 4 次为系统性错误) |\n| 残留强 claim | **4** 处 | 🟡 中 (\"sole\"/\"exclusive\" 与 graded routing 叙事矛盾) |\n| AI 写作标志 | **4** 处 | 🟢 低 (-ing 分词句尾，仅 appendix 和 conclusion) |\n| 孤立 figure labels | **5** 处 | 🟡 中 (appendix 图未被引用，违反 CLAUDE.md §1.1 \"附录内容必须在正文中有明确引用\") |\n| 编译 warnings | **30** 处 | 🟢 低 (无 error，warnings 均为排版调优) |\n| 悬空 ref / 缺失 cite | **0** 处 | ✅ 无问题 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/paper_consistency_report.md",
    "content": "# 论文全文一致性检查报告\n\n检查时间: 2026-05-18\n论文路径: `docs/paper/`\n\n## 1. 数值一致性\n\n**总计: 155 个数值, 135 匹配, 9 不匹配, 11 未找到 registry 记录**\n\n### 不匹配项\n\n| 位置 (file:line) | 论文数值 | Registry 数值 | 状态 |\n|---|---|---|---|\n| introduction.tex:18 | L1: 24 heads | `l1_heads_gt50pct.trained` = **25** | ❌ 不匹配 |\n| experiments.tex:12 | N = 63,228 | `lg_dino_extract.total_frames` = **63,728** | ❌ 不匹配 |\n| experiments.tex:40 | L8 untrained readout: 95.5% | `dense_probe_L8_acc` untrained = **98.6%** | ❌ 不匹配 |\n| experiments.tex:41 | L16 untrained readout: 91.1% | `dense_probe_L16_acc` untrained = **92.0%** | ❌ 不匹配 |\n| experiments.tex:52 | VLA 24/32 heads (57.7%) | registry = **25/32** | ❌ 不匹配 |\n| experiments.tex:91 | VLA: 24/32 heads | registry = **25/32** | ❌ 不匹配 |\n| discussion.tex:8 | 0 → 9 → 24 heads | registry = 0, 9, **25** | ❌ 不匹配 |\n| discussion.tex:13 | p = 0.002 (bootstrap CIs) | `task_paired_t.p` = **0.0018** | ❌ 不匹配 (rounding imprecise) |\n| discussion.tex:18 | bottom-24 d = 0.57 | `bottom24_d` = **0.565** | ❌ 不匹配 (borderline rounding) |\n\n### 分析\n\n1. **L1 heads 24 vs 25** — 系统性问题，出现 4 次 (introduction, experiments×2, discussion)。需确认 50% 阈值下的正确 head 数量并全文统一。\n2. **N = 63,228 vs 63,728** — 500 帧差异，需核实数据提取记录。\n3. **Untrained readout L8/L16** — 论文 95.5%/91.1% vs registry 98.6%/92.0%。可能来自不同 probe run，appendix Table `tab:dense_routing` 与正文一致 (95.5%)，但与 registry 不一致。需确认哪个是最终结果。\n4. **p = 0.002 vs 0.0018** — 精度损失。建议用准确值 0.0018 或写 \"p < 0.002\"。\n5. **bottom-24 d = 0.57 vs 0.565** — 四舍五入边界。appendix 用 0.565，discussion 用 0.57。建议统一精度。\n\n### 未找到 registry 记录 (11 项)\n\n主要来自 appendix 中的 robustness 分析 (OOD diagnostics, permutation tests, per-DOF RSA, metric invariance) 和 Llama-2 base mid-depth attention profile，可能是本地计算未录入 registry。\n\n---\n\n## 2. 措辞问题\n\n**总计: 8 处需修改**\n\n### 残留强 claim (4 处)\n\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n| abstract.tex:4 | \"the readout token serves as the **sole** multimodal convergence point\" | 残留强claim | → \"the **primary** multimodal convergence point\" |\n| related_work.tex:25 | \"identify the readout token as the **sole** multimodal integration site\" | 残留强claim | → \"the **primary** multimodal integration site\" |\n| related_work.tex:29 | \"the readout token serves as the **exclusive** multimodal hub\" | 残留强claim | → \"the **primary** multimodal hub\" |\n| experiments.tex:26 | \"The readout is thus the **sole** locus of multimodal integration\" | 残留强claim | → \"the **primary** locus of multimodal integration\" |\n\n### AI 写作标志 — -ing 分词句尾 (4 处)\n\n| 位置 (file:line) | 问题文本 | 问题类型 | 建议修改 |\n|---|---|---|---|\n| conclusion.tex:4 | \"...revealing that VLA fine-tuning primarily reorganizes...\" | AI写作-ing | 拆为两句: \"...VLA representations. The analysis reveals that...\" |\n| appendix.tex:72 | \"...indicating stable but unspecialized processing.\" | AI写作-ing | → \"). This indicates stable but unspecialized processing.\" |\n| appendix.tex:461 | \"...indicating that deep-layer stability derives from...\" | AI写作-ing | → \"; this indicates that deep-layer stability...\" |\n| appendix.tex:620 | \"...indicating instruction-dominant heads have disproportionate influence...\" | AI写作-ing | → \"; instruction-dominant heads thus have disproportionate...\" |\n\n### 已清理确认 (无问题)\n\n- em-dash (—): **0** 处\n- 解释性 en-dash ( – ): **0** 处\n- \"Furthermore\"/\"Moreover\"/\"Additionally\" 序列: **0** 处\n- \"It is worth noting\"/\"Notably\": **0** 处\n- 黑名单用词 (delve/leverage/utilize/facilitate/myriad/plethora): **0** 处\n- \"uniquely responsible\"/\"exclusively\"/\"solely driven\"/\"only instruction heads\": **0** 处\n\n### 新叙事关键词确认\n\n| 关键词 | 出现位置 |\n|---|---|\n| \"graded\" | appendix.tex:676 (\"graded, attention-ordered contribution to routing\") |\n| \"distributed\" | method.tex:4 (\"how action-relevant structure is distributed across a VLA\") |\n| \"primarily\" | conclusion.tex:4, discussion.tex:5, appendix.tex:432 |\n| \"the primary\" | abstract.tex:8, introduction.tex:21, introduction.tex:23, conclusion.tex:5 |\n\n**注**: \"preferentially\" 和 \"predominantly\" 未出现，当前叙事依赖 \"primarily\"/\"the primary\"，用词略单一。\n\n---\n\n## 3. 交叉引用\n\n**总 labels: 89 | 总 unique refs: 53 | 总 bib 条目: 46**\n\n### 孤立 \\label (defined but never referenced)\n\n**附录 figure labels (5 个, 应修复):**\n- appendix.tex:63 — `\\label{fig:rsa_perlayer_curve}`\n- appendix.tex:95 — `\\label{fig:random_subset_ablation}`\n- appendix.tex:210 — `\\label{fig:ood_diagnostics}`\n- appendix.tex:227 — `\\label{fig:linear_vs_mlp}`\n- appendix.tex:545 — `\\label{fig:multilayer_attention}`\n\n**附录 section labels (22 个):** 附录 subsection labels 未被引用，部分可能需要在正文添加 \"see Appendix~\\ref{...}\" 引用。\n\n**主文 section labels (9 个):** section labels 未被 `\\ref` 引用属正常行为。\n\n### 悬空 \\ref (referenced but never defined)\n无。\n\n### 缺失 \\cite (cited but not in .bib)\n无。\n\n### 未使用 bib 条目\n0 条。全部 46 个 bib 条目均被引用。\n\n### 其他问题\n- 重复 labels: 无\n- 缺失 `~\\ref`: 无 (全部使用了非断空格)\n\n---\n\n## 4. 编译结果\n\n### 编译环境\n- Tool: `latexmk -pdf` (pdfTeX 3.141592653, TeX Live 2025)\n- Location: local\n- Output: `main.pdf` (26 pages, 555 KB)\n\n### Errors: 0\n\n### Warnings: 30\n\n| 类型 | 数量 | 说明 |\n|---|---|---|\n| Float specifier `[h]` → `[ht]` | 17 | 全在 appendix.tex，改为 `[htbp]` 即可消除 |\n| Underfull hbox | 3 | bibliography URL 断行，可用 `\\url{}` 缓解 |\n| Underfull vbox | 7 | 浮动体页面分布导致，排版调优问题 |\n| Hyperref token | 3 | appendix.tex:638 section 标题含 `$R^2$`，用 `\\texorpdfstring{$R^2$}{R2}` 修复 |\n\n---\n\n## 总结\n\n| 检查项 | 问题数 | 严重程度 |\n|---|---|---|\n| 数值不匹配 | **9** 处 | 🔴 高 (其中 L1 heads 24→25 出现 4 次为系统性错误) |\n| 残留强 claim | **4** 处 | 🟡 中 (\"sole\"/\"exclusive\" 与 graded routing 叙事矛盾) |\n| AI 写作标志 | **4** 处 | 🟢 低 (-ing 分词句尾，仅 appendix 和 conclusion) |\n| 孤立 figure labels | **5** 处 | 🟡 中 (appendix 图未被引用，违反 CLAUDE.md §1.1 \"附录内容必须在正文中有明确引用\") |\n| 编译 warnings | **30** 处 | 🟢 低 (无 error，warnings 均为排版调优) |\n| 悬空 ref / 缺失 cite | **0** 处 | ✅ 无问题 |\n"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-18T19:33:45.244539+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/paper_consistency_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-18T19:33:45.244745+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_consistency_report",
  "type": "report",
  "description": "论文全文一致性检查报告：数值验证、措辞一致性、交叉引用、编译结果",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/paper_consistency_report.md",
  "tags": "['paper', 'consistency-check', 'quality']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_consistency_report",
    "type": "report",
    "description": "论文全文一致性检查报告：数值验证、措辞一致性、交叉引用、编译结果",
    "project": "vla-ssd",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/paper_consistency_report.md",
    "tags": "['paper', 'consistency-check', 'quality']"
  }
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-18T19:33:45.244983+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_721c88\", \"name\": \"paper_consistency_report\", \"type\": \"report\", \"description\": \"论文全文一致性检查报告：数值验证、措辞一致性、交叉引用、编译结果\", \"path\": \"projects/vla-ssd/artifacts/_project/report/paper_consistency_report.md\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-18T19:33:34.625266+00:00\", \"tags\": [\"paper\", \"consistency-check\", \"quality\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_paper_consistency_check_20260518T192717",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 223 · 2026-05-18T19:33:45.245263+00:00_

报告已写入并注册。核心发现：

**🔴 高优先级 — 数值不匹配 9 处**
- **L1 heads 24→25**: 系统性错误，出现 4 次 (introduction, experiments×2, discussion)。Registry 记录 `l1_heads_gt50pct.trained=25`，论文全写 24。
- **总帧数 63,228 vs 63,728**: 500 帧差异。
- **Untrained readout L8/L16**: 论文 95.5%/91.1% vs registry 98.6%/92.0%，差距显著，需确认哪组是最终数据。
- **p=0.002 vs 0.0018**: 精度损失，建议用准确值。

**🟡 中优先级 — 措辞 4 处**
- "sole" 出现 3 次、"exclusive" 出现 1 次，与 "graded distributed routing" 叙事矛盾，建议统一改为 "primary"。

**🟡 中优先级 — 5 个附录 figure 有 label 但未被引用**
- `fig:rsa_perlayer_curve`, `fig:random_subset_ablation`, `fig:ood_diagnostics`, `fig:linear_vs_mlp`, `fig:multilayer_attention`

**🟢 低优先级**
- 4 处 -ing 分词句尾 (AI 写作标志)
- 30 个编译 warnings (0 errors, 17 个 float specifier, 3 个 hyperref)
- 交叉引用和 citation 完整性良好 (0 悬空 ref, 0 缺失 cite)

报告路径: `artifacts/paper_consistency_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_paper_consistency_check_20260518T192717"
}
```

</details>

---
