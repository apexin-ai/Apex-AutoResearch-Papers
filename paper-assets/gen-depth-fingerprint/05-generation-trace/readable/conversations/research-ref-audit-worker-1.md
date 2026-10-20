# research ref audit worker 1

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 403
- **Recorded user turns:** 0
- **Tool calls:** 201
- **Original source:** `logs/chats/worker_research_ref-audit-worker-1_20260526T102052.jsonl`
- **Structured JSON:** [`81ca90d5fc9ae45ce2f5.json`](../../sessions/81/81ca90d5fc9ae45ce2f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

403 recorded events

### Tool call

_source line 1 · 2026-05-26T10:34:47.736219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:34:47.736680+00:00_

1	% ===== Data Provenance / Contamination =====
2	
3	% ===== Statistics =====
4	
5	@book{cohen1988statistical,
6	  title = {{Statistical Power Analysis for the Behavioral Sciences}},
7	  author = {Cohen, Jacob},
8	  edition = {2nd},
9	  publisher = {Lawrence Erlbaum Associates},
10	  year = {1988},
11	}
12	
13	% ===== Detection =====
14	
15	@inproceedings{detectgpt,
16	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
17	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
18	  booktitle = {Proceedings of the International Conference on Machine Learning},
19	  year = {2023},
20	}
21	
22	@inproceedings{gltr,
23	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
24	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
25	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
26	  year = {2019},
27	}
28	
29	@inproceedings{dna_gpt,
30	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
31	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
32	  booktitle = {Proceedings of the International Conference on Learning Representations},
33	  year = {2024},
34	}
35	
36	@inproceedings{binoculars,
37	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
38	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
39	  booktitle = {Proceedings of the International Conference on Machine Learning},
40	  year = {2024},
41	}
42	
43	@inproceedings{fast_detectgpt,
44	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
45	  auth
…[truncated 27488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:34:47.736875+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:34:47.737043+00:00_

artifacts/_project/paper/appendix_ablation.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_cross_model_detail.tex
artifacts/_project/paper/appendix_cross_temp.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/appendix_feature_correlation.tex
artifacts/_project/paper/appendix_generator_subsets.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_qualitative_examples.tex
artifacts/_project/paper/appendix_temperature_stability.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table2.tex
artifacts/_project/paper/appendix_feature_distributions.tex
artifacts/_project/paper/per_family_cohens_d_table.tex
artifacts/_project/paper/per_family_ddr_table.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/appendix_ai_assistants.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_ddr_validation.tex
artifacts/_project/paper/appendix_iterative_comparison.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/appendix_feature_candidates.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_variance_decomposition.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_error_analysis.tex
artifacts/_project/paper/appendix_nll_distribution.tex
artifacts/_project/paper/appendix_9gen_scale.tex
artifacts/_project/paper/appendix_ddr_causality.tex
artifacts/_project/paper/appendix_convergence.tex
artifacts/_project/paper/appendix_instruct.tex
artifacts/_project/paper/appendix_seed_control.tex
artifacts/_project/paper/appendix_transfer.tex
artifacts/_project/paper/appendix_tost.tex
artifacts/_project/paper/appendix_tost_bootstrap.tex
artifacts/_project/paper/appendix_domain.tex
artifacts/_project/paper/appendix_finer_depth.tex
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:34:47.737221+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:34:47.737388+00:00_

artifacts/_project/paper/related_work.tex:5:\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.
artifacts/_project/paper/related_work.tex:6:Recent work moves beyond binary detection---multi-generator attribution \cite{semeval2024_task8}, collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}.
artifacts/_project/paper/related_work.tex:7:Recent work reframes detection as an out-of-distribution problem \cite{human_texts_outliers}; depth profiling differs in targeting ordinal depth rather than binary membership, with cross-generator transfer as the evaluation axis.
artifacts/_project/paper/related_work.tex:8:We introduce ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal} as a complementary task; repurposing existing detection scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.54--0.71; Table~\ref{tab:baselines}).
artifacts/_project/paper/related_work.tex:11:\looseness=-1 Self-consuming generative models lose distributional coverage via training-loop parameter updates \cite{self_consuming_mad,curse_of_recursion,strong_model_collapse,dohmatob_tale_of_tails,schaeffer_collapse_position}; we instead examine \emph{inference chains} where parameters are fixed.
artifacts/_project/paper/related_work.tex:12:Concurrent iterative-generation studies document complementary phenomena: paraphrasing chains show factuality degradation \cite{broken_telephone}, Markovian analysis bounds distinguishable depth to ${\sim}$3 classes \cite{markovian_chains}, and attractor cycle evidence emerges \cite{attractor_cycles}.
artifacts/_project/paper/related_work.tex:16:\looseness=-1 Dec
…[truncated 6700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:34:47.737559+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 8 · 2026-05-26T10:34:47.737701+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:34:47.737865+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 1 (1-12)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n1. key=cohen1988statistical\ntitle: Statistical Power Analysis for the Behavioral Sciences\nauthor: Cohen, Jacob\npublisher: Lawrence Erlbaum Associates, edition 2nd\nyear: 1988\n\n2. key=detectgpt\ntitle: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\nauthors: Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea\nvenue: ICML 2023\n\n3. key=gltr\ntitle: GLTR: Statistical Detection and Visualization of Generated Text\nauthors: Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\nvenue: ACL System Demonstrations 2019\n\n4. key=dna_gpt\ntitle: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\nauthors: Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng\nvenue: ICLR 2024\n\n5. key=binoculars\ntitle: Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\nauthors: Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom\nvenue: ICML 2024\n\n6. key=fast_detectgpt\ntitle: Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\nauthors: Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue\nvenue: ICLR 2024\n\n7. key=ld_score\ntitle: Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\nauthors: Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul\njournal: arXiv preprint arXiv:2605.01647\nyear: 2026\n\n8. key=diveye\ntitle: Diversity Boosts AI-Generated Text Detection\nauthors: Basani, Advik Raj and Chen, Pin-Yu\nvenue: ICLR 2026\neprint: 2509.18880\n\n9. key=feat_aug_transformer\ntitle: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\nauthors: Mady, Mohamed and Reschke, Johannes and Schuller, Björn\njournal: arXiv preprint arXiv:2605.03969\nyear: 2026\n\n10. key=reliable_detection\ntitle: Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\nauthors: Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil\njournal: Transactions on Machine Learning Research, year 2025\n\n11. key=paraphrase_evades\ntitle: Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\nauthors: Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit\nvenue: NeurIPS 2023\n\n12. key=detection_possibilities\ntitle: Position: On the Possibilities of AI-Generated Text Detection\nauthors: Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong\nvenue: ICML 2024\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 1 (1-12)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n1. key=cohen1988statistical\ntitle: Statistical Power Analysis for the Behavioral Sciences\nauthor: Cohen, Jacob\npublisher: Lawrence Erlbaum Associates, edition 2nd\nyear: 1988\n\n2. key=detectgpt\ntitle: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\nauthors: Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea\nvenue: ICML 2023\n\n3. key=gltr\ntitle: GLTR: Statistical Detection and Visualization of Generated Text\nauthors: Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\nvenue: ACL System Demonstrations 2019\n\n4. key=dna_gpt\ntitle: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\nauthors: Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng\nvenue: ICLR 2024\n\n5. key=binoculars\ntitle: Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\nauthors: Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom\nvenue: ICML 2024\n\n6. key=fast_detectgpt\ntitle: Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\nauthors: Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue\nvenue: ICLR 2024\n\n7. key=ld_score\ntitle: Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\nauthors: Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul\njournal: arXiv preprint arXiv:2605.01647\nyear: 2026\n\n8. key=diveye\ntitle: Diversity Boosts AI-Generated Text Detection\nauthors: Basani, Advik Raj and Chen, Pin-Yu\nvenue: ICLR 2026\neprint: 2509.18880\n\n9. key=feat_aug_transformer\ntitle: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\nauthors: Mady, Mohamed and Reschke, Johannes and Schuller, Björn\njournal: arXiv preprint arXiv:2605.03969\nyear: 2026\n\n10. key=reliable_detection\ntitle: Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\nauthors: Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil\njournal: Transactions on Machine Learning Research, year 2025\n\n11. key=paraphrase_evades\ntitle: Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\nauthors: Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit\nvenue: NeurIPS 2023\n\n12. key=detection_possibilities\ntitle: Position: On the Possibilities of AI-Generated Text Detection\nauthors: Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong\nvenue: ICML 2024\n"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:34:47.738075+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 11 · 2026-05-26T10:34:47.738194+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:34:47.738311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Statistical Power Analysis for the Behavioral Sciences\" Cohen Jacob 1988 Lawrence Erlbaum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Statistical Power Analysis for the Behavioral Sciences\" Cohen Jacob 1988 Lawrence Erlbaum"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:34:47.738436+00:00_

Web search results for query: ""Statistical Power Analysis for the Behavioral Sciences" Cohen Jacob 1988 Lawrence Erlbaum"

Links: [{"title":"Statistical Power Analysis for the Behavioral Sciences | Jacob Cohen |","url":"https://www.taylorfrancis.com/books/mono/10.4324/9780203771587/statistical-power-analysis-behavioral-sciences-jacob-cohen"},{"title":"Statistical Power Analysis for the Behavioral Sciences - 2nd Edition -","url":"https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition): Cohen, Jacob: 9780805802832: Amazon.com: Books","url":"https://www.amazon.com/Statistical-Power-Analysis-Behavioral-Sciences/dp/0805802835"},{"title":"Statistical Power Analysis for the Behavioral Sciences - Jacob Cohen - Google Books","url":"https://books.google.com/books/about/Statistical_Power_Analysis_for_the_Behav.html?id=gA04ngAACAAJ"},{"title":"Statistical Power Analysis for the Behavioral Sciences","url":"https://utstat.toronto.edu/~brunner/oldclass/378f16/readings/CohenPower.pdf"},{"title":"Statistical Power Analysis for the Behavioral Sciences || - DOKUMEN.PUB","url":"https://dokumen.pub/statistical-power-analysis-for-the-behavioral-sciences.html"},{"title":"Statistical power analysis for the behavioral sciences : Cohen, Jacob, 1923-1998 : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/statisticalpower0000cohe_j0l3"},{"title":"Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Hillsdale, NJ Lawrence Erlbaum Associates, Publishers. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2041144"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition) - Cohen, Jacob: 9780805802832 - AbeBooks","url":"https://www.abebooks.com/9780805802832/Statistical-Power-Analysis-Behavioral-Sciences-0805
…[truncated 973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:34:47.738567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" Mitchell ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\" Mitchell ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-26T10:34:47.738718+00:00_

Web search results for query: ""DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature" Mitchell ICML 2023"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"ICML Oral DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"}]

I found the paper! Here's information about it based on the search results:

**Paper Overview:**

The paper was published in the Proceedings of the 40th International Conference on Machine Learning, PMLR 202:24950-2
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:34:47.738870+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 2 (13-24)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n13. key=intrinsic_dim_detection\ntitle: Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\nauthors: Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina\nvenue: NeurIPS 2023\n\n14. key=seqxgpt\ntitle: SeqXGPT: Sentence-Level AI-Generated Text Detection\nauthors: Wang, Pengyu and Li, Linyang and Ren, Ke and Jiang, Botian and Zhang, Dong and Qiu, Xipeng\nvenue: EMNLP 2023\n\n15. key=grover\ntitle: Defending Against Neural Fake News\nauthors: Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin\nvenue: NeurIPS 2019\n\n16. key=release_strategies\ntitle: Release Strategies and the Social Impacts of Language Models\nauthors: Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine\njournal: arXiv preprint arXiv:1908.09203, year 2019\n\n17. key=beyond_binary\ntitle: Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\nauthors: Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\nvenue: ACM Web Conference 2025\n\n18. key=semeval2024_task8\ntitle: SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\nauthors: Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav\nvenue: SemEval 2024\n\n19. key=self_consuming_mad\ntitle: Self-Consuming Generative Models Go MAD\nauthors: Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\nvenue: ICLR 2024\n\n20. key=curse_of_recursion\ntitle: AI models collapse when trained on recursively generated data\nauthors: Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\njournal: Nature, volume 631, pages 755-759, year 2024\n\n21. key=dohmatob_tale_of_tails\ntitle: A Tale of Tails: Model Collapse as a Change of Scaling Laws\nauthors: Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, François and Kempe, Julia\nvenue: ICML 2024\n\n22. key=strong_model_collapse\ntitle: Strong Model Collapse\nauthors: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\nvenue: ICLR 2025\n\n23. key=model_collapse_avoidable\ntitle: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\nauthors: Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\nvenue: COLM 2024\n\n24. key=schaeffer_collapse_position\ntitle: Position: Model Collapse Does Not Mean What You Think\nauthors: Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi\njournal: arXiv preprint arXiv:2503.03150, year 2025\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 2 (13-24)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n13. key=intrinsic_dim_detection\ntitle: Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\nauthors: Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina\nvenue: NeurIPS 2023\n\n14. key=seqxgpt\ntitle: SeqXGPT: Sentence-Level AI-Generated Text Detection\nauthors: Wang, Pengyu and Li, Linyang and Ren, Ke and Jiang, Botian and Zhang, Dong and Qiu, Xipeng\nvenue: EMNLP 2023\n\n15. key=grover\ntitle: Defending Against Neural Fake News\nauthors: Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin\nvenue: NeurIPS 2019\n\n16. key=release_strategies\ntitle: Release Strategies and the Social Impacts of Language Models\nauthors: Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine\njournal: arXiv preprint arXiv:1908.09203, year 2019\n\n17. key=beyond_binary\ntitle: Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\nauthors: Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\nvenue: ACM Web Conference 2025\n\n18. key=semeval2024_task8\ntitle: SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\nauthors: Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav\nvenue: SemEval 2024\n\n19. key=self_consuming_mad\ntitle: Self-Consuming Generative Models Go MAD\nauthors: Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\nvenue: ICLR 2024\n\n20. key=curse_of_recursion\ntitle: AI models collapse when trained on recursively generated data\nauthors: Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\njournal: Nature, volume 631, pages 755-759, year 2024\n\n21. key=dohmatob_tale_of_tails\ntitle: A Tale of Tails: Model Collapse as a Change of Scaling Laws\nauthors: Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, François and Kempe, Julia\nvenue: ICML 2024\n\n22. key=strong_model_collapse\ntitle: Strong Model Collapse\nauthors: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\nvenue: ICLR 2025\n\n23. key=model_collapse_avoidable\ntitle: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\nauthors: Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\nvenue: COLM 2024\n\n24. key=schaeffer_collapse_position\ntitle: Position: Model Collapse Does Not Mean What You Think\nauthors: Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi\njournal: arXiv preprint arXiv:2503.03150, year 2025\n"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:34:47.739101+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"GLTR: Statistical Detection and Visualization of Generated Text\" Gehrmann Strobelt Rush ACL 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"GLTR: Statistical Detection and Visualization of Generated Text\" Gehrmann Strobelt Rush ACL 2019"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:34:47.739243+00:00_

Web search results for query: ""GLTR: Statistical Detection and Visualization of Generated Text" Gehrmann Strobelt Rush ACL 2019"

Links: [{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ACL Anthology","url":"https://aclanthology.org/P19-3019/"},{"title":"[1906.04043] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://arxiv.org/abs/1906.04043"},{"title":"GLTR: Statistical detection and visualization of generated text for ACL 2019 - IBM Research","url":"https://research.ibm.com/publications/gltr-statistical-detection-and-visualization-of-generated-text"},{"title":"[PDF] GLTR: Statistical Detection and Visualization of Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLTR:-Statistical-Detection-and-Visualization-of-Gehrmann-Strobelt/867db5097ad6aaef098c60b0845785b440eca49a"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text","url":"https://scholar.harvard.edu/files/gehrmann/files/acl_demo_2019_gltr_statistical_detection_of_fake_text_5.pdf"},{"title":"GLTR from MIT-IBM Watson AI Lab and HarvardNLP","url":"http://gltr.io/"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Sebastian Gehrmann","url":"https://scholar.harvard.edu/gehrmann/publications/gltr-statistical-detection-and-visualization-generated-text"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text | Request PDF","url":"https://www.researchgate.net/publication/335781128_GLTR_Statistical_Detection_and_Visualization_of_Generated_Text"},{"title":"GLTR: Statistical Detection and Visualization of Generated Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190604043G/abstract"},{"title":"[Quick Review] GLTR: Statistical Detection and Visualization of Generated Text","url":"https://liner.com/review/gltr-statistical-detection-and-visualization-generated-text"}]

I found the paper! Here's what I found about "GLTR: Statistical Detection and Visualiz
…[truncated 1247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:34:47.739383+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\" Yang ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\" Yang ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:34:47.739508+00:00_

Web search results for query: ""DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text" Yang ICLR 2024"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | OpenReview","url":"https://openreview.net/forum?id=Xlayxj2fWp"},{"title":"ICLR Poster DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://iclr.cc/virtual/2024/poster/18444"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/Yang0WPWC24.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.nec-labs.com/blog/dna-gpt-divergent-n-gram-analysis-for-training-free-detection-of-gpt-generated-text/"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://paperreading.club/page?id=167623"}]

I found comprehensive information about the paper "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text" by Yang et al., which was presented at ICLR 2024.

## Overview

DNA-GPT is a novel 
…[truncated 1480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:34:47.739658+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 22 · 2026-05-26T10:34:47.739769+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:34:47.739875+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" Tulchinskii NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\" Tulchinskii NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:34:47.739993+00:00_

Web search results for query: ""Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" Tulchinskii NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://neurips.cc/virtual/2023/poster/72624"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html"},{"title":"[2306.04723] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/abs/2306.04723"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | OpenReview","url":"https://openreview.net/forum?id=8uOZ0kNji6"},{"title":"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://arxiv.org/pdf/2306.04723"},{"title":"Intrinsic dimension estimation for robust detection of AI-generated texts | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667828"},{"title":"[PDF] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a5fab19553e623e8787383cb3da76b8a3c42a8f4"},{"title":"[Quick Review] Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts","url":"https://liner.com/review/intrinsic-dimension-estimation-for-robust-detection-of-aigenerated-texts"},{"title":"Are AI Detectors Good Enough? A Survey on Quality of Datasets with","url":"https://openreview.net/pdf?id=WDhwO4Hhq2"}]

I found the paper you're looking for! Here's what I found:

The paper "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" was authored by Eduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Pio
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:34:47.740126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SeqXGPT: Sentence-Level AI-Generated Text Detection\" Wang Pengyu EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SeqXGPT: Sentence-Level AI-Generated Text Detection\" Wang Pengyu EMNLP 2023"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:34:47.740250+00:00_

Web search results for query: ""SeqXGPT: Sentence-Level AI-Generated Text Detection" Wang Pengyu EMNLP 2023"

Links: [{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.73/"},{"title":"[2310.08903] SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://arxiv.org/abs/2310.08903"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection | Request PDF","url":"https://www.researchgate.net/publication/376393940_SeqXGPT_Sentence-Level_AI-Generated_Text_Detection"},{"title":"[Quick Review] SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://liner.com/review/seqxgpt-sentencelevel-aigenerated-text-detection"},{"title":"GitHub - Jihuai-wpy/SeqXGPT: SeqXGPT: An advance method for sentence-level AI-generated text detection.","url":"https://github.com/Jihuai-wpy/SeqXGPT"},{"title":"Paper page - SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://huggingface.co/papers/2310.08903"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection","url":"https://arxiv.org/html/2310.08903v2"},{"title":"SeqXGPT: Sentence-Level AI-Generated Text Detection | Papers With Code","url":"https://paperswithcode.com/paper/seqxgpt-sentence-level-ai-generated-text"}]

I found comprehensive information about this paper. Here's what I found:

## SeqXGPT: Sentence-Level AI-Generated Text Detection

SeqXGPT is a paper by Pengyu Wang, Linyang Li, Ke Ren, Botian Jiang, Dong Zhang, and Xipeng Qiu, published at EMNLP 2023. It was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 1144–1156, in Singapore.

### Problem and Approach

The paper introduces a sentence-level detection challenge by synthesizing a dataset that contains documents that are polished with LLMs, where the documents contain sentences written by humans and sentences modified by LLMs. SeqXGPT is built based on convolution and self-attention networks and is
…[truncated 736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:34:47.740397+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 3 (25-37)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n25. key=seddik_synthetic_data\ntitle: How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\nauthors: Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane\nvenue: COLM 2024\n\n26. key=qlora\ntitle: QLoRA: Efficient Finetuning of Quantized LLMs\nauthors: Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke\nvenue: NeurIPS 2023\n\n27. key=dsir\ntitle: Data Selection for Language Models via Importance Resampling\nauthors: Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\nvenue: NeurIPS 2023\n\n28. key=qurating\ntitle: QuRating: Selecting High-Quality Data for Training Language Models\nauthors: Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\nvenue: ICML 2024\n\n29. key=ccnet\ntitle: CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\nauthors: Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzmán, Francisco and Joulin, Armand and Grave, Edouard\nvenue: LREC 2020\n\n30. key=watermark_llm\ntitle: A Watermark for Large Language Models\nauthors: Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom\nvenue: ICML 2023\n\n31. key=synthid_text\ntitle: Scalable Watermarking for Identifying Large Language Model Outputs\nauthors: Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet\njournal: Nature, volume 634, pages 818-823, year 2024\n\n32. key=aaronson_watermark\ntitle: Watermarking GPT Outputs\nauthors: Aaronson, Scott and Kirchner, Jan Hendrik\nyear: 2022, note: Blog post, url: https://scottaaronson.blog/?p=6823\n\n33. key=chainwash\ntitle: Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\nauthors: Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\njournal: arXiv preprint arXiv:2605.05503, year 2026\n\n34. key=curious_decline\ntitle: The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\nauthors: Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloé\nvenue: Findings of NAACL 2024\n\n35. key=writing_diversity\ntitle: Does Writing with Language Models Reduce Content Diversity?\nauthors: Padmakumar, Vishakh and He, He\nvenue: ICLR 2024\n\n36. key=nucleus_sampling\ntitle: The Curious Case of Neural Text Degeneration\nauthors: Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\nvenue: ICLR 2020\n\n37. key=welleck_unlikelihood\ntitle: Neural Text Generation with Unlikelihood Training\nauthors: Welleck, Sean and Kulikov, Ilia and Roller, Stephen and Dinan, Emily and Cho, Kyunghyun and Weston, Jason\nvenue: ICLR 2020\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 3 (25-37)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n25. key=seddik_synthetic_data\ntitle: How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\nauthors: Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane\nvenue: COLM 2024\n\n26. key=qlora\ntitle: QLoRA: Efficient Finetuning of Quantized LLMs\nauthors: Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke\nvenue: NeurIPS 2023\n\n27. key=dsir\ntitle: Data Selection for Language Models via Importance Resampling\nauthors: Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\nvenue: NeurIPS 2023\n\n28. key=qurating\ntitle: QuRating: Selecting High-Quality Data for Training Language Models\nauthors: Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\nvenue: ICML 2024\n\n29. key=ccnet\ntitle: CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\nauthors: Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzmán, Francisco and Joulin, Armand and Grave, Edouard\nvenue: LREC 2020\n\n30. key=watermark_llm\ntitle: A Watermark for Large Language Models\nauthors: Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom\nvenue: ICML 2023\n\n31. key=synthid_text\ntitle: Scalable Watermarking for Identifying Large Language Model Outputs\nauthors: Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet\njournal: Nature, volume 634, pages 818-823, year 2024\n\n32. key=aaronson_watermark\ntitle: Watermarking GPT Outputs\nauthors: Aaronson, Scott and Kirchner, Jan Hendrik\nyear: 2022, note: Blog post, url: https://scottaaronson.blog/?p=6823\n\n33. key=chainwash\ntitle: Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\nauthors: Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\njournal: arXiv preprint arXiv:2605.05503, year 2026\n\n34. key=curious_decline\ntitle: The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\nauthors: Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloé\nvenue: Findings of NAACL 2024\n\n35. key=writing_diversity\ntitle: Does Writing with Language Models Reduce Content Diversity?\nauthors: Padmakumar, Vishakh and He, He\nvenue: ICLR 2024\n\n36. key=nucleus_sampling\ntitle: The Curious Case of Neural Text Degeneration\nauthors: Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\nvenue: ICLR 2020\n\n37. key=welleck_unlikelihood\ntitle: Neural Text Generation with Unlikelihood Training\nauthors: Welleck, Sean and Kulikov, Ilia and Roller, Stephen and Dinan, Emily and Cho, Kyunghyun and Weston, Jason\nvenue: ICLR 2020\n"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:34:47.740646+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\" Hans ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\" Hans ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:34:47.740793+00:00_

Web search results for query: ""Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" Hans ICML 2024"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text - Zilliz Learn","url":"https://zilliz.com/learn/spotting-llms-with-binoculars-zero-shot-detection-of-machine-generated-text"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/html/2401.12070v3"},{"title":"Paper page - Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://huggingface.co/papers/2401.12070"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | OpenReview","url":"https://openreview.net/forum?id=iARAKITHTH"},{"title":"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://proceedings.mlr.press/v235/hans24a.html"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[Literature Review] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://www.themoonlight.io/en/review/spotting-llms-with-binoculars-zero-shot-detection-of-machine-generated-text"}]

I found comprehensive information about this paper. Here are the key details:

## Paper Overview

"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is by Abhimanyu Hans and 7 other authors.

## Core Method

The paper proposes that a score based on contrasting two closely related language models is highly accurate at separating human-generated and machine-generated text, requiring only simple calculations using a pair of pre-trained LLMs. Specifically, the Binoculars detector works by computing log perplexity usin
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:34:47.740938+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" Bao ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\" Bao ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:34:47.741067+00:00_

Web search results for query: ""Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature" Bao ICLR 2024"

Links: [{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"ICLR Poster Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://iclr.cc/virtual/2024/poster/19201"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | OpenReview","url":"https://openreview.net/forum?id=Bpcgcr8E8Z"},{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6b8c6f846c3575e1d1ad496abea28826-Abstract-Conference.html"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature | alphaXiv","url":"https://www.alphaxiv.org/abs/2310.05130"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"}]

Based on the search results, here's information about the Fast-DetectGPT paper:

## Overview

The paper introduces the concept of con
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:34:47.741204+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Defending Against Neural Fake News\" Zellers Rowan NeurIPS 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Defending Against Neural Fake News\" Zellers Rowan NeurIPS 2019"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:34:47.741331+00:00_

Web search results for query: ""Defending Against Neural Fake News" Zellers Rowan NeurIPS 2019"

Links: [{"title":"Grover - Defending Against Neural Fake News","url":"https://rowanzellers.com/grover/"},{"title":"Defending Against Neural Fake News","url":"https://papers.neurips.cc/paper_files/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Paper.pdf"},{"title":"Reviews: Defending Against Neural Fake News","url":"https://proceedings.neurips.cc/paper/2019/file/3e9f0fc9b2f89e043bc6233994dfcf76-Reviews.html"},{"title":"GitHub - rowanz/grover: Code for Defending Against Neural Fake News, https://rowanzellers.com/grover/ · GitHub","url":"https://github.com/rowanz/grover"},{"title":"Defending Against Neural Fake News - researchr publication","url":"https://researchr.org/publication/ZellersHRBFRC19"},{"title":"Defending against neural fake news | Proceedings of the 33rd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3454287.3455099"},{"title":"Defending Against Neural Fake News","url":"http://rowanzellers.com/grover/?domain=wired.com&date=June+1%2C+2019&authors=&title=Deep+Yearning+and+Artificial+Righteousness+now+generating+sermons&article=We"},{"title":"[1905.12616] Defending Against Neural Fake News","url":"https://arxiv.org/abs/1905.12616"},{"title":"[PDF] Defending Against Neural Fake News | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defending-Against-Neural-Fake-News-Zellers-Holtzman/ad7129af0644dbcafa9aa2f111cb76526ea444a1"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** Defending Against Neural Fake News

**Authors:** Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi

**Publication:** Published in Advances in Neural Information Processing Systems 32 in 2019

**Main Contribution:** The paper introduced Grover, a state-of-the-art model for detecting neural fake news. The paper addresses dual
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:34:47.741461+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Release Strategies and the Social Impacts of Language Models\" Solaiman arXiv 1908.09203"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Release Strategies and the Social Impacts of Language Models\" Solaiman arXiv 1908.09203"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:34:47.741603+00:00_

Web search results for query: ""Release Strategies and the Social Impacts of Language Models" Solaiman arXiv 1908.09203"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models | Request PDF","url":"https://www.researchgate.net/publication/335419868_Release_Strategies_and_the_Social_Impacts_of_Language_Models"},{"title":"link the \"Release Strategies and the Social Impacts of Language Models\" paper · openai-community/roberta-large-openai-detector at 913a6ec","url":"https://huggingface.co/openai-community/roberta-large-openai-detector/commit/913a6ec95e2254ae3b31b2037de05a2ac23583e1"}]

I found the paper for you! Here's what I found about it:

**"Release Strategies and the Social Impacts of Language Models"** (arXiv 1908.09203)

This report discusses OpenAI's work related to the release of its GPT-2 language model, authored by Irene Solaiman and 14 other co-authors including Miles Brundage, Jack Clark, Amanda Askell, and others.

**Key Focus:**

The paper discusses staged release, which allows time between model releases to conduct risk and benefit analyses as model size
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:34:47.741749+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 37 · 2026-05-26T10:34:47.741862+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:34:47.741968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\" Seddik"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\" Seddik"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:34:47.742090+00:00_

Web search results for query: ""How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" Seddik"

Links: [{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"How bad is training on synthetic data? A statistical analysis of language model collapse | OpenReview","url":"https://openreview.net/forum?id=t3z6UlV09o"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/html/2502.07164v1"}]

I found the paper you're looking for. Here are the key details:

**Title:** "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"

**Authors:** Mohamed El Amine Seddik and 4 other authors (Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah)

**Publication:** Posted to arXiv on April 7, 2024

**Main Findings:**

The paper studies model collapse, which refers to the deterioration in performance that occurs when new models are trai
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:34:47.742227+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"QLoRA: Efficient Finetuning of Quantized LLMs\" Dettmers NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"QLoRA: Efficient Finetuning of Quantized LLMs\" Dettmers NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:34:47.742357+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 4 (38-49)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n38. key=stamatatos_survey\ntitle: A Survey of Modern Authorship Attribution Methods\nauthors: Stamatatos, Efstathios\njournal: Journal of the American Society for Information Science and Technology, volume 60, number 3, pages 538-556, year 2009\n\n39. key=koppel_authorship\ntitle: Computational Methods in Authorship Attribution\nauthors: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\njournal: Journal of the American Society for Information Science and Technology, volume 60, number 1, pages 9-26, year 2009\n\n40. key=uchendu_attribution\ntitle: Authorship Attribution for Neural Text Generation\nauthors: Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\nvenue: EMNLP 2020\n\n41. key=munir_looking_glass\ntitle: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\nauthors: Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed\nvenue: EACL 2021\n\n42. key=briesch_self_consuming\ntitle: Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\nauthors: Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\njournal: arXiv preprint arXiv:2311.16822, year 2023\n\n43. key=broken_telephone\ntitle: LLM as a Broken Telephone: Iterative Generation Distorts Information\nauthors: Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\nvenue: ACL 2025\n\n44. key=markovian_chains\ntitle: Markovian Generation Chains in Large Language Models\nauthors: Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry\njournal: arXiv preprint arXiv:2603.11228, year 2026\n\n45. key=attractor_cycles\ntitle: Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\nauthors: Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue\nvenue: ACL 2025, eprint: 2502.15208\n\n46. key=min_k_percent\ntitle: Detecting Pretraining Data from Large Language Models\nauthors: Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke\nvenue: ICLR 2024\n\n47. key=koike_mia_detection\ntitle: Machine Text Detectors are Membership Inference Attacks\nauthors: Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki\njournal: arXiv preprint arXiv:2510.19492, year 2025\n\n48. key=wu_survey_2025\ntitle: A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\nauthors: Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai\njournal: Computational Linguistics (MIT Press), year 2025\n\n49. key=jawahar_survey\ntitle: Automatic Detection of Machine Generated Text: A Critical Survey\nauthors: Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\nvenue: COLING 2020\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 4 (38-49)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n38. key=stamatatos_survey\ntitle: A Survey of Modern Authorship Attribution Methods\nauthors: Stamatatos, Efstathios\njournal: Journal of the American Society for Information Science and Technology, volume 60, number 3, pages 538-556, year 2009\n\n39. key=koppel_authorship\ntitle: Computational Methods in Authorship Attribution\nauthors: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\njournal: Journal of the American Society for Information Science and Technology, volume 60, number 1, pages 9-26, year 2009\n\n40. key=uchendu_attribution\ntitle: Authorship Attribution for Neural Text Generation\nauthors: Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\nvenue: EMNLP 2020\n\n41. key=munir_looking_glass\ntitle: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\nauthors: Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed\nvenue: EACL 2021\n\n42. key=briesch_self_consuming\ntitle: Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\nauthors: Briesch, Martin and Sobania, Dominik and Rothlauf, Franz\njournal: arXiv preprint arXiv:2311.16822, year 2023\n\n43. key=broken_telephone\ntitle: LLM as a Broken Telephone: Iterative Generation Distorts Information\nauthors: Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\nvenue: ACL 2025\n\n44. key=markovian_chains\ntitle: Markovian Generation Chains in Large Language Models\nauthors: Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry\njournal: arXiv preprint arXiv:2603.11228, year 2026\n\n45. key=attractor_cycles\ntitle: Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing\nauthors: Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue\nvenue: ACL 2025, eprint: 2502.15208\n\n46. key=min_k_percent\ntitle: Detecting Pretraining Data from Large Language Models\nauthors: Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke\nvenue: ICLR 2024\n\n47. key=koike_mia_detection\ntitle: Machine Text Detectors are Membership Inference Attacks\nauthors: Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and Callison-Burch, Chris and Okazaki, Naoaki\njournal: arXiv preprint arXiv:2510.19492, year 2025\n\n48. key=wu_survey_2025\ntitle: A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\nauthors: Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai\njournal: Computational Linguistics (MIT Press), year 2025\n\n49. key=jawahar_survey\ntitle: Automatic Detection of Machine Generated Text: A Critical Survey\nauthors: Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\nvenue: COLING 2020\n"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:34:47.742627+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast-DetectGPT Bao Guangsheng authors list ICLR 2024 arxiv 2310.05130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast-DetectGPT Bao Guangsheng authors list ICLR 2024 arxiv 2310.05130"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T10:34:47.742773+00:00_

Web search results for query: "Fast-DetectGPT Bao Guangsheng authors list ICLR 2024 arxiv 2310.05130"

Links: [{"title":"[2310.05130] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130"},{"title":"[2310.05130v3] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v3"},{"title":"[2310.05130v2] Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/abs/2310.05130v2"},{"title":"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://arxiv.org/html/2310.05130v3"},{"title":"GitHub - baoguangsheng/fast-detect-gpt: Code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\". · GitHub","url":"https://github.com/baoguangsheng/fast-detect-gpt"},{"title":"Paper page - Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature","url":"https://huggingface.co/papers/2310.05130"},{"title":"Fast, Interpretable AI-Generated Text Detection Using Style Embeddings","url":"https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/GiuliaZoeSocolofRitikaKacholia.pdf"},{"title":"(PDF) FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC- TION OF MACHINE-GENERATED TEXT VIA CONDI- TIONAL PROBABILITY CURVATURE","url":"https://www.researchgate.net/publication/388188914_FAST-DETECTGPT_EFFICIENT_ZERO-SHOT_DETEC-_TION_OF_MACHINE-GENERATED_TEXT_VIA_CONDI-_TIONAL_PROBABILITY_CURVATURE"},{"title":"Guangsheng Bao PhD Candidate Advisor: Prof. Yue Zhang","url":"https://baoguangsheng.github.io/assets/pdf/cv.pdf"}]

Based on the search results, here is the authors list for the Fast-DetectGPT paper (arXiv 2310.05130) published at
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:34:47.742911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond Perplexity: Character Distribution Signatures\" MDTA Benchmark Narayanasamy arXiv 2605.01647"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond Perplexity: Character Distribution Signatures\" MDTA Benchmark Narayanasamy arXiv 2605.01647"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:34:47.743035+00:00_

Web search results for query: ""Beyond Perplexity: Character Distribution Signatures" MDTA Benchmark Narayanasamy arXiv 2605.01647"

Links: [{"title":"[2605.01647] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647"},{"title":"[2605.01647v1] Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/abs/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260501647N/abstract"},{"title":"[2605.13652] Beyond Perplexity: A Geometric and Spectral Study of Low-Rank Pre-Training","url":"https://arxiv.org/abs/2605.13652"},{"title":"Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in","url":"https://arxiv.org/pdf/2601.03505"}]

I found the paper! Here are the key details about this research:

## Paper Overview

The paper is titled "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection" by Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, and Fardina Fathmiul Alam from the University of Maryland, College Park.

## Main Contribution

Training-free AI text detection methods primarily rely on model log-probabilities through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions. The authors introduce an alternative detection signal based on character distribution signatures.

They provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distr
…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:34:47.743171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen Pin-Yu ICLR 2026 arXiv 2509.18880"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen Pin-Yu ICLR 2026 arXiv 2509.18880"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:34:47.743285+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition\" Cheng Zihao ACM Web Conference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition\" Cheng Zihao ACM Web Conference 2025"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:34:47.743407+00:00_

Web search results for query: ""Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition" Cheng Zihao ACM Web Conference 2025"

Links: [{"title":"[2410.14259] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/html/2410.14259v2"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text","url":"https://arxiv.org/pdf/2410.14259"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714770"},{"title":"[2410.14259v1] Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement","url":"https://arxiv.org/abs/2410.14259v1"},{"title":"Computation and Language Oct 2024","url":"https://arxiv.org/list/cs.CL/2024-10?skip=1225&show=500"},{"title":"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement – Own Your AI","url":"https://ownyourai.com/beyond-binary-towards-fine-grained-llm-generated-text-detection-via-role-recognition-and-involvement-measurement/"}]

I found the paper you're looking for! Here are the key details:

"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement" is a paper by Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, and Haizhou Li, presented at the ACM Web Conference 2025 (WWW '25) in April 28-May 2, 2025, in Sydney, NSW, Australia.

**Paper Overview:**

The paper addresses the rapid development of large language models (LLMs) like ChatGPT and the widespread presence of LLM-generated content on social media platforms, raising concerns a
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:34:47.743542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\" Wang Yuxia"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\" Wang Yuxia"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:34:47.743689+00:00_

Web search results for query: ""QLoRA: Efficient Finetuning of Quantized LLMs" Dettmers NeurIPS 2023"

Links: [{"title":"[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/abs/2305.14314"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs | OpenReview","url":"https://openreview.net/forum?id=OUIFPHEgJU"},{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://openreview.net/pdf?id=OUIFPHEgJU"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html"},{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf"},{"title":"[PDF] QLoRA: Efficient Finetuning of Quantized LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QLoRA:-Efficient-Finetuning-of-Quantized-LLMs-Dettmers-Pagnoni/32ac52069e562d4f900afee70bdca63f53461481"},{"title":"GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub","url":"https://github.com/artidoro/qlora"},{"title":"NeurIPS Poster QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://neurips.cc/virtual/2023/poster/71815"},{"title":"QLORA: efficient finetuning of quantized LLMs","url":"https://dl.acm.org/doi/10.5555/3666122.3666563"}]

I found comprehensive information about the QLoRA paper. Here are the key details:

## Paper Overview

QLoRA is an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).

## Authors and Conference

The paper was authored by Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, a
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T10:34:47.743821+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Selection for Language Models via Importance Resampling\" Xie Santurkar NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Selection for Language Models via Importance Resampling\" Xie Santurkar NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:34:47.743949+00:00_

Web search results for query: ""Data Selection for Language Models via Importance Resampling" Xie Santurkar NeurIPS 2023"

Links: [{"title":"NeurIPS Poster Data Selection for Language Models via Importance Resampling","url":"https://neurips.cc/virtual/2023/poster/70154"},{"title":"[2302.03169] Data Selection for Language Models via Importance Resampling","url":"https://arxiv.org/abs/2302.03169"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/6b9aa8f418bde2840d5f4ab7a02f663b-Abstract-Conference.html"},{"title":"Data Selection for Language Models via Importance Resampling | OpenReview","url":"https://openreview.net/forum?id=uPSQv0leAu"},{"title":"[PDF] Data Selection for Language Models via Importance Resampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Data-Selection-for-Language-Models-via-Importance-Xie-Santurkar/74013b7cfa0fc524803350fca51341004565eb22"},{"title":"Data Selection for Language Models via Importance Resampling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230203169X/abstract"},{"title":"[Quick Review] Data Selection for Language Models via Importance Resampling","url":"https://liner.com/review/data-selection-for-language-models-via-importance-resampling"},{"title":"[2302.03169v3] Data Selection for Language Models via Importance Resampling","url":"http://arxiv.org/abs/2302.03169v3"},{"title":"Data Selection for Language Models via Importance Resampling","url":"https://www.researchgate.net/publication/368333487_Data_Selection_for_Language_Models_via_Importance_Resampling"},{"title":"GitHub - p-lambda/dsir: DSIR large-scale data selection framework for language model training · GitHub","url":"https://github.com/p-lambda/dsir"}]

I found the paper you're looking for. Here's information about it:

## "Data Selection for Language Models via Importance Resampling"

**Authors:** Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy L
…[truncated 1193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:34:47.744084+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"QuRating: Selecting High-Quality Data for Training Language Models\" Wettig ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"QuRating: Selecting High-Quality Data for Training Language Models\" Wettig ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:34:47.744207+00:00_

Web search results for query: ""QuRating: Selecting High-Quality Data for Training Language Models" Wettig ICML 2024"

Links: [{"title":"GitHub - princeton-nlp/QuRating: [ICML 2024] Selecting High-Quality Data for Training Language Models","url":"https://github.com/princeton-nlp/QuRating"},{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Language Models","url":"https://iclr.cc/virtual/2024/21159"},{"title":"QuRating: selecting high-quality data for training language ...","url":"https://dl.acm.org/doi/10.5555/3692070.3694241"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models","url":"https://proceedings.mlr.press/v235/wettig24a.html"},{"title":"[PDF] QuRating: Selecting High-Quality Data for Training Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QuRating:-Selecting-High-Quality-Data-for-Training-Wettig-Gupta/34efdeaf0a78d6906b4da7335afc7182df11f639"},{"title":"[2402.09739v3] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739v3"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240209739W/abstract"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models | OpenReview","url":"https://openreview.net/forum?id=GLGYYqPwjy"}]

I found comprehensive information about the QuRating paper. Here are the key details:

## Paper Overview

QuRating is a method for selecting pre-training data that can capture human intuitions about data quality. The authors are Alexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen, and it was published at the 41st International Conference on Machine Learning (ICML 2024).

## Key Methodology

The paper investigates four qualities - writing style, required expertise, facts & tr
…[truncated 881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:34:47.744342+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 56 · 2026-05-26T10:34:47.744450+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:34:47.744555+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey of Modern Authorship Attribution Methods\" Stamatatos"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey of Modern Authorship Attribution Methods\" Stamatatos"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T10:34:47.744695+00:00_

Web search results for query: ""A Survey of Modern Authorship Attribution Methods" Stamatatos"

Links: [{"title":"A survey of modern authorship attribution methods - Stamatatos - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21001"},{"title":"1 A Survey of Modern Authorship Attribution Methods Efstathios Stamatatos","url":"https://icsdweb.aegean.gr/stamatatos/papers/survey.pdf"},{"title":"A survey of modern authorship attribution methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-survey-of-modern-authorship-attribution-methods-Stamatatos/d25c27c7a3e9f41f150e8eadbad34c1c05d67510"},{"title":"A Survey of Modern Authorship Attribution Methods | Request PDF","url":"https://www.researchgate.net/publication/220435062_A_Survey_of_Modern_Authorship_Attribution_Methods"},{"title":"A survey of modern authorship attribution methods | Journal of the American Society for Information Science and Technology","url":"https://dl.acm.org/doi/10.5555/1527090.1527102"},{"title":"dblp: A survey of modern authorship attribution methods.","url":"https://dblp.org/rec/journals/jasis/Stamatatos09.html"},{"title":"Stamatatos, E. (2009) A Survey of Modern Authorship Attribution Methods. Journal of the American Society for Information Science and Technology, 60, 538-556. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2540164"},{"title":"(PDF) A survey of modern authorship attribution methods (2009) | Efstathios Stamatatos | 1366 Citations","url":"https://scispace.com/papers/a-survey-of-modern-authorship-attribution-methods-2lb4q2gu7n"},{"title":"A survey of modern authorship attribution methods - researchr publication","url":"https://researchr.org/publication/Stamatatos09"}]

I found the survey paper you're looking for. Here are the key details:

**Publication Information:**
Stamatatos, E. (20
…[truncated 1140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:34:47.744823+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Computational Methods in Authorship Attribution\" Koppel Schler Argamon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Computational Methods in Authorship Attribution\" Koppel Schler Argamon"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:34:47.744953+00:00_

Web search results for query: ""Computational Methods in Authorship Attribution" Koppel Schler Argamon"

Links: [{"title":"Computational methods in authorship attribution - Koppel - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.20961"},{"title":"(PDF) Computational Methods in Authorship Attribution","url":"https://www.researchgate.net/publication/220433607_Computational_Methods_in_Authorship_Attribution"},{"title":"\"Computational Methods in Authorship Attribution\" by Moshe Koppel, Jonathan Schler et al.","url":"https://touroscholar.touro.edu/president_pubs/275/"},{"title":"Computational methods in authorship attribution","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i1p9-26.html"},{"title":"Computational methods in authorship attribution - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/computational-methods-in-authorship-attribution-4/"},{"title":"Computational methods in authorship attribution | Journal of the American Society for Information Science and Technology","url":"https://dl.acm.org/citation.cfm?id=1484627"},{"title":"Survey of Methods in Computational Literary Studies - 5 What is Authorship Attribution?","url":"https://methods.clsinfra.io/what-author.html"},{"title":"Computational methods in authorship attribution | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Computational-methods-in-authorship-attribution-Koppel-Schler/97b4a29cc2209f8ff0c89383a42d59ba56ac6604"},{"title":"1 Computational Methods in Authorship Attribution","url":"https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf"},{"title":"(PDF) Computational methods in authorship attribution","url":"https://www.academia.edu/15373725/Computational_methods_in_authorship_attribution"}]

Based on the search results, I found information about the paper you're looking for:

"Computational Methods in Authorship Attribution" is a paper b
…[truncated 802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T10:34:47.745092+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu Le Shu Lee EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Authorship Attribution for Neural Text Generation\" Uchendu Le Shu Lee EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:34:47.745215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\" Wenzek LREC 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\" Wenzek LREC 2020"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:34:47.745343+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 5 (50-62)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n50. key=pythia\ntitle: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\nauthors: Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar\nvenue: ICML 2023\n\n51. key=olmo\ntitle: OLMo: Accelerating the Science of Language Models\nauthors: Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh\nvenue: ACL 2024\n\n52. key=qwen3\ntitle: Qwen3 Technical Report\nauthors: Qwen Team\njournal: arXiv preprint arXiv:2505.09388, year 2025\n\n53. key=ghostbuster\ntitle: Ghostbuster: Detecting Text Ghostwritten by Large Language Models\nauthors: Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan\nvenue: NAACL 2024\n\n54. key=two_birds\ntitle: Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text\nauthors: Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan\njournal: arXiv preprint arXiv:2508.14190, year 2025\n\n55. key=beyond_final_actor\ntitle: Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection\nauthors: Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan\nvenue: ACL 2026\n\n56. key=gutierrez_ordinal_survey\ntitle: Ordinal Regression Methods: Survey and Experimental Study\nauthors: Gutiérrez, Pedro Antonio and Pérez-Ortiz, María and Sánchez-Monedero, Javier and Fernández-Navarro, Francisco and Hervás-Martínez, César\njournal: IEEE Transactions on Knowledge and Data Engineering, volume 28, number 1, pages 127-146, year 2016\n\n57. key=coral_ordinal\ntitle: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\nauthors: Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\njournal: Pattern Recognition Letters, volume 140, pages 325-331, year 2020\n\n58. key=frank_hall_ordinal\ntitle: A Simple Approach to Ordinal Classification\nauthors: Frank, Eibe and Hall, Mark\nvenue: ECML 2001\n\n59. key=corn_ordinal\ntitle: Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\nauthors: Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian\njournal: Pattern Analysis and Applications, volume 26, pages 941-955, year 2023\n\n60. key=diaz_soft_labels_ordinal\ntitle: Soft Labels for Ordinal Regression\nauthors: Diaz, Raul and Marathe, Amit\nvenue: CVPR 2019\n\n61. key=kasa_ordinality_nlp\ntitle: Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques\nauthors: Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa\nvenue: Findings of ACL 2024\n\n62. key=xgboost\ntitle: XGBoost: A Scalable Tree Boosting System\nauthors: Chen, Tianqi and Guestrin, Carlos\nvenue: KDD 2016\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 5 (50-62)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n50. key=pythia\ntitle: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\nauthors: Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar\nvenue: ICML 2023\n\n51. key=olmo\ntitle: OLMo: Accelerating the Science of Language Models\nauthors: Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh\nvenue: ACL 2024\n\n52. key=qwen3\ntitle: Qwen3 Technical Report\nauthors: Qwen Team\njournal: arXiv preprint arXiv:2505.09388, year 2025\n\n53. key=ghostbuster\ntitle: Ghostbuster: Detecting Text Ghostwritten by Large Language Models\nauthors: Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan\nvenue: NAACL 2024\n\n54. key=two_birds\ntitle: Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text\nauthors: Rao, Zixin and Mohamed, Youssef and Liu, Shang and Liu, Zeyan\njournal: arXiv preprint arXiv:2508.14190, year 2025\n\n55. key=beyond_final_actor\ntitle: Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection\nauthors: Li, Yang and Sheng, Qiang and Wang, Zhengjia and Yang, Yehan and Wang, Danding and Cao, Juan\nvenue: ACL 2026\n\n56. key=gutierrez_ordinal_survey\ntitle: Ordinal Regression Methods: Survey and Experimental Study\nauthors: Gutiérrez, Pedro Antonio and Pérez-Ortiz, María and Sánchez-Monedero, Javier and Fernández-Navarro, Francisco and Hervás-Martínez, César\njournal: IEEE Transactions on Knowledge and Data Engineering, volume 28, number 1, pages 127-146, year 2016\n\n57. key=coral_ordinal\ntitle: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\nauthors: Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\njournal: Pattern Recognition Letters, volume 140, pages 325-331, year 2020\n\n58. key=frank_hall_ordinal\ntitle: A Simple Approach to Ordinal Classification\nauthors: Frank, Eibe and Hall, Mark\nvenue: ECML 2001\n\n59. key=corn_ordinal\ntitle: Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\nauthors: Shi, Xintong and Cao, Wenzhi and Raschka, Sebastian\njournal: Pattern Analysis and Applications, volume 26, pages 941-955, year 2023\n\n60. key=diaz_soft_labels_ordinal\ntitle: Soft Labels for Ordinal Regression\nauthors: Diaz, Raul and Marathe, Amit\nvenue: CVPR 2019\n\n61. key=kasa_ordinality_nlp\ntitle: Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques\nauthors: Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and Roychowdhury, Sumegh and Priyatam, Pattisapu and Bhanushali, Anish and Murthy, Prasanna Srinivasa\nvenue: Findings of ACL 2024\n\n62. key=xgboost\ntitle: XGBoost: A Scalable Tree Boosting System\nauthors: Chen, Tianqi and Guestrin, Carlos\nvenue: KDD 2016\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:34:47.745679+00:00_

Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen Pin-Yu ICLR 2026 arXiv 2509.18880"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Pin-Yu Chen on X: \"Happy to see this work published at @TmlrOrg We show that diversity-driven features (computed by a very small LM, such as GPT-2) are powerful for detecting AI-written content. Try out our online detector at https://t.co/7sLfMdcmDG Kudos to Advik for leading this work.\" / X","url":"https://x.com/pinyuchenTW/status/2031014939846995984"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

I found the paper you're looking for! Here's what I found about the research:

**Paper Details:**
The paper "Diversity Boosts AI-Generated Text Detection" was submitted on September 23, 2025 and last revised on
…[truncated 1053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:34:47.745869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Feature-Augmented Transformers for Robust AI-Text Detection\" Mady Reschke Schuller arXiv 2605.03969"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Feature-Augmented Transformers for Robust AI-Text Detection\" Mady Reschke Schuller arXiv 2605.03969"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:34:47.746012+00:00_

Web search results for query: ""Feature-Augmented Transformers for Robust AI-Text Detection" Mady Reschke Schuller arXiv 2605.03969"

Links: [{"title":"[2605.03969] Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/abs/2605.03969"},{"title":"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators","url":"https://arxiv.org/html/2605.03969"},{"title":"[2410.08113] Robust AI-Generated Text Detection by Restricted Embeddings","url":"https://arxiv.org/abs/2410.08113"},{"title":"[2507.05157] AI Generated Text Detection Using Instruction Fine-tuned Large Language and Transformer-Based Models","url":"https://arxiv.org/abs/2507.05157"},{"title":"Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/html/2403.13335v1"},{"title":"[2601.03812] AI Generated Text Detection","url":"https://arxiv.org/abs/2601.03812"},{"title":"[2509.20375] Assessing Classical Machine Learning and Transformer-based Approaches for Detecting AI-Generated Research Text","url":"https://arxiv.org/abs/2509.20375"},{"title":"Enhancing Text Authenticity: A Novel Hybrid Approach for AI-Generated Text Detection","url":"https://arxiv.org/html/2406.06558v1"},{"title":"Efficient detection of AI-generated scientific abstracts with a lightweight transformer | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-35203-3"},{"title":"[2403.13335] Adaptive Ensembles of Fine-Tuned Transformers for LLM-Generated Text Detection","url":"https://arxiv.org/abs/2403.13335"}]

I found the paper! Here are the key details about the paper from arXiv:

**Title:** Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators

**Authors:** Mohamed Mady, Johannes Reschke, Björn Schuller

**arXiv ID:** 2605.03969 (submitted May 5, 2026)

**Key Findings:**

AI-generated text is produced at scale across diverse domains and heterogeneous genera
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:34:47.746156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected?\" Sadasivan Kumar Balasubramanian Wang Feizi TMLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected?\" Sadasivan Kumar Balasubramanian Wang Feizi TMLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:34:47.746281+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected?" Sadasivan Kumar Balasubramanian Wang Feizi TMLR 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Venue:** Action editor: Kamalika Chaudhuri (TMLR - Transactions on Machine Learning Research)

**Summary:**
The paper stress-tests the robustness of AI text detectors in the presence of an att
…[truncated 548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:34:47.746426+00:00_

Web search results for query: ""SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection" Wang Yuxia"

Links: [{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"[PDF] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/c56eab12bd00e2fe28868af21d518044d66df00d"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/bfca76cf8884cdacbcb4db85e0b442bc"},{"title":"Semeval-2024 task 8: Multigenerator, multidomain, and multilingual black-box machine-generated text detection","url":"https://airi.net/articles/semeval-2024-task-8-multigenerator-multidomain-and-multilingual-black-box-machine-generated-text-det/"}]

I found detailed information about SemEval-2024 Task 8. Here are the key findings:

## Overview

SemEval-2024 Task 8 was on Multigenerator, Multidomain, and Multilingual Machine-Generated Text Detection. The task was organized by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mah
…[truncated 991 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-26T10:34:47.746562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Self-Consuming Generative Models Go MAD\" Alemohammad ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Self-Consuming Generative Models Go MAD\" Alemohammad ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:34:47.746730+00:00_

Web search results for query: ""Self-Consuming Generative Models Go MAD" Alemohammad ICLR 2024"

Links: [{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Two Papers at ICLR 2024","url":"https://dsp.rice.edu/2024/03/16/two-papers-at-iclr/"}]

I found the paper! Here's a summary of the search results:

"Self-Consuming Generative Models Go MAD" is a paper by Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk, and it was published at the International Conference on Learning Representations (ICLR) in January 2024.

The paper addresses a critical problem in generative AI. Advances in generative AI have led to the temptation to use AI-synthesized data to train next-generation m
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:34:47.746866+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AI models collapse when trained on recursively generated data\" Shumailov Nature 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AI models collapse when trained on recursively generated data\" Shumailov Nature 2024"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:34:47.746990+00:00_

Web search results for query: ""AI models collapse when trained on recursively generated data" Shumailov Nature 2024"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"Using AI to train AI: Model collapse could be coming for LLMs, say researchers","url":"https://techxplore.com/news/2024-07-ai-collapse-llms.html"}]

I found the research you're looking for. Here are the key findings:

The paper "AI models collapse when trained on recursively generated data" by Shumailov et al. was published in Nature 631, 755–759 (2024).

Analysis shows that indiscriminately training generative artificial intelligence on real and generated content, usually 
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:34:47.747127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:34:47.747254+00:00_

Web search results for query: ""CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data" Wenzek LREC 2020"

Links: [{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://aclanthology.org/2020.lrec-1.494/"},{"title":"[1911.00359] CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://arxiv.org/abs/1911.00359"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from ...","url":"https://aclanthology.org/2020.lrec-1.494.pdf"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - ACL Anthology","url":"https://arne.chark.eu/anthology/2020.lrec-1.494/"},{"title":"Papers with Code - CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://paperswithcode.com/paper/ccnet-extracting-high-quality-monolingual"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/245540f9667239913db153792be9fff73/dblp"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data - DataoceanAI","url":"https://dataoceanai.com/ccnet-extracting-high-quality-monolingual-datasets-from-web-crawl-data/"},{"title":"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data","url":"https://www.researchgate.net/publication/337005596_CCNet_Extracting_High_Quality_Monolingual_Datasets_from_Web_Crawl_Data"}]

I found the paper you're looking for. Here's the information:

## CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data

The paper was authored by Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Joulin, and Edouard Grave, and was published in the Proceedings of the Twelfth Language Resources and Evaluation Conference (LREC 2020), pages 4003–4012, in Marseille, France.

### Summary

The paper describes an automatic pipeline to extract massive hi
…[truncated 630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:34:47.747388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Watermark for Large Language Models\" Kirchenbauer ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Watermark for Large Language Models\" Kirchenbauer ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:34:47.747511+00:00_

Web search results for query: ""A Watermark for Large Language Models" Kirchenbauer ICML 2023"

Links: [{"title":"A Watermark for Large Language Models","url":"https://proceedings.mlr.press/v202/kirchenbauer23a.html"},{"title":"[2301.10226] A Watermark for Large Language Models","url":"https://arxiv.org/abs/2301.10226"},{"title":"[PDF] A Watermark for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Watermark-for-Large-Language-Models-Kirchenbauer-Geiping/cb5b71a622aff47014d4f28a958679629a8b6363"},{"title":"ICML Poster A Watermark for Large Language Models","url":"https://icml.cc/virtual/2023/poster/24544"},{"title":"A Watermark for Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10522346-watermark-large-language-models"},{"title":"dblp: A Watermark for Large Language Models.","url":"https://dblp.org/rec/conf/icml/KirchenbauerGWK23.html"},{"title":"A Watermark for Large Language Models - TL;DR With Paper Author","url":"https://arize.com/blog/a-watermark-for-large-language-models/"},{"title":"A Watermark for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/367388838_A_Watermark_for_Large_Language_Models"},{"title":"A Watermark for Large Language Models","url":"https://arxiv.org/pdf/2301.10226"}]

I found the paper! Here are the key details about "A Watermark for Large Language Models" by Kirchenbauer et al., published at ICML 2023:

## Overview
The paper proposes watermarking model output to mitigate potential harms of large language models by embedding signals into generated text that are invisible to humans but algorithmically detectable from a short span of tokens.

## Authors
The paper is authored by John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.

## Publication Details
It was published in the Proceedings of the 40th International Conference on Machine Learning, PMLR 202:17061-17084, 2023.

## Key Technical
…[truncated 994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:34:47.747661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Scalable Watermarking for Identifying Large Language Model Outputs\" SynthID Nature 2024 Dathathri"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Scalable Watermarking for Identifying Large Language Model Outputs\" SynthID Nature 2024 Dathathri"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:34:47.747791+00:00_

Web search results for query: ""Authorship Attribution for Neural Text Generation" Uchendu Le Shu Lee EMNLP 2020"

Links: [{"title":"Authorship Attribution for Neural Text Generation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.673/"},{"title":"Authorship Attribution for Neural Text Generation | Request PDF","url":"https://www.researchgate.net/publication/347235360_Authorship_Attribution_for_Neural_Text_Generation"},{"title":"Authorship attribution for neural text generation - Penn State","url":"https://pure.psu.edu/en/publications/authorship-attribution-for-neural-text-generation"},{"title":"GitHub - AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation · GitHub","url":"https://github.com/AdaUchendu/Authorship-Attribution-for-Neural-Text-Generation"},{"title":"Authorship Attribution for Neural Text Generation.","url":"https://dblp.org/rec/conf/emnlp/UchenduLSL20.xml"},{"title":"[PDF] Authorship Attribution for Neural Text Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Authorship-Attribution-for-Neural-Text-Generation-Uchendu-Le/9da9cab545bd1534a8c953bb66e611243dcee24d"},{"title":"Papers with Code - Authorship Attribution for Neural Text Generation","url":"https://paperswithcode.com/paper/authorship-attribution-for-neural-text"},{"title":"Authorship Attribution for Neural Text Generation - researchr publication","url":"https://researchr.org/publication/UchenduLSL20"}]

I found the paper! Here are the results:

"Authorship Attribution for Neural Text Generation" is a paper by Adaku Uchendu, Thai Le, Kai Shu, and Dongwon Lee, published at EMNLP 2020. It was published in the Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 8384–8395, Online.

The work investigates the authorship attribution problem in three versions, and finds that most generators still generate texts significantly different from human-written ones, thereby making three problems easier to solve.
…[truncated 535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:34:47.747927+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\" Munir EACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\" Munir EACL"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:34:47.748054+00:00_

Web search results for query: ""Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models" Munir EACL"

Links: [{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.155/"},{"title":"EACL2021: Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models","url":"https://www.virtual2021.eacl.org/paper_main.753.html"},{"title":"[PDF] Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Through-the-Looking-Glass:-Learning-to-Attribute-by-Munir-Batool/03e6b951e3665d28a7beeef87fcb1c9baecfd396"},{"title":"Through the looking glass: Learning to attribute synthetic text generated by language models","url":"https://papertalk.org/papertalks/28247"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - researchr publication","url":"https://researchr.org/publication/MunirBSSZ21"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models | Request PDF","url":"https://www.researchgate.net/publication/355428226_Through_the_Looking_Glass_Learning_to_Attribute_Synthetic_Text_Generated_by_Language_Models"},{"title":"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models - About Me","url":"http://shaoormunir.com/publications/1-through-the-looking-glass/"},{"title":"Fareed Zaffar - ACL Anthology","url":"https://aclanthology.org/people/fareed-zaffar/unverified/"}]

I found the paper you're looking for! Here's the information:

**"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models"** was published by Shaoor Munir, Brishna Batool, Zubair Shafiq, Padmini Srinivasan, and Fareed Zaffar at EACL 2021 (the 16th Conference of the European Chapt
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T10:34:47.748184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Large Language Models Suffer From Their Own Output\" Briesch Sobania Rothlauf arXiv 2311.16822"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Large Language Models Suffer From Their Own Output\" Briesch Sobania Rothlauf arXiv 2311.16822"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:34:47.748314+00:00_

Web search results for query: ""Large Language Models Suffer From Their Own Output" Briesch Sobania Rothlauf arXiv 2311.16822"

Links: [{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"[PDF] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Suffer-From-Their-Own-Output:-Briesch-Sobania/c24ed03689adc2a075004c6619f43f7f6230fe4b"},{"title":"[2311.16822v2] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/abs/2311.16822v2"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-suffer-from-their-own"},{"title":"[2311.16822] Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://ar5iv.labs.arxiv.org/html/2311.16822"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2311.16822"},{"title":"Large Language Models Suffer From Their Own Output:","url":"https://arxiv.org/pdf/2311.16822v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"}]

I found the paper! Here's information about the research:

**Paper Details:**
The p
…[truncated 1075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:34:47.748445+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 85 · 2026-05-26T10:34:47.748552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:34:47.748680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\" Biderman ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\" Biderman ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T10:34:47.748798+00:00_

Web search results for query: ""Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling" Biderman ICML 2023"

Links: [{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling [Quick Review]","url":"https://liner.com/review/pythia-suite-for-analyzing-large-language-models-across-training-and"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | OpenReview","url":"https://openreview.net/forum?id=bpRTAnJ8LW"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"},{"title":"ICML Poster Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://icml.cc/virtual/2023/poster/24093"},{"title":"Paper Summary: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://queirozf.com/entries/paper-summary-pythia-a-suite-for-analyzing-large-language-models-across-training-and-scaling"},{"title":"ICML 2023 Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling Oral","url":"https://icml.cc/virtual/2023/oral/25487"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling" by Stella Biderman and 12 other authors


…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:34:47.748939+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OLMo: Accelerating the Science of Language Models\" Groeneveld ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OLMo: Accelerating the Science of Language Models\" Groeneveld ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-26T10:34:47.749071+00:00_

Web search results for query: ""OLMo: Accelerating the Science of Language Models" Groeneveld ACL 2024"

Links: [{"title":"OLMo: Accelerating the Science of Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.841/"},{"title":"[2402.00838] OLMo: Accelerating the Science of Language Models","url":"https://arxiv.org/abs/2402.00838"},{"title":"OLMo: Accelerating the Science of Language Models | Request PDF","url":"https://www.researchgate.net/publication/384217754_OLMo_Accelerating_the_Science_of_Language_Models"},{"title":"[PDF] OLMo: Accelerating the Science of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OLMo:-Accelerating-the-Science-of-Language-Models-Groeneveld-Beltagy/ac45bbf9940512d9d686cf8cd3a95969bc313570"},{"title":"OLMo: Accelerating the Science of Language Models Dirk Groeneveld>a> Iz Beltagy>a> - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/olmo-accelerating-the-science-of-language-models-dirk-groenevelds"},{"title":"Allen School News » A way with words and trillions of tokens: Allen School researchers recognized at ACL 2024 for expanding the capabilities of language models","url":"https://news.cs.washington.edu/2024/10/08/a-way-with-words-and-trillions-of-tokens-allen-school-researchers-recognized-at-acl-2024-for-expanding-the-capabilities-of-language-models/"},{"title":"OLMo : Accelerating the Science of Language Models Dirk Groeneveldα Iz Beltagyα","url":"https://arxiv.org/pdf/2402.00838"},{"title":"OLMo: Accelerating the Science of Language Models","url":"https://www.researchhub.com/paper/6025716/olmo-accelerating-the-science-of-language-models"},{"title":"[2402.00838v4] OLMo: Accelerating the Science of Language Models","url":"http://arxiv.org/abs/2402.00838v4"}]

I found the paper you're looking for! Here are the key details:

"OLMo: Accelerating the Science of Language Models" was published by Dirk Groeneveld, Iz Beltagy, Evan Walsh, Akshita Bhagia, Rodney Kinney, O
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:34:47.749198+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 Technical Report arXiv 2505.09388 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 Technical Report arXiv 2505.09388 2025"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:34:47.749329+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries batch 6 (63-74)",
  "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n63. key=lakens_equivalence\ntitle: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\nauthors: Lakens, Daniël\njournal: Social Psychological and Personality Science, volume 8, number 4, pages 355-362, year 2017\n\n64. key=llama3\ntitle: The Llama 3 Herd of Models\nauthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others\njournal: arXiv preprint arXiv:2407.21783, year 2024\n\n65. key=mistral7b\ntitle: Mistral 7B\nauthors: Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others\njournal: arXiv preprint arXiv:2310.06825, year 2023\n\n66. key=strobl_conditional_2008\ntitle: Conditional Variable Importance for Random Forests\nauthors: Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim\njournal: BMC Bioinformatics, volume 9, pages 307, year 2008\n\n67. key=dolma\ntitle: Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research\nauthors: Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle\nvenue: ACL 2024\n\n68. key=fineweb\ntitle: The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\nauthors: Penedo, Guilherme and Kydlíček, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas\nvenue: NeurIPS Datasets and Benchmarks Track 2024\n\n69. key=mapping_llm_science\ntitle: Mapping the Increasing Use of LLMs in Scientific Papers\nauthors: Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.\nvenue: Conference on Language Modeling (COLM) 2024\n\n70. key=monitoring_ai_review\ntitle: Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\nauthors: Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.\nvenue: ICML 2024\n\n71. key=raid\ntitle: RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\nauthors: Dugan, Liam and Hwang, Alyssa and Trhlík, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris\nvenue: ACL 2024, pages 12463-12492\n\n72. key=human_texts_outliers\ntitle: Human Texts Are Outliers: Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\nauthors: Li, Yafu and Hu, Zhilin and Guo, Zetian and Zhao, Wei and Li, Lixin and Hou, Yuanxin\njournal: arXiv preprint arXiv:2510.08602, year 2025\n\n73. key=xu_spectrum_detection\ntitle: Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood\nauthors: Xu, Yang and Wang, Yu and An, Hao and Liu, Zhichen and Li, Yongyuan\njournal: arXiv preprint arXiv:2406.19874, year 2024\n\n74. key=mauve\ntitle: MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers\nauthors: Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid\nvenue: NeurIPS 2021\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 6 (63-74)",
    "prompt": "You are verifying academic bibliography entries for correctness. For each entry below, use WebSearch to verify: (a) paper exists, (b) author names are correct, (c) year is correct, (d) title is accurate, (e) venue is correct, (f) volume/pages if applicable. Search with query like `\"paper title\" first_author_lastname` or `paper title site:arxiv.org`.\n\nReturn results in this exact format for each entry:\n### [key] — title (year)\n- **Exists**: ✓/✗\n- **Authors**: ✓/✗ (detail if wrong)\n- **Year**: ✓/✗ (detail if wrong)\n- **Title**: ✓/✗ (detail if wrong)\n- **Venue**: ✓/✗ (detail if wrong)\n- **Notes**: ...\n\nHere are the entries to verify:\n\n63. key=lakens_equivalence\ntitle: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\nauthors: Lakens, Daniël\njournal: Social Psychological and Personality Science, volume 8, number 4, pages 355-362, year 2017\n\n64. key=llama3\ntitle: The Llama 3 Herd of Models\nauthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and others\njournal: arXiv preprint arXiv:2407.21783, year 2024\n\n65. key=mistral7b\ntitle: Mistral 7B\nauthors: Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and Casas, Diego de las and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and others\njournal: arXiv preprint arXiv:2310.06825, year 2023\n\n66. key=strobl_conditional_2008\ntitle: Conditional Variable Importance for Random Forests\nauthors: Strobl, Carolin and Boulesteix, Anne-Laure and Kneib, Thomas and Augustin, Thomas and Zeileis, Achim\njournal: BMC Bioinformatics, volume 9, pages 307, year 2008\n\n67. key=dolma\ntitle: Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research\nauthors: Soldaini, Luca and Kinney, Rodney and Bhagia, Akshita and Schwenk, Dustin and Atkinson, David and Authur, Russell and Bogin, Ben and Chandu, Khyathi and Dumas, Jennifer and Elazar, Yanai and Hofmann, Valentin and Jha, Ananya Harsh and Kumar, Sachin and Lucy, Li and Lyu, Xinxi and Lambert, Nathan and Magnusson, Ian and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Ravichander, Abhilasha and Richardson, Kyle and Shen, Zejiang and Strubell, Emma and Subramani, Nishant and Tafjord, Oyvind and Walsh, Evan Pete and Zettlemoyer, Luke and Smith, Noah A. and Hajishirzi, Hannaneh and Beltagy, Iz and Groeneveld, Dirk and Dodge, Jesse and Lo, Kyle\nvenue: ACL 2024\n\n68. key=fineweb\ntitle: The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\nauthors: Penedo, Guilherme and Kydlíček, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas\nvenue: NeurIPS Datasets and Benchmarks Track 2024\n\n69. key=mapping_llm_science\ntitle: Mapping the Increasing Use of LLMs in Scientific Papers\nauthors: Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.\nvenue: Conference on Language Modeling (COLM) 2024\n\n70. key=monitoring_ai_review\ntitle: Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\nauthors: Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.\nvenue: ICML 2024\n\n71. key=raid\ntitle: RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\nauthors: Dugan, Liam and Hwang, Alyssa and Trhlík, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris\nvenue: ACL 2024, pages 12463-12492\n\n72. key=human_texts_outliers\ntitle: Human Texts Are Outliers: Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\nauthors: Li, Yafu and Hu, Zhilin and Guo, Zetian and Zhao, Wei and Li, Lixin and Hou, Yuanxin\njournal: arXiv preprint arXiv:2510.08602, year 2025\n\n73. key=xu_spectrum_detection\ntitle: Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood\nauthors: Xu, Yang and Wang, Yu and An, Hao and Liu, Zhichen and Li, Yongyuan\njournal: arXiv preprint arXiv:2406.19874, year 2024\n\n74. key=mauve\ntitle: MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers\nauthors: Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid\nvenue: NeurIPS 2021\n"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-26T10:34:47.749539+00:00_

Web search results for query: ""A Tale of Tails: Model Collapse as a Change of Scaling Laws" Dohmatob ICML 2024"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"ICML Poster A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://icml.cc/virtual/2024/poster/34339"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"}]

I found the paper! Here's what I discovered:

"A Tale of Tails: Model Collapse as a Change of Scaling Laws" is a paper by Dohmatob, Feng, Yang, Charton, and Kempe, presented at the 41st International Conference on Machine Learning (ICML 2024).

**Overview:**

The paper develops a theoretical framework of model collapse through the lens of scaling laws. The motivation is that as popular AI models are widely used, the ecosystem of online data 
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-26T10:34:47.749707+00:00_

Web search results for query: "Qwen3 Technical Report arXiv 2505.09388 2025"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"},{"title":"Qwen3 Technical Report - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250509388Y/abstract"}]

I found the Qwen3 Technical Report (arXiv 2505.09388) from May 2025. Here are the key details:

## Overview
Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities.

## Model Architecture
The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

## Key Innovations
A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, eliminating the need to switch between different models and enabling dynamic mode switching based on user queries or chat templates.

Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity.

## Multilingual Capabilities
Compared to its predecessor Qwen2.5, Qwen3 expa
…[truncated 347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:34:47.749858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM as a Broken Telephone: Iterative Generation Distorts Information\" Mohamed Geng Vazirgiannis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM as a Broken Telephone: Iterative Generation Distorts Information\" Mohamed Geng Vazirgiannis"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:34:47.749985+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR publication year 2025 OpenReview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Can AI-Generated Text be Reliably Detected\" TMLR publication year 2025 OpenReview"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:34:47.750104+00:00_

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
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
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

_source line 97 · 2026-05-26T10:34:47.750212+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-26T10:34:47.750328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\" Dohmatob authors full list"
  }
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:34:47.750446+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\" Verma NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\" Verma NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-26T10:34:47.750561+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\" Lakens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses\" Lakens"
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T10:34:47.750709+00:00_

Web search results for query: ""LLM as a Broken Telephone: Iterative Generation Distorts Information" Mohamed Geng Vazirgiannis"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.371/"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"GitHub - amr-mohamedd/LLM-as-a-Broken-Telephone: [ACL 2025] Code implementation for the \"LLM as a Broken Telephone: Iterative Generation Distorts Information\" paper.","url":"https://github.com/amr-mohamedd/LLM-as-a-Broken-Telephone"},{"title":"Paper page - LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://huggingface.co/papers/2502.20258"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258"},{"title":"dblp: LLM as a Broken Telephone: Iterative Generation Distorts Information.","url":"https://dblp.org/rec/journals/corr/abs-2502-20258.html"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"[Quick Review] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://liner.com/review/llm-as-broken-telephone-iterative-generation-distorts-information"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts ...","url":"https://aclanthology.org/2025.acl-long.371.pdf"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.20258v1"}]

I found the research paper you're looking for. Here are the key details:

**Paper Title:** "LLM as a Broken Telephone: Iterative Generation Distorts Information"

**Authors:** Amr Mohamed, Mingmeng Geng, Michalis Vazirgia
…[truncated 966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:34:47.750852+00:00_

Web search results for query: "Sadasivan "Can AI-Generated Text be Reliably Detected" TMLR publication year 2025 OpenReview"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? Stress ...","url":"https://openreview.net/pdf/a06fe5303ab3d0c635e565d4eae91e5ab7ac8175.pdf"}]

Based on the search results, I found the paper you're looking for:

"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" is by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

The paper was published at TMLR (Transactions on Machine Learning Research). According to the search results, the submission was previously submitted to TMLR, and the revised version was pub
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:34:47.750991+00:00_

Web search results for query: ""A Tale of Tails: Model Collapse as a Change of Scaling Laws" Dohmatob authors full list"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://openreview.net/pdf/c028ead5595978096e7ba1f2c41cc3bb709058f9.pdf"},{"title":"A tale of tails: model collapse as a change of scaling laws","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"Paper page - A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://huggingface.co/papers/2402.07043"},{"title":"Elvis DOHMATOB on LinkedIn: A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://www.linkedin.com/posts/elvis-dohmatob-53bba979_a-tale-of-tails-model-collapse-as-a-change-activity-7163099409554079744-Fx1e"}]

Based on the search results, the authors of "A Tale of Tails: Model Collapse as a Change of Scaling Laws" are Dohmatob, E., Feng, Y., Yang, P., Charton, F., and Kempe, J.

The full list of authors is:
1. **Elvis Dohmatob**
2. **Yunzhen Feng**
3. **Pu Yang**
4.
…[truncated 253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-26T10:34:47.751131+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Markovian Generation Chains in Large Language Models\" Geng Mohamed Shang Vazirgiannis Poibeau arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Markovian Generation Chains in Large Language Models\" Geng Mohamed Shang Vazirgiannis Poibeau arXiv 2603"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:34:47.751253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\" Krishna NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\" Krishna NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:34:47.751380+00:00_

Web search results for query: ""Ghostbuster: Detecting Text Ghostwritten by Large Language Models" Verma NAACL 2024"

Links: [{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.95/"},{"title":"GitHub - vivek3141/ghostbuster: Ghostbuster: Detecting Text Ghostwritten by Large Language Models (NAACL 2024) · GitHub","url":"https://github.com/vivek3141/ghostbuster"},{"title":"[2305.15047] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/abs/2305.15047"},{"title":"Detecting Text Ghostwritten by Large Language Models","url":"https://aclanthology.org/2024.naacl-long.95.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models Vivek Verma","url":"https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/382631441_Ghostbuster_Detecting_Text_Ghostwritten_by_Large_Language_Models"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://arxiv.org/html/2305.15047v3"},{"title":"Ghostbuster: Detecting Text Ghostwritten by Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/ghostbuster-detecting-text-ghostwritten-by-large-language"},{"title":"[Quick Review] Ghostbuster: Detecting Text Ghostwritten by Large Language Models","url":"https://liner.com/review/ghostbuster-detecting-text-ghostwritten-by-large-language-models"}]

I found the paper! Here are the details about **"Ghostbuster: Detecting Text Ghostwritten by Large Language Models"** by Verma et al. at NAACL 2024:

## Paper Information
The paper was authored by Vivek Verma, Eve Fleisig, Nicholas Tomlin, and Dan Klein, and was presented at the 2024 Conference of the North American Chapter of the Association for Computational Ling
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:34:47.751524+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Strong Model Collapse\" Dohmatob Elvis ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Strong Model Collapse\" Dohmatob Elvis ICLR 2025"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:34:47.751691+00:00_

Web search results for query: ""Scalable Watermarking for Identifying Large Language Model Outputs" SynthID Nature 2024 Dathathri"

Links: [{"title":"Scalable watermarking for identifying large language model outputs | Nature","url":"https://www.nature.com/articles/s41586-024-08025-4"},{"title":"Scalable watermarking for identifying large language model outputs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scalable-watermarking-for-identifying-large-model-Dathathri-See/89bd8efe0b9c0427cb7814d7b8c2b0190d2ffa9e"},{"title":"(PDF) Scalable watermarking for identifying large language model outputs","url":"https://www.researchgate.net/publication/385176946_Scalable_watermarking_for_identifying_large_language_model_outputs"},{"title":"Scalable watermarking for identifying large language model outputs - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11499265/"},{"title":"Scalable watermarking for identifying large language model outputs","url":"https://ideas.repec.org/a/nat/nature/v634y2024i8035d10.1038_s41586-024-08025-4.html"},{"title":"Scalable watermarking for identifying large language model outputs – ScienceOpen","url":"https://www.scienceopen.com/document?vid=e36b034b-6be1-439b-bccb-f413efc57773"},{"title":"Scalable watermarking for identifying large language model outputs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024Natur.634..818D/abstract"}]

Based on the web search results, here's what I found about this research:

## Overview

Large language models (LLMs) have enabled the generation of high-quality synthetic text, often indistinguishable from human-written content, at a scale that can markedly affect the nature of the information ecosystem.

## SynthID-Text Solution

SynthID-Text is a production-ready text watermarking scheme that preserves text quality and enables high detection accuracy, with minimal latency overhead. SynthID-Text does not affect LLM training and modifies only the sampling procedure; watermark detection is compu
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-26T10:34:47.751845+00:00_

Web search results for query: ""Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses" Lakens"

Links: [{"title":"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/28736600/"},{"title":"Cornell Statistical Consulting Unit Equivalence Testing","url":"https://cscu.cornell.edu/wp-content/uploads/equiv.pdf"},{"title":"Equivalence Tests - Daniël Lakens, 2017","url":"https://journals.sagepub.com/doi/10.1177/1948550617697177"},{"title":"Equivalence Testing for Psychological Research: A Tutorial - Daniël Lakens, Anne M. Scheel, Peder M. Isager, 2018","url":"https://journals.sagepub.com/doi/10.1177/2515245918770963"},{"title":"The 20% Statistician: Equivalence Testing and the Second Generation P-Value","url":"http://daniellakens.blogspot.com/2018/08/equivalence-testing-and-second.html"},{"title":"(PDF) Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses","url":"https://www.researchgate.net/publication/316752481_Equivalence_Tests_A_Practical_Primer_for_t_Tests_Correlations_and_Meta-Analyses"},{"title":"GitHub - Lakens/TOSTER: TOST equivalence test and power functions · GitHub","url":"https://github.com/Lakens/TOSTER"},{"title":"[PDF] Equivalence Tests | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Equivalence-Tests-Lakens/3590ee5cd78891e1cdc95429ba3bedd0ae433704"},{"title":"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses | FORRT - Framework for Open and Reproducible Research Training","url":"https://forrt.org/curated_resources/equivalence-tests-a-practical-primer-for/"},{"title":"Equivalence Testing With TOSTER","url":"https://www.psychologicalscience.org/observer/equivalence-testing-with-toster"}]

Here are the search results for "Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses" by Lakens:

## Publication Details

The article was written by Daniël L
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-26T10:34:47.751995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text\" Rao arXiv 2508.14190"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text\" Rao arXiv 2508.14190"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:34:47.752122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Aaronson \"Watermarking GPT Outputs\" blog post 2022 scottaaronson.blog"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Aaronson \"Watermarking GPT Outputs\" blog post 2022 scottaaronson.blog"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-26T10:34:47.752245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Llama 3 Herd of Models\" Grattafiori arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Llama 3 Herd of Models\" Grattafiori arXiv 2407.21783"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:34:47.752364+00:00_

Web search results for query: ""Markovian Generation Chains in Large Language Models" Geng Mohamed Shang Vazirgiannis Poibeau arXiv 2603"

Links: [{"title":"Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/html/2603.11228"},{"title":"[2603.11228] Markovian Generation Chains in Large Language Models","url":"https://arxiv.org/abs/2603.11228"},{"title":"Large Language Models as Markov Chains","url":"https://arxiv.org/html/2410.02724v1"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information | Request PDF","url":"https://www.researchgate.net/publication/394300051_LLM_as_a_Broken_Telephone_Iterative_Generation_Distorts_Information"},{"title":"[2410.02724v1] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724v1"},{"title":"[2410.02724] Large Language Models as Markov Chains","url":"https://arxiv.org/abs/2410.02724"},{"title":"Markovian Generation Chains in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nTDn4OMiym"},{"title":"[2502.20258] LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/abs/2502.20258"},{"title":"Large Language Models as Markov Chains","url":"https://www.alphaxiv.org/abs/2410.02724"}]

I found the paper you're looking for! Here are the details:

**"Markovian Generation Chains in Large Language Models"**

**Authors:** Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, and Thierry Poibeau

**ArXiv ID:** 2603.11228 (Submitted March 11, 2026)

**Summary:**

The paper addresses the question of how texts evolve when they are repeatedly processed by LLMs. The authors define this iterative inference process as Markovian generation chains, where each step takes a specific prompt template and the previous output as input, without including any prior memory.

**Key Findings:**

In iterative rephrasing and round-trip translation experiments, the output either converges to a small recurrent set or cont
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:34:47.752512+00:00_

Web search results for query: ""Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense" Krishna NeurIPS 2023"

Links: [{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://arxiv.org/pdf/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230313408K/abstract"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Paraphrasing evades detectors of AI-generated text, bu
…[truncated 1338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:34:47.752678+00:00_

Web search results for query: ""Strong Model Collapse" Dohmatob Elvis ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://par.nsf.gov/servlets/purl/10649434"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=MQXrTMonT1"},{"title":"Elvis Dohmatob - Concordia University","url":"https://www.concordia.ca/faculty/elvis-dohmatob.html"},{"title":"dblp: Elvis Dohmatob","url":"https://dblp.org/pid/134/9794.html"},{"title":"Elvis Dohmatob (@dohmatobelvis) / Posts / X","url":"https://x.com/dohmatobelvis?lang=en"}]

I found the paper! Here's what I found about "Strong Model Collapse" by Elvis Dohmatob and colleagues at ICLR 2025:

## Overview

The paper is authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe from Meta FAIR, Concordia University, Mila, NYU, and UCLA.

## Main Findings

The paper considers a supervised regression setting and establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus.

The key results show that even the smallest fraction of synthetic data (e.g., as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance.

## Research Questions

The authors further investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse.

The paper has been published at ICLR 2025 and is also available on arXiv (arXiv:2410.04840).


REMINDER: Yo
…[truncated 88 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:34:47.752829+00:00_

Web search results for query: ""Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text" Rao arXiv 2508.14190"

Links: [{"title":"Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://arxiv.org/html/2508.14190v1"},{"title":"[2508.14190] Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://arxiv.org/abs/2508.14190"},{"title":"Two Birds with One Stone: Multi-Task Detection","url":"https://arxiv.org/pdf/2508.14190"},{"title":"(PDF) Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://www.researchgate.net/publication/394790500_Two_Birds_with_One_Stone_Multi-Task_Detection_and_Attribution_of_LLM-Generated_Text"},{"title":"Accepted Papers – EAI securecomm 2025","url":"https://securecomm.eai-conferences.org/2025/accepted-papers/"},{"title":"Paper page - &lt;think> So let's replace this phrase with insult... &lt;/think> Lessons learned from generation of toxic texts with LLMs","url":"https://huggingface.co/papers/2509.08358"},{"title":"EAI SecureComm 2025 conference program Day 1. July 4ᵗʰ(Friday) 9:00-9:10","url":"https://securecomm.eai-conferences.org/2025/wp-content/uploads/sites/944/2025/07/eai-securecomm-2025-full-program.pdf"}]

I found the paper! Here's information about it:

**Title:** Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text

**Authors:** Zixin Rao, Youssef Mohamed, Shang Liu, and Zeyan Liu

**ArXiv ID:** 2508.14190

**Overview:**
The paper presents DA-MTL, a multi-task learning framework that simultaneously addresses both text detection and authorship attribution. The approach uses shared representations to solve two tasks: (1) distinguishing between human-written and machine-generated text, and (2) identifying the specific source LLM of machine-generated text.

**Key Points:**
- DA-MTL was evaluated on nine datasets and four backbone models, demonstrating i
…[truncated 586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:34:47.752985+00:00_

Web search results for query: "Aaronson "Watermarking GPT Outputs" blog post 2022 scottaaronson.blog"

Links: [{"title":"Scottaaronson","url":"https://www.scottaaronson.com/talks/watermark.ppt"},{"title":"November 2022 – Shtetl-Optimized","url":"https://scottaaronson.blog/?m=202211"},{"title":"Shtetl-Optimized » Blog Archive » My AI Safety Lecture for UT Effective Altruism","url":"https://scottaaronson.blog/?p=6823"},{"title":"Watermarking Needs Input Repetition Masking","url":"https://arxiv.org/html/2504.12229v1"},{"title":"AXRP Episode 20 - 'Reform' AI Alignment with Scott ...","url":"https://www.lesswrong.com/posts/nsygJvidfgidmgKqX/axrp-episode-20-reform-ai-alignment-with-scott-aaronson"},{"title":"Scott Aaronson worked on watermarking text from GPT to catch plagiarizing. This ... | Hacker News","url":"https://news.ycombinator.com/item?id=45408514"},{"title":"Watermarking text in LLM outputs – Dr Alan D. Thompson","url":"https://lifearchitect.ai/watermarking/"},{"title":"Shtetl-Optimized » Blog Archive » AI safety: what should actually be done now?","url":"https://scottaaronson.blog/?p=7230"},{"title":"#8: Scott Aaronson - by Theo Jaffee - Theo's Substack","url":"https://www.theojaffee.com/p/8-scott-aaronson"},{"title":"Topic-Based Watermarks for Large Language Models","url":"https://arxiv.org/pdf/2404.02138"}]

Based on the search results, I found information about Scott Aaronson's work on watermarking GPT outputs from 2022. Here's what I found:

Aaronson's main project involved creating a tool for statistically watermarking the outputs of a text model like GPT, where whenever GPT generates some long text, there is an otherwise unnoticeable secret signal in its choices of words that can later prove the text came from GPT.

A working prototype of the watermarking scheme was built by OpenAI engineer Hendrik Kirchner. Empirically, a few hundred tokens seemed to be enough to get a reasonable signal that text came from GPT, and in principle, you could even take a lo
…[truncated 539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:34:47.753142+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Unveiling Attractor Cycles in Large Language Models\" Wang Li Yan Cheng Zhang ACL 2025 arXiv 2502.15208"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Unveiling Attractor Cycles in Large Language Models\" Wang Li Yan Cheng Zhang ACL 2025 arXiv 2502.15208"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:34:47.753269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" Gerstgrasser"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\" Gerstgrasser"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:34:47.753394+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:34:47.753516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor\" Li Yang LLM-Generated Text Detection ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor\" Li Yang LLM-Generated Text Detection ACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:34:47.753659+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Chainwash: Multi-Step Rewriting Attacks\" watermark arXiv 2605.05503"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Chainwash: Multi-Step Rewriting Attacks\" watermark arXiv 2605.05503"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:34:47.753784+00:00_

Web search results for query: ""The Llama 3 Herd of Models" Grattafiori arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"}]

I found the paper you're looking for. Here's the information:

**Title:** "The Llama 3 Herd of Models"

**Authors:** Aaron Grattafiori, Abhimanyu Dubey, and 558 other co-authors

**arXiv ID:** 2407.21783

**Key Details:**

The paper presents a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Their largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. 

Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. Additionally, the paper presents results of experiments in which image, video, and speech capabilities were integrated into Llama 3 via a compositional approach.

The paper includes the public release of Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety.

The paper was initially submitted on Jul
…[truncated 173 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:34:47.753933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mistral 7B\" Jiang Sablayrolles arXiv 2310.06825"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mistral 7B\" Jiang Sablayrolles arXiv 2310.06825"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:34:47.754064+00:00_

Web search results for query: ""Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" Gerstgrasser"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by","url":"https://openreview.net/pdf/264715d321dd6b63cbc356483cbb650791eb374b.pdf"}]

I found the research paper you were looking for. Here are the key details:

"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" is authored by Matthias Gerstgrasser and 13 other authors.

**Main Findings:**

The paper addresses what happens when 
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:34:47.754214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Is Model Collapse Inevitable?\" Gerstgrasser COLM 2024 conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Is Model Collapse Inevitable?\" Gerstgrasser COLM 2024 conference"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-26T10:34:47.754341+00:00_

Web search results for query: ""Chainwash: Multi-Step Rewriting Attacks" watermark arXiv 2605.05503"

Links: [{"title":"[2605.05503] Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/abs/2605.05503"},{"title":"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks","url":"https://arxiv.org/html/2605.05503"},{"title":"Hashed Watermark as a Filter: Defeating Forging and ...","url":"https://arxiv.org/pdf/2507.11137"},{"title":"[2505.05190] Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite Attacks","url":"https://arxiv.org/abs/2505.05190"},{"title":"Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite","url":"https://arxiv.org/pdf/2505.05190"},{"title":"Watermarks Attack Watermarks: Re-Watermarking as a Generic Removal Strategy","url":"https://arxiv.org/html/2605.16796v1"},{"title":"Mitigating Watermark Stealing Attacks in Generative Models via Multi-Key Watermarking","url":"https://arxiv.org/html/2507.07871v1"},{"title":"Review Not peer-reviewed version Digital Watermarking Technology for AI-","url":"https://www.preprints.org/frontend/manuscript/2295181bd830f7111bc227542060d837/download_pub"},{"title":"Revealing Weaknesses in Text Watermarking Through Self-Information Rewrite Attacks","url":"https://arxiv.org/html/2505.05190v1"},{"title":"Hashed Watermark as a Filter: Defeating Forging and Overwriting Attacks in Weight-based Neural Network Watermarking","url":"https://arxiv.org/html/2507.11137v1"}]

I found the paper! Here are the details about "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks" (arXiv:2605.05503):

The paper examines statistical watermarking as a common approach for verifying whether text was written by a language model. Most existing watermarking schemes assume autoregressive generation where tokens are produced left to right, but diffusion language models generate text by denoising tokens in arbit
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:34:47.754486+00:00_

Web search results for query: ""Unveiling Attractor Cycles in Large Language Models" Wang Li Yan Cheng Zhang ACL 2025 arXiv 2502.15208"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"[2502.15208v1] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208v1"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/unveiling-attractor-cycles-large-language-models-dynamical"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"dblp: Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing.","url":"https://dblp.org/rec/journals/corr/abs-2502-15208.html"}]

I found the paper! Here are the key details:

**Paper Title:** Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing

**Authors:** Zhilin W
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-26T10:34:47.754648+00:00_

Web search results for query: ""Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor" Li Yang LLM-Generated Text Detection ACL 2026"

Links: [{"title":"[2604.04932] Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/abs/2604.04932"},{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/html/2604.04932"},{"title":"Yang Liu's Homepage at Tsinghua University","url":"https://nlp.csai.tsinghua.edu.cn/~ly/pub.html"},{"title":"Collaborative Multi-Agent Method for Zero-Shot LLM-Generated Text Detection","url":"https://doi.org/10.3390/informatics13040062"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"}]

I found the paper! Here's what I found:

"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection" by Yang Li and co-authors explores fine-grained LLM-generated text detection under a four-class setting and proposes RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creator and editor.

The paper addresses the limitation of existing binary or ternary classification settings, which can only distinguish pure human/LLM text or collaborative text at best, while LLM-polished human text and humanized LLM text often trigger different policy consequences.

Specifically, RACE utilizes Rhetorical Structure Theory to construct a logic graph for the creator's foundation while extracting Elementary Discourse Unit-level features for the editor's style
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:34:47.754798+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\" Guo Findings NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\" Guo Findings NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-26T10:34:47.754924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Detecting Pretraining Data from Large Language Models\" Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Detecting Pretraining Data from Large Language Models\" Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-26T10:34:47.755050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ordinal Regression Methods: Survey and Experimental Study\" Gutiérrez IEEE TKDE 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ordinal Regression Methods: Survey and Experimental Study\" Gutiérrez IEEE TKDE 2016"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:34:47.755179+00:00_

Web search results for query: ""Mistral 7B" Jiang Sablayrolles arXiv 2310.06825"

Links: [{"title":"[2310.06825] Mistral 7B","url":"https://arxiv.org/abs/2310.06825"},{"title":"[2310.06825] Mistral 7B - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2310.06825"},{"title":"Mistral 7B","url":"https://bibbase.org/network/publication/jiang-sablayrolles-mensch-bamford-chaplot-casas-bressand-lengyel-etal-mistral7b-2023"},{"title":"[PDF] Mistral 7B | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mistral-7B-Jiang-Sablayrolles/db633c6b1c286c0386f0078d8a2e6224e03a6227"},{"title":"Mistral 7B - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231006825J/abstract"},{"title":"Paper page - Mistral 7B","url":"https://huggingface.co/papers/2310.06825"},{"title":"Mistral 7B | BibSonomy","url":"https://www.bibsonomy.org/bibtex/8f3889cfa5f3ce6e7d9c6db646399276"},{"title":"Mistral 7B: Foundation Model Research Paper Summary","url":"https://blog.athina.ai/mistral-7b-foundation-model-research-paper-summary"},{"title":"[2310.06825] Mistral 7B","url":"http://export.arxiv.org/abs/2310.06825"}]

Based on the web search results, here's information about the Mistral 7B paper:

## Paper Overview

The paper "Mistral 7B" was authored by Albert Q. Jiang, Alexandre Sablayrolles, and 17 other authors, and introduces Mistral 7B v0.1, a 7-billion-parameter language model engineered for superior performance and efficiency.

## Key Performance Claims

Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks, and Llama 1 34B in reasoning, mathematics, and code generation.

## Technical Innovations

The model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost.

The paper also provides a model fine-tuned to follow instructions, Mistral 7B – Instruct, that surpasses Llama 2 13B – chat model both on human and automated benchmarks.

The paper
…[truncated 176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:34:47.755327+00:00_

Web search results for query: ""Position: On the Possibilities of AI-Generated Text Detection" Chakraborty Bedi Zhu An Manocha Huang ICML 2024"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/59ae4e4ff7a27010554081e478d9ee707d16d583"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"On the Possibilities of AI-Generated Text Detection - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230404736C/abstract"},{"title":"On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/pdf/2304.04736"}]

I found the paper you're looking for. Here's what I discovered:

**Title:** Position: On the Possibilities of AI-Generated Text Detection

**Authors:** Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang

**Publication:** Proceedings of the 41st International Conference on Machine Learning, PMLR 235:6093-6115, 2024

**Main Fi
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-26T10:34:47.755476+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Conditional Variable Importance for Random Forests\" Strobl Boulesteix BMC Bioinformatics 2008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Conditional Variable Importance for Random Forests\" Strobl Boulesteix BMC Bioinformatics 2008"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:34:47.755620+00:00_

Web search results for query: ""Detecting Pretraining Data from Large Language Models" Shi Ajith Xia Huang Liu Blevins Chen Zettlemoyer ICLR 2024"

Links: [{"title":"DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/detecting-pretraining-data-from-large-language-models/"},{"title":"[2310.16789] Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/abs/2310.16789"},{"title":"DETECTING PRETRAINING DATA FROM LARGE LAN","url":"https://openreview.net/pdf?id=zWqr3MQuNs"},{"title":"GitHub - swj0419/detect-pretrain-code: This repository provides an original implementation of Detecting Pretraining Data from Large Language Models by *Weijia Shi, *Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu , Terra Blevins , Danqi Chen , Luke Zettlemoyer. · GitHub","url":"https://github.com/swj0419/detect-pretrain-code"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://swj0419.github.io/detect-pretrain.github.io/"},{"title":"Detecting Pretraining Data from Large Language Models","url":"https://arxiv.org/html/2310.16789v3"},{"title":"Detecting Pretraining Data from Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231016789S/abstract"},{"title":"[PDF] Detecting Pretraining Data from Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Detecting-Pretraining-Data-from-Large-Language-Shi-Ajith/3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a"}]

I found the paper you're looking for! Here are the key details:

"Detecting Pretraining Data from Large Language Models" by Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, and Zettlemoyer was presented at ICLR 2024 (the 12th International Conference on Learning Representations) in Vienna, Austria in May 2024.

**Paper Overview:**

Although large language models (LLMs) are widely deployed, the data used to train them is rarely disclosed. Given the incredib
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-26T10:34:47.755774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DNA-GPT Yang Xianjun full author list arxiv 2305.17359 ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DNA-GPT Yang Xianjun full author list arxiv 2305.17359 ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-26T10:34:47.755906+00:00_

Web search results for query: ""Is Model Collapse Inevitable?" Gerstgrasser COLM 2024 conference"

Links: [{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-sy
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:34:47.756060+00:00_

Web search results for query: ""The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" Guo Findings NAACL 2024"

Links: [{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"(PDF) The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://www.researchgate.net/publication/382631840_The_Curious_Decline_of_Linguistic_Diversity_Training_Language_Models_on_Synthetic_Text"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399v1"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231109807G/abstract"},{"title":"@inproceedings{guo-etal-2024-curious,","url":"https://aclanthology.org/2024.findings-naacl.228.bib"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-div
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-26T10:34:47.756204+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Machine Text Detectors are Membership Inference Attacks\" Koike Dugan Kaneko Callison-Burch Okazaki arXiv 2510.19492"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Machine Text Detectors are Membership Inference Attacks\" Koike Dugan Kaneko Callison-Burch Okazaki arXiv 2510.19492"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:34:47.756335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position: Model Collapse Does Not Mean What You Think\" Schaeffer Rylan arXiv 2503.03150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position: Model Collapse Does Not Mean What You Think\" Schaeffer Rylan arXiv 2503.03150"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T10:34:47.756462+00:00_

Web search results for query: ""Conditional Variable Importance for Random Forests" Strobl Boulesteix BMC Bioinformatics 2008"

Links: [{"title":"Conditional variable importance for random forests | BMC Bioinformatics | Springer Nature Link","url":"https://link.springer.com/article/10.1186/1471-2105-9-307"},{"title":"(PDF) Conditional Variable Importance for Random Forests","url":"https://www.researchgate.net/publication/5231126_Conditional_Variable_Importance_for_Random_Forests"},{"title":"Conditional variable importance for random forests - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC2491635/"},{"title":"Conditional Variable Importance for Random Forests - WU Vienna University of Economics and Business","url":"https://epub.wu.ac.at/4987/1/Strobl_etal_2008_BMC-Bioinformatics_Conditional-variable-importance-for-random-forests.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Conditional+variable+importance+for+random+forests&amp=&author=C.+Strobl&amp=&author=A.-L.+Boulesteix&amp=&author=T.+Kneib&amp=&author=T.+Augustin&amp=&author=A.+Zeileis&amp=&publication_year=2008&amp=&journal=BMC+Bioinformatics&amp=&volume=9&amp=&pages=307"},{"title":"Strobl, C., Boulesteix, A.L., Kneib, T., Augustin, T. and Zeileis, A. (2008) Conditional Variable Importance for Random Forests. BMC Bioinformatics, 9, 307. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1904998"},{"title":"C. Strobl, A. L. Boulesteix, T. Kneib, T. Augustin and A. Zeileis, “Conditional Variable Importance for Random Forests,” BMC Bioinformatics, Vol. 9, Article 307, 2008. doi10.1186/1471-2105-9-307 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=244582"},{"title":"Conditional variable importance for random forests - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/18620558/?dopt=Abstract"}]

I found the paper you're looking for. The
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:34:47.756620+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Does Writing with Language Models Reduce Content Diversity?\" Padmakumar He ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Does Writing with Language Models Reduce Content Diversity?\" Padmakumar He ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-26T10:34:47.756752+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dolma: an Open Corpus of Three Trillion Tokens\" Soldaini ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dolma: an Open Corpus of Three Trillion Tokens\" Soldaini ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:34:47.756878+00:00_

Web search results for query: "DNA-GPT Yang Xianjun full author list arxiv 2305.17359 ICLR 2024"

Links: [{"title":"[2305.17359] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://arxiv.org/abs/2305.17359"},{"title":"Paper page - DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://huggingface.co/papers/2305.17359"},{"title":"(PDF) DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text","url":"https://www.researchgate.net/publication/371136931_DNA-GPT_Divergent_N-Gram_Analysis_for_Training-Free_Detection_of_GPT-Generated_Text"},{"title":"GitHub - Xianjun-Yang/DNA-GPT: Offiical codes for DNA-GPT (ICLR 2024)","url":"https://github.com/Xianjun-Yang/DNA-GPT"},{"title":"[PDF] DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DNA-GPT:-Divergent-N-Gram-Analysis-for-Detection-of-Yang-Cheng/08145978da4c8912f4a05444a6bbf048778dc4af"},{"title":"DNA-GPT/DNA-GPT-dist.py at main · Xianjun-Yang/DNA-GPT","url":"https://github.com/Xianjun-Yang/DNA-GPT/blob/main/DNA-GPT-dist.py"},{"title":"publications | Xianjun Yang","url":"https://xianjun-yang.github.io/publications/"},{"title":"DNA-GPT/README.md at main · Xianjun-Yang/DNA-GPT","url":"https://github.com/Xianjun-Yang/DNA-GPT/blob/main/README.md"},{"title":"dblp: DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text.","url":"https://dblp.org/rec/journals/corr/abs-2305-17359.html"},{"title":"DNA-GPT: Divergent N-Gram Analysis for Training-Free ...","url":"https://arxiv.org/pdf/2305.17359"}]

Based on the search results, I found the full author list for the DNA-GPT paper (arxiv 2305.17359):

The authors are: Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, and Haifeng Chen.

However, I should note a discrepancy: Most sources list only 5 authors (Xianjun Yang, Wei 
…[truncated 348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-26T10:34:47.757036+00:00_

Web search results for query: ""Ordinal Regression Methods: Survey and Experimental Study" Gutiérrez IEEE TKDE 2016"

Links: [{"title":"[PDF] Ordinal Regression Methods: Survey and Experimental Study | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ordinal-Regression-Methods:-Survey-and-Experimental-Guti%C3%A9rrez-P%C3%A9rez-Ortiz/d67edf85746a2fc64f803de44cc4169b87525c27"},{"title":"Ordinal regression methods: Survey and experimental study -ORCA","url":"https://orca.cardiff.ac.uk/id/eprint/112802/"},{"title":"Ordinal regression methods: survey and experimental study - Pedro Antonio Gutiérrez","url":"https://pagutierrez.github.io/publication/2016-01-01-Ordinal-regression-methods-survey-and-experimental-study"},{"title":"Ordinal Regression Methods: Survey and Experimental Study - R Discovery","url":"https://discovery.researcher.life/article/ordinal-regression-methods-survey-and-experimental-study/31458b5b781030c4941bf4f32aaeb0a5"},{"title":"Ordinal Regression Methods: Survey and Experimental Study | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7161338/"},{"title":"2016-Ordinal regression methods% ...","url":"https://orca.cardiff.ac.uk/id/eprint/112802/1/2016-Ordinal%20regression%20methods%253a%20Survey%20and%20experimental%20study.pdf"},{"title":"Ordinal Regression Methods: Survey and Experimental Study","url":"https://repositorio.uloyola.es/handle/20.500.12412/1185"},{"title":"(PDF) Ordinal Regression Methods: Survey and Experimental Study","url":"https://www.researchgate.net/publication/280245851_Ordinal_Regression_Methods_Survey_and_Experimental_Study"},{"title":"Ordinal Regression Methods: Survey and Experimental Study | IEEE Transactions on Knowledge and Data Engineering","url":"https://dl.acm.org/doi/abs/10.1109/TKDE.2015.2457911"}]

I found the paper you're looking for! Here are the key details:

**Publication Information:**
The paper "Ordinal regression methods: survey and experimental study" was authored 
…[truncated 860 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:34:47.757179+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Binoculars Hans Schwarzschild Cherepanova authors full list arxiv 2401.12070"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Binoculars Hans Schwarzschild Cherepanova authors full list arxiv 2401.12070"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T10:34:47.757304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\" Cao Raschka Pattern Recognition Letters 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\" Cao Raschka Pattern Recognition Letters 2020"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-26T10:34:47.757434+00:00_

Web search results for query: ""Position: Model Collapse Does Not Mean What You Think" Schaeffer Rylan arXiv 2503.03150"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/html/2504.03814v4"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"Computers and Society Mar 2025","url":"https://arxiv.org/list/cs.CY/2025-03?skip=300&show=25"}]

I found the paper you were looking for. Here's what the research is about:

## "Position: Model Collapse Does Not Mean What You Think"

This paper addresses concerns about model collapse, which is a degradation in future generative models' performance when trained on syn
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:34:47.757595+00:00_

Web search results for query: ""Machine Text Detectors are Membership Inference Attacks" Koike Dugan Kaneko Callison-Burch Okazaki arXiv 2510.19492"

Links: [{"title":"[2510.19492] Machine Text Detectors are Membership Inference Attacks","url":"https://arxiv.org/abs/2510.19492"},{"title":"Machine Text Detectors are Membership Inference Attacks","url":"https://arxiv.org/html/2510.19492"},{"title":"Preprint. MACHINE TEXT DETECTORS ARE MEMBERSHIP INFERENCE ATTACKS","url":"https://arxiv.org/pdf/2510.19492"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/cs?searchtype=author&amp=&query=Callison-Burch,+C"},{"title":"Machine Text Detectors are Membership Inference Attacks - Paper Details","url":"https://www.chatpaper.ai/dashboard/paper/62620ac8-49a3-4f3c-bc95-d4a650e1cbe0"},{"title":"Ryuto Koike - PhD at Science Tokyo | Prev: UPenn | AI safety and security | ryuryukke.github.io | LinkedIn","url":"https://www.linkedin.com/in/ryuto-koike/"},{"title":"Liam Dugan ldugan@seas.upenn.edu | linkedin.com/in/liam-dugan | liamdugan.com","url":"https://liamdugan.com/files/cv.pdf"}]

I found the paper! Here's information about it:

**Paper Title:** Machine Text Detectors are Membership Inference Attacks

**Authors:** Ryuto Koike, Liam Dugan, Masahiro Kaneko, Chris Callison-Burch, Naoaki Okazaki

**arXiv ID:** 2510.19492

**Main Contribution:**

Although membership inference attacks (MIAs) and machine-generated text detection target different goals, their methods often exploit similar signals based on a language model's probability distribution. The authors theoretically and empirically demonstrate the transferability between MIAs and machine text detection, and prove that the metric achieving asymptotically optimal performance is identical for both tasks.

**Key Findings:**

The empirical experiments demonstrate very strong rank correlation (ρ≈0.7) in cross-task performance. Additionally, the authors introduce MINT, a unified evaluation suite implementing 
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T10:34:47.757753+00:00_

Web search results for query: ""Dolma: an Open Corpus of Three Trillion Tokens" Soldaini ACL 2024"

Links: [{"title":"Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.840/"},{"title":"[2402.00159] Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research","url":"https://arxiv.org/abs/2402.00159"},{"title":"Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/dolma-an-open-corpus-of-three-trillion-tokens-for-language-model-/"},{"title":"Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240200159S/abstract"},{"title":"Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research | Request PDF","url":"https://www.researchgate.net/publication/384207944_Dolma_an_Open_Corpus_of_Three_Trillion_Tokens_for_Language_Model_Pretraining_Research"},{"title":"[PDF] Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dolma:-an-Open-Corpus-of-Three-Trillion-Tokens-for-Soldaini-Kinney/ad1bb59e3e18a0dd8503c3961d6074f162baf710"},{"title":"Dolma : an Open Corpus of Three Trillion Tokens for ...","url":"https://aclanthology.org/2024.acl-long.840.pdf"},{"title":"[2402.00159v1] Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research","url":"https://arxiv.org/abs/2402.00159v1"}]

I found the paper you're looking for! Here's what I found:

"Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research" by Soldaini et al. was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in August 2024, with pages 15725–15788.

D
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:34:47.757898+00:00_

Web search results for query: ""Does Writing with Language Models Reduce Content Diversity?" Padmakumar He ICLR 2024"

Links: [{"title":"[2309.05196] Does Writing with Language Models Reduce Content Diversity?","url":"https://arxiv.org/abs/2309.05196"},{"title":"Does Writing with Language Models Reduce Content Diversity? | OpenReview","url":"https://openreview.net/forum?id=Feiz5HtCD0"},{"title":"DOES WRITING WITH LANGUAGE MODELS REDUCE CONTENT DIVERSITY? - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/does-writing-with-language-models-reduce-content-diversity"},{"title":"Does Writing With Language Models (LLMs) Reduce Content Diversity?","url":"https://iclr.cc/media/iclr-2024/Slides/19056.pdf"},{"title":"Does Writing with Language Models Reduce Content Diversity? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/does-writing-language-models-reduce-content-diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | Request PDF","url":"https://www.researchgate.net/publication/373837896_Does_Writing_with_Language_Models_Reduce_Content_Diversity"},{"title":"Does Writing with Language Models Reduce Content Diversity? | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534705-does-writing-language-models-reduce-content-diversity"},{"title":"[PDF] Does Writing with Language Models Reduce Content Diversity? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Does-Writing-with-Language-Models-Reduce-Content-Padmakumar-He/f95fb254da1f7b74a14ac8feb3f834d64e67e4cd"},{"title":"ICLR Poster Does Writing with Language Models Reduce Content Diversity?","url":"https://iclr.cc/virtual/2024/poster/19056"}]

I found the paper you're looking for! Here's what the research shows:

"Does Writing with Language Models Reduce Content Diversity?" is a paper by Padmakumar and He presented at ICLR 2024.

**Key Findings:**

The researchers conducted a controlled experiment where users wrote argumentativ
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T10:34:47.758044+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\" Wu Yang Zhan Yuan Chao Wong Computational Linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\" Wu Yang Zhan Yuan Chao Wong Computational Linguistics"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-26T10:34:47.758171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" Penedo NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\" Penedo NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-26T10:34:47.758291+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SemEval-2024 Task 8 Wang Yuxia authors Whitehouse Chenxi ACL Anthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SemEval-2024 Task 8 Wang Yuxia authors Whitehouse Chenxi ACL Anthology"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-26T10:34:47.758411+00:00_

Web search results for query: "Binoculars Hans Schwarzschild Cherepanova authors full list arxiv 2401.12070"

Links: [{"title":"[2401.12070] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070"},{"title":"GitHub - ahans30/Binoculars: [ICML 2024] Binoculars: Zero-Shot Detection of LLM-Generated Text · GitHub","url":"https://github.com/ahans30/Binoculars"},{"title":"[PDF] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Spotting-LLMs-With-Binoculars:-Zero-Shot-Detection-Hans-Schwarzschild/8dafb105a0cec1956443003eeea9fcf13c0ffa99"},{"title":"[2401.12070v2] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v2"},{"title":"[2401.12070v1] Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2401.12070v1"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Abhimanyu+Hans%2C+Avi+Schwarzschild%2C+Valeriia+Cherepanova%2C+Hamid+Kazemi%2C+Aniruddha+Saha%2C+Micah+Goldblum%2C+Jonas+Geiping%2C+and+Tom+Goldstein.+2024.+Spotting+llms+with+binoculars%3A+Zero-shot+detection+of+machine-generated+text.+arXiv+preprint+arXiv%3A2401.12070%282024%29."},{"title":"Paper page - Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text","url":"https://huggingface.co/papers/2401.12070"},{"title":"Binoculars/README.md at main · ahans30/Binoculars","url":"https://github.com/ahans30/Binoculars/blob/main/README.md"},{"title":"Publications - Valeriia Cherepanova - GitHub Pages","url":"https://vcherepanova.github.io/publications/"}]

Based on the search results, the full list of authors for the arxiv paper 2401.12070 "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text" is: Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Mica
…[truncated 148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-26T10:34:47.758557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Curious Case of Neural Text Degeneration\" Holtzman nucleus sampling ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Curious Case of Neural Text Degeneration\" Holtzman nucleus sampling ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T10:34:47.758704+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan TMLR accepted date 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan TMLR accepted date 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T10:34:47.758834+00:00_

Web search results for query: ""Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation" Cao Raschka Pattern Recognition Letters 2020"

Links: [{"title":"Rank consistent ordinal regression for neural networks with application to age estimation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S016786552030413X"},{"title":"[1901.07884] Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://arxiv.org/abs/1901.07884"},{"title":"(PDF) Rank consistent ordinal regression for neural networks with application to age estimation","url":"https://www.researchgate.net/publication/347503290_Rank_consistent_ordinal_regression_for_neural_networks_with_application_to_age_estimation"},{"title":"GitHub - Raschka-research-group/coral-cnn: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation · GitHub","url":"https://github.com/Raschka-research-group/coral-cnn"},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"},{"title":"Publications - Dr. Raschka","url":"https://pages.stat.wisc.edu/~sraschka/publications/bibtex/CaoRaschka2020Coral/"},{"title":"1 Rank-consistent ordinal regression for neural networks","url":"https://sebastianraschka.com/pdf/papers/2020-coral2-2020-july.pdf"},{"title":"Rank consistent ordinal regression for neural networks with application to age estimation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020PaReL.140..325C/abstract"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"},{"title":"Rank consistent ordinal regression for neural networks with ...","url":"https://sebastianraschka.com/pdf/papers/2020-coral.pdf"}]

I found the paper you're looking for! Here are the key details:

**"Rank Consistent Ordinal R
…[truncated 1047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-26T10:34:47.758982+00:00_

Web search results for query: ""The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" Penedo NeurIPS 2024"

Links: [{"title":"[2406.17557] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://arxiv.org/abs/2406.17557"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"NeurIPS Poster The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://neurips.cc/virtual/2024/poster/97513"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale | OpenReview","url":"https://openreview.net/forum?id=n6SCkn2QaG"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://papers.neurips.cc/paper_files/paper/2024/file/370df50ccfdf8bde18f8f9c2d9151bda-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://www.researchgate.net/publication/397205318_The_FineWeb_Datasets_Decanting_the_Web_for_the_Finest_Text_Data_at_Scale"},{"title":"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale","url":"https://papers.nips.cc/paper_files/paper/2024/hash/370df50ccfdf8bde18f8f9c2d9151bda-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"[Quick Review] The FineWeb Datasets: Decanting the Web for the Finest Text Data at\\n Scale","url":"https://liner.com/review/fineweb-datasets-decanting-web-for-finest-text-data-at-scale"},{"title":"[PDF] The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-FineWeb-Datasets:-Decanting-the-Web-for-the-at-Penedo-Kydl%C3%ADcek/b83a9e35c3aeeb37708e362473c7617d59b815b5"},{"title":"[2406.17557v2] The FineWeb Datasets: Decanting the
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:34:47.759137+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Simple Approach to Ordinal Classification\" Frank Hall ECML 2001"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Simple Approach to Ordinal Classification\" Frank Hall ECML 2001"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T10:34:47.759271+00:00_

Web search results for query: ""A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions" Wu Yang Zhan Yuan Chao Wong Computational Linguistics"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"[PDF] A Survey on LLM-generated Text Detection: Necessity, Methods, and Future Directions | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-LLM-generated-Text-Detection:-Methods,-Wu-Yang/a09d3686285f609b60b18b5935da64b29a5cce0f"},{"title":"GitHub - junchaoIU/LLM-generated-Text-Detection: A survey and reflection on the latest research breakthroughs in LLM-generated Text detection, including data, detectors, metrics, current issues and future directions.","url":"https://github.com/junchaoIU/LLM-generated-Text-Detection"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://arxiv.org/pdf/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/survey-llm-generated-text-detection-necessity-methods"},{"title":"[2310.14724v3] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724v3"},{"title":"GitHub - NLP2CT/LLM-generated-Text-Detection: A survey and reflection on the la
…[truncated 1386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T10:34:47.759416+00:00_

Web search results for query: ""The Curious Case of Neural Text Degeneration" Holtzman nucleus sampling ICLR 2020"

Links: [{"title":"ICLR: The Curious Case of Neural Text Degeneration","url":"https://iclr.cc/virtual_2020/poster_rygGQyrFvH.html"},{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://www.researchgate.net/publication/332590110_The_Curious_Case_of_Neural_Text_Degeneration"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"},{"title":"The Curious Case of Neural Text Degeneration","url":"https://hyunyoung2.github.io/2020/06/04/The_Curious_Case_of_Neural_Text_Degeneration/"},{"title":"(PDF) The Curious Case of Neural Text Degeneration (2020) | Ari Holtzman | 689 Citations","url":"https://scispace.com/papers/the-curious-case-of-neural-text-degeneration-2xplgl0dw1"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"},{"title":"CLOSING THE CURIOUS CASE OF NEURAL TEXT DEGENERATION Matthew Finlayson∗","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf"}]

Based on the search results, here's what I found about "The Curious Case of Neural Text Degeneration" by Holtzman et al.:

## Overview

This paper was presented at the International Conference on Learning Representations (ICLR) on April 26 - May 1, 2020. The authors include Ari Holtzman, Jan Buys, Leo Du, Maxwell Forbes, and Yejin Choi from the Allen Institute for Artificial Intelligence and University of Washington.

## Main Problem

The paper identifies a coun
…[truncated 1247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T10:34:47.759566+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang Zhang Wu COLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mapping the Increasing Use of LLMs in Scientific Papers\" Liang Zhang Wu COLM 2024"
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T10:34:47.759713+00:00_

Web search results for query: "SemEval-2024 Task 8 Wang Yuxia authors Whitehouse Chenxi ACL Anthology"

Links: [{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.279/"},{"title":"SemEval-2024 Task 8: Multigenerator, Multidomain, and ...","url":"https://github.com/mbzuai-nlp/SemEval2024-task8"},{"title":"SemEval-2024 Tasks | SemEval-2024","url":"https://semeval.github.io/SemEval2024/tasks.html"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/semeval-2024-task-8-multidomain-multimodel-and-multilingual-machi"},{"title":"[2404.14183] SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/abs/2404.14183"},{"title":"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2404.14183v1"},{"title":"Team QUST at SemEval-2024 Task 8: A Comprehensive Study of Monolingual and Multilingual Approaches for Detecting AI-generated Text - ACL Anthology","url":"https://aclanthology.org/2024.semeval-1.71/"}]

I found the information you're looking for! SemEval-2024 Task 8 is on Multidomain, Multimodel and Multilingual Machine-Generated Text Detection, authored by Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, and Thomas Arnold. 

Chenxi Whitehouse is also listed as one of the authors in the official bibtex entry, along with Alham Fikri Aji, Nizar Habash, Iryna Gurevych, and Preslav Nakov.

The paper is available on the ACL Anthology at aclanthology.org/2024.semeval-1.279, and was published in the Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024) in Mexico City.


REMINDER: You MUST incl
…[truncated 77 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-26T10:34:47.759863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Automatic Detection of Machine Generated Text: A Critical Survey\" Jawahar Abdul-Mageed Lakshmanan COLING 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Automatic Detection of Machine Generated Text: A Critical Survey\" Jawahar Abdul-Mageed Lakshmanan COLING 2020"
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-26T10:34:47.759987+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Neural Text Generation with Unlikelihood Training\" Welleck ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Neural Text Generation with Unlikelihood Training\" Welleck ICLR 2020"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-26T10:34:47.760109+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan TMLR accepted date 2024 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2024"}]

Based on the search results, I found information about the paper "Can AI-Generated Text be Reliably Detected?" by Sadasivan and colleagues:

**Paper Details:**
The paper is authored by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi.

**TMLR Status:**
The paper was previously submitted to TMLR, with the note that "all reviewers appreciated the technical developments of the paper and think this could be an exciting paper that addresses a very important and timely challenge". The authors modified the title to "Can AI-Generated Text be Reliably Detected?" following the reviews. The OpenReview page shows an update date of October 20, 2024.

**Main Contributions:**
The paper introduces a recursive par
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-26T10:34:47.760249+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shumailov \"AI models collapse\" Nature volume 631 pages 755"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov \"AI models collapse\" Nature volume 631 pages 755"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-26T10:34:47.760376+00:00_

Web search results for query: ""A Simple Approach to Ordinal Classification" Frank Hall ECML 2001"

Links: [{"title":"A Simple Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/3-540-44795-4_13"},{"title":"[PDF] A Simple Approach to Ordinal Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Simple-Approach-to-Ordinal-Classification-Frank-Hall/76fc26939d73c565431e1f38107a4245e739284e"},{"title":"A Simple Approach to Ordinal Classiﬁcation Eibe Frank and Mark Hall","url":"https://link.springer.com/content/pdf/10.1007/3-540-44795-4_13.pdf"},{"title":"A simple approach to ordinal classification | Proceedings of the 12th European Conference on Machine Learning","url":"https://dl.acm.org/doi/10.1007/3-540-44795-4_13"},{"title":"A simple approach to ordinal classification.","url":"https://researchcommons.waikato.ac.nz/items/ce0009f5-92fa-4113-b8b2-7ac929cfd32c"},{"title":"(PDF) A Simple Approach to Ordinal Classification","url":"https://www.researchgate.net/publication/226877154_A_Simple_Approach_to_Ordinal_Classification"},{"title":"(PDF) A Simple Approach to Ordinal Classification (2001) | Eibe Frank | 655 Citations","url":"https://scispace.com/papers/a-simple-approach-to-ordinal-classification-2mjbzk39ox"},{"title":"Classification of Ordinal Data Using Neural Networks | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/11564096_70"},{"title":"An Improved Approach to Ordinal Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-662-45652-1_4"},{"title":"A Simple Approach to Ordinal Classification - Eibe Frank, Mark Andrew Hall - Google Books","url":"https://books.google.com/books/about/A_Simple_Approach_to_Ordinal_Classificat.html?id=SI2oMQAACAAJ"}]

I found the paper you're looking for. Here are the key details:

The paper "A Simple Approach to Ordinal Classification" by Frank and Hall was published in the Machine Learning:
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-26T10:34:47.760522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"OOgsAZdFOt\" TMLR accepted \"Stress Testing\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"OOgsAZdFOt\" TMLR accepted \"Stress Testing\""
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-26T10:34:47.760667+00:00_

Web search results for query: ""Neural Text Generation with Unlikelihood Training" Welleck ICLR 2020"

Links: [{"title":"Neural Text Generation With Unlikelihood Training | OpenReview","url":"https://openreview.net/forum?id=SJeYe0NtvH"},{"title":"dblp: Neural Text Generation With Unlikelihood Training.","url":"https://dblp.org/rec/conf/iclr/WelleckKRDCW20.html"},{"title":"[1908.04319] Neural Text Generation with Unlikelihood Training","url":"https://arxiv.org/abs/1908.04319"},{"title":"Neural Text Generation With Unlikelihood Training - researchr publication","url":"https://researchr.org/publication/WelleckKRDCW20"},{"title":"ICLR: Neural Text Generation With Unlikelihood Training","url":"https://iclr.cc/virtual_2020/poster_SJeYe0NtvH.html"},{"title":"Published as a conference paper at ICLR 2020 THE CURIOUS CASE OF","url":"https://scispace.com/pdf/the-curious-case-of-neural-text-degeneration-2xplgl0dw1.pdf"},{"title":"Neural Text Generation With Unlikelihood Training - Papertalk","url":"https://papertalk.org/papertalks/3877"},{"title":"[PDF] Neural Text Generation with Unlikelihood Training | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Neural-Text-Generation-with-Unlikelihood-Training-Welleck-Kulikov/53a77e8f73f2ca422d6e38fa9ecc490231ac044c"},{"title":"Papers with Code - Neural Text Generation with Unlikelihood Training","url":"https://paperswithcode.com/paper/neural-text-generation-with-unlikelihood"}]

I found the paper! Here's what I found about "Neural Text Generation with Unlikelihood Training" by Welleck et al., presented at ICLR 2020:

**Publication Details:**
The paper was authored by Sean Welleck, Ilia Kulikov, Stephen Roller, Emily Dinan, KyungHyun Cho, and Jason Weston, presented at the 8th International Conference on Learning Representations (ICLR) 2020 in Addis Ababa, Ethiopia, April 26-30, 2020.

**Main Contribution:**
The paper addresses problems in neural text generation, particularly that standard likelihood training and decoding 
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T10:34:47.760811+00:00_

Web search results for query: ""Mapping the Increasing Use of LLMs in Scientific Papers" Liang Zhang Wu COLM 2024"

Links: [{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://openreview.net/pdf/eff0ea8ed41a89a9e267752af56df912888fee65.pdf"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://arxiv.org/html/2404.01268v1"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers","url":"https://www.semanticscholar.org/paper/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Liang-Zhang/882f3d1b718e833156ccd6f5bda3190cd06791ea"},{"title":"How much are LLMs changing the language of academic papers after ChatGPT? A multi-database and full text analysis","url":"https://arxiv.org/pdf/2509.09596"},{"title":"Have LLM-associated terms increased in article full texts in all fields?","url":"https://arxiv.org/pdf/2604.07565"},{"title":"Large Language Models Penetration in Scholarly Writing and Peer Review","url":"https://arxiv.org/pdf/2502.11193"},{"title":"Mapping the Increasing Use of LLMs in Scientific Papers | OpenReview","url":"https://openreview.net/forum?id=YX7QnhxESU"}]

I found the paper you're looking for! The paper "Mapping the Increasing Use of LLMs in Scientific Papers" was published at COLM 2024 and is authored by Weixin Liang, Yaohui Zhang, and Zhengxuan Wu, along with several colleagues from Stanford University and other institutions.

The study addresses the gap in lacking a precise measure of the proportion of academic writing substantially modified or produced by LLMs by conducting the first systematic, large-scale analysis across 950,965 papers published between January 2020 and February 2024 on arXiv, bioRxiv, and Nature portfolio journals, using a population-level statistical framework to measure the prevalence of LLM-modified content over time.

The paper is available through multiple sources:
- OpenReview PDF: https://openreview.net/pdf/eff0ea8ed41a89a9e267752af56df912888fee65.pdf
- arXiv
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T10:34:47.760965+00:00_

Web search results for query: ""Automatic Detection of Machine Generated Text: A Critical Survey" Jawahar Abdul-Mageed Lakshmanan COLING 2020"

Links: [{"title":"Automatic Detection of Machine Generated Text: A Critical Survey - ACL Anthology","url":"https://aclanthology.org/2020.coling-main.208/"},{"title":"[PDF] Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c"},{"title":"Automatic Detection of Machine Generated Text: A Critical Survey | Request PDF","url":"https://www.researchgate.net/publication/348344789_Automatic_Detection_of_Machine_Generated_Text_A_Critical_Survey"},{"title":"GitHub - UBC-NLP/coling2020_machine_generated_text: Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://github.com/UBC-NLP/coling2020_machine_generated_text"},{"title":"Automatic Detection of Machine Generated Text: A Critical Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201101314J/abstract"},{"title":"Automatic Detection of Machine Generated Text: A Critical ...","url":"https://aclanthology.org/2020.coling-main.208.pdf"},{"title":"Table 2 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/2"},{"title":"(PDF) Automatic Detection of Machine Generated Text: A Critical Survey","url":"https://www.researchgate.net/publication/345261249_Automatic_Detection_of_Machine_Generated_Text_A_Critical_Survey"},{"title":"Table 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:34:47.761114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\" Shi Cao Raschka Pattern Analysis Applications 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities\" Shi Cao Raschka Pattern Analysis Applications 2023"
  }
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-26T10:34:47.761241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\" Liang Izzo ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\" Liang Izzo ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-26T10:34:47.761364+00:00_

Web search results for query: "Shumailov "AI models collapse" Nature volume 631 pages 755"

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"AI models collapse when trained on recursively generated data - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:fa1155e9-c2ff-436a-8391-455b622f4e64"},{"title":"AI model collapse might be prevented by studying human language transmission","url":"https://www.nature.com/articles/d41586-024-03023-y"},{"title":"AI models collapse when trained on recursively generated data - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/ai-models-collapse-when-trained-on-recursively-generated-data/"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"(PDF) AI models collapse when trained on recursively generated data","url":"https://www.researchgate.net/publication/382526401_AI_models_collapse_when_trained_on_recursively_generated_data"},{"title":"AI models fed AI-generated data quickly spew nonsense","url":"https://www.nature.com/articles/d41586-024-02420-7"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"}]

I found the paper you were looking for. Here are the key details:

The paper was published in Nature volume 631, pages 755-759 (2024), authored by Shumailov,
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-26T10:34:47.761499+00:00_

Web search results for query: "site:openreview.net "OOgsAZdFOt" TMLR accepted "Stress Testing""

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"TMLR - Transactions on Machine Learning Research","url":"https://openreview.net/group?id=TMLR"},{"title":"TMLR Event Certifications | OpenReview","url":"https://openreview.net/group?id=TMLR%2FEvent_Certifications&event=automl.cc%2FAutoML%2F2023%2FJournal_Track"},{"title":"Under review as submission to TMLR","url":"https://openreview.net/pdf/fa3ba1455b83eae92616443009ac0403a7409507.pdf"},{"title":"TMLR Submissions","url":"https://openreview.net/submissions?venue=TMLR"},{"title":"TMLR Expert Reviewers | OpenReview","url":"https://openreview.net/group?id=TMLR/Expert_Reviewers"},{"title":"TMLR | OpenReview","url":"https://dev.openreview.net/group?id=.TMLR"},{"title":"TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering | OpenReview","url":"https://openreview.net/forum?id=fXn4Rk8B3l"},{"title":"TMLR Submissions | OpenReview","url":"https://openreview.net/submissions?page=62&venue=TMLR"},{"title":"The Adaptive Stress Testing Formulation Mark Koren mkoren@stanford.edu","url":"https://openreview.net/pdf?id=rJgoNK-oaE"}]

Based on the search results, I found the paper you're looking for. The paper titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" is available at https://openreview.net/forum?id=OOgsAZdFOt on OpenReview.

The paper stress-tests the robustness of AI text detectors in the presence of an attacker. This is a TMLR submission that was previously submitted and has been updated based on reviewer feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-26T10:34:47.761661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jawahar Abdul-Mageed Lakshmanan COLING 2020 \"Laks V.S.\" author name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jawahar Abdul-Mageed Lakshmanan COLING 2020 \"Laks V.S.\" author name"
  }
}
```

</details>

---

### Tool call

_source line 180 · 2026-05-26T10:34:47.761791+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sadasivan \"Stress Testing AI Text Detectors\" TMLR 2025 published accepted March"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sadasivan \"Stress Testing AI Text Detectors\" TMLR 2025 published accepted March"
  }
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-26T10:34:47.761915+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1908.09203 \"Release Strategies\" Solaiman full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1908.09203 \"Release Strategies\" Solaiman full author list"
  }
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-26T10:34:47.762035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SynthID text Nature volume 634 pages 818 2024 authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SynthID text Nature volume 634 pages 818 2024 authors list"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-26T10:34:47.762155+00:00_

Web search results for query: "Jawahar Abdul-Mageed Lakshmanan COLING 2020 "Laks V.S." author name"

Links: [{"title":"Automatic Detection of Machine Generated Text: A Critical Survey - ACL Anthology","url":"https://aclanthology.org/2020.coling-main.208/"},{"title":"Table 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/0"},{"title":"Laks Lakshmanan, V.S. - ACL Anthology","url":"https://aclanthology.org/people/l/laks-lakshmanan-v-s/"},{"title":"dblp: Laks V. S. Lakshmanan","url":"https://dblp.org/pid/l/LVSLakshmanan.html"},{"title":"Table 2 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/2"},{"title":"Figure 1 from Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c/figure/1"},{"title":"Laks V. S. Lakshmanan - ACL Anthology","url":"https://aclanthology.org/people/laks-v-s-lakshmanan/"},{"title":"Laks V.S. Lakshmanan","url":"https://scholar.google.com/citations?user=_RCsaOsAAAAJ&hl=en"},{"title":"[PDF] Automatic Detection of Machine Generated Text: A Critical Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Automatic-Detection-of-Machine-Generated-Text:-A-Jawahar-Abdul-Mageed/9438bc5626b2d9a771cecc7a41ecabf6639db53c"}]

Based on the search results, I found information about the paper you're looking for:

The paper "Automatic Detection of Machine Generated Text: A Critical Survey" was authored by Ganesh Jawahar, Muhammad Abdul-Mageed, and Laks Lakshmanan, V
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-26T10:34:47.762310+00:00_

Web search results for query: ""Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities" Shi Cao Raschka Pattern Analysis Applications 2023"

Links: [{"title":"[2111.08851] Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/abs/2111.08851"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities","url":"https://www.researchgate.net/publication/371915425_Deep_neural_networks_for_rank-consistent_ordinal_regression_based_on_conditional_probabilities"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10044-023-01181-9"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal ...","url":"https://arxiv.org/pdf/2111.08851"},{"title":"Deep neural networks for rank-consistent ordinal regression based on conditional probabilities | Pattern Analysis & Applications","url":"https://dl.acm.org/doi/abs/10.1007/s10044-023-01181-9"},{"title":"[2111.08851v1] Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities","url":"https://arxiv.org/abs/2111.08851v1"},{"title":"Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211108851S/abstract"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Deep+neural+networks+for+rank-consistent+ordinal+regression+based+on+conditional+probabilities."},{"title":"GitHub - Raschka-research-group/coral-pytorch: CORAL and CORN implementations for ordinal regression with deep neural networks. · GitHub","url":"https://github.com/Raschka-research-group/coral-pytorch"}]

I found the paper you're looking for! Here are the key details:

**Publication Information:**
The paper "Deep neu
…[truncated 1243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-26T10:34:47.762470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Stamatatos 2009 \"authorship attribution\" JASIST volume 60 number pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Stamatatos 2009 \"authorship attribution\" JASIST volume 60 number pages"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-26T10:34:47.762669+00:00_

Web search results for query: ""Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews" Liang Izzo ICML 2024"

Links: [{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://proceedings.mlr.press/v235/liang24b.html"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/html/2403.07183v2"},{"title":"[PDF] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Monitoring-AI-Modified-Content-at-Scale:-A-Case-on-Liang-Izzo/023e113b11ff7bac182713a069fedcbcccad9562"},{"title":"Monitoring AI-modified content at scale | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693262"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the ...","url":"http://lingjiaochen.com/papers/2024_MonitoringAIContent_ICML.pdf"},{"title":"ICML 2024 Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews Oral","url":"https://icml.cc/virtual/2024/oral/35507"},{"title":"[2403.07183v2] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183v2"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/monitoring-ai-modified-content-at-scale-case"}]

I found the paper you were searching for! Here are the key details:

**"Monitorin
…[truncated 1667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-26T10:34:47.762838+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Soft Labels for Ordinal Regression\" Diaz Marathe CVPR 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Soft Labels for Ordinal Regression\" Diaz Marathe CVPR 2019"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-26T10:34:47.762968+00:00_

Web search results for query: "arxiv 1908.09203 "Release Strategies" Solaiman full author list"

Links: [{"title":"[1908.09203] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203"},{"title":"[1908.09203v2] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v2"},{"title":"[1908.09203v1] Release Strategies and the Social Impacts of Language Models","url":"https://arxiv.org/abs/1908.09203v1"},{"title":"Release Strategies and the Social Impacts of Language ...","url":"https://arxiv.org/pdf/1908.09203"},{"title":"[PDF] Release Strategies and the Social Impacts of Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Release-Strategies-and-the-Social-Impacts-of-Models-Solaiman-Brundage/c7462e0ee928f095a7fc40b91f1e7557d283ae8e"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=I.+Solaiman+%2C+%E2%80%98Release+Strategies+and+the+Social+Impacts+of+Language+Models%E2%80%99.+arXiv%2C+Nov.+12%2C+2019.+Accessed%3A+Feb.+21%2C+2023.+%5BOnline%5D.+Available%3A+http%3A%2F%2Farxiv.org%2Fabs%2F1908.09203"},{"title":"Release Strategies and the Social Impacts of Language Models","url":"https://www.catalyzex.com/paper/arxiv:1908.09203"},{"title":"Paper page - Release Strategies and the Social Impacts of Language Models","url":"https://huggingface.co/papers/1908.09203"},{"title":"Natural Fingerprints of Large Language Models","url":"https://arxiv.org/html/2504.14871v2"},{"title":"Human Variability vs. Machine Consistency: A Linguistic Analysis of Texts Generated by Humans and Large Language Models","url":"https://arxiv.org/html/2412.03025"}]

The full author list for arxiv 1908.09203 "Release Strategies and the Social Impacts of Language Models" is: Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim, Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kri
…[truncated 132 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-26T10:34:47.763154+00:00_

Web search results for query: "Sadasivan "Stress Testing AI Text Detectors" TMLR 2025 published accepted March"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"M-DAIGT: A Shared Task on Multi-Domain Detection of AI-Generated Text","url":"https://arxiv.org/pdf/2511.11340"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large   Language Models","url":"https://arxiv.org/pdf/2412.05139"},{"title":"Adversarial Attacks on AI-Generated Text Detection Models: A Token   Probability-Based Approach Using Embeddings","url":"https://arxiv.org/pdf/2501.18998"}]

Based on the search results, I found the paper you're looking for:

"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi was accepted and published at TMLR on March 13, 2025. The action editor was Kamalika Chaudhuri.

The paper introduces recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework 
…[truncated 311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T10:34:47.763312+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\" Dugan Hwang ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors\" Dugan Hwang ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-26T10:34:47.763444+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Schaeffer\" \"Kazdan\" \"Arulandu\" \"Model Collapse Does Not Mean\" authors Caleb Alvan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Schaeffer\" \"Kazdan\" \"Arulandu\" \"Model Collapse Does Not Mean\" authors Caleb Alvan"
  }
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-26T10:34:47.763592+00:00_

Web search results for query: "SynthID text Nature volume 634 pages 818 2024 authors list"

Links: [{"title":"Scalable watermarking for identifying large language model outputs | Nature","url":"https://www.nature.com/articles/s41586-024-08025-4"},{"title":"GitHub - google-deepmind/synthid-text · GitHub","url":"https://github.com/google-deepmind/synthid-text"},{"title":"818 | Nature | Vol 634 | 24 October 2024 Article","url":"https://www.nature.com/articles/s41586-024-08025-4.pdf"},{"title":"Volume 634 | Nature","url":"https://www.nature.com/nature/volumes/634"},{"title":"AI watermarking must be watertight to be effective","url":"https://www.nature.com/articles/d41586-024-03418-x"},{"title":"(PDF) Scalable watermarking for identifying large language model outputs","url":"https://www.researchgate.net/publication/385176946_Scalable_watermarking_for_identifying_large_language_model_outputs"},{"title":"Scalable watermarking for identifying large language model outputs – ScienceOpen","url":"https://www.scienceopen.com/document?vid=e36b034b-6be1-439b-bccb-f413efc57773"},{"title":"Robustness Assessment and Enhancement of Text Watermarking for Google’s SynthID","url":"https://arxiv.org/html/2508.20228v1"},{"title":"Volume 634 Issue 8035, 24 October 2024","url":"https://www.nature.com/nature/volumes/634/issues/8035"}]

Based on the search results, here is the complete author list for the SynthID-Text article published in Nature:

Sumanth Dathathri, Abigail See, Sumedh Ghaisas, Po-Sen Huang, Rob McAdam, Johannes Welbl, Vandana Bachani, Alex Kaskasoli, Robert Stanforth, Tatiana Matejovicova, Jamie Hayes, Nidhi Vyas, Majd Al Merey, Jonah Brown-Cohen, Rudy Bunel, Borja Balle, Taylan Cemgil, Zahra Ahmed, Kitty Stacpoole, Ilia Shumailov, Ciprian Baetu, Sven Gowal, Demis Hassabis, and Pushmeet Kohli.

The article is titled "Scalable watermarking for identifying large language model outputs" and was published in Nature volume 634, pages 818–823 (2024).


REMINDER: You MUST include th
…[truncated 71 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-26T10:34:47.763763+00:00_

Web search results for query: "Stamatatos 2009 "authorship attribution" JASIST volume 60 number pages"

Links: [{"title":"dblp: JASIST, Volume 60, 2009","url":"https://dblp.org/db/journals/jasis/jasis60.html"},{"title":"A survey of modern authorship attribution methods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-survey-of-modern-authorship-attribution-methods-Stamatatos/050dc61904fb3ab1add296ad98a7aefbcd8020a5"},{"title":"dblp: A survey of modern authorship attribution methods.","url":"https://dblp.org/rec/journals/jasis/Stamatatos09.html"},{"title":"A survey of modern authorship attribution methods","url":"https://ideas.repec.org/a/bla/jamist/v60y2009i3p538-556.html"},{"title":"Stamatatos, E. (2009) A Survey of Modern Authorship Attribution Methods. Journal of the American Society for Information Science and Technology, 60, 538-556. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2540164"},{"title":"A survey of modern authorship attribution methods. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/19b36b85e07a64fd5295da2a2ad9a9efb"},{"title":"A survey of modern authorship attribution methods - Stamatatos - 2009 - Journal of the American Society for Information Science and Technology - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/asi.21001"},{"title":"(PDF) A survey of modern authorship attribution methods (2009) | Efstathios Stamatatos | 1366 Citations","url":"https://scispace.com/papers/a-survey-of-modern-authorship-attribution-methods-2lb4q2gu7n"},{"title":"JASIST: Vol 60, No 1 - ACM Digital Library","url":"https://dl.acm.org/toc/jasist/2009/60/1"}]

Based on the search results, here is the complete citation information for the Stamatatos 2009 article:

**Author:** Efstathios Stamatatos

**Title:** A survey of modern authorship attribution methods

**Journal:** Journal of the American Society for Information Science and Technology (JASIST)

**
…[truncated 193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-26T10:34:47.763912+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Krishna \"Paraphrasing evades detectors\" NeurIPS 2023 exact title capitalization proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Krishna \"Paraphrasing evades detectors\" NeurIPS 2023 exact title capitalization proceedings"
  }
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-26T10:34:47.764038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Curious Case of Neural Text Degeneration\" authors \"Li Du\" OR \"Leo Du\" Holtzman Buys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Curious Case of Neural Text Degeneration\" authors \"Li Du\" OR \"Leo Du\" Holtzman Buys"
  }
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T10:34:47.764167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"A Survey on LLM-Generated Text Detection\" Wu Yang Zhan 2025 Computational Linguistics authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"A Survey on LLM-Generated Text Detection\" Wu Yang Zhan 2025 Computational Linguistics authors"
  }
}
```

</details>

---

### Tool result

_source line 197 · 2026-05-26T10:34:47.764301+00:00_

Web search results for query: ""Soft Labels for Ordinal Regression" Diaz Marathe CVPR 2019"

Links: [{"title":"Soft Labels for Ordinal Regression - CVF Open Access","url":"https://openaccess.thecvf.com/content_CVPR_2019/html/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.html"},{"title":"Soft Labels for Ordinal Regression","url":"https://openaccess.thecvf.com/content_CVPR_2019/papers/Diaz_Soft_Labels_for_Ordinal_Regression_CVPR_2019_paper.pdf"},{"title":"Soft Labels for Ordinal Regression Ra´ul D´ıaz, Amit Marathe HP Inc.","url":"https://rauldiaz.github.io/pdfs/sord_cvpr_2019.pdf"},{"title":"Soft Labels for Ordinal Regression","url":"https://www.researchgate.net/publication/338511937_Soft_Labels_for_Ordinal_Regression"},{"title":"Soft Labels for Ordinal Regression","url":"https://www.computer.org/csdl/proceedings-article/cvpr/2019/329300e733/1gyr8A2OoRW"},{"title":"Soft Labels for Ordinal Regression | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8953836/"},{"title":"Soft Labels for Ordinal Regression","url":"https://paperswithcode.com/paper/soft-labels-for-ordinal-regression"},{"title":"Calibration of ordinal regression networks","url":"https://arxiv.org/html/2410.15658v2"},{"title":"An Ordinal Regression Framework for a Deep Learning Based Severity Assessment for Chest Radiographs","url":"https://arxiv.org/html/2402.05685v1"}]

I found the paper! Here are the key details about "Soft Labels for Ordinal Regression" by Diaz and Marathe from CVPR 2019:

## Paper Overview

The paper addresses ordinal regression, which attempts to solve classification problems in which categories are not independent, but rather follow a natural order.

## Main Contribution

The authors present a method that constrains relationships among categories by seamlessly incorporating metric penalties into ground truth label representations, allowing deep neural networks to automatically learn intraclass and interclass relationships without any e
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-26T10:34:47.764451+00:00_

Web search results for query: ""Schaeffer" "Kazdan" "Arulandu" "Model Collapse Does Not Mean" authors Caleb Alvan"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Escaping Collapse: The Strength of Weak Data for Large Language Model TrainingAuthors ordered alphabetically. Author contributions are listed at the end.","url":"https://arxiv.org/html/2502.08924v2"},{"title":"Sanmi Koyejo, Rylan Schaeffer, Joshua Kazdan, Alvan Arlando, Angelina Wang · Model Collapse Does Not Mean What You Think","url":"https://slideslive.com/39038994/model-collapse-does-not-mean-what-you-think"},{"title":"LLM Web Dynamics: Tracing Model Collapse in a Network of LLMs","url":"https://arxiv.org/html/2506.15690v1"},{"title":"Model collapse occurs under some definitions, but does not occur under... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Model-collapse-occurs-under-some-definitions-but-does-not-occur-under-others-for-the_tbl1_389617145"},{"title":"Alvan Caleb Arulandu","url":"https://arxiv.org/search/?searchtype=author&query=Alvan+Caleb+Arulandu"}]

Based on the search results, I found the paper you're looking for:

**"Position: Model Collapse Does Not Mean What You Think"** by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

The paper addresses concerns over model collapse, which is a degradation in future generative models' performance when trained o
…[truncated 670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-26T10:34:47.764629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Exploring Ordinality in Text Classification\" Kasa Findings ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Exploring Ordinality in Text Classification\" Kasa Findings ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-26T10:34:47.764776+00:00_

Web search results for query: "Krishna "Paraphrasing evades detectors" NeurIPS 2023 exact title capitalization proceedings"

Links: [{"title":"NeurIPS Poster Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://neurips.cc/virtual/2023/poster/71402"},{"title":"GitHub - martiansideofthemoon/ai-detection-paraphrases: Official repository for our NeurIPS 2023 paper \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\" (https://arxiv.org/abs/2303.13408). · GitHub","url":"https://github.com/martiansideofthemoon/ai-detection-paraphrases"},{"title":"[PDF] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Paraphrasing-evades-detectors-of-AI-generated-text,-Krishna-Song/1c13af186d1e177b85ef1ec3fc7b8d33ec314cfd"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | OpenReview","url":"https://openreview.net/forum?id=WbFhFvjjKj"},{"title":"[2303.13408] Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://arxiv.org/abs/2303.13408"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense","url":"https://papers.nips.cc/paper_files/paper/2023/hash/575c450013d0e99e4b0ecf82bd1afaa4-Abstract-Conference.html"},{"title":"Paraphrasing evades detectors of AI-generated text, but ...","url":"https://openreview.net/pdf?id=WbFhFvjjKj"},{"title":"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense | Request PDF","url":"https://www.researchgate.net/publication/369477232_Paraphrasing_evades_detectors_of_AI-generated_text_but_retrieval_is_an_effective_defense"},{"title":"No Free Lunch in LLM Watermarking: Trade-offs in Watermarking Design Choices","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/fa86a9c7b9f
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-26T10:34:47.764930+00:00_

Web search results for query: ""The Curious Case of Neural Text Degeneration" authors "Li Du" OR "Leo Du" Holtzman Buys"

Links: [{"title":"[PDF] The Curious Case of Neural Text Degeneration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Case-of-Neural-Text-Degeneration-Holtzman-Buys/cf4aa38ae31b43fd07abe13b4ffdb265babb7be1"},{"title":"[Paper Note] The Curious Case of Neural Text Degeneration, Ari Holtzman+, ICLR'20 · Issue #1889 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1889"},{"title":"The Curious Case of Neural Text Degeneration - UCT Computer Science Research Document Archive","url":"https://pubs.cs.uct.ac.za/id/eprint/1407/"},{"title":"The Curious Case of Neural Text Degeneration | OpenReview","url":"https://openreview.net/forum?id=rygGQyrFvH"},{"title":"dblp: The Curious Case of Neural Text Degeneration.","url":"https://dblp.org/rec/conf/iclr/HoltzmanBDFC20.html"},{"title":"The curious case of neural text degeneration","url":"https://ceur-ws.org/Vol-2540/FAIR2019_paper_15.pdf"},{"title":"[1904.09751] The Curious Case of Neural Text Degeneration","url":"https://arxiv.org/abs/1904.09751"},{"title":"The Curious Case of Neural Text Degeneration. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/229fdab5aeb4deb740ceb07a72a6e9058/albinzehe"},{"title":"The Curious Case of Neural Text Degeneration. | PUMA","url":"https://puma.ub.uni-stuttgart.de/bibtex/1ce28540963fab56aa0395674be178bf9"},{"title":"THE CURIOUS CASE OF NEURAL TEXT DeGENERATION","url":"https://openreview.net/pdf?id=rygGQyrFvH"}]

Based on the search results, I found the paper you're looking for:

"The Curious Case of Neural Text Degeneration" is authored by Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 

The paper was published in the Proceedings of the International Conference on Learning Representations in 2020. The paper shows that maximization-based decoding methods such as beam search lead to degenera
…[truncated 228 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-26T10:34:47.765092+00:00_

Web search results for query: ""RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors" Dugan Hwang ACL 2024"

Links: [{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.674/"},{"title":"[2405.07940] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/abs/2405.07940"},{"title":"GitHub - liamdugan/raid: RAID is the largest and most challenging benchmark for AI-generated text detection. (ACL 2024) · GitHub","url":"https://github.com/liamdugan/raid"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Request PDF","url":"https://www.researchgate.net/publication/384214327_RAID_A_Shared_Benchmark_for_Robust_Evaluation_of_Machine-Generated_Text_Detectors"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://arxiv.org/html/2405.07940v1"},{"title":"[Quick Review] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors","url":"https://liner.com/review/raid-shared-benchmark-for-robust-evaluation-machinegenerated-text-detectors"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors - Liam Dugan","url":"https://liamdugan.com/talks/2024-08-10-raid-benchmark"},{"title":"[PDF] RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAID:-A-Shared-Benchmark-for-Robust-Evaluation-of-Dugan-Hwang/a28474db72957c239127374cfee3c8ed8190defc"},{"title":"RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10563509-raid-shared-benchmark-robust-evaluation-machine-generated-text-detectors"}]

I found the paper for you. Here are the key details:

**Paper Titl
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T10:34:47.765249+00:00_

Web search results for query: "site:aclanthology.org "A Survey on LLM-Generated Text Detection" Wu Yang Zhan 2025 Computational Linguistics authors"

Links: [{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions - ACL Anthology","url":"https://aclanthology.org/2025.cl-1.8/"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/51/1/275/127462/A-Survey-on-LLM-Generated-Text-Detection-Necessity"},{"title":"[2310.14724] A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/abs/2310.14724"},{"title":"A Survey on LLM-Generated Text Detection:","url":"https://aclanthology.org/2025.cl-1.8.pdf"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/2687"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Junchao+Wu%2C+Shu+Yang%2C+Runzhe+Zhan%2C+Yulin+Yuan%2C+Lidia+Sam+Chao%2C+and+Derek+Fai+Wong.+2025.+A+survey+on+LLM-generated+text+detection%3A+Necessity%2C+methods%2C+and+future+directions.+Computational+Linguistics%282025%29%2C+1-65."},{"title":"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://arxiv.org/html/2310.14724v3"},{"title":"(PDF) A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions","url":"https://www.researchgate.net/publication/387905627_A_Survey_on_LLM-Generated_Text_Detection_Necessity_Methods_and_Future_Directions"}]

I found the paper you were looking for! Here are the key details:

**Paper Title:** A Survey on LLM-Generated Text Detection: Necessity, Methods, and Fut
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-26T10:34:47.765398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Seddik \"How Bad is Training on Synthetic Data\" COLM 2024 authors \"Suei-Wen Chen\" \"Pierre Youssef\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Seddik \"How Bad is Training on Synthetic Data\" COLM 2024 authors \"Suei-Wen Chen\" \"Pierre Youssef\""
  }
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-26T10:34:47.765528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DivEye \"Diversity Boosts AI-Generated Text Detection\" Basani venue ICLR 2026 TMLR published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DivEye \"Diversity Boosts AI-Generated Text Detection\" Basani venue ICLR 2026 TMLR published"
  }
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-26T10:34:47.765673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Human Texts Are Outliers: Rethinking Machine-Generated Text Detection\" Li Hu Guo arXiv 2510.08602"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Human Texts Are Outliers: Rethinking Machine-Generated Text Detection\" Li Hu Guo arXiv 2510.08602"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-26T10:34:47.765806+00:00_

Web search results for query: ""Exploring Ordinality in Text Classification" Kasa Findings ACL 2024"

Links: [{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.320/"},{"title":"[2405.11775] Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/abs/2405.11775"},{"title":"Generative or Discriminative? Revisiting Text Classification in the Era of Transformers","url":"https://arxiv.org/html/2506.12181v1"},{"title":"Accepted Findings Papers - ACL 2024","url":"https://2024.aclweb.org/program/finding_papers/"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques | OpenReview","url":"https://openreview.net/forum?id=XUqyfa8X14"},{"title":"Computation and Language May 2024","url":"https://arxiv.org/list/cs.CL/2024-05?skip=600&show=100"},{"title":"Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques","url":"https://arxiv.org/html/2405.11775"},{"title":"Exploring ordinality in text classification: A comparative study of explicit and implicit techniques - Amazon Science","url":"https://www.amazon.science/publications/exploring-ordinality-in-text-classification-a-comparative-study-of-explicit-and-implicit-techniques"}]

I found the paper! Here are the search results for "Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques" by Kasa et al. at ACL 2024 Findings:

## Paper Details

The paper was authored by Siva Rajesh Kasa, Aniket Goel, Karan Gupta, Sumegh Roychowdhury, Pattisapu Priyatam, Anish Bhanushali, and Prasanna Srinivasa Murthy, and published in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand on pages 5390–5404.

## Research Overview

The paper addresses Ordinal Classification (OC
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-26T10:34:47.765958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"XGBoost: A Scalable Tree Boosting System\" Chen Guestrin KDD 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"XGBoost: A Scalable Tree Boosting System\" Chen Guestrin KDD 2016"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-26T10:34:47.766089+00:00_

Web search results for query: "Seddik "How Bad is Training on Synthetic Data" COLM 2024 authors "Suei-Wen Chen" "Pierre Youssef""

Links: [{"title":"[2404.05090] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/abs/2404.05090"},{"title":"How Bad is Training on Synthetic Data? A Statistical ...","url":"https://openreview.net/pdf/4b55130ce33429ab600e5cde927dfe10a36328ba.pdf"},{"title":"[PDF] How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Bad-is-Training-on-Synthetic-Data-A-Statistical-Seddik-Chen/1f71820adfe5eaa344494b1158cbe46ca2d00fc3"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/how-bad-is-training-synthetic-data-statistical"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse | alphaXiv","url":"https://www.alphaxiv.org/resources/2404.05090v1"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis","url":"https://arxiv.org/pdf/2404.05090"},{"title":"Does Training on Synthetic Data Make Models Less Robust?","url":"https://arxiv.org/html/2502.07164v1"},{"title":"Real vs Synthetic Data: Is Generative Content in Need of Human Touch - Khalifa University","url":"https://www.ku.ac.ae/real-vs-synthetic-data-is-generative-content-in-need-of-human-touch"}]

I found the paper you're looking for! Here are the details:

**Paper Title:** "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse," published as a conference paper at COLM 2024

**Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane De
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-26T10:34:47.766229+00:00_

Web search results for query: ""Human Texts Are Outliers: Rethinking Machine-Generated Text Detection" Li Hu Guo arXiv 2510.08602"

Links: [{"title":"[2510.08602] Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/abs/2510.08602"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/html/2510.08602v1"},{"title":"(PDF) Human Texts Are Outliers: Detecting LLM-generated ...","url":"https://arxiv.org/pdf/2510.08602"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Hidden Human-Like Nature of Machine-Generated Texts: Theory and Detection Enhancement","url":"https://arxiv.org/html/2605.23190"},{"title":"[2406.18259] Detecting Machine-Generated Texts: Not Just \"AI vs Humans\" and Explainability is Complicated","url":"https://arxiv.org/abs/2406.18259"},{"title":"multiscale positive-unlabeled detection of ai-generated texts","url":"https://arxiv.org/pdf/2305.18149"},{"title":"MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/html/2305.13242v3"}]

I found the paper for you. Here's a summary of the key information:

The paper addresses the rapid advancement of large language models (LLMs) such as ChatGPT, DeepSeek, and Claude, which has significantly increased the presence of AI-generated text in digital communication, heightening the need for reliable detection methods to distinguish between human-authored and machine-generated content.

**Main Argument:**

The paper argues that treating machine-generated text detection as a binary classification problem fundamentally mischaracterizes the task by assuming a coherent representation of human-written texts, when in reality human texts do not constitute a unified distribution and their diversity cannot be effectively captured through limited sampling.

**Proposed Solutio
…[truncated 423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-26T10:34:47.766375+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "QuRating ICML 2024 authors Wettig Gupta Malik Chen complete author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "QuRating ICML 2024 authors Wettig Gupta Malik Chen complete author list"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-26T10:34:47.766506+00:00_

Web search results for query: "DivEye "Diversity Boosts AI-Generated Text Detection" Basani venue ICLR 2026 TMLR published"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"DivEye","url":"https://diveye.vercel.app/"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://www.arxiv.org/pdf/2509.18880v1"}]

Based on the search results, I found information about DivEye and the paper "Diversity Boosts AI-Generated Text Detection":

**Paper Details:**
The paper is authored by Advik Raj Basani from Birla Institute of Technology and Science, Goa and Pin-Yu Chen from IBM Research.

**Regarding Publication Venue:**
The search results show conflicting information about the venue:
- One source (GitHub) indicates the paper was published at "Data in Generative Models - The Bad, the Ugly, and the Greats" in 2025
- Another source (OpenReview) shows a different submission ID (DNgsOhGZBI) on OpenReview
- The paper also appe
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-26T10:34:47.766677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood\" Xu Wang An arXiv 2406.19874"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood\" Xu Wang An arXiv 2406.19874"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-26T10:34:47.766806+00:00_

Web search results for query: ""XGBoost: A Scalable Tree Boosting System" Chen Guestrin KDD 2016"

Links: [{"title":"Chen, T. and Guestrin, C. (2016) XGBoost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3417949"},{"title":"XGBoost: A Scalable Tree Boosting System Tianqi Chen University of Washington","url":"https://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf"},{"title":"[1603.02754] XGBoost: A Scalable Tree Boosting System","url":"https://arxiv.org/abs/1603.02754"},{"title":"[PDF] XGBoost: A Scalable Tree Boosting System | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGBoost:-A-Scalable-Tree-Boosting-System-Chen-Guestrin/26bc9195c6343e4d7f434dd65b4ad67efe2be27a"},{"title":"Chen, T.Q. and Guestrin, C. (2016) Xgboost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3251268"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://www.kdd.org/kdd2016/subtopic/view/xgboost-a-scalable-tree-boosting-system"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://bibbase.org/network/publication/chen-guestrin-xgboostascalabletreeboostingsystem-2016"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://www.researchgate.net/publication/310824798_XGBoost_A_Scalable_Tree_Boosting_System"},{"title":"XGBoost Paper | XGBoosting","url":"https://xgboosting.com/xgboost-paper/"}]

I found the paper you were looking for! Here are the search results:

## Publication Details

"XGBoost: A Scalable Tree Boosti
…[truncated 1154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-26T10:34:47.766979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:github.com/IBM/diveye TMLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:github.com/IBM/diveye TMLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-26T10:34:47.767100+00:00_

Web search results for query: "QuRating ICML 2024 authors Wettig Gupta Malik Chen complete author list"

Links: [{"title":"GitHub - princeton-nlp/QuRating: [ICML 2024] Selecting High-Quality Data for Training Language Models","url":"https://github.com/princeton-nlp/QuRating"},{"title":"[2402.09739] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739"},{"title":"ICLR QuRating: Selecting High-Quality Data for Training Language Models","url":"https://iclr.cc/virtual/2024/21159"},{"title":"[PDF] QuRating: Selecting High-Quality Data for Training Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/QuRating:-Selecting-High-Quality-Data-for-Training-Wettig-Gupta/34efdeaf0a78d6906b4da7335afc7182df11f639"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models","url":"https://proceedings.mlr.press/v235/wettig24a.html"},{"title":"[2402.09739v3] QuRating: Selecting High-Quality Data for Training Language Models","url":"https://arxiv.org/abs/2402.09739v3"},{"title":"QuRating: Selecting High-Quality Data for Training Language Models | OpenReview","url":"https://openreview.net/forum?id=GLGYYqPwjy"},{"title":"ICML 2024 Reviewers","url":"https://icml.cc/Conferences/2024/Reviewers"}]

Based on the search results, the complete author list for the QuRating paper at ICML 2024 is: Alexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-26T10:34:47.767243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2304.01373 Pythia authors full list Biderman Schoelkopf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2304.01373 Pythia authors full list Biderman Schoelkopf"
  }
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T10:34:47.767372+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Aaronson Kirchner watermarking GPT authors \"Jan Hendrik Kirchner\" OR \"Hendrik Kirchner\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Aaronson Kirchner watermarking GPT authors \"Jan Hendrik Kirchner\" OR \"Hendrik Kirchner\""
  }
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-26T10:34:47.767497+00:00_

Web search results for query: "site:github.com/IBM/diveye TMLR 2026"

Links: [{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Published in Transactions on Machine Learning Research (02/2026)","url":"https://arxiv.org/pdf/2509.18880"},{"title":"IBM on GitHub","url":"https://ibm.github.io/"},{"title":"TMLR Group · GitHub","url":"https://github.com/tmlr-group"},{"title":"International Business Machines · GitHub","url":"https://github.com/IBM"},{"title":"tmlr-2026 · GitHub Topics · GitHub","url":"https://github.com/topics/tmlr-2026"},{"title":"GitHub Enterprise - IBM","url":"https://github.ibm.com/login"},{"title":"IBM repositories · GitHub","url":"https://github.com/orgs/IBM/repositories"},{"title":"tmlr · GitHub Topics · GitHub","url":"https://github.com/topics/tmlr"},{"title":"IBM Security · GitHub","url":"https://github.com/ibm-security"}]

Based on the search results, I found relevant information about the IBM/diveye repository with TMLR 2026:

The repository is an official implementation of DivEye for the paper "Diversity Boosts AI-Generated Text Detection" which was accepted at TMLR '26 and ICML, Data in Generative Models (DIG-BUG) '25.

DivEye is motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, and it captures this signal through a set of interpretable statistical features. The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks.

DivEye is robust to paraphrasing and adversarial attacks, generalizes well across domains and models, and improves the performance of existing detectors by up to 18.7% when used as an auxiliary signal.

The GitHub repository is available at: https://github.com/IBM/diveye


REMINDER: You MUST include the sources above in your response to th
…[truncated 33 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-26T10:34:47.767666+00:00_

Web search results for query: ""Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood" Xu Wang An arXiv 2406.19874"

Links: [{"title":"[2406.19874] Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood","url":"https://arxiv.org/abs/2406.19874"},{"title":"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood","url":"https://arxiv.org/html/2406.19874"},{"title":"Detecting Subtle Differences between Human and Model Languages Using","url":"https://arxiv.org/pdf/2406.19874"},{"title":"(PDF) Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood","url":"https://www.researchgate.net/publication/381851117_Detecting_Subtle_Differences_between_Human_and_Model_Languages_Using_Spectrum_of_Relative_Likelihood"},{"title":"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.564/"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=9390&show=1000"}]

I found the paper successfully! Here's the information about this research:

## Paper Summary

Human and model-generated texts can be distinguished by examining the magnitude of likelihood in language, however it is becoming increasingly difficult as language model's capabilities of generating human-like texts keep evolving.

The study provides a new perspective by using the relative likelihood values instead of absolute ones, and extracting useful features from the spectrum-view of likelihood for the human-model text detection task.

## Key Methodology

The core idea is to obtain the spectrum of likelihood using the Fourier transform, which summarizes the complex patterns of likelihood change in time domain into a much more compact view that magnifies the subtle differences between different texts. The appro
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-26T10:34:47.767816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers\" Pillutla Swayamdipta NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers\" Pillutla Swayamdipta NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-26T10:34:47.767945+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected?\" shorter title without \"Stress Testing\" Sadasivan TMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Can AI-Generated Text be Reliably Detected?\" shorter title without \"Stress Testing\" Sadasivan TMLR"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T10:34:47.768070+00:00_

Web search results for query: "arxiv 2304.01373 Pythia authors full list Biderman Schoelkopf"

Links: [{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/pdf/2304.01373"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://ar5iv.labs.arxiv.org/html/2304.01373"},{"title":"Paper page - Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://huggingface.co/papers/2304.01373"},{"title":"[2304.01373v1] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373v1"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"},{"title":"(PDF) Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://www.researchgate.net/publication/369792568_Pythia_A_Suite_for_Analyzing_Large_Language_Models_Across_Training_and_Scaling"},{"title":"Pythia: A Suite for Analyzing Large Language Models Acros...","url":"https://www.researchhub.com/paper/1275740/pythia-a-suite-for-analyzing-large-language-models-across-training-and-scaling"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/journals/corr/abs-2304-01373.html"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/?searchtype=author&query=Stella+Biderman"}]

Based on the search results for arxiv 2304.01373, the full list of authors is: Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Bri
…[truncated 404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-26T10:34:47.768218+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.04932 \"Beyond the Final Actor\" authors Li Sheng Wang Yang Cao ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.04932 \"Beyond the Final Actor\" authors Li Sheng Wang Yang Cao ACL 2026"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-26T10:34:47.768362+00:00_

Web search results for query: "Aaronson Kirchner watermarking GPT authors "Jan Hendrik Kirchner" OR "Hendrik Kirchner""

Links: [{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"},{"title":"Ensemble Watermarks for Large Language Models","url":"https://aclanthology.org/2025.acl-long.145.pdf"},{"title":"STYLOMETRIC WATERMARKS FOR LARGE LANGUAGE MODELS A PREPRINT Georg Niess","url":"https://arxiv.org/pdf/2405.08400"},{"title":"ChatGPT: Metadata 'watermark' could help combat plagiarism fears","url":"https://www.techmonitor.ai/digital-economy/ai-and-automation/chatgpt-plagiarism-metadata-watermark"},{"title":"Watermarking text in LLM outputs – Dr Alan D. Thompson","url":"https://lifearchitect.ai/watermarking/"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://cic.iacr.org/p/1/4/31"},{"title":"Three Bricks to Consolidate Watermarks for Large Language Models | Pierre Fernandez","url":"https://pierrefdz.github.io/publications/threebricks/"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://arxiv.org/html/2310.18491"},{"title":"Watermark under Fire: A Robustness Evaluation of LLM Watermarking | Request PDF","url":"https://www.researchgate.net/publication/397422053_Watermark_under_Fire_A_Robustness_Evaluation_of_LLM_Watermarking"}]

Based on the search results, here's what I found about Aaronson and Kirchner's work on watermarking for GPT:

Jan Hendrik Kirchner, Jan Ahmad, Scott Aaronson, and Jan Leike authored work on watermarking for language models. Jan Hendrik Kirchner, Jan Ahmad, Scott Aaronson, and Jan Leike published "New AI classifier for indicating AI-written text" in January 2023.

A working prototype of the watermarking scheme was built by OpenAI engineer Hendrik Kirchner. The research focused on developing methods to detect AI-generated text through watermarking rather than through traditional detection approaches.

Scott Aaronson and Hendrik Kirc
…[truncated 332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-26T10:34:47.768563+00:00_

All searches are complete. Here are the verification results for all 12 entries:

---

### [stamatatos_survey] — A Survey of Modern Authorship Attribution Methods (2009)
- **Exists**: ✓
- **Authors**: ✓ (Stamatatos, Efstathios)
- **Year**: ✓ (2009)
- **Title**: ✓ (exact match)
- **Venue**: ✓ (Journal of the American Society for Information Science and Technology, volume 60, number 3, pages 538--556)
- **Notes**: All metadata verified correct.

### [koppel_authorship] — Computational Methods in Authorship Attribution (2009)
- **Exists**: ✓
- **Authors**: ✓ (Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo)
- **Year**: ✓ (2009)
- **Title**: ✓ (exact match)
- **Venue**: ✓ (JASIST, volume 60, number 1, pages 9--26)
- **Notes**: All metadata verified correct.

### [uchendu_attribution] — Authorship Attribution for Neural Text Generation (2020)
- **Exists**: ✓
- **Authors**: ✓ (Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon)
- **Year**: ✓ (2020)
- **Title**: ✓ (exact match)
- **Venue**: ✓ (EMNLP 2020, pages 8384--8395)
- **Notes**: All metadata verified correct.

### [munir_looking_glass] — Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models (2021)
- **Exists**: ✓
- **Authors**: ✓ (Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed)
- **Year**: ✓ (2021)
- **Title**: ✓ (exact match)
- **Venue**: ✓ (EACL 2021, pages 1811--1822)
- **Notes**: All metadata verified correct.

### [briesch_self_consuming] — Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop (2023)
- **Exists**: ✓
- **Authors**: ✓ (Briesch, Martin and Sobania, Dominik and Rothlauf, Franz)
- **Year**: ✓ (2023)
- **Title**: ✓ (exact match)
- **Venue**: ✓ (arXiv preprint arXiv:2311.16822)
- **Notes**: All metadata verified correct.

### [broken_telephone] — LLM as a Broken Telephone: Iterative Generation Distorts Information (2025)
- **Exists**: ✓
- **Authors**: ✓ (M
…[truncated 3031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 26
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-26T10:34:47.768750+00:00_

Web search results for query: ""Can AI-Generated Text be Reliably Detected?" shorter title without "Stress Testing" Sadasivan TMLR"

Links: [{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://bibbase.org/network/publication/sadasivan-kumar-balasubramanian-wang-feizi-canaigeneratedtextbereliablydetected-2023"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"}]

I found the paper you're looking for! Here's what I found:

**Paper Title:** "Can AI-Generated Text be Reliably Detected?"

**Authors:** Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi

**Publication:** Published at TMLR (Transactions on Machine Learning Research) with Kamalika Chaudhuri as the action editor

**Main Findings:*
…[truncated 725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-26T10:34:47.768905+00:00_

Web search results for query: ""MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers" Pillutla Swayamdipta NeurIPS 2021"

Links: [{"title":"MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers","url":"https://proceedings.neurips.cc/paper/2021/hash/260c2432a0eecc28ce03c10dadc078a4-Abstract.html"},{"title":"GitHub - krishnap25/mauve: Package to compute Mauve, a similarity score between neural text and human text. Install with `pip install mauve-text`. · GitHub","url":"https://github.com/krishnap25/mauve"},{"title":"GitHub - krishnap25/mauve-experiments · GitHub","url":"https://github.com/krishnap25/mauve-experiments"},{"title":"Allen School News » Allen School and AI2 researchers paint the NeurIPS conference MAUVE and take home an Outstanding Paper Award","url":"https://news.cs.washington.edu/2022/02/28/allen-school-and-ai2-researchers-paint-the-neurips-conference-mauve-and-take-home-an-outstanding-paper-award/"},{"title":"[2102.01454] MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers","url":"https://arxiv.org/abs/2102.01454"},{"title":"mauve-text · PyPI","url":"https://pypi.org/project/mauve-text/"},{"title":"Accurate modeling of human-like and interestingness of generated text: MAUVE | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/natural-language-processing/mauve"},{"title":"mauve-experiments/README.md at main · krishnap25/mauve-experiments","url":"https://github.com/krishnap25/mauve-experiments/blob/main/README.md"},{"title":"[PDF] MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAUVE:-Measuring-the-Gap-Between-Neural-Text-and-Pillutla-Swayamdipta/8484fdb56e4690927dc0191ede11c2d24bc5e2ef"},{"title":"MAUVE: Measuring the Gap Between Neural Text and Human Text","url":"https://proc
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-26T10:34:47.769077+00:00_

Web search results for query: "arxiv 2604.04932 "Beyond the Final Actor" authors Li Sheng Wang Yang Cao ACL 2026"

Links: [{"title":"[2604.04932] Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/abs/2604.04932"},{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/html/2604.04932"},{"title":"[2604.23792] Beyond the Final Label: Exploiting the Untapped Potential of Classification Histories in Astronomical Light Curve Analysis","url":"https://arxiv.org/abs/2604.23792"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=84&show=2000"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure","url":"https://arxiv.org/html/2604.02547v1"},{"title":"Beyond Final Code: A Process-Oriented Error Analysis of Software Development Agents in Real-World GitHub Scenarios","url":"https://arxiv.org/html/2503.12374v3"},{"title":"[2604.05467v1] CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2604.05467v1"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=725&show=2000"}]

Based on the search results, I found the paper you're looking for:

**Paper Details:**

The paper titled "Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection" (arXiv:2604.04932) was submitted on April 6, 2026, with authors Yang Li, Qiang Sheng, Zhengjia Wang, Yehan Yang, Danding Wang, and Juan Cao.

**Summary:**

The paper explores fine-grained LLM-generated text detection under a four-class setting. The authors propose RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creato
…[truncated 348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-26T10:34:47.769292+00:00_

Now I have all the information needed. Let me compile the verification results.

Here are the verification results for all 12 bibliography entries:

---

### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)
- **Exists**: ✓
- **Authors**: ✓ (Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya -- all confirmed via NeurIPS proceedings)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2023)
- **Notes**: Confirmed at [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7baa48bc166aa2013d78cbdc15010530-Abstract-Conference.html) and [arXiv:2306.04723](https://arxiv.org/abs/2306.04723).

---

### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)
- **Exists**: ✓
- **Authors**: ✓ (Wang Pengyu, Li Linyang, Ren Ke, Jiang Botian, Zhang Dong, Qiu Xipeng -- all confirmed via [ACL Anthology](https://aclanthology.org/2023.emnlp-main.73/))
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (EMNLP 2023)
- **Notes**: All clean.

---

### [grover] — Defending Against Neural Fake News (2019)
- **Exists**: ✓
- **Authors**: ✓ (Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi -- all confirmed)
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2019)
- **Notes**: All clean. [arXiv:1905.12616](https://arxiv.org/abs/1905.12616).

---

### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)
- **Exists**: ✓
- **Authors**: ✓ (Solaiman, Brundage, Clark, Askell, Herbert-Voss, Wu, Radford, Krueger, Kim, Kreps, McCain, Newhouse, Blazakis, McGuffie, Wang -- all 15 authors confirmed via [arXiv:1908.09203](https://arxiv.org/abs/1908.09203))
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:1908.09203)
- **Notes**: All clean.

---

### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement 
…[truncated 3958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-26T10:34:47.769456+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Beyond the Final Actor\" RACE creator editor ACL 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Beyond the Final Actor\" RACE creator editor ACL 2026 accepted"
  }
}
```

</details>

---

### Tool call

_source line 232 · 2026-05-26T10:34:47.769606+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.08602 \"Human Texts Are Outliers\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.08602 \"Human Texts Are Outliers\" authors full list"
  }
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-26T10:34:47.769737+00:00_

Web search results for query: ""Beyond the Final Actor" RACE creator editor ACL 2026 accepted"

Links: [{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/html/2604.04932"},{"title":"[2604.04932] Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/abs/2604.04932"},{"title":"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection","url":"https://arxiv.org/pdf/2604.04932"},{"title":"Neural Coreference Resolution based on Reinforcement Learning","url":"https://arxiv.org/pdf/2212.09028"},{"title":"CL Scholar: The ACL Anthology Knowledge Graph Miner","url":"https://arxiv.org/pdf/1804.05514"}]

Based on the search results, I found relevant information about your query:

**"Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection"** is authored by Yang Li, Qiang Sheng, Zhengjia Wang, Yehan Yang, Danding Wang, and Juan Cao from the Institute of Computing Technology, Chinese Academy of Sciences and University of Chinese Academy of Sciences.

The paper proposes RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creator and editor. RACE utilizes Rhetorical Structure Theory to construct a logic graph for the creator's foundation while extracting Elementary Discourse Unit-level features for the editor's style.

The paper was dated April 7th, 2026, and is scheduled for presentation at ACL 2026, confirming it has been accepted to the venue. The project information is available at https://race.yang-li.cn.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-26T10:34:47.769881+00:00_

Web search results for query: "arxiv 2510.08602 "Human Texts Are Outliers" authors full list"

Links: [{"title":"[2510.08602] Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/abs/2510.08602"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/html/2510.08602"},{"title":"(PDF) Human Texts Are Outliers: Detecting LLM-generated ...","url":"https://arxiv.org/pdf/2510.08602"},{"title":"GitHub - cong-zeng/ood-llm-detect · GitHub","url":"https://github.com/cong-zeng/ood-llm-detect"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection | OpenReview","url":"https://openreview.net/forum?id=0XKZFK4hQt"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://www.nec-labs.com/blog/human-texts-are-outliers-detecting-llm-generated-texts-via-out-of-distribution-detection/"},{"title":"Human Texts Are Outliers: Detecting LLM-generated","url":"https://openreview.net/pdf?id=0XKZFK4hQt"}]

Based on the search results, here is the complete list of authors for the arxiv paper 2510.08602 "Human Texts Are Outliers":

Cong Zeng, Shengkun Tang, Yuanzhou Chen, Zhiqiang Shen, Wenchao Yu, Xujiang Zhao, Haifeng Chen, Wei Cheng, and Zhiqiang Xu


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 235 · 2026-05-26T10:34:47.770026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2508.14190 \"Two Birds with One Stone\" Rao Mohamed year 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2508.14190 \"Two Birds with One Stone\" Rao Mohamed year 2025"
  }
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-26T10:34:47.770155+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\" Li Yafu Hu Zhilin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\" Li Yafu Hu Zhilin"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-26T10:34:47.770287+00:00_

Web search results for query: "arxiv 2508.14190 "Two Birds with One Stone" Rao Mohamed year 2025"

Links: [{"title":"[2508.14190] Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://arxiv.org/abs/2508.14190"},{"title":"Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://arxiv.org/html/2508.14190"},{"title":"(PDF) Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text","url":"https://www.researchgate.net/publication/394790500_Two_Birds_with_One_Stone_Multi-Task_Detection_and_Attribution_of_LLM-Generated_Text"},{"title":"[1711.00300] Killing Two Birds with One Stone: Malicious Domain Detection with High Accuracy and Coverage","url":"https://arxiv.org/abs/1711.00300"},{"title":"[2508.17097] Two Birds with One Stone: Enhancing Uncertainty Quantification and Interpretability with Graph Functional Neural Process","url":"https://arxiv.org/abs/2508.17097"},{"title":"[2106.00841] Two Birds With One Stone: Fairness and Welfare via Transfers","url":"https://arxiv.org/abs/2106.00841"},{"title":"[1912.05274] Two Birds with One Stone: Investigating Invertible Neural Networks for Inverse Problems in Morphology","url":"https://arxiv.org/abs/1912.05274"},{"title":"Two Birds with One Stone: Enhancing Uncertainty Quantification","url":"https://arxiv.org/pdf/2508.17097"},{"title":"[2412.20671] Two Birds with One Stone: Improving Rumor Detection by Addressing the Unfairness Issue","url":"https://arxiv.org/abs/2412.20671"}]

Based on the search results, I found the paper you're looking for:

**Title:** Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text

**ArXiv ID:** 2508.14190

**Authors:** Zixin Rao, Youssef Mohamed, Shang Liu, Zeyan Liu

**Submission Date:** August 19, 2025

**Summary:**

The paper presents DA-MTL, a multi-task learning framework that simultaneously addresses both text detection and authorship attribution, ev
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-26T10:34:47.770437+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pythia Biderman 2023 ICML author \"Quentin Gregory Anthony\" OR \"Quentin Anthony\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pythia Biderman 2023 ICML author \"Quentin Gregory Anthony\" OR \"Quentin Anthony\" full author list"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:34:47.770562+00:00_

Web search results for query: ""Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective" Li Yafu Hu Zhilin"

Links: [{"title":"MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/html/2305.13242v3"},{"title":"MAGE: Machine-generated Text Detection in the Wild - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.3/"},{"title":"[PDF] MAGE: Machine-generated Text Detection in the Wild | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAGE:-Machine-generated-Text-Detection-in-the-Wild-Li-Li/435f070f4779a184285917184899fbdb43bb6d7e"},{"title":"GitHub - yafuly/MAGE: Machine-generated text detection in the wild (ACL 2024) · GitHub","url":"https://github.com/yafuly/MAGE"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v1"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"[2510.08602] Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/abs/2510.08602"}]

Based on the search results, I found relevant information about machine-generated text detection research involving the authors you mentioned.

The most relevant paper appears to be "MAGE: Machine-generated Text Detection in the Wild", authored by Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang, Longyue Wang, Linyi Yang, Shuming Shi, and Yue Zhang. This paper was presented at the 62nd Annual Meeting of the Association for Computational Linguistics in 2024.

The paper addresses machine-generated text detection from an out-of-distribution perspective. The researchers built a comprehensive testbed by gathering texts from diverse human writings and texts generated by different LLMs, finding challenges in distinguishing machine-generated texts from h
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-26T10:34:47.770732+00:00_

Web search results for query: "Pythia Biderman 2023 ICML author "Quentin Gregory Anthony" OR "Quentin Anthony" full author list"

Links: [{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"},{"title":"GitHub - EleutherAI/pythia: The hub for EleutherAI's work on interpretability and learning dynamics · GitHub","url":"https://github.com/eleutherai/pythia"},{"title":"Pythia | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3618510"},{"title":"[2304.01373v1] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373v1"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://ar5iv.labs.arxiv.org/html/2304.01373"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Stella+Biderman,+Hailey+Schoelkopf,+Quentin+Gregory+Anthony,+Herbie+Bradley,+Kyle+O%E2%80%99Brien,+Eric+Hallahan,+Mohammad+Aflah+Khan,+Shivanshu+Purohit,+USVSN+Sai+Prashanth,+Edward+Raff,+et+al.+Pythia:+A+suite+for+analyzing+large+language+models+across+training+and+scaling.+In+International+Conference+on+Machine+Learning,+pages+2397%E2%80%932430.+PMLR,+2023."},{"title":"[2304.01373v2] Pythia: A Suite for Analyzing Large La
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-26T10:34:47.770879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Yafu \"Human Texts Are Outliers\" \"Rethinking\" machine-generated text detection OOD arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Yafu \"Human Texts Are Outliers\" \"Rethinking\" machine-generated text detection OOD arXiv 2025"
  }
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-26T10:34:47.771003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo ACL 2024 full author list aclanthology.org/2024.acl-long.841"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo ACL 2024 full author list aclanthology.org/2024.acl-long.841"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-26T10:34:47.771190+00:00_

Now I have all the information needed. Let me compile the verification results.

### [seddik_synthetic_data] — How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse (2024)
- **Exists**: ✓
- **Authors**: ✓ — Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah confirmed
- **Year**: ✓ — 2024
- **Title**: ✓
- **Venue**: ✓ — COLM 2024 confirmed (Conference on Language Modeling, University of Pennsylvania, Oct 7-9 2024)
- **Notes**: All fields correct.

### [qlora] — QLoRA: Efficient Finetuning of Quantized LLMs (2023)
- **Exists**: ✓
- **Authors**: ✓ — Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer confirmed
- **Year**: ✓ — 2023
- **Title**: ✓
- **Venue**: ✓ — NeurIPS 2023 confirmed (proceedings.neurips.cc)
- **Notes**: All fields correct.

### [dsir] — Data Selection for Language Models via Importance Resampling (2023)
- **Exists**: ✓
- **Authors**: ✓ — Sang Michael Xie, Shibani Santurkar, Tengyu Ma, Percy Liang confirmed
- **Year**: ✓ — 2023
- **Title**: ✓
- **Venue**: ✓ — NeurIPS 2023 confirmed
- **Notes**: All fields correct.

### [qurating] — QuRating: Selecting High-Quality Data for Training Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ — Alexander Wettig, Aatmik Gupta, Saumya Malik, Danqi Chen confirmed
- **Year**: ✓ — 2024
- **Title**: ✓
- **Venue**: ✓ — ICML 2024 confirmed (proceedings.mlr.press/v235/wettig24a)
- **Notes**: All fields correct.

### [ccnet] — CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (2020)
- **Exists**: ✓
- **Authors**: ✓ — Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzman, Armand Joulin, Edouard Grave confirmed
- **Year**: ✓ — 2020
- **Title**: ✓
- **Venue**: ✓ — LREC 2020 confirmed (aclanthology.org/2020.lrec-1.494)
- **Notes**: All fields correct.

### [watermark_llm] — A Watermark for Large Language Models (2023)
- **Exists**: ✓
- **Authors**: ✓ — John Kirchenbauer, Jonas Geipi
…[truncated 4640 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-26T10:34:47.771413+00:00_

The TMLR accepted version has the longer title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" — which matches the bib entry. Now I have all the information I need. Let me compile the results.

Here are the verification results for all 12 bibliography entries:

---

### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)
- **Exists**: ✓
- **Authors**: ✓ (Jacob Cohen)
- **Year**: ✓ (1988, 2nd edition)
- **Title**: ✓
- **Venue**: ✓ (Lawrence Erlbaum Associates, 2nd edition)
- **Notes**: Classic reference book. No issues found.

### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)
- **Exists**: ✓
- **Authors**: ✓ (Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (ICML 2023, PMLR 202:24950-24962)
- **Notes**: No issues found.

### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)
- **Exists**: ✓
- **Authors**: ✓ (Sebastian Gehrmann, Hendrik Strobelt, Alexander M. Rush)
- **Year**: ✓ (2019)
- **Title**: ✓
- **Venue**: ✓ (ACL 2019, System Demonstrations, pages 111-116)
- **Notes**: No issues found.

### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Xianjun Yang, Wei Cheng, Yue Wu, Linda Petzold, William Yang Wang, Haifeng Chen)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICLR 2024)
- **Notes**: No issues found.

### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)
- **Exists**: ✓
- **Authors**: ✓ (Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, Tom Goldstein)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ICML 2024, PMLR 235)
- **Notes**: No issues found.

### [fast_detectgpt] — Fast-DetectGPT: E
…[truncated 4557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 33
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-26T10:34:47.771586+00:00_

Web search results for query: "Li Yafu "Human Texts Are Outliers" "Rethinking" machine-generated text detection OOD arXiv 2025"

Links: [{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/html/2510.08602v1"},{"title":"[2510.08602] Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/abs/2510.08602"},{"title":"(PDF) Human Texts Are Outliers: Detecting LLM-generated ...","url":"https://arxiv.org/pdf/2510.08602"},{"title":"MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/html/2305.13242v3"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v2"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large Language Models","url":"https://arxiv.org/html/2412.05139v4"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://www.nec-labs.com/blog/human-texts-are-outliers-detecting-llm-generated-texts-via-out-of-distribution-detection/"}]

I found the paper you were searching for! Here's what I found:

The paper proposes reframing the detection task as an out-of-distribution (OOD) detection problem, treating human-written texts as distributional outliers while machine-generated texts are in-distribution (ID) samples. 

The authors argue that binary formulation fundamentally mischaracterizes the detection task by assuming a coherent representation of human-written texts, noting that in reality human texts do not constitute a unified distribution, and their diversity cannot be effectively captured through limited sampling.

The researchers developed a detection framework using one-class learning methods including DeepSVDD and HRN, and score-based learning techniques such as energy-based methods. The OOD-based method achieves 98.3% AUROC and AUPR with only 8.9% FPR95 on the De
…[truncated 395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-26T10:34:47.771747+00:00_

Web search results for query: "OLMo ACL 2024 full author list aclanthology.org/2024.acl-long.841"

Links: [{"title":"OLMo: Accelerating the Science of Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.841/"},{"title":"OLMo : Accelerating the Science of Language Models","url":"https://aclanthology.org/2024.acl-long.841.pdf"},{"title":"Allen School News » A way with words and trillions of tokens: Allen School researchers recognized at ACL 2024 for expanding the capabilities of language models","url":"https://news.cs.washington.edu/2024/10/08/a-way-with-words-and-trillions-of-tokens-allen-school-researchers-recognized-at-acl-2024-for-expanding-the-capabilities-of-language-models/"},{"title":"Findings of the Association for Computational Linguistics: ACL 2024 - ACL Anthology","url":"https://aclanthology.org/volumes/2024.findings-acl/"},{"title":"ACL 2024 The 62nd Annual Meeting of the Association for","url":"https://aclanthology.org/2024.acl-short.0.pdf"},{"title":"Document-Level Machine Translation with Large-Scale Public Parallel Corpora - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.712/"},{"title":"Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2024.acl-long/"},{"title":"dblp: ACL","url":"https://dblp.org/db/conf/acl/index.html"}]

Based on the search results, I found the full author list for the OLMo paper from ACL 2024 (paper ID: 2024.acl-long.841):

The authors are: Dirk Groeneveld, Iz Beltagy, Evan Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, Shane Arora, David Atkinson, Russell Authur, Khyathi Chandu, Arman Cohan, Jennifer Dumas, Yanai Elazar, Yuling Gu, Jack Hessel, Tushar Khot, William Merrill, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew Peters, Valentina Pyatkin, Abhilasha Ravichander, Dustin Schwenk, 
…[truncated 325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-26T10:34:47.771902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\" Li Yafu Hu Zhilin Guo Zetian arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\" Li Yafu Hu Zhilin Guo Zetian arXiv"
  }
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-26T10:34:47.772033+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.09388 Qwen3 Technical Report authors \"Qwen Team\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.09388 Qwen3 Technical Report authors \"Qwen Team\""
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-26T10:34:47.772157+00:00_

Web search results for query: ""Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective" Li Yafu Hu Zhilin Guo Zetian arXiv"

Links: [{"title":"MAGE: Machine-generated Text Detection in the Wild","url":"https://arxiv.org/html/2305.13242v3"},{"title":"[PDF] MAGE: Machine-generated Text Detection in the Wild | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAGE:-Machine-generated-Text-Detection-in-the-Wild-Li-Li/435f070f4779a184285917184899fbdb43bb6d7e"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654v1"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/pdf/2509.18880"},{"title":"[2111.02878] Unsupervised and Distributional Detection of Machine-Generated Text","url":"https://arxiv.org/abs/2111.02878"},{"title":"Exploring the Limitations of Detecting Machine-Generated Text","url":"https://arxiv.org/html/2406.11073v2"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large Language Models","url":"https://arxiv.org/html/2412.05139v4"},{"title":"Advancing Machine-Generated Text Detection from an Easy to Hard Supervision Perspective","url":"https://arxiv.org/html/2511.00988"},{"title":"Authorship Obfuscation in Multilingual Machine-Generated Text Detection","url":"https://arxiv.org/html/2401.07867v2"}]

The search results show several papers on machine-generated text detection, but I didn't find the specific paper with the exact title "Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective" by Li Yafu, Hu Zhilin, and Guo Zetian. 

However, I did find a highly relevant paper by some of these authors: MAGE: Machine-generated Text Detection in the Wild by Yafu Li, Qintong Li, Leyang Cui, Wei Bi, Zhilin Wang, Longyue Wang, Linyi Yang, Shuming Shi, and Yue Zhang. This paper builds a comprehensive testbed by gathering texts from diverse human writings and texts generated by different LLM
…[truncated 575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-26T10:34:47.772302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.08602 authors Cong Zeng \"Human Texts Are Outliers\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.08602 authors Cong Zeng \"Human Texts Are Outliers\""
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T10:34:47.772421+00:00_

Web search results for query: "arxiv 2505.09388 Qwen3 Technical Report authors "Qwen Team""

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388.pdf"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"Qwen3 Technical Report | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.09388v1"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Qwen/Qwen3-VL-8B-Thinking - Demo - DeepInfra","url":"https://deepinfra.com/Qwen/Qwen3-VL-8B-Thinking"}]

I found the paper you're looking for! Here are the key details:

**Paper:** Qwen3 Technical Report

**ArXiv ID:** 2505.09388

**Authors:** An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu, Jianwei Zhang and 38 additional authors

**Organization:** Qwen Team

**Publication Date:** May 14, 2025

**Overview:** Qwen3 is the latest version of the Qwen model family comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities, including models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-26T10:34:47.772565+00:00_

Web search results for query: "arxiv 2510.08602 authors Cong Zeng "Human Texts Are Outliers""

Links: [{"title":"[2510.08602] Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/abs/2510.08602"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://arxiv.org/html/2510.08602"},{"title":"(PDF) Human Texts Are Outliers: Detecting LLM-generated ...","url":"https://arxiv.org/pdf/2510.08602"},{"title":"GitHub - cong-zeng/ood-llm-detect · GitHub","url":"https://github.com/cong-zeng/ood-llm-detect"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://www.nec-labs.com/blog/human-texts-are-outliers-detecting-llm-generated-texts-via-out-of-distribution-detection/"},{"title":"On the Detectability of LLM-Generated Text: What Exactly Is LLM-Generated Text?","url":"https://arxiv.org/html/2510.20810v1"},{"title":"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection | OpenReview","url":"https://openreview.net/forum?id=0XKZFK4hQt"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3575&show=2000"},{"title":"NeurIPS Poster Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120309"}]

I found the paper! Here's what the search revealed:

## Paper Details

**Title:** "Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection"

**ArXiv ID:** 2510.08602

**Submitted:** October 7, 2025

## Authors

The authors are: Cong Zeng (Mohamed bin Zayed University of Artificial Intelligence), Shengkun Tang (Mohamed bin Zayed University of Artificial Intelligence), Yuanzhou Chen (University of California, Los Angeles), Zhiqiang Shen (Mohamed bin Zayed University of Artificial Intelligence), Wenchao Yu (NEC Laborat
…[truncated 928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-26T10:34:47.772736+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "xu_spectrum_detection \"Detecting Subtle Differences\" EMNLP 2024 authors Yang Xu Yu Wang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "tool_args": {
    "query": "xu_spectrum_detection \"Detecting Subtle Differences\" EMNLP 2024 authors Yang Xu Yu Wang"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-26T10:34:47.772871+00:00_

Web search results for query: "xu_spectrum_detection "Detecting Subtle Differences" EMNLP 2024 authors Yang Xu Yu Wang"

Links: [{"title":"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.564/"},{"title":"[2406.19874] Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood","url":"https://arxiv.org/abs/2406.19874"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=9390&show=1000"},{"title":"Detecting Subtle Differences between Human and Model ...","url":"https://aclanthology.org/2024.emnlp-main.564.pdf"},{"title":"(PDF) Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood","url":"https://www.researchgate.net/publication/381851117_Detecting_Subtle_Differences_between_Human_and_Model_Languages_Using_Spectrum_of_Relative_Likelihood"},{"title":"Detecting Subtle Differences between Human and Model Languages Using   Spectrum of Relative Likelihood","url":"https://arxiv.org/pdf/2406.19874"}]

Based on the search results, I found the paper you're looking for:

"Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood" was published at EMNLP 2024 by Yang Xu, Yu Wang, Hao An, Zhichen Liu, and Yongyuan Li.

The paper appears in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 10108–10121, Miami, Florida, USA.

The study provides a new perspective by using relative likelihood values instead of absolute ones, and extracting useful features from the spectrum-view of likelihood for the human-model text detection task. The authors propose a detection procedure with two classification methods, supervised and heuristic-based, respectively, which results in competitive performances with previous zero-shot detection methods and a new state-of-the-art on sh
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-26T10:34:47.773119+00:00_

Now I have all the information needed. Let me compile the verification results.

Here are the verification results for all 13 bibliography entries:

---

### [pythia] — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (2023)
- **Exists**: ✓
- **Authors**: ✓ (Biderman, Schoelkopf, Anthony, Bradley, O'Brien, Hallahan, Khan, Purohit, Prashanth, Raff, Skowron, Sutawika, van der Wal — the middle name "Gregory" for Quentin Anthony is present on arXiv but DBLP uses full name; acceptable either way)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (ICML 2023, Proceedings of the 40th ICML)
- **Notes**: All clean.

---

### [olmo] — OLMo: Accelerating the Science of Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (The long author list matches the ACL Anthology entry. Minor note: "Ananya Harsh Jha" in bib vs "Ananya Jha" in some listings — the full name on the paper itself includes "Harsh", so the bib is correct.)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ACL 2024, won Best Theme Paper)
- **Notes**: All clean.

---

### [qwen3] — Qwen3 Technical Report (2025)
- **Exists**: ✓
- **Authors**: ✓ (Listed as "Qwen Team" which is acceptable; the actual arXiv paper lists 60+ individual authors under the Qwen Team umbrella)
- **Year**: ✓ (2025, submitted May 14, 2025)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:2505.09388)
- **Notes**: All clean.

---

### [ghostbuster] — Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Vivek Verma, Eve Fleisig, Nicholas Tomlin, Dan Klein)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (NAACL 2024, pages 1702-1717)
- **Notes**: All clean.

---

### [two_birds] — Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text (2025)
- **Exists**: ✓
- **Authors**: ✓ (Zixin Rao, Youssef Mohamed, Shang Liu, Zeyan Liu)
- **Year**: ✓ (2025, submitted August 19, 2025)
- **Title**: ✓
- **Venue**: ✓ (arXiv preprint arXiv:
…[truncated 4863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-26T10:34:47.773349+00:00_

Now I have all the information needed. Let me compile the results.

Here are the verification results for all 12 bibliography entries:

---

### [lakens_equivalence] — Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (2017)
- **Exists**: ✓
- **Authors**: ✓ (Lakens, Daniel)
- **Year**: ✓ (2017)
- **Title**: ✓
- **Venue**: ✓ (Social Psychological and Personality Science, volume 8, number 4, pages 355-362)
- **Notes**: All metadata correct.

---

### [llama3] — The Llama 3 Herd of Models (2024)
- **Exists**: ✓
- **Authors**: ✓ (Grattafiori, Dubey, et al. — first author is Aaron Grattafiori as listed)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (arXiv:2407.21783)
- **Notes**: All metadata correct.

---

### [mistral7b] — Mistral 7B (2023)
- **Exists**: ✓
- **Authors**: ✓ (Jiang, Sablayrolles, Mensch, Bamford, Chaplot, de las Casas, Bressand, Lengyel, Lample, Saulnier, et al.)
- **Year**: ✓ (2023)
- **Title**: ✓
- **Venue**: ✓ (arXiv:2310.06825)
- **Notes**: All metadata correct.

---

### [strobl_conditional_2008] — Conditional Variable Importance for Random Forests (2008)
- **Exists**: ✓
- **Authors**: ✓ (Strobl, Boulesteix, Kneib, Augustin, Zeileis)
- **Year**: ✓ (2008)
- **Title**: ✓
- **Venue**: ✓ (BMC Bioinformatics, volume 9, pages 307)
- **Notes**: All metadata correct.

---

### [dolma] — Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (2024)
- **Exists**: ✓
- **Authors**: ✓ (Soldaini, Kinney, Bhagia, et al.)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (ACL 2024, pages 15725-15788)
- **Notes**: All metadata correct.

---

### [fineweb] — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (2024)
- **Exists**: ✓
- **Authors**: ✓ (Penedo, Kydlicek, Ben Allal, Lozhkov, Mitchell, Raffel, Von Werra, Wolf)
- **Year**: ✓ (2024)
- **Title**: ✓
- **Venue**: ✓ (NeurIPS 2024 Datasets and Benchmarks Track)
- **Notes**: All metadata correct.

---

### [mapping_llm_sci
…[truncated 4121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-26T10:34:47.773557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-26T10:34:47.773748+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1 An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions, and which properties change versus which are preserved, is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	\looseness=-1 Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+) and decompose this compression into structurally distinct components.
10	Across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency---mean entropy (per-token NLL under a fixed reference model, not information-theoretic entropy; \S\ref{sec:featur
…[truncated 3862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-26T10:34:47.773901+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": "0",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "head_limit": "0",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-26T10:34:47.774069+00:00_

artifacts/_project/paper/related_work.tex:5:\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.
artifacts/_project/paper/related_work.tex:6:Recent work moves beyond binary detection---multi-generator attribution \cite{semeval2024_task8}, collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}.
artifacts/_project/paper/related_work.tex:7:Recent work reframes detection as an out-of-distribution problem \cite{human_texts_outliers}; depth profiling differs in targeting ordinal depth rather than binary membership, with cross-generator transfer as the evaluation axis.
artifacts/_project/paper/related_work.tex:8:We introduce ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal} as a complementary task; repurposing existing detection scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.54--0.71; Table~\ref{tab:baselines}).
artifacts/_project/paper/related_work.tex:11:\looseness=-1 Self-consuming generative models lose distributional coverage via training-loop parameter updates \cite{self_consuming_mad,curse_of_recursion,strong_model_collapse,dohmatob_tale_of_tails,schaeffer_collapse_position}; we instead examine \emph{inference chains} where parameters are fixed.
artifacts/_project/paper/related_work.tex:12:Concurrent iterative-generation studies document complementary phenomena: paraphrasing chains show factuality degradation \cite{broken_telephone}, Markovian analysis bounds distinguishable depth to ${\sim}$3 classes \cite{markovian_chains}, and attractor cycle evidence emerges \cite{attractor_cycles}.
artifacts/_project/paper/related_work.tex:16:\looseness=-1 Dec
…[truncated 6700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-26T10:34:47.774287+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find uncited bib entries",
  "subagent_type": "Explore",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/, search all .tex files for citations of these specific bib keys. For each key, grep for it in all .tex files and report which ones have ZERO matches (i.e., are never cited):\n\nKeys to check: gltr, feat_aug_transformer, detection_possibilities, paraphrase_evades, intrinsic_dim_detection, seqxgpt, grover, release_strategies, model_collapse_avoidable, seddik_synthetic_data, qurating, aaronson_watermark, nucleus_sampling, welleck_unlikelihood, koppel_authorship, uchendu_attribution, munir_looking_glass, briesch_self_consuming, jawahar_survey, beyond_final_actor, diaz_soft_labels_ordinal, kasa_ordinality_nlp, strobl_conditional_2008, raid, mauve\n\nFor each key, just report: CITED or UNCITED, and if cited, which file.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "tool_args": {
    "description": "Find uncited bib entries",
    "subagent_type": "Explore",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/, search all .tex files for citations of these specific bib keys. For each key, grep for it in all .tex files and report which ones have ZERO matches (i.e., are never cited):\n\nKeys to check: gltr, feat_aug_transformer, detection_possibilities, paraphrase_evades, intrinsic_dim_detection, seqxgpt, grover, release_strategies, model_collapse_avoidable, seddik_synthetic_data, qurating, aaronson_watermark, nucleus_sampling, welleck_unlikelihood, koppel_authorship, uchendu_attribution, munir_looking_glass, briesch_self_consuming, jawahar_survey, beyond_final_actor, diaz_soft_labels_ordinal, kasa_ordinality_nlp, strobl_conditional_2008, raid, mauve\n\nFor each key, just report: CITED or UNCITED, and if cited, which file.\n"
  }
}
```

</details>

---

### Tool call

_source line 262 · 2026-05-26T10:34:47.774446+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-26T10:34:47.774588+00:00_

artifacts/_project/paper/appendix_ablation.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_cross_model_detail.tex
artifacts/_project/paper/appendix_cross_temp.tex
artifacts/_project/paper/appendix_dataset_stats.tex
artifacts/_project/paper/appendix_downstream.tex
artifacts/_project/paper/appendix_feature_correlation.tex
artifacts/_project/paper/appendix_generator_subsets.tex
artifacts/_project/paper/appendix_human_edit.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/appendix_qualitative_examples.tex
artifacts/_project/paper/appendix_temperature_stability.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table2.tex
artifacts/_project/paper/appendix_feature_distributions.tex
artifacts/_project/paper/per_family_cohens_d_table.tex
artifacts/_project/paper/per_family_ddr_table.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/appendix_ai_assistants.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/appendix_ddr_validation.tex
artifacts/_project/paper/appendix_iterative_comparison.tex
artifacts/_project/paper/appendix_qlora.tex
artifacts/_project/paper/appendix_feature_candidates.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/appendix_variance_decomposition.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/appendix_error_analysis.tex
artifacts/_project/paper/appendix_nll_distribution.tex
artifacts/_project/paper/appendix_9gen_scale.tex
artifacts/_project/paper/appendix_ddr_causality.tex
artifacts/_project/paper/appendix_convergence.tex
artifacts/_project/paper/appendix_instruct.tex
artifacts/_project/paper/appendix_seed_control.tex
artifacts/_project/paper/appendix_transfer.tex
artifacts/_project/paper/appendix_tost.tex
artifacts/_project/paper/appendix_tost_bootstrap.tex
artifacts/_project/paper/appendix_domain.tex
artifacts/_project/paper/appendix_finer_depth.tex
…[truncated 413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-26T10:34:47.774737+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gltr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gltr",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-26T10:34:47.774849+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-26T10:34:47.774972+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "feat_aug_transformer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "feat_aug_transformer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-26T10:34:47.775082+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-26T10:34:47.775195+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "detection_possibilities",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "detection_possibilities",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 269 · 2026-05-26T10:34:47.775301+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 270 · 2026-05-26T10:34:47.775413+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paraphrase_evades",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paraphrase_evades",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 271 · 2026-05-26T10:34:47.775517+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 272 · 2026-05-26T10:34:47.775648+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "intrinsic_dim_detection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "intrinsic_dim_detection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 273 · 2026-05-26T10:34:47.775755+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-26T10:34:47.775865+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seqxgpt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seqxgpt",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 275 · 2026-05-26T10:34:47.775967+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-26T10:34:47.776075+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "grover",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "grover",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-26T10:34:47.776176+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 278 · 2026-05-26T10:34:47.776285+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "release_strategies",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "release_strategies",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-26T10:34:47.776388+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 280 · 2026-05-26T10:34:47.776496+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model_collapse_avoidable",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model_collapse_avoidable",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-26T10:34:47.776621+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-26T10:34:47.776737+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seddik_synthetic_data",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seddik_synthetic_data",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-26T10:34:47.776840+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-26T10:34:47.776959+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "qurating",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "qurating",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-26T10:34:47.777065+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-26T10:34:47.777173+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "aaronson_watermark",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "aaronson_watermark",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 287 · 2026-05-26T10:34:47.777276+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 288 · 2026-05-26T10:34:47.777384+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "nucleus_sampling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "nucleus_sampling",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-26T10:34:47.777484+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 290 · 2026-05-26T10:34:47.777607+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "welleck_unlikelihood",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "welleck_unlikelihood",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-26T10:34:47.777716+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-26T10:34:47.777825+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "koppel_authorship",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "koppel_authorship",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-26T10:34:47.777927+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-26T10:34:47.778035+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "uchendu_attribution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "uchendu_attribution",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-26T10:34:47.778136+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 296 · 2026-05-26T10:34:47.778250+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "munir_looking_glass",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "munir_looking_glass",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-26T10:34:47.778352+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 298 · 2026-05-26T10:34:47.778459+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "briesch_self_consuming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "briesch_self_consuming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 299 · 2026-05-26T10:34:47.778560+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 300 · 2026-05-26T10:34:47.778690+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jawahar_survey",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jawahar_survey",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 301 · 2026-05-26T10:34:47.778792+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 302 · 2026-05-26T10:34:47.778901+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "beyond_final_actor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "beyond_final_actor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 303 · 2026-05-26T10:34:47.779003+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 304 · 2026-05-26T10:34:47.779110+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "diaz_soft_labels_ordinal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "diaz_soft_labels_ordinal",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 305 · 2026-05-26T10:34:47.779212+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 306 · 2026-05-26T10:34:47.779319+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "kasa_ordinality_nlp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "kasa_ordinality_nlp",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 307 · 2026-05-26T10:34:47.779420+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 308 · 2026-05-26T10:34:47.779528+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "strobl_conditional_2008",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "strobl_conditional_2008",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 309 · 2026-05-26T10:34:47.779649+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 310 · 2026-05-26T10:34:47.779759+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "raid",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "raid",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 311 · 2026-05-26T10:34:47.779871+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 312 · 2026-05-26T10:34:47.779983+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "mauve",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "mauve",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 313 · 2026-05-26T10:34:47.780083+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 314 · 2026-05-26T10:34:47.780191+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 315 · 2026-05-26T10:34:47.780322+00:00_

1	% ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{placeins}
15	\usepackage{multirow}
16	\usepackage{float}
17	\usepackage{stfloats}
18	\usepackage{alphalph}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{breakable}
21	
22	\graphicspath{{../chart/}}
23	
24	\title{Depth Profiling: Classifying Recursive Generation Depth\\in Base-Model LLM Text}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{results}
37	
38	\input{discussion}
39	\input{conclusion}
40	\input{limitations}
41	\input{ethics}
42	\bibliography{references}
43	
44	\appendix
45	\renewcommand{\thesection}{\alphalph{\value{section}}}
46	
47	\noindent\textbf{Note:} Unless otherwise stated, appendix experiments use the original six-generator subset (Pythia-2.8B/1B, OLMo-2-1B, Qwen3-1.7B/0.6B/8B).
48	Main paper results (\S\ref{sec:results}) use the full eight-generator set (adding Llama-3.2-3B and Mistral-7B-v0.3).
49	
50	\input{appendix_dataset_stats}
51	
52	\section{Length Confound Analysis}
53	\label{app:length}
54	\input{appendix_length}
55	
56	\section{Prompt Type Generalization}
57	\label{app:prompt-type}
58	\input{appendix_prompt_type}
59	\FloatBarrier
60	
61	\section{Finer-Grained Depth Classification}
62	\label{app:finer-depth}
63	\input{appendix_finer_depth}
64	\FloatBarrier
65	
66	\section{End-to-End Depth Classification (QLoRA)}
67	\label{app:qlora}
68	\input{appendix_qlora}
69	\FloatBarrier
70	
71	\section{Leave-One-Feature-Out Analysis}
72	\label{app:lofo}
73	\input{appendix_lofo}
74	\FloatBarrier
75	
76	\subsection{Candidate Feature Screening}
77	\label{app:feature-candidate}
78	\input{appendix_fe
…[truncated 3254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 316 · 2026-05-26T10:34:47.780457+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/related_work.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 317 · 2026-05-26T10:34:47.780593+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{AI-generated text detection.}
5	\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.
6	Recent work moves beyond binary detection---multi-generator attribution \cite{semeval2024_task8}, collaboration roles \cite{beyond_binary}, joint detection-attribution \cite{two_birds}---but all taxonomize by \emph{source} or \emph{production mode}, not recursive generation \emph{depth}.
7	Recent work reframes detection as an out-of-distribution problem \cite{human_texts_outliers}; depth profiling differs in targeting ordinal depth rather than binary membership, with cross-generator transfer as the evaluation axis.
8	We introduce ordinal depth classification \cite{gutierrez_ordinal_survey,coral_ordinal} as a complementary task; repurposing existing detection scores as depth predictors reveals high cross-generator variance (binary F1\,=\,0.54--0.71; Table~\ref{tab:baselines}).
9	
10	\paragraph{Model collapse and iterative generation.}
11	\looseness=-1 Self-consuming generative models lose distributional coverage via training-loop parameter updates \cite{self_consuming_mad,curse_of_recursion,strong_model_collapse,dohmatob_tale_of_tails,schaeffer_collapse_position}; we instead examine \emph{inference chains} where parameters are fixed.
12	Concurrent iterative-generation studies document complementary phenomena: paraphrasing chains show factuality degradation \cite{broken_telephone}, Markovian analysis bounds distinguishable depth to ${\sim}$3 classes \cite{markovian_chains}, and attractor cycle evidence emerges \cite{attractor_cycles}.
13	DDR differs in chain type (non-paraphrastic continuation), analysis lens (location/shape decomposition identifying what is \emph{preserved}), and downstream ut
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 318 · 2026-05-26T10:34:47.780743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 319 · 2026-05-26T10:34:47.780870+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1 An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions, and which properties change versus which are preserved, is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
5	Base models provide the cleanest substrate to isolate depth effects from alignment-induced changes.
6	We find that recursive generation produces a decomposable depth profile: distributional \emph{location} drifts with depth while \emph{shape} remains stable across generators, an asymmetry sufficient for cross-generator depth prediction.
7	
8	\looseness=-1 Distributional compression under recursive generation is well-documented \cite{curious_decline,broken_telephone,markovian_chains}, yet existing analyses characterize \emph{that} and \emph{why} convergence occurs without decomposing what drifts from what is preserved.
9	We introduce \emph{depth profiling} (coarse ordinal classification into gen-0\,/\,gen-1\,/\,gen-2+) and decompose this compression into structurally distinct components.
10	Across eight base-model generators spanning five architectural families (0.6B--8B), the NLL distribution's central tendency---mean entropy (per-token NLL under a fixed reference model, not information-theoretic entropy; \S\ref{sec:featur
…[truncated 3862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 320 · 2026-05-26T10:34:47.781043+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*gltr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*gltr",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 321 · 2026-05-26T10:34:47.781155+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 322 · 2026-05-26T10:34:47.781272+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*feat_aug_transformer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*feat_aug_transformer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 323 · 2026-05-26T10:34:47.781380+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 324 · 2026-05-26T10:34:47.781496+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*detection_possibilities",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*detection_possibilities",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 325 · 2026-05-26T10:34:47.781620+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 326 · 2026-05-26T10:34:47.781740+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*paraphrase_evades",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*paraphrase_evades",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 327 · 2026-05-26T10:34:47.781848+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 328 · 2026-05-26T10:34:47.781962+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*intrinsic_dim_detection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*intrinsic_dim_detection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 329 · 2026-05-26T10:34:47.782066+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 330 · 2026-05-26T10:34:47.782189+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*seqxgpt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*seqxgpt",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 331 · 2026-05-26T10:34:47.782292+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 332 · 2026-05-26T10:34:47.782401+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*grover",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*grover",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 333 · 2026-05-26T10:34:47.782501+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 334 · 2026-05-26T10:34:47.782636+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*release_strategies",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*release_strategies",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 335 · 2026-05-26T10:34:47.782745+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 336 · 2026-05-26T10:34:47.782855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*model_collapse_avoidable",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*model_collapse_avoidable",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 337 · 2026-05-26T10:34:47.782958+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 338 · 2026-05-26T10:34:47.783068+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*seddik_synthetic_data",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*seddik_synthetic_data",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 339 · 2026-05-26T10:34:47.783169+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 340 · 2026-05-26T10:34:47.783277+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*qurating",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*qurating",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 341 · 2026-05-26T10:34:47.783378+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 342 · 2026-05-26T10:34:47.783487+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite\\{.*aaronson_watermark",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite\\{.*aaronson_watermark",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 343 · 2026-05-26T10:34:47.783603+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 344 · 2026-05-26T10:34:47.783718+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "gltr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "gltr",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 345 · 2026-05-26T10:34:47.783821+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 346 · 2026-05-26T10:34:47.783931+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "feat_aug_transformer",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "feat_aug_transformer",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 347 · 2026-05-26T10:34:47.784033+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 348 · 2026-05-26T10:34:47.784140+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "detection_possibilities",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "detection_possibilities",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 349 · 2026-05-26T10:34:47.784247+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 350 · 2026-05-26T10:34:47.784358+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "paraphrase_evades",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "paraphrase_evades",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 351 · 2026-05-26T10:34:47.784460+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 352 · 2026-05-26T10:34:47.784568+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "intrinsic_dim_detection",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "intrinsic_dim_detection",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 353 · 2026-05-26T10:34:47.784715+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 354 · 2026-05-26T10:34:47.784830+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seqxgpt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seqxgpt",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 355 · 2026-05-26T10:34:47.784945+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 356 · 2026-05-26T10:34:47.785058+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "grover",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "grover",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 357 · 2026-05-26T10:34:47.785161+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 358 · 2026-05-26T10:34:47.785272+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "release_strategies",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "release_strategies",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 359 · 2026-05-26T10:34:47.785375+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 360 · 2026-05-26T10:34:47.785484+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model_collapse_avoidable",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model_collapse_avoidable",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 361 · 2026-05-26T10:34:47.785603+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 362 · 2026-05-26T10:34:47.785719+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "seddik_synthetic_data",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "seddik_synthetic_data",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 363 · 2026-05-26T10:34:47.785827+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 364 · 2026-05-26T10:34:47.785938+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "qurating",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "qurating",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 365 · 2026-05-26T10:34:47.786039+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 366 · 2026-05-26T10:34:47.786147+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "aaronson_watermark",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "aaronson_watermark",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 367 · 2026-05-26T10:34:47.786249+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 368 · 2026-05-26T10:34:47.786359+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "nucleus_sampling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "nucleus_sampling",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 369 · 2026-05-26T10:34:47.786460+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 370 · 2026-05-26T10:34:47.786568+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "welleck_unlikelihood",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "welleck_unlikelihood",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 371 · 2026-05-26T10:34:47.786690+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 372 · 2026-05-26T10:34:47.786799+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "koppel_authorship",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "koppel_authorship",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 373 · 2026-05-26T10:34:47.786901+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 374 · 2026-05-26T10:34:47.787010+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "uchendu_attribution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "uchendu_attribution",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 375 · 2026-05-26T10:34:47.787109+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 376 · 2026-05-26T10:34:47.787216+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "munir_looking_glass",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "munir_looking_glass",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 377 · 2026-05-26T10:34:47.787322+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 378 · 2026-05-26T10:34:47.787433+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "briesch_self_consuming",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "briesch_self_consuming",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 379 · 2026-05-26T10:34:47.787535+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 380 · 2026-05-26T10:34:47.787664+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "jawahar_survey",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "jawahar_survey",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 381 · 2026-05-26T10:34:47.787767+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 382 · 2026-05-26T10:34:47.787876+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "beyond_final_actor",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "beyond_final_actor",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 383 · 2026-05-26T10:34:47.787976+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 384 · 2026-05-26T10:34:47.788083+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "diaz_soft_labels_ordinal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "diaz_soft_labels_ordinal",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 385 · 2026-05-26T10:34:47.788191+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 386 · 2026-05-26T10:34:47.788300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "kasa_ordinality_nlp",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "kasa_ordinality_nlp",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 387 · 2026-05-26T10:34:47.788400+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 388 · 2026-05-26T10:34:47.788508+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "strobl_conditional_2008",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "strobl_conditional_2008",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 389 · 2026-05-26T10:34:47.788626+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 390 · 2026-05-26T10:34:47.788739+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "raid",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "raid",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 391 · 2026-05-26T10:34:47.788847+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 392 · 2026-05-26T10:34:47.788973+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "mauve",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "**/*.tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "tool_args": {
    "pattern": "mauve",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
    "glob": "**/*.tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 393 · 2026-05-26T10:34:47.789076+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 394 · 2026-05-26T10:34:47.789189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -r \"detectgpt\" *.tex | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && grep -r \"detectgpt\" *.tex | head -5"
  }
}
```

</details>

---

### Tool result

_source line 395 · 2026-05-26T10:34:47.789298+00:00_

introduction.tex:\looseness=-1 An estimated 7--17\% of recent scientific publications already contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}. As these outputs re-enter training corpora \cite{dolma,fineweb} and seed further generation, text accumulates at varying \emph{generation depths}; each successive cycle reshapes distributional properties in ways that matter for data provenance, corpus auditing, and contamination monitoring in base-model pretraining corpora \cite{ccnet,dsir} as well as model collapse analysis \cite{curse_of_recursion,strong_model_collapse}. Understanding \emph{how} recursive generation alters text distributions, and which properties change versus which are preserved, is therefore a prerequisite for principled corpus curation, yet current methods address only binary human-or-machine detection \cite{detectgpt,fast_detectgpt,binoculars,ld_score}.
method.tex:We compare the 7-feature ensemble against four single-score detection methods repurposed as depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
related_work.tex:\looseness=-1 Detection methods span zero-shot scoring \cite{detectgpt,fast_detectgpt,binoculars,dna_gpt}, learned classifiers \cite{ghostbuster,ld_score,reliable_detection}, and surprisal-based approaches \cite{diveye,xu_spectrum_detection}; see \citet{wu_survey_2025} for a survey.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 396 · 2026-05-26T10:34:47.789426+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && for key in gltr feat_aug_transformer detection_possibilities paraphrase_evades intrinsic_dim_detection seqxgpt grover release_strategies model_collapse_avoidable seddik_synthetic_data qurating aaronson_watermark nucleus_sampling welleck_unlikelihood koppel_authorship uchendu_attribution munir_looking_glass briesch_self_consuming jawahar_survey beyond_final_actor diaz_soft_labels_ordinal kasa_ordinality_nlp strobl_conditional_2008 raid mauve; do result=$(grep -r \"$key\" *.tex 2>/dev/null | head -1); if [ -z \"$result\" ]; then echo \"$key: UNCITED\"; else echo \"$key: CITED - $(grep -r \"$key\" *.tex 2>/dev/null | head -1 | cut -d: -f1)\"; fi; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && for key in gltr feat_aug_transformer detection_possibilities paraphrase_evades intrinsic_dim_detection seqxgpt grover release_strategies model_collapse_avoidable seddik_synthetic_data qurating aaronson_watermark nucleus_sampling welleck_unlikelihood koppel_authorship uchendu_attribution munir_looking_glass briesch_self_consuming jawahar_survey beyond_final_actor diaz_soft_labels_ordinal kasa_ordinality_nlp strobl_conditional_2008 raid mauve; do result=$(grep -r \"$key\" *.tex 2>/dev/null | head -1); if [ -z \"$result\" ]; then echo \"$key: UNCITED\"; else echo \"$key: CITED - $(grep -r \"$key\" *.tex 2>/dev/null | head -1 | cut -d: -f1)\"; fi; done"
  }
}
```

</details>

---

### Tool result

_source line 397 · 2026-05-26T10:34:47.789540+00:00_

gltr: UNCITED
feat_aug_transformer: UNCITED
detection_possibilities: UNCITED
paraphrase_evades: UNCITED
intrinsic_dim_detection: UNCITED
seqxgpt: UNCITED
grover: UNCITED
release_strategies: UNCITED
model_collapse_avoidable: UNCITED
seddik_synthetic_data: UNCITED
qurating: UNCITED
aaronson_watermark: UNCITED
nucleus_sampling: UNCITED
welleck_unlikelihood: UNCITED
koppel_authorship: UNCITED
uchendu_attribution: UNCITED
munir_looking_glass: UNCITED
briesch_self_consuming: UNCITED
jawahar_survey: UNCITED
beyond_final_actor: UNCITED
diaz_soft_labels_ordinal: UNCITED
kasa_ordinality_nlp: UNCITED
strobl_conditional_2008: UNCITED
raid: UNCITED
mauve: UNCITED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 398 · 2026-05-26T10:34:47.789687+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && echo \"=== Checking for 'gltr' ===\" && grep -r \"gltr\" *.tex 2>/dev/null | wc -l && echo \"=== Checking for 'mauve' ===\" && grep -r \"mauve\" *.tex 2>/dev/null | wc -l && echo \"=== Checking for 'raid' ===\" && grep -r \"raid\" *.tex 2>/dev/null | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && echo \"=== Checking for 'gltr' ===\" && grep -r \"gltr\" *.tex 2>/dev/null | wc -l && echo \"=== Checking for 'mauve' ===\" && grep -r \"mauve\" *.tex 2>/dev/null | wc -l && echo \"=== Checking for 'raid' ===\" && grep -r \"raid\" *.tex 2>/dev/null | wc -l"
  }
}
```

</details>

---

### Tool result

_source line 399 · 2026-05-26T10:34:47.789798+00:00_

=== Checking for 'gltr' ===
0
=== Checking for 'mauve' ===
0
=== Checking for 'raid' ===
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 400 · 2026-05-26T10:34:47.789933+00:00_

Perfect. Let me generate a comprehensive final report:

## Citation Search Results

I searched all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/` for the 25 specified bibliography keys. Here are the results:

**ALL 25 KEYS ARE UNCITED:**

1. gltr - UNCITED
2. feat_aug_transformer - UNCITED
3. detection_possibilities - UNCITED
4. paraphrase_evades - UNCITED
5. intrinsic_dim_detection - UNCITED
6. seqxgpt - UNCITED
7. grover - UNCITED
8. release_strategies - UNCITED
9. model_collapse_avoidable - UNCITED
10. seddik_synthetic_data - UNCITED
11. qurating - UNCITED
12. aaronson_watermark - UNCITED
13. nucleus_sampling - UNCITED
14. welleck_unlikelihood - UNCITED
15. koppel_authorship - UNCITED
16. uchendu_attribution - UNCITED
17. munir_looking_glass - UNCITED
18. briesch_self_consuming - UNCITED
19. jawahar_survey - UNCITED
20. beyond_final_actor - UNCITED
21. diaz_soft_labels_ordinal - UNCITED
22. kasa_ordinality_nlp - UNCITED
23. strobl_conditional_2008 - UNCITED
24. raid - UNCITED
25. mauve - UNCITED

None of these 25 bibliography keys appear anywhere in the 52 .tex files examined, indicating they are present in the bibliography file (references.bib) but not actually cited in any of the paper sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Agent",
  "elapsed_ms": 15
}
```

</details>

---

### Tool call

_source line 401 · 2026-05-26T10:34:47.790159+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ref_audit_worker1.md",
  "content": "# Reference Audit — Worker 1\n\n## Summary\n- Total entries: 74\n- Verified OK: 70\n- Issues found: 4 (1 critical, 2 venue errors, 1 unconfirmed venue)\n- Uncited entries (in bib but not in any tex): 25\n\n## Issues Overview\n\n| # | Key | Severity | Issue |\n|---|-----|----------|-------|\n| 1 | `human_texts_outliers` | **CRITICAL** | Authors and subtitle are hallucinated; arXiv ID maps to different paper |\n| 2 | `diveye` | **ERROR** | Venue is TMLR 2026, not ICLR 2026 |\n| 3 | `xu_spectrum_detection` | **WARNING** | Published at EMNLP 2024; still listed as arXiv preprint |\n| 4 | `beyond_final_actor` | **WARNING** | ACL 2026 venue could not be independently confirmed |\n\n## Entry-by-Entry Results\n\n### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)\n- **Exists**: ✓\n- **Authors**: ✓\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Lawrence Erlbaum Associates, 2nd edition)\n- **Cite usage**: ✓ (appendix_tost.tex: used as SESOI justification for Cohen's d=0.20)\n- **Notes**: Classic reference. No issues.\n\n### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Mitchell, Lee, Khazatsky, Manning, Finn)\n- **Year**: ✓ (ICML 2023)\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023, PMLR 202:24950-24962)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: cited as zero-shot detection method)\n- **Notes**: No issues.\n\n### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Gehrmann, Strobelt, Rush)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2019 System Demonstrations, pages 111-116)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Yang, Cheng, Wu, Petzold, Wang, Chen)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as zero-shot scoring method)\n- **Notes**: No issues.\n\n### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)\n- **Notes**: No issues.\n\n### [fast_detectgpt] — Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Bao, Zhao, Teng, Yang, Zhang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)\n- **Notes**: No issues.\n\n### [ld_score] — Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Narayanasamy, Agrawal, Faber, Alam)\n- **Year**: ✓ (2026, submitted May 3, 2026)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.01647)\n- **Cite usage**: ✓ (related_work.tex, method.tex: cited as learned classifier / baseline)\n- **Notes**: No issues.\n\n### [diveye] — Diversity Boosts AI-Generated Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Basani, Chen)\n- **Year**: ✓ (2026)\n- **Title**: ✓\n- **Venue**: **✗ — Listed as ICLR 2026 (`@inproceedings` with `booktitle = {Proceedings of the International Conference on Learning Representations}`), but actual venue is TMLR (Transactions on Machine Learning Research), published February 2026. GitHub repo (IBM/diveye) and arXiv PDF header both state \"[TMLR '26]\".**\n- **Cite usage**: ✓ (related_work.tex: cited as surprisal-based approach)\n- **Notes**: Must change entry type to `@article` with `journal = {Transactions on Machine Learning Research}` and `year = {2026}`.\n\n### [feat_aug_transformer] — Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Mady, Reschke, Schuller)\n- **Year**: ✓ (2026)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.03969)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [reliable_detection] — Can AI-Generated Text be Reliably Detected? (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Sadasivan, Kumar, Balasubramanian, Wang, Feizi)\n- **Year**: ✓ (accepted TMLR March 2025)\n- **Title**: ✓\n- **Venue**: ✓ (Transactions on Machine Learning Research)\n- **Cite usage**: ✓ (related_work.tex: cited as learned classifier)\n- **Notes**: No issues.\n\n### [paraphrase_evades] — Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Krishna, Song, Karpinska, Wieting, Iyyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [detection_possibilities] — Position: On the Possibilities of AI-Generated Text Detection (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Chakraborty, Bedi, Zhu, An, Manocha, Huang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235:6093-6115)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Li, Ren, Jiang, Zhang, Qiu)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EMNLP 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [grover] — Defending Against Neural Fake News (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2019)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Solaiman, Brundage, Clark, et al. — 15 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:1908.09203)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Cheng, Zhou, Jiang, Wang, Li)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACM Web Conference 2025 / WWW '25)\n- **Cite usage**: ✓ (related_work.tex: cited as collaboration role detection)\n- **Notes**: No issues.\n\n### [semeval2024_task8] — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Mansurov, Ivanov, et al. — 15 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (SemEval 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as multi-generator attribution)\n- **Notes**: No issues.\n\n### [self_consuming_mad] — Self-Consuming Generative Models Go MAD (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as model collapse reference)\n- **Notes**: No issues.\n\n### [curse_of_recursion] — AI models collapse when trained on recursively generated data (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Nature, volume 631, pages 755-759)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex: cited as model collapse, contrasted with DDR)\n- **Notes**: No issues.\n\n### [dohmatob_tale_of_tails] — A Tale of Tails: Model Collapse as a Change of Scaling Laws (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dohmatob, Feng, Yang, Charton, Kempe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024)\n- **Cite usage**: ✓ (related_work.tex: model collapse reference)\n- **Notes**: No issues.\n\n### [strong_model_collapse] — Strong Model Collapse (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Dohmatob, Feng, Subramonian, Kempe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2025)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex)\n- **Notes**: No issues.\n\n### [model_collapse_avoidable] — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Gerstgrasser, Schaeffer, Dey, et al. — 14 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [schaeffer_collapse_position] — Position: Model Collapse Does Not Mean What You Think (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Schaeffer, Kazdan, Arulandu, Koyejo)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2503.03150)\n- **Cite usage**: ✓ (related_work.tex: model collapse reference)\n- **Notes**: No issues.\n\n### [seddik_synthetic_data] — How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Seddik, Chen, Hayou, Youssef, Debbah)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [qlora] — QLoRA: Efficient Finetuning of Quantized LLMs (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Dettmers, Pagnoni, Holtzman, Zettlemoyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: ✓ (introduction.tex, appendix_qlora.tex: QLoRA classifier)\n- **Notes**: No issues.\n\n### [dsir] — Data Selection for Language Models via Importance Resampling (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Xie, Santurkar, Ma, Liang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation quality signal)\n- **Notes**: No issues.\n\n### [qurating] — QuRating: Selecting High-Quality Data for Training Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Wettig, Gupta, Malik, Chen)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [ccnet] — CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Wenzek, Lachaux, Conneau, Chaudhary, Guzman, Joulin, Grave)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (LREC 2020)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation reference)\n- **Notes**: No issues.\n\n### [watermark_llm] — A Watermark for Large Language Models (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023, PMLR 202:17061-17084)\n- **Cite usage**: ✓ (related_work.tex: watermarking reference)\n- **Notes**: No issues.\n\n### [synthid_text] — Scalable Watermarking for Identifying Large Language Model Outputs (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dathathri, See, Ghaisas, et al. — 24 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Nature, volume 634, pages 818-823)\n- **Cite usage**: ✓ (related_work.tex: watermarking reference)\n- **Notes**: No issues.\n\n### [aaronson_watermark] — Watermarking GPT Outputs (2022)\n- **Exists**: ✓\n- **Authors**: ✓ (Aaronson, Kirchner — conventional dual attribution used across literature)\n- **Year**: ✓ (November 2022)\n- **Title**: ✓ (conventional citation title; actual blog post titled differently but this is standard practice)\n- **Venue**: ✓ (Blog post, URL valid)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [chainwash] — Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Ameen, Islam, Mahmud, Hamid)\n- **Year**: ✓ (2026, submitted May 6)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.05503)\n- **Cite usage**: ✓ (related_work.tex: watermark degradation across multi-step chains)\n- **Notes**: No issues.\n\n### [curious_decline] — The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Guo, Shang, Vazirgiannis, Clavel)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Findings of NAACL 2024)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: lexical diversity decline)\n- **Notes**: No issues.\n\n### [writing_diversity] — Does Writing with Language Models Reduce Content Diversity? (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Padmakumar, He)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: lexical diversity decline)\n- **Notes**: No issues.\n\n### [nucleus_sampling] — The Curious Case of Neural Text Degeneration (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Holtzman, Buys, Du, Forbes, Choi)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [welleck_unlikelihood] — Neural Text Generation with Unlikelihood Training (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Welleck, Kulikov, Roller, Dinan, Cho, Weston)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [stamatatos_survey] — A Survey of Modern Authorship Attribution Methods (2009)\n- **Exists**: ✓\n- **Authors**: ✓ (Stamatatos)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (JASIST, vol. 60, no. 3, pp. 538-556)\n- **Cite usage**: ✓ (related_work.tex: classical stylometric features)\n- **Notes**: No issues.\n\n### [koppel_authorship] — Computational Methods in Authorship Attribution (2009)\n- **Exists**: ✓\n- **Authors**: ✓ (Koppel, Schler, Argamon)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (JASIST, vol. 60, no. 1, pp. 9-26)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [uchendu_attribution] — Authorship Attribution for Neural Text Generation (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Uchendu, Le, Shu, Lee)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EMNLP 2020, pages 8384-8395)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [munir_looking_glass] — Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models (2021)\n- **Exists**: ✓\n- **Authors**: ✓ (Munir, Batool, Shafiq, Srinivasan, Zaffar)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EACL 2021, pages 1811-1822)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [briesch_self_consuming] — Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Briesch, Sobania, Rothlauf)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2311.16822)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [broken_telephone] — LLM as a Broken Telephone: Iterative Generation Distorts Information (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Mohamed, Geng, Vazirgiannis, Shang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2025, Long Papers, pages 7493-7509)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex: iterative generation distortion)\n- **Notes**: No issues.\n\n### [markovian_chains] — Markovian Generation Chains in Large Language Models (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Geng, Mohamed, Shang, Vazirgiannis, Poibeau)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2603.11228)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex, results.tex: Markovian convergence dynamics)\n- **Notes**: No issues.\n\n### [attractor_cycles] — Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Li, Yan, Cheng, Zhang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2025, Long Papers, pages 12740-12755; arXiv:2502.15208)\n- **Cite usage**: ✓ (related_work.tex: attractor cycle evidence)\n- **Notes**: No issues.\n\n### [min_k_percent] — Detecting Pretraining Data from Large Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: membership inference baseline)\n- **Notes**: No issues.\n\n### [koike_mia_detection] — Machine Text Detectors are Membership Inference Attacks (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Koike, Dugan, Kaneko, Callison-Burch, Okazaki)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2510.19492)\n- **Cite usage**: ✓ (related_work.tex: membership inference connection)\n- **Notes**: No issues.\n\n### [wu_survey_2025] — A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Wu, Yang, Zhan, Yuan, Chao, Wong)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Computational Linguistics, MIT Press, vol. 51, no. 1, pp. 275-338)\n- **Cite usage**: ✓ (related_work.tex: survey reference)\n- **Notes**: No issues.\n\n### [jawahar_survey] — Automatic Detection of Machine Generated Text: A Critical Survey (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Jawahar, Abdul-Mageed, Lakshmanan)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLING 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [pythia] — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Biderman, Schoelkopf, Anthony, et al. — 13 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [olmo] — OLMo: Accelerating the Science of Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Groeneveld, Beltagy, Walsh, et al. — large author list confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, Best Theme Paper)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [qwen3] — Qwen3 Technical Report (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Qwen Team)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2505.09388)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [ghostbuster] — Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Verma, Fleisig, Tomlin, Klein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NAACL 2024, pages 1702-1717)\n- **Cite usage**: ✓ (related_work.tex: learned classifier)\n- **Notes**: No issues.\n\n### [two_birds] — Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Rao, Mohamed, Liu, Liu)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2508.14190)\n- **Cite usage**: ✓ (related_work.tex: joint detection-attribution)\n- **Notes**: No issues.\n\n### [beyond_final_actor] — Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Li, Sheng, Wang, Yang, Wang, Cao)\n- **Year**: ✓ (arXiv April 2026)\n- **Title**: ✓\n- **Venue**: **⚠ — Listed as ACL 2026 (`@inproceedings` with `booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics}`), but ACL 2026 acceptance could not be independently confirmed from official accepted paper lists. The paper exists on arXiv (2604.04932) and its project page mentions ACL 2026. Consider verifying acceptance or citing as arXiv preprint.**\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced. Venue unconfirmed.\n\n### [gutierrez_ordinal_survey] — Ordinal Regression Methods: Survey and Experimental Study (2016)\n- **Exists**: ✓\n- **Authors**: ✓ (Gutierrez, Perez-Ortiz, Sanchez-Monedero, Fernandez-Navarro, Hervas-Martinez)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (IEEE TKDE, vol. 28, no. 1, pp. 127-146)\n- **Cite usage**: ✓ (related_work.tex: ordinal regression reference)\n- **Notes**: No issues.\n\n### [coral_ordinal] — Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Cao, Mirjalili, Raschka)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Pattern Recognition Letters, vol. 140, pp. 325-331)\n- **Cite usage**: ✓ (related_work.tex, method.tex, appendix_classifier.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [frank_hall_ordinal] — A Simple Approach to Ordinal Classification (2001)\n- **Exists**: ✓\n- **Authors**: ✓ (Frank, Hall)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ECML 2001, LNCS 2167, pp. 145-156)\n- **Cite usage**: ✓ (method.tex, appendix_classifier.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [corn_ordinal] — Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Shi, Cao, Raschka)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Pattern Analysis and Applications, vol. 26, pp. 941-955)\n- **Cite usage**: ✓ (method.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [diaz_soft_labels_ordinal] — Soft Labels for Ordinal Regression (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Diaz, Marathe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (CVPR 2019, pp. 4738-4747)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [kasa_ordinality_nlp] — Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Kasa, Goel, Gupta, Roychowdhury, Priyatam, Bhanushali, Murthy)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Findings of ACL 2024, pp. 5390-5404)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [xgboost] — XGBoost: A Scalable Tree Boosting System (2016)\n- **Exists**: ✓\n- **Authors**: ✓ (Chen, Guestrin)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (KDD 2016, pp. 785-794)\n- **Cite usage**: ✓ (method.tex: classifier used throughout)\n- **Notes**: No issues.\n\n### [lakens_equivalence] — Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (2017)\n- **Exists**: ✓\n- **Authors**: ✓ (Lakens)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Social Psychological and Personality Science, vol. 8, no. 4, pp. 355-362)\n- **Cite usage**: ✓ (appendix_tost.tex, appendix_downstream.tex: TOST equivalence testing)\n- **Notes**: No issues.\n\n### [llama3] — The Llama 3 Herd of Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Grattafiori, Dubey, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2407.21783)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [mistral7b] — Mistral 7B (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Jiang, Sablayrolles, Mensch, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2310.06825)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [strobl_conditional_2008] — Conditional Variable Importance for Random Forests (2008)\n- **Exists**: ✓\n- **Authors**: ✓ (Strobl, Boulesteix, Kneib, Augustin, Zeileis)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (BMC Bioinformatics, vol. 9, p. 307)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [dolma] — Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Soldaini, Kinney, Bhagia, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, pages 15725-15788)\n- **Cite usage**: ✓ (introduction.tex: training corpora reference)\n- **Notes**: No issues.\n\n### [fineweb] — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Penedo, Kydlicek, Ben Allal, Lozhkov, Mitchell, Raffel, Von Werra, Wolf)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2024 Datasets and Benchmarks Track)\n- **Cite usage**: ✓ (introduction.tex: training corpora reference)\n- **Notes**: No issues.\n\n### [mapping_llm_science] — Mapping the Increasing Use of LLMs in Scientific Papers (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Liang, Zhang, Wu, Lepp, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)\n- **Notes**: No issues.\n\n### [monitoring_ai_review] — Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Liang, Izzo, Zhang, Lepp, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235:29575-29620)\n- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)\n- **Notes**: No issues.\n\n### [raid] — RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dugan, Hwang, Trhlik, Zhu, Ludan, Xu, Ippolito, Callison-Burch)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, pages 12463-12492)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [human_texts_outliers] — Human Texts Are Outliers: Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective (2025)\n- **Exists**: **✗ — HALLUCINATED ENTRY**\n- **Authors**: **✗ — Bib lists \"Li, Yafu and Hu, Zhilin and Guo, Zetian and Zhao, Wei and Li, Lixin and Hou, Yuanxin\" but arXiv:2510.08602 is authored by Cong Zeng, Shengkun Tang, Yuanzhou Chen, Zhiqiang Shen, Wenchao Yu, Xujiang Zhao, Haifeng Chen, Wei Cheng, Zhiqiang Xu**\n- **Year**: ✓ (2025)\n- **Title**: **✗ — Actual title at arXiv:2510.08602 is \"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection\", not \"...Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\"**\n- **Venue**: **✗ — The real paper at this arXiv ID was accepted at NeurIPS 2025 (poster), not listed as arXiv article**\n- **Cite usage**: ✓ context is valid (related_work.tex: \"reframes detection as an out-of-distribution problem\") but must point to correct paper\n- **Notes**: **CRITICAL — Authors and subtitle are fabricated. The arXiv ID exists but maps to a completely different author set. Must be corrected: fix authors to Cong Zeng et al., fix subtitle, change venue to NeurIPS 2025.**\n\n### [xu_spectrum_detection] — Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Xu, Wang, An, Liu, Li)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: **✗ — Listed as \"arXiv preprint arXiv:2406.19874\" but was published at EMNLP 2024 (pages 10108-10121). Should be updated to `@inproceedings` with `booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing}`.**\n- **Cite usage**: ✓ (related_work.tex: surprisal-based approach)\n- **Notes**: Venue should be upgraded from arXiv to EMNLP 2024.\n\n### [mauve] — MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (2021)\n- **Exists**: ✓\n- **Authors**: ✓ (Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2021, Outstanding Paper Award)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n## Cite Context Issues\n\n1. **`\\cite{human_texts_outliers}`** in `related_work.tex:7` — \"Recent work reframes detection as an out-of-distribution problem \\cite{human_texts_outliers}\". The citation context is thematically appropriate (the real paper IS about OOD-based detection), but the bib entry has hallucinated authors and wrong subtitle. The arXiv ID is correct but the metadata is fabricated.\n\nNo other cite-context mismatches found. All other cited papers correctly support the claims made in the surrounding text.\n\n## Uncited Entries (25 entries in bib but not in any \\cite{} in tex files)\n\nThese entries exist in `references.bib` but are never referenced in any `.tex` file. They will generate LaTeX warnings and should either be cited or removed:\n\n1. `gltr` — GLTR: Statistical Detection and Visualization of Generated Text (2019)\n2. `feat_aug_transformer` — Feature-Augmented Transformers for Robust AI-Text Detection (2026)\n3. `detection_possibilities` — Position: On the Possibilities of AI-Generated Text Detection (2024)\n4. `paraphrase_evades` — Paraphrasing Evades Detectors of AI-Generated Text (2023)\n5. `intrinsic_dim_detection` — Intrinsic Dimension Estimation for Robust Detection (2023)\n6. `seqxgpt` — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)\n7. `grover` — Defending Against Neural Fake News (2019)\n8. `release_strategies` — Release Strategies and the Social Impacts of Language Models (2019)\n9. `model_collapse_avoidable` — Is Model Collapse Inevitable? (2024)\n10. `seddik_synthetic_data` — How Bad is Training on Synthetic Data? (2024)\n11. `qurating` — QuRating: Selecting High-Quality Data (2024)\n12. `aaronson_watermark` — Watermarking GPT Outputs (2022)\n13. `nucleus_sampling` — The Curious Case of Neural Text Degeneration (2020)\n14. `welleck_unlikelihood` — Neural Text Generation with Unlikelihood Training (2020)\n15. `koppel_authorship` — Computational Methods in Authorship Attribution (2009)\n16. `uchendu_attribution` — Authorship Attribution for Neural Text Generation (2020)\n17. `munir_looking_glass` — Through the Looking Glass (2021)\n18. `briesch_self_consuming` — Large Language Models Suffer From Their Own Output (2023)\n19. `jawahar_survey` — Automatic Detection of Machine Generated Text: A Critical Survey (2020)\n20. `beyond_final_actor` — Beyond the Final Actor (2026)\n21. `diaz_soft_labels_ordinal` — Soft Labels for Ordinal Regression (2019)\n22. `kasa_ordinality_nlp` — Exploring Ordinality in Text Classification (2024)\n23. `strobl_conditional_2008` — Conditional Variable Importance for Random Forests (2008)\n24. `raid` — RAID: A Shared Benchmark for Robust Evaluation (2024)\n25. `mauve` — MAUVE: Measuring the Gap Between Neural Text and Human Text (2021)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ref_audit_worker1.md",
    "content": "# Reference Audit — Worker 1\n\n## Summary\n- Total entries: 74\n- Verified OK: 70\n- Issues found: 4 (1 critical, 2 venue errors, 1 unconfirmed venue)\n- Uncited entries (in bib but not in any tex): 25\n\n## Issues Overview\n\n| # | Key | Severity | Issue |\n|---|-----|----------|-------|\n| 1 | `human_texts_outliers` | **CRITICAL** | Authors and subtitle are hallucinated; arXiv ID maps to different paper |\n| 2 | `diveye` | **ERROR** | Venue is TMLR 2026, not ICLR 2026 |\n| 3 | `xu_spectrum_detection` | **WARNING** | Published at EMNLP 2024; still listed as arXiv preprint |\n| 4 | `beyond_final_actor` | **WARNING** | ACL 2026 venue could not be independently confirmed |\n\n## Entry-by-Entry Results\n\n### [cohen1988statistical] — Statistical Power Analysis for the Behavioral Sciences (1988)\n- **Exists**: ✓\n- **Authors**: ✓\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Lawrence Erlbaum Associates, 2nd edition)\n- **Cite usage**: ✓ (appendix_tost.tex: used as SESOI justification for Cohen's d=0.20)\n- **Notes**: Classic reference. No issues.\n\n### [detectgpt] — DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Mitchell, Lee, Khazatsky, Manning, Finn)\n- **Year**: ✓ (ICML 2023)\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023, PMLR 202:24950-24962)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: cited as zero-shot detection method)\n- **Notes**: No issues.\n\n### [gltr] — GLTR: Statistical Detection and Visualization of Generated Text (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Gehrmann, Strobelt, Rush)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2019 System Demonstrations, pages 111-116)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [dna_gpt] — DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Yang, Cheng, Wu, Petzold, Wang, Chen)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as zero-shot scoring method)\n- **Notes**: No issues.\n\n### [binoculars] — Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)\n- **Notes**: No issues.\n\n### [fast_detectgpt] — Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Bao, Zhao, Teng, Yang, Zhang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, method.tex: cited as baseline detection method)\n- **Notes**: No issues.\n\n### [ld_score] — Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Narayanasamy, Agrawal, Faber, Alam)\n- **Year**: ✓ (2026, submitted May 3, 2026)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.01647)\n- **Cite usage**: ✓ (related_work.tex, method.tex: cited as learned classifier / baseline)\n- **Notes**: No issues.\n\n### [diveye] — Diversity Boosts AI-Generated Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Basani, Chen)\n- **Year**: ✓ (2026)\n- **Title**: ✓\n- **Venue**: **✗ — Listed as ICLR 2026 (`@inproceedings` with `booktitle = {Proceedings of the International Conference on Learning Representations}`), but actual venue is TMLR (Transactions on Machine Learning Research), published February 2026. GitHub repo (IBM/diveye) and arXiv PDF header both state \"[TMLR '26]\".**\n- **Cite usage**: ✓ (related_work.tex: cited as surprisal-based approach)\n- **Notes**: Must change entry type to `@article` with `journal = {Transactions on Machine Learning Research}` and `year = {2026}`.\n\n### [feat_aug_transformer] — Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Mady, Reschke, Schuller)\n- **Year**: ✓ (2026)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.03969)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [reliable_detection] — Can AI-Generated Text be Reliably Detected? (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Sadasivan, Kumar, Balasubramanian, Wang, Feizi)\n- **Year**: ✓ (accepted TMLR March 2025)\n- **Title**: ✓\n- **Venue**: ✓ (Transactions on Machine Learning Research)\n- **Cite usage**: ✓ (related_work.tex: cited as learned classifier)\n- **Notes**: No issues.\n\n### [paraphrase_evades] — Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Krishna, Song, Karpinska, Wieting, Iyyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [detection_possibilities] — Position: On the Possibilities of AI-Generated Text Detection (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Chakraborty, Bedi, Zhu, An, Manocha, Huang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235:6093-6115)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [intrinsic_dim_detection] — Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Tulchinskii, Kuznetsov, Kushnareva, Cherniavskii, Nikolenko, Burnaev, Barannikov, Piontkovskaya)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [seqxgpt] — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Li, Ren, Jiang, Zhang, Qiu)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EMNLP 2023)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [grover] — Defending Against Neural Fake News (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Zellers, Holtzman, Rashkin, Bisk, Farhadi, Roesner, Choi)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2019)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [release_strategies] — Release Strategies and the Social Impacts of Language Models (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Solaiman, Brundage, Clark, et al. — 15 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:1908.09203)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [beyond_binary] — Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Cheng, Zhou, Jiang, Wang, Li)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACM Web Conference 2025 / WWW '25)\n- **Cite usage**: ✓ (related_work.tex: cited as collaboration role detection)\n- **Notes**: No issues.\n\n### [semeval2024_task8] — SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Mansurov, Ivanov, et al. — 15 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (SemEval 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as multi-generator attribution)\n- **Notes**: No issues.\n\n### [self_consuming_mad] — Self-Consuming Generative Models Go MAD (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: cited as model collapse reference)\n- **Notes**: No issues.\n\n### [curse_of_recursion] — AI models collapse when trained on recursively generated data (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Nature, volume 631, pages 755-759)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex: cited as model collapse, contrasted with DDR)\n- **Notes**: No issues.\n\n### [dohmatob_tale_of_tails] — A Tale of Tails: Model Collapse as a Change of Scaling Laws (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dohmatob, Feng, Yang, Charton, Kempe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024)\n- **Cite usage**: ✓ (related_work.tex: model collapse reference)\n- **Notes**: No issues.\n\n### [strong_model_collapse] — Strong Model Collapse (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Dohmatob, Feng, Subramonian, Kempe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2025)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, discussion.tex)\n- **Notes**: No issues.\n\n### [model_collapse_avoidable] — Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Gerstgrasser, Schaeffer, Dey, et al. — 14 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [schaeffer_collapse_position] — Position: Model Collapse Does Not Mean What You Think (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Schaeffer, Kazdan, Arulandu, Koyejo)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2503.03150)\n- **Cite usage**: ✓ (related_work.tex: model collapse reference)\n- **Notes**: No issues.\n\n### [seddik_synthetic_data] — How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Seddik, Chen, Hayou, Youssef, Debbah)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [qlora] — QLoRA: Efficient Finetuning of Quantized LLMs (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Dettmers, Pagnoni, Holtzman, Zettlemoyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: ✓ (introduction.tex, appendix_qlora.tex: QLoRA classifier)\n- **Notes**: No issues.\n\n### [dsir] — Data Selection for Language Models via Importance Resampling (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Xie, Santurkar, Ma, Liang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2023)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation quality signal)\n- **Notes**: No issues.\n\n### [qurating] — QuRating: Selecting High-Quality Data for Training Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Wettig, Gupta, Malik, Chen)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [ccnet] — CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Wenzek, Lachaux, Conneau, Chaudhary, Guzman, Joulin, Grave)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (LREC 2020)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: data curation reference)\n- **Notes**: No issues.\n\n### [watermark_llm] — A Watermark for Large Language Models (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023, PMLR 202:17061-17084)\n- **Cite usage**: ✓ (related_work.tex: watermarking reference)\n- **Notes**: No issues.\n\n### [synthid_text] — Scalable Watermarking for Identifying Large Language Model Outputs (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dathathri, See, Ghaisas, et al. — 24 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Nature, volume 634, pages 818-823)\n- **Cite usage**: ✓ (related_work.tex: watermarking reference)\n- **Notes**: No issues.\n\n### [aaronson_watermark] — Watermarking GPT Outputs (2022)\n- **Exists**: ✓\n- **Authors**: ✓ (Aaronson, Kirchner — conventional dual attribution used across literature)\n- **Year**: ✓ (November 2022)\n- **Title**: ✓ (conventional citation title; actual blog post titled differently but this is standard practice)\n- **Venue**: ✓ (Blog post, URL valid)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [chainwash] — Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Ameen, Islam, Mahmud, Hamid)\n- **Year**: ✓ (2026, submitted May 6)\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2605.05503)\n- **Cite usage**: ✓ (related_work.tex: watermark degradation across multi-step chains)\n- **Notes**: No issues.\n\n### [curious_decline] — The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Guo, Shang, Vazirgiannis, Clavel)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Findings of NAACL 2024)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex: lexical diversity decline)\n- **Notes**: No issues.\n\n### [writing_diversity] — Does Writing with Language Models Reduce Content Diversity? (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Padmakumar, He)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: lexical diversity decline)\n- **Notes**: No issues.\n\n### [nucleus_sampling] — The Curious Case of Neural Text Degeneration (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Holtzman, Buys, Du, Forbes, Choi)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [welleck_unlikelihood] — Neural Text Generation with Unlikelihood Training (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Welleck, Kulikov, Roller, Dinan, Cho, Weston)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [stamatatos_survey] — A Survey of Modern Authorship Attribution Methods (2009)\n- **Exists**: ✓\n- **Authors**: ✓ (Stamatatos)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (JASIST, vol. 60, no. 3, pp. 538-556)\n- **Cite usage**: ✓ (related_work.tex: classical stylometric features)\n- **Notes**: No issues.\n\n### [koppel_authorship] — Computational Methods in Authorship Attribution (2009)\n- **Exists**: ✓\n- **Authors**: ✓ (Koppel, Schler, Argamon)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (JASIST, vol. 60, no. 1, pp. 9-26)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [uchendu_attribution] — Authorship Attribution for Neural Text Generation (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Uchendu, Le, Shu, Lee)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EMNLP 2020, pages 8384-8395)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [munir_looking_glass] — Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models (2021)\n- **Exists**: ✓\n- **Authors**: ✓ (Munir, Batool, Shafiq, Srinivasan, Zaffar)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (EACL 2021, pages 1811-1822)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [briesch_self_consuming] — Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Briesch, Sobania, Rothlauf)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2311.16822)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [broken_telephone] — LLM as a Broken Telephone: Iterative Generation Distorts Information (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Mohamed, Geng, Vazirgiannis, Shang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2025, Long Papers, pages 7493-7509)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex: iterative generation distortion)\n- **Notes**: No issues.\n\n### [markovian_chains] — Markovian Generation Chains in Large Language Models (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Geng, Mohamed, Shang, Vazirgiannis, Poibeau)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2603.11228)\n- **Cite usage**: ✓ (introduction.tex, related_work.tex, appendix_iterative_comparison.tex, results.tex: Markovian convergence dynamics)\n- **Notes**: No issues.\n\n### [attractor_cycles] — Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Wang, Li, Yan, Cheng, Zhang)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2025, Long Papers, pages 12740-12755; arXiv:2502.15208)\n- **Cite usage**: ✓ (related_work.tex: attractor cycle evidence)\n- **Notes**: No issues.\n\n### [min_k_percent] — Detecting Pretraining Data from Large Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICLR 2024)\n- **Cite usage**: ✓ (related_work.tex: membership inference baseline)\n- **Notes**: No issues.\n\n### [koike_mia_detection] — Machine Text Detectors are Membership Inference Attacks (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Koike, Dugan, Kaneko, Callison-Burch, Okazaki)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2510.19492)\n- **Cite usage**: ✓ (related_work.tex: membership inference connection)\n- **Notes**: No issues.\n\n### [wu_survey_2025] — A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Wu, Yang, Zhan, Yuan, Chao, Wong)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Computational Linguistics, MIT Press, vol. 51, no. 1, pp. 275-338)\n- **Cite usage**: ✓ (related_work.tex: survey reference)\n- **Notes**: No issues.\n\n### [jawahar_survey] — Automatic Detection of Machine Generated Text: A Critical Survey (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Jawahar, Abdul-Mageed, Lakshmanan)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLING 2020)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [pythia] — Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Biderman, Schoelkopf, Anthony, et al. — 13 authors confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2023)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [olmo] — OLMo: Accelerating the Science of Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Groeneveld, Beltagy, Walsh, et al. — large author list confirmed)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, Best Theme Paper)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [qwen3] — Qwen3 Technical Report (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Qwen Team)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2505.09388)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [ghostbuster] — Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Verma, Fleisig, Tomlin, Klein)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NAACL 2024, pages 1702-1717)\n- **Cite usage**: ✓ (related_work.tex: learned classifier)\n- **Notes**: No issues.\n\n### [two_birds] — Two Birds with One Stone: Multi-Task Detection and Attribution of LLM-Generated Text (2025)\n- **Exists**: ✓\n- **Authors**: ✓ (Rao, Mohamed, Liu, Liu)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2508.14190)\n- **Cite usage**: ✓ (related_work.tex: joint detection-attribution)\n- **Notes**: No issues.\n\n### [beyond_final_actor] — Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection (2026)\n- **Exists**: ✓\n- **Authors**: ✓ (Li, Sheng, Wang, Yang, Wang, Cao)\n- **Year**: ✓ (arXiv April 2026)\n- **Title**: ✓\n- **Venue**: **⚠ — Listed as ACL 2026 (`@inproceedings` with `booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics}`), but ACL 2026 acceptance could not be independently confirmed from official accepted paper lists. The paper exists on arXiv (2604.04932) and its project page mentions ACL 2026. Consider verifying acceptance or citing as arXiv preprint.**\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced. Venue unconfirmed.\n\n### [gutierrez_ordinal_survey] — Ordinal Regression Methods: Survey and Experimental Study (2016)\n- **Exists**: ✓\n- **Authors**: ✓ (Gutierrez, Perez-Ortiz, Sanchez-Monedero, Fernandez-Navarro, Hervas-Martinez)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (IEEE TKDE, vol. 28, no. 1, pp. 127-146)\n- **Cite usage**: ✓ (related_work.tex: ordinal regression reference)\n- **Notes**: No issues.\n\n### [coral_ordinal] — Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation (2020)\n- **Exists**: ✓\n- **Authors**: ✓ (Cao, Mirjalili, Raschka)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Pattern Recognition Letters, vol. 140, pp. 325-331)\n- **Cite usage**: ✓ (related_work.tex, method.tex, appendix_classifier.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [frank_hall_ordinal] — A Simple Approach to Ordinal Classification (2001)\n- **Exists**: ✓\n- **Authors**: ✓ (Frank, Hall)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ECML 2001, LNCS 2167, pp. 145-156)\n- **Cite usage**: ✓ (method.tex, appendix_classifier.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [corn_ordinal] — Deep Neural Networks for Rank-Consistent Ordinal Regression Based On Conditional Probabilities (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Shi, Cao, Raschka)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Pattern Analysis and Applications, vol. 26, pp. 941-955)\n- **Cite usage**: ✓ (method.tex: ordinal classifier alternative)\n- **Notes**: No issues.\n\n### [diaz_soft_labels_ordinal] — Soft Labels for Ordinal Regression (2019)\n- **Exists**: ✓\n- **Authors**: ✓ (Diaz, Marathe)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (CVPR 2019, pp. 4738-4747)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [kasa_ordinality_nlp] — Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Kasa, Goel, Gupta, Roychowdhury, Priyatam, Bhanushali, Murthy)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Findings of ACL 2024, pp. 5390-5404)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [xgboost] — XGBoost: A Scalable Tree Boosting System (2016)\n- **Exists**: ✓\n- **Authors**: ✓ (Chen, Guestrin)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (KDD 2016, pp. 785-794)\n- **Cite usage**: ✓ (method.tex: classifier used throughout)\n- **Notes**: No issues.\n\n### [lakens_equivalence] — Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses (2017)\n- **Exists**: ✓\n- **Authors**: ✓ (Lakens)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (Social Psychological and Personality Science, vol. 8, no. 4, pp. 355-362)\n- **Cite usage**: ✓ (appendix_tost.tex, appendix_downstream.tex: TOST equivalence testing)\n- **Notes**: No issues.\n\n### [llama3] — The Llama 3 Herd of Models (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Grattafiori, Dubey, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2407.21783)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [mistral7b] — Mistral 7B (2023)\n- **Exists**: ✓\n- **Authors**: ✓ (Jiang, Sablayrolles, Mensch, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (arXiv preprint arXiv:2310.06825)\n- **Cite usage**: ✓ (method.tex: generator model reference)\n- **Notes**: No issues.\n\n### [strobl_conditional_2008] — Conditional Variable Importance for Random Forests (2008)\n- **Exists**: ✓\n- **Authors**: ✓ (Strobl, Boulesteix, Kneib, Augustin, Zeileis)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (BMC Bioinformatics, vol. 9, p. 307)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [dolma] — Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Soldaini, Kinney, Bhagia, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, pages 15725-15788)\n- **Cite usage**: ✓ (introduction.tex: training corpora reference)\n- **Notes**: No issues.\n\n### [fineweb] — The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Penedo, Kydlicek, Ben Allal, Lozhkov, Mitchell, Raffel, Von Werra, Wolf)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2024 Datasets and Benchmarks Track)\n- **Cite usage**: ✓ (introduction.tex: training corpora reference)\n- **Notes**: No issues.\n\n### [mapping_llm_science] — Mapping the Increasing Use of LLMs in Scientific Papers (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Liang, Zhang, Wu, Lepp, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (COLM 2024)\n- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)\n- **Notes**: No issues.\n\n### [monitoring_ai_review] — Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Liang, Izzo, Zhang, Lepp, et al.)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ICML 2024, PMLR 235:29575-29620)\n- **Cite usage**: ✓ (introduction.tex: LLM content in scientific publications)\n- **Notes**: No issues.\n\n### [raid] — RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Dugan, Hwang, Trhlik, Zhu, Ludan, Xu, Ippolito, Callison-Burch)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (ACL 2024, pages 12463-12492)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n### [human_texts_outliers] — Human Texts Are Outliers: Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective (2025)\n- **Exists**: **✗ — HALLUCINATED ENTRY**\n- **Authors**: **✗ — Bib lists \"Li, Yafu and Hu, Zhilin and Guo, Zetian and Zhao, Wei and Li, Lixin and Hou, Yuanxin\" but arXiv:2510.08602 is authored by Cong Zeng, Shengkun Tang, Yuanzhou Chen, Zhiqiang Shen, Wenchao Yu, Xujiang Zhao, Haifeng Chen, Wei Cheng, Zhiqiang Xu**\n- **Year**: ✓ (2025)\n- **Title**: **✗ — Actual title at arXiv:2510.08602 is \"Human Texts Are Outliers: Detecting LLM-generated Texts via Out-of-distribution Detection\", not \"...Rethinking Machine-Generated Text Detection from an Out-of-Distribution Perspective\"**\n- **Venue**: **✗ — The real paper at this arXiv ID was accepted at NeurIPS 2025 (poster), not listed as arXiv article**\n- **Cite usage**: ✓ context is valid (related_work.tex: \"reframes detection as an out-of-distribution problem\") but must point to correct paper\n- **Notes**: **CRITICAL — Authors and subtitle are fabricated. The arXiv ID exists but maps to a completely different author set. Must be corrected: fix authors to Cong Zeng et al., fix subtitle, change venue to NeurIPS 2025.**\n\n### [xu_spectrum_detection] — Detecting Subtle Differences between Human and Model Languages Using Spectrum of Relative Likelihood (2024)\n- **Exists**: ✓\n- **Authors**: ✓ (Xu, Wang, An, Liu, Li)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: **✗ — Listed as \"arXiv preprint arXiv:2406.19874\" but was published at EMNLP 2024 (pages 10108-10121). Should be updated to `@inproceedings` with `booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing}`.**\n- **Cite usage**: ✓ (related_work.tex: surprisal-based approach)\n- **Notes**: Venue should be upgraded from arXiv to EMNLP 2024.\n\n### [mauve] — MAUVE: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers (2021)\n- **Exists**: ✓\n- **Authors**: ✓ (Pillutla, Swayamdipta, Zellers, Thickstun, Welleck, Choi, Harchaoui)\n- **Year**: ✓\n- **Title**: ✓\n- **Venue**: ✓ (NeurIPS 2021, Outstanding Paper Award)\n- **Cite usage**: N/A — **UNCITED** in any tex file\n- **Notes**: Entry exists in bib but is never referenced.\n\n## Cite Context Issues\n\n1. **`\\cite{human_texts_outliers}`** in `related_work.tex:7` — \"Recent work reframes detection as an out-of-distribution problem \\cite{human_texts_outliers}\". The citation context is thematically appropriate (the real paper IS about OOD-based detection), but the bib entry has hallucinated authors and wrong subtitle. The arXiv ID is correct but the metadata is fabricated.\n\nNo other cite-context mismatches found. All other cited papers correctly support the claims made in the surrounding text.\n\n## Uncited Entries (25 entries in bib but not in any \\cite{} in tex files)\n\nThese entries exist in `references.bib` but are never referenced in any `.tex` file. They will generate LaTeX warnings and should either be cited or removed:\n\n1. `gltr` — GLTR: Statistical Detection and Visualization of Generated Text (2019)\n2. `feat_aug_transformer` — Feature-Augmented Transformers for Robust AI-Text Detection (2026)\n3. `detection_possibilities` — Position: On the Possibilities of AI-Generated Text Detection (2024)\n4. `paraphrase_evades` — Paraphrasing Evades Detectors of AI-Generated Text (2023)\n5. `intrinsic_dim_detection` — Intrinsic Dimension Estimation for Robust Detection (2023)\n6. `seqxgpt` — SeqXGPT: Sentence-Level AI-Generated Text Detection (2023)\n7. `grover` — Defending Against Neural Fake News (2019)\n8. `release_strategies` — Release Strategies and the Social Impacts of Language Models (2019)\n9. `model_collapse_avoidable` — Is Model Collapse Inevitable? (2024)\n10. `seddik_synthetic_data` — How Bad is Training on Synthetic Data? (2024)\n11. `qurating` — QuRating: Selecting High-Quality Data (2024)\n12. `aaronson_watermark` — Watermarking GPT Outputs (2022)\n13. `nucleus_sampling` — The Curious Case of Neural Text Degeneration (2020)\n14. `welleck_unlikelihood` — Neural Text Generation with Unlikelihood Training (2020)\n15. `koppel_authorship` — Computational Methods in Authorship Attribution (2009)\n16. `uchendu_attribution` — Authorship Attribution for Neural Text Generation (2020)\n17. `munir_looking_glass` — Through the Looking Glass (2021)\n18. `briesch_self_consuming` — Large Language Models Suffer From Their Own Output (2023)\n19. `jawahar_survey` — Automatic Detection of Machine Generated Text: A Critical Survey (2020)\n20. `beyond_final_actor` — Beyond the Final Actor (2026)\n21. `diaz_soft_labels_ordinal` — Soft Labels for Ordinal Regression (2019)\n22. `kasa_ordinality_nlp` — Exploring Ordinality in Text Classification (2024)\n23. `strobl_conditional_2008` — Conditional Variable Importance for Random Forests (2008)\n24. `raid` — RAID: A Shared Benchmark for Robust Evaluation (2024)\n25. `mauve` — MAUVE: Measuring the Gap Between Neural Text and Human Text (2021)\n"
  }
}
```

</details>

---

### Tool result

_source line 402 · 2026-05-26T10:34:47.790692+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/ref_audit_worker1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-worker-1_20260526T102052",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 403 · 2026-05-26T10:34:47.790876+00:00_

审计完成。结果写入 `ref_audit_worker1.md`。

**核心发现：**

| 严重级别 | 条目 | 问题 |
|---------|------|------|
| **CRITICAL** | `human_texts_outliers` | arXiv:2510.08602 的真实作者是 Cong Zeng 等人，标题副标题也不同，bib 中的作者和标题是幻觉生成的 |
| **ERROR** | `diveye` | 会议写的 ICLR 2026，实际发表在 TMLR 2026 |
| **WARNING** | `xu_spectrum_detection` | 已发表于 EMNLP 2024，但仍标为 arXiv preprint |
| **WARNING** | `beyond_final_actor` | ACL 2026 未能从官方接收列表独立确认 |

另外发现 **25 条 bib entry 在所有 tex 文件中未被引用**（详见报告末尾列表），编译时会产生 warning，建议清理或补充引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-worker-1_20260526T102052"
}
```

</details>

---
