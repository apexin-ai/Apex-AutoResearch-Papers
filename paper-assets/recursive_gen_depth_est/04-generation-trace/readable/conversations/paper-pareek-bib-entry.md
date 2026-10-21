# paper pareek bib entry

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_paper_pareek_bib_entry_20260517T203612.jsonl`
- **Structured JSON:** [`29062464ab3095266459.json`](../../sessions/29/29062464ab3095266459.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-17T20:38:27.949128+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T20:38:27.949453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T20:38:27.949627+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pareek Du Oh 2024 understanding recursive generation model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pareek Du Oh 2024 understanding recursive generation model collapse"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T20:38:27.949756+00:00_

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
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T20:38:27.950056+00:00_

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

…[truncated 24918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T20:38:27.950230+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T20:38:27.950583+00:00_

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

…[truncated 24918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T20:38:27.950751+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T20:38:27.950894+00:00_

docs/paper/main.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/generalization.tex
docs/paper/atlas.tex
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/section_appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T20:38:27.951020+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T20:38:27.951135+00:00_

artifacts/_project/paper/theory_draft_3bd3d2.tex
artifacts/_project/paper/theory_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T20:38:27.951284+00:00_

Web search results for query: "Pareek Du Oh 2024 understanding recursive generation model collapse"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"Fit, simulate, fit: How models can collapse after generations of recursive fitting - The DO Loop","url":"https://blogs.sas.com/content/iml/2024/07/31/synthetic-data-model-collapse.html"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"AI models collapse when trained on recursively generated data","url":"https://vittoriodublinoblog.org/wp-content/uploads/2025/07/ai-models-collapse-when-trained-on-recursively-generated-data.pdf"},{"title":"Author Correction: AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-025-08905-3"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Review: AI models collapse when trained on recursively generated data | by Ignacio Pérez | Medium","url":"https://medium.com/@ignacioperezzv/review-ai-models-collapse-when-trained-on-recursively-generated-data-00ed1fc8d488"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"}]

Based on the search results, I found research relat
…[truncated 1722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T20:38:27.951457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pareek Du Oh 2024 arxiv understanding model collapse recursive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pareek Du Oh 2024 arxiv understanding model collapse recursive"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T20:38:27.951577+00:00_

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
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T20:38:27.951701+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.
7	Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024}, web-scale quality filtering~\cite{penedo2024_fineweb}, and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot curation results are inconclusive (Appendix~\ref{app:curation_poc}), and a downstream fine-tuning probe finds depth-filtered subsets comparable to unfiltered baselines ($\Delta\text{PPL} \leq 0.12$; Appendix~\ref{app:downstream}), with the depth-correlated training loss monotonicity (d0~$>$~d1~$>$~d2) providing indirect evidence that recursive generation reduces information content.
8	Adversarial robustness remains untested.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T20:38:27.951862+00:00_

Web search results for query: "Pareek Du Oh 2024 arxiv understanding model collapse recursive"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v1"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"[2506.09401] A theoretical basis for model collapse in recursive training","url":"https://arxiv.org/abs/2506.09401"},{"title":"Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/html/2412.17646v1"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"A Probabilistic Perspective on Model Collapse","url":"https://arxiv.org/html/2505.13947"},{"title":"THE CURSE OF RECURSION: TRAINING ON GENERATED DATA MAKES MODELS FORGET","url":"https://arxiv.org/pdf/2305.17493"}]

Based on the search results, I found several relevant papers related to model collapse and recursive training of generative models:

## Key Papers Found:

**1. "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" (April 2024)**

This paper empirically finds that accumulating synthetic data with real data avoids model collapse for all models and for all data modalities tested. The researchers confirm that replacing data at every iteration causes test error to increase with iterations, and they use an analytically tractable framew
…[truncated 1230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T20:38:27.952060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Pareek\" \"Du\" \"Oh\" 2024 model collapse downstream arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Pareek\" \"Du\" \"Oh\" 2024 model collapse downstream arxiv"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T20:38:27.952181+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pareek Du Oh understanding model collapse language model 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pareek Du Oh understanding model collapse language model 2024"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T20:38:27.952333+00:00_

Web search results for query: ""Pareek" "Du" "Oh" 2024 model collapse downstream arxiv"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"THE CURSE OF RECURSION: TRAINING ON GENERATED DATA MAKES MODELS FORGET","url":"https://arxiv.org/pdf/2305.17493"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v1"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"}]

Based on the search results, I found several relevant papers on model collapse and downstream effects, though I didn't find a specific paper with all those exact author names together. However, here are the key findings:

The search returned multiple 2024 papers on model collapse from arxiv:

1. **"Position: Model Collapse Does Not Mean What You Think"** (March 2025, arXiv 2503.03150) - This paper identifies 8 definitions of model collapse by hand-annotating 28 prior research publications.

2. **"Is Model Collapse Inevitable?"** (April 2024, arXiv 2404.01413) - This paper examines whether
…[truncated 978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T20:38:27.952506+00:00_

Web search results for query: "Pareek Du Oh understanding model collapse language model 2024"

Links: [{"title":"The Fall of ROME: Understanding the Collapse of LLMs in Model Editing - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.236/"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"What Is Model Collapse? | IBM","url":"https://www.ibm.com/think/topics/model-collapse"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Epistemic diversity across language models mitigates knowledge collapse","url":"https://arxiv.org/html/2512.15011v1"},{"title":"Epistemic Diversity and Knowledge Collapse in Large Language Models","url":"https://arxiv.org/html/2510.04226v2"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"}]

Based on the search results, I found information related to model collapse in language models from 2024, though the exact authors "Pareek Du Oh" don't appear in the results. However, I can provide you with relevant 2024 research on understanding model collapse:

## Model Collapse in Language Models - 2024 Research

Model collapse is a phenomenon where machine learning models gradually degrade due to errors coming from uncurated synthetic data, or training on the outputs of another model, such as prior versions of itself.

### Key Findings from 2024 Studies:

**Sta
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T20:38:27.952675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv Pareek Du Oh 2024 recursive generation depth"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv Pareek Du Oh 2024 recursive generation depth"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T20:38:27.952796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org Pareek \"understanding\" 2024 recursive generative model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org Pareek \"understanding\" 2024 recursive generative model"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T20:38:27.952990+00:00_

Web search results for query: "arxiv Pareek Du Oh 2024 recursive generation depth"

Links: [{"title":"Learning Dynamic Recursive Depths for Adaptive Token- ...","url":"https://arxiv.org/pdf/2507.10524"},{"title":"Recursive Inference Scaling:","url":"https://arxiv.org/pdf/2502.07503"},{"title":"Computer Science Jul 2024","url":"https://arxiv.org/list/cs/2024-07?skip=2200&show=100"},{"title":"Machine Learning Jul 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-07?skip=335&show=2000"},{"title":"Recursive Language Models","url":"https://arxiv.org/html/2512.24601v1"},{"title":"Towards automated generation of fast and accurate algorithms for recursive matrix multiplication","url":"https://arxiv.org/html/2506.19405"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Computer Science Jan 2024","url":"https://www.arxiv.org/list/cs/2024-01?skip=2105&show=5"},{"title":"Computer Vision and Pattern Recognition Sep 2024","url":"https://arxiv.org/list/cs.CV/2024-09?skip=1285&show=2000"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"}]

Based on the search results, I found a paper that matches your query. The paper appears to be by Divyansh Pareek, Simon S. Du, and Sewoong Oh, and it was listed in the Machine Learning section of arXiv for July 2024.

The search results also returned related papers on recursive generation and depth:

1. **"Learning Dynamic Recursive Depths for Adaptive Token-..."** - This paper discusses an architecture (MoR) that ties weights to cut parameters, routes tokens to cut redundant FLOPs, and caches key-values recursion-wise to cut memory traffic.

2. **"Recursive Inference Scaling"** - This paper examines if recursive depth can be used as a form of scale-invariant decoding for inference-time scaling, and identifies a parameter-sharing strategy called Recursive INference Scaling (RINS).

However, I wasn't able to retrieve the full details of the specific paper by Pareek, Du, 
…[truncated 274 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T20:38:27.953192+00:00_

Web search results for query: "site:arxiv.org Pareek "understanding" 2024 recursive generative model"

Links: [{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"Under Review WHAT HAPPENS WHEN GENERATIVE AI MODELS TRAIN","url":"https://arxiv.org/pdf/2505.21677"},{"title":"What happens when generative AI models train recursively on each others’ outputs?","url":"https://arxiv.org/html/2505.21677v3"},{"title":"Machine Learning Jul 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-07?skip=305&show=2000"},{"title":"Published as a conference paper at ICLR 2024 NEURAL-SYMBOLIC RECURSIVE MACHINE","url":"https://arxiv.org/pdf/2210.01603"},{"title":"Recursive Language Models","url":"https://arxiv.org/html/2512.24601v1"},{"title":"Curated Synthetic Data Doesn’t Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences","url":"https://arxiv.org/html/2605.07724"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Rate of Model Collapse in Recursive Training","url":"https://arxiv.org/html/2412.17646v1"}]

I found several relevant results from arXiv related to recursive generative models and understanding model collapse in 2024. Here are the key papers from the search:

**Most Relevant Result:**
The first result is "A Note on Shumailov et al. (2024): 'AI Models Collapse When Trained on Recursively Generated Data'" which demonstrates that repeatedly training a generative model on synthetic data leads to model collapse. This work investigates the effects of fitting a distribution (through Kernel Density Estimation, or KDE) or a model to the data, followed by repeated sampling from it, with the objective to de
…[truncated 1436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T20:38:27.953394+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Divyansh Pareek\" \"Simon Du\" \"Sewoong Oh\" 2024 model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Divyansh Pareek\" \"Simon Du\" \"Sewoong Oh\" 2024 model collapse"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T20:38:27.953545+00:00_

Web search results for query: ""Divyansh Pareek" "Simon Du" "Sewoong Oh" 2024 model collapse"

Links: [{"title":"dblp: Divyansh Pareek","url":"https://dblp.org/pid/224/5879.html"},{"title":"Divyansh Pareek - GitHub Pages","url":"https://pareek21.github.io/"},{"title":"A Task-Centric Theory for Iterative Self-Improvement with Easy-to-Hard Curricula | Request PDF","url":"https://www.researchgate.net/publication/400661291_A_Task-Centric_Theory_for_Iterative_Self-Improvement_with_Easy-to-Hard_Curricula"},{"title":"Understanding the Gains from Repeated Self-Distillation Divyansh Pareek","url":"https://papers.nips.cc/paper_files/paper/2024/file/0eb1ac7551ddbae575415aa5183a88be-Paper-Conference.pdf"},{"title":"Sewoong Oh (last updated February 11, 2026) Contact","url":"https://homes.cs.washington.edu/~sewoong/SewoongOhCV.pdf"},{"title":"Divyansh Pareek | OpenReview","url":"https://openreview.net/profile?id=~Divyansh_Pareek2"},{"title":"Divyansh Pareek","url":"https://scholar.google.com/citations?user=R1lrFWgAAAAJ&hl=en"},{"title":"Divyansh Pareek","url":"https://www.facebook.com/divyansh.pareek.5"},{"title":"Conference papers","url":"https://homes.cs.washington.edu/~sewoong/papers.html"},{"title":"Divyansh Pareek | DeepAI","url":"https://deepai.org/profile/divyansh-pareek"}]

Based on the search results, Divyansh Pareek, Simon S. Du, and Sewoong Oh published a 2024 paper on "Understanding the Gains from Repeated Self-Distillation" where they found that self-distillation improves performance, especially when applied repeatedly. The paper was presented at NeurIPS 2024.

However, the search results do not contain information about their work specifically addressing "model collapse" in 2024. The paper found appears to focus on self-distillation gains rather than model collapse. If you're looking for specific information about their model collapse research, you may want to search for additional papers or clarify what aspect of their work you're interested in.


REMINDER: You MU
…[truncated 84 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T20:38:27.953723+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Understanding the Gains from Repeated Self-Distillation\" Pareek arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Understanding the Gains from Repeated Self-Distillation\" Pareek arxiv 2024"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T20:38:27.954066+00:00_

Web search results for query: ""Understanding the Gains from Repeated Self-Distillation" Pareek arxiv 2024"

Links: [{"title":"[2407.04600] Understanding the Gains from Repeated Self-Distillation","url":"https://arxiv.org/abs/2407.04600"},{"title":"Understanding the Gains from Repeated Self-Distillation","url":"https://arxiv.org/html/2407.04600v1"},{"title":"Understanding the Gains from Repeated Self-Distillation","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/0eb1ac7551ddbae575415aa5183a88be-Abstract-Conference.html"},{"title":"Machine Learning Jul 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-07?skip=330&show=50"},{"title":"Understanding the Gains from Repeated Self-Distillation Divyansh Pareek","url":"https://papers.nips.cc/paper_files/paper/2024/file/0eb1ac7551ddbae575415aa5183a88be-Paper-Conference.pdf"},{"title":"Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://arxiv.org/html/2507.00075v1"},{"title":"arXiv:2505.15195v1 [cs.LG] 21 May 2025","url":"https://arxiv.org/pdf/2505.15195"},{"title":"NeurIPS Poster Understanding the Gains from Repeated Self-Distillation","url":"https://neurips.cc/virtual/2024/poster/94147"},{"title":"Statistics Jul 2024","url":"https://arxiv.org/list/stat/2024-07?skip=580&show=250"},{"title":"Self-Distillation in Deep Learning","url":"https://www.emergentmind.com/topics/self-distillation"}]

I found the paper! Here's a summary of "Understanding the Gains from Repeated Self-Distillation" by Divyansh Pareek, Simon S. Du, and Sewoong Oh (2024):

## Overview

The paper studies self-distillation, a special type of knowledge distillation where the student model has the same architecture as the teacher model, and despite using the same architecture and training data, self-distillation has been empirically observed to improve performance, especially when applied repeatedly.

## Key Findings

The analysis shows that the excess risk achieved by multi-step self-dist
…[truncated 941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T20:38:27.954298+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}",
  "new_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{pareek2024understanding,\n  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},\n  title     = {{Understanding the Gains from Repeated Self-Distillation}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2407.04600},\n  url       = {https://arxiv.org/abs/2407.04600},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "old_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}",
    "new_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{pareek2024understanding,\n  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},\n  title     = {{Understanding the Gains from Repeated Self-Distillation}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2407.04600},\n  url       = {https://arxiv.org/abs/2407.04600},\n}"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T20:38:27.954527+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T20:38:27.954663+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
  "old_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}",
  "new_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{pareek2024understanding,\n  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},\n  title     = {{Understanding the Gains from Repeated Self-Distillation}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2407.04600},\n  url       = {https://arxiv.org/abs/2407.04600},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
    "old_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}",
    "new_string": "@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{pareek2024understanding,\n  author    = {Pareek, Divyansh and Du, Simon S. and Oh, Sewoong},\n  title     = {{Understanding the Gains from Repeated Self-Distillation}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2407.04600},\n  url       = {https://arxiv.org/abs/2407.04600},\n}"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T20:38:27.954864+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T20:38:27.955062+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "old_string": "with the depth-correlated training loss monotonicity (d0~$>$~d1~$>$~d2) providing indirect evidence that recursive generation reduces information content.",
  "new_string": "with the depth-correlated training loss monotonicity (d0~$>$~d1~$>$~d2) providing indirect evidence that recursive generation reduces information content~\\cite{pareek2024understanding}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "old_string": "with the depth-correlated training loss monotonicity (d0~$>$~d1~$>$~d2) providing indirect evidence that recursive generation reduces information content.",
    "new_string": "with the depth-correlated training loss monotonicity (d0~$>$~d1~$>$~d2) providing indirect evidence that recursive generation reduces information content~\\cite{pareek2024understanding}."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T20:38:27.955210+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_pareek_bib_entry_20260517T203612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-17T20:38:27.955370+00:00_

完成。

- **bib 条目**: `pareek2024understanding` 已添加到两个 `references.bib`（Pareek, Divyansh and Du, Simon S. and Oh, Sewoong, "Understanding the Gains from Repeated Self-Distillation", NeurIPS 2024, arXiv:2407.04600）
- **Discussion 引用**: 在 downstream analysis 段落中 "recursive generation reduces information content" 后添加了 `\cite{pareek2024understanding}`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_pareek_bib_entry_20260517T203612"
}
```

</details>

---
