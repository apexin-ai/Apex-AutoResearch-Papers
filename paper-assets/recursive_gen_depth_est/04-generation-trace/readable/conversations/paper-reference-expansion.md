# paper reference expansion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_reference_expansion_20260517T170455.jsonl`
- **Structured JSON:** [`ece97526ee3e23c7726f.json`](../../sessions/ec/ece97526ee3e23c7726f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-17T17:07:42.003576+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:07:42.004071+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:07:42.004336+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:07:42.004536+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:07:42.004721+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:07:42.004924+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:07:42.005129+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:07:42.005303+00:00_

artifacts/_project/paper/references.bib
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:07:42.005471+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:07:42.005647+00:00_

artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
docs/paper/main.tex
artifacts/dream_reports/dream_20260517T075852/best/paper.tex
artifacts/dream_reports/dream_20260517T075852/median/paper.tex
artifacts/dream_reports/dream_20260517T075852/worst/paper.tex
docs/paper/related_work.tex
artifacts/_project/paper/theory_draft.tex
docs/paper/atlas.tex
docs/paper/discussion.tex
docs/paper/method.tex
docs/paper/generalization.tex
docs/paper/conclusion.tex
docs/paper/section_appendix.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/theory_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:07:42.005841+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recursive_gen_depth_est",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recursive_gen_depth_est",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:07:42.006531+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\", \"content\": \"# Literature Map — recursive_gen_depth_est\\n# Last updated: 2026-05-15\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\n#\\n# Tags used for cite_in: introduction, related-work, background, method,\\n#   experiments, discussion, limitations, dcol-section\\n\\n# =============================================================\\n# MODEL COLLAPSE — foundational theory & recursive generation\\n# =============================================================\\n\\nshumailov2024_nature:\\n  title: \\\"AI models collapse when trained on recursively generated data\\\"\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\n  venue: Nature\\n  year: 2024\\n  doi: \\\"10.1038/s41586-024-07566-y\\\"\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\n  relevance: direct\\n  cite_in: [introduction, related-work, background]\\n  notes: >\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\n    sampling strategies—uses standard sampling (T=1).\\n\\nmarchi2024_heat_death:\\n  title: \\\"Heat Death of Generative Models in Closed-Loop Learning\\\"\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\n  venue: ICASSP 2025\\n  year: 2024\\n  arxiv: \\\"2404.02325\\\"\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\n  relevance: direct\\n  cite_in: [discussion]\\n  notes: >\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\n    support for our tau=0.9 accelerated convergence finding.\\n\\ndohmatob2024_tale_of_tails:\\n  title: \\\"A Tale of Tails: Model Collapse as a Cha
…[truncated 26478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T17:07:42.006781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:07:42.007111+00:00_

1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},

…[truncated 23503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:07:42.007310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:07:42.007490+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}) and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sada
…[truncated 2236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:07:42.007685+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
    "output_mode": "content",
    "glob": "*.tex",
    "head_limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:07:42.007857+00:00_

docs/paper/related_work.tex:5:\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
docs/paper/related_work.tex:6:Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
docs/paper/related_work.tex:7:\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
docs/paper/related_work.tex:8:Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/related_work.tex:13:M4-SemEval \cite{wang2024_m4_semeval} and RAID \cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.
docs/paper/related_work.tex:17:EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; LOKI \cite{loki2025} benchmarks synthetic data detection across modalities.
docs/paper/related_work.tex:18:\citet{mohamed2025_brok
…[truncated 6881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:07:42.008114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract all unique citation keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T17:07:42.008266+00:00_

alemohammad2024_mad
bakshi2026_collapse_improvement
basu2021_mirostat
bevendorff2025_two_paradigms
binoculars2024
briesch2024selfconsuming
cloc2025
coral2020
diveye2026
dohmatob2024_demystified
dohmatob2024_tale_of_tails
dohmatob2025_strong_collapse
drayson2025_detection_prevents_collapse
dsir2023
dugan2024_raid
editlens2026
falahati2026_curated
fast_detectgpt2024
finlayson2024_closing
frank2001
garces_arias2025_decoding_decoded
gehrmann2019_gltr
gerstgrasser2024_accumulate
guo2024curious
he2021_deberta_v3
holtzman2020_nucleus
hu2022lora
kirchenbauer2023_watermark
knowledge_collapse2025
liu2019_roberta
llama3
loki2025
marchi2024_heat_death
mccullagh1980_ordinal
mitchell2023_detectgpt
mohamed2025_broken_telephone
padmakumar2024diversity
pu2026_generator_barrier
pudasaini2026_detection_fails
qurating2024
qwen2.5
rennie2005
sadasivan2023_paraphrase
schaeffer2025
seddik2024synthetic
shi2025_closer_look
shumailov2024_nature
sigma2026_spectral
sugiyama2007_importance_weighting
synthetic_eggs2026
uchendu2020_attribution
verma2024_ghostbuster
wang2024_m4_semeval
wang2026_contamination
wenzek2020_ccnet
wiher2022_decoding
wu2025_detection_survey
yang2024_dnagpt
yi2026_escaping_collapse

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:07:42.008461+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,",
  "new_string": "% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "old_string": "% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,",
    "new_string": "% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T17:07:42.008666+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T17:07:42.008797+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@inproceedings{yang2024_dnagpt,",
  "new_string": "@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "old_string": "@inproceedings{yang2024_dnagpt,",
    "new_string": "@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T17:07:42.009072+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T17:07:42.009236+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@article{sugiyama2007_importance_weighting,",
  "new_string": "@inproceedings{penedo2024_fineweb,\n  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},\n  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2406.17557},\n  url       = {https://arxiv.org/abs/2406.17557},\n}\n\n@article{sugiyama2007_importance_weighting,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "old_string": "@article{sugiyama2007_importance_weighting,",
    "new_string": "@inproceedings{penedo2024_fineweb,\n  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},\n  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2406.17557},\n  url       = {https://arxiv.org/abs/2406.17557},\n}\n\n@article{sugiyama2007_importance_weighting,"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T17:07:42.009428+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T17:07:42.009574+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "old_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.",
  "new_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2024_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "old_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.",
    "new_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2024_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T17:07:42.009750+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:07:42.009904+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T17:07:42.010038+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.
7	Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024} and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\ref{app:curation_poc}) and adversarial robustness remains untested.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T17:07:42.010166+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "old_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
  "new_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024}, web-scale quality filtering~\\cite{penedo2024_fineweb}, and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "old_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
    "new_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024}, web-scale quality filtering~\\cite{penedo2024_fineweb}, and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T17:07:42.010323+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T17:07:42.010469+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
  "description": "Count total unique citations in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
    "description": "Count total unique citations in paper"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T17:07:42.010586+00:00_

62

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T17:07:42.010698+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort | uniq -d",
  "description": "Check for duplicate bib keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort | uniq -d",
    "description": "Check for duplicate bib keys"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T17:07:42.010809+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T17:07:42.010940+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort -u)",
  "description": "Find cited keys missing from bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "tool_args": {
    "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort -u)",
    "description": "Find cited keys missing from bib"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T17:07:42.011056+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T17:07:42.011175+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
  "description": "Sync bib file to artifacts copy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "tool_args": {
    "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
    "description": "Sync bib file to artifacts copy"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T17:07:42.011292+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reference_expansion_20260517T170455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-17T17:07:42.011447+00:00_

验证结果：

- **总引用数：62**（远超 30+ 目标）
- **无重复 bib 条目**
- **所有 `\cite{}` 在 bib 中均有对应条目**
- **无 undefined citation**

新增 3 篇（均来自 literature_map 中已有但 bib 中缺失的条目）：

| 引用键 | 论文 | 会议 | 集成位置 |
|--------|------|------|----------|
| `tulchinskii2024_intrinsic_dim` | Intrinsic Dimension Estimation for Robust Detection | NeurIPS 2023 | Related Work: AI Text Detection 段 |
| `li2024_mage` | MAGE: Machine-generated Text Detection in the Wild | ACL 2024 | Related Work: AI Text Detection 段（benchmark 列表） |
| `penedo2024_fineweb` | The FineWeb Datasets | NeurIPS 2024 | Discussion: data curation 引用链 |

论文已有的 62 篇引用覆盖了任务要求的所有类别。literature_map 中 43 篇条目现已全部在 bib 中有对应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_reference_expansion_20260517T170455"
}
```

</details>

---
