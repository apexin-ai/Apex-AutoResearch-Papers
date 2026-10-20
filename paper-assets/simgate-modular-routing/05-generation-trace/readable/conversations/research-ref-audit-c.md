# research ref audit C

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 259
- **Recorded user turns:** 0
- **Tool calls:** 129
- **Original source:** `logs/chats/worker_research_ref-audit-C_20260526T101534.jsonl`
- **Structured JSON:** [`7e6df6cec460e7bae399.json`](../../sessions/7e/7e6df6cec460e7bae399.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

259 recorded events

### Tool call

_source line 1 · 2026-05-26T10:26:36.689654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:26:36.690455+00:00_

1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
5	  year={2022}
6	}
7	
8	@inproceedings{react-2023,
9	  title={ReAct: Synergizing Reasoning and Acting in Language Models},
10	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2023}
13	}
14	
15	@inproceedings{toolformer-2023,
16	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
17	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
18	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
19	  year={2023}
20	}
21	
22	@article{art-2023,
23	  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
24	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
25	  journal={arXiv preprint arXiv:2303.09014},
26	  year={2023}
27	}
28	
29	@inproceedings{chameleon-2023,
30	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
31	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{retool-2025,
37	  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
38	  author={Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others},
39	  j
…[truncated 20832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:26:36.690813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex | sort -u",
  "description": "Extract all cite keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/*.tex | sort -u",
    "description": "Extract all cite keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:26:36.691187+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{alfworld-2021}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{gemma2-2024}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{llama3-2024}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{math-2021}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{natarajan2013learning}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex:\citep{reflexion-2023}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex:\citep{art-2023,chameleon-2023}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex:\citep{cogrouter-2026,ares-2026}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex:\citep{mtrouter-2026,budget-aware-routing-2026}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex:\citep{scienceworld-2022}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex:\citep{toolformer-2023}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:\citep{cameron-2008,webb-2023}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:\citep{math-2021}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:\citep{qwen25-2024}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex:\citep{react-2023}
/hom
…[truncated 6021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:26:36.691563+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 6 · 2026-05-26T10:26:36.691816+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:26:36.692157+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 1",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n1. scienceworld-2022\nTitle: ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\nAuthors: Wang, Ruoyao and Jansen, Peter and Côté, Marc-Alexandre and Ammanabrolu, Prithviraj\nVenue: EMNLP 2022\nYear: 2022\n\n2. react-2023\nTitle: ReAct: Synergizing Reasoning and Acting in Language Models\nAuthors: Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan\nVenue: ICLR 2023\nYear: 2023\n\n3. toolformer-2023\nTitle: Toolformer: Language Models Can Teach Themselves to Use Tools\nAuthors: Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas\nVenue: NeurIPS 2023\nYear: 2023\n\n4. art-2023\nTitle: ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\nAuthors: Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio\nJournal: arXiv preprint arXiv:2303.09014\nYear: 2023\n\n5. chameleon-2023\nTitle: Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\nAuthors: Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng\nVenue: NeurIPS 2023\nYear: 2023\n\n6. retool-2025\nTitle: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\nAuthors: Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others\nJournal: arXiv preprint arXiv:2504.11536\nYear: 2025\n\n7. cogrouter-2026\nTitle: Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\nAuthors: Yang, Ruihan and Ye, Fanghua and Wei, Xiang and Zhao, Ruoqing and Luo, Kang and others\nJournal: arXiv preprint arXiv:2602.12662\nYear: 2026\n\n8. ares-2026\nTitle: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\nAuthors: Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu and others\nJournal: arXiv preprint arXiv:2603.07915\nYear: 2026\n\n9. mixture-of-recursions-2025\nTitle: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\nAuthors: Bae, Sangmin and Kim, Yujin and Bayat, Reza and Kim, Sungnyun and Ha, Jiyoun and others\nVenue: NeurIPS 2025\nYear: 2025\n\n10. mtrouter-2026\nTitle: MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\nAuthors: Zhang, Yiqun and Li, Hao and Wang, Zihan and Feng, Shi and Yang, Xiaocui and others\nVenue: ACL 2026\nYear: 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 1",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n1. scienceworld-2022\nTitle: ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\nAuthors: Wang, Ruoyao and Jansen, Peter and Côté, Marc-Alexandre and Ammanabrolu, Prithviraj\nVenue: EMNLP 2022\nYear: 2022\n\n2. react-2023\nTitle: ReAct: Synergizing Reasoning and Acting in Language Models\nAuthors: Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan\nVenue: ICLR 2023\nYear: 2023\n\n3. toolformer-2023\nTitle: Toolformer: Language Models Can Teach Themselves to Use Tools\nAuthors: Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas\nVenue: NeurIPS 2023\nYear: 2023\n\n4. art-2023\nTitle: ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\nAuthors: Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio\nJournal: arXiv preprint arXiv:2303.09014\nYear: 2023\n\n5. chameleon-2023\nTitle: Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\nAuthors: Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng\nVenue: NeurIPS 2023\nYear: 2023\n\n6. retool-2025\nTitle: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\nAuthors: Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others\nJournal: arXiv preprint arXiv:2504.11536\nYear: 2025\n\n7. cogrouter-2026\nTitle: Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\nAuthors: Yang, Ruihan and Ye, Fanghua and Wei, Xiang and Zhao, Ruoqing and Luo, Kang and others\nJournal: arXiv preprint arXiv:2602.12662\nYear: 2026\n\n8. ares-2026\nTitle: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\nAuthors: Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu and others\nJournal: arXiv preprint arXiv:2603.07915\nYear: 2026\n\n9. mixture-of-recursions-2025\nTitle: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\nAuthors: Bae, Sangmin and Kim, Yujin and Bayat, Reza and Kim, Sungnyun and Ha, Jiyoun and others\nVenue: NeurIPS 2025\nYear: 2025\n\n10. mtrouter-2026\nTitle: MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\nAuthors: Zhang, Yiqun and Li, Hao and Wang, Zihan and Feng, Shi and Yang, Xiaocui and others\nVenue: ACL 2026\nYear: 2026"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:26:36.692695+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 9 · 2026-05-26T10:26:36.692950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:26:36.693209+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? Wang Jansen EMNLP 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? Wang Jansen EMNLP 2022"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:26:36.693447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReAct: Synergizing Reasoning and Acting in Language Models Yao Zhao ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReAct: Synergizing Reasoning and Acting in Language Models Yao Zhao ICLR 2023"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:26:36.693634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Toolformer: Language Models Can Teach Themselves to Use Tools Schick NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Toolformer: Language Models Can Teach Themselves to Use Tools Schick NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:26:36.693779+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models Paranjape arXiv 2303.09014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models Paranjape arXiv 2303.09014"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:26:36.693916+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models Lu Peng NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models Lu Peng NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:26:36.694109+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs Feng arXiv 2504.11536"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs Feng arXiv 2504.11536"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:26:36.694253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\" Yang arXiv 2602.12662"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\" Yang arXiv 2602.12662"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:26:36.694405+00:00_

Web search results for query: "ReAct: Synergizing Reasoning and Acting in Language Models Yao Zhao ICLR 2023"

Links: [{"title":"[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://arxiv.org/abs/2210.03629"},{"title":"GitHub - ysymyth/ReAct: [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models · GitHub","url":"https://github.com/ysymyth/ReAct"},{"title":"REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models | OpenReview","url":"https://openreview.net/forum?id=WE_vluYUL-X"},{"title":"Yao, S.Y., Zhao, J., Yu, D., et al. (2023) React Synergizing Reasoning and Acting in Language Models. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3984197"},{"title":"ICLR 2023 ReAct: Synergizing Reasoning and Acting in Language Models Oral","url":"https://iclr.cc/virtual/2023/oral/12647"},{"title":"ReAct: Synergizing Reasoning and Acting in Language ...","url":"https://arxiv.org/pdf/2210.03629"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://react-lm.github.io/"}]

I found comprehensive information about this paper. Here's what I found:

## ReAct: Synergizing Reasoning and Acting in Language Models

The paper was authored by Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao, and was published at the International Confe
…[truncated 1440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:26:36.694661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\" Yang Hou arXiv 2603.07915"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\" Yang Hou arXiv 2603.07915"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:26:36.694921+00:00_

Web search results for query: "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? Wang Jansen EMNLP 2022"

Links: [{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.775/"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"[PDF] ScienceWorld: Is your Agent Smarter than a 5th Grader? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ScienceWorld:-Is-your-Agent-Smarter-than-a-5th-Wang-Jansen/0e41fd22d483047bd8fdb1757d90c7702493567e"},{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5","url":"https://aclanthology.org/2022.emnlp-main.775.pdf"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? | Request PDF","url":"https://www.researchgate.net/publication/372924838_ScienceWorld_Is_your_Agent_Smarter_than_a_5th_Grader"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/scienceworld-is-your-agent-smarter-than-a-5th-grader/"},{"title":"GitHub - allenai/ScienceWorld: ScienceWorld is a text-based virtual environment centered around accomplishing tasks from the standardized elementary science curriculum. · GitHub","url":"https://github.com/allenai/ScienceWorld"},{"title":"Paper page - ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://huggingface.co/papers/2203.07540"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://www.arxiv-vanity.com/papers/2203.07540/"}]

I found the research paper you're looking for. Here are the key details:

The paper is authored by Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu, and was published in the Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 11279–11298, Abu Dhabi, United Arab Emirates.

The paper presents ScienceWorld, a benchma
…[truncated 1080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:26:36.695215+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation Bae Kim NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation Bae Kim NeurIPS 2025"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:26:36.695482+00:00_

Web search results for query: "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models Paranjape arXiv 2303.09014"

Links: [{"title":"[2303.09014] ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/abs/2303.09014"},{"title":"[PDF] ART: Automatic multi-step reasoning and tool-use for large language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ART:-Automatic-multi-step-reasoning-and-tool-use-Paranjape-Lundberg/0d42221038c05cee8443c5b5af838505ee137dc3"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://blog.athina.ai/art-automatic-multi-step-reasoning-and-tool-use-for-large-language-models"},{"title":"ART: Automatic multi-step reasoning and tool-use for large ...","url":"https://www.summarizepaper.com/en/arxiv-id/2303.09014v1/"},{"title":"[2303.09014v1] ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/abs/2303.09014v1"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/pdf/2303.09014v1"},{"title":"Paper page - ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://huggingface.co/papers/2303.09014"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230309014P/abstract"}]

Based on the search results, here's what I found about the paper:

## ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models

This paper was authored by Bhargavi Paranjape, Scott Lundberg, Sameer Singh, Hannaneh Hajishirzi, Luke Zettlemoyer, and Marco Tulio Ribeiro, and was submitted to arXiv on March 16, 2023.

### Overview
ART is a framework that uses frozen LLMs to automatically generate intermediate reasoning steps as a program. Given a new task to solve, ART selects demonstrations of multi-step re
…[truncated 853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:26:36.695738+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\" Zhang Li ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\" Zhang Li ACL 2026"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:26:36.695978+00:00_

Web search results for query: "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs Feng arXiv 2504.11536"

Links: [{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/pdf/2504.11536"},{"title":"Paper page - ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://huggingface.co/papers/2504.11536"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Request PDF","url":"https://www.researchgate.net/publication/390845884_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs"},{"title":"[PDF] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReTool:-Reinforcement-Learning-for-Strategic-Tool-Feng-Huang/8402e446158252992b6ddf1ff1b0658c39d7604e"},{"title":"[2504.11536v1] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536v1"},{"title":"[2504.11536v2] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"http://arxiv.org/abs/2504.11536v2"}]

I found the paper! Here's information about **ReTool: Reinforcement Learning for Strategic Tool Use in LLMs**:

The paper was submitted on April 15, 2025, with the latest version on April 17, 2025, authored by Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin Chi, and Wanjun Zhong.

**Key Problem:** While reasoning models (e.g., DeepSeek R1) trained with reinforcement learning excel in textual reasoning, they struggle in scenarios requiring structured problem-solving, such as geometric reasoning, concise computation, or complex equation solving—areas where computational tools like code interpreters demonstrate distinct advantages.

**Main Contributions:** ReTool enhances long-form reasoning with tool-integrated learn
…[truncated 665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:26:36.696323+00:00_

Web search results for query: "Toolformer: Language Models Can Teach Themselves to Use Tools Schick NeurIPS 2023"

Links: [{"title":"[2302.04761] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://arxiv.org/abs/2302.04761"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | OpenReview","url":"https://openreview.net/forum?id=Yacmpz84TH"},{"title":"NeurIPS Poster Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://neurips.cc/virtual/2023/poster/71288"},{"title":"[PDF] Toolformer: Language Models Can Teach Themselves to Use Tools | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toolformer:-Language-Models-Can-Teach-Themselves-to-Schick-Dwivedi-Yu/53d128ea815bcc0526856eb5a9c42cc977cb36a7"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://openreview.net/pdf?id=Yacmpz84TH"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://arxiv.org/pdf/2302.04761"},{"title":"Timo_schick Toolformer Language Models Can Teach Themselves to Use Tools 2023 | Sukai Huang","url":"https://sino-huang.github.io/posts/timo_schick-toolformer-language-models-can-teach-themselves-to-use-tools-2023/"},{"title":"[Quick Review] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://liner.com/review/toolformer-language-models-can-teach-themselves-to-use-tools"}]

I found the paper you're looking for! Here's what I found:

**Toolformer: Language Models Can Teach Themselves to Use Tools** is a paper by Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom, presented at NeurIPS 2023.

**Key Details:**

- **Main Contribution:*
…[truncated 1129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:26:36.696618+00:00_

Web search results for query: "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models Lu Peng NeurIPS 2023"

Links: [{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/871ed095b734818cfba48db6aeb25a62-Abstract-Conference.html"},{"title":"[2304.09842] Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://arxiv.org/abs/2304.09842"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://lupantech.github.io/papers/neurips23_chameleon.pdf"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://chameleon-llm.github.io/"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"http://web.cs.ucla.edu/~kwchang/bibliography/lu2023chameleon/"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/chameleon-plug-and-play-compositional-reasoning-with-large-language-models/"},{"title":"[PDF] Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chameleon:-Plug-and-Play-Compositional-Reasoning-Lu-Peng/170c97c7215f42edfb20c2248f954879e91ef86e"},{"title":"GitHub - lupantech/chameleon-llm: Codes for \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\".","url":"https://github.com/lupantech/chameleon-llm"}]

I found comprehensive information about this paper. Here's what the search revealed:

## Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models

**Authors and Venue:** Pan Lu, Baolin Peng, Hao Cheng, Michel Galley, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, and Jianfeng Gao from University of California, Los Angeles and Microsoft Research, Redmond
…[truncated 996 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:26:36.696936+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 2",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n11. tool-overuse-illusion-2026\nTitle: The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\nAuthors: Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting\nJournal: arXiv preprint arXiv:2604.19749\nYear: 2026\n\n12. when2tool-2026\nTitle: LLM Agents Already Know When to Call Tools -- Even Without Reasoning\nAuthors: Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\nJournal: arXiv preprint arXiv:2605.09252\nYear: 2026\n\n13. tool-use-tax-2026\nTitle: Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\nAuthors: Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying\nJournal: arXiv preprint arXiv:2605.00136\nYear: 2026\n\n14. to-call-or-not-2026\nTitle: To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\nAuthors: Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal\nJournal: arXiv preprint arXiv:2605.00737\nYear: 2026\n\n15. dagger-2011\nTitle: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\nAuthors: Ross, Stéphane and Gordon, Geoffrey J and Bagnell, Drew\nVenue: AISTATS 2011\nYear: 2011\n\n16. toolkengpt-2023\nTitle: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\nAuthors: Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\nVenue: NeurIPS 2023\nYear: 2023\n\n17. alfworld-2021\nTitle: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\nAuthors: Shridhar, Mohit and Yuan, Xingdi and Côté, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew\nVenue: ICLR 2021\nYear: 2021\n\n18. garcia2015comprehensive\nTitle: A Comprehensive Survey on Safe Reinforcement Learning\nAuthors: García, Javier and Fernández, Fernando\nJournal: Journal of Machine Learning Research, vol 16(1), pp 1437-1480\nYear: 2015\n\n19. amitai2024explaining\nTitle: Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\nAuthors: Amitai, Yotam and Septon, Guy and Amir, Ofra\nVenue: AAAI 2024\nYear: 2024\n\n20. gajcin2023counterfactual\nTitle: Counterfactual Explanations for Reinforcement Learning Agents\nAuthors: Gajcin, Jasmina\nVenue: AAMAS 2023\nYear: 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 2",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n11. tool-overuse-illusion-2026\nTitle: The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\nAuthors: Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting\nJournal: arXiv preprint arXiv:2604.19749\nYear: 2026\n\n12. when2tool-2026\nTitle: LLM Agents Already Know When to Call Tools -- Even Without Reasoning\nAuthors: Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\nJournal: arXiv preprint arXiv:2605.09252\nYear: 2026\n\n13. tool-use-tax-2026\nTitle: Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\nAuthors: Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying\nJournal: arXiv preprint arXiv:2605.00136\nYear: 2026\n\n14. to-call-or-not-2026\nTitle: To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\nAuthors: Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal\nJournal: arXiv preprint arXiv:2605.00737\nYear: 2026\n\n15. dagger-2011\nTitle: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\nAuthors: Ross, Stéphane and Gordon, Geoffrey J and Bagnell, Drew\nVenue: AISTATS 2011\nYear: 2011\n\n16. toolkengpt-2023\nTitle: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\nAuthors: Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\nVenue: NeurIPS 2023\nYear: 2023\n\n17. alfworld-2021\nTitle: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\nAuthors: Shridhar, Mohit and Yuan, Xingdi and Côté, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew\nVenue: ICLR 2021\nYear: 2021\n\n18. garcia2015comprehensive\nTitle: A Comprehensive Survey on Safe Reinforcement Learning\nAuthors: García, Javier and Fernández, Fernando\nJournal: Journal of Machine Learning Research, vol 16(1), pp 1437-1480\nYear: 2015\n\n19. amitai2024explaining\nTitle: Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\nAuthors: Amitai, Yotam and Septon, Guy and Amir, Ofra\nVenue: AAAI 2024\nYear: 2024\n\n20. gajcin2023counterfactual\nTitle: Counterfactual Explanations for Reinforcement Learning Agents\nAuthors: Gajcin, Jasmina\nVenue: AAMAS 2023\nYear: 2023"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:26:36.697553+00:00_

Web search results for query: ""Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents" Yang arXiv 2602.12662"

Links: [{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"[2602.12662v1] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive"},{"title":"Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/html/2505.21097"},{"title":"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens","url":"https://arxiviq.substack.com/p/think-deep-not-just-long-measuring"}]

I found the paper you're looking for! Here's what I found:

**"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents"** (arXiv 2602.12662)

This paper addresses how large language models are increasingly deployed as autonomous agents for multi-turn decision-making tasks. The authors identify that current agents rely on fixed cognitive patterns—non-thinking models generate immediate responses while thinking models engage in deep reasoning uniformly—which is inefficient for long-horizon tasks where cognitive demands vary significantly from step to step.

The paper introduces CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step, grounded in ACT-R theory, with four hierarchical cognitive levels ranging from instinctive responses to strategic planning.

Their training approach includes two stages: Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level 
…[truncated 290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:26:36.697849+00:00_

Web search results for query: ""MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings" Zhang Li ACL 2026"

Links: [{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"GitHub - ZhangYiqun018/MTRouter: [ACL 2026] Official implementation of MTRouter, a cost-aware multi-turn LLM routing framework accepted to ACL 2026 Main Conference. · GitHub","url":"https://github.com/ZhangYiqun018/MTRouter"},{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"Iterative Critique-and-Routing Controller for Multi-Agent Systems with Heterogeneous LLMs","url":"https://arxiv.org/html/2605.08686v1"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"[2604.12385] From Myopic Selection to Long-Horizon Awareness: Sequential LLM Routing for Multi-Turn Dialogue","url":"https://arxiv.org/abs/2604.12385"},{"title":"Beyond the Monolith: How Multi-Model Routing Is Redefining LLM Orchestration in 2026 | Mindra Blog","url":"https://mindra.co/blog/multi-model-routing-llm-orchestration-2026"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.00136v2"}]

I found the paper you're searching for! Here's what I discovered:

MTRouter is a cost-aware multi-turn LLM routing framework that was accepted to the ACL 2026 Main Conference. However, I should note that the lead author is Yiqun Zhang, not "Zhang Li" as mentioned in your query.

**Overview of MTRouter:**

MTRouter encodes the interaction history and candidate models into joint history-model embeddings, and learns an outcome estimator from logged trajectories to predict turn-level model utility. The work studies cost-aware multi-turn LLM routing: selecting which model to invoke at each turn from a model pool, given a fixed
…[truncated 662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:26:36.698164+00:00_

Web search results for query: ""Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" Yang Hou arXiv 2603.07915"

Links: [{"title":"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/html/2603.07915v1"},{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.10788v3"},{"title":"Jingbo Yang | UC Santa Barbara","url":"https://kimperyang.github.io/"},{"title":"[2511.10788] From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/abs/2511.10788"},{"title":"e1: Learning Adaptive Control of Reasoning Effort","url":"https://arxiv.org/html/2510.27042v1"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"LLM-based Agentic Reasoning Frameworks: A Survey from Methods to Scenarios","url":"https://arxiv.org/html/2508.17692v1"}]

I found the paper you're looking for! Here's what I found about "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents":

## Overview

Ares is a framework that optimizes LLM agent efficiency by dynamically selecting appropriate reasoning effort levels based on task complexity.

## Key Problem and Solution

While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction. However, agents should reserve high reasoning effort for difficult steps like navigating complex website structures, while using lower-effort modes for simpler steps like opening a target URL.

## Methodology

Ares employs 
…[truncated 806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:26:36.698457+00:00_

Web search results for query: "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation Bae Kim NeurIPS 2025"

Links: [{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"[2507.10524] Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/abs/2507.10524"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | OpenReview","url":"https://openreview.net/forum?id=QuqsEIVWIG"},{"title":"NeurIPS Poster Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118085"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"},{"title":"(PDF) Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://www.researchgate.net/publication/393684588_Mixture-of-Recursions_Learning_Dynamic_Recursive_Depths_for_Adaptive_Token-Level_Computation"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/html/2507.10524v1"},{"title":"ICML Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Thinking","url":"https://icml.cc/virtual/2025/51797"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiviq.substack.com/p/mixture-of-recursions-learning-dynamic"},{"title":"mixture_of_recursions/README.md at main · raymin0223/mixture_of_recursions","url":"https://github.com/raymin0223/mixture_of_recursions/blob/main/README.md"}]

I found comprehensive information about this paper. Here's what I disco
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:26:36.698737+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.12662 \"Think Fast and Slow\" authors full list Yang Ruihan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.12662 \"Think Fast and Slow\" authors full list Yang Ruihan"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:26:36.698966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:26:36.699226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2504.11536 ReTool authors full list Jiazhan Feng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2504.11536 ReTool authors full list Jiazhan Feng"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:26:36.699442+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.23530 MTRouter authors full list Yiqun Zhang ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.23530 MTRouter authors full list Yiqun Zhang ACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-26T10:26:36.699665+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Toolformer NeurIPS 2023 authors list Eric Hambro"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Toolformer NeurIPS 2023 authors list Eric Hambro"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T10:26:36.699895+00:00_

Web search results for query: "arXiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"

Links: [{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=694&show=1000"},{"title":"Computation and Language Apr 2026","url":"https://arxiv.org/list/cs.CL/current?skip=35&show=2000"},{"title":"dblp: Yujia Bao","url":"https://dblp.org/pid/214/4122.html"},{"title":"Computation and Language","url":"https://www.arxiv.org/list/cs.CL/pastweek?skip=4&show=500"},{"title":"Computer Science Jan 2022","url":"https://arxiv.org/list/cs/2022-01?skip=230&show=2000"},{"title":"Computer Vision and Pattern Recognition","url":"https://web3.arxiv.org/list/cs.CV/recent?skip=145&show=500"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=1350&show=1000"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=1450&show=2000"}]

Based on the search results, the full list of authors for arXiv paper 2603.07915 "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" is: Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, and Shiyu Chang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:26:36.700204+00:00_

Web search results for query: "Toolformer NeurIPS 2023 authors list Eric Hambro"

Links: [{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html"},{"title":"NeurIPS Poster Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://neurips.cc/virtual/2023/poster/71288"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | Research - AI at Meta","url":"https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/"},{"title":"NeurIPS 2023 Orals","url":"https://nips.cc/virtual/2023/events/oral"},{"title":"NeurIPS Oral Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://nips.cc/virtual/2023/oral/73843"},{"title":"NeurIPS 2023 Toolformer: Language Models Can Teach Themselves to Use Tools Oral","url":"https://neurips.cc/virtual/2023/oral/73843"},{"title":"Eric Hambro","url":"https://scholar.google.com/citations?user=ehquBPIAAAAJ&hl=en"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | OpenReview","url":"https://openreview.net/forum?id=Yacmpz84TH"},{"title":"Track: Oral 3B NLP/Tools","url":"https://neurips.cc/virtual/2023/session/74043"},{"title":"dblp: Eric Hambro","url":"https://dblp.org/pid/290/1986.html"}]

Based on the search results, I found the authors list for the Toolformer paper presented at NeurIPS 2023:

The authors of "Toolformer: Language Models Can Teach Themselves to Use Tools" are Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. The paper was published in the Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track and was presented as an oral presentation at the conference.


REMINDER: You MUST include the sources above in your response to the user using markd
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T10:26:36.700486+00:00_

Web search results for query: "arXiv 2602.12662 "Think Fast and Slow" authors full list Yang Ruihan"

Links: [{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"[2602.12662v1] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive"},{"title":"Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/html/2505.21097v1"},{"title":"[1906.00855] Deep Reasoning Networks: Thinking Fast and Slow","url":"https://arxiv.org/abs/1906.00855"},{"title":"[2505.21097] Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/abs/2505.21097"},{"title":"[1704.07785] Thinking Fast and Slow: Optimization Decomposition Across Timescales","url":"https://arxiv.org/abs/1704.07785"},{"title":"[2010.06002] Thinking Fast and Slow in AI","url":"https://arxiv.org/abs/2010.06002"}]

Based on the search results, here is the full list of authors for the arXiv paper 2602.12662 "Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents":

Ruihan Yang, Fanghua Ye, Xiang Wei, Ruoqing Zhao, Kang Luo, Xinbo Xu, Bo Zhao, Ruotian Ma, Shanyi Wang, Zhaopeng Tu, Xiaolong Li, Deqing Yang, and Linus.

The authors are from Fudan University and Tencent Hunyuan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:26:36.700759+00:00_

Web search results for query: "arXiv 2504.11536 ReTool authors full list Jiazhan Feng"

Links: [{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536"},{"title":"Paper page - ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://huggingface.co/papers/2504.11536"},{"title":"[2504.11536v1] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536v1"},{"title":"[PDF] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReTool:-Reinforcement-Learning-for-Strategic-Tool-Feng-Huang/8402e446158252992b6ddf1ff1b0658c39d7604e"},{"title":"[2504.11536v2] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"http://arxiv.org/abs/2504.11536v2"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Request PDF","url":"https://www.researchgate.net/publication/390845884_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs"},{"title":"dblp: Jiazhan Feng","url":"https://dblp.org/pid/242/9191.html"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.11536v1?locale=en"},{"title":"Computation and Language 2025","url":"https://www.arxiv.org/list/cs.CL/2025?skip=4750&show=500"}]

Based on the search results, here is the full list of authors for the paper arXiv 2504.11536 "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs":

1. Jiazhan Feng
2. Shijue Huang
3. Xingwei Qu
4. Ge Zhang
5. Yujia Qin
6. Baoquan Zhong
7. Chengquan Jiang
8. Jinxin Chi
9. Wanjun Zhong

The paper was submitted on April 15, 2025, and last revised on April 17, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:26:36.701047+00:00_

Web search results for query: "arXiv 2604.23530 MTRouter authors full list Yiqun Zhang ACL 2026"

Links: [{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2604.10150"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=543&show=2000"},{"title":"Computation and Language Apr 2026","url":"https://arxiv.org/list/cs.CL/current?skip=35&show=2000"},{"title":"Publications | Yulun Zhang","url":"https://yulunzhang.com/publications/"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=1125&show=2000"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2800&show=2000"},{"title":"Computer Science Jan 2024","url":"https://arxiv.org/list/cs/2024-01?skip=195&show=2000"}]

Based on the search results, I found the paper you're looking for. Here is the full list of authors for arXiv paper 2604.23530 (MTRouter):

The authors are: Yiqun Zhang, Hao Li, Zihan Wang, Shi Feng, Xiaocui Yang, Daling Wang, Bo Zhang, Lei Bai, and Shuyue Hu.

The authors are affiliated with the School of Computer Science and Engineering at Northeastern University (Shenyang, China) and the Shanghai Artificial Intelligence Laboratory.

Regarding the ACL 2026 submission: The search results show that the paper was submitted to arXiv on April 26, 2026, but I did not find specific information in the search results confirming whether it has been accepted to or submitted to ACL 2026. You may want to check the paper directly on arXiv or the ACL 2026 conference website for the most current acceptance status.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:26:36.701332+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 42 · 2026-05-26T10:26:36.701561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:26:36.701791+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.19749 \"The Tool-Overuse Illusion\" LLM external tools internal knowledge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.19749 \"The Tool-Overuse Illusion\" LLM external tools internal knowledge"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:26:36.702043+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.09252 \"LLM Agents Already Know When to Call Tools\" Sun Chung-En"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.09252 \"LLM Agents Already Know When to Call Tools\" Sun Chung-En"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:26:36.702290+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.00136 \"Are Tools All We Need\" \"Tool-Use Tax\" LLM Agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.00136 \"Are Tools All We Need\" \"Tool-Use Tax\" LLM Agents"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:26:36.702529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.00737 \"To Call or Not to Call\" LLM Tool Calling Wu Qinyuan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.00737 \"To Call or Not to Call\" LLM Tool Calling Wu Qinyuan"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:26:36.702734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DAgger \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\" Ross Gordon Bagnell AISTATS 2011"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DAgger \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\" Ross Gordon Bagnell AISTATS 2011"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:26:36.702958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolkenGPT \"Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\" Hao Shibo NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolkenGPT \"Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\" Hao Shibo NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T10:26:36.703281+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ALFWorld \"Aligning Text and Embodied Environments for Interactive Learning\" Shridhar ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ALFWorld \"Aligning Text and Embodied Environments for Interactive Learning\" Shridhar ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T10:26:36.703515+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "García Fernández \"A Comprehensive Survey on Safe Reinforcement Learning\" JMLR 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "García Fernández \"A Comprehensive Survey on Safe Reinforcement Learning\" JMLR 2015"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:26:36.703766+00:00_

Web search results for query: "arXiv 2604.19749 "The Tool-Overuse Illusion" LLM external tools internal knowledge"

Links: [{"title":"[2604.19749] The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?","url":"https://arxiv.org/abs/2604.19749"},{"title":"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?","url":"https://arxiv.org/html/2604.19749"},{"title":"From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models","url":"https://arxiv.org/html/2511.10899v2"},{"title":"Thinking Isn’t an Illusion: Overcoming the Limitations of Reasoning Models via Tool Augmentations","url":"https://arxiv.org/html/2507.17699v1"},{"title":"Breaking the Illusion of Identity in LLM Tooling","url":"https://arxiv.org/html/2604.07398v1"},{"title":"Thinking Isn’t an Illusion: Overcoming the Limitations of","url":"https://arxiv.org/pdf/2507.17699"},{"title":"[2507.17699] Thinking Isn't an Illusion: Overcoming the Limitations of Reasoning Models via Tool Augmentations","url":"https://arxiv.org/abs/2507.17699"},{"title":"How Enhancing LLM Reasoning Amplifies Tool Hallucination","url":"https://arxiv.org/pdf/2510.22977"}]

I found the paper you're searching for! Here's what I found:

"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?" (arXiv:2604.19749) addresses how equipping LLMs with external tools addresses internal reasoning limitations, but introduces a critical phenomenon called tool overuse—the unnecessary use of tools during reasoning.

The paper reveals this phenomenon is pervasive across diverse LLMs. By analyzing tool-use behavior across different internal knowledge availability regions, the researchers identify a "knowledge epistemic illusion," where models misjudge internal knowledge boundaries and fail to accurately perceive their actual knowledge availability.

To address this, the authors propose a knowledge-aware epistemic boundary a
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-26T10:26:36.704071+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Amitai Septon Amir \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\" AAAI 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Amitai Septon Amir \"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\" AAAI 2024"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:26:36.704328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gajcin \"Counterfactual Explanations for Reinforcement Learning Agents\" AAMAS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gajcin \"Counterfactual Explanations for Reinforcement Learning Agents\" AAMAS 2023"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:26:36.704595+00:00_

Web search results for query: "DAgger "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning" Ross Gordon Bagnell AISTATS 2011"

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"},{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"[1011.0686] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://arxiv.org/abs/1011.0686"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) - HackMD","url":"https://hackmd.io/@XiNyAicATy2jGaBhGc2ZRg/r1a97tfCU"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.researchgate.net/publication/47646552_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No-RegretOnline_Learning"},{"title":"(PDF) A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.academia.edu/24009408/A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No_Regret_Online_Learning"},{"title":"A Reduction of Imitation Learning and Structure Prediction ...","url":"https://www.cl.uni-heidelberg.de/courses/ws18/iml/dagger.pdf"},{"title":"[PDF] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Reduction-of-Imitation-Learning-and-Structured-to-Ross-Gordon/79ab3c49903ec8cb339437ccf5cf998607fc313e"}]

I've found the paper you're looking for! Here are the key details:

**Paper Title:** "A Reduction of Imitation Learning and S
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:26:36.704894+00:00_

Web search results for query: "arXiv 2605.00136 "Are Tools All We Need" "Tool-Use Tax" LLM Agents"

Links: [{"title":"[2605.00136] Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/abs/2605.00136"},{"title":"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/html/2605.00136v1"},{"title":"The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration","url":"https://arxiv.org/html/2603.22862v2"},{"title":"Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback","url":"https://arxiv.org/html/2605.17453"},{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252"},{"title":"LLM Agents Already Know When to Call Tools","url":"https://lilywenglab.github.io/when2tool/"},{"title":"Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows","url":"https://arxiv.org/html/2604.21816v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.01498"}]

I found the paper! Here are the key details about arXiv paper 2605.00136:

**Title:** "Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents"

**Authors:** Kaituo Zhang, Zhen Xiong, Mingyu Zhong, Zhimeng Jiang, Zhouyuan Yuan, Zhecheng Li, Ying Lin

**Main Findings:**

While tool-augmented reasoning for LLM-based agents is widely assumed to improve reasoning and reliability, the consensus does not always hold: in the presence of semantic distractors, tool-augmented reasoning does not necessarily outperform native CoT.

**Key Contribution:**

The authors propose a Factorized Intervention Framework that isolates the cost of prompt formatting, the overhead of the tool-calling protocol, and the actual gain from executing tools.

**Critical Finding:**

Under semantic noise, the gains from tools often fail to offset the "tool-use tax", which is the per
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:26:36.705202+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 3",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n21. olson2021counterfactual\nTitle: Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\nAuthors: Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen\nJournal: Artificial Intelligence, vol 295, pp 103455\nYear: 2021\n\n22. routellm-2024\nTitle: RouteLLM: Learning to Route LLMs with Preference Data\nAuthors: Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tianhao and Gonzalez, Joseph E. and Kadous, M Waleed and Stoica, Ion\nJournal: arXiv preprint arXiv:2406.18665\nYear: 2024\n\n23. reflexion-2023\nTitle: Reflexion: Language Agents with Verbal Reinforcement Learning\nAuthors: Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu\nVenue: NeurIPS 2023\nYear: 2023\n\n24. tool-learning-survey-2024\nTitle: Tool Learning with Large Language Models: A Survey\nAuthors: Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqiang and Yin, Dawei and Xu, Jun and Wen, Ji-Rong\nJournal: arXiv preprint arXiv:2405.17935\nYear: 2024\n\n25. tot-2023\nTitle: Tree of Thoughts: Deliberate Problem Solving with Large Language Models\nAuthors: Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L and Cao, Yuan and Narasimhan, Karthik\nVenue: NeurIPS 2023\nYear: 2023\n\n26. agentbench-2024\nTitle: AgentBench: Evaluating LLMs as Agents\nAuthors: Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and Huang, Minlie and Zhang, Yuxiao and Tang, Jie\nVenue: ICLR 2024\nYear: 2024\n\n27. lats-2024\nTitle: Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\nAuthors: Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong\nVenue: ICML 2024\nYear: 2024\n\n28. math-2021\nTitle: Measuring Mathematical Problem Solving With the MATH Dataset\nAuthors: Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob\nVenue: NeurIPS 2021 Datasets and Benchmarks Track\nYear: 2021\n\n29. qwen25-2024\nTitle: Qwen2.5 Technical Report\nAuthors: Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and others\nJournal: arXiv preprint arXiv:2412.15115\nYear: 2024\n\n30. llama3-2024\nTitle: The Llama 3 Herd of Models\nAuthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others\nJournal: arXiv preprint arXiv:2407.21783\nYear: 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 3",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n21. olson2021counterfactual\nTitle: Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\nAuthors: Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen\nJournal: Artificial Intelligence, vol 295, pp 103455\nYear: 2021\n\n22. routellm-2024\nTitle: RouteLLM: Learning to Route LLMs with Preference Data\nAuthors: Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tianhao and Gonzalez, Joseph E. and Kadous, M Waleed and Stoica, Ion\nJournal: arXiv preprint arXiv:2406.18665\nYear: 2024\n\n23. reflexion-2023\nTitle: Reflexion: Language Agents with Verbal Reinforcement Learning\nAuthors: Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu\nVenue: NeurIPS 2023\nYear: 2023\n\n24. tool-learning-survey-2024\nTitle: Tool Learning with Large Language Models: A Survey\nAuthors: Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqiang and Yin, Dawei and Xu, Jun and Wen, Ji-Rong\nJournal: arXiv preprint arXiv:2405.17935\nYear: 2024\n\n25. tot-2023\nTitle: Tree of Thoughts: Deliberate Problem Solving with Large Language Models\nAuthors: Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L and Cao, Yuan and Narasimhan, Karthik\nVenue: NeurIPS 2023\nYear: 2023\n\n26. agentbench-2024\nTitle: AgentBench: Evaluating LLMs as Agents\nAuthors: Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and Huang, Minlie and Zhang, Yuxiao and Tang, Jie\nVenue: ICLR 2024\nYear: 2024\n\n27. lats-2024\nTitle: Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\nAuthors: Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong\nVenue: ICML 2024\nYear: 2024\n\n28. math-2021\nTitle: Measuring Mathematical Problem Solving With the MATH Dataset\nAuthors: Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob\nVenue: NeurIPS 2021 Datasets and Benchmarks Track\nYear: 2021\n\n29. qwen25-2024\nTitle: Qwen2.5 Technical Report\nAuthors: Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and others\nJournal: arXiv preprint arXiv:2412.15115\nYear: 2024\n\n30. llama3-2024\nTitle: The Llama 3 Herd of Models\nAuthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others\nJournal: arXiv preprint arXiv:2407.21783\nYear: 2024"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:26:36.705670+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 Sangmin Bae venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 Sangmin Bae venue"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:26:36.705924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MTRouter ACL 2026 main conference accepted Zhang Yiqun"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MTRouter ACL 2026 main conference accepted Zhang Yiqun"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-26T10:26:36.706216+00:00_

Web search results for query: "arXiv 2605.09252 "LLM Agents Already Know When to Call Tools" Sun Chung-En"

Links: [{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v2"},{"title":"[2605.09252] LLM Agents Already Know When to Call Tools -- Even Without Reasoning","url":"https://arxiv.org/abs/2605.09252"},{"title":"LLM Agents Already Know When to Call Tools","url":"https://lilywenglab.github.io/when2tool/"},{"title":"GitHub - Trustworthy-ML-Lab/when2tool · GitHub","url":"https://github.com/Trustworthy-ML-Lab/when2tool"},{"title":"[2605.00737] To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/abs/2605.00737"},{"title":"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/html/2605.00136v1"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737v1"},{"title":"From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents","url":"https://arxiv.org/html/2605.15104"},{"title":"0.75686 0.33333 0.65882F0.64706 0.35294 0.68627i0.54118 0.37255 0.71765n0.43137 0.39216 0.7451T0.32549 0.41176 0.77647r0.21569 0.43137 0.80392a0.1098 0.45098 0.83529c0 0.47059 0.86275e\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:: Holistic Trajectory-Level Evaluation of LLM Tool Calling for Long-Horizon Financial Tasks","url":"https://arxiv.org/html/2604.10015"},{"title":"LLM-Based Agents for Tool Learning: A Survey | Data Science and Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41019-025-00296-9"}]

I found the paper! Here are the details about arXiv 2605.09252:

**Title:** "LLM Agents Already Know When to Call Tools - Even Without Reasoning"

**Author
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:26:36.706501+00:00_

Web search results for query: "arXiv 2605.00737 "To Call or Not to Call" LLM Tool Calling Wu Qinyuan"

Links: [{"title":"[2605.00737] To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/abs/2605.00737"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737v1"},{"title":"When2Call: When (not) to Call Tools","url":"https://arxiv.org/pdf/2504.18851"},{"title":"Tool Calling for Arabic LLMs: Data Strategies and Instruction Tuning","url":"https://arxiv.org/pdf/2509.20957"},{"title":"Achieving Tool Calling Functionality in LLMs Using Only Prompt   Engineering Without Fine-Tuning","url":"https://arxiv.org/pdf/2407.04997"},{"title":"ToolCaching: Towards Efficient Caching for LLM Tool-calling","url":"https://arxiv.org/pdf/2601.15335"},{"title":"Enhancing Function-Calling Capabilities in LLMs: Strategies for Prompt   Formats, Data Integration, and Multilingual Translation","url":"https://arxiv.org/pdf/2412.01130"},{"title":"Try, Check and Retry: A Divide-and-Conquer Framework for Boosting Long-context Tool-Calling Performance of LLMs","url":"https://arxiv.org/pdf/2603.11495"}]

I found the paper! Here's what I found:

The paper "To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling" is authored by Qinyuan Wu, Soumi Das, and others.

The paper addresses how agentic AI architectures augment LLMs with external tools to unlock strong capabilities. However, tool use is not always beneficial; some calls may be redundant or even harmful, and effective tool use hinges on a core LLM decision: whether to call or not call a tool, when performing a task.

This decision is particularly challenging for web search tools, where the benefits of external information depend on the model's internal knowledge and its ability to integrate potentially noisy tool responses. The paper introduces a principled framework inspired by decision-making theory to ev
…[truncated 260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:26:36.706791+00:00_

Web search results for query: "ToolkenGPT "Augmenting Frozen Language Models with Massive Tools via Tool Embeddings" Hao Shibo NeurIPS 2023"

Links: [{"title":"GitHub - Ber666/ToolkenGPT: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings - NeurIPS 2023 (oral)","url":"https://github.com/Ber666/ToolkenGPT"},{"title":"[2305.11554] ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://arxiv.org/abs/2305.11554"},{"title":"NeurIPS Poster ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://neurips.cc/virtual/2023/poster/72492"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://papers.nips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html"},{"title":"NeurIPS 2023 ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings Oral","url":"https://nips.cc/virtual/2023/oral/73868"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings | OpenReview","url":"https://openreview.net/forum?id=BHXsb69bSx"},{"title":"ToolkenGPT: Augmenting Frozen Language Models","url":"https://arxiv.org/pdf/2305.11554"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with ...","url":"https://openreview.net/pdf?id=BHXsb69bSx"},{"title":"Releases · Ber666/ToolkenGPT","url":"https://github.com/Ber666/ToolkenGPT/releases"}]

I found the paper you're looking for! Here's what I found:

"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings" is authored by Shibo Hao and 3 other authors, and it was presented at NeurIPS 2023 as an oral presentation.

**Key Concept:**
The key idea of ToolkenGPT is to represent each tool as a new token ("toolken") to augment the vocabulary. Specifically, each tool is associated with an embedding inserted into the LLM head like a regular word token emb
…[truncated 1276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T10:26:36.707108+00:00_

Web search results for query: "García Fernández "A Comprehensive Survey on Safe Reinforcement Learning" JMLR 2015"

Links: [{"title":"[PDF] A comprehensive survey on safe reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-comprehensive-survey-on-safe-reinforcement-Garc%C3%ADa-Fern%C3%A1ndez/c0f2c4104ef6e36bb67022001179887e6600d24d"},{"title":"(PDF) A comprehensive survey on safe reinforcement learning (2015) | Javier García | 1705 Citations","url":"https://scispace.com/papers/a-comprehensive-survey-on-safe-reinforcement-learning-3p8tg32zci"},{"title":"A comprehensive survey on safe reinforcement learning","url":"https://bibbase.org/network/publication/garcia-fernndez-acomprehensivesurveyonsafereinforcementlearning-2015"},{"title":"dblp: A comprehensive survey on safe reinforcement learning.","url":"https://dblp.org/rec/journals/jmlr/GarciaF15.html"},{"title":"A comprehensive survey on safe reinforcement learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/2789272.2886795"},{"title":"A comprehensive survey on safe reinforcement learning","url":"https://www.researchgate.net/publication/301361203_A_comprehensive_survey_on_safe_reinforcement_learning"},{"title":"A comprehensive survey on safe reinforcement learning | Documents - Universidade de Santiago de Compostela","url":"https://investigacion.usc.gal/documentos/61ff061313638e1cfc277281?lang=en"}]

I found the paper you're looking for. Here are the details:

The paper "A comprehensive survey on safe reinforcement learning" was authored by Javier García and Fernando Fernández and published in the Journal of Machine Learning Research in 2015, volume 16, pages 1437-1480.

Safe Reinforcement Learning is defined as the process of learning policies that maximize the expectation of the return in problems in which it is important to ensure reasonable system performance and/or respect safety constraints during the learning and/or deployment processes
…[truncated 385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-26T10:26:36.707424+00:00_

Web search results for query: "ALFWorld "Aligning Text and Embodied Environments for Interactive Learning" Shridhar ICLR 2021"

Links: [{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"ICLR Poster ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://iclr.cc/virtual/2021/poster/2973"},{"title":"[PDF] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ALFWorld:-Aligning-Text-and-Embodied-Environments-Shridhar-Yuan/398a0625e8707a0b41ac58eaec51e8feb87dd7cb"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://papertalk.org/papertalks/28910"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"alfworld - Overview","url":"https://github.com/alfworld/"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/alfworld-aligning-text-and-embodied-environments-for-interactive-learning/"},{"title":"(PDF) ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://www.researchgate.net/publication/344551961_ALFWorld_Aligning_Text_and_Embodied_Environments_for_Interactive_Learning"}]

I found comprehensive information about the ALFWorld paper. Here are the search results:

## ALFWorld: Aligning Text and Embodied Environments for Interactive Learning

**Citation:** Authors: Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew Hausknecht. P
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:26:36.707716+00:00_

Web search results for query: "Gajcin "Counterfactual Explanations for Reinforcement Learning Agents" AAMAS 2023"

Links: [{"title":"Counterfactual Explanations for Reinforcement Learning Agents","url":"https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p2925.pdf"},{"title":"Counterfactual Explanations for Reinforcement Learning Agents | Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems","url":"https://dl.acm.org/doi/abs/10.5555/3545946.3599126"},{"title":"GitHub - hcmlab/GANterfactual-RL: Counterfactual explanations for Reinforcement Learning agents on Atari","url":"https://github.com/hcmlab/GANterfactual-RL"},{"title":"GitHub - Allenpandas/2023-Reinforcement-Learning-Conferences-Papers: The proceedings of top conference in 2023 on the topic of Reinforcement Learning (RL), including: AAAI, IJCAI, NeurIPS, ICML, ICLR, ICRA, AAMAS and more. · GitHub","url":"https://github.com/Allenpandas/2023-Reinforcement-Learning-Conferences-Papers"},{"title":"Counterfactual Explanations for Reinforcement Learning Agents","url":"https://www.southampton.ac.uk/~eg/AAMAS2023/pdfs/p2925.pdf"},{"title":"GANterfactual-RL: Understanding Reinforcement Learning Agents'   Strategies through Visual Counterfactual Explanations","url":"https://arxiv.org/pdf/2302.12689"},{"title":"Counterfactual Explanations for Continuous Action Reinforcement Learning","url":"https://arxiv.org/pdf/2505.12701"}]

I found the paper you're looking for! Jasmina Gajcin published "Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium" in 2023 at the 22nd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023), held in London, United Kingdom, May 29 – June 2, 2023.

The approach generates contrastive explanations about two policies by analysing the state space in which policies disagree on the best course of action due to the difference in their preference. The paper is available through the IFAAMAS proceedings.


REMINDE
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:26:36.708024+00:00_

Web search results for query: "Amitai Septon Amir "Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes" AAAI 2024"

Links: [{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/explaining-reinforcement-learning-agents-through-counterfactual-a"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes","url":"https://ojs.aaai.org/index.php/AAAI/article/download/28863/29640"},{"title":"[2312.11118] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/abs/2312.11118"},{"title":"Explaining reinforcement learning agents through counterfactual action outcomes | Proceedings of the Thirty-Eighth AAAI Conference on Artificial Intelligence and Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence and Fourteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v38i9.28863"},{"title":"[PDF] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Explaining-Reinforcement-Learning-Agents-Through-Amitai-Septon/66766682c5669964ec6405e0acd9ca228024c5ab"},{"title":"Yotam Amitai - Publications","url":"https://www.yotamitai.com/publications"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes | Request PDF","url":"https://www.researchgate.net/publication/379288542_Explaining_Reinforcement_Learning_Agents_through_Counterfactual_Action_Outcomes"},{"title":"Yotam Amitai's research works","url":"https://www.researchgate.net/scientific-contributions/Yotam-Amitai-2199187157"},{"title":"Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/html/2312.11118"}]

Based on the search results, I found the pape
…[truncated 1039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:26:36.708329+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.19749 authors full list Zeng Yirong"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.19749 authors full list Zeng Yirong"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:26:36.708568+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.00737 authors full list \"To Call or Not to Call\" Qinyuan Wu Soumi Das"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.00737 authors full list \"To Call or Not to Call\" Qinyuan Wu Soumi Das"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:26:36.708796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolkenGPT NeurIPS 2023 authors full list Shibo Hao Tianyang Liu Zhen Wang Zhiting Hu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolkenGPT NeurIPS 2023 authors full list Shibo Hao Tianyang Liu Zhen Wang Zhiting Hu"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:26:36.709047+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 70 · 2026-05-26T10:26:36.709277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:26:36.709499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson 2021 Artificial Intelligence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson 2021 Artificial Intelligence"
  }
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:26:36.709774+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 4",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n31. cameron-2008\nTitle: Bootstrap-Based Improvements for Inference with Clustered Errors\nAuthors: Cameron, A. Colin and Gelbach, Jonah B. and Miller, Douglas L.\nJournal: The Review of Economics and Statistics, vol 90(3), pp 414-427\nYear: 2008\n\n32. achiam2017cpo\nTitle: Constrained Policy Optimization\nAuthors: Achiam, Joshua and Held, David and Tamar, Aviv and Abbeel, Pieter\nVenue: ICML 2017, pp 22-31\nYear: 2017\n\n33. toolace-2025\nTitle: ToolACE: Winning the Points of LLM Function Calling\nAuthors: Zhang, Weiwen and others\nVenue: ICLR 2025\nYear: 2025\n\n34. webb-2023\nTitle: Reworking Wild Bootstrap-Based Inference for Clustered Errors\nAuthors: Webb, Matthew D.\nJournal: Canadian Journal of Economics, vol 56(3), pp 839-858\nYear: 2023\n\n35. moldovan2012safe\nTitle: Safe Exploration in Markov Decision Processes\nAuthors: Moldovan, Teodor Mihai and Abbeel, Pieter\nVenue: ICML 2012\nYear: 2012\n\n36. graves2016act\nTitle: Adaptive Computation Time for Recurrent Neural Networks\nAuthors: Graves, Alex\nJournal: arXiv preprint arXiv:1603.08983\nYear: 2016\n\n37. ruan2024failures\nTitle: Identifying the Risks of LM Agents with an LM-Emulated Sandbox\nAuthors: Ruan, Yangjun and Dong, Honghua and Wang, Andrew and Pitis, Silviu and Zhou, Yongchao and Ba, Jimmy and Dubois, Yann and Maddison, Chris J. and Hashimoto, Tatsunori\nVenue: ICLR 2024\nYear: 2024\n\n38. saferoute-2025\nTitle: SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\nAuthors: Lee, Seanie and others\nVenue: Findings of ACL 2025\nYear: 2025\n\n39. altman1999constrained\nTitle: Constrained Markov Decision Processes\nAuthors: Altman, Eitan\nPublisher: Chapman & Hall/CRC\nYear: 1999\n\n40. mihatsch2002risk\nTitle: Risk-Sensitive Reinforcement Learning\nAuthors: Mihatsch, Oliver and Neuneier, Ralph\nJournal: Machine Learning, vol 49(2-3), pp 267-290\nYear: 2002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 4",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n31. cameron-2008\nTitle: Bootstrap-Based Improvements for Inference with Clustered Errors\nAuthors: Cameron, A. Colin and Gelbach, Jonah B. and Miller, Douglas L.\nJournal: The Review of Economics and Statistics, vol 90(3), pp 414-427\nYear: 2008\n\n32. achiam2017cpo\nTitle: Constrained Policy Optimization\nAuthors: Achiam, Joshua and Held, David and Tamar, Aviv and Abbeel, Pieter\nVenue: ICML 2017, pp 22-31\nYear: 2017\n\n33. toolace-2025\nTitle: ToolACE: Winning the Points of LLM Function Calling\nAuthors: Zhang, Weiwen and others\nVenue: ICLR 2025\nYear: 2025\n\n34. webb-2023\nTitle: Reworking Wild Bootstrap-Based Inference for Clustered Errors\nAuthors: Webb, Matthew D.\nJournal: Canadian Journal of Economics, vol 56(3), pp 839-858\nYear: 2023\n\n35. moldovan2012safe\nTitle: Safe Exploration in Markov Decision Processes\nAuthors: Moldovan, Teodor Mihai and Abbeel, Pieter\nVenue: ICML 2012\nYear: 2012\n\n36. graves2016act\nTitle: Adaptive Computation Time for Recurrent Neural Networks\nAuthors: Graves, Alex\nJournal: arXiv preprint arXiv:1603.08983\nYear: 2016\n\n37. ruan2024failures\nTitle: Identifying the Risks of LM Agents with an LM-Emulated Sandbox\nAuthors: Ruan, Yangjun and Dong, Honghua and Wang, Andrew and Pitis, Silviu and Zhou, Yongchao and Ba, Jimmy and Dubois, Yann and Maddison, Chris J. and Hashimoto, Tatsunori\nVenue: ICLR 2024\nYear: 2024\n\n38. saferoute-2025\nTitle: SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\nAuthors: Lee, Seanie and others\nVenue: Findings of ACL 2025\nYear: 2025\n\n39. altman1999constrained\nTitle: Constrained Markov Decision Processes\nAuthors: Altman, Eitan\nPublisher: Chapman & Hall/CRC\nYear: 1999\n\n40. mihatsch2002risk\nTitle: Risk-Sensitive Reinforcement Learning\nAuthors: Mihatsch, Oliver and Neuneier, Ralph\nJournal: Machine Learning, vol 49(2-3), pp 267-290\nYear: 2002"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:26:36.710311+00:00_

Web search results for query: "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 Sangmin Bae venue"

Links: [{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"[2507.10524] Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/abs/2507.10524"},{"title":"dblp: Sangmin Bae","url":"https://dblp.org/pid/91/1588.html"},{"title":"NeurIPS Poster Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118085"},{"title":"ICML Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Thinking","url":"https://icml.cc/virtual/2025/51797"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/html/2507.10524v1"},{"title":"mixture_of_recursions/README.md at main · raymin0223/mixture_of_recursions","url":"https://github.com/raymin0223/mixture_of_recursions/blob/main/README.md"},{"title":"(PDF) Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://www.researchgate.net/publication/393684588_Mixture-of-Recursions_Learning_Dynamic_Recursive_Depths_for_Adaptive_Token-Level_Computation"},{"title":"dblp: Hrayr Harutyunyan","url":"https://dblp.org/pid/198/1465.html"}]

Based on the search results, I can provide you with information about the "Mixture-of-Recursions" paper:

Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation was published at NeurIPS 2025. The paper is authored by Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, Tal Sc
…[truncated 468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:26:36.710619+00:00_

Web search results for query: "MTRouter ACL 2026 main conference accepted Zhang Yiqun"

Links: [{"title":"GitHub - ZhangYiqun018/MTRouter: [ACL 2026] Official implementation of MTRouter, a cost-aware multi-turn LLM routing framework accepted to ACL 2026 Main Conference. · GitHub","url":"https://github.com/ZhangYiqun018/MTRouter"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"ACL 2026 (@aclmeeting) / Posts / X","url":"https://x.com/aclmeeting"},{"title":"ACL: Meeting of the Association for Computational Linguistics 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=37"},{"title":"What Really Matters for Table LLMs? A Meta-Evaluation of Model and Data Effects - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.195/"},{"title":"ACL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2F2026%2FConference"}]

Based on the search results, MTRouter is a cost-aware multi-turn LLM routing framework accepted to the ACL 2026 Main Conference. The official implementation is available on GitHub under the repository ZhangYiqun018/MTRouter.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:26:36.710885+00:00_

Web search results for query: "arxiv 2605.00737 authors full list "To Call or Not to Call" Qinyuan Wu Soumi Das"

Links: [{"title":"[2605.00737] To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/abs/2605.00737"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737"},{"title":"Artificial Intelligence May 2026","url":"https://arxiv.org/list/cs.AI/current"},{"title":"When2Call: When (not) to Call Tools","url":"https://arxiv.org/pdf/2504.18851"},{"title":"Developing a Production System for Purpose of Call Detection in Business   Phone Conversations","url":"https://arxiv.org/pdf/2205.06904"},{"title":"FunReason: Enhancing Large Language Models' Function Calling via Self-Refinement Multiscale Loss and Automated Data Refinement","url":"https://arxiv.org/pdf/2505.20192"}]

Based on the search results, the full list of authors for arxiv paper 2605.00737 "To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling" is: Qinyuan Wu, Soumi Das, Mahsa Amani, Arijit Nag, Seungeon Lee, Krishna P. Gummadi, Abhilasha Ravichander, and Muhammad Bilal Zafar.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:26:36.711182+00:00_

Web search results for query: "arxiv 2604.19749 authors full list Zeng Yirong"

Links: [{"title":"[2604.19749] The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?","url":"https://arxiv.org/abs/2604.19749"},{"title":"Computational Geometry authors/titles Mar 2021","url":"http://export.arxiv.org/list/cs.CG/2103"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1259&show=1000"},{"title":"Digital Libraries authors/titles Jul 2016","url":"https://arxiv.org/list/cs.DL/1607"},{"title":"Computer Science 2016","url":"https://arxiv.org/list/cs/2016"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/abs/0809.3243"},{"title":"Computation authors/titles Jan 2013","url":"https://arxiv.org/list/stat.CO/1301"},{"title":"Computer Vision and Pattern Recognition","url":"https://arxiv.org/list/cs.CV/pastweek?skip=187&show=50"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"[2404.19756] KAN: Kolmogorov-Arnold Networks","url":"https://arxiv.org/abs/2404.19756"}]

Based on the search results, the authors of arxiv paper 2604.19749 are: Yirong Zeng, Shen You, Yufei Liu, Qunyao Du, Xiao Ding, Yutai Hou, Yuxian Wang, Wu Ning, Haonan Song, Dandan Tu, Bibo Cai, and Ting Liu. The paper is titled "The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:26:36.711454+00:00_

Web search results for query: "ToolkenGPT NeurIPS 2023 authors full list Shibo Hao Tianyang Liu Zhen Wang Zhiting Hu"

Links: [{"title":"ToolkenGPT: Augmenting Frozen Language Models with ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8fd1a81c882cd45f64958da6284f4a3f-Paper-Conference.pdf"},{"title":"[PDF] Toolformer: Language Models Can Teach Themselves to Use Tools | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toolformer:-Language-Models-Can-Teach-Themselves-to-Schick-Dwivedi-Yu/53d128ea815bcc0526856eb5a9c42cc977cb36a7"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html"},{"title":"ToolkenGPT: Augmenting Frozen Language Models","url":"https://arxiv.org/pdf/2305.11554"},{"title":"NeurIPS Poster ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://nips.cc/virtual/2023/poster/72492"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with ...","url":"https://openreview.net/pdf?id=BHXsb69bSx"},{"title":"NeurIPS 2023 ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings Oral","url":"https://nips.cc/virtual/2023/oral/73868"},{"title":"NeurIPS 2023 Orals","url":"https://nips.cc/virtual/2023/events/oral"},{"title":"[2305.11554] ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://arxiv.org/abs/2305.11554"}]

Based on the search results, the authors of ToolkenGPT are Shibo Hao, Tianyang Liu, Zhen Wang, and Zhiting Hu. The paper was presented as an Oral Poster at NeurIPS 2023.

The search results confirm that these are the four authors listed for the paper "ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings" which was presented at NeurIPS 2023.


REMINDER: You MUST include the sources above in your resp
…[truncated 43 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:26:36.711740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Stephane Ross DAgger imitation learning CMU full name accent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Stephane Ross DAgger imitation learning CMU full name accent"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:26:36.712006+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jasmina Gajcin AAMAS 2023 \"Counterfactual Explanations\" doctoral consortium extended abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jasmina Gajcin AAMAS 2023 \"Counterfactual Explanations\" doctoral consortium extended abstract"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:26:36.712293+00:00_

Web search results for query: "Jasmina Gajcin AAMAS 2023 "Counterfactual Explanations" doctoral consortium extended abstract"

Links: [{"title":"Counterfactual Explanations for Reinforcement Learning Agents","url":"https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p2925.pdf"},{"title":"Accepted Papers - AAMAS 2023","url":"https://aamas2023.soton.ac.uk/program/accepted-papers/"},{"title":"[PDF] RACCER: Towards Reachable and Certain Counterfactual Explanations for Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RACCER:-Towards-Reachable-and-Certain-Explanations-Gajcin-Dusparic/86148a95c5bd64493d8fc19b4289494c4ab0f0cf"},{"title":"(PDF) RACCER: Towards Reachable and Certain Counterfactual Explanations for Reinforcement Learning","url":"https://www.researchgate.net/publication/383739696_RACCER_Towards_Reachable_and_Certain_Counterfactual_Explanations_for_Reinforcement_Learning"},{"title":"[2402.06503] ACTER: Diverse and Actionable Counterfactual Sequences for Explaining and Diagnosing RL Policies","url":"https://arxiv.org/abs/2402.06503"},{"title":"Counterfactual explanations for reinforcement learning: interview with Jasmina Gajcin - ΑΙhub","url":"https://aihub.org/2022/11/22/counterfactual-explanations-for-reinforcement-learning-interview-with-jasmina-gajcin/"},{"title":"Jasmina Gajcin","url":"https://www.catalyzex.com/author/Jasmina%20Gajcin"},{"title":"Programme - AAMAS 2023","url":"https://aamas2023.soton.ac.uk/program/detailed-program/"}]

Based on the search results, I found the information about Jasmina Gajcin's work at AAMAS 2023:

Jasmina Gajcin presented "Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium" at the 22nd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2023) in London, United Kingdom, May 29 – June 2, 2023. The extended abstract was 3 pages.

The approach generates contrastive explanations about two policies by analyzing the state space in which po
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:26:36.712581+00:00_

Web search results for query: "Stephane Ross DAgger imitation learning CMU full name accent"

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"Reduction of Imitation Learning to No-Regret Online Learning Stephane Ross","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-Slides.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"[1011.0686] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://arxiv.org/abs/1011.0686"},{"title":"Stéphane Ross - Robotics Institute","url":"https://www.cs.cmu.edu/~sross1/"},{"title":"arXiv:1406.5979v1 [cs.LG] 23 Jun 2014 Reinforcement and Imitation Learning","url":"https://arxiv.org/pdf/1406.5979"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"},{"title":"Deeply AggreVaTeD: Differentiable Imitation Learning for Sequential Prediction","url":"https://homes.cs.washington.edu/~bboots/files/RLDM_AggreVaTeD.pdf"},{"title":"A Reduction of Imitation Learning and Structure Prediction ...","url":"https://www.cl.uni-heidelberg.de/courses/ws18/iml/dagger.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.researchgate.net/publication/47646552_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No-RegretOnline_Learning"}]

Based on the search results, I can provide you with information about Stephane Ross and DAgger:

The researcher's name is Stéphane Ross (note the accent on the 'e' in Stéphane). Stéphane Ross is affiliated with CMU (Carnegie Mellon University), where he works at the Robotics Institute.

DAgger (Dataset Aggregation) is an algorithm developed by
…[truncated 559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:26:36.712885+00:00_

Web search results for query: "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson 2021 Artificial Intelligence"

Links: [{"title":"[2101.12446] Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://arxiv.org/abs/2101.12446"},{"title":"Counterfactual state explanations for reinforcement learning agents via generative deep learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370221000060"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Counterfactual+state+explanations+for+reinforcement+learning+agents+via+generative+deep+learning&amp=&author=Matthew+L.+Olson&amp=&author=Roli+Khanna&amp=&author=Lawrence+Neal&amp=&author=Fuxin+Li&amp=&author=Weng-Keen+Wong&amp=&publication_year=2021&amp=&journal=Artificial+Intelligence&amp=&pages=103455&amp=&doi=10.1016/j.artint.2021.103455"},{"title":"(PDF) Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://www.researchgate.net/publication/348928549_Counterfactual_State_Explanations_for_Reinforcement_Learning_Agents_via_Generative_Deep_Learning"},{"title":"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://www.researchgate.net/publication/348831791_Counterfactual_State_Explanations_for_Reinforcement_Learning_Agents_via_Generative_Deep_Learning"},{"title":"Counterfactual Explanations for Continuous Action Reinforcement Learning","url":"https://arxiv.org/html/2505.12701v1"},{"title":"Counterfactual Explanations for Continuous Action Reinforcement Learning","url":"https://www.ijcai.org/proceedings/2025/0561.pdf"},{"title":"Matthew L. Olson, Roli Khanna, Lawrence Neal, Fuxin Li & Weng-Keen Wong, Counterfactual state explanations for reinforcement learning agents via generative deep learning - PhilPapers","url":"https://philpapers.org/rec/OL
…[truncated 1752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:26:36.713195+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RouteLLM Learning to Route LLMs with Preference Data arXiv 2406.18665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RouteLLM Learning to Route LLMs with Preference Data arXiv 2406.18665"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:26:36.713445+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 85 · 2026-05-26T10:26:36.713684+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:26:36.713921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cameron Gelbach Miller \"Bootstrap-Based Improvements for Inference with Clustered Errors\" Review of Economics and Statistics 2008"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cameron Gelbach Miller \"Bootstrap-Based Improvements for Inference with Clustered Errors\" Review of Economics and Statistics 2008"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-26T10:26:36.714179+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Achiam Held Tamar Abbeel \"Constrained Policy Optimization\" ICML 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Achiam Held Tamar Abbeel \"Constrained Policy Optimization\" ICML 2017"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-26T10:26:36.714414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolACE \"Winning the Points of LLM Function Calling\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolACE \"Winning the Points of LLM Function Calling\" ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:26:36.714641+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Webb \"Reworking Wild Bootstrap-Based Inference for Clustered Errors\" Canadian Journal of Economics 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Webb \"Reworking Wild Bootstrap-Based Inference for Clustered Errors\" Canadian Journal of Economics 2023"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:26:36.714868+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Moldovan Abbeel \"Safe Exploration in Markov Decision Processes\" ICML 2012"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Moldovan Abbeel \"Safe Exploration in Markov Decision Processes\" ICML 2012"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:26:36.715127+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Graves \"Adaptive Computation Time for Recurrent Neural Networks\" arXiv 1603.08983"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Graves \"Adaptive Computation Time for Recurrent Neural Networks\" arXiv 1603.08983"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:26:36.715346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ruan Dong Wang Pitis \"Identifying the Risks of LM Agents with an LM-Emulated Sandbox\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ruan Dong Wang Pitis \"Identifying the Risks of LM Agents with an LM-Emulated Sandbox\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:26:36.715573+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeRoute \"Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeRoute \"Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\" ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:26:36.715803+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Altman \"Constrained Markov Decision Processes\" Chapman Hall CRC 1999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Altman \"Constrained Markov Decision Processes\" Chapman Hall CRC 1999"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:26:36.716091+00:00_

Web search results for query: "Cameron Gelbach Miller "Bootstrap-Based Improvements for Inference with Clustered Errors" Review of Economics and Statistics 2008"

Links: [{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors","url":"https://ideas.repec.org/a/tpr/restat/v90y2008i3p414-427.html"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors | The Review of Economics and Statistics | MIT Press","url":"https://direct.mit.edu/rest/article/90/3/414/57731/Bootstrap-Based-Improvements-for-Inference-with"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors | NBER","url":"https://www.nber.org/papers/t0344"},{"title":"Bootstrap-Based Improvements for Inference with ...","url":"https://www.nber.org/system/files/working_papers/t0344/t0344.pdf"},{"title":"EconPapers: Bootstrap-Based Improvements for Inference with Clustered Errors","url":"https://econpapers.repec.org/RePEc:tpr:restat:v:90:y:2008:i:3:p:414-427"},{"title":"Bootstrap-Based Improvments for Inference With Clustered Errors | Request PDF","url":"https://www.researchgate.net/publication/24096179_Bootstrap-Based_Improvments_for_Inference_With_Clustered_Errors"},{"title":"Sci-Hub | Bootstrap-Based Improvements for Inference with Clustered Errors | 10.1162/rest.90.3.414","url":"https://sci-hub.ee/10.1162/REST.90.3.414"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors by A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=956890"},{"title":"(PDF) Bootstrap-Based Improvements for Inference with Clustered Errors (2007) | A. Colin Cameron | 999 Citations","url":"https://scispace.com/papers/bootstrap-based-improvements-for-inference-with-clustered-2rr1liz8yy"}]

I found the paper you're looking for. Here are the key details:

**Citation:** A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller; Bootstrap-Based Improvements for Inference with Clustered Errors, p
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:26:36.716415+00:00_

Web search results for query: "Achiam Held Tamar Abbeel "Constrained Policy Optimization" ICML 2017"

Links: [{"title":"Constrained Policy Optimization","url":"https://proceedings.mlr.press/v70/achiam17a.html"},{"title":"Constrained policy optimization | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305384"},{"title":"Constrained Policy Optimization | Tejaswi Kasarla","url":"https://tkasarla.github.io/2017/10/19/constrained-policy-optimization/"},{"title":"[1705.10528] Constrained Policy Optimization","url":"https://arxiv.org/abs/1705.10528"},{"title":"[PDF] Constrained Policy Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Constrained-Policy-Optimization-Achiam-Held/7a4193d0b042643a8bb9ec262ed7f9d509bdb12e"},{"title":"Constrained Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/317240991_Constrained_Policy_Optimization"},{"title":"Constrained policy optimization - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/constrained-policy-optimization/"},{"title":"GitHub - jachiam/cpo: Constrained Policy Optimization · GitHub","url":"https://github.com/jachiam/cpo"},{"title":"Constrained Policy Optimization - Robotics Institute Carnegie Mellon University","url":"https://www.ri.cmu.edu/publications/constrained-policy-optimization/"},{"title":"State-wise Constrained Policy Optimization","url":"https://arxiv.org/html/2306.12594v3"}]

Based on the search results, here's what I found about the paper:

The paper "Constrained Policy Optimization" was authored by Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel and was published in the Proceedings of the 34th International Conference on Machine Learning (ICML 2017).

The paper proposes Constrained Policy Optimization (CPO), the first general-purpose policy search algorithm for constrained reinforcement learning with guarantees for nea
…[truncated 749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:26:36.716681+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mihatsch Neuneier \"Risk-Sensitive Reinforcement Learning\" Machine Learning 2002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mihatsch Neuneier \"Risk-Sensitive Reinforcement Learning\" Machine Learning 2002"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:26:36.716921+00:00_

Web search results for query: "Webb "Reworking Wild Bootstrap-Based Inference for Clustered Errors" Canadian Journal of Economics 2023"

Links: [{"title":"Reworking wild bootstrap‐based inference for clustered errors - Webb - 2023 - Canadian Journal of Economics/Revue canadienne d'économique - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/caje.12661"},{"title":"Wild Bootstrap for Instrumental Variables Regressions with Weak and Few   Clusters","url":"https://arxiv.org/pdf/2108.13707"},{"title":"Cluster-Robust Bootstrap Inference in Quantile Regression Models","url":"https://arxiv.org/pdf/1407.7166"},{"title":"Fast and Reliable Jackknife and Bootstrap Methods for Cluster-Robust   Inference","url":"https://arxiv.org/pdf/2301.04527"},{"title":"Gradient Wild Bootstrap for Instrumental Variable Quantile Regressions   with Weak and Few Clusters","url":"https://arxiv.org/pdf/2408.10686"},{"title":"Cluster-Robust Inference: A Guide to Empirical Practice","url":"https://arxiv.org/pdf/2205.03285"},{"title":"Refined Cluster Robust Inference","url":"https://arxiv.org/pdf/2603.24786"}]

I found the paper you're looking for! The article was published in the Canadian Journal of Economics/Revue canadienne d'économique, volume 56, pages 839-858 (2023).

The paper addresses how with few clusters, inference is often conducted using the wild cluster bootstrap, but with conventional bootstrap weights the set of valid p-values can create ambiguities in inference, which the author considers several modifications to resolve. Monte Carlo simulations provide evidence that both a new 6-point bootstrap weight distribution and a kernel density estimation approach improve the reliability of inference.

The article is available on Wiley Online Library at: https://onlinelibrary.wiley.com/doi/10.1111/caje.12661


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:26:36.717240+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 5",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n41. natarajan2013learning\nTitle: Learning with Noisy Labels\nAuthors: Natarajan, Nagarajan and Dhillon, Inderjit S. and Ravikumar, Pradeep and Tewari, Ambuj\nVenue: NeurIPS 2013\nYear: 2013\n\n42. budget-aware-routing-2026\nTitle: Budget-Aware Agentic Routing via Boundary-Guided Training\nAuthors: Zhang, Caiqi and Xia, Menglin and Zhang, Xuchao and Madrigal, Daniel and Mallick, Ankur and Kessler, Samuel and Ruehle, Victor and Rajmohan, Saravan\nJournal: arXiv preprint arXiv:2602.21227\nYear: 2026\n\n43. pona2025abstract\nTitle: Abstract Counterfactuals for Language Model Agents\nAuthors: Pona, Edoardo and Kazemi, Milad and Du, Yali and Watson, David and Paoletti, Nicola\nJournal: arXiv preprint arXiv:2506.02946\nYear: 2025\n\n44. cso-2026\nTitle: Verified Critical Step Optimization for LLM Agents\nAuthors: Li, Mukai and Zeng, Qingcheng and Fang, Tianqing and Liang, Zhenwen and Song, Linfeng and Liu, Qi and Mi, Haitao and Yu, Dong\nJournal: arXiv preprint arXiv:2602.03412\nYear: 2026\n\n45. axis-2026\nTitle: Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\nAuthors: Gyevnár, Bálint and Lucas, Christopher G. and Albrecht, Stefano V. and Cohen, Shay B.\nJournal: arXiv preprint arXiv:2505.17801\nYear: 2025\n\n46. salt-2026\nTitle: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\nAuthors: Li, Jiazheng and Wang, Yawei and Yan, David and Tian, Yijun and Xu, Zhichao and Song, Huan and Xu, Panpan and Cheong, Lin Lee\nVenue: Findings of EACL 2026\nYear: 2026\n\n47. gemma2-2024\nTitle: Gemma 2: Improving Open Language Models at a Practical Size\nAuthors: Gemma Team\nJournal: arXiv preprint arXiv:2408.00118\nYear: 2024\n\n48. northcutt2021confident\nTitle: Confident Learning: Estimating Uncertainty in Dataset Labels\nAuthors: Northcutt, Curtis and Jiang, Lu and Chuang, Isaac\nJournal: Journal of Artificial Intelligence Research, vol 70, pp 1373-1411\nYear: 2021\n\n49. li2020dividemix\nTitle: DivideMix: Learning with Noisy Labels as Semi-supervised Learning\nAuthors: Li, Junnan and Socher, Richard and Hoi, Steven C.H.\nVenue: ICLR 2020\nYear: 2020\n\n50. ng1999policy\nTitle: Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\nAuthors: Ng, Andrew Y. and Harada, Daishi and Russell, Stuart\nVenue: ICML 1999\nYear: 1999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 5",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n41. natarajan2013learning\nTitle: Learning with Noisy Labels\nAuthors: Natarajan, Nagarajan and Dhillon, Inderjit S. and Ravikumar, Pradeep and Tewari, Ambuj\nVenue: NeurIPS 2013\nYear: 2013\n\n42. budget-aware-routing-2026\nTitle: Budget-Aware Agentic Routing via Boundary-Guided Training\nAuthors: Zhang, Caiqi and Xia, Menglin and Zhang, Xuchao and Madrigal, Daniel and Mallick, Ankur and Kessler, Samuel and Ruehle, Victor and Rajmohan, Saravan\nJournal: arXiv preprint arXiv:2602.21227\nYear: 2026\n\n43. pona2025abstract\nTitle: Abstract Counterfactuals for Language Model Agents\nAuthors: Pona, Edoardo and Kazemi, Milad and Du, Yali and Watson, David and Paoletti, Nicola\nJournal: arXiv preprint arXiv:2506.02946\nYear: 2025\n\n44. cso-2026\nTitle: Verified Critical Step Optimization for LLM Agents\nAuthors: Li, Mukai and Zeng, Qingcheng and Fang, Tianqing and Liang, Zhenwen and Song, Linfeng and Liu, Qi and Mi, Haitao and Yu, Dong\nJournal: arXiv preprint arXiv:2602.03412\nYear: 2026\n\n45. axis-2026\nTitle: Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\nAuthors: Gyevnár, Bálint and Lucas, Christopher G. and Albrecht, Stefano V. and Cohen, Shay B.\nJournal: arXiv preprint arXiv:2505.17801\nYear: 2025\n\n46. salt-2026\nTitle: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\nAuthors: Li, Jiazheng and Wang, Yawei and Yan, David and Tian, Yijun and Xu, Zhichao and Song, Huan and Xu, Panpan and Cheong, Lin Lee\nVenue: Findings of EACL 2026\nYear: 2026\n\n47. gemma2-2024\nTitle: Gemma 2: Improving Open Language Models at a Practical Size\nAuthors: Gemma Team\nJournal: arXiv preprint arXiv:2408.00118\nYear: 2024\n\n48. northcutt2021confident\nTitle: Confident Learning: Estimating Uncertainty in Dataset Labels\nAuthors: Northcutt, Curtis and Jiang, Lu and Chuang, Isaac\nJournal: Journal of Artificial Intelligence Research, vol 70, pp 1373-1411\nYear: 2021\n\n49. li2020dividemix\nTitle: DivideMix: Learning with Noisy Labels as Semi-supervised Learning\nAuthors: Li, Junnan and Socher, Richard and Hoi, Steven C.H.\nVenue: ICLR 2020\nYear: 2020\n\n50. ng1999policy\nTitle: Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\nAuthors: Ng, Andrew Y. and Harada, Daishi and Russell, Stuart\nVenue: ICML 1999\nYear: 1999"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:26:36.717701+00:00_

Web search results for query: "RouteLLM Learning to Route LLMs with Preference Data arXiv 2406.18665"

Links: [{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"Paper page - RouteLLM: Learning to Route LLMs with Preference Data","url":"https://huggingface.co/papers/2406.18665"},{"title":"Quick Read :: RouteLLM: Learning to Route LLMs with Preference Data | by QvickRead | Medium","url":"https://readqvick.medium.com/quick-read-routellm-learning-to-route-llms-with-preference-data-88a2b2e94f5e"},{"title":"[2406.18665v2] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v2"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data Isaac Ong† UC Berkeley","url":"https://arxiv.org/pdf/2406.18665v3"},{"title":"[2406.18665v3] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v3"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data","url":"https://www.opentrain.ai/papers/routellm-learning-to-route-llms-with-preference-data--arxiv-2406.18665/"},{"title":"[2406.18665v1] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v1"}]

I found the paper for you! Here's what RouteLLM is about:

## Overview

RouteLLM proposes efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality.

## Problem and Solution

Large language models exhibit impressive capabilities across a wide range of tasks, yet the choice of which model to use often involves a trade-off between performance and cost, with more powerful models being effective but expensive, while less capable models are more cost-effective.

## Methodology

The training framework for these routers leverages human preference data and data augmentation techniques to enhance performance. The framework uses 2 c
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:26:36.718016+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion Language Agents with Verbal Reinforcement Learning Shinn NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion Language Agents with Verbal Reinforcement Learning Shinn NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:26:36.718288+00:00_

Web search results for query: "ToolACE "Winning the Points of LLM Function Calling" ICLR 2025"

Links: [{"title":"ToolACE: Winning the Points of LLM Function Calling | OpenReview","url":"https://openreview.net/forum?id=8EB8k6DdCU"},{"title":"[2409.00920] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920"},{"title":"ICLR Poster ToolACE: Winning the Points of LLM Function Calling","url":"https://iclr.cc/virtual/2025/poster/30779"},{"title":"ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/html/2409.00920v1"},{"title":"Team-ACE/ToolACE-8B · Hugging Face","url":"https://huggingface.co/Team-ACE/ToolACE-8B"},{"title":"WINNING THE POINTS OF LLM FUNCTION CALLING","url":"https://openreview.net/pdf?id=8EB8k6DdCU"},{"title":"ToolACE: Winning the Points of LLM Function Calling | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/toolace-winning-points-llm-function-calling"},{"title":"[2409.00920v1] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920v1"},{"title":"(PDF) ToolACE: Winning the Points of LLM Function Calling","url":"https://www.researchgate.net/publication/383701460_ToolACE_Winning_the_Points_of_LLM_Function_Calling"}]

I found relevant information about ToolACE. Here's what I found:

## ToolACE: Winning the Points of LLM Function Calling

ToolACE is an automatic agentic pipeline designed to generate accurate, complex, and diverse tool-learning data. The paper was published at ICLR 2025.

### Key Features:

ToolACE leverages a novel self-evolution synthesis process to curate a comprehensive API pool of 26,507 diverse APIs. Dialogs are generated through the interplay among multiple agents, guided by a formalized thinking process, and a dual-layer verification system combining rule-based and model-based checks ensures data accuracy.

### Performance:

Models trained on ToolACE's synthesized data, even with only 8B parameters, achieve st
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:26:36.718582+00:00_

Web search results for query: "Ruan Dong Wang Pitis "Identifying the Risks of LM Agents with an LM-Emulated Sandbox" ICLR 2024"

Links: [{"title":"[2309.15817] Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://arxiv.org/abs/2309.15817"},{"title":"Identifying the Risks of LM Agents with an LM-Emulated Sandbox | OpenReview","url":"https://openreview.net/forum?id=GEcwtMk1uA"},{"title":"Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/7274ed909a312d4d869cc328ad1c5f04-Abstract-Conference.html"},{"title":"ICLR Poster Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://iclr.cc/virtual/2024/poster/19037"},{"title":"Published as a conference paper at ICLR 2024 IDENTIFYING THE RISKS OF LM AGENTS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf"},{"title":"GitHub - ryoungj/ToolEmu: [ICLR'24 Spotlight] A language model (LM)-based emulation framework for identifying the risks of LM agents with tool use · GitHub","url":"https://github.com/ryoungj/ToolEmu"},{"title":"[PDF] Identifying the Risks of LM Agents with an LM-Emulated Sandbox | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Identifying-the-Risks-of-LM-Agents-with-an-Sandbox-Ruan-Dong/0a893657e00fe8ecfadcc65c63bf293e70cb1564"},{"title":"Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://www.cs.toronto.edu/~yjruan/assets/pdf/poster/ToolEmu_poster.pdf"}]

I found the research paper you're looking for! Here's what I found:

The paper "Identifying the Risks of LM Agents with an LM-Emulated Sandbox" was authored by Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris Maddison, and Tatsunori Hashimoto, and was published at ICLR 2024.

The paper addresses how recent advances in Language Model agents and tool use, exemplified by applications l
…[truncated 879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:26:36.718877+00:00_

Web search results for query: "Moldovan Abbeel "Safe Exploration in Markov Decision Processes" ICML 2012"

Links: [{"title":"Safe Exploration in Markov Decision Processes Teodor Mihai Moldovan","url":"https://icml.cc/2012/papers/838.pdf"},{"title":"[1205.4810] Safe Exploration in Markov Decision Processes","url":"https://arxiv.org/abs/1205.4810"},{"title":"Safe Exploration in Finite Markov Decision Processes with Gaussian Processes","url":"https://las.inf.ethz.ch/files/turchetta16safemdp.pdf"},{"title":"[PDF] Safe Exploration in Markov Decision Processes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Safe-Exploration-in-Markov-Decision-Processes-Moldovan-Abbeel/d66ab178e941e3a79954c858d3c1bcdee8e1d17d"},{"title":"Safe exploration in Markov decision processes | Proceedings of the 29th International Coference on International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3042573.3042759"},{"title":"Safe Exploration in Markov Decision Processes | Request PDF","url":"https://www.researchgate.net/publication/225045205_Safe_Exploration_in_Markov_Decision_Processes"},{"title":"Safe Exploration for Optimization with Gaussian Processes","url":"http://proceedings.mlr.press/v37/sui15-supp.pdf"},{"title":"Safe Exploration in Markov Decision Processes Teodor Mihai Moldovan","url":"https://www.cs.ubc.ca/~hutter/nips2011workshop/papers_and_posters/safe_exploration.pdf"}]

I found the research paper! Here are the details:

**"Safe Exploration in Markov Decision Processes"** by Teodor Mihai Moldovan and Pieter Abbeel was published at the International Conference on Machine Learning (ICML) in 2012, pages 1711–1718.

**Key contributions of the paper:**

The paper proposes a general formulation of safety through ergodicity, and shows that imposing safety by restricting attention to the resulting set of guaranteed safe policies is NP-hard, and presents an efficient algorithm for guaranteed safe, but potentially suboptimal, exploration.

**Main p
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-26T10:26:36.719202+00:00_

Web search results for query: "Graves "Adaptive Computation Time for Recurrent Neural Networks" arXiv 1603.08983"

Links: [{"title":"[1603.08983] Adaptive Computation Time for Recurrent Neural Networks","url":"https://arxiv.org/abs/1603.08983"},{"title":"Adaptive Computation Time for Recurrent Neural Networks","url":"https://www.researchgate.net/publication/301879022_Adaptive_Computation_Time_for_Recurrent_Neural_Networks"},{"title":"Adaptive Computation Time for Recurrent Neural Networks Alex Graves","url":"https://arxiv.org/pdf/1603.08983"},{"title":"Adaptive Computation Time - Hugo Cisneros","url":"https://hugocisneros.com/notes/adaptive_computation_time/"},{"title":"[PDF] Adaptive Computation Time for Recurrent Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Computation-Time-for-Recurrent-Neural-Graves/04cca8e341a5da42b29b0bc831cb25a0f784fa01"},{"title":"[1603.08983v1] Adaptive Computation Time for Recurrent Neural Networks","url":"https://arxiv.org/abs/1603.08983v1"},{"title":"Adaptive Computation Time (ACT) in Neural Networks [1/3] | by Grigory Sapunov | Medium","url":"https://moocaholic.medium.com/adaptive-computation-time-act-in-neural-networks-part-1-2a28484b53df"},{"title":"Adaptive Computation Time for Recurrent Neural Networks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1960640a28f3e578a76d374b587717749"}]

I found the paper you're looking for! Here are the key details:

**Title:** Adaptive Computation Time for Recurrent Neural Networks

**Author:** Alex Graves

**arXiv ID:** 1603.08983

**Overview:** This paper introduces Adaptive Computation Time (ACT), an algorithm that allows recurrent neural networks to learn how many computational steps to take between receiving an input and emitting an output.

**Key Features:** ACT requires minimal changes to the network architecture, is deterministic and differentiable, and does not add any noise to the parameter gradients.

**Experimental Results:** Experiment
…[truncated 547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:26:36.719486+00:00_

Web search results for query: "SafeRoute "Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs" ACL 2025"

Links: [{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.105/"},{"title":"[2502.12464] SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/abs/2502.12464"},{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/html/2502.12464v1"},{"title":"Paper page - SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://huggingface.co/papers/2502.12464"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"No Free Lunch With Guardrails","url":"https://arxiv.org/html/2504.00441v2"}]

I found the paper! Here are the search results for SafeRoute:

## Overview

SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models is a paper accepted to the Findings of the Association for Computational Linguistics: ACL 2025, published in Vienna, Austria.

## Author Information

The paper is authored by Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, and Sung Ju Hwang.

## Main Contribution

The paper addresses the challenge that while large safety guard models achieve strong performance for detecting and blocking harmful user prompts, their computational cost is substantial. The authors propose SafeRoute, a binary router that distinguishes hard examples from easy ones, selectively applying the larger safety guard model to data the router considers hard, improving efficiency while maintaining accuracy.

## Results

Experimental results on multiple benchmark
…[truncated 357 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T10:26:36.719780+00:00_

Web search results for query: "Altman "Constrained Markov Decision Processes" Chapman Hall CRC 1999"

Links: [{"title":"Constrained Markov Decision Processes - 1st Edition - Shaler Stidham J","url":"https://www.routledge.com/Constrained-Markov-Decision-Processes/Altman/p/book/9780849303821"},{"title":"Amazon.com: Constrained Markov Decision Processes: Stochastic Modeling (Stochastic Modeling Series): 9780849303821: Altman, Eitan: Books","url":"https://www.amazon.com/Constrained-Decision-Processes-Stochastic-Modeling/dp/0849303826"},{"title":"Constrained Markov decision processes by Eitan Altman | Open Library","url":"https://openlibrary.org/books/OL97592M/Constrained_Markov_decision_processes"},{"title":"Constrained Markov Decision Processes: Stochastic Modeling (Stochastic Modeling Series) - Altman, Eitan: 9780849303821 - AbeBooks","url":"https://www.abebooks.com/9780849303821/Constrained-Markov-Decision-Processes-Stochastic-0849303826/plp"},{"title":"Constrained Markov Decision Processes with Total Expected Cost Criteria | Proceedings of the 12th EAI International Conference on Performance Evaluation Methodologies and Tools","url":"https://dl.acm.org/doi/10.1145/3306309.3306342"},{"title":"Constrained Markov Decision Processes | BibSonomy","url":"https://www.bibsonomy.org/bibtex/184fb43430ab46ff2336d7e9926a37b45/jleny"},{"title":"[PDF] Constrained Markov Decision Processes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Constrained-Markov-Decision-Processes-Altman/3cc2608fd77b9b65f5bd378e8797b2ab1b8acde7"},{"title":"Constrained Markov Decision Processes | Eitan Altman | Taylor & Franci","url":"https://www.taylorfrancis.com/books/mono/10.1201/9781315140223/constrained-markov-decision-processes-eitan-altman"},{"title":"CONSTRAINED MARKOV DECISION PROCESSES Eitan ALTMAN INRIA","url":"https://www-sop.inria.fr/members/Eitan.Altman/TEMP/h.pdf"}]

I found the book you're looking for! The book "Constrained Markov Decision Processes" by Eitan Altman was pu
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T10:26:36.720088+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 109 · 2026-05-26T10:26:36.720348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-26T10:26:36.720572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Natarajan Dhillon Ravikumar Tewari \"Learning with Noisy Labels\" NeurIPS 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Natarajan Dhillon Ravikumar Tewari \"Learning with Noisy Labels\" NeurIPS 2013"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:26:36.720809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Budget-Aware Agentic Routing via Boundary-Guided Training\" arXiv 2602.21227"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Budget-Aware Agentic Routing via Boundary-Guided Training\" arXiv 2602.21227"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-26T10:26:36.721055+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Abstract Counterfactuals for Language Model Agents\" Pona Kazemi arXiv 2506.02946"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Abstract Counterfactuals for Language Model Agents\" Pona Kazemi arXiv 2506.02946"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-26T10:26:36.721297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Verified Critical Step Optimization for LLM Agents\" Li Zeng Fang arXiv 2602.03412"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Verified Critical Step Optimization for LLM Agents\" Li Zeng Fang arXiv 2602.03412"
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-26T10:26:36.721526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\" Gyevnár arXiv 2505.17801"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\" Gyevnár arXiv 2505.17801"
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-26T10:26:36.721759+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\" Li Wang EACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\" Li Wang EACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-26T10:26:36.722004+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 6",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n51. agent-safetybench-2024\nTitle: Agent-SafetyBench: Evaluating the Safety of LLM Agents\nAuthors: Zhang, Zhexin and Cui, Shiyao and Lu, Yida and Zhou, Jingzhuo and Yang, Junhao and Liu, Jie and Wang, Renhao and Li, Jiangjie and Huang, Minlie\nJournal: arXiv preprint arXiv:2412.14470\nYear: 2024\n\n52. pearl2009causality\nTitle: Causality: Models, Reasoning, and Inference\nAuthors: Pearl, Judea\nPublisher: Cambridge University Press, 2nd edition\nYear: 2009\n\n53. rubin1974estimating\nTitle: Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\nAuthors: Rubin, Donald B.\nJournal: Journal of Educational Psychology, vol 66(5), pp 688-701\nYear: 1974\n\n54. switch-transformer-2022\nTitle: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\nAuthors: Fedus, William and Zoph, Barret and Shazeer, Noam\nJournal: Journal of Machine Learning Research, vol 23(120), pp 1-39\nYear: 2022\n\n55. gshard-2021\nTitle: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\nAuthors: Lepikhin, Dmitry and Lee, HyoukJoong and Xu, Yuanzhong and Chen, Dehao and Firat, Orhan and Huang, Yanping and Krikun, Maxim and Shazeer, Noam and Chen, Zhifeng\nVenue: ICLR 2021\nYear: 2021\n\n56. alshiekh2018safe\nTitle: Safe Reinforcement Learning via Shielding\nAuthors: Alshiekh, Mohammed and Bloem, Roderick and Ehlers, Rüdiger and Könighofer, Bettina and Niekum, Scott and Topcu, Ufuk\nVenue: AAAI 2018\nYear: 2018\n\n57. kaushik2020learning\nTitle: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\nAuthors: Kaushik, Divyansh and Hovy, Eduard and Lipton, Zachary C.\nVenue: ICLR 2020\nYear: 2020\n\n58. frugalgpt-2023\nTitle: FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\nAuthors: Chen, Lingjiao and Zaharia, Matei and Zou, James\nJournal: arXiv preprint arXiv:2305.05176\nYear: 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 6",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n51. agent-safetybench-2024\nTitle: Agent-SafetyBench: Evaluating the Safety of LLM Agents\nAuthors: Zhang, Zhexin and Cui, Shiyao and Lu, Yida and Zhou, Jingzhuo and Yang, Junhao and Liu, Jie and Wang, Renhao and Li, Jiangjie and Huang, Minlie\nJournal: arXiv preprint arXiv:2412.14470\nYear: 2024\n\n52. pearl2009causality\nTitle: Causality: Models, Reasoning, and Inference\nAuthors: Pearl, Judea\nPublisher: Cambridge University Press, 2nd edition\nYear: 2009\n\n53. rubin1974estimating\nTitle: Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\nAuthors: Rubin, Donald B.\nJournal: Journal of Educational Psychology, vol 66(5), pp 688-701\nYear: 1974\n\n54. switch-transformer-2022\nTitle: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\nAuthors: Fedus, William and Zoph, Barret and Shazeer, Noam\nJournal: Journal of Machine Learning Research, vol 23(120), pp 1-39\nYear: 2022\n\n55. gshard-2021\nTitle: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\nAuthors: Lepikhin, Dmitry and Lee, HyoukJoong and Xu, Yuanzhong and Chen, Dehao and Firat, Orhan and Huang, Yanping and Krikun, Maxim and Shazeer, Noam and Chen, Zhifeng\nVenue: ICLR 2021\nYear: 2021\n\n56. alshiekh2018safe\nTitle: Safe Reinforcement Learning via Shielding\nAuthors: Alshiekh, Mohammed and Bloem, Roderick and Ehlers, Rüdiger and Könighofer, Bettina and Niekum, Scott and Topcu, Ufuk\nVenue: AAAI 2018\nYear: 2018\n\n57. kaushik2020learning\nTitle: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\nAuthors: Kaushik, Divyansh and Hovy, Eduard and Lipton, Zachary C.\nVenue: ICLR 2020\nYear: 2020\n\n58. frugalgpt-2023\nTitle: FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\nAuthors: Chen, Lingjiao and Zaharia, Matei and Zou, James\nJournal: arXiv preprint arXiv:2305.05176\nYear: 2023"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:26:36.722614+00:00_

Here are the verification results for all 10 entries:

### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?
- 真实性：✓
- 作者：✓ (Wang, Ruoyao and Jansen, Peter and Côté, Marc-Alexandre and Ammanabrolu, Prithviraj — matches ACL Anthology)
- 年份：✓ (2022)
- 标题：✓ (minor: official title uses lowercase "your" — "Is your Agent Smarter than a 5th Grader?" — but this is a capitalization-only difference, acceptable in BibTeX)
- Venue：✓ (EMNLP 2022)
- ID：N/A (no arXiv ID claimed; actual arXiv ID is 2203.07540)

### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models
- 真实性：✓
- 作者：✓ (Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan — matches arXiv/ICLR)
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (ICLR 2023)
- ID：N/A (no arXiv ID claimed; actual arXiv ID is 2210.03629)

### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools
- 真实性：✓
- 作者：✓ (Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas — matches NeurIPS proceedings)
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A (no arXiv ID claimed; actual arXiv ID is 2302.04761)

### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models
- 真实性：✓
- 作者：✓ (Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio — matches arXiv)
- 年份：✓ (2023)
- 标题：✗ (official title uses lowercase "multi-step" and "tool-use": "ART: Automatic multi-step reasoning and tool-use for large language models" — minor capitalization difference)
- Venue：✓ (arXiv preprint arXiv:2303.09014)
- ID：✓ (2303.09014)

### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models
- 真实性：✓
- 作者：✓ (Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei an
…[truncated 2622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-26T10:26:36.722974+00:00_

Here are the verification results for all 10 entries:

---

### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?
- 真实性：✓
- 作者：✓
- 年份：✓ (2026, submitted March 2026)
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2604.19749)
- ID：✓ (2604.19749)

### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning
- 真实性：✓
- 作者：✓ (Sun, Chung-En; Liu, Linbo; Yan, Ge; Wang, Zimo; Weng, Tsui-Wei — all confirmed)
- 年份：✓ (2026, submitted May 2026)
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2605.09252)
- ID：✓ (2605.09252)

### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents
- 真实性：✓
- 作者：✓ (Zhang, Kaituo; Xiong, Zhen; Zhong, Mingyu; Jiang, Zhimeng; Yuan, Zhouyuan; Li, Zhecheng; Lin, Ying — all confirmed)
- 年份：✓ (2026, submitted April 30, 2026)
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2605.00136)
- ID：✓ (2605.00136)

### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling
- 真实性：✓
- 作者：✓ (Wu, Qinyuan; Das, Soumi; Amani, Mahsa; Nag, Arijit; Lee, Seungeon; Gummadi, Krishna P.; Ravichander, Abhilasha; Zafar, Muhammad Bilal — all confirmed)
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2605.00737)
- ID：✓ (2605.00737)

### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning
- 真实性：✓
- 作者：✓ (Ross, Stéphane; Gordon, Geoffrey J; Bagnell, Drew — confirmed, note the author's name is "Stéphane" with accent, matching the bib entry)
- 年份：✓ (2011)
- 标题：✓
- Venue：✓ (AISTATS 2011, pp. 627-635)
- ID：N/A

### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings
- 真实性：✓
- 作者：✓ (Hao, Shibo; Liu, Tianyang; Wang, Zhen; Hu, Zhiting — all confirmed)
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (NeurIPS 2023, presented as oral)
- ID：N/A

### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interac
…[truncated 1812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 26
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-26T10:26:36.723304+00:00_

Web search results for query: "Reflexion Language Agents with Verbal Reinforcement Learning Shinn NeurIPS 2023"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://openreview.net/pdf?id=vAElhFcKW6"}]

I found the research paper you're looking for. Here's what the search revealed:

"Reflexion" is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

The paper proposes an alternative approach called
…[truncated 820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:26:36.723582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tool Learning with Large Language Models A Survey Qu Changle arXiv 2405.17935"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tool Learning with Large Language Models A Survey Qu Changle arXiv 2405.17935"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-26T10:26:36.723847+00:00_

Web search results for query: "Mihatsch Neuneier "Risk-Sensitive Reinforcement Learning" Machine Learning 2002"

Links: [{"title":"Risk-Sensitive Reinforcement Learning | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1023/A:1017940631555"},{"title":"Risk-Sensitive Reinforcement Learning Applied to Control ...","url":"https://arxiv.org/pdf/1109.2147"},{"title":"Risk-Sensitive Reinforcement Learning","url":"https://www.researchgate.net/publication/225256871_Risk-Sensitive_Reinforcement_Learning"},{"title":"[PDF] Risk-Sensitive Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Risk-Sensitive-Reinforcement-Learning-Mihatsch-Neuneier/165f4a4bc8080093c89b8e9916b779aee8b37b81"},{"title":"Risk Sensitive Reinforcement Learning","url":"https://papers.nips.cc/paper/1583-risk-sensitive-reinforcement-learning"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Risk-sensitive+reinforcement+learning&amp=&author=O.+Mihatsch&amp=&author=R.+Neuneier&amp=&publication_year=2002&amp=&journal=Mach.+Learn.&amp=&pages=267-290&amp=&doi=10.1023/A:1017940631555"},{"title":"Risk-sensitive reinforcement learning | Proceedings of the First ACM International Conference on AI in Finance","url":"https://dl.acm.org/doi/10.1145/3383455.3422519"},{"title":"(PDF) Risk-Sensitive Reinforcement Learning","url":"https://www.researchgate.net/publication/261441730_Risk-Sensitive_Reinforcement_Learning"},{"title":"Risk-sensitive reinforcement learning applied to control under constraints | Journal of Artificial Intelligence Research","url":"https://dl.acm.org/doi/10.5555/1622519.1622522"},{"title":"Epistemic Risk-Sensitive Reinforcement Learning","url":"https://arxiv.org/pdf/1906.06273"}]

I found the paper you're looking for. The paper "Risk-Sensitive Reinforcement Learning" by Mihatsch, O. and Neuneier, R. was published in Machine Learning 49, 267–290 (2002).

The paper addresses the fact that most re
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:26:36.724139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolACE ICLR 2025 authors \"Weiwen Zhang\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolACE ICLR 2025 authors \"Weiwen Zhang\" full author list"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-26T10:26:36.724390+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Achiam \"Constrained Policy Optimization\" ICML 2017 pages proceedings volume 70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Achiam \"Constrained Policy Optimization\" ICML 2017 pages proceedings volume 70"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:26:36.724599+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Webb 2023 \"Reworking wild bootstrap\" Canadian Journal Economics volume issue pages author first name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Webb 2023 \"Reworking wild bootstrap\" Canadian Journal Economics volume issue pages author first name"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-26T10:26:36.724822+00:00_

Web search results for query: "Achiam "Constrained Policy Optimization" ICML 2017 pages proceedings volume 70"

Links: [{"title":"Constrained policy optimization | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305384"},{"title":"Constrained Policy Optimization","url":"https://proceedings.mlr.press/v70/achiam17a.html"},{"title":"[1705.10528] Constrained Policy Optimization","url":"https://arxiv.org/abs/1705.10528"},{"title":"[PDF] Constrained Policy Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Constrained-Policy-Optimization-Achiam-Held/7a4193d0b042643a8bb9ec262ed7f9d509bdb12e"},{"title":"Constrained Policy Optimization | Tejaswi Kasarla","url":"https://tkasarla.github.io/2017/10/19/constrained-policy-optimization/"},{"title":"Constrained Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/317240991_Constrained_Policy_Optimization"},{"title":"Constrained Policy Optimization","url":"https://www.ri.cmu.edu/app/uploads/2017/11/1705.10528.pdf"},{"title":"Constrained update projection approach to safe policy optimization | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3600932"}]

Based on the search results, I found the information you requested:

The paper "Constrained Policy Optimization" by Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel was published in the Proceedings of the 34th International Conference on Machine Learning, volume 70, pages 22-31, in 2017.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-26T10:26:36.725074+00:00_

Web search results for query: "Webb 2023 "Reworking wild bootstrap" Canadian Journal Economics volume issue pages author first name"

Links: [{"title":"Reworking wild bootstrap‐based inference for clustered errors - Webb - 2023 - Canadian Journal of Economics/Revue canadienne d'économique - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/caje.12661"},{"title":"Reworking wild bootstrap‐based inference for clustered errors - No. 56-3, August 2023 - Canadian Journal of Economics - Books and Journals - VLEX 1042749625 - vLex","url":"https://ca.vlex.com/vid/reworking-wild-bootstrapbased-inference-1042749625"},{"title":"Reworking Wild Bootstrap Based Inference For Clustered Errors","url":"https://ideas.repec.org/p/qed/wpaper/1315.html"},{"title":"Reworking wild bootstrap‐based inference for clustered errors","url":"https://ideas.repec.org/a/wly/canjec/v56y2023i3p839-858.html"},{"title":"Literature on the Wild Bootstrap and Clustered Inference in Regression Models • fwildclusterboot","url":"https://s3alfisc.github.io/fwildclusterboot/articles/Literature.html"},{"title":"Replication Data and Code for: Reworking Wild Bootstrap Based Inference for Clustered Errors - Canadian Journal of Economics (CJE)","url":"https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/BBZFOY"},{"title":"Matt Webb - Research","url":"https://sites.google.com/site/matthewdwebb/r"},{"title":"Matthew D. Webb - Economics","url":"https://carleton.ca/economics/people/webb-matthew-d/"},{"title":"Cluster-robust inference: A guide to empirical practice","url":"https://ideas.repec.org/a/eee/econom/v232y2023i2p272-299.html"}]

Based on the search results, here is the information about the publication:

**Author:** Matthew D. Webb (first name: Matthew)

**Title:** Reworking wild bootstrap-based inference for clustered errors

**Journal:** Canadian Journal of Economics/Revue canadienne d'économique

**Volume:** 56

**Issue:** 3

**Pages:** 839-858

**Year:** 2023 (published i
…[truncated 112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-26T10:26:36.725318+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Gemma 2: Improving Open Language Models at a Practical Size\" arXiv 2408.00118"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Gemma 2: Improving Open Language Models at a Practical Size\" arXiv 2408.00118"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:26:36.725551+00:00_

Web search results for query: "Natarajan Dhillon Ravikumar Tewari "Learning with Noisy Labels" NeurIPS 2013"

Links: [{"title":"Learning with Noisy Labels Nagarajan Natarajan Inderjit S. Dhillon","url":"https://proceedings.neurips.cc/paper/5073-learning-with-noisy-labels.pdf"},{"title":"Learning with noisy labels | Request PDF","url":"https://www.researchgate.net/publication/285956588_Learning_with_noisy_labels"},{"title":"Learning with Noisy Labels | Center for Big Data Analytics","url":"https://bigdata.oden.utexas.edu/publication/learning-with-noisy-labels-2/"},{"title":"dblp: Learning with Noisy Labels.","url":"https://dblp.org/rec/conf/nips/NatarajanDRT13.html"},{"title":"Learning from Noisy Labels with No Change to the Training Process","url":"https://proceedings.mlr.press/v139/zhang21k/zhang21k.pdf"},{"title":"Learning with noisy labels — the Research Networking System","url":"https://researchers.dellmed.utexas.edu/en/publications/learning-with-noisy-labels"},{"title":"Learning with Noisy Labels - Nagarajan Natarajan","url":"https://scispace.com/papers/learning-with-noisy-labels-9mxpknjttv"},{"title":"IJCAI 2021 Tutorial - Learning with Noisy Supervision","url":"https://wsl-workshop.github.io/ijcai21-tutorial"}]

The search results show that "Learning with Noisy Labels" was authored by Nagarajan Natarajan, Inderjit S. Dhillon, Pradeep Ravikumar, and Ambuj Tewari. 

The paper was published in Neural Information Processing Systems (NIPS) in December 2013.

The paper theoretically studies binary classification in the presence of random classification noise, where labels have independently been flipped with some small probability, and the random label noise is class-conditional with the flip probability depending on the class.

The paper is available as a PDF from the NeurIPS proceedings and appears to be a foundational work on learning from noisy labels, introducing methods for correcting surrogate loss functions to handle class-conditional label noise.


REMINDE
…[truncated 93 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-26T10:26:36.725775+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Northcutt Jiang Chuang \"Confident Learning: Estimating Uncertainty in Dataset Labels\" JAIR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Northcutt Jiang Chuang \"Confident Learning: Estimating Uncertainty in Dataset Labels\" JAIR 2021"
  }
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:26:36.725968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"DivideMix: Learning with Noisy Labels as Semi-supervised Learning\" Li Socher Hoi ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"DivideMix: Learning with Noisy Labels as Semi-supervised Learning\" Li Socher Hoi ICLR 2020"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T10:26:36.726224+00:00_

Web search results for query: ""Budget-Aware Agentic Routing via Boundary-Guided Training" arXiv 2602.21227"

Links: [{"title":"Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/pdf/2602.21227"},{"title":"[2602.21227] Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/abs/2602.21227"},{"title":"[2602.11541v1] Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use","url":"https://arxiv.org/abs/2602.11541v1"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"Budget-Aware Routing for Long Clinical Text","url":"https://arxiv.org/html/2605.00336"},{"title":"[2602.11541] Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use","url":"https://arxiv.org/abs/2602.11541"},{"title":"[2604.03527] Explainable Model Routing for Agentic Workflows","url":"https://arxiv.org/abs/2604.03527"}]

I found the paper! Here's what it's about:

"Budget-Aware Agentic Routing" selects between a cheap and an expensive model at each step to optimize the cost–success frontier and to operate under strict per-task budgets.

The paper addresses a key challenge: As LLMs evolve into autonomous agents executing long-horizon workflows, invoking a high-capability model at every step becomes economically unsustainable, and agentic routing is a sequential, path-dependent problem where early mistakes compound and feedback is often at the end of the episode.

**Key Contributions:**

The authors profile tasks into an intrinsic difficulty taxonomy (Easy/Hard/Intractable) and propose Boundary-Guided Supervised Fine-Tuning (BoSFT), which provides unambiguous labels for Easy and Intractable tasks while synthesizing cost-effective proxies for Hard tasks through stratified sampling.

They also introduce Boundary-Guided Policy Optimization (BoPO), an online reinforcement learning method that prevents the common "al
…[truncated 284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-26T10:26:36.726499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ng Harada Russell \"Policy Invariance Under Reward Transformations\" reward shaping ICML 1999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ng Harada Russell \"Policy Invariance Under Reward Transformations\" reward shaping ICML 1999"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:26:36.726748+00:00_

Web search results for query: ""Verified Critical Step Optimization for LLM Agents" Li Zeng Fang arXiv 2602.03412"

Links: [{"title":"[2602.03412] Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/abs/2602.03412"},{"title":"Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/html/2602.03412v1"},{"title":"Verified Critical Step Optimization for LLM Agents Mukai Li†,1,2","url":"https://arxiv.org/pdf/2602.03412"},{"title":"GitHub - kiaia/CSO: Verified Critical Step Optimization for LLM Agents(CSO) · GitHub","url":"https://github.com/kiaia/CSO"},{"title":"GPO: Learning from Critical Steps to Improve LLM Reasoning","url":"https://arxiv.org/html/2509.16456v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662"},{"title":"Hierarchical Reinforcement Learning with Augmented Step-Level Transitions for LLM Agents","url":"https://arxiv.org/html/2604.05808"},{"title":"Self-Improving LLM Agents at Test-Time","url":"https://arxiv.org/html/2510.07841v1"}]

Based on the search results, here's what I found about this research:

## Paper Overview

The paper "Verified Critical Step Optimization for LLM Agents" was authored by Mukai Li, Qingcheng Zeng, Tianqing Fang, Zhenwen Liang, Linfeng Song, Qi Liu, Haitao Mi, and Dong Yu from Tencent AI Lab, The University of Hong Kong, and Northwestern University.

## Main Contribution

The paper proposes Critical Step Optimization (CSO), which focuses preference learning on verified critical steps—decision points where alternate actions demonstrably flip task outcomes from failure to success.

## Problem Statement

Prior work faces fundamental challenges: outcome-only rewards fail to precisely attribute credit to intermediate steps, estimated step-level rewards introduce systematic noise, and Monte Carlo sampling approaches for step reward estimation incur prohibitive computational cost.

## Methodology

The method start
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:26:36.727056+00:00_

Web search results for query: ""SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph" Li Wang EACL 2026"

Links: [{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.247/"},{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"Step-level Advantage Assignment for Long-horizon Agents ...","url":"https://aclanthology.org/2026.findings-eacl.247.pdf"},{"title":"SALT: Step-level advantage assignment for long-horizon agents via trajectory graph - Amazon Science","url":"https://www.amazon.science/publications/salt-step-level-advantage-assignment-for-long-horizon-agents-via-trajectory-graph"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph | Request PDF","url":"https://www.researchgate.net/publication/403067374_SALT_Step-level_Advantage_Assignment_for_Long-horizon_Agents_via_Trajectory_Graph"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://chatpaper.com/chatpaper/paper/202952"},{"title":"Jiazheng Li","url":"https://lijiazheng0917.github.io/"}]

Based on the search results, here's what I found about the SALT paper:

## SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph

This paper was published in the Findings of the Association for Computational Linguistics: EACL 2026.

**Authors:** The paper is authored by Jiazheng Li, Yawei Wang, Qiaojing Yan, Yijun Tian, Zhichao Xu, Huan Song, Panpan Xu, and Lin Lee Cheong.

**Main Contribution:** The paper proposes SALT, a novel and lightweight framework that provides a finer-grained advantage assignment, derived solely from outcome rewards. This is achieved by constructing a graph from trajectories of the same prompt, which allows quantifying the quality of eac
…[truncated 618 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:26:36.727352+00:00_

Web search results for query: ""Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour" Gyevnár arXiv 2505.17801"

Links: [{"title":"[2505.17801] Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/abs/2505.17801"},{"title":"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/html/2505.17801"},{"title":"Integrating Counterfactual Simulations with Language Models","url":"https://arxiv.org/pdf/2505.17801"},{"title":"GitHub - gyevnarb/axis: Agentic Explanations via Interrogative Simulations · GitHub","url":"https://github.com/gyevnarb/axis"},{"title":"publications | Bálint Gyevnár","url":"https://gbalint.me/publications/"},{"title":"Towards Ethical Multi-Agent Systems of Large Language Models: A Mechanistic Interpretability Perspective","url":"https://www.researchgate.net/publication/398356965_Towards_Ethical_Multi-Agent_Systems_of_Large_Language_Models_A_Mechanistic_Interpretability_Perspective"}]

I found the paper you're looking for! Here's what the search revealed:

## Paper Overview

The paper proposes AXIS (Agentic eXplanations via Interrogative Simulation), which leverages the counterfactual effect size model and LLMs to generate human-centred action explanations for multi-agent policies by having an LLM interrogate an environment simulator using prompts like 'whatif' and 'remove' to observe and synthesise counterfactual information over multiple rounds.

## Key Motivation

Autonomous multi-agent systems are useful for automating complex tasks but raise trust concerns due to risks such as miscoordination or goal misalignment. Explainability is vital for users' trust calibration, but explainable MAS face challenges due to complex environments, the human factor, and non-standardised evaluation.

## Evaluation Results

Compared to baselines, AXIS improves perceived explanation correct
…[truncated 570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:26:36.727646+00:00_

Web search results for query: ""Gemma 2: Improving Open Language Models at a Practical Size" arXiv 2408.00118"

Links: [{"title":"[2408.00118] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v1"},{"title":"2024-06-27 Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/pdf/2408.00118"},{"title":"(PDF) Gemma 2: Improving Open Language Models at a Practical Size","url":"https://www.researchgate.net/publication/382797528_Gemma_2_Improving_Open_Language_Models_at_a_Practical_Size"},{"title":"Paper page - Gemma 2: Improving Open Language Models at a Practical Size","url":"https://huggingface.co/papers/2408.00118"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240800118G/abstract"},{"title":"[PDF] Gemma 2: Improving Open Language Models at a Practical Size | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gemma-2:-Improving-Open-Language-Models-at-a-Size-Riviere-Pathak/ec2ce4e38af8bc82f1b8928ba51a84911bad0cc6"},{"title":"[2408.00118v1] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v1"},{"title":"[2408.00118v3] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v3"}]

I found the research paper you're looking for. Here's a summary of the key information about this paper:

**Title:** "Gemma 2: Improving Open Language Models at a Practical Size"

**arXiv ID:** 2408.00118

**What it's about:** The paper introduces Gemma 2, a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters.

**Key technical contributions:** The new version applies several known technical modifications to the Transformer architecture,
…[truncated 655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-26T10:26:36.727925+00:00_

Web search results for query: "Ng Harada Russell "Policy Invariance Under Reward Transformations" reward shaping ICML 1999"

Links: [{"title":"Policy Invariance Under Reward Transformations | Proceedings of the Sixteenth International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/645528.657613"},{"title":"[PDF] Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Policy-Invariance-Under-Reward-Transformations:-and-Ng-Harada/94066dc12fe31e96af7557838159bde598cb4f10"},{"title":"Publications policy invariance under reward transformations: theory and application to reward shaping","url":"https://www.cs.utexas.edu/~shivaram/readings/b2hd-NgHR1999.html"},{"title":"(Open Access) Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (1999) | Andrew Y. Ng | 2376 Citations","url":"https://scispace.com/papers/policy-invariance-under-reward-transformations-theory-and-41w7bsjxkj"},{"title":"(PDF) Policy Invariance under Reward Transformations for Multi-Objective Reinforcement Learning","url":"https://www.researchgate.net/publication/316839917_Policy_Invariance_under_Reward_Transformations_for_Multi-Objective_Reinforcement_Learning"},{"title":"Policy Invariance under Reward Transformations for Multi- ...","url":"https://eprints.whiterose.ac.uk/id/eprint/118049/1/MO_PBRS_R3.pdf"},{"title":"Improving the Effectiveness of Potential-Based Reward Shaping in Reinforcement Learning","url":"https://arxiv.org/html/2502.01307v1"},{"title":"Expressing Arbitrary Reward Functions as Potential-Based Advice","url":"https://ai.vub.ac.be/sites/default/files/harutyunyan-907-aaai15.pdf"}]

I've found the paper you're looking for! Here are the key details:

"Policy Invariance Under Reward Transformations" is authored by Andrew Y. Ng, Daishi Harada, and Stuart J. Russell and was published in ICML '99 (Proceedings of the Sixteenth International
…[truncated 786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-26T10:26:36.728262+00:00_

Web search results for query: ""Abstract Counterfactuals for Language Model Agents" Pona Kazemi arXiv 2506.02946"

Links: [{"title":"[2506.02946] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946"},{"title":"[2506.02946v1] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946v1"},{"title":"Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/html/2506.02946v1"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=325&show=2000"},{"title":"Abstract Counterfactuals for Language Model Agents | OpenReview","url":"https://openreview.net/forum?id=ifMZw5fm7K"},{"title":"Abstract Counterfactuals for Language Model Agents Edoardo Pona","url":"https://openreview.net/pdf/c39308d32f99302b4eb8a97c6d7eae5b2e2c4466.pdf"},{"title":"NeurIPS Poster Abstract Counterfactuals for Language Model Agents","url":"https://neurips.cc/virtual/2025/poster/116537"},{"title":"[2505.17801] Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/abs/2505.17801"}]

I found the paper! Here's what I found about "Abstract Counterfactuals for Language Model Agents":

**Paper Details:**
- arXiv:2506.02946, submitted on June 3, 2025, with authors Edoardo Pona, Milad Kazemi, Yali Du, David Watson, and Nicola Paoletti

**Main Contribution:**
Counterfactual inference is a powerful tool for analyzing and evaluating autonomous agents, but its application to language model (LM) agents remains challenging, as existing work on counterfactuals in LMs has primarily focused on token-level counterfactuals, which are often inadequate for LM agents due to their open-ended action spaces.

**The Problem:**
Unlike traditional agents with fixed, clearly defined action spaces, the actions of LM agents are often implicit in the strings they output, making their action spaces difficult to define and interpret, and the mea
…[truncated 581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:26:36.728554+00:00_

Web search results for query: ""DivideMix: Learning with Noisy Labels as Semi-supervised Learning" Li Socher Hoi ICLR 2020"

Links: [{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning | OpenReview","url":"https://openreview.net/forum?id=HJgExaVtwr"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning [Quick Review]","url":"https://liner.com/review/dividemix-learning-with-noisy-labels-as-semisupervised-learning"},{"title":"ICLR: DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://iclr.cc/virtual_2020/poster_HJgExaVtwr.html"},{"title":"DIVIDEMIX: LEARNING WITH NOISY LABELS AS SEMI- ...","url":"https://openreview.net/pdf?id=HJgExaVtwr"},{"title":"[PDF] DivideMix: Learning with Noisy Labels as Semi-supervised Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivideMix:-Learning-with-Noisy-Labels-as-Learning-Li-Socher/ce435482acc0e195be8d8f002b2655b4c7b08be6"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised ...","url":"https://arxiv.org/pdf/2002.07394"},{"title":"[2002.07394] DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://arxiv.org/abs/2002.07394"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning | Request PDF","url":"https://www.researchgate.net/publication/339350598_DivideMix_Learning_with_Noisy_Labels_as_Semi-supervised_Learning"}]

I found the paper you're looking for! Here's what I found about "DivideMix: Learning with Noisy Labels as Semi-supervised Learning":

DivideMix is a novel framework for learning with noisy labels by leveraging semi-supervised learning techniques. It models the per-sample loss distribution with a mixture model to dynamically divide the training data into a labeled set with clean samples and an unlabeled set with noisy samples, and trains the model on both the labeled and unlabeled data in a semi-supervised manner.

To avoid confirmation bias, the method simult
…[truncated 603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T10:26:36.728852+00:00_

Web search results for query: "Northcutt Jiang Chuang "Confident Learning: Estimating Uncertainty in Dataset Labels" JAIR 2021"

Links: [{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels | Journal of Artificial Intelligence Research","url":"https://jair.org/index.php/jair/article/view/12125"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels | Request PDF","url":"https://www.researchgate.net/publication/350909446_Confident_Learning_Estimating_Uncertainty_in_Dataset_Labels"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://www.jair.org/index.php/jair/article/download/12125/26676/26691"},{"title":"Confident Learning: : Estimating Uncertainty in Dataset Labels: Journal of Artificial Intelligence Research: Vol 70, No null","url":"https://dl.acm.org/doi/10.1613/jair.1.12125"},{"title":"Journal of Artiﬁcial Intelligence Research 70 (2021) 1373-1411","url":"https://www.jair.org/index.php/jair/article/download/12125/26676/"},{"title":"dblp: Confident Learning: Estimating Uncertainty in Dataset Labels.","url":"https://dblp.org/rec/journals/jair/NorthcuttJC21.html"},{"title":"[1911.00068] Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://arxiv.org/abs/1911.00068"},{"title":"[PDF] Confident Learning: Estimating Uncertainty in Dataset Labels | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confident-Learning:-Estimating-Uncertainty-in-Northcutt-Jiang/cbaaa1154c491f9da2f050d3c22970e15bb7b52b"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://dspace.mit.edu/handle/1721.1/142946"}]

I found the paper! Here are the key details:

## Paper Information

The paper "Confident Learning: Estimating Uncertainty in Dataset Labels" was published on April 14, 2021 in the Journal of Artificial Intelligence Research by Curtis Northcutt from MIT, Lu Jiang from Google Research, and Isaac Chuang from MIT.

## Summary

Confident learning (C
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:26:36.729155+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 142 · 2026-05-26T10:26:36.729389+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:26:36.729611+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-SafetyBench Evaluating Safety LLM Agents arXiv 2412.14470"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-SafetyBench Evaluating Safety LLM Agents arXiv 2412.14470"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-26T10:26:36.729858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pearl \"Causality Models Reasoning and Inference\" Cambridge University Press 2nd edition 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pearl \"Causality Models Reasoning and Inference\" Cambridge University Press 2nd edition 2009"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-26T10:26:36.730116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rubin 1974 \"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\" Journal of Educational Psychology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rubin 1974 \"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\" Journal of Educational Psychology"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-26T10:26:36.730352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Switch Transformers Scaling Trillion Parameter Models Fedus Zoph Shazeer JMLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Switch Transformers Scaling Trillion Parameter Models Fedus Zoph Shazeer JMLR 2022"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:26:36.730582+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GShard Scaling Giant Models Conditional Computation Automatic Sharding Lepikhin ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GShard Scaling Giant Models Conditional Computation Automatic Sharding Lepikhin ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T10:26:36.730812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alshiekh \"Safe Reinforcement Learning via Shielding\" AAAI 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alshiekh \"Safe Reinforcement Learning via Shielding\" AAAI 2018"
  }
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-26T10:26:36.731070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kaushik Hovy Lipton \"Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\" ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kaushik Hovy Lipton \"Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\" ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-26T10:26:36.731305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FrugalGPT Chen Zaharia Zou arXiv 2305.05176"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FrugalGPT Chen Zaharia Zou arXiv 2305.05176"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T10:26:36.731557+00:00_

Web search results for query: "Switch Transformers Scaling Trillion Parameter Models Fedus Zoph Shazeer JMLR 2022"

Links: [{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/papers/v23/21-0998.html"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://jmlr.org/papers/volume23/21-0998/21-0998.pdf"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"[PDF] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Switch-Transformers:-Scaling-to-Trillion-Parameter-Fedus-Zoph/fdacf2a732f55befdc410ea927091cad3b791f13"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Request PDF","url":"https://www.researchgate.net/publication/348403003_Switch_Transformers_Scaling_to_Trillion_Parameter_Models_with_Simple_and_Efficient_Sparsity"},{"title":"[2101.03961v3] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961v3"},{"title":"Scaling to Trillion Parameter Models With Switch Transformers | by Zia Babar | Medium","url":"https://medium.com/@zbabar/scaling-to-trillion-parameter-models-with-switch-transformers-88ca5fb95e5c"},{"title":"[2101.03961v1] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961v1"}]

I found the paper you're searching for! Here's the information:

The paper "Switch Transformers: Scaling to Trillion Parame
…[truncated 997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:26:36.731852+00:00_

Web search results for query: "Agent-SafetyBench Evaluating Safety LLM Agents arXiv 2412.14470"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241214470Z/abstract"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/387263688_Agent-SafetyBench_Evaluating_the_Safety_of_LLM_Agents"},{"title":"[2412.14470v2] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"http://arxiv.org/abs/2412.14470v2"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"}]

Based on the search results, here's what I found about the paper:

## Agent-SafetyBench: Evaluating the Safety of LLM Agents

Agent-SafetyBench is a comprehensive benchmark designed to evaluate the safety of LLM agents. 

**Scale and Scope:**
The benchmark encompasses 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 common failure modes frequently encountered in unsafe interactions.

**Key Findings:**
An evaluation of 16 popular LLM agents reveals a concerning result: none of the agents achieves a safety score above 60%.

**Core Issues Ident
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-26T10:26:36.732157+00:00_

Web search results for query: "Pearl "Causality Models Reasoning and Inference" Cambridge University Press 2nd edition 2009"

Links: [{"title":"Amazon.com: Causality: Models, Reasoning and Inference: 9780521895606: Pearl, Judea: Books","url":"https://www.amazon.com/Causality-Reasoning-Inference-Judea-Pearl/dp/052189560X"},{"title":"Causality: Models, Reasoning and Inference (Hardcover) by Judea Pearl - Buy, Rent or Sell - BooksRun","url":"https://booksrun.com/9780521895606-causality-models-reasoning-and-inference-2nd-edition"},{"title":"Pearl, J. (2009) Causality Models, Reasoning, and Inference. 2nd Edition, Cambridge University Press. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4077487"},{"title":"Pearl, J. (2009) Causality Models, Reasoning and Inference. 2nd Edition, Cambridge University Press, Cambridge. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3432511"},{"title":"Causality : models, reasoning, and inference","url":"https://archive.illc.uva.nl/cil/uploaded_files/inlineitem/Pearl_2009_Causality.pdf"},{"title":"Causality: Models, Reasoning and Inference - Pearl, Judea: 9780521895606 - AbeBooks","url":"https://www.abebooks.com/9780521895606/Causality-Models-Reasoning-Inference-Pearl-052189560X/plp"},{"title":"Judea Pearl, Causality: Models, Reasoning and Inference - PhilPapers","url":"https://philpapers.org/rec/PEACMR"},{"title":"Pearl, J. (2009) Causality. Models, Reasoning, and Inference. 2nd Edition, Cambridge University Press, New York. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1111926"},{"title":"J. Pearl, “Causality Models, Reasoning, and Inference,” 2nd Edition, Cambridge University Press, Cambridge, 2009. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=918888"}]

I found infor
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T10:26:36.732463+00:00_

Web search results for query: "Alshiekh "Safe Reinforcement Learning via Shielding" AAAI 2018"

Links: [{"title":"Safe Reinforcement Learning via Shielding | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11797"},{"title":"Safe Reinforcement Learning via Shielding - Graz University of Technology","url":"https://tugraz.elsevierpure.com/en/publications/safe-reinforcement-learning-via-shielding/"},{"title":"(PDF) Safe Reinforcement Learning via Shielding","url":"https://www.researchgate.net/publication/319349967_Safe_Reinforcement_Learning_via_Shielding"},{"title":"[1708.08611] Safe Reinforcement Learning via Shielding","url":"https://arxiv.org/abs/1708.08611"},{"title":"Safe Reinforcement Learning via Shielding - AAAI","url":"https://aaai.org/papers/11797-safe-reinforcement-learning-via-shielding/"},{"title":"dblp: Safe Reinforcement Learning via Shielding.","url":"https://dblp.org/rec/conf/aaai/AlshiekhBEKNT18.html"},{"title":"Safe reinforcement learning via shielding under partial observability | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i12.26723"},{"title":"Probabilistic Shielding for Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.07671v1"}]

I found the paper you're looking for! Here are the key details:

The paper "Safe Reinforcement Learning via Shielding" was authored by Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu, and it was published in AAAI 2018, pages 2669-2678.

**Overview of the paper:**

The paper addresses how reinforcement learning algorithms discover policies that maximize reward, but do not necessarily guarantee safety during learning or execution phases. The authors intr
…[truncated 797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-26T10:26:36.732733+00:00_

Web search results for query: "Tool Learning with Large Language Models A Survey Qu Changle arXiv 2405.17935"

Links: [{"title":"[2405.17935] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935"},{"title":"Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/html/2405.17935v3"},{"title":"[2405.17935v3] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935v3"},{"title":"(PDF) Tool Learning with Large Language Models: A Survey","url":"https://www.researchgate.net/publication/380935103_Tool_Learning_with_Large_Language_Models_A_Survey"},{"title":"Paper page - Tool Learning with Large Language Models: A Survey","url":"https://huggingface.co/papers/2405.17935"},{"title":"Tool Learning with Large Language Models: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240517935Q/abstract"},{"title":"[PDF] Tool Learning with Large Language Models: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tool-Learning-with-Large-Language-Models:-A-Survey-Qu-Dai/0479547a69ffa48fe106137eba8358a9d8a2cc48"},{"title":"From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions","url":"https://arxiv.org/html/2410.08197v2"},{"title":"Tool Learning with Large Language Models: A Survey | PromptLayer","url":"https://www.promptlayer.com/research-papers/tool-learning-with-large-language-models-a-survey"}]

I found the paper you're looking for. Here's what the search reveals:

"Tool Learning with Large Language Models: A Survey" is authored by Changle Qu, Sunhao Dai, and others, with the arXiv identifier 2405.17935.

The survey addresses how tool learning with large language models has emerged as a promising paradigm for augmenting the capabilities of LLMs to tackle highly complex problems. The survey focuses on reviewing existing literature from two primary aspects: (1) why tool learning is beneficial and (2) how tool learning is i
…[truncated 627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T10:26:36.733037+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 7",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n59. automix-2024\nTitle: AutoMix: Automatically Mixing Language Models\nAuthors: Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket\nVenue: NeurIPS 2024\nYear: 2024\n\n60. mixture-of-depths-2024\nTitle: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\nAuthors: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam\nVenue: ICML 2024\nYear: 2024\n\n61. leviathan2023speculative\nTitle: Fast Inference from Transformers via Speculative Decoding\nAuthors: Leviathan, Yaniv and Kalman, Matan and Matias, Yossi\nVenue: ICML 2023\nYear: 2023\n\n62. bonagiri2025check\nTitle: Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\nAuthors: Bonagiri, Vamshi Krishna and Nguyen, Khanh and Plaut, Benjamin and Kumaraguru, Ponnurangam\nJournal: arXiv preprint arXiv:2510.16492\nYear: 2025\n\n63. manakul2023selfcheckgpt\nTitle: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\nAuthors: Potsawee Manakul and Adian Liusie and Mark J. F. Gales\nVenue: EMNLP 2023\nYear: 2023\n\n64. kadavath2022language\nTitle: Language Models (Mostly) Know What They Know\nAuthors: Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Geesaman and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan\nJournal: arXiv preprint arXiv:2207.05221\nYear: 2022\n\n65. xin2020deebert\nTitle: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\nAuthors: Ji Xin and Raphael Tang and Jaejun Lee and Yaoliang Yu and Jimmy Lin\nVenue: ACL 2020\nYear: 2020\n\n66. zhou2020bert\nTitle: BERT Loses Patience: Fast and Robust Inference with Early Exit\nAuthors: Wangchunshu Zhou and Canwen Xu and Tao Ge and Julian McAuley and Ke Xu and Furu Wei\nVenue: NeurIPS 2020, vol 33\nYear: 2020\n\n67. chow2015risk\nTitle: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\nAuthors: Yinlam Chow and Aviv Tamar and Shie Mannor and Marco Pavone\nVenue: NeurIPS 2015, vol 28\nYear: 2015\n\n68. tamar2015optimizing\nTitle: Optimizing the CVaR via Sampling\nAuthors: Aviv Tamar and Yonatan Glassner and Shie Mannor\nVenue: AAAI 2015\nYear: 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 7",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title, then verify: (1) paper exists, (2) author names correct, (3) year correct, (4) title correct, (5) venue correct, (6) arXiv ID correct if present. Today is May 2026, so 2025-2026 papers are real.\n\nReport your findings in this exact format for each entry:\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (details if wrong)\n- 年份：✓/✗ (details if wrong)\n- 标题：✓/✗ (details if wrong)\n- Venue：✓/✗ (details if wrong)\n- ID：✓/✗ or N/A (details if wrong)\n\nHere are the entries to verify:\n\n59. automix-2024\nTitle: AutoMix: Automatically Mixing Language Models\nAuthors: Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket\nVenue: NeurIPS 2024\nYear: 2024\n\n60. mixture-of-depths-2024\nTitle: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\nAuthors: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam\nVenue: ICML 2024\nYear: 2024\n\n61. leviathan2023speculative\nTitle: Fast Inference from Transformers via Speculative Decoding\nAuthors: Leviathan, Yaniv and Kalman, Matan and Matias, Yossi\nVenue: ICML 2023\nYear: 2023\n\n62. bonagiri2025check\nTitle: Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\nAuthors: Bonagiri, Vamshi Krishna and Nguyen, Khanh and Plaut, Benjamin and Kumaraguru, Ponnurangam\nJournal: arXiv preprint arXiv:2510.16492\nYear: 2025\n\n63. manakul2023selfcheckgpt\nTitle: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\nAuthors: Potsawee Manakul and Adian Liusie and Mark J. F. Gales\nVenue: EMNLP 2023\nYear: 2023\n\n64. kadavath2022language\nTitle: Language Models (Mostly) Know What They Know\nAuthors: Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Geesaman and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan\nJournal: arXiv preprint arXiv:2207.05221\nYear: 2022\n\n65. xin2020deebert\nTitle: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\nAuthors: Ji Xin and Raphael Tang and Jaejun Lee and Yaoliang Yu and Jimmy Lin\nVenue: ACL 2020\nYear: 2020\n\n66. zhou2020bert\nTitle: BERT Loses Patience: Fast and Robust Inference with Early Exit\nAuthors: Wangchunshu Zhou and Canwen Xu and Tao Ge and Julian McAuley and Ke Xu and Furu Wei\nVenue: NeurIPS 2020, vol 33\nYear: 2020\n\n67. chow2015risk\nTitle: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\nAuthors: Yinlam Chow and Aviv Tamar and Shie Mannor and Marco Pavone\nVenue: NeurIPS 2015, vol 28\nYear: 2015\n\n68. tamar2015optimizing\nTitle: Optimizing the CVaR via Sampling\nAuthors: Aviv Tamar and Yonatan Glassner and Shie Mannor\nVenue: AAAI 2015\nYear: 2015"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-26T10:26:36.733424+00:00_

Web search results for query: "GShard Scaling Giant Models Conditional Computation Automatic Sharding Lepikhin ICLR 2021"

Links: [{"title":"ICLR Poster GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://iclr.cc/virtual/2021/poster/3196"},{"title":"dblp: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding.","url":"https://dblp.org/rec/conf/iclr/LepikhinLXCFHKS21.html"},{"title":"GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | OpenReview","url":"https://openreview.net/forum?id=qrwe7XHTmYb"},{"title":"GShard: Scaling Giant Models With Conditional Computation and Automatic Sharding","url":"https://research.google/pubs/gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding/"},{"title":"GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding - researchr publication","url":"https://researchr.org/publication/LepikhinLXCFHKS21"},{"title":"Brief Review — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding-91393d98f7a4"},{"title":"[2006.16668] GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://arxiv.org/abs/2006.16668"},{"title":"Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, Zhifeng Chen · GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://slideslive.com/38953673/gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding"},{"title":"GSHARD: SCALING GIANT MODELS WITH CONDI","url":"https://openreview.net/pdf/cdb90e31da8446076492c5aef0c8c6ae35dd472a.pdf"}]

I found comprehensive information about the GShard paper. Here are the key details:

## Overview

GShard: 
…[truncated 1410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-26T10:26:36.733711+00:00_

Web search results for query: "ToolACE ICLR 2025 authors "Weiwen Zhang" full author list"

Links: [{"title":"Biography - Weiwen Liu","url":"https://wwliu555.github.io/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf"},{"title":"Tool Learning in the Wild: Empowering Language Models as Automatic Tool Agents | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714825"},{"title":"Published as a conference paper at ICLR 2026 TOOLACE-MT: NON-AUTOREGRESSIVE","url":"https://openreview.net/pdf/49af3922ccc97c3f6a8c85159576ac98513d1b42.pdf"},{"title":"ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/html/2409.00920v1"},{"title":"ICLR Poster ToolACE: Winning the Points of LLM Function Calling","url":"https://iclr.cc/virtual/2025/poster/30779"},{"title":"(PDF) ToolACE-R: Tool Learning with Adaptive Self-Refinement","url":"https://www.researchgate.net/publication/390439693_ToolACE-R_Tool_Learning_with_Adaptive_Self-Refinement"},{"title":"ICLR 2025 Conference Submissions","url":"https://openreview.net/submissions?page=393&venue=ICLR.cc/2025/Conference"}]

Based on the search results, I found the full author list for ToolACE published at ICLR 2025. The authors are: Weiwen Liu, Xu Huang, Xingshan Zeng, xinlong hao, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Zhengying Liu, Yuanqing Yu, Zezhong WANG, Yuxian Wang, Wu Ning, Yutai Hou, Bin Wang, Chuhan Wu, Wang Xinzhi, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, and Enhong Chen.

Note: The search results show "Weiwen Liu" as the first author, not "Weiwen Zhang" as mentioned in your query. It's possible there may have been a name variation or the query had a slight discrepancy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-26T10:26:36.734028+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tree of Thoughts Deliberate Problem Solving Large Language Models Yao NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tree of Thoughts Deliberate Problem Solving Large Language Models Yao NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-26T10:26:36.734294+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.17801 authors Gyevnár Lucas Albrecht Cohen 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.17801 authors Gyevnár Lucas Albrecht Cohen 2025"
  }
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:26:36.734548+00:00_

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
  "session": "worker_research_ref-audit-C_20260526T101534",
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

_source line 162 · 2026-05-26T10:26:36.734787+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-26T10:26:36.735051+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.20022 SALT step-level advantage authors Jiazheng Li full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.20022 SALT step-level advantage authors Jiazheng Li full author list"
  }
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T10:26:36.735309+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.21227 authors full list \"Budget-Aware Agentic Routing\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.21227 authors full list \"Budget-Aware Agentic Routing\""
  }
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T10:26:36.735561+00:00_

Web search results for query: "Rubin 1974 "Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies" Journal of Educational Psychology"

Links: [{"title":"Estimating causal effects of treatments in randomized and nonrandomized studies | Request PDF","url":"https://www.researchgate.net/publication/38414431_Estimating_causal_effects_of_treatments_in_randomized_and_nonrandomized_studies"},{"title":"ERIC - EJ118470 - Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies, Journal of Educational Psychology, 1974","url":"https://eric.ed.gov/?id=EJ118470"},{"title":"[PDF] Estimating causal effects of treatments in randomized and nonrandomized studies. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Estimating-causal-effects-of-treatments-in-and-Rubin/545122e2990590524459ec9b59ccac6ce71e3b6a"},{"title":"Rubin, D. (1974) Estimating Causal Effects of Treatments in Randomized and Non Randomized Studies. Journal of Educational Psychology, 66, 688-701. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2548121"},{"title":"Rubin, D.B. (1974) Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies. Journal of Educational Psychology, 66, 688-701. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4114686"},{"title":"Estimating causal effects of treatments in randomized and nonrandomized studies. (1974) | Donald B. Rubin | 9804 Citations","url":"https://scispace.com/papers/estimating-causal-effects-of-treatments-in-randomized-and-48sipamxi0"},{"title":"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies","url":"https://dash.harvard.edu/entities/publication/73120378-82c0-6bd4-e053-0100007fdf3b"},{"title":"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies","url":"https://www.ets.org/research/policy_research_reports
…[truncated 1141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-26T10:26:36.735856+00:00_

Web search results for query: "FrugalGPT Chen Zaharia Zou arXiv 2305.05176"

Links: [{"title":"[2305.05176] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://arxiv.org/abs/2305.05176"},{"title":"[2305.05176] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://ar5iv.labs.arxiv.org/html/2305.05176"},{"title":"FrugalGPT: How to Use Large Language Models While ...","url":"https://arxiv.org/pdf/2305.05176"},{"title":"FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://www.researchgate.net/publication/370633900_FrugalGPT_How_to_Use_Large_Language_Models_While_Reducing_Cost_and_Improving_Performance"},{"title":"Paper page - FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://huggingface.co/papers/2305.05176"},{"title":"[2305.05176v1] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://arxiv.org/abs/2305.05176v1"},{"title":"[PDF] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FrugalGPT:-How-to-Use-Large-Language-Models-While-Chen-Zaharia/585f8b9725f5f5e5495c3508d39f70d1c053e190"},{"title":"FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance - Summary","url":"https://portkey.ai/blog/frugalgpt-how-to-use-large-language-models-while-reducing-cost-and-improving-performance-summary/"},{"title":"dblp: FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance.","url":"https://dblp.org/rec/journals/corr/abs-2305-05176.html"}]

Based on the search results, here's what I found about the paper:

## FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

**Paper Details:**
- Authors: Lingjiao Chen, Matei Zahar
…[truncated 982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-26T10:26:36.736176+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeRoute Seanie Lee full author list arXiv 2502.12464"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeRoute Seanie Lee full author list arXiv 2502.12464"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T10:26:36.736454+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoMix: Automatically Mixing Language Models NeurIPS 2024 Madaan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoMix: Automatically Mixing Language Models NeurIPS 2024 Madaan"
  }
}
```

</details>

---

### Tool result

_source line 169 · 2026-05-26T10:26:36.736711+00:00_

Web search results for query: "Kaushik Hovy Lipton "Learning the Difference that Makes a Difference with Counterfactually-Augmented Data" ICLR 2020"

Links: [{"title":"[1909.12434] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://arxiv.org/abs/1909.12434"},{"title":"Learning The Difference That Makes A Difference With Counterfactually-Augmented Data | OpenReview","url":"https://openreview.net/forum?id=Sklgs0NFvr"},{"title":"ICLR: Learning The Difference That Makes A Difference With Counterfactually-Augmented Data","url":"https://iclr.cc/virtual_2020/poster_Sklgs0NFvr.html"},{"title":"Papers with Code - Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://paperswithcode.com/paper/learning-the-difference-that-makes-a"},{"title":"ICLR Poster Learning The Difference That Makes A Difference With Counterfactually-Augmented Data","url":"https://iclr.cc/virtual/2020/poster/1891"},{"title":"[PDF] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Learning-the-Difference-that-Makes-a-Difference-Kaushik-Hovy/47f1eb0dc42189ba7cf21b76598c8217eb1b6e05"},{"title":"GitHub - acmi-lab/counterfactually-augmented-data: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data · GitHub","url":"https://github.com/acmi-lab/counterfactually-augmented-data"},{"title":"[1909.12434v1] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://arxiv.org/abs/1909.12434v1"},{"title":"Learning the Difference that Makes a Difference with Counterfactually-Augmented Data | Request PDF","url":"https://www.researchgate.net/publication/336132499_Learning_the_Difference_that_Makes_a_Difference_with_Counterfactually-Augmented_Data"}]

I found the paper you're searching for. Here are the key details:

**Title:** Learning the Difference that M
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T10:26:36.737036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2412.14470 Agent-SafetyBench full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2412.14470 Agent-SafetyBench full author list"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T10:26:36.737279+00:00_

Web search results for query: "arxiv 2602.21227 authors full list "Budget-Aware Agentic Routing""

Links: [{"title":"[2602.21227] Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/abs/2602.21227"},{"title":"Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/pdf/2602.21227"},{"title":"[2602.11541v1] Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use","url":"https://arxiv.org/abs/2602.11541v1"},{"title":"[2602.06025] Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory","url":"https://arxiv.org/abs/2602.06025"},{"title":"[2602.11541] Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use","url":"https://arxiv.org/abs/2602.11541"},{"title":"(PDF) Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory","url":"https://www.researchgate.net/publication/400506087_Learning_Query-Aware_Budget-Tier_Routing_for_Runtime_Agent_Memory"},{"title":"[2604.03527] Explainable Model Routing for Agentic Workflows","url":"https://arxiv.org/abs/2604.03527"}]

Based on the search results, the authors of arxiv paper 2602.21227 "Budget-Aware Agentic Routing via Boundary-Guided Training" are: Caiqi Zhang, Menglin Xia, Xuchao Zhang, Daniel Madrigal, Ankur Mallick, Samuel Kessler, Victor Ruehle, and Saravan Rajmohan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-26T10:26:36.737539+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Switch Transformers JMLR volume 23 number 120 pages 1-39"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Switch Transformers JMLR volume 23 number 120 pages 1-39"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T10:26:36.737783+00:00_

Web search results for query: "Tree of Thoughts Deliberate Problem Solving Large Language Models Yao NeurIPS 2023"

Links: [{"title":"[2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/abs/2305.10601"},{"title":"GitHub - princeton-nlp/tree-of-thought-llm: [NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models · GitHub","url":"https://github.com/princeton-nlp/tree-of-thought-llm"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models - Princeton University","url":"https://collaborate.princeton.edu/en/publications/tree-of-thoughts-deliberate-problem-solving-with-large-language-m-2/"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/pdf/2305.10601"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf"},{"title":"Tree of Thoughts: A New Way to Unlock Problem-Solving in Large Language Models | by Research Graph | Medium","url":"https://medium.com/@researchgraph/tree-of-thoughts-a-new-way-to-unlock-problem-solving-in-large-language-models-cd50189e59a1"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html"},{"title":"[PDF] Tree of Thoughts: Deliberate Problem Solving with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tree-of-Thoughts:-Deliberate-Problem-Solving-with-Yao-Yu/2f3822eb380b5e753a6d579f31dfc3ec4c4a0820"},{"title":"NeurIPS 2023 Tree of Thoughts: Deliberate Problem Solving with Large Language Models Oral","url":"https://neurips.cc/virtual/2023/oral/73874"},{"title":"NeurIPS Poster Tree of Thoughts: Deliberate Problem Solving with Large Language Models","ur
…[truncated 1778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T10:26:36.738065+00:00_

Web search results for query: "arxiv 2510.20022 SALT step-level advantage authors Jiazheng Li full author list"

Links: [{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/html/2510.20022v1"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents","url":"https://arxiv.org/pdf/2510.20022"},{"title":"Paper page - SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://huggingface.co/papers/2510.20022"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2025-10-27&page=37&range=7"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.247/"},{"title":"TreeAdv: Tree-Structured Advantage Redistribution for Group-Based RL Lang Cao*","url":"https://www.arxiv.org/pdf/2601.03703"}]

The full author list for arxiv paper 2510.20022 "SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph" is:

1. Jiazheng Li
2. Yawei Wang
3. David Yan
4. Yijun Tian
5. Zhichao Xu
6. Huan Song
7. Panpan Xu
8. Lin Lee Cheong

Jiazheng Li is affiliated with the University of Connecticut, while the other authors are affiliated with Amazon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:26:36.738319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentBench Evaluating LLMs as Agents Liu Xiao ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentBench Evaluating LLMs as Agents Liu Xiao ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-26T10:26:36.738535+00:00_

Web search results for query: "arxiv 2412.14470 Agent-SafetyBench full author list"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/387263688_Agent-SafetyBench_Evaluating_the_Safety_of_LLM_Agents"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"[2412.14470v2] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"http://arxiv.org/abs/2412.14470v2"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"},{"title":"Regulating the Agency of LLM-based Agents Seán Boddy","url":"https://arxiv.org/pdf/2509.22735"},{"title":"RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments","url":"https://arxiv.org/html/2506.15253v1"}]

The full author list for arxiv paper 2412.14470 "Agent-SafetyBench: Evaluating the Safety of LLM Agents" is: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, and Minlie Huang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-26T10:26:36.738775+00:00_

Web search results for query: "AutoMix: Automatically Mixing Language Models NeurIPS 2024 Madaan"

Links: [{"title":"AutoMix: Automatically Mixing Language Models Pranjal Aggarwal♢∗ Aman Madaan♣∗","url":"https://arxiv.org/pdf/2310.12963"},{"title":"NeurIPS Poster AutoMix: Automatically Mixing Language Models","url":"https://neurips.cc/virtual/2024/poster/94293"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://proceedings.neurips.cc//paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html"},{"title":"[2310.12963] AutoMix: Automatically Mixing Language Models","url":"https://arxiv.org/abs/2310.12963"},{"title":"AutoMix: automatically mixing language models","url":"https://dl.acm.org/doi/10.5555/3737916.3742080"},{"title":"AutoMix: Automatically Mixing Language Models | OpenReview","url":"https://openreview.net/forum?id=e6WrwIvgzX"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://automix-llm.github.io/automix/"},{"title":"AutoMix: Automatically Mixing Language Models - proceedings.com","url":"https://www.proceedings.com/079017-4164.html"},{"title":"AutoMix: Automatically Mixing Language Models [Quick Review]","url":"https://liner.com/review/automix-automatically-mixing-language-models"}]

Based on the search results, here's what I found about AutoMix:

## Overview

AutoMix is an approach that strategically routes queries to larger language models, based on the approximate correctness of outputs from a smaller LM.

## Technical Contributions

The method has a few-shot self-verification mechanism, which estimates the reliability of its own outputs without requiring extensive training, and employs a POMDP based router that can effectively select an appropriately sized model, based on answer confidence.

## Performance and Impact

Experiments across five language models and five challenging datasets show that AutoMix consistently surpasses strong baselines, reducing computational cost by over 50%
…[truncated 481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-26T10:26:36.739044+00:00_

Web search results for query: "SafeRoute Seanie Lee full author list arXiv 2502.12464"

Links: [{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/html/2502.12464"},{"title":"[2502.12464] SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/abs/2502.12464"},{"title":"Paper page - SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://huggingface.co/papers/2502.12464"},{"title":"dblp: Seanie Lee","url":"https://dblp.org/pid/219/6771.html"},{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.105/"},{"title":"Seanie Lee","url":"https://www.catalyzex.com/author/Seanie%20Lee"},{"title":"Seanie Lee - Homepage","url":"https://seanie12.github.io/"},{"title":"Seanie Lee 님 - PhD student at KAIST AI | Apple Scholar in ...","url":"https://kr.linkedin.com/in/seanie-lee-601196b4"},{"title":"[1811.01147] SafeRoute: Learning to Navigate Streets Safely in an Urban Environment","url":"https://arxiv.org/abs/1811.01147"}]

Based on the search results, the full author list for SafeRoute (arXiv 2502.12464) is: Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, and Sung Ju Hwang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T10:26:36.739311+00:00_

Web search results for query: "arxiv 2505.17801 authors Gyevnár Lucas Albrecht Cohen 2025"

Links: [{"title":"[2505.17801] Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/abs/2505.17801"},{"title":"Bálint Gyevnár","url":"https://gbalint.me/"},{"title":"HEADD: Human Explanations for Autonomous Driving Decisions","url":"https://datashare.ed.ac.uk/handle/10283/8930"},{"title":"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/html/2505.17801"},{"title":"arXiv:2505.01868v1 [cs.CL] 3 May 2025","url":"https://www.arxiv.org/pdf/2505.01868"},{"title":"Physics Jan 2025","url":"https://arxiv.org/list/physics/2025-01?skip=1200&show=2000"},{"title":"Quantum Physics Feb 2025","url":"https://arxiv.org/list/quant-ph/2025-02?skip=75&show=1000"},{"title":"Arxiv","url":"https://www.arxiv.org/pdf/2505.09356"},{"title":"[2505.14766] This Time is Different: An Observability Perspective on Time Series Foundation Models","url":"https://arxiv.org/abs/2505.14766"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=1625&show=2000"}]

Based on the search results, I found information about arxiv paper 2505.17801:

**Title:** Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour

**Authors:** Bálint Gyevnár, Christopher G. Lucas, Stefano V. Albrecht, Shay B. Cohen

**Summary:** The paper addresses trust concerns in autonomous multi-agent systems (MAS) due to risks such as miscoordination or goal misalignment, with explainability vital for users' trust calibration. The authors propose AXIS (Agentic eXplanations via Interrogative Simulation), which generates human-centred action explanations for multi-agent policies by having an LLM interrogate an environment simulator using prompts like 'what-if' and 'remove' to observe and synthesise counterfactual information. The approach i
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-26T10:26:36.739582+00:00_

Web search results for query: "Switch Transformers JMLR volume 23 number 120 pages 1-39"

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/beta/papers/v23/21-0998.html"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity | BibSonomy","url":"https://www.bibsonomy.org/bibtex/278a9c4fb8cee182f863af53ce1cf41ca/andolab"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"JMLR Volume 23","url":"https://www.jmlr.org/papers/v23/"},{"title":"SwitchHead: Accelerating Transformers with Mixture-of-Experts Attention","url":"https://openreview.net/pdf?id=80SSl69GAz"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec16.pdf"}]

I found the paper you're looking for! "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity" was published in the Journal of Machine Learning Research (JMLR) Volume 23, Issue 120, Pages 1-39 in 2022. The paper was authored by William Fedus, Barret Zoph, and Noam Shazeer.

The paper introduces Mixture of Experts (MoE) models that select different parameters for each incoming example, resulting in a sparsely-activated model with an extremely large number of parameters but constant computational cost. The authors simplify the MoE routing algorithm and design improved models with reduced communication and computational costs.

The paper is available on the JMLR website at: https://jmlr.org/beta/papers/v23/21-0998.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-26T10:26:36.739847+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Depths Dynamically Allocating Compute Transformer ICML 2024 Raposo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Depths Dynamically Allocating Compute Transformer ICML 2024 Raposo"
  }
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-26T10:26:36.740113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SALT step-level advantage \"Qiaojing Yan\" OR \"David Yan\" author findings EACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SALT step-level advantage \"Qiaojing Yan\" OR \"David Yan\" author findings EACL"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-26T10:26:36.740361+00:00_

Web search results for query: "AgentBench Evaluating LLMs as Agents Liu Xiao ICLR 2024"

Links: [{"title":"[2308.03688] AgentBench: Evaluating LLMs as Agents","url":"https://arxiv.org/abs/2308.03688"},{"title":"ICLR Poster AgentBench: Evaluating LLMs as Agents","url":"https://iclr.cc/virtual/2024/poster/17388"},{"title":"AgentBench: Evaluating LLMs as Agents","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html"},{"title":"AgentBench: Evaluating LLMs as Agents | OpenReview","url":"https://openreview.net/forum?id=zAdUB0aCTQ"},{"title":"GitHub - THUDM/AgentBench: A Comprehensive Benchmark to Evaluate LLMs as Agents (ICLR'24) · GitHub","url":"https://github.com/THUDM/AgentBench"},{"title":"AGENTBENCH: EVALUATING LLMS AS AGENTS","url":"https://openreview.net/pdf/6eee0bd1fd98c135372baedb2a5644233a013bb2.pdf"},{"title":"AgentBench (AgentBench) - Agentic Design | Agentic Design Patterns","url":"https://agentic-design.ai/patterns/evaluation-monitoring/agentbench"},{"title":"[PDF] AgentBench: Evaluating LLMs as Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentBench:-Evaluating-LLMs-as-Agents-Liu-Yu/5dbf93a68b7fda600521f046dea35ea8ba9e884f"},{"title":"AgentBench: Evaluating LLMs as Agents","url":"https://arxiv.org/pdf/2308.03688"},{"title":"(PDF) AgentBench: Evaluating LLMs as Agents","url":"https://www.researchgate.net/publication/372962217_AgentBench_Evaluating_LLMs_as_Agents"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## AgentBench: Evaluating LLMs as Agents

AgentBench was published as a conference paper at ICLR 2024 with authors Xiao Liu, Hao Yu, Hanchen Zhang, and others from Tsinghua University, The Ohio State University, and UC Berkeley.

**Overview:**
AgentBench is a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent's reasoning and decision-making abilities. It assesses re
…[truncated 692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 184 · 2026-05-26T10:26:36.740617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2506.02946 \"Abstract Counterfactuals\" NeurIPS 2025 year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2506.02946 \"Abstract Counterfactuals\" NeurIPS 2025 year"
  }
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-26T10:26:36.740833+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-SafetyBench \"Zhexin Zhang\" \"Shiyao Cui\" \"Yida Lu\" authors complete list semantic scholar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-SafetyBench \"Zhexin Zhang\" \"Shiyao Cui\" \"Yida Lu\" authors complete list semantic scholar"
  }
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-26T10:26:36.741081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Language Agent Tree Search Unifies Reasoning Acting Planning Zhou Andy ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Language Agent Tree Search Unifies Reasoning Acting Planning Zhou Andy ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-26T10:26:36.741310+00:00_

Web search results for query: "Mixture-of-Depths Dynamically Allocating Compute Transformer ICML 2024 Raposo"

Links: [{"title":"[2404.02258] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/abs/2404.02258"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language","url":"https://arxiv.org/pdf/2404.02258"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/paper-review-mixture-of-depths-dddf00029026"},{"title":"[PDF] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mixture-of-Depths:-Dynamically-allocating-compute-Raposo-Ritter/a1f23f04421cdc62e80fe9f04c1ce60f4a6af9f0"},{"title":"Paper page - Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://huggingface.co/papers/2404.02258"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mixture-depths-dynamically-allocating-compute-transformer-based"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models, David Raposo+, N/A, arXiv'24 · Issue #1273 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1273"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/html/2404.02258v1"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69ce3feb84947a5132b622ec"},{"title":"GitHub - sramshetty/mixture-of-depths: An unofficial implementation of \"Mixture-o
…[truncated 1502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-26T10:26:36.741546+00:00_

Web search results for query: "arxiv 2506.02946 "Abstract Counterfactuals" NeurIPS 2025 year"

Links: [{"title":"[2506.02946] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946"},{"title":"[2506.02946v1] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946v1"},{"title":"Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/html/2506.02946"},{"title":"NeurIPS Poster Abstract Counterfactuals for Language Model Agents","url":"https://neurips.cc/virtual/2025/loc/mexico-city/poster/116537"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=325&show=2000"},{"title":"Counterfactual reasoning: an analysis of in-context emergence","url":"https://arxiv.org/html/2506.05188v2"}]

Based on the search results, here's what I found about arxiv 2506.02946:

The paper introduces "Abstract Counterfactuals," a framework that emphasises high-level characteristics of actions and interactions within an environment, enabling counterfactual reasoning tailored to user-relevant features.

The paper is titled "Abstract Counterfactuals for Language Model Agents" and was submitted on June 3, 2025, with authors including Edoardo Pona, Milad Kazemi, Yali Du, David Watson, and Nicola Paoletti.

The paper was accepted at NeurIPS 2025. The experiments demonstrate that the approach produces consistent and meaningful counterfactuals while minimising undesired side effects of token-level methods, with experiments conducted on text-based games and counterfactual text generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-26T10:26:36.741798+00:00_

Web search results for query: "Agent-SafetyBench "Zhexin Zhang" "Shiyao Cui" "Yida Lu" authors complete list semantic scholar"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241214470Z"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"},{"title":"dblp: Zhexin Zhang","url":"https://dblp.org/pid/225/5264.html"},{"title":"GitHub - thu-coai/AISafetyLab: AISafetyLab: A comprehensive framework covering safety attack, defense, evaluation and paper list. · GitHub","url":"https://github.com/thu-coai/AISafetyLab"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"Zhexin Zhang","url":"https://www.catalyzex.com/author/Zhexin%20Zhang"}]

Based on the search results, here is the complete list of authors for the Agent-SafetyBench paper:

The authors of Agent-SafetyBench: Evaluating the Safety of LLM Agents are: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, and Minlie Huang.

The paper was published on arXiv on December 19, 2024 (arXiv:2412.14470) and is available on Semantic Scholar and other academic platforms. The benchmark encompasses 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 c
…[truncated 169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T10:26:36.742105+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mixture-of-Depths\" Raposo ICML 2024 accepted proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mixture-of-Depths\" Raposo ICML 2024 accepted proceedings"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T10:26:36.742356+00:00_

Web search results for query: "SALT step-level advantage "Qiaojing Yan" OR "David Yan" author findings EACL"

Links: [{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Step-level Advantage Assignment for Long-horizon Agents ...","url":"https://aclanthology.org/2026.findings-eacl.247.pdf"},{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/html/2510.20022v1"},{"title":"dblp: Yijun Tian 0001","url":"https://dblp.org/pid/234/9123-1.html"},{"title":"Qiaojing Yan | IEEE Xplore Author Details","url":"https://ieeexplore.ieee.org/author/37085372444"},{"title":"David Yan","url":"https://david-yan1.github.io/"},{"title":"Qiaojing Yan","url":"https://sciprofiles.com/profile/author/bVk1Ulp2cm1ncEIwbEJETnJqRnR4QT09"}]

Based on the search results, I found information about the SALT paper:

SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph was authored by Jiazheng Li, Yawei Wang, Qiaojing Yan, Yijun Tian, Zhichao Xu, Huan Song, Panpan Xu, and Lin Lee Cheong. The paper was accepted as a Findings paper at EACL 2026.

SALT is a novel and lightweight framework that provides a finer-grained advantage assignment, derived solely from outcome rewards. The work addresses a limitation where mainstream reinforcement learning approaches for long-horizon tasks rely solely on sparse, outcome-based rewards, which becomes especially problematic for group-based RL algorithms lacking critic models, such as Group Relative Policy Optimization (GRPO).

Note: The author name in the paper is "Qiaojing Yan" (not "David Yan"). Based on the publication details, David Yan is a co-author from Amazon, while Qiaojing Yan appears to be listed at the same institution.


REMINDER: You MUST include the sources ab
…[truncated 59 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-26T10:26:36.742644+00:00_

Web search results for query: "Language Agent Tree Search Unifies Reasoning Acting Planning Zhou Andy ICML 2024"

Links: [{"title":"GitHub - lapisrocks/LanguageAgentTreeSearch: [ICML 2024] Official repository for \"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models\" · GitHub","url":"https://github.com/lapisrocks/LanguageAgentTreeSearch"},{"title":"LanguageAgentTreeSearch | [ICML 2024] Official repository for “Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models”","url":"http://lapisrocks.github.io/LanguageAgentTreeSearch/"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/language-agent-tree-search-unifies-reasoning-acting-and-planning-/"},{"title":"[2310.04406] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406"},{"title":"ICML Poster Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://icml.cc/virtual/2024/poster/33107"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in","url":"https://arxiv.org/pdf/2310.04406"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://proceedings.mlr.press/v235/zhou24r.html"},{"title":"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/language-agent-tree-search-unifies-reasoning-acting"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://arxiv.org/html/2310.04406v3"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## Paper Summary

"Language Agent Tree Search" (LATS) is a general framework that synergizes the capabilities of LMs in reason
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-26T10:26:36.742853+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Measuring Mathematical Problem Solving MATH Dataset Hendrycks NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Measuring Mathematical Problem Solving MATH Dataset Hendrycks NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-26T10:26:36.743066+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2026.findings-eacl.247 SALT authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2026.findings-eacl.247 SALT authors"
  }
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-26T10:26:36.743309+00:00_

Web search results for query: ""Mixture-of-Depths" Raposo ICML 2024 accepted proceedings"

Links: [{"title":"γ−MOD: EXPLORING MIXTURE-OF-DEPTH ADAPTA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf"},{"title":"UniMoD: Efficient Unified Multimodal Transformers with Mixture-of-Depths","url":"https://arxiv.org/pdf/2502.06474"},{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipedia-mixture-of-depths/"},{"title":"Raposo Et Al. - 2024 - Mixture-of-Depths Dynamically Allocating Compute | PDF | Routing | Applied Mathematics","url":"https://www.scribd.com/document/723064609/Raposo-et-al-2024-Mixture-of-Depths-Dynamically-allocating-compute"},{"title":"CNN Mixture-of-Depths Rinor Cakaj 1,2, Jens Mehnert 1, and Bin Yang2","url":"https://openaccess.thecvf.com/content/ACCV2024/papers/Cakaj_CNN_Mixture-of-Depths_ACCV_2024_paper.pdf"},{"title":"[PDF] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mixture-of-Depths:-Dynamically-allocating-compute-Raposo-Ritter/a1f23f04421cdc62e80fe9f04c1ce60f4a6af9f0"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/paper-review-mixture-of-depths-dddf00029026"},{"title":"REINFORCED ADAPTIVE ROUTING FOR MIXTURE-OF","url":"https://openreview.net/pdf/1f7aee75d6c7230669eca4fb80e138c2790fdb96.pdf"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69ce3feb84947a5132b622ec"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"}]

Based on the search results, here's what I found about "Mixture-of-Depth
…[truncated 963 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T10:26:36.743593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Lin Lee Cheong\" OR \"Lin-Lee Cheong\" SALT EACL Amazon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Lin Lee Cheong\" OR \"Lin-Lee Cheong\" SALT EACL Amazon"
  }
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-26T10:26:36.743849+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast Inference Transformers Speculative Decoding Leviathan Kalman Matias ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast Inference Transformers Speculative Decoding Leviathan Kalman Matias ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-26T10:26:36.744230+00:00_

Now I have all the information needed. Here are the verification results:

---

### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors
- 真实性：✓
- 作者：✓ (A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller)
- 年份：✓ (2008)
- 标题：✓
- Venue：✓ (The Review of Economics and Statistics, vol 90(3), pp 414-427)
- ID：N/A

### 32. [achiam2017cpo] — Constrained Policy Optimization
- 真实性：✓
- 作者：✓ (Joshua Achiam, David Held, Aviv Tamar, Pieter Abbeel)
- 年份：✓ (2017)
- 标题：✓
- Venue：✓ (ICML 2017, Proceedings of the 34th ICML, volume 70, pp 22-31)
- ID：N/A

### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling
- 真实性：✓
- 作者：✗ (第一作者是 **Weiwen Liu**，不是 "Weiwen Zhang"；完整作者列表包含 Weiwen Liu, Xu Huang, Xingshan Zeng 等 27 人)
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (ICLR 2025)
- ID：N/A

### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors
- 真实性：✓
- 作者：✓ (Matthew D. Webb)
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (Canadian Journal of Economics, vol 56(3), pp 839-858)
- ID：N/A

### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes
- 真实性：✓
- 作者：✓ (Teodor Mihai Moldovan, Pieter Abbeel)
- 年份：✓ (2012)
- 标题：✓
- Venue：✓ (ICML 2012)
- ID：N/A

### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks
- 真实性：✓
- 作者：✓ (Alex Graves)
- 年份：✓ (2016)
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:1603.08983)

### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- 真实性：✓
- 作者：✓ (Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori Hashimoto)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (ICLR 2024)
- ID：N/A

### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs
- 真实性：✓
- 作者：✓ (Seanie Lee 为第一作者，"and others" 可接受；完整列表为 Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, Sung Ju Hwang)
- 年份：✓ (2025)
- 标题：✗ (实际全称为 
…[truncated 869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 34
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-26T10:26:36.744545+00:00_

Web search results for query: "Measuring Mathematical Problem Solving MATH Dataset Hendrycks NeurIPS 2021"

Links: [{"title":"GitHub - hendrycks/math: The MATH Dataset (NeurIPS 2021) · GitHub","url":"https://github.com/hendrycks/math"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/be83ab3ecd0db773eb2dc1b0a17836a1-Paper-round2.pdf"},{"title":"[2103.03874] Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://arxiv.org/abs/2103.03874"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract-round2.html"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://arxiv.org/pdf/2103.03874"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset | OpenReview","url":"https://openreview.net/forum?id=7Bywt2mQsCe"},{"title":"[PDF] Measuring Mathematical Problem Solving With the MATH Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-Mathematical-Problem-Solving-With-the-Hendrycks-Burns/57d1e7ac339e783898f2c3b1af55737cbeee9fc5"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset | Request PDF","url":"https://www.researchgate.net/publication/349880265_Measuring_Mathematical_Problem_Solving_With_the_MATH_Dataset"},{"title":"--- dataset_info: features: - name: problem dtype: string - name: solution","url":"https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark/raw/main/README.md"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303874H/abstract"}]

I found comprehensive information about this research paper. Here's what the search results reveal:

## Overview

The paper "Measuring Mathematical Problem Solving With the
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-26T10:26:36.744828+00:00_

Web search results for query: ""Lin Lee Cheong" OR "Lin-Lee Cheong" SALT EACL Amazon"

Links: [{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"dblp: Yijun Tian 0001","url":"https://dblp.org/pid/234/9123-1.html"},{"title":"Lin Lee Cheong","url":"https://scholar.google.com/citations?user=TYvhX6wAAAAJ&hl=en"},{"title":"SALT: Step-level advantage assignment for long-horizon agents via trajectory graph - Amazon Science","url":"https://www.amazon.science/publications/salt-step-level-advantage-assignment-for-long-horizon-agents-via-trajectory-graph"},{"title":"Lin Lee Cheong - Amazon Science","url":"https://www.amazon.science/author/lin-lee-cheong"},{"title":"Lin Lee Cheong - Amazon Web Services (AWS) | LinkedIn","url":"https://www.linkedin.com/in/linleecheong/"},{"title":"Lin Lee | Working at amazon","url":"https://www.weekday.works/people/lin%20lee-cheong-linleecheong"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"Lin Lee Cheong - Manager & Senior Deep Learning Scientist, Machine Learning Solutions Lab (MLSL) @ Amazon Web Services - Crunchbase Person Profile","url":"https://www.crunchbase.com/person/lin-lee-cheong"}]

Based on the search results, I found information about Lin Lee Cheong and his work related to SALT and EACL:

Lin Lee Cheong is an author on the paper "SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph," which was accepted to the EACL findings.

Lin Lee Cheong works at Amazon AWS, and he is a Manager and Senior Deep Learning Scientist for Machine Learning Solutions Lab (MLSL) at Amazon Web Services (AWS).

The SALT paper addresses reinforcement learning for language agents. SALT is a novel and lightweight framework that provides a finer-grained advantage assi
…[truncated 305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-26T10:26:36.745138+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 Technical Report arXiv 2412.15115 Yang An"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 Technical Report arXiv 2412.15115 Yang An"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-26T10:26:36.745394+00:00_

Web search results for query: "aclanthology.org 2026.findings-eacl.247 SALT authors"

Links: [{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.247/"},{"title":"Findings of the Association for Computational Linguistics: EACL 2026 - ACL Anthology","url":"https://aclanthology.org/volumes/2026.findings-eacl/"},{"title":"Aclanthology","url":"https://aclanthology.org/2026.findings-eacl.247.pdf"},{"title":"Findings of the Association for Computational Linguistics (2026) - ACL Anthology","url":"https://aclanthology.org/events/findings-2026/"},{"title":"Findings of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/findings/"},{"title":"FINDINGS 2026 The 19th Conference of the European Chapter of the","url":"https://aclanthology.org/2026.findings-eacl.0.pdf"},{"title":"ACL Anthology - Google Groups","url":"https://groups.google.com/g/acl-anthology"}]

Based on the search results, the paper with the identifier aclanthology.org/2026.findings-eacl.247 is titled "SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph".

The authors are Jiazheng Li, Yawei Wang, Qiaojing Yan, Yijun Tian, Zhichao Xu, Huan Song, Panpan Xu, and Lin Lee Cheong.

The paper was published in Findings of the Association for Computational Linguistics: EACL 2026, pages 4709–4725, in Rabat, Morocco.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T10:26:36.745680+00:00_

Web search results for query: "Fast Inference Transformers Speculative Decoding Leviathan Kalman Matias ICML 2023"

Links: [{"title":"[2211.17192] Fast Inference from Transformers via Speculative Decoding","url":"https://arxiv.org/abs/2211.17192"},{"title":"Fast inference from transformers via speculative decoding | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3619203"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://proceedings.mlr.press/v202/leviathan23a.html"},{"title":"GitHub - romsto/Speculative-Decoding: Implementation of the paper Fast Inference from Transformers via Speculative Decoding, Leviathan et al. 2023. · GitHub","url":"https://github.com/romsto/Speculative-Decoding"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://openreview.net/pdf?id=C9NEblP8vS"},{"title":"Fast Inference from Transformers via Speculative Decoding - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/fast-inference-from-transformers-via-speculative-decoding/"},{"title":"ICML 2023 Fast Inference from Transformers via Speculative Decoding Oral","url":"https://icml.cc/virtual/2023/oral/25546"},{"title":"Speculative Decoding Reyna Abhyankar","url":"https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/spec-decoding.pdf"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://www.summarizepaper.com/en/arxiv-id/2211.17192v2/"},{"title":"dblp: Fast Inference from Transformers via Speculative Decoding.","url":"https://dblp.org/rec/conf/icml/LeviathanKM23.html"}]

I found the paper you're looking for! Here's what I found:

**Paper Details:**

The paper "Fast Inference from Transformers via Speculative Decoding" was authored by Yaniv Leviathan, Matan Kalman, and Yossi Matias, and it was presented at the 40th International Conference on Machine Learning (ICML 2023) held July 23-29, 2023.

**Key Contribution:*
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-26T10:26:36.745971+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Check Yourself Before You Wreck Yourself\" Selectively Quitting LLM Agent Safety Bonagiri arXiv 2510.16492"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Check Yourself Before You Wreck Yourself\" Selectively Quitting LLM Agent Safety Bonagiri arXiv 2510.16492"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-26T10:26:36.746241+00:00_

Web search results for query: "Qwen2.5 Technical Report arXiv 2412.15115 Yang An"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5 Technical Report","url":"https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"},{"title":"Paper page - Qwen2.5 Technical Report","url":"https://huggingface.co/papers/2412.15115"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"[2412.15115v1] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v1"},{"title":"dblp: Qwen2.5 Technical Report.","url":"https://dblp.org/rec/journals/corr/abs-2412-15115.html"},{"title":"[2412.15115v2] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v2"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"}]

I found the paper you're looking for! The Qwen2.5 Technical Report (arXiv 2412.15115) was authored by An Yang and many other Qwen team members, introducing a comprehensive series of large language models (LLMs) designed to meet diverse needs.

The paper was submitted on December 19, 2024, with a revision released on January 3, 2025. The Qwen2.5 models have been instrumental in training specialized models such as Qwen2.5-Math, Qwen2.5-Coder, QwQ, and multimodal models.

The paper is available on arXiv at: https://arxiv.org/abs/2412.15115


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-26T10:26:36.746520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 3 Herd of Models arXiv 2407.21783 Grattafiori Dubey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 3 Herd of Models arXiv 2407.21783 Grattafiori Dubey"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-26T10:26:36.746843+00:00_

Now I have all the information needed. The Agent-SafetyBench paper's actual author list from arXiv is: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, and Minlie Huang. The bib entry lists 9 authors including "Junhao Yang, Jie Liu, Renhao Wang, Jiangjie Li" which differ significantly. Let me compile the full report.

Here are the verification results:

---

### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents
- 真实性：✓
- 作者：✗ — 实际作者为 Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang（共7人）。bib 中列出了9人，其中 "Junhao Yang" 应为 "Junxiao Yang"，"Jie Liu"、"Renhao Wang"、"Jiangjie Li" 不在实际作者列表中，且缺少 "Hongning Wang"
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:2412.14470)

### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference
- 真实性：✓
- 作者：✓ (Judea Pearl)
- 年份：✓ (2009)
- 标题：✓
- Venue：✓ (Cambridge University Press, 2nd edition)
- ID：N/A

### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies
- 真实性：✓
- 作者：✓ (Donald B. Rubin)
- 年份：✓ (1974)
- 标题：✓
- Venue：✓ (Journal of Educational Psychology, vol 66, pp 688-701)
- ID：N/A

### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- 真实性：✓
- 作者：✓ (William Fedus, Barret Zoph, Noam Shazeer)
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (JMLR, vol 23(120), pp 1-39)
- ID：N/A

### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- 真实性：✓
- 作者：✓ (Lepikhin, Lee, Xu, Chen, Firat, Huang, Krikun, Shazeer, Chen)
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (ICLR 2021)
- ID：N/A

### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding
- 真实性：✓
- 作者：✓ (Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, Ufuk Topcu)
- 年份：✓ (2018)
- 标题：✓
- Venue：✓ (AAAI 2018)
- ID：N/A

### 57. [kaushik2020learning] — Learning the Difference th
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 24
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-26T10:26:36.747195+00:00_

Web search results for query: ""Check Yourself Before You Wreck Yourself" Selectively Quitting LLM Agent Safety Bonagiri arXiv 2510.16492"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492v3"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"(PDF) Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://www.researchgate.net/publication/396714988_Check_Yourself_Before_You_Wreck_Yourself_Selectively_Quitting_Improves_LLM_Agent_Safety"},{"title":"Ponnurangam Kumaraguru “PK” on X: \"🎉 New paper accepted to the NeurIPS 2025 “Reliable ML from Unreliable Data” Workshop: “Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety.” 📜 Preprint: https://t.co/bMWbFiER02 https://t.co/vKVz2cmssG\" / X","url":"https://x.com/ponguru/status/1986649704671957348"},{"title":"[1806.02307] Check yourself before you wreck yourself: Assessing discrete choice models through predictive simulations","url":"https://arxiv.org/abs/1806.02307"},{"title":"GitHub - timothyb0912/check-yourself: A case study in discrete choice model assessment with predictive simulations.","url":"https://github.com/timothyb0912/check-yourself"},{"title":"NeurIPS Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://neurips.cc/virtual/2025/loc/san-diego/125248"}]

I found the paper! Here's what I discovered:

"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" is a paper by Vamshi Krishna Bonagiri and co-authors that addresses safety in LLM agents operating in compl
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-26T10:26:36.747505+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Manakul Liusie Gales EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Manakul Liusie Gales EMNLP 2023"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-26T10:26:36.747765+00:00_

Web search results for query: "Llama 3 Herd of Models arXiv 2407.21783 Grattafiori Dubey"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"}]

I found the paper you're looking for! Here's what I found about arXiv 2407.21783:

**Paper Title:** "The Llama 3 Herd of Models"

**Authors:** The paper is authored by Aaron Grattafiori and 558 other authors (including Abhimanyu Dubey as a lead author in earlier versions).

**Key Information:**

The paper presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Their largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

The paper presents an extensive empirical evaluation of Llama 3, finding that it delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

They publicly released Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and their Llama Guard 3 model for input and output safety. The paper also presents results of experiments integrating image, video, and speech capabilities into Llama 3 via a
…[truncated 177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-26T10:26:36.748093+00:00_

Web search results for query: "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Manakul Liusie Gales EMNLP 2023"

Links: [{"title":"[2303.08896] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://arxiv.org/abs/2303.08896"},{"title":"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.557/"},{"title":"SELFCHECKGPT: Zero-Resource Black-Box Hallucination ...","url":"https://aclanthology.org/2023.emnlp-main.557.pdf"},{"title":"GitHub - potsawee/selfcheckgpt: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models · GitHub","url":"https://github.com/potsawee/selfcheckgpt"},{"title":"(PDF) SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://www.researchgate.net/publication/376402462_SelfCheckGPT_Zero-Resource_Black-Box_Hallucination_Detection_for_Generative_Large_Language_Models"},{"title":"Paper page - SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://huggingface.co/papers/2303.08896"},{"title":"[PDF] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelfCheckGPT:-Zero-Resource-Black-Box-Hallucination-Manakul-Liusie/7c1707db9aafd209aa93db3251e7ebd593d55876"},{"title":"EMNLP2023: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://virtual2023.emnlp.org/paper_349.html"},{"title":"[Quick Review] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://liner.com/review/selfcheckgpt-zeroresource-blackbox-hallucination-detection-for-generative-large-language-models"}]

I've found comprehensive 
…[truncated 1419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-26T10:26:36.748414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion arXiv 2303.11366 authors Noah Shinn Federico Cassano Edward Berman Ashwin Gopinath"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion arXiv 2303.11366 authors Noah Shinn Federico Cassano Edward Berman Ashwin Gopinath"
  }
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-26T10:26:36.748673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Language Models Mostly Know What They Know\" Kadavath arXiv 2207.05221"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Language Models Mostly Know What They Know\" Kadavath arXiv 2207.05221"
  }
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-26T10:26:36.748932+00:00_

Web search results for query: "Reflexion arXiv 2303.11366 authors Noah Shinn Federico Cassano Edward Berman Ashwin Gopinath"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"[2303.11366v1] Reflexion: an autonomous agent with dynamic memory and self-reflection","url":"https://web3.arxiv.org/abs/2303.11366v1"},{"title":"[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v4"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning citation","url":"https://duruofei.com/cites/Shinn2023Reflexion.html"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"[2303.11366v3] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v3"},{"title":"reflexion/README.md at main · noahshinn/reflexion","url":"https://github.com/noahshinn/reflexion/blob/main/README.md"},{"title":"(PDF) Reflexion: an autonomous agent with dynamic memory and self-reflection","url":"https://www.researchgate.net/publication/369414009_Reflexion_an_autonomous_agent_with_dynamic_memory_and_self-reflection"}]

Based on the search results, I found comprehensive information about the Reflexion paper with arXiv ID 2303.11366:

The paper "Reflexion: Language Agents with Verbal Reinforcement Learning" was authored by Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.

The authors are affiliated with: Noah Shinn, Federico Cassano, and Edward Berman at Northeastern University; Ashwin
…[truncated 580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-26T10:26:36.749340+00:00_

Now I have all the information needed. The key finding for SALT is that the bib entry lists "David Yan" but the ACL Anthology official version lists "Qiaojing Yan". Also, the bib entry has "Lin Lee Cheong" but the actual paper uses "Lin Lee Cheong" (matching). Let me compile the full report.

Here are the verification results:

### 41. [natarajan2013learning] — Learning with Noisy Labels
- 真实性：✓
- 作者：✓ Natarajan, Nagarajan; Dhillon, Inderjit S.; Ravikumar, Pradeep; Tewari, Ambuj — all correct
- 年份：✓ 2013
- 标题：✓ "Learning with Noisy Labels"
- Venue：✓ NeurIPS (NIPS) 2013
- ID：N/A

### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training
- 真实性：✓
- 作者：✗ Last author surname is **Rajmohan**, but the bib entry gives first name as "Saravan" — the actual author appears to be "Saravan Rajmohan" (need to confirm if full first name is correct; the rest of the authors match)
- 年份：✓ 2026
- 标题：✓ "Budget-Aware Agentic Routing via Boundary-Guided Training"
- Venue：✓ arXiv preprint
- ID：✓ arXiv:2602.21227

### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents
- 真实性：✓
- 作者：✓ Pona, Edoardo; Kazemi, Milad; Du, Yali; Watson, David; Paoletti, Nicola — all correct
- 年份：✓ 2025 (arXiv June 2025, accepted NeurIPS 2025)
- 标题：✓ "Abstract Counterfactuals for Language Model Agents"
- Venue：✗ Listed as "arXiv preprint" but the paper was accepted at **NeurIPS 2025**. The venue should be updated to NeurIPS 2025 for accuracy.
- ID：✓ arXiv:2506.02946

### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents
- 真实性：✓
- 作者：✓ Li, Mukai; Zeng, Qingcheng; Fang, Tianqing; Liang, Zhenwen; Song, Linfeng; Liu, Qi; Mi, Haitao; Yu, Dong — all correct
- 年份：✓ 2026
- 标题：✓ "Verified Critical Step Optimization for LLM Agents"
- Venue：✓ arXiv preprint
- ID：✓ arXiv:2602.03412

### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour
- 真实性：✓
- 作者：✓ Gyevnár, Bálint; Lucas, Christoph
…[truncated 2525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 32
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-26T10:26:36.749648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RouteLLM arXiv 2406.18665 full author list Isaac Ong Amjad Almahairi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RouteLLM arXiv 2406.18665 full author list Isaac Ong Amjad Almahairi"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-26T10:26:36.749911+00:00_

Web search results for query: ""Language Models Mostly Know What They Know" Kadavath arXiv 2207.05221"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"}]

I found the paper you're searching for. Here's the information:

**Title:** Language Models (Mostly) Know What They Know

**Authors:** Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Jo
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-26T10:26:36.750221+00:00_

Web search results for query: "RouteLLM arXiv 2406.18665 full author list Isaac Ong Amjad Almahairi"

Links: [{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"[2406.18665v1] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v1"},{"title":"[2406.18665v2] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v2"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Ong%2C+I.%2C+Almahairi%2C+A.%2C+Wu%2C+V.%2C+Chiang%2C+W.-L.%2C+Wu%2C+T.%2C+Gonzalez%2C+J.+E.%2C+Kadous%2C+M.+W.%2C+and+Stoica%2C+I.+Routellm%3A+Learning+to+route+llms+with+preference+data.+arXiv+preprint+arXiv%3A2406.18665+%282024%29."},{"title":"[2406.18665v3] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v3"},{"title":"GitHub - lm-sys/RouteLLM: A framework for serving and evaluating LLM routers - save LLM costs without compromising quality · GitHub","url":"https://github.com/lm-sys/RouteLLM"},{"title":"dblp: RouteLLM: Learning to Route LLMs with Preference Data.","url":"https://dblp.org/rec/journals/corr/abs-2406-18665.html"},{"title":"RouteLLM: Learning to Route LLMs from Preference Data","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html"},{"title":"dblp: Amjad Almahairi","url":"https://dblp.org/pid/167/5984.html"}]

Based on the search results, the full author list for RouteLLM (arXiv 2406.18665) is: Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, M Waleed Kadous, and Ion Stoica.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-26T10:26:36.750522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2103.03874 MATH dataset Hendrycks Burns Kadavath authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2103.03874 MATH dataset Hendrycks Burns Kadavath authors list"
  }
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-26T10:26:36.750784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Xin Tang Lee Yu Lin ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Xin Tang Lee Yu Lin ACL 2020"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-26T10:26:36.751059+00:00_

Web search results for query: "arxiv 2103.03874 MATH dataset Hendrycks Burns Kadavath authors list"

Links: [{"title":"[2103.03874] Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://arxiv.org/abs/2103.03874"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Hendrycks%2C+D.%2C+Burns%2C+C.%2C+Kadavath%2C+S.%2C+Arora%2C+A.%2C+Basart%2C+S.%2C+Tang%2C+E.%2C+Song%2C+D.%2C+and+Steinhardt%2C+J.+Measuring+mathematical+problem+solving+with+the+math+dataset.+arXiv+preprint+arXiv%3A2103.03874+%282021%29."},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://arxiv.org/pdf/2103.03874"},{"title":"GitHub - hendrycks/math: The MATH Dataset (NeurIPS 2021) · GitHub","url":"https://github.com/hendrycks/math"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset | Request PDF","url":"https://www.researchgate.net/publication/349880265_Measuring_Mathematical_Problem_Solving_With_the_MATH_Dataset"},{"title":"[PDF] Measuring Mathematical Problem Solving With the MATH Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-Mathematical-Problem-Solving-With-the-Hendrycks-Burns/57d1e7ac339e783898f2c3b1af55737cbeee9fc5"},{"title":"Paper page - Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://huggingface.co/papers/2103.03874"},{"title":"MathScale | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694024"},{"title":"Update README.md · nlile/hendrycks-MATH-benchmark at 465bcdb","url":"https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark/commit/465bcdb36f5962aa3512891498966df785fc3c18"},{"title":"lm-evaluation-harness/lm_eval/tasks/hendrycks_math/README.md at main · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/hendrycks_math/README.md"}]

Based on the search results, the authors of th
…[truncated 263 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-26T10:26:36.751356+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2407.21783 Llama 3 first author Grattafiori vs Dubey author change"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2407.21783 Llama 3 first author Grattafiori vs Dubey author change"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T10:26:36.751621+00:00_

Web search results for query: "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Xin Tang Lee Yu Lin ACL 2020"

Links: [{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.204/"},{"title":"GitHub - castorini/DeeBERT: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference · GitHub","url":"https://github.com/castorini/DeeBERT"},{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://cs.uwaterloo.ca/~jimmylin/publications/Xin_etal_ACL2020.pdf"},{"title":"ACL2020: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://virtual.acl2020.org/paper_main.204.html"},{"title":"[Quick Review] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://liner.com/review/deebert-dynamic-early-exiting-for-accelerating-bert-inference"},{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://papertalk.org/papertalks/6390"},{"title":"[2004.12993] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://arxiv.org/abs/2004.12993"},{"title":"dblp: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference.","url":"https://dblp.uni-trier.de/rec/conf/acl/XinTLYL20.html"},{"title":"[PDF] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeeBERT:-Dynamic-Early-Exiting-for-Accelerating-Xin-Tang/90a1491ac32e732c93773354e4e665794ed4d490"}]

I found comprehensive information about the DeeBERT paper. Here are the results:

## Paper Overview

DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference was published by Ji Xin, Raphael Tang, Jaejun Lee, Yaoliang Yu, and Jimmy Lin at ACL 2020.

## Main Contribution

The paper proposes DeeBERT, a method to accelerate BERT inference by allowing samples to exit earlier without passing through the entire model. Experiments show that DeeBERT is a
…[truncated 781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-26T10:26:36.751921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"BERT Loses Patience\" Fast Robust Inference Early Exit Zhou Xu Ge McAuley NeurIPS 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"BERT Loses Patience\" Fast Robust Inference Early Exit Zhou Xu Ge McAuley NeurIPS 2020"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-26T10:26:36.752214+00:00_

Web search results for query: "arXiv 2407.21783 Llama 3 first author Grattafiori vs Dubey author change"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"}]

Based on the search results, I can see that there was indeed a change in the first author of the arXiv paper 2407.21783 "The Llama 3 Herd of Models":

- In version 1 (submitted July 31, 2024), the first author was Abhimanyu Dubey
- In version 2 (revised August 15, 2024), the first author remained Abhimanyu Dubey
- In version 3 (last revised November 23, 2024), Aaron Grattafiori became the first author, with Abhimanyu Dubey as the second author

So the paper originally had Abhimanyu Dubey as the first author in versions 1 and 2, but this was changed to Aaron Grattafiori as the first author in version 3, with Dubey moving to second position.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-26T10:26:36.752505+00:00_

Web search results for query: ""BERT Loses Patience" Fast Robust Inference Early Exit Zhou Xu Ge McAuley NeurIPS 2020"

Links: [{"title":"[2006.04152] BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://arxiv.org/abs/2006.04152"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://proceedings.neurips.cc/paper/2020/hash/d4dd111a4fd973394238aca5c05bebe3-Abstract.html"},{"title":"GitHub - JetRunner/PABEE: Code for the paper \"BERT Loses Patience: Fast and Robust Inference with Early Exit\". · GitHub","url":"https://github.com/JetRunner/PABEE"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200604152Z/abstract"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://cseweb.ucsd.edu/~jmcauley/pdfs/nips20.pdf"},{"title":"BERT loses patience: Fast and robust inference with early exit - Beihang University","url":"https://research.buaa.edu.cn/en/publications/bert-loses-patience-fast-and-robust-inference-with-early-exit/"},{"title":"[PDF] BERT Loses Patience: Fast and Robust Inference with Early Exit | Semantic Scholar","url":"https://www.semanticscholar.org/paper/4abdbcf983f78cf3f5bf6e2032503f0e534f6ca8"},{"title":"[2006.04152v3] BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://arxiv.org/abs/2006.04152v3"},{"title":"BERT loses patience: fast and robust inference with early exit","url":"https://dl.acm.org/doi/abs/10.5555/3495724.3497263"},{"title":"[2006.04152v2] BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://arxiv.org/abs/2006.04152v2"}]

I found the paper "BERT Loses Patience: Fast and Robust Inference with Early Exit" for you. Here are the key details:

**Paper Information:**
- Authors: Wangchunshu Zhou, Canwen Xu, Tao Ge, Julian McAuley, Ke Xu, and Furu Wei
- Published at the 34th Conference on Neural Information Processing Systems (
…[truncated 917 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-26T10:26:36.752800+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2405.17935 \"Tool Learning with Large Language Models\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2405.17935 \"Tool Learning with Large Language Models\" full author list"
  }
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-26T10:26:36.753083+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Risk-Sensitive and Robust Decision-Making\" CVaR Optimization Chow Tamar Mannor Pavone NeurIPS 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Risk-Sensitive and Robust Decision-Making\" CVaR Optimization Chow Tamar Mannor Pavone NeurIPS 2015"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-26T10:26:36.753345+00:00_

Web search results for query: "arXiv 2405.17935 "Tool Learning with Large Language Models" full author list"

Links: [{"title":"[2405.17935] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935"},{"title":"[2405.17935v3] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935v3"},{"title":"Paper page - Tool Learning with Large Language Models: A Survey","url":"https://huggingface.co/papers/2405.17935"},{"title":"(PDF) Tool Learning with Large Language Models: A Survey","url":"https://www.researchgate.net/publication/380935103_Tool_Learning_with_Large_Language_Models_A_Survey"},{"title":"[PDF] Tool Learning with Large Language Models: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tool-Learning-with-Large-Language-Models:-A-Survey-Qu-Dai/0479547a69ffa48fe106137eba8358a9d8a2cc48"},{"title":"Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/pdf/2405.17935"},{"title":"From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions","url":"https://arxiv.org/html/2410.08197v2"},{"title":"Tool Learning with LLMs Survey","url":"https://www.emergentmind.com/papers/2405.17935"},{"title":"Towards Completeness-Oriented Tool Retrieval for Large Language Models","url":"https://arxiv.org/html/2405.16089"}]

Based on the search results, the full author list for arXiv paper 2405.17935 "Tool Learning with Large Language Models: A Survey" is: Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-26T10:26:36.753627+00:00_

Web search results for query: ""Risk-Sensitive and Robust Decision-Making" CVaR Optimization Chow Tamar Mannor Pavone NeurIPS 2015"

Links: [{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"https://proceedings.neurips.cc/paper/2015/hash/64223ccf70bbb65a3a4aceac37e21016-Abstract.html"},{"title":"[1506.02188] Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"https://arxiv.org/abs/1506.02188"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"http://papers.neurips.cc/paper/6014-risk-sensitive-and-robust-decision-making-a-cvar-optimization-approach.pdf"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach | Request PDF","url":"https://www.researchgate.net/publication/277959194_Risk-Sensitive_and_Robust_Decision-Making_a_CVaR_Optimization_Approach"},{"title":"Risk-sensitive and robust decision-making: A CVaR optimization approach - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/risk-sensitive-and-robust-decision-making-a-cvar-optimization-app-2/"},{"title":"[PDF] Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Risk-Sensitive-and-Robust-Decision-Making:-a-CVaR-Chow-Tamar/f583f9e720c16f6bb50f9d624b61c3bc851be008"},{"title":"dblp: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach.","url":"https://dblp.org/rec/conf/nips/ChowTMP15.html"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150602188C/abstract"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/aa91bc4a0f1ab6da6105c77e552d27e1"},{"title":"Risk-Sensitive and Robust Decision-Makin... - NIPS 2015","url":"https://nips2015.sched.com/event/5QQ5/risk-sens
…[truncated 1244 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-26T10:26:36.753929+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Optimizing the CVaR via Sampling\" Tamar Glassner Mannor AAAI 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Optimizing the CVaR via Sampling\" Tamar Glassner Mannor AAAI 2015"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-26T10:26:36.754210+00:00_

Web search results for query: ""Optimizing the CVaR via Sampling" Tamar Glassner Mannor AAAI 2015"

Links: [{"title":"[1404.3862] Optimizing the CVaR via Sampling","url":"https://arxiv.org/abs/1404.3862"},{"title":"Optimizing the CVaR via Sampling - AAAI","url":"https://aaai.org/papers/9561-optimizing-the-cvar-via-sampling/"},{"title":"Optimizing the CVaR via Sampling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/9561"},{"title":"CVaR Optimization via Sampling","url":"https://www.emergentmind.com/papers/1404.3862"},{"title":"Optimizing the CVaR via Sampling Aviv Tamar, Yonatan Glassner, and Shie Mannor","url":"https://cdn.aaai.org/ojs/9561/9561-13-13089-1-2-20201228.pdf"},{"title":"Optimizing the CVaR via Sampling | Request PDF","url":"https://www.researchgate.net/publication/280035978_Optimizing_the_CVaR_via_Sampling"},{"title":"[PDF] Optimizing the CVaR via Sampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/2e939ed3bb378ea966bf9f710fc1138f4e16ef38"},{"title":"Optimizing the CVaR via Sampling | Request PDF","url":"https://www.google.com/goto?url=CAESjwEBO6uMpdB4mOdMUIWE6oYtHXSOsPHVRycyJKV4Z3Wh_g4uMnd9xUsBpH83jz5NJl5jpvymICeOM4661VTMIzdi_H51z0uDwntc8UJixsOq11XKpmMcIL5kTNfgZCQ1eylM5TS8W1bNXuaWxqv88iiHLxeHbWrlHhIBzTfMuFSQw3ATJ-jZZvacV5M_Ir4j3A%3D%3D"}]

I found the paper you were searching for. Here's the information:

"Optimizing the CVaR via Sampling" was published by Tamar, Glassner, and Mannor in 2015 in the Proceedings of the AAAI Conference on Artificial Intelligence, volume 29(1).

**Paper Overview:**

The paper addresses Conditional Value at Risk (CVaR), a prominent risk measure used extensively in various domains. The authors develop a new formula for the gradient of the CVaR in the form of a conditional expectation and propose a novel sampling-based estimator for the gradient of the CVaR, in the spirit of the likelihood-ratio method.

They analyze the bias of th
…[truncated 501 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-26T10:26:36.754496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoMix NeurIPS 2024 full author list Aggarwal Madaan Anand"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoMix NeurIPS 2024 full author list Aggarwal Madaan Anand"
  }
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-26T10:26:36.754830+00:00_

I now have all the information needed. Here are the verification results:

---

### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)
- ID：N/A

### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2406.18665; also later accepted at ICLR 2025)
- ID：✓ (2406.18665)

### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning
- 真实性：✓
- 作者：✗ — 缺少 Edward Berman。实际作者为 Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A

### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2405.17935)
- ID：✓ (2405.17935)

### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- 真实性：✓
- 作者：✗ — "Thomas L Griffiths" 在论文中通常写作 "Tom Griffiths" 或 "Thomas L. Griffiths"（可接受的变体，非实质性错误）
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A

### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (ICLR 2024)
- ID：N/A

### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (ICML 2024)
- ID：N/A

### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)
- ID：N/A

### 29. [qwen25-2024] — Qwen2.5 Technical Report
- 真实性：✓
- 作者：✓ (论文作者众多，列出的前几位 + "others" 是合理做法)
- 年份：✓ (arXiv 提交于 2024年12月)
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2412.15115)
- ID：✓ (2412.15115)

### 30. [llama3-2024] — The Llama 3 Herd of Models
- 真实性：✓
- 作者：✓ (Aaron Grattafiori 为 v3 版本的第一作者，Abhimanyu Dube
…[truncated 486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 49
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-26T10:26:36.755174+00:00_

Web search results for query: "AutoMix NeurIPS 2024 full author list Aggarwal Madaan Anand"

Links: [{"title":"NeurIPS Poster AutoMix: Automatically Mixing Language Models","url":"https://neurips.cc/virtual/2024/poster/94293"},{"title":"[2310.12963] AutoMix: Automatically Mixing Language Models","url":"https://arxiv.org/abs/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://proceedings.neurips.cc//paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html"},{"title":"[PDF] AutoMix: Automatically Mixing Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AutoMix:-Automatically-Mixing-Language-Models-Madaan-Aggarwal/f0ed191bdcbd56610ab4d95c5a80d5ac31ffc074"},{"title":"AutoMix: Automatically Mixing Language Models Pranjal Aggarwal♢∗ Aman Madaan♣∗","url":"https://arxiv.org/pdf/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models | Request PDF","url":"https://www.researchgate.net/publication/397213626_AutoMix_Automatically_Mixing_Language_Models"},{"title":"GitHub - automix-llm/automix: Mixing Language Models with Self-Verification and Meta-Verification · GitHub","url":"https://github.com/automix-llm/automix"},{"title":"AutoMix: Automatically Mixing Language Models [Quick Review]","url":"https://liner.com/review/automix-automatically-mixing-language-models"},{"title":"NeurIPS 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2024-paper-list/"}]

Based on the search results, the full author list for the AutoMix paper at NeurIPS 2024 is: Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 236 · 2026-05-26T10:26:36.755475+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"
  }
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-26T10:26:36.755740+00:00_

Web search results for query: "arXiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/?searchtype=author&query=Benjamin+Plaut"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"dblp: BibTeX records: Ponnurangam Kumaraguru","url":"https://dblp.org/pid/97/5147.html?view=bibtex"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1575&show=1000"},{"title":"Computation and Language","url":"https://arxiv.org/list/cs.CL/recent"},{"title":"Computer Science Jun 2024","url":"https://www.arxiv.org/list/cs/2024-06?skip=8925&show=2000"}]

Based on the search results, here is the information about arXiv paper 2510.16492:

**Paper:** "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety"

**Authors:** Vamshi Krishna Bonagiri, Ponnurangam Kumaraguru, Khanh Nguyen, and Benjamin Plaut

**Affiliations:** The authors are from University of California, Berkeley, Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), and International Institute of Information Technology, Hyderabad (IIIT Hyderabad)

**Summary:** The paper proposes using "quitting" as a simple yet effective behavioral mechanism for LLM agents to recognize and withdraw from situations where they lack confidence. The researchers conducted a systematic evaluation of quitting behavior across 12 state-of-the-art LLMs, and their results demonstrate a favorable safety-helpfulness trade-off, with agents prompted to quit 
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-26T10:26:36.756045+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2207.05221 Kadavath \"Eli Tran-Geesaman\" OR \"Eli Tran-Johnson\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2207.05221 Kadavath \"Eli Tran-Geesaman\" OR \"Eli Tran-Johnson\" authors"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:26:36.756325+00:00_

Web search results for query: "arXiv 2207.05221 Kadavath "Eli Tran-Geesaman" OR "Eli Tran-Johnson" authors"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"https://arxiv.org/search/cs?searchtype=author&quer...","url":"https://arxiv.org/search/cs?searchtype=author&query=Kadavath,+S"},{"title":"ml-papers/papers/2022/220711 Language Models (Mostly) Know What They Know.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2022/220711%20Language%20Models%20(Mostly)%20Know%20What%20They%20Know.md"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"GitHub - anthropics/evals · GitHub","url":"https://github.com/anthropics/evals"}]

Based on the search results, the paper arXiv 2207.05221 titled "Language Models (Mostly) Know What They Know" was authored by Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, and others
…[truncated 403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-26T10:26:36.756719+00:00_

Now I have all the information needed. Let me also verify the AutoMix bib entry author details against the actual paper. The bib entry says: "Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket" but the real authors are: "Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam." The bib entry has several wrong names and is missing many authors.

Here are my findings:

---

### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models
- 真实性：✓
- 作者：✗ — bib 中只列了 6 人且多个名字有误。实际作者为 Pranjal Aggarwal, Aman Madaan, Ankit Anand (非 Prakhar), Srividya Pranavi Potharaju (非 Potdar), Swaroop Mishra (非 Gupta), Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam (共13人，无 Niket Tandon)
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2024)
- ID：N/A

### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✗ — 实际标题中 "allocating" 和 "language" 首字母小写："Mixture-of-Depths: Dynamically allocating compute in transformer-based language models"（但这仅是大小写差异，语义无误）
- Venue：✓ (ICML 2024)
- ID：N/A

### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (ICML 2023)
- ID：N/A

### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety
- 真实性：✓
- 作者：✓ — Bonagiri, Nguyen, Plaut, Kumaraguru 均正确
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint arXiv:2510.16492)
- ID：✓ (2510.16492)

### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (EMNLP 2023)
- ID：N/A

### 64. [kadavath2022language] — Language Models (Most
…[truncated 2159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Agent",
  "elapsed_ms": 23
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-26T10:26:36.757107+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-26T10:26:36.757400+00:00_

1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.95\textwidth]{figures/pipeline_overview.pdf}
6	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
7	\label{fig:pipeline}
8	\end{figure*}
9	
10	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
11	Existing routing methods, whether inserting API calls by perplexity reduction~\citep{toolformer-2023}, decomposing tasks into tool-augmented programs~\citep{art-2023,chameleon-2023}, or adaptively selecting reasoning depths~\citep{cogrouter-2026,ares-2026} and model tiers~\citep{mtrouter-2026,budget-aware-routing-2026}, share an implicit assumption: that routing signal stems from diverse sources and a learned router can exploit it. But before training a router, we should understand what mechanistic signal drives the routing preference. If signal collapses to a single dominant mechanism, a learned step-level router may not be the right solution.
12	
13	We propose an \emph{episode-level counterfactual diagnostic framework} to address this prior question. The framework compares pure-strategy outcomes (internal-only vs.\ deterministic-only) and introduces the Death Avoidance Factor (DAF) to decompose the routing score gap into death-avoidance and non-death components (\S\ref{sec:collection}--\ref{sec:daf}). Operating at episode granularity is essential: per-step oracle labeling degenerates under sparse terminal rewards (97.4\% tie rate in ScienceWorld; \S\ref{sec:collection}).
14	
15	Applied to ScienceWorld~\citep{scienceworld-2022}, the framework reveals that \textbf{78.9\% of non-tie routing labels arise from death asymmetry}, where the internal strategy triggers a catastrophic failure while the deterministic strategy survives. This pattern re
…[truncated 1468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-26T10:26:36.757675+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-26T10:26:36.757937+00:00_

1	\section{Related Work}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{figures/death_action_comparison.pdf}
6	\vspace{-2mm}
7	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies within death episodes. Both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
8	\label{fig:death-comparison}
9	\end{figure*}
10	
11	\paragraph{Tool-Augmented Agents and Adaptive Routing.}
12	Methods for augmenting LLMs with external tools span self-supervised invocation~\citep{toolformer-2023,toolace-2025}, task-level decomposition~\citep{art-2023,chameleon-2023}, and RL-based tool selection~\citep{retool-2025,tool-learning-survey-2024}. Concurrent work examines \emph{when} to invoke tools: \citet{when2tool-2026} analyze accuracy--latency tradeoffs, \citet{tool-use-tax-2026} quantify invocation overhead, and \citet{to-call-or-not-2026,tool-overuse-illusion-2026} investigate overuse patterns. On the routing side, adaptive methods range from learned halting~\citep{graves2016act} and token-level recursion~\citep{mixture-of-recursions-2025} to per-step depth adjustment~\citep{cogrouter-2026,ares-2026} and multi-turn model selection~\citep{mtrouter-2026}. Model-selection routing~\citep{routellm-2024,frugalgpt-2023,automix-2024} optimizes \emph{which} model to invoke based on query difficulty; \citet{budget-aware-routing-2026} train episode-level routing under sparse rewards via counterfactual rollouts, the closest setting to ours, though they focus on learning the router rather than diagnosing what signal it captures. All these approaches presuppose that diverse routing signals exist; our decomposition reveals that in ScienceWorld, a single mechanism accounts for 78.9\% of routing labels.
13	
14	\paragraph{Counterfactua
…[truncated 2295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-26T10:26:36.758225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-26T10:26:36.758543+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework (Figure~\ref{fig:pipeline}) quantifies what drives routing signal in interactive environments through two components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). A supplementary Signal Concentration Index (SCI; Appendix~\ref{app:sci}) measures whether signal is concentrated in a few task types. Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), which uses the same LLM to generate candidate actions but evaluates them through privileged environment feedback (ground-truth simulator state in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld; see \S\ref{sec:cross-env} for environment-specific operationalizations). Crucially, the deterministic strategy does not provide optimal actions; it reduces observation uncertainty by grounding the LLM's choices in verified environment state rather than predicted state. These qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our
…[truncated 6428 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-26T10:26:36.758799+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-26T10:26:36.759182+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
7	\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
8	\label{fig:decomposition}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\scriptsize
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{@{}lrr@{}}
16	\toprule
17	Condition & Death\% & $N$ \\
18	\midrule
19	Single-trial baseline & 42.9 & 245 \\
20	Reflexion ($3{\times}$) & 31.4 & 220 \\
21	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
22	Deterministic baseline & 16.3 & 245 \\
23	\midrule
24	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
25	Death-prone baseline & 48.0 & 200 \\
26	Retry ($5{\times}$) & 43.5 & 200 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}
30	\label{tab:agent-improvement}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=0.95\columnwidth]{figures/death_action_timeline.pdf}
36	\vspace{-2mm}
37	\caption{Action sequences for 6 representative death episodes. The fatal \texttt{focus on} (arrow) appears in final steps after long \texttt{connect} sequences (``connect loop $\to$ fatal focus'').}
38	\label{fig:death-timeline}
39	\end{figure}
40	
41	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performa
…[truncated 12492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-26T10:26:36.759547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 250 · 2026-05-26T10:26:36.759974+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\%$); leave-one-task-out degrades to $50.0\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\%$), and cross-model death-rate stability ($31$--$49\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\ref{app:grounding-ablation}) than learned routing policies.
6	
7	\paragraph{Failure mechanism.}
8	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\ref{fig:death-action-dist}, Appendix~\ref{app:failure-modes}) shows that \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while Figure~\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\sim}5\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} is the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs 
…[truncated 2608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-26T10:26:36.760403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-26T10:26:36.760648+00:00_

1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.
4	
5	The framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.
6	
7	Key open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 253 · 2026-05-26T10:26:36.760982+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2207.05221 \"Language Models Mostly Know What They Know\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2207.05221 \"Language Models Mostly Know What They Know\" authors"
  }
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-26T10:26:36.761280+00:00_

Web search results for query: "arxiv 2207.05221 "Language Models Mostly Know What They Know" authors"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know","url":"https://arxiv.org/pdf/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"}]

Based on the search results, here are the authors of the arxiv paper 2207.05221 titled "Language Models (Mostly) Know What They Know":

The authors are Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna K
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 255 · 2026-05-26T10:26:36.761574+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit",
  "description": "Create ref-audit directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit",
    "description": "Create ref-audit directory"
  }
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-26T10:26:36.761789+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-26T10:26:36.762093+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md",
  "content": "# Reference Audit — Worker C\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：59\n- ✗ 发现问题：9（5 项硬错误，2 项中等问题，2 项 venue 升级建议）\n\n### 硬错误（必须修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 33 | toolace-2025 | 第一作者姓名错误：\"Zhang, Weiwen\" → **\"Liu, Weiwen\"** |\n| 59 | automix-2024 | 作者列表严重错误：多个名字拼错，缺少 7 位作者，包含不存在的作者 |\n| 51 | agent-safetybench-2024 | 作者列表错误：\"Junhao Yang\" → \"Junxiao Yang\"，包含 3 名非作者，缺少 \"Hongning Wang\" |\n| 46 | salt-2026 | 第三作者错误：\"David Yan\" → **\"Qiaojing Yan\"** |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n\n### 中等问题（建议修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 64 | kadavath2022language | 作者 \"Eli Tran-Geesaman\" → **\"Eli Tran-Johnson\"** |\n| 20 | gajcin2023counterfactual | 实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文；标题省略了 \": Doctoral Consortium\" 后缀 |\n\n### Venue 升级建议（arXiv → 已被会议接收）\n\n| # | cite_key | 当前 venue | 实际已接收 |\n|---|----------|-----------|-----------|\n| 22 | routellm-2024 | arXiv 2406.18665 | **ICLR 2025** |\n| 43 | pona2025abstract | arXiv 2506.02946 | **NeurIPS 2025** |\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (大小写差异属 BibTeX 正常行为)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16(1), pp 1437-1480)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✗ 实际标题为 \"Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium\"，bib 省略了后缀\n- Venue：✗ 实为 AAMAS 2023 Doctoral Consortium 论文，非正式会议论文\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2406.18665，但已被 **ICLR 2025** 接收，建议更新\n- ID：✓ (2406.18665)\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ 缺少作者 **Edward Berman**。完整作者应为 Shinn, Cassano, **Berman**, Gopinath, Narasimhan, Yao\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (The Review of Economics and Statistics, vol 90(3), pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ 第一作者姓名错误。bib 写 **\"Zhang, Weiwen\"**，实际第一作者为 **\"Liu, Weiwen\"** (Weiwen Liu)。完整作者列表包含 Weiwen Liu, Xu Huang, Xingshan Zeng 等 27 人\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56(3), pp 839-858)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓ (bib 用 \"LLMs\" 缩写，原文用 \"Large Language Models\"，可接受)\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49(2-3), pp 267-290)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2506.02946，但已被 **NeurIPS 2025** 接收，建议更新\n- ID：✓ (2506.02946)\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ 第三作者错误。bib 写 **\"Yan, David\"**，ACL Anthology 实际为 **\"Qiaojing Yan\"**\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓ (Gemma Team)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70, pp 1373-1411)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 9 人，实际为 7 人。具体问题：(1) \"Junhao Yang\" 应为 **\"Junxiao Yang\"**；(2) \"Jie Liu\"、\"Renhao Wang\"、\"Jiangjie Li\" 三人并非该论文作者；(3) 缺少作者 **\"Hongning Wang\"**。正确作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd ed.)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66(5), pp 688-701)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (JMLR, vol 23(120), pp 1-39)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 6 人中 3 个名字有误且遗漏 7 位作者：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 并非该论文作者；(5) 缺少 Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam 等作者。正确完整列表：Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✗ 第 10 位作者姓名错误。bib 写 **\"Eli Tran-Geesaman\"**，实际为 **\"Eli Tran-Johnson\"**（已通过 arXiv 2207.05221 原始页面确认）\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n---\n\n## 正文引用上下文检查\n\n逐篇 tex 文件检查 `\\cite{}` 用法是否存在\"引用 paper A 但描述 paper B 结论\"的情况：\n\n- **introduction.tex**：所有引用与描述匹配。✓\n- **related_work.tex**：所有引用与描述匹配。✓\n- **method.tex**：所有引用与描述匹配。✓\n- **experiments.tex**：所有引用与描述匹配。✓\n- **discussion.tex**：无引用。✓\n- **conclusion.tex**：无引用。✓\n\n未发现引用上下文错配。\n\n## 附加发现\n\n1. bib 中有 12 条 entry 未在正文 tex 中被 `\\cite` 引用：dagger-2011, toolkengpt-2023, altman1999constrained, mihatsch2002risk, northcutt2021confident, li2020dividemix, moldovan2012safe, leviathan2023speculative, bonagiri2025check, manakul2023selfcheckgpt, kadavath2022language, zhou2020bert, chow2015risk, tamar2015optimizing。这些可能在 appendix 中使用，或为冗余条目。\n2. cite key `axis-2026` 对应的 bib entry year 为 2025（arXiv:2505.17801），key 与年份不一致（不影响编译，但不规范）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md",
    "content": "# Reference Audit — Worker C\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：59\n- ✗ 发现问题：9（5 项硬错误，2 项中等问题，2 项 venue 升级建议）\n\n### 硬错误（必须修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 33 | toolace-2025 | 第一作者姓名错误：\"Zhang, Weiwen\" → **\"Liu, Weiwen\"** |\n| 59 | automix-2024 | 作者列表严重错误：多个名字拼错，缺少 7 位作者，包含不存在的作者 |\n| 51 | agent-safetybench-2024 | 作者列表错误：\"Junhao Yang\" → \"Junxiao Yang\"，包含 3 名非作者，缺少 \"Hongning Wang\" |\n| 46 | salt-2026 | 第三作者错误：\"David Yan\" → **\"Qiaojing Yan\"** |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n\n### 中等问题（建议修正）\n\n| # | cite_key | 问题 |\n|---|----------|------|\n| 64 | kadavath2022language | 作者 \"Eli Tran-Geesaman\" → **\"Eli Tran-Johnson\"** |\n| 20 | gajcin2023counterfactual | 实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文；标题省略了 \": Doctoral Consortium\" 后缀 |\n\n### Venue 升级建议（arXiv → 已被会议接收）\n\n| # | cite_key | 当前 venue | 实际已接收 |\n|---|----------|-----------|-----------|\n| 22 | routellm-2024 | arXiv 2406.18665 | **ICLR 2025** |\n| 43 | pona2025abstract | arXiv 2506.02946 | **NeurIPS 2025** |\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (大小写差异属 BibTeX 正常行为)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16(1), pp 1437-1480)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✗ 实际标题为 \"Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium\"，bib 省略了后缀\n- Venue：✗ 实为 AAMAS 2023 Doctoral Consortium 论文，非正式会议论文\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2406.18665，但已被 **ICLR 2025** 接收，建议更新\n- ID：✓ (2406.18665)\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ 缺少作者 **Edward Berman**。完整作者应为 Shinn, Cassano, **Berman**, Gopinath, Narasimhan, Yao\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (The Review of Economics and Statistics, vol 90(3), pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ 第一作者姓名错误。bib 写 **\"Zhang, Weiwen\"**，实际第一作者为 **\"Liu, Weiwen\"** (Weiwen Liu)。完整作者列表包含 Weiwen Liu, Xu Huang, Xingshan Zeng 等 27 人\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56(3), pp 839-858)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓ (bib 用 \"LLMs\" 缩写，原文用 \"Large Language Models\"，可接受)\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49(2-3), pp 267-290)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✗ bib 标注为 arXiv 2506.02946，但已被 **NeurIPS 2025** 接收，建议更新\n- ID：✓ (2506.02946)\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ 第三作者错误。bib 写 **\"Yan, David\"**，ACL Anthology 实际为 **\"Qiaojing Yan\"**\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓ (Gemma Team)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70, pp 1373-1411)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 9 人，实际为 7 人。具体问题：(1) \"Junhao Yang\" 应为 **\"Junxiao Yang\"**；(2) \"Jie Liu\"、\"Renhao Wang\"、\"Jiangjie Li\" 三人并非该论文作者；(3) 缺少作者 **\"Hongning Wang\"**。正确作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd ed.)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66(5), pp 688-701)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (JMLR, vol 23(120), pp 1-39)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ 作者列表严重错误。bib 列出 6 人中 3 个名字有误且遗漏 7 位作者：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 并非该论文作者；(5) 缺少 Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam 等作者。正确完整列表：Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✗ 第 10 位作者姓名错误。bib 写 **\"Eli Tran-Geesaman\"**，实际为 **\"Eli Tran-Johnson\"**（已通过 arXiv 2207.05221 原始页面确认）\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓ (未在正文中引用，仅在 bib 中存在)\n\n---\n\n## 正文引用上下文检查\n\n逐篇 tex 文件检查 `\\cite{}` 用法是否存在\"引用 paper A 但描述 paper B 结论\"的情况：\n\n- **introduction.tex**：所有引用与描述匹配。✓\n- **related_work.tex**：所有引用与描述匹配。✓\n- **method.tex**：所有引用与描述匹配。✓\n- **experiments.tex**：所有引用与描述匹配。✓\n- **discussion.tex**：无引用。✓\n- **conclusion.tex**：无引用。✓\n\n未发现引用上下文错配。\n\n## 附加发现\n\n1. bib 中有 12 条 entry 未在正文 tex 中被 `\\cite` 引用：dagger-2011, toolkengpt-2023, altman1999constrained, mihatsch2002risk, northcutt2021confident, li2020dividemix, moldovan2012safe, leviathan2023speculative, bonagiri2025check, manakul2023selfcheckgpt, kadavath2022language, zhou2020bert, chow2015risk, tamar2015optimizing。这些可能在 appendix 中使用，或为冗余条目。\n2. cite key `axis-2026` 对应的 bib entry year 为 2025（arXiv:2505.17801），key 与年份不一致（不影响编译，但不规范）。\n"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-26T10:26:36.762660+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_C.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-C_20260526T101534",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 259 · 2026-05-26T10:26:36.762936+00:00_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_C.md`。

68 条 bib entry 中发现 9 条有问题：

**硬错误（5）：**
- `toolace-2025`：第一作者 "Zhang, Weiwen" → **Liu, Weiwen**
- `automix-2024`：作者列表严重错误（3 个名字拼错 + 缺少 7 位作者 + 含 1 位非作者）
- `agent-safetybench-2024`：作者列表错误（"Junhao Yang" → "Junxiao Yang"，含 3 名非作者，缺 "Hongning Wang"）
- `salt-2026`：第三作者 "David Yan" → **Qiaojing Yan**
- `reflexion-2023`：缺少作者 Edward Berman

**中等问题（2）：**
- `kadavath2022language`：作者 "Eli Tran-Geesaman" → **Eli Tran-Johnson**
- `gajcin2023counterfactual`：实为 AAMAS 2023 Doctoral Consortium 论文，非正式论文

**Venue 升级建议（2）：**
- `routellm-2024`：arXiv → 已被 ICLR 2025 接收
- `pona2025abstract`：arXiv → 已被 NeurIPS 2025 接收

无 hallucinated paper，无引用上下文错配。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-C_20260526T101534"
}
```

</details>

---
