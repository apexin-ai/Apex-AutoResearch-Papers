# audit claim consistency — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../audit-claim-consistency.md) · [Structured JSON](../../../sessions/e3/e3cbc095b55e1ab7d7ea.json)

## Before a recorded user message

### Assistant

_source line 85_

Let me now read the temperature ablation data and check the main.tex to determine which experiments file is compiled.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "6d4d3a4f-fbc6-4374-b9df-78fa4418329b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WX1dT6HJ2f8XEtWbj1Usfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 78542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8518
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_01KaZydPqaENiL2uxewNL1gV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 1436,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "21e20422-648f-4ff1-b29a-c12b036b0318",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WX1dT6HJ2f8XEtWbj1Usfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 78542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8518
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T02:44:34.410Z_

<details><summary>↩ Tool result · `toolu_01KaZydPqaENiL2uxewNL1gV`</summary>

```text
1436	
1437	\paragraph{Temperature controls degeneracy and LP spread.}
1438	Table~\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.
1439	Both quantities are strictly monotonic in $T$: degeneracy falls from 41.4\% ($T{=}0.5$) to 14.9\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.
1440	Temperature thus provides a direct lever for practitioners to shift the degeneracy regime.
1441	However, even at $T{=}1.2$ where degeneracy (14.9\%) approaches Few-NERD levels (${\sim}$13\%), within-instance $\rho(\text{LP}, \text{F1})$ remains at 0.225, far below Few-NERD's ${\sim}$0.5.
1442	This confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\S\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\S\ref{sec:discussion}).
1443	
1444	\begin{table}[h]
1445	\centering
1446	\small
1447	\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}
1448	\label{tab:t_degeneracy}
1449	\resizebox{\columnwidth}{!}{
1450	\begin{tabular}{ccccc}
1451	\toprule
1452	$T$ & Degen.\% & LP range (nats) & Fleiss' $\kappa$ & SJ mean \\
1453	\midrule
1454	0.5 & 41.4 & 0.015 & 0.572 & 0.830 \\
1455	0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\
1456	1.0 & 17.8 & 0.042 & 0.405 & 0.700 \\
1457	1.2 & 14.9 & 0.058 & 0.352 & 0.647 \\
1458	\bottomrule
1459	\end{tabular}
1460	}
1461	\end{table}
1462	
1463	\section{Cross-Dataset OOD Analysis}\label{app:ood}
1464	
1465	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "2aab54a6-2f73-4f33-9ca2-ee021044c2c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\n\\paragraph{Temperature controls degeneracy and LP spread.}\nTable~\\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.\nBoth quantities are strictly monotonic in $T$: degeneracy falls from 41.4\\% ($T{=}0.5$) to 14.9\\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.\nTemperature thus provides a direct lever for practitioners to shift the degeneracy regime.\nHowever, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$13\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\nThis confirms that temperature controls degeneracy but cannot improve LP-quality alignment, which is largely determined by task structure and remains relatively stable across generation configurations (\\S\\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\\S\\ref{sec:discussion}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\n\\label{tab:t_degeneracy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ccccc}\n\\toprule\n$T$ & Degen.\\% & LP range (nats) & Fleiss' $\\kappa$ & SJ mean \\\\\n\\midrule\n0.5 & 41.4 & 0.015 & 0.572 & 0.830 \\\\\n0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\\\\n1.0 & 17.8 & 0.042 & 0.405 & 0.700 \\\\\n1.2 & 14.9 & 0.058 & 0.352 & 0.647 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).",
      "numLines": 30,
      "startLine": 1436,
      "totalLines": 2025
    }
  }
}
```

</details>

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01B3pGu6GmNB3dRF1pv6Y5g9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "02417af3-9d5f-44de-8755-6c97260279e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WX1dT6HJ2f8XEtWbj1Usfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 78542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8518
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-21T02:44:35.498Z_

