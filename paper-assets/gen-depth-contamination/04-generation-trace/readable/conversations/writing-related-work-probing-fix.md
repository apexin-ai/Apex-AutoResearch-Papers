# writing related work probing fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_writing_related-work-probing-fix_20260514T045514.jsonl`
- **Structured JSON:** [`ca15de6739da73c75dfd.json`](../../sessions/ca/ca15de6739da73c75dfd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-14T04:56:21.499500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/drafts/related_work_audit.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T04:56:21.500026+00:00_

1	# Related Work 完整性审查
2	
3	审查日期: 2026-05-14
4	审查范围: `related_work.tex` (54行, 5个段落)
5	
6	---
7	
8	## 已覆盖
9	
10	### Model Collapse and Recursive Generation
11	- Shumailov et al. (2024, Nature): line 6, tail-distribution degradation
12	- Alemohammad et al. (2024, ICLR): line 7, self-consuming models, fixed point convergence
13	- Dohmatob et al. (2024, ICML): line 8, scaling laws for tail loss
14	- Schaeffer et al. (2025, ICML): line 9-10, 8-definition taxonomy, K* 与 Family B 对齐
15	- Kazdan et al. (2025, ICML): line 11-12, replace vs accumulate regimes
16	- Shi et al. (2025, NeurIPS Spotlight): line 13, generalization-to-memorization transition
17	- Amin et al. (2025, NeurIPS): line 47, weak signals suffice to escape collapse
18	- Gambetta et al. (2025): line 48, surplexity metric
19	
20	### Binary Synthetic Text Detection
21	- GLTR (Gehrmann et al. 2019): line 18, token-level likelihood visualization
22	- Grover (Zellers et al. 2019): line 19, generator-as-detector
23	- Ippolito et al. (2020): line 19, detection difficulty vs generation quality
24	- DetectGPT (Mitchell et al. 2023): line 20, probability curvature
25	- Binoculars (Hans et al. 2024): line 21, cross-perplexity ratio
26	- DivEye (Basani et al. 2026): line 22, surprisal diversity
27	- Min-K%++ (Zhang et al. 2024): line 22, outlier token likelihoods
28	- CoDeC (Zawalski et al. 2026): line 23, in-context learning contamination detection
29	
30	### Ordinal Classification
31	- CORAL (Cao et al. 2020): line 32-33, rank-consistent ordinal regression
32	
33	### Data Selection and Curation
34	- DSIR (Xie et al. 2023): line 40, importance resampling
35	- D4 (Tirumala et al. 2023): line 41, deduplication + diversification
36	- DoReMi (Xie et al. 2023): line 41, domain weight optimization
37	- Drayson et al. (2025): line 44-46, binary detection + SIR (positioned as special case of our framework)
38	
39	### Watermarking
40	- Kirchenbauer et al. (2023): line 52-53, statistical watermarking
41	
42	---
43	
44	## 需要补充
45	
…[truncated 5257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T04:56:21.500259+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T04:56:21.500403+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T04:56:21.500528+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T04:56:21.500649+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T04:56:21.500806+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T04:56:21.500982+00:00_

artifacts/dream_reports/dream_20260512T200328/best/paper.tex
artifacts/dream_reports/dream_20260512T200328/median/paper.tex
artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
artifacts/dream_reports/dream_20260513T080728/best/paper.tex
artifacts/dream_reports/dream_20260513T080728/median/paper.tex
artifacts/dream_reports/dream_20260513T080728/worst/paper.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_c1.tex
docs/paper/method.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/experiments_c1.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T04:56:21.501126+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T04:56:21.501495+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T04:56:21.501641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T04:56:21.501843+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model Collapse and Recursive Generation.}
5	Training on model-generated data can cause progressive distribution shift known as \emph{model collapse}.
6	Shumailov et al.~\cite{shumailov2024collapse} showed that iteratively training language models on their own outputs leads to irreversible tail-distribution degradation, with minority modes vanishing across generations.
7	Alemohammad et al.~\cite{alemohammad2024selfconsuming} formalized this for self-consuming generative models, proving convergence to a fixed point under mild regularity conditions.
8	Dohmatob et al.~\cite{dohmatob2024model} derived scaling laws for collapse, demonstrating that tail probability mass is lost at rates predictable from model and data scale.
9	Schaeffer et al.~\cite{schaeffer2025position} organized the fragmented literature into a taxonomy of eight definitions across three families.
10	Our $\Kstar$ aligns with their Family~B (distributional deformation), specifically D4 (collapsing variance) and D6 (mode entanglement)---the features that degrade most rapidly in our experiments are precisely variance-based surprisal measures.
11	Kazdan et al.~\cite{kazdan2025collapse} distinguished \emph{replace} and \emph{accumulate} regimes: in the replace regime each generation completely supplants its predecessor, producing faster collapse.
12	Our prompt-chain protocol operates in the replace regime, so $\Kempirical = 2$ is a conservative lower bound; the accumulate regime would yield slower degradation and higher $\Kstar$.
13	Shi et al.~\cite{shi2025generalization} identified a generalization-to-memorization transition in recursively trained models, providing cross-modal evidence that information loss is progressive.
14	These works characterize the macro dynamics of collapse but do not provide tools for per-text generational depth estimation.
15	
16	\paragraph{Binary Synthetic Text Detection.}
17	Distinguishing machine-generated from h
…[truncated 5812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T04:56:21.502006+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T04:56:21.502179+00:00_

1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-14
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{shi2025generalization,
31	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
32	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
33	  booktitle={Advances in NeurIPS},
34	  year={2025},
35	  note={Spotlight},
36	  url={https://arxiv.org/abs/2509.16499}
37	}
38	
39	@inproceedings{mitchell2023detectgpt,
40	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
41	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
42	  booktitle={Proceedings of ICML},
43	  year={2023}
44	}
45	
46	% === Should-Cite ===
47	
48	@article{basani2026diveye,
49	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
50	  author={Basani, Advik Raj and Chen, Pin-Yu}
…[truncated 5128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T04:56:21.502459+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
  "old_string": "Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}",
  "new_string": "The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Boundary Detection (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Probing Classifiers.}\nLinear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\nBelinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\nOur neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.\n\n\\paragraph{Data Selection and Curation.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
    "old_string": "Our Ordinal Boundary Detection (OBD) head leverages this ordered structure, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Data Selection and Curation.}",
    "new_string": "The idea of decomposing ordinal problems into a series of binary decisions dates to Frank \\& Hall~\\cite{frank2001ordinal}; our Ordinal Boundary Detection (OBD) head follows this principle by learning $K\\!-\\!1$ cumulative boundary classifiers, yielding monotonic depth predictions and stronger calibration than a flat softmax baseline.\n\n\\paragraph{Probing Classifiers.}\nLinear and shallow MLP probes have become a standard tool for analyzing what information is encoded in pretrained representations~\\cite{alain2017understanding,conneau2018probing}.\nBelinkov~\\cite{belinkov2022probing} surveys the methodology and cautions that probe complexity must be controlled to ensure that performance reflects representational content rather than probe capacity.\nOur neural probe experiment follows this protocol: a two-layer MLP on frozen Qwen2.5-1.5B embeddings, where the probe's limited capacity ensures that discriminability reflects depth information already present in the representations rather than learned de novo.\n\n\\paragraph{Data Selection and Curation.}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T04:56:21.502634+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T04:56:21.502801+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "old_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}",
  "new_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n\n% === Probing Classifiers ===\n\n@article{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  journal={arXiv preprint arXiv:1610.01644},\n  year={2017}\n}\n\n@inproceedings{conneau2018probing,\n  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Ordinal Classification (additional) ===\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
    "old_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}",
    "new_string": "@inproceedings{ippolito2020detection,\n  title={Automatic Detection of Generated Text is Easiest when Humans are Fooled},\n  author={Ippolito, Daphne and Duckworth, Daniel and Callison-Burch, Chris and Eck, Douglas},\n  booktitle={Proceedings of ACL},\n  year={2020}\n}\n\n% === Probing Classifiers ===\n\n@article{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  journal={arXiv preprint arXiv:1610.01644},\n  year={2017}\n}\n\n@inproceedings{conneau2018probing,\n  title={What You Can Cram into a Single \\$\\&!\\#* Vector: Probing Sentence Embeddings for Linguistic Properties},\n  author={Conneau, Alexis and Kruszewski, German and Lample, Guillaume and Barrault, Lo{\\\"\\i}c and Baroni, Marco},\n  booktitle={Proceedings of ACL},\n  year={2018}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Ordinal Classification (additional) ===\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T04:56:21.502987+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_related-work-probing-fix_20260514T045514",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T04:56:21.503145+00:00_

修改完成。摘要：

**related_work.tex**:
- **Ordinal Classification 段落**：将原来独立引用 CORAL 的结尾句改写，加入 Frank & Hall (2001) 作为 ordinal-to-binary decomposition 的开创性工作，并将 OBD head 的设计与之关联
- **新增 Probing Classifiers 段落**（3 句，位于 Ordinal Classification 和 Data Selection 之间）：引用 Alain & Bengio (2017)、Conneau et al. (2018)、Belinkov (2022)，说明 neural probe 实验遵循该范式，probe 的有限容量确保可区分性来自表征本身而非 probe 学到的新信息

**references.bib**：新增 4 条 bib entry — `alain2017understanding`、`conneau2018probing`、`belinkov2022probing`、`frank2001ordinal`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_related-work-probing-fix_20260514T045514"
}
```

</details>

---