<details><summary>↩ Tool result · `toolu_01B3pGu6GmNB3dRF1pv6Y5g9`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	
25	\graphicspath{{figures/}}
26	
27	\title{The Capability Ceiling of Self-Consistency:\\ Why Entity-Level Self-Verification Fails in Structured Generation}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\input{sections/abstract}
35	\input{sections/introduction}
36	\input{sections/diagnostic}
37	\input{sections/mechanistic}
38	\input{sections/single_signal}
39	\input{sections/adaptive}
40	\input{sections/theory}
41	\input{sections/experiments_main}
42	\input{sections/background}
43	\input{sections/discussion}
44	\input{sections/conclusion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
59	\bibliography{references}
60	
61	\appendix
62	\renewcommand{\thesection}{\alphalph{\value{section}}}
63	\input{sections/appendix}
64	
65	\end{document}
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "78dcdbe9-76b0-4b0b-8e4f-080f44ca492e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}{Corollary}\n\\newtheorem{definition}{Definition}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{alphalph}\n\n\\graphicspath{{figures/}}\n\n\\title{The Capability Ceiling of Self-Consistency:\\\\ Why Entity-Level Self-Verification Fails in Structured Generation}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/diagnostic}\n\\input{sections/mechanistic}\n\\input{sections/single_signal}\n\\input{sections/adaptive}\n\\input{sections/theory}\n\\input{sections/experiments_main}\n\\input{sections/background}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).\nCoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\nCode and data will be released upon acceptance at [anonymized URL].\n\n\\section*{Responsible NLP Research Checklist}\n\\input{sections/checklist}\n\n\\bibliography{references}\n\n\\appendix\n\\renewcommand{\\thesection}{\\alphalph{\\value{section}}}\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  }
}
```

</details>

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Grep · `toolu_01LQoxHcYAJmPukWho2SrCXX`</summary>

```json
{
  "pattern": "\\\\input|\\\\include",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "de761dd8-1e89-48f7-9f2f-a05b1671f67e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WX1dT6HJ2f8XEtWbj1Usfa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8518,
      "cache_read_input_tokens": 78542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8518
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-21T02:44:36.193Z_

<details><summary>↩ Tool result · `toolu_01LQoxHcYAJmPukWho2SrCXX`</summary>

```text
34:\input{sections/abstract}
35:\input{sections/introduction}
36:\input{sections/diagnostic}
37:\input{sections/mechanistic}
38:\input{sections/single_signal}
39:\input{sections/adaptive}
40:\input{sections/theory}
41:\input{sections/experiments_main}
42:\input{sections/background}
43:\input{sections/discussion}
44:\input{sections/conclusion}
47:\input{sections/limitations}
57:\input{sections/checklist}
63:\input{sections/appendix}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "d01124b8-bd2d-4124-a1e0-0865ac7a318e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "34:\\input{sections/abstract}\n35:\\input{sections/introduction}\n36:\\input{sections/diagnostic}\n37:\\input{sections/mechanistic}\n38:\\input{sections/single_signal}\n39:\\input{sections/adaptive}\n40:\\input{sections/theory}\n41:\\input{sections/experiments_main}\n42:\\input{sections/background}\n43:\\input{sections/discussion}\n44:\\input{sections/conclusion}\n47:\\input{sections/limitations}\n57:\\input{sections/checklist}\n63:\\input{sections/appendix}",
    "numLines": 14
  }
}
```

</details>

---


### Assistant

_source line 92_

<details><summary>Logged reasoning block</summary>

```text
Now I know which file is compiled. The main.tex includes `sections/experiments_main.tex` (not `sections/experiments.tex`). So `experiments.tex` is the old version that's NOT compiled. The compiled version is `experiments_main.tex`.

Now let me also extract the registry data for specific experiments to verify the numbers. Let me use jq to query the registry file.

Let me compile my findings now. Let me also verify the Holm p-value for the abstract claim "Holm-adjusted p=0.019" — this is for LP selection, not construction. The construction has different Holm values.


I'm seeing the distinction now: the abstract and introduction both reference the same LP selection result with Holm p=0.019 on Few-NERD, while the construction results show different p-values (0.006 for Few-NERD and 0.004 for SciERC).

There's a discrepancy between the compiled experiments_main.tex and the uncompiled experiments.tex file—the latter claims the result survives at k=57 while the former says it doesn't at that family size. Since experiments.tex isn't part of the final paper, this won't affect the published version, but it's worth noting the inconsistency exists in the repository.

I'm also noticing that the cross-model improvement of +0.42 percentage points is consistently attributed to SciERC in the technical sections, but the abstract and introduction mention it without that dataset specification, which could be misleading to readers. Additionally, I need to verify the oracle scaling exponent values—they vary across sections (conclusion and discussion say c≈0.5, while the theory section breaks it down by dataset as c≈0.61 for Few-NERD and c≈0.35 for SciERC), so I should check if these are meant to represent different things or if there's an inconsistency to flag. Looking at the appendix more carefully, I see the "+0.12 pp" for LP gain in one of the tables, which is close to the "+0.1pp" reference I was searching for. The VC method shows "+0.28 pp" over single-sample, while LP shows a smaller gain around "+0.12 pp" on some datasets, though WNUT shows a negative gain of "-0.45 pp". I need to trace whether these specific numbers correspond to the claims about single-sample versus greedy comparisons.

Now I'm checking the probe AUROC results more carefully—the memory notes show FewNERD at 0.987 and CoNLL at 0.980 for the linear probe, but the mechanistic.tex file has a placeholder comment indicating the hidden state probe results haven't been integrated into the paper yet. The placeholder suggests the probe AUROC should be around 0.87 (matching the majority vote baseline) while the ESJ AUROC is 0.51, which would demonstrate that information exists in the representations but the prompt-based interface can't access it.

The confusion seems to stem from different experiments—the 0.987 AUROC is from entity correctness classification on hidden states (P0-1), which is separate from the per-sample F1 prediction task shown in the appendix table. I'm also noticing the task mentions a 0.920 figure that I can't locate anywhere, and there's a verifier AUC around 0.923 that might be getting conflated with the probe results.

Now I need to cross-reference the Holm-Bonferroni correction table in the appendix to verify the reported adjusted p-values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "1c3b26a6-bfc1-4e05-a31d-16ee6231746b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r6Z8wwaKiATBgEsa4whLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 87060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 93_

Now let me read the Holm table and the self-verification full table in the appendix to verify the p-values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "703ffeee-df66-459d-b8d0-9fc3cbe70721",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r6Z8wwaKiATBgEsa4whLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 87060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Read · `toolu_01WYD71CyDxU4nKDJ5hwNZcq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 315,
  "limit": 90
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "7c0f9be4-4b40-4294-bb2d-6525565b066f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r6Z8wwaKiATBgEsa4whLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 87060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-21T02:45:14.352Z_

<details><summary>↩ Tool result · `toolu_01WYD71CyDxU4nKDJ5hwNZcq`</summary>

```text
315	
316	Table~\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.
317	Under this most conservative family, no core NER claim survives ($p_{\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).
318	We report per-family corrections in the main text (\S\ref{sec:prescriptive}); the global enumeration is provided here for transparency.
319	
320	\begin{table*}[t]
321	\centering
322	\small
323	\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\dagger$Survives correction at $\alpha{=}0.05$.}
324	\label{tab:holm_family}
325	\begin{tabular}{clllcc}
326	\toprule
327	\# & Family & Test Description & Raw $p$ & $p_{\text{adj}}$ & Sig. \\
328	\midrule
329	\multicolumn{6}{l}{\textit{Selection}} \\
330	1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\
331	2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\
332	3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\
333	4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\
334	5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\
335	6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\
336	7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\
337	8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\
338	9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\
339	10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\
340	11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\
341	12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\
342	13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\
343	14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\
344	15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\
345	16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\
346	17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\
347	18 & & SciERC LP selection, non-tied subset ($\varepsilon{=}0.05$) & $0.004$ & $0.180$ &  \\
348	19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\
349	\addlinespace
350	\multicolumn{6}{l}{\textit{Construction}} \\
351	20 & & SciERC LP-weighted construction (Qwen, 3-seed) & $0.004$ & $0.180$ &  \\
352	21 & & SciERC uniform construction (Qwen, 3-seed) & $0.023$ & $0.874$ &  \\
353	22 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\
354	23 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\
355	24 & & CoNLL uniform construction (Qwen) & $0.500$ & $1.0$ &  \\
356	25 & & SciERC ZS construction (72B) & $0.008$ & $0.320$ &  \\
357	26 & & SciERC FS construction (72B) & $0.544$ & $1.0$ &  \\
358	27 & & CoNLL FS construction (72B) & $0.417$ & $1.0$ &  \\
359	28 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\
360	29 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\
361	\addlinespace
362	\multicolumn{6}{l}{\textit{Calibration}} \\
363	30 & & SciERC MF-Platt vs Raw LP & $0.720$ & $1.0$ &  \\
364	31 & & CoNLL MF-Platt vs Raw LP & $0.310$ & $1.0$ &  \\
365	32 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\
366	\addlinespace
367	\multicolumn{6}{l}{\textit{Signal $\Delta\rho$}} \\
368	33 & & SciERC $\Delta\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\
369	34 & & SciERC $\Delta\rho$ VC$-$SJ ($N{=}8$, seed 42) & $0.300$ & $1.0$ &  \\
370	35 & & SciERC $\Delta\rho$ SJ$-$EM ($N{=}8$, seed 42) & $0.045$ & $1.0$ &  \\
371	36 & & CoNLL $\Delta\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\
372	37 & & CoNLL $\Delta\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\
373	38 & & CoNLL $\Delta\rho$ VC$-$FK ($N{=}16$) & $0.040$ & $1.0$ &  \\
374	39 & & SciERC $\Delta\rho$ SJ$-$FK (LLaMA, permutation) & $0.060$ & $1.0$ &  \\
375	40 & & SciERC RE $\Delta\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\
376	41 & & RE SJ $\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\
377	\addlinespace
378	\multicolumn{6}{l}{\textit{Correlation}} \\
379	42 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\
380	43 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\
381	44 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\
382	45 & & Per-type degeneracy--headroom ($\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\
383	46 & & SciERC per-type degeneracy--LP ($\rho{=}0.14$) & $0.790$ & $1.0$ &  \\
384	47 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\
385	\addlinespace
386	\multicolumn{6}{l}{\textit{FS error}} \\
387	48 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\
388	49 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\
389	50 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\
390	51 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\dagger$ \\
391	\addlinespace
392	\multicolumn{6}{l}{\textit{Other}} \\
393	52 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\
394	53 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\dagger$ \\
395	54 & & WNUT-17 conditional $\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\
396	55 & & WNUT-17 conditional $\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\
397	56 & & SciERC LP favorable subset ($+$2.47 pp) & $0.015$ & $0.585$ &  \\
398	57 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\
399	\bottomrule
400	\end{tabular}
401	\end{table*}
402	
403	\section{Diversity and Selection Analysis}\label{app:diversity}
404	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "4cb338d8-a0aa-4b6f-8b41-1efbde0a2a0d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\nTable~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.\nUnder this most conservative family, no core NER claim survives ($p_{\\text{adj}}{=}0.055$ for Few-NERD LP selection and construction); only two peripheral tests reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\n\\label{tab:holm_family}\n\\begin{tabular}{clllcc}\n\\toprule\n\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Selection}} \\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\n18 & & SciERC LP selection, non-tied subset ($\\varepsilon{=}0.05$) & $0.004$ & $0.180$ &  \\\\\n19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Construction}} \\\\\n20 & & SciERC LP-weighted construction (Qwen, 3-seed) & $0.004$ & $0.180$ &  \\\\\n21 & & SciERC uniform construction (Qwen, 3-seed) & $0.023$ & $0.874$ &  \\\\\n22 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\\\\n23 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\n24 & & CoNLL uniform construction (Qwen) & $0.500$ & $1.0$ &  \\\\\n25 & & SciERC ZS construction (72B) & $0.008$ & $0.320$ &  \\\\\n26 & & SciERC FS construction (72B) & $0.544$ & $1.0$ &  \\\\\n27 & & CoNLL FS construction (72B) & $0.417$ & $1.0$ &  \\\\\n28 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\n29 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Calibration}} \\\\\n30 & & SciERC MF-Platt vs Raw LP & $0.720$ & $1.0$ &  \\\\\n31 & & CoNLL MF-Platt vs Raw LP & $0.310$ & $1.0$ &  \\\\\n32 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Signal $\\Delta\\rho$}} \\\\\n33 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\\\\n34 & & SciERC $\\Delta\\rho$ VC$-$SJ ($N{=}8$, seed 42) & $0.300$ & $1.0$ &  \\\\\n35 & & SciERC $\\Delta\\rho$ SJ$-$EM ($N{=}8$, seed 42) & $0.045$ & $1.0$ &  \\\\\n36 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n37 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n38 & & CoNLL $\\Delta\\rho$ VC$-$FK ($N{=}16$) & $0.040$ & $1.0$ &  \\\\\n39 & & SciERC $\\Delta\\rho$ SJ$-$FK (LLaMA, permutation) & $0.060$ & $1.0$ &  \\\\\n40 & & SciERC RE $\\Delta\\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\\\\n41 & & RE SJ $\\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Correlation}} \\\\\n42 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\\\\n43 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\n44 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\\\\n45 & & Per-type degeneracy--headroom ($\\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\\\\n46 & & SciERC per-type degeneracy--LP ($\\rho{=}0.14$) & $0.790$ & $1.0$ &  \\\\\n47 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{FS error}} \\\\\n48 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\\\\n49 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\\\\n50 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\\\\n51 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\\dagger$ \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Other}} \\\\\n52 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\\\\n53 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\\dagger$ \\\\\n54 & & WNUT-17 conditional $\\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\\\\n55 & & WNUT-17 conditional $\\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\\\\n56 & & SciERC LP favorable subset ($+$2.47 pp) & $0.015$ & $0.585$ &  \\\\\n57 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n",
      "numLines": 90,
      "startLine": 315,
      "totalLines": 2025
    }
  }
}
```

</details>

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_012Zm12Fi5kcHXeqEDxy4Sq6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 603,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "761fd596-c364-4b2a-8cf6-275371c02729",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r6Z8wwaKiATBgEsa4whLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 87060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-21T02:45:15.232Z_

<details><summary>↩ Tool result · `toolu_012Zm12Fi5kcHXeqEDxy4Sq6`</summary>

```text
603	\section{Entity-Level Self-Verification Probes}\label{app:self_verification}
604	
605	Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).
606	
607	\begin{table}[t]
608	\centering
609	\small
610	\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}
611	\label{tab:self_verification}
612	\begin{tabular}{@{}lcc@{}}
613	\toprule
614	Method & Key Metric & F1 \\
615	\midrule
616	Greedy ($T{=}0$) & --- & .794 \\
617	MV ($\theta{=}0.375$) & --- & .792 \\
618	Oracle & --- & .882 \\
619	\midrule
620	ESJ (best $\theta{=}0.02$) & AUROC${=}0.512$ & .711 \\
621	MRSC (best $\theta{=}0.5$) & $\Delta P(\text{yes}){=}0.001$ & .763 \\
622	LSC (centroid) & $\rho_{\text{LP-latent}}{=}0.52$ & .759 \\
623	LSC (entity conf.) & --- & .839 \\
624	\midrule
625	Freq.\ agreement & AUROC${=}0.868$ & --- \\
626	\bottomrule
627	\end{tabular}
628	\end{table}
629	
630	\paragraph{Entity Self-Judgment (ESJ).}
631	For each extracted entity, we prompt the model: ``Is [entity] a [type] entity in this sentence?''
632	The entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$ (separation $0.001$).
633	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$), confirming the model lacks entity-level self-judgment.
634	
635	\paragraph{Multi-Round Self-Consistency (MRSC).}
636	We re-prompt the model on disputed entities (agreement ${<}0.6$) with a focused verification query and aggregate with Round~2 weight${=}2$.
637	P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$), and MRSC best F1 ($0.763$) falls below both greedy and MV.
638	
639	\paragraph{Latent Self-Consistency (LSC).}
640	Mean-pooled final-layer hidden states ($d{=}3584$) provide latent representations per sample.
641	Centroid selection ($0.759$) underperforms greedy ($0.779$); latent entity confidence ($0.839$) marginally outperforms MV ($0.837$) but does not close the oracle gap.
642	
643	\paragraph{Frequency agreement as the viable signal.}
644	Cross-sample entity frequency agreement achieves AUROC${=}0.868$ for entity correctness prediction---the only effective entity-level signal.
645	This asymmetry (self-judgment fails, frequency agreement succeeds) implies that models encode entity-level quality in output \textit{distributions} rather than in per-sample self-evaluation capacity, consistent with the correlation-selection gap diagnosed in the main text (\S\ref{sec:selection_gap}).
646	
647	\section{Multi-Seed Stability}\label{app:multiseed}
648	
649	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
650	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
651	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.
652	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
653	
654	\begin{table}[t]
655	\centering
656	\small
657	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
658	\label{tab:multiseed}
659	\resizebox{\columnwidth}{!}{
660	\begin{tabular}{lccccc}
661	\toprule
662	& LP & FK & SJ & VC & EM \\
663	\midrule
664	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
665	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
666	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
667	\midrule
668	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
669	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
670	\midrule
671	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
672	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
673	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
674	\bottomrule
675	\end{tabular}
676	}
677	\end{table}
678	
679	\section{Training Configuration}\label{app:training}
680	
681	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
682	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "61fb2eca-bf70-48f7-b9fb-c3f46cd3746c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}\n\nThree independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\n\\label{tab:self_verification}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Key Metric & F1 \\\\\n\\midrule\nGreedy ($T{=}0$) & --- & .794 \\\\\nMV ($\\theta{=}0.375$) & --- & .792 \\\\\nOracle & --- & .882 \\\\\n\\midrule\nESJ (best $\\theta{=}0.02$) & AUROC${=}0.512$ & .711 \\\\\nMRSC (best $\\theta{=}0.5$) & $\\Delta P(\\text{yes}){=}0.001$ & .763 \\\\\nLSC (centroid) & $\\rho_{\\text{LP-latent}}{=}0.52$ & .759 \\\\\nLSC (entity conf.) & --- & .839 \\\\\n\\midrule\nFreq.\\ agreement & AUROC${=}0.868$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Entity Self-Judgment (ESJ).}\nFor each extracted entity, we prompt the model: ``Is [entity] a [type] entity in this sentence?''\nThe entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$ (separation $0.001$).\nESJ-weighted construction degrades F1 to $0.711$ (vs.\\ greedy $0.794$), confirming the model lacks entity-level self-judgment.\n\n\\paragraph{Multi-Round Self-Consistency (MRSC).}\nWe re-prompt the model on disputed entities (agreement ${<}0.6$) with a focused verification query and aggregate with Round~2 weight${=}2$.\nP(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\\ $0.4997$), and MRSC best F1 ($0.763$) falls below both greedy and MV.\n\n\\paragraph{Latent Self-Consistency (LSC).}\nMean-pooled final-layer hidden states ($d{=}3584$) provide latent representations per sample.\nCentroid selection ($0.759$) underperforms greedy ($0.779$); latent entity confidence ($0.839$) marginally outperforms MV ($0.837$) but does not close the oracle gap.\n\n\\paragraph{Frequency agreement as the viable signal.}\nCross-sample entity frequency agreement achieves AUROC${=}0.868$ for entity correctness prediction---the only effective entity-level signal.\nThis asymmetry (self-judgment fails, frequency agreement succeeds) implies that models encode entity-level quality in output \\textit{distributions} rather than in per-sample self-evaluation capacity, consistent with the correlation-selection gap diagnosed in the main text (\\S\\ref{sec:selection_gap}).\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:multiseed}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n",
      "numLines": 80,
      "startLine": 603,
      "totalLines": 2025
    }
  }
}
```

</details>

---


### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_018ynFeyTPesQhYNtcqgR4Da`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 255,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "5106dc46-5ddb-4120-baea-4c58bd99cac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017r6Z8wwaKiATBgEsa4whLi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3543,
      "cache_read_input_tokens": 87060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-21T02:45:15.712Z_

<details><summary>↩ Tool result · `toolu_018ynFeyTPesQhYNtcqgR4Da`</summary>

```text
255	
256	\paragraph{Diminishing returns of $N$-scaling.}
257	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
258	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
259	Structural signals use $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.
260	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
261	For sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
262	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
263	
264	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
265	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
266	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
267	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
268	This reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.
269	
270	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
271	
272	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
273	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \S\ref{sec:qe_results} is robust.
274	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.
275	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
276	
277	\begin{table}[t]
278	\centering
279	\small
280	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
281	\label{tab:bootstrap_signal_ci}
282	\begin{tabular}{lcc}
283	\toprule
284	Signal & $\rho$ & 95\% CI \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "dbae21e6-a544-4d25-8730-c25adfd8b658",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals use $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \\S\\ref{sec:qe_results} is robust.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\",
      "numLines": 30,
      "startLine": 255,
      "totalLines": 2025
    }
  }
}
```

</details>

---


### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also verify the Holm p-value claims.

From the Holm table (appendix):
- Row 6: Few-NERD LP selection (N=8, Qwen, 3-seed): raw p < .001, p_adj = 0.055
- Row 19: Few-NERD LP selection (N=8, LLaMA, 3-seed): raw p < .001, p_adj = 0.055
- Row 22: Few-NERD LP-weighted construction (Qwen): raw p < .001, p_adj = 0.055


- Abstract claims "Holm-adjusted p=0.019" but the global Holm correction at k=57 gives 0.055, not 0.019 — that's a discrepancy. The Introduction mentions "Holm p_adj=0.019, selection family k=19" which suggests they're using a per-family correction instead of global; with k=19, the Holm adjustment for p < 0.001 would indeed be around 0.019. The construction result claims "Holm p_adj=0.006" but I need to check what correction level that corresponds to.

Actually, looking at the construction family with k=10, the Holm adjustment for p < 0.001 would be approximately 0.006, which matches. The experiments_main.tex file explicitly states "Holm p_adj=0.006, construction family k=10" and the footnote acknowledges that under the global family (k=57), no core claims survive with p_adj=0.055. So the abstract's 0.019 appears to be the selection-family correction, not the global one — technically correct if per-family Holm is acceptable, but potentially misleading since readers might assume it's the most conservative correction.

The introduction's bullet 4 also reports the same 0.019 for the selection family, which is accurate for that specific family but not for the global correction. Meanwhile, the non-compiled experiments.tex incorrectly claims the result "survives Holm–Bonferroni at k=57," but the Holm table clearly shows p_adj=0.055 at k=57, which fails to survive at α=0.05. The compiled experiments_main.tex avoids this error by correctly specifying the construction family (k=10) where the adjustment does survive. The compiled version correctly uses k=10 for the family correction, while the stale non-compiled file incorrectly references k=57—this inconsistency could be misleading even though only the correct version gets compiled. Now I'm cross-checking key numerical results against the memory file to verify consistency across the paper. I'm verifying the cross-model +0.42 pp result — it's specifically on SciERC comparing combined Qwen and LLaMA sampling against pure LLaMA sampling, not against greedy decoding, which is an important distinction that the abstract glosses over. Checking the Spider SQL metrics now: the 87.2% degeneracy figure and +0.51 pp gain from multi-value handling both align across the paper sections. Now I need to address the flagged issues from the original task. 's SciERC, but the abstract and intro don't make that clear.

Looking at the probe AUROC numbers, there's a discrepancy between what's in the paper text and what's in memory.md. The paper mentions 0.868 for frequency agreement, 0.512 for entity self-judgment, and 0.923 for the trained verifier, but memory.md shows much higher values like 0.987 and 0.980 for the linear probes on FewNERD and CoNLL respectively. I need to figure out which numbers are actually being reported and whether these are measuring different things.

The hidden state probes that do appear in the paper measure Spearman correlation with per-sample F1, not entity-level AUROC, so the 0.987 and 0.980 from memory.md aren't directly comparable to what's in the appendix. The 0.920 mentioned as inconsistent might be a rounded version of the 0.923 verifier AUC, but neither of these high probe numbers actually show up in the current paper text.

For degeneracy, the definition is consistent across the paper — it's the fraction of instances where all N samples produce identical F1 scores.

Now I'm checking the reported degeneracy numbers across datasets to verify consistency: SciERC stays at 17.8%, CoNLL at 61.7%, Few-NERD at 13.0%, WNUT-17 at 67.9%, and Spider SQL at 87.2%. The scaling table confirms CoNLL's 61.7% for 8B fine-tuned and 67.7% for 72B zero-shot, which matches what's in memory.md. For the temperature ablation, I need to check which seed the appendix table is using.

The temperature ablation table references seed=42 with different task configurations at each temperature level, and the discussion cites SciERC results at T=1.2 showing 14.9% degeneracy. But memory.md has temperature ablation data for CoNLL under seed=123 and Few-NERD under seed=42, while the paper's table only references SciERC with seed=42. There's a mismatch between what's documented in memory and what appears in the paper.

Now I'm looking at the specific metrics from the temperature ablations across these datasets—CoNLL shows relatively stable F1 scores around 0.907 with varying correlation patterns, while Few-NERD shows consistent F1 around 0.788 but with notable drops in correlation at higher temperatures.

I'm also verifying the key claims against the tables: the maximum correlation of 0.451 on CoNLL with Qwen checks out, the AUROC value of 0.816 rounds appropriately to the stated 0.82, and for SciERC the oracle-greedy gap is about 13 percentage points as claimed.

But I'm noticing a discrepancy with the majority vote claim on FewNERD—the introduction states +1.40 pp, which matches the LP-weighted construction result in the table, but the uniform majority vote actually shows only +0.74 pp, so the paper appears to be citing the LP-weighted version without clarifying that distinction. I need to double-check the Holm-adjusted p-values more carefully. The abstract claims p=0.019 for LP selection, but looking at the actual table, the Few-NERD LP selection test has a raw p < .001 with a global adjusted p of 0.055. When I trace through the Holm correction for the selection family (k=19 tests), this particular test should have a different adjusted p-value than what's stated. the paper reports p_adj=0.006 for construction, which matches the family-corrected calculation. Checking the introduction's contribution claims, the LP selection gain of +1.39 pp comes from Few-NERD as stated. For the oracle scaling claim of c≈0.5, the actual values are c≈0.61 for Few-NERD and c≈0.35 for SciERC, averaging to roughly 0.48—so the rounded figure checks out.

The seven methods listed in the introduction count correctly: entity self-judgment, multi-round self-consistency, latent-space aggregation, heterogeneous temperature sampling, adaptive sampling budget, self-consistency distillation, and the supervised verifier. Now I'm verifying the LP ensemble weight claim of 0.78 that appears in both the method and diagnostic sections.

Looking at the memory file, I see specific configurations like LP=0.9 with VC=0.1 yielding +0.30pp improvement, and Qwen3-8B showing LP=0.8 with VC=0.2 for +0.64pp, so 0.78 as a mean across different setups seems reasonable. I'm also noticing a potential inconsistency between the two sections about structural signals—one describes them as "secondary regularizers" while the other says "zero weight"—but since only the diagnostic section is actually compiled into the final document, that's the version that matters. There's a discrepancy between what the compiled diagnostic.tex claims about structural signals receiving zero weight versus what memory.md documents — VC is listed with non-zero weights (0.1-0.2) across different configurations, yet VC is itself a structural signal. This could mean the paper text is inaccurate, the memory notes describe a different experimental setup, or "structural signals" refers to a narrower subset like SJ/FK specifically.

Looking at the uncompiled method.tex clarifies this somewhat — it describes structural signals as "secondary regularizers," which is compatible with VC having modest weight. I'll flag this as a potential inconsistency but note it's resolvable depending on the exact definitions.

Now I'm verifying the numerical claims: the "AUROC up to 0.82" checks out since the maximum observed is 0.816, which rounds appropriately. I need to confirm the "ρ up to 0.45" claim against the actual maximum values before compiling the full audit table. CoNLL Qwen EM = 0.451, which rounds to 0.45. ✓ The LP compression median range of 0.041 nats checks out across the related work and temperature table—0.041 versus 0.042 is just a minor rounding difference.

Now I'm identifying the critical inconsistencies. The abstract reports Holm-adjusted p=0.019 for the per-family correction (k=19), but this isn't the global correction (k=57 gives p_adj=0.055), which is misleading without that context. The introduction claims entity-level construction improves by +1.40 pp via majority vote, but that's actually the LP-weighted version—plain majority vote is only +0.74 pp. The experiments.tex file falsely claims the result survives Holm-Bonferroni at k=57, which contradicts the actual table showing p_adj=0.055, though this file isn't compiled anyway. Diagnostic.tex states structural signals receive zero weight, yet memory.md shows VC gets 0.1–0.2 weight in the ensemble, so that's imprecise. There's also ambiguity around the cross-model +0.42 pp improvement in the abstract regarding which dataset it applies to.

Additionally, the abstract and introduction don't specify that the SciERC-only result is limited to that dataset—Limitations.tex clarifies this, but readers could be misled. The probe AUROC results (0.987 on FewNERD, 0.980 on CoNLL) from memory.md aren't included in the paper despite a placeholder comment, and these measure entity correctness prediction rather than the sample-level F1 correlation that the appendix probes measure. The abstract rounds AUROC values to 0.87 and 0.51 when the actual values are 0.868 and 0.512—technically correct rounding but worth noting.

Now I'm verifying the reported numbers against the tables and derivations: the performance improvements across datasets check out, the critical threshold of 0.70 derives correctly from the given parameters, and the verifier AUC, ESJ AUROC, frequency agreement AUROC, and temperature ablation results all align with what's documented.

I'm also cross-checking the oracle scaling coefficients and dataset sizes, which are consistent with the memory documentation. However, I'm noticing some discrepancies—those claimed improvements of +0.1pp and +0.4pp don't appear in the current compiled text, and the probe AUROC values seem to have conflicting numbers in the paper where 0.987 and 0.920 can't both be correct.

Looking at the source more carefully, 0.920 appears to be the verifier AUC rounded, while 0.987 comes from the P0-1 probe in the memory file. Now I'm ready to compile the final audit table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "a192f1b6-391b-4ba3-a39c-f8c2bfc17bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZEDapk7jiyKhNSgS4BeSM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8474,
      "cache_read_input_tokens": 90603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8474
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 101_

Now I have sufficient data. Let me compile the full audit.

---

## Claim Audit Report

### Compiled files (per main.tex)
`sections/abstract.tex`, `sections/introduction.tex`, `sections/diagnostic.tex`, `sections/mechanistic.tex`, `sections/single_signal.tex`, `sections/adaptive.tex`, `sections/theory.tex`, `sections/experiments_main.tex`, `sections/background.tex`, `sections/discussion.tex`, `sections/conclusion.tex`, `sections/limitations.tex`, `sections/appendix.tex`

**NOT compiled**: `sections/experiments.tex`, `sections/method.tex`, `sections/theoretical.tex` — stale versions with some inconsistencies.

---

### Audit Table

| # | Location (compiled file:line) | Paper Claim | Source Value | Source | Match? | Action |
|---|---|---|---|---|---|---|
| **A. Core positive results** | | | | | | |
| 1 | abstract.tex:8 | LP selection +1.39 pp on Few-NERD | +1.39 pp | experiments_main.tex Tab fewnerd; memory.md (LP Δ=+1.39) | ✅ | — |
| 2 | abstract.tex:8 | Holm-adjusted p=0.019 | Family-level (k=19): <0.019; **Global (k=57): 0.055** | appendix.tex:335 Holm table row 6 | ⚠️ MISLEADING | Abstract does not specify "selection family k=19". Global correction gives p_adj=0.055 (not significant). Suggest adding "selection family" qualifier |
| 3 | abstract.tex:8 | weighted voting +1.02–1.40 pp | +1.02 (SciERC LP-wt), +1.40 (FewNERD LP-wt) | experiments_main.tex Tab entity_construction | ✅ | — |
| 4 | abstract.tex:8 | cross-model ensembles +0.42 pp | +0.42 pp on SciERC, over LLaMA baseline | adaptive.tex:10 | ⚠️ AMBIGUOUS | Dataset (SciERC) and baseline (pure LLaMA, not greedy) unspecified in abstract. Limitations.tex:3 confirms "limited to one dataset (SciERC)" |
| 5 | abstract.tex:6 | AUROC 0.87 (frequency agreement) | 0.868 | appendix.tex:625 Tab self_verification | ✅ ROUNDED | Standard rounding 0.868→0.87 |
| 6 | abstract.tex:6 | AUROC 0.51 (self-evaluation) | 0.512 | mechanistic.tex:8; appendix.tex:620,632 | ✅ ROUNDED | Standard rounding 0.512→0.51 |
| 7 | abstract.tex:5 | 87.2% SQL degeneracy | 87.2% | memory.md Spider SQL data | ✅ | — |
| **B. Introduction** | | | | | | |
| 8 | introduction.tex:20 | ρ up to 0.45 | 0.451 (EM on CoNLL Qwen) | experiments_main.tex Tab quality_estimation | ✅ ROUNDED | 0.451→0.45 |
| 9 | introduction.tex:20 | AUROC up to 0.82 | 0.816 (EM on CoNLL Qwen) | experiments_main.tex Tab quality_estimation | ✅ ROUNDED | 0.816→0.82 |
| 10 | introduction.tex:26 | MRSC P(yes) separation 0.0006 | 0.0006 (0.5003 vs 0.4997) | appendix.tex:637 | ✅ | — |
| 11 | introduction.tex:27 | Supervised verifier AUC 0.923, +0.30 pp | AUC=0.923±0.002; +0.30 pp OOF | adaptive.tex:14-15; memory.md B2 OOF | ✅ | — |
| 12 | introduction.tex:34 | "via majority vote (+1.40 pp)" | **+1.40 is LP-weighted, not uniform MV** | experiments_main.tex Tab entity_construction: LP=+1.40, Unif=+0.74 | ❌ MISLABELED | "majority vote" implies uniform weighting. +1.40 is LP-weighted construction. Uniform MV is +0.74 pp. Abstract correctly says "weighted voting" |
| 13 | introduction.tex:34 | Holm p_adj=0.006 (construction) | <0.010 at k=10 family; 0.055 at k=57 global | appendix.tex Holm table row 22 | ✅ | Per-family correction, correctly labeled k=10 |
| 14 | introduction.tex:32 | RE ~44% zero-F1 | Need to verify | Not found in memory.md or registry | ❓ UNVERIFIED | RE zero-F1 rate not cross-referenced |
| **C. Mechanistic section** | | | | | | |
| 15 | mechanistic.tex:8 | ESJ AUROC 0.512 | 0.512 | appendix.tex:620,632 | ✅ | — |
| 16 | mechanistic.tex:12 | MRSC P(yes) 0.5003 vs 0.4997 | 0.5003 vs 0.4997 | appendix.tex:637 | ✅ | — |
| 17 | mechanistic.tex:17 | LSC centroid 0.759, greedy 0.779 | centroid=0.759, greedy=.794 | appendix.tex:616,622 | ❌ DISCREPANCY | mechanistic.tex says greedy=0.779, appendix table says greedy=0.794. **15 pp difference** |
| 18 | mechanistic.tex:17 | LSC entity conf 0.839, MV 0.837 | entity conf=0.839, MV=0.792 | appendix.tex:617,623 | ❌ DISCREPANCY | mechanistic.tex says MV=0.837, appendix tab says MV(θ=0.375)=0.792. **4.5 pp gap** |
| 19 | mechanistic.tex:20 | Frequency agreement AUROC=0.868 | 0.868 | appendix.tex:625 | ✅ | — |
| 20 | mechanistic.tex:24 | PLACEHOLDER: P0-1 probe results | AUROC=0.987 (FewNERD), 0.980 (CoNLL) | memory.md P0-1 section | ⚠️ NOT IN PAPER | Placeholder still present; results exist in memory.md but never written into paper |
| **D. Theory / Degeneracy** | | | | | | |
| 21 | theory.tex:28 | G_nd≈14.8 pp, α≈0.068, θ_crit=0.70 | 1 - 0.3/(14.8×0.068) = 0.70 | appendix.tex:1071 | ✅ | Math checks out |
| 22 | theory.tex:28 | D>70% → SC gain < 0.3 pp | Consistent with bound formula | appendix.tex Fig bound | ✅ | — |
| 23 | conclusion.tex:3 | c≈0.5 (oracle scaling) | c≈0.61 (FewNERD), c≈0.35 (SciERC) | theory.tex:11; memory.md | ✅ SUMMARY | Approximate average of 0.61 and 0.35 |
| **E. Experiments (compiled: experiments_main.tex)** | | | | | | |
| 24 | experiments_main.tex Tab fewnerd | SciERC: n=529, Greedy=.644, Degen=17.8% | — | Consistent across all mentions | ✅ | — |
| 25 | experiments_main.tex Tab fewnerd | CoNLL: n=2756, Degen=61.7% | — | Consistent across all mentions | ✅ | — |
| 26 | experiments_main.tex Tab fewnerd | FewNERD: n=32565, Degen=13.0% | — | memory.md 72B data shows different values for different regimes | ✅ | 13.0% is Qwen3-8B FT |
| 27 | experiments_main.tex Tab fewnerd | WNUT: n=1287, Degen=67.9% | — | Consistent | ✅ | — |
| 28 | experiments_main.tex:106 | 8B degen 17.8% vs 4B 10.4% on SciERC | — | Tab degeneracy (referenced) | ✅ | — |
| **F. Scaling (experiments_main.tex)** | | | | | | |
| 29 | experiments_main.tex Tab scale_comparison | 72B ZS SciERC: Greedy=.399, Degen=21.0%, LP ρ=.081 | .399, 21.0%, .081 | memory.md 72B table | ✅ | — |
| 30 | experiments_main.tex Tab scale_comparison | 72B ZS FewNERD: Greedy=.628, Degen=46.2%, VC ρ=.416 | .628, 46.2%, .416 | memory.md 72B table | ✅ | — |
| 31 | experiments_main.tex Tab scale_comparison | 72B ZS CoNLL: Greedy=.712, Degen=67.7%, LP ρ=-.002 | .712, 67.7%, -.002 | memory.md 72B table | ✅ | — |
| 32 | experiments_main.tex:118 | ZS LP-weighting necessary: SciERC +1.5 pp | +1.53 pp (p=0.008) | memory.md 72B table: LP Δ=+1.53 | ✅ ROUNDED | 1.53→1.5 |
| **G. Prescriptive** | | | | | | |
| 33 | experiments_main.tex Tab entity_construction | SciERC LP: .646±.002 → .656±.003, +1.02±0.49 pp, p=.004 | — | Self-consistent within table | ✅ | — |
| 34 | experiments_main.tex Tab entity_construction | FewNERD LP: .748 → .762±.005, +1.40±0.51 pp, p<.001 | — | Self-consistent within table | ✅ | — |
| 35 | experiments_main.tex Tab entity_construction | CoNLL Unif: .908 → .904, -0.39 pp, n.s. | — | Self-consistent | ✅ | — |
| **H. Adaptive section** | | | | | | |
| 36 | adaptive.tex:10 | Cross-model +0.42 pp, p<0.001, CI [0.27, 0.58] on SciERC | +0.42 pp | Holm table row 29: p<.001, p_adj=0.055 | ✅ | Baseline is "over pure LLaMA sampling" not greedy |
| 37 | adaptive.tex:15 | Verifier OOF: +1.28 SciERC, +0.55 CoNLL, +0.02 FewNERD | +1.28, +0.55, +0.02 | memory.md B2 OOF section | ✅ | memory.md: SciERC +1.28, CoNLL +0.55, FewNERD +0.02 |
| **I. Discussion** | | | | | | |
| 38 | discussion.tex:3 | ρ 0.043–0.667 | — | Need to verify range | ❓ UNVERIFIED | 0.043 source unclear; 0.667 likely within-instance ρ |
| 39 | discussion.tex:4 | T=1.2: degen 14.9%, LP ρ=0.225 | 14.9%, 0.225 | appendix.tex:1457 (T=1.2 row: 14.9) and :1441 (ρ=0.225) | ✅ | — |
| **J. Diagnostic (compiled)** | | | | | | |
| 40 | diagnostic.tex:8 | LP mean weight 0.78 | LP=0.8–0.9 in memory.md | memory.md E2v2 | ✅ APPROX | 0.78 is plausible mean across configs (LP ranges 0.8–0.9) |
| 41 | diagnostic.tex:8 | "structural signals receiving zero weight" | VC=0.1–0.2 in memory.md | memory.md E2v2 | ⚠️ IMPRECISE | VC is a structural signal with non-zero weight. Claim should be "SJ/FK/EM receive zero weight; VC receives small weight" or similar |
| **K. Temperature ablation** | | | | | | |
| 42 | appendix.tex:1414 | Tab t_degeneracy: seed=42, SciERC | — | Self-consistent | ✅ | Clearly labeled seed=42 |
| 43 | appendix.tex:1454-1457 | T=0.5: 41.4%, T=0.8: 23.8%, T=1.0: 17.8%, T=1.2: 14.9% | — | Internal table data | ✅ | — |
| **L. LP compression** | | | | | | |
| 44 | related_work.tex:11 | "median range 0.041 nats" | 0.042 nats at T=1.0 | appendix.tex:1456 Tab t_degeneracy | ⚠️ MINOR | 0.042 in table vs 0.041 in text. Rounding artifact |

---

### Summary of Flagged Issues

**Critical (❌)**:

1. **#12 — Introduction "majority vote (+1.40 pp)"**: The +1.40 pp is LP-weighted construction. Plain majority vote gives +0.74 pp. The abstract correctly says "weighted voting" but the introduction mislabels it. This affects the contribution claims.

2. **#17, #18 — Mechanistic section greedy/MV baselines**: `mechanistic.tex` reports greedy=0.779 and MV=0.837, but the appendix self-verification table (same experiment, Qwen2.5-7B FewNERD) shows greedy=0.794 and MV=0.792. These are significant discrepancies (1.5 pp and 4.5 pp respectively). Likely the mechanistic.tex numbers are from an older run or different model.

**Misleading (⚠️)**:

3. **#2 — Abstract Holm p=0.019 without family qualifier**: The global correction (k=57) gives p_adj=0.055, which does NOT survive α=0.05. The per-family value (k=19 → <0.019) is valid but the abstract omits the family size.

4. **#4 — Cross-model +0.42pp dataset/baseline ambiguity**: Abstract and introduction don't specify this is SciERC-only and compared to pure LLaMA (not greedy).

5. **#20 — P0-1 probe AUROC placeholder**: Memory.md records AUROC=0.987 (FewNERD) and 0.980 (CoNLL) for hidden state probes predicting entity correctness. A PLACEHOLDER comment exists in mechanistic.tex but the results were never written into the paper.

6. **#41 — "structural signals receiving zero weight"**: VC (a structural signal) has non-zero weight (0.1–0.2) in ensemble optimization per memory.md.

7. **#44 — LP median range 0.041 vs 0.042**: Minor rounding mismatch.

**Task-flagged items resolution**:

- **a. "+0.1pp over single-sample" vs "+0.4pp over greedy"**: NOT found in current compiled text. These claims appear to have been removed/rewritten in the current version.
- **b. Cross-model +0.42pp**: Confirmed on **SciERC** (not FewNERD), over **pure LLaMA baseline** (not greedy).
- **c. Probe AUROC two numbers**: The 0.987 (P0-1 probe) exists only in memory.md; the 0.920 likely refers to verifier AUC 0.923. Neither 0.987 nor 0.920 appears in the compiled paper. The PLACEHOLDER has not been filled.
- **d. Degeneracy definition**: Consistent throughout ("fraction of instances where all N samples yield identical F1").
- **e. Temperature ablation seed**: Clearly labeled seed=42 in appendix table. Uses SciERC only.

**Stale files note**: `sections/experiments.tex` (NOT compiled) falsely claims "survives Holm–Bonferroni at k=57" — the Holm table shows p_adj=0.055 at k=57, which does NOT survive. The compiled `experiments_main.tex` correctly reports per-family corrections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "uuid": "32e152a1-eedd-435b-a6d1-527a4953de6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ZEDapk7jiyKhNSgS4BeSM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8474,
      "cache_read_input_tokens": 90603,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8474
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 102_

Now I have sufficient data. Let me compile the full audit.

---

## Claim Audit Report

### Compiled files (per main.tex)
`sections/abstract.tex`, `sections/introduction.tex`, `sections/diagnostic.tex`, `sections/mechanistic.tex`, `sections/single_signal.tex`, `sections/adaptive.tex`, `sections/theory.tex`, `sections/experiments_main.tex`, `sections/background.tex`, `sections/discussion.tex`, `sections/conclusion.tex`, `sections/limitations.tex`, `sections/appendix.tex`

**NOT compiled**: `sections/experiments.tex`, `sections/method.tex`, `sections/theoretical.tex` — stale versions with some inconsistencies.

---

### Audit Table

| # | Location (compiled file:line) | Paper Claim | Source Value | Source | Match? | Action |
|---|---|---|---|---|---|---|
| **A. Core positive results** | | | | | | |
| 1 | abstract.tex:8 | LP selection +1.39 pp on Few-NERD | +1.39 pp | experiments_main.tex Tab fewnerd; memory.md (LP Δ=+1.39) | ✅ | — |
| 2 | abstract.tex:8 | Holm-adjusted p=0.019 | Family-level (k=19): <0.019; **Global (k=57): 0.055** | appendix.tex:335 Holm table row 6 | ⚠️ MISLEADING | Abstract does not specify "selection family k=19". Global correction gives p_adj=0.055 (not significant). Suggest adding "selection family" qualifier |
| 3 | abstract.tex:8 | weighted voting +1.02–1.40 pp | +1.02 (SciERC LP-wt), +1.40 (FewNERD LP-wt) | experiments_main.tex Tab entity_construction | ✅ | — |
| 4 | abstract.tex:8 | cross-model ensembles +0.42 pp | +0.42 pp on SciERC, over LLaMA baseline | adaptive.tex:10 | ⚠️ AMBIGUOUS | Dataset (SciERC) and baseline (pure LLaMA, not greedy) unspecified in abstract. Limitations.tex:3 confirms "limited to one dataset (SciERC)" |
| 5 | abstract.tex:6 | AUROC 0.87 (frequency agreement) | 0.868 | appendix.tex:625 Tab self_verification | ✅ ROUNDED | Standard rounding 0.868→0.87 |
| 6 | abstract.tex:6 | AUROC 0.51 (self-evaluation) | 0.512 | mechanistic.tex:8; appendix.tex:620,632 | ✅ ROUNDED | Standard rounding 0.512→0.51 |
| 7 | abstract.tex:5 | 87.2% SQL degeneracy | 87.2% | memory.md Spider SQL data | ✅ | — |
| **B. Introduction** | | | | | | |
| 8 | introduction.tex:20 | ρ up to 0.45 | 0.451 (EM on CoNLL Qwen) | experiments_main.tex Tab quality_estimation | ✅ ROUNDED | 0.451→0.45 |
| 9 | introduction.tex:20 | AUROC up to 0.82 | 0.816 (EM on CoNLL Qwen) | experiments_main.tex Tab quality_estimation | ✅ ROUNDED | 0.816→0.82 |
| 10 | introduction.tex:26 | MRSC P(yes) separation 0.0006 | 0.0006 (0.5003 vs 0.4997) | appendix.tex:637 | ✅ | — |
| 11 | introduction.tex:27 | Supervised verifier AUC 0.923, +0.30 pp | AUC=0.923±0.002; +0.30 pp OOF | adaptive.tex:14-15; memory.md B2 OOF | ✅ | — |
| 12 | introduction.tex:34 | "via majority vote (+1.40 pp)" | **+1.40 is LP-weighted, not uniform MV** | experiments_main.tex Tab entity_construction: LP=+1.40, Unif=+0.74 | ❌ MISLABELED | "majority vote" implies uniform weighting. +1.40 is LP-weighted construction. Uniform MV is +0.74 pp. Abstract correctly says "weighted voting" |
| 13 | introduction.tex:34 | Holm p_adj=0.006 (construction) | <0.010 at k=10 family; 0.055 at k=57 global | appendix.tex Holm table row 22 | ✅ | Per-family correction, correctly labeled k=10 |
| 14 | introduction.tex:32 | RE ~44% zero-F1 | Need to verify | Not found in memory.md or registry | ❓ UNVERIFIED | RE zero-F1 rate not cross-referenced |
| **C. Mechanistic section** | | | | | | |
| 15 | mechanistic.tex:8 | ESJ AUROC 0.512 | 0.512 | appendix.tex:620,632 | ✅ | — |
| 16 | mechanistic.tex:12 | MRSC P(yes) 0.5003 vs 0.4997 | 0.5003 vs 0.4997 | appendix.tex:637 | ✅ | — |
| 17 | mechanistic.tex:17 | LSC centroid 0.759, greedy 0.779 | centroid=0.759, greedy=.794 | appendix.tex:616,622 | ❌ DISCREPANCY | mechanistic.tex says greedy=0.779, appendix table says greedy=0.794. **15 pp difference** |
| 18 | mechanistic.tex:17 | LSC entity conf 0.839, MV 0.837 | entity conf=0.839, MV=0.792 | appendix.tex:617,623 | ❌ DISCREPANCY | mechanistic.tex says MV=0.837, appendix tab says MV(θ=0.375)=0.792. **4.5 pp gap** |
| 19 | mechanistic.tex:20 | Frequency agreement AUROC=0.868 | 0.868 | appendix.tex:625 | ✅ | — |
| 20 | mechanistic.tex:24 | PLACEHOLDER: P0-1 probe results | AUROC=0.987 (FewNERD), 0.980 (CoNLL) | memory.md P0-1 section | ⚠️ NOT IN PAPER | Placeholder still present; results exist in memory.md but never written into paper |
| **D. Theory / Degeneracy** | | | | | | |
| 21 | theory.tex:28 | G_nd≈14.8 pp, α≈0.068, θ_crit=0.70 | 1 - 0.3/(14.8×0.068) = 0.70 | appendix.tex:1071 | ✅ | Math checks out |
| 22 | theory.tex:28 | D>70% → SC gain < 0.3 pp | Consistent with bound formula | appendix.tex Fig bound | ✅ | — |
| 23 | conclusion.tex:3 | c≈0.5 (oracle scaling) | c≈0.61 (FewNERD), c≈0.35 (SciERC) | theory.tex:11; memory.md | ✅ SUMMARY | Approximate average of 0.61 and 0.35 |
| **E. Experiments (compiled: experiments_main.tex)** | | | | | | |
| 24 | experiments_main.tex Tab fewnerd | SciERC: n=529, Greedy=.644, Degen=17.8% | — | Consistent across all mentions | ✅ | — |
| 25 | experiments_main.tex Tab fewnerd | CoNLL: n=2756, Degen=61.7% | — | Consistent across all mentions | ✅ | — |
| 26 | experiments_main.tex Tab fewnerd | FewNERD: n=32565, Degen=13.0% | — | memory.md 72B data shows different values for different regimes | ✅ | 13.0% is Qwen3-8B FT |
| 27 | experiments_main.tex Tab fewnerd | WNUT: n=1287, Degen=67.9% | — | Consistent | ✅ | — |
| 28 | experiments_main.tex:106 | 8B degen 17.8% vs 4B 10.4% on SciERC | — | Tab degeneracy (referenced) | ✅ | — |
| **F. Scaling (experiments_main.tex)** | | | | | | |
| 29 | experiments_main.tex Tab scale_comparison | 72B ZS SciERC: Greedy=.399, Degen=21.0%, LP ρ=.081 | .399, 21.0%, .081 | memory.md 72B table | ✅ | — |
| 30 | experiments_main.tex Tab scale_comparison | 72B ZS FewNERD: Greedy=.628, Degen=46.2%, VC ρ=.416 | .628, 46.2%, .416 | memory.md 72B table | ✅ | — |
| 31 | experiments_main.tex Tab scale_comparison | 72B ZS CoNLL: Greedy=.712, Degen=67.7%, LP ρ=-.002 | .712, 67.7%, -.002 | memory.md 72B table | ✅ | — |
| 32 | experiments_main.tex:118 | ZS LP-weighting necessary: SciERC +1.5 pp | +1.53 pp (p=0.008) | memory.md 72B table: LP Δ=+1.53 | ✅ ROUNDED | 1.53→1.5 |
| **G. Prescriptive** | | | | | | |
| 33 | experiments_main.tex Tab entity_construction | SciERC LP: .646±.002 → .656±.003, +1.02±0.49 pp, p=.004 | — | Self-consistent within table | ✅ | — |
| 34 | experiments_main.tex Tab entity_construction | FewNERD LP: .748 → .762±.005, +1.40±0.51 pp, p<.001 | — | Self-consistent within table | ✅ | — |
| 35 | experiments_main.tex Tab entity_construction | CoNLL Unif: .908 → .904, -0.39 pp, n.s. | — | Self-consistent | ✅ | — |
| **H. Adaptive section** | | | | | | |
| 36 | adaptive.tex:10 | Cross-model +0.42 pp, p<0.001, CI [0.27, 0.58] on SciERC | +0.42 pp | Holm table row 29: p<.001, p_adj=0.055 | ✅ | Baseline is "over pure LLaMA sampling" not greedy |
| 37 | adaptive.tex:15 | Verifier OOF: +1.28 SciERC, +0.55 CoNLL, +0.02 FewNERD | +1.28, +0.55, +0.02 | memory.md B2 OOF section | ✅ | memory.md: SciERC +1.28, CoNLL +0.55, FewNERD +0.02 |
| **I. Discussion** | | | | | | |
| 38 | discussion.tex:3 | ρ 0.043–0.667 | — | Need to verify range | ❓ UNVERIFIED | 0.043 source unclear; 0.667 likely within-instance ρ |
| 39 | discussion.tex:4 | T=1.2: degen 14.9%, LP ρ=0.225 | 14.9%, 0.225 | appendix.tex:1457 (T=1.2 row: 14.9) and :1441 (ρ=0.225) | ✅ | — |
| **J. Diagnostic (compiled)** | | | | | | |
| 40 | diagnostic.tex:8 | LP mean weight 0.78 | LP=0.8–0.9 in memory.md | memory.md E2v2 | ✅ APPROX | 0.78 is plausible mean across configs (LP ranges 0.8–0.9) |
| 41 | diagnostic.tex:8 | "structural signals receiving zero weight" | VC=0.1–0.2 in memory.md | memory.md E2v2 | ⚠️ IMPRECISE | VC is a structural signal with non-zero weight. Claim should be "SJ/FK/EM receive zero weight; VC receives small weight" or similar |
| **K. Temperature ablation** | | | | | | |
| 42 | appendix.tex:1414 | Tab t_degeneracy: seed=42, SciERC | — | Self-consistent | ✅ | Clearly labeled seed=42 |
| 43 | appendix.tex:1454-1457 | T=0.5: 41.4%, T=0.8: 23.8%, T=1.0: 17.8%, T=1.2: 14.9% | — | Internal table data | ✅ | — |
| **L. LP compression** | | | | | | |
| 44 | related_work.tex:11 | "median range 0.041 nats" | 0.042 nats at T=1.0 | appendix.tex:1456 Tab t_degeneracy | ⚠️ MINOR | 0.042 in table vs 0.041 in text. Rounding artifact |

---

### Summary of Flagged Issues

**Critical (❌)**:

1. **#12 — Introduction "majority vote (+1.40 pp)"**: The +1.40 pp is LP-weighted construction. Plain majority vote gives +0.74 pp. The abstract correctly says "weighted voting" but the introduction mislabels it. This affects the contribution claims.

2. **#17, #18 — Mechanistic section greedy/MV baselines**: `mechanistic.tex` reports greedy=0.779 and MV=0.837, but the appendix self-verification table (same experiment, Qwen2.5-7B FewNERD) shows greedy=0.794 and MV=0.792. These are significant discrepancies (1.5 pp and 4.5 pp respectively). Likely the mechanistic.tex numbers are from an older run or different model.

**Misleading (⚠️)**:

3. **#2 — Abstract Holm p=0.019 without family qualifier**: The global correction (k=57) gives p_adj=0.055, which does NOT survive α=0.05. The per-family value (k=19 → <0.019) is valid but the abstract omits the family size.

4. **#4 — Cross-model +0.42pp dataset/baseline ambiguity**: Abstract and introduction don't specify this is SciERC-only and compared to pure LLaMA (not greedy).

5. **#20 — P0-1 probe AUROC placeholder**: Memory.md records AUROC=0.987 (FewNERD) and 0.980 (CoNLL) for hidden state probes predicting entity correctness. A PLACEHOLDER comment exists in mechanistic.tex but the results were never written into the paper.

6. **#41 — "structural signals receiving zero weight"**: VC (a structural signal) has non-zero weight (0.1–0.2) in ensemble optimization per memory.md.

7. **#44 — LP median range 0.041 vs 0.042**: Minor rounding mismatch.

**Task-flagged items resolution**:

- **a. "+0.1pp over single-sample" vs "+0.4pp over greedy"**: NOT found in current compiled text. These claims appear to have been removed/rewritten in the current version.
- **b. Cross-model +0.42pp**: Confirmed on **SciERC** (not FewNERD), over **pure LLaMA baseline** (not greedy).
- **c. Probe AUROC two numbers**: The 0.987 (P0-1 probe) exists only in memory.md; the 0.920 likely refers to verifier AUC 0.923. Neither 0.987 nor 0.920 appears in the compiled paper. The PLACEHOLDER has not been filled.
- **d. Degeneracy definition**: Consistent throughout ("fraction of instances where all N samples yield identical F1").
- **e. Temperature ablation seed**: Clearly labeled seed=42 in appendix table. Uses SciERC only.

**Stale files note**: `sections/experiments.tex` (NOT compiled) falsely claims "survives Holm–Bonferroni at k=57" — the Holm table shows p_adj=0.055 at k=57, which does NOT survive. The compiled `experiments_main.tex` correctly reports per-family corrections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 373263,
  "duration_api_ms": 372179,
  "num_turns": 41,
  "stop_reason": "end_turn",
  "session_id": "6f03df03-75c2-4c8b-aba0-dbf6cd70c3b2",
  "total_cost_usd": 1.41166625,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 107807,
    "cache_read_input_tokens": 461961,
    "output_tokens": 20207,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 107807,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 10926,
        "cache_read_input_tokens": 90603,
        "cache_creation_input_tokens": 8474,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8474
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1582,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001652,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 20207,
      "cacheReadInputTokens": 461961,
      "cacheCreationInputTokens": 107807,
      "webSearchRequests": 0,
      "costUSD": 1.41001425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e908ba13-4cff-4da9-86a4-84258cec9db4"
}
```

</details>

---
