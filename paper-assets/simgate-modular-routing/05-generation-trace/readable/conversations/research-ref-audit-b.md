# research ref audit B

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 279
- **Recorded user turns:** 0
- **Tool calls:** 139
- **Original source:** `logs/chats/worker_research_ref-audit-B_20260526T101527.jsonl`
- **Structured JSON:** [`0a43098bd26918bbbd3e.json`](../../sessions/0a/0a43098bd26918bbbd3e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

279 recorded events

### Tool call

_source line 1 · 2026-05-26T10:26:42.865737+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:26:42.866295+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:26:42.866518+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 4 · 2026-05-26T10:26:42.866715+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:26:42.866936+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 6 · 2026-05-26T10:26:42.867111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:26:42.867308+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 1",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n1. scienceworld-2022\nTitle: ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\nAuthors: Wang, Ruoyao and Jansen, Peter and Côté, Marc-Alexandre and Ammanabrolu, Prithviraj\nVenue: EMNLP 2022\nYear: 2022\n\n2. react-2023\nTitle: ReAct: Synergizing Reasoning and Acting in Language Models\nAuthors: Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan\nVenue: ICLR 2023\nYear: 2023\n\n3. toolformer-2023\nTitle: Toolformer: Language Models Can Teach Themselves to Use Tools\nAuthors: Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas\nVenue: NeurIPS 2023\nYear: 2023\n\n4. art-2023\nTitle: ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\nAuthors: Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio\nJournal: arXiv:2303.09014\nYear: 2023\n\n5. chameleon-2023\nTitle: Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\nAuthors: Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng\nVenue: NeurIPS 2023\nYear: 2023\n\n6. retool-2025\nTitle: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\nAuthors: Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others\nJournal: arXiv:2504.11536\nYear: 2025\n\n7. cogrouter-2026\nTitle: Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\nAuthors: Yang, Ruihan and Ye, Fanghua and Wei, Xiang and Zhao, Ruoqing and Luo, Kang and others\nJournal: arXiv:2602.12662\nYear: 2026\n\n8. ares-2026\nTitle: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\nAuthors: Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu and others\nJournal: arXiv:2603.07915\nYear: 2026\n\n9. mixture-of-recursions-2025\nTitle: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\nAuthors: Bae, Sangmin and Kim, Yujin and Bayat, Reza and Kim, Sungnyun and Ha, Jiyoun and others\nVenue: NeurIPS 2025\nYear: 2025\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 1",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n1. scienceworld-2022\nTitle: ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\nAuthors: Wang, Ruoyao and Jansen, Peter and Côté, Marc-Alexandre and Ammanabrolu, Prithviraj\nVenue: EMNLP 2022\nYear: 2022\n\n2. react-2023\nTitle: ReAct: Synergizing Reasoning and Acting in Language Models\nAuthors: Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan\nVenue: ICLR 2023\nYear: 2023\n\n3. toolformer-2023\nTitle: Toolformer: Language Models Can Teach Themselves to Use Tools\nAuthors: Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas\nVenue: NeurIPS 2023\nYear: 2023\n\n4. art-2023\nTitle: ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\nAuthors: Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio\nJournal: arXiv:2303.09014\nYear: 2023\n\n5. chameleon-2023\nTitle: Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\nAuthors: Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng\nVenue: NeurIPS 2023\nYear: 2023\n\n6. retool-2025\nTitle: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\nAuthors: Feng, Jiazhan and Huang, Shijue and Qu, Xingwei and Zhang, Ge and Qin, Yujia and others\nJournal: arXiv:2504.11536\nYear: 2025\n\n7. cogrouter-2026\nTitle: Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\nAuthors: Yang, Ruihan and Ye, Fanghua and Wei, Xiang and Zhao, Ruoqing and Luo, Kang and others\nJournal: arXiv:2602.12662\nYear: 2026\n\n8. ares-2026\nTitle: Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\nAuthors: Yang, Jingbo and Hou, Bairu and Wei, Wei and Bao, Yujia and Chang, Shiyu and others\nJournal: arXiv:2603.07915\nYear: 2026\n\n9. mixture-of-recursions-2025\nTitle: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\nAuthors: Bae, Sangmin and Kim, Yujin and Bayat, Reza and Kim, Sungnyun and Ha, Jiyoun and others\nVenue: NeurIPS 2025\nYear: 2025\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:26:42.867558+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 9 · 2026-05-26T10:26:42.867708+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:26:42.867846+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? EMNLP 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? EMNLP 2022"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:26:42.868024+00:00_

Web search results for query: "ScienceWorld: Is Your Agent Smarter Than a 5th Grader? EMNLP 2022"

Links: [{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.775/"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"[Quick Review] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://liner.com/review/scienceworld-is-your-agent-smarter-than-5th-grader"},{"title":"[PDF] ScienceWorld: Is your Agent Smarter than a 5th Grader? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ScienceWorld:-Is-your-Agent-Smarter-than-a-5th-Wang-Jansen/0e41fd22d483047bd8fdb1757d90c7702493567e"},{"title":"GitHub - allenai/ScienceWorld: ScienceWorld is a text-based virtual environment centered around accomplishing tasks from the standardized elementary science curriculum. · GitHub","url":"https://github.com/allenai/ScienceWorld"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/scienceworld-is-your-agent-smarter-than-a-5th-grader/"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? | Request PDF","url":"https://www.researchgate.net/publication/372924838_ScienceWorld_Is_your_Agent_Smarter_than_a_5th_Grader"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? (arXiv:2203.07540v2) - ScienceStack","url":"https://www.sciencestack.ai/paper/2203.07540v2"}]

Based on the search results, here's what I found about this paper:

## Overview

ScienceWorld is a benchmark to test agents' scientific reasoning abilities in a new interactive text environment at the level of a standard elementary school science curriculum. The paper was authored by Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu, and published in the Proceedings of the 2022 Conference on Empirical Methods
…[truncated 1126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:26:42.868216+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReAct: Synergizing Reasoning and Acting in Language Models ICLR 2023 Yao Shunyu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReAct: Synergizing Reasoning and Acting in Language Models ICLR 2023 Yao Shunyu"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:26:42.868380+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 2",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n10. mtrouter-2026\nTitle: MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\nAuthors: Zhang, Yiqun and Li, Hao and Wang, Zihan and Feng, Shi and Yang, Xiaocui and others\nVenue: ACL 2026\nYear: 2026\n\n11. tool-overuse-illusion-2026\nTitle: The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\nAuthors: Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting\nJournal: arXiv:2604.19749\nYear: 2026\n\n12. when2tool-2026\nTitle: LLM Agents Already Know When to Call Tools -- Even Without Reasoning\nAuthors: Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\nJournal: arXiv:2605.09252\nYear: 2026\n\n13. tool-use-tax-2026\nTitle: Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\nAuthors: Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying\nJournal: arXiv:2605.00136\nYear: 2026\n\n14. to-call-or-not-2026\nTitle: To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\nAuthors: Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal\nJournal: arXiv:2605.00737\nYear: 2026\n\n15. dagger-2011\nTitle: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\nAuthors: Ross, Stéphane and Gordon, Geoffrey J and Bagnell, Drew\nVenue: AISTATS 2011\nYear: 2011\n\n16. toolkengpt-2023\nTitle: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\nAuthors: Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\nVenue: NeurIPS 2023\nYear: 2023\n\n17. alfworld-2021\nTitle: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\nAuthors: Shridhar, Mohit and Yuan, Xingdi and Côté, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew\nVenue: ICLR 2021\nYear: 2021\n\n18. garcia2015comprehensive\nTitle: A Comprehensive Survey on Safe Reinforcement Learning\nAuthors: García, Javier and Fernández, Fernando\nJournal: JMLR, vol 16, no 1, pp 1437-1480\nYear: 2015\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 2",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n10. mtrouter-2026\nTitle: MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\nAuthors: Zhang, Yiqun and Li, Hao and Wang, Zihan and Feng, Shi and Yang, Xiaocui and others\nVenue: ACL 2026\nYear: 2026\n\n11. tool-overuse-illusion-2026\nTitle: The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\nAuthors: Zeng, Yirong and You, Shen and Liu, Yufei and Du, Qunyao and Ding, Xiao and Hou, Yutai and Wang, Yuxian and Ning, Wu and Song, Haonan and Tu, Dandan and Cai, Bibo and Liu, Ting\nJournal: arXiv:2604.19749\nYear: 2026\n\n12. when2tool-2026\nTitle: LLM Agents Already Know When to Call Tools -- Even Without Reasoning\nAuthors: Sun, Chung-En and Liu, Linbo and Yan, Ge and Wang, Zimo and Weng, Tsui-Wei\nJournal: arXiv:2605.09252\nYear: 2026\n\n13. tool-use-tax-2026\nTitle: Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\nAuthors: Zhang, Kaituo and Xiong, Zhen and Zhong, Mingyu and Jiang, Zhimeng and Yuan, Zhouyuan and Li, Zhecheng and Lin, Ying\nJournal: arXiv:2605.00136\nYear: 2026\n\n14. to-call-or-not-2026\nTitle: To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\nAuthors: Wu, Qinyuan and Das, Soumi and Amani, Mahsa and Nag, Arijit and Lee, Seungeon and Gummadi, Krishna P. and Ravichander, Abhilasha and Zafar, Muhammad Bilal\nJournal: arXiv:2605.00737\nYear: 2026\n\n15. dagger-2011\nTitle: A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\nAuthors: Ross, Stéphane and Gordon, Geoffrey J and Bagnell, Drew\nVenue: AISTATS 2011\nYear: 2011\n\n16. toolkengpt-2023\nTitle: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\nAuthors: Hao, Shibo and Liu, Tianyang and Wang, Zhen and Hu, Zhiting\nVenue: NeurIPS 2023\nYear: 2023\n\n17. alfworld-2021\nTitle: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\nAuthors: Shridhar, Mohit and Yuan, Xingdi and Côté, Marc-Alexandre and Bisk, Yonatan and Trischler, Adam and Hausknecht, Matthew\nVenue: ICLR 2021\nYear: 2021\n\n18. garcia2015comprehensive\nTitle: A Comprehensive Survey on Safe Reinforcement Learning\nAuthors: García, Javier and Fernández, Fernando\nJournal: JMLR, vol 16, no 1, pp 1437-1480\nYear: 2015\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:26:42.868636+00:00_

Web search results for query: "ReAct: Synergizing Reasoning and Acting in Language Models ICLR 2023 Yao Shunyu"

Links: [{"title":"[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://arxiv.org/abs/2210.03629"},{"title":"GitHub - ysymyth/ReAct: [ICLR 2023] ReAct: Synergizing Reasoning and Acting in Language Models · GitHub","url":"https://github.com/ysymyth/ReAct"},{"title":"REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS - Princeton University","url":"https://collaborate.princeton.edu/en/publications/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10451467-react-synergizing-reasoning-acting-language-models"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://react-lm.github.io/"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/"},{"title":"ICLR 2023 ReAct: Synergizing Reasoning and Acting in Language Models Oral","url":"https://iclr.cc/virtual/2023/oral/12647"},{"title":"The ReAct Framework: Synergizing Reasoning and Acting","url":"https://apxml.com/courses/agentic-llm-memory-architectures/chapter-2-advanced-agent-architectures-reasoning/react-framework-reasoning-acting"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models - Summary","url":"https://portkey.ai/blog/react-synergizing-reasoning-and-acting-in-language-models-summary/"}]

I found comprehensive information about the ReAct paper. Here are the key details:

## Overview

ReAct: Synergizing Reasoning and Acting in Language Models is an ICLR 2023 paper by Yao, Shunyu and co-authors Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; and Cao, Yuan.

## Main Contribution

The paper explores the use of LLMs to generate both reasoning trace
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:26:42.868813+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Toolformer: Language Models Can Teach Themselves to Use Tools NeurIPS 2023 Schick"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Toolformer: Language Models Can Teach Themselves to Use Tools NeurIPS 2023 Schick"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:26:42.868953+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 17 · 2026-05-26T10:26:42.869111+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:26:42.869242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MTRouter Cost-Aware Multi-Turn LLM Routing History-Model Joint Embeddings ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MTRouter Cost-Aware Multi-Turn LLM Routing History-Model Joint Embeddings ACL 2026"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:26:42.869392+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 3",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n19. amitai2024explaining\nTitle: Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\nAuthors: Amitai, Yotam and Septon, Guy and Amir, Ofra\nVenue: AAAI 2024\nYear: 2024\n\n20. gajcin2023counterfactual\nTitle: Counterfactual Explanations for Reinforcement Learning Agents\nAuthors: Gajcin, Jasmina\nVenue: AAMAS 2023\nYear: 2023\n\n21. olson2021counterfactual\nTitle: Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\nAuthors: Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen\nJournal: Artificial Intelligence, vol 295, pp 103455\nYear: 2021\n\n22. routellm-2024\nTitle: RouteLLM: Learning to Route LLMs with Preference Data\nAuthors: Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tianhao and Gonzalez, Joseph E. and Kadous, M Waleed and Stoica, Ion\nJournal: arXiv:2406.18665\nYear: 2024\n\n23. reflexion-2023\nTitle: Reflexion: Language Agents with Verbal Reinforcement Learning\nAuthors: Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu\nVenue: NeurIPS 2023\nYear: 2023\n\n24. tool-learning-survey-2024\nTitle: Tool Learning with Large Language Models: A Survey\nAuthors: Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqiang and Yin, Dawei and Xu, Jun and Wen, Ji-Rong\nJournal: arXiv:2405.17935\nYear: 2024\n\n25. tot-2023\nTitle: Tree of Thoughts: Deliberate Problem Solving with Large Language Models\nAuthors: Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L and Cao, Yuan and Narasimhan, Karthik\nVenue: NeurIPS 2023\nYear: 2023\n\n26. agentbench-2024\nTitle: AgentBench: Evaluating LLMs as Agents\nAuthors: Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and Huang, Minlie and Zhang, Yuxiao and Tang, Jie\nVenue: ICLR 2024\nYear: 2024\n\n27. lats-2024\nTitle: Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\nAuthors: Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong\nVenue: ICML 2024\nYear: 2024\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 3",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n19. amitai2024explaining\nTitle: Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\nAuthors: Amitai, Yotam and Septon, Guy and Amir, Ofra\nVenue: AAAI 2024\nYear: 2024\n\n20. gajcin2023counterfactual\nTitle: Counterfactual Explanations for Reinforcement Learning Agents\nAuthors: Gajcin, Jasmina\nVenue: AAMAS 2023\nYear: 2023\n\n21. olson2021counterfactual\nTitle: Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\nAuthors: Olson, Matthew L. and Khanna, Roli and Neal, Lawrence and Li, Fuxin and Wong, Weng-Keen\nJournal: Artificial Intelligence, vol 295, pp 103455\nYear: 2021\n\n22. routellm-2024\nTitle: RouteLLM: Learning to Route LLMs with Preference Data\nAuthors: Ong, Isaac and Almahairi, Amjad and Wu, Vincent and Chiang, Wei-Lin and Wu, Tianhao and Gonzalez, Joseph E. and Kadous, M Waleed and Stoica, Ion\nJournal: arXiv:2406.18665\nYear: 2024\n\n23. reflexion-2023\nTitle: Reflexion: Language Agents with Verbal Reinforcement Learning\nAuthors: Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu\nVenue: NeurIPS 2023\nYear: 2023\n\n24. tool-learning-survey-2024\nTitle: Tool Learning with Large Language Models: A Survey\nAuthors: Qu, Changle and Dai, Sunhao and Wei, Xiaochi and Cai, Hengyi and Wang, Shuaiqiang and Yin, Dawei and Xu, Jun and Wen, Ji-Rong\nJournal: arXiv:2405.17935\nYear: 2024\n\n25. tot-2023\nTitle: Tree of Thoughts: Deliberate Problem Solving with Large Language Models\nAuthors: Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L and Cao, Yuan and Narasimhan, Karthik\nVenue: NeurIPS 2023\nYear: 2023\n\n26. agentbench-2024\nTitle: AgentBench: Evaluating LLMs as Agents\nAuthors: Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and Huang, Minlie and Zhang, Yuxiao and Tang, Jie\nVenue: ICLR 2024\nYear: 2024\n\n27. lats-2024\nTitle: Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\nAuthors: Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong\nVenue: ICML 2024\nYear: 2024\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:26:42.869751+00:00_

Web search results for query: "Toolformer: Language Models Can Teach Themselves to Use Tools NeurIPS 2023 Schick"

Links: [{"title":"[2302.04761] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://arxiv.org/abs/2302.04761"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | OpenReview","url":"https://openreview.net/forum?id=Yacmpz84TH"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html"},{"title":"NeurIPS Poster Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://neurips.cc/virtual/2023/poster/71288"},{"title":"[PDF] Toolformer: Language Models Can Teach Themselves to Use Tools | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toolformer:-Language-Models-Can-Teach-Themselves-to-Schick-Dwivedi-Yu/53d128ea815bcc0526856eb5a9c42cc977cb36a7"},{"title":"[Quick Review] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://liner.com/review/toolformer-language-models-can-teach-themselves-to-use-tools"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://arxiv.org/pdf/2302.04761"},{"title":"Timo_schick Toolformer Language Models Can Teach Themselves to Use Tools 2023 | Sukai Huang","url":"https://sino-huang.github.io/posts/timo_schick-toolformer-language-models-can-teach-themselves-to-use-tools-2023/"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://openreview.net/pdf?id=Yacmpz84TH"}]

Based on the search results, I found comprehensive information about the Toolformer paper:

## Toolformer: Language Models Can Teach Themselves to Use Tools

Toolformer is a paper by Timo Schick and colleagues that was presented at NeurIPS 2023.

**Core Concept:**
The paper shows that language models can teach themselves to use external to
…[truncated 1118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:26:42.869944+00:00_

Web search results for query: "MTRouter Cost-Aware Multi-Turn LLM Routing History-Model Joint Embeddings ACL 2026"

Links: [{"title":"GitHub - ZhangYiqun018/MTRouter: [ACL 2026] Official implementation of MTRouter, a cost-aware multi-turn LLM routing framework accepted to ACL 2026 Main Conference. · GitHub","url":"https://github.com/ZhangYiqun018/MTRouter"},{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530v1"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"Intelligent LLM Routing: How Multi-Model AI Cuts Costs by 85% — Swfte AI","url":"https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai"},{"title":"Best LLM Router and AI Gateway (2026)","url":"https://inworld.ai/resources/best-llm-router-ai-gateway"},{"title":"Beyond the Monolith: How Multi-Model Routing Is Redefining LLM Orchestration in 2026 | Mindra Blog","url":"https://mindra.co/blog/multi-model-routing-llm-orchestration-2026"},{"title":"RouterWise: Joint Resource Allocation and Routing for Latency-Aware Multi-Model LLM Serving","url":"https://arxiv.org/html/2604.10907v1"}]

I found relevant information about MTRouter. Here's what the search results show:

## MTRouter Overview

MTRouter is a cost-aware multi-turn LLM routing framework accepted to the ACL 2026 Main Conference.

## Key Methodology

MTRouter encodes the interaction history and candidate models into joint history-model embeddings, and learns an outcome estimator from logged trajectories to predict turn-level model utility. The framework is designed to address the challenge that multi-turn, long-horizon tasks are increasingly common for large language models (LLMs), but solving them typically requires ma
…[truncated 804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:26:42.870193+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 4",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n28. math-2021\nTitle: Measuring Mathematical Problem Solving With the MATH Dataset\nAuthors: Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob\nVenue: NeurIPS 2021 Datasets and Benchmarks Track\nYear: 2021\n\n29. qwen25-2024\nTitle: Qwen2.5 Technical Report\nAuthors: Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and others\nJournal: arXiv:2412.15115\nYear: 2024\n\n30. llama3-2024\nTitle: The Llama 3 Herd of Models\nAuthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others\nJournal: arXiv:2407.21783\nYear: 2024\n\n31. cameron-2008\nTitle: Bootstrap-Based Improvements for Inference with Clustered Errors\nAuthors: Cameron, A. Colin and Gelbach, Jonah B. and Miller, Douglas L.\nJournal: The Review of Economics and Statistics, vol 90, no 3, pp 414-427\nYear: 2008\n\n32. achiam2017cpo\nTitle: Constrained Policy Optimization\nAuthors: Achiam, Joshua and Held, David and Tamar, Aviv and Abbeel, Pieter\nVenue: ICML 2017, pp 22-31\nYear: 2017\n\n33. toolace-2025\nTitle: ToolACE: Winning the Points of LLM Function Calling\nAuthors: Zhang, Weiwen and others\nVenue: ICLR 2025\nYear: 2025\n\n34. webb-2023\nTitle: Reworking Wild Bootstrap-Based Inference for Clustered Errors\nAuthors: Webb, Matthew D.\nJournal: Canadian Journal of Economics, vol 56, no 3, pp 839-858\nYear: 2023\n\n35. moldovan2012safe\nTitle: Safe Exploration in Markov Decision Processes\nAuthors: Moldovan, Teodor Mihai and Abbeel, Pieter\nVenue: ICML 2012\nYear: 2012\n\n36. graves2016act\nTitle: Adaptive Computation Time for Recurrent Neural Networks\nAuthors: Graves, Alex\nJournal: arXiv:1603.08983\nYear: 2016\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 4",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n28. math-2021\nTitle: Measuring Mathematical Problem Solving With the MATH Dataset\nAuthors: Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob\nVenue: NeurIPS 2021 Datasets and Benchmarks Track\nYear: 2021\n\n29. qwen25-2024\nTitle: Qwen2.5 Technical Report\nAuthors: Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and others\nJournal: arXiv:2412.15115\nYear: 2024\n\n30. llama3-2024\nTitle: The Llama 3 Herd of Models\nAuthors: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others\nJournal: arXiv:2407.21783\nYear: 2024\n\n31. cameron-2008\nTitle: Bootstrap-Based Improvements for Inference with Clustered Errors\nAuthors: Cameron, A. Colin and Gelbach, Jonah B. and Miller, Douglas L.\nJournal: The Review of Economics and Statistics, vol 90, no 3, pp 414-427\nYear: 2008\n\n32. achiam2017cpo\nTitle: Constrained Policy Optimization\nAuthors: Achiam, Joshua and Held, David and Tamar, Aviv and Abbeel, Pieter\nVenue: ICML 2017, pp 22-31\nYear: 2017\n\n33. toolace-2025\nTitle: ToolACE: Winning the Points of LLM Function Calling\nAuthors: Zhang, Weiwen and others\nVenue: ICLR 2025\nYear: 2025\n\n34. webb-2023\nTitle: Reworking Wild Bootstrap-Based Inference for Clustered Errors\nAuthors: Webb, Matthew D.\nJournal: Canadian Journal of Economics, vol 56, no 3, pp 839-858\nYear: 2023\n\n35. moldovan2012safe\nTitle: Safe Exploration in Markov Decision Processes\nAuthors: Moldovan, Teodor Mihai and Abbeel, Pieter\nVenue: ICML 2012\nYear: 2012\n\n36. graves2016act\nTitle: Adaptive Computation Time for Recurrent Neural Networks\nAuthors: Graves, Alex\nJournal: arXiv:1603.08983\nYear: 2016\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:26:42.870527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models arXiv 2303.09014 Paranjape"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models arXiv 2303.09014 Paranjape"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:26:42.870693+00:00_

Web search results for query: "ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models arXiv 2303.09014 Paranjape"

Links: [{"title":"[2303.09014] ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/abs/2303.09014"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://blog.athina.ai/art-automatic-multi-step-reasoning-and-tool-use-for-large-language-models"},{"title":"[PDF] ART: Automatic multi-step reasoning and tool-use for large language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ART:-Automatic-multi-step-reasoning-and-tool-use-Paranjape-Lundberg/0d42221038c05cee8443c5b5af838505ee137dc3"},{"title":"ART: Automatic multi-step reasoning and tool-use for large ...","url":"https://www.summarizepaper.com/en/arxiv-id/2303.09014v1/"},{"title":"[2303.09014v1] ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/abs/2303.09014v1"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://arxiv.org/pdf/2303.09014v1"},{"title":"ART: Automatic multi-step reasoning and tool-use for large language models","url":"https://paperreading.club/page?id=156016"},{"title":"ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models","url":"https://blog.synapticlabs.ai/art-automatic-multi-step-reasoning-and-tool-use-for-large-language-models"}]

I found the paper you're looking for. Here's what I found:

**ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models** is a paper authored by Bhargavi Paranjape, Scott Lundberg, Sameer Singh, Hannaneh Hajishirzi, Luke Zettlemoyer, and Marco Tulio Ribeiro, published on March 16, 2023, as arXiv paper 2303.09014.

**Key Points about the Paper:**

ART is a framework that uses frozen LLMs to automatically generate intermediate reasoning steps as a program. Given a new task to solve, ART
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:26:42.870856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models NeurIPS 2023 Lu Pan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models NeurIPS 2023 Lu Pan"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:26:42.871013+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge\" arXiv 2604.19749"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge\" arXiv 2604.19749"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:26:42.871174+00:00_

Web search results for query: ""The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge" arXiv 2604.19749"

Links: [{"title":"[2604.19749] The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?","url":"https://arxiv.org/abs/2604.19749"},{"title":"The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?","url":"https://arxiv.org/html/2604.19749v1"},{"title":"From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in Large Language Models","url":"https://arxiv.org/html/2511.10899v2"},{"title":"Do LLMs Know Tool Irrelevance? Demystifying Structural Alignment Bias in Tool Invocations","url":"https://arxiv.org/html/2604.11322"},{"title":"Breaking the Illusion of Identity in LLM Tooling","url":"https://arxiv.org/html/2604.07398v1"},{"title":"Thinking Isn’t an Illusion: Overcoming the Limitations of Reasoning Models via Tool Augmentations","url":"https://arxiv.org/html/2507.17699v1"},{"title":"TInR: Exploring Tool-Internalized Reasoning in Large Language Models","url":"https://arxiv.org/html/2604.10788"},{"title":"Reducing Tool Hallucination via Reliability Alignment","url":"https://arxiv.org/html/2412.04141v1"},{"title":"Teaching LLMs to Learn Tool Trialing and Execution through Environment Interaction","url":"https://arxiv.org/html/2601.12762v1"}]

I found the paper! Here's information about "The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?" (arXiv 2604.19749):

## Overview

This paper, submitted on March 3, 2026, addresses the phenomenon of tool overuse—unnecessary tool-use during reasoning—which emerges when LLMs are equipped with external tools.

## Key Findings

The paper reveals that tool overuse is pervasive across diverse LLMs. The authors identify a "knowledge epistemic illusion": models misjudge internal knowledge boundaries and fail to accurately perceive their actual knowledge availability.

## Proposed Solution

…[truncated 759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:26:42.871343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLM Agents Already Know When to Call Tools\" arXiv 2605.09252"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLM Agents Already Know When to Call Tools\" arXiv 2605.09252"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:26:42.871482+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 30 · 2026-05-26T10:26:42.871610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:26:42.871739+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes Amitai Septon Amir AAAI 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes Amitai Septon Amir AAAI 2024"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:26:42.871880+00:00_

Web search results for query: "Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes Amitai Septon Amir AAAI 2024"

Links: [{"title":"Explaining reinforcement learning agents through counterfactual action outcomes | Proceedings of the Thirty-Eighth AAAI Conference on Artificial Intelligence and Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence and Fourteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v38i9.28863"},{"title":"[2312.11118] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/abs/2312.11118"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/explaining-reinforcement-learning-agents-through-counterfactual-a"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes","url":"https://ojs.aaai.org/index.php/AAAI/article/download/28863/29640"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes | Request PDF","url":"https://www.researchgate.net/publication/379288542_Explaining_Reinforcement_Learning_Agents_through_Counterfactual_Action_Outcomes"},{"title":"[PDF] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Explaining-Reinforcement-Learning-Agents-Through-Amitai-Septon/66766682c5669964ec6405e0acd9ca228024c5ab"},{"title":"Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/html/2312.11118v1"},{"title":"Counterfactual Explanations for Continuous Action Reinforcement Learning","url":"https://arxiv.org/html/2505.12701v1"},{"title":"Yotam Amitai - Publications","url":"https://www.yotamitai.com/publications"}]

I found the research paper you're looking fo
…[truncated 1275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:26:42.872063+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Counterfactual Explanations for Reinforcement Learning Agents Gajcin Jasmina AAMAS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Counterfactual Explanations for Reinforcement Learning Agents Gajcin Jasmina AAMAS 2023"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:26:42.872221+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 35 · 2026-05-26T10:26:42.872354+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:26:42.872484+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Measuring Mathematical Problem Solving With the MATH Dataset Hendrycks NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Measuring Mathematical Problem Solving With the MATH Dataset Hendrycks NeurIPS 2021"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:26:42.872613+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 Technical Report arXiv 2412.15115"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 Technical Report arXiv 2412.15115"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:26:42.872740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "The Llama 3 Herd of Models arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "The Llama 3 Herd of Models arXiv 2407.21783"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:26:42.872863+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cameron Gelbach Miller \"Bootstrap-Based Improvements for Inference with Clustered Errors\" Review of Economics and Statistics 2008"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:26:42.873008+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Achiam Held Tamar Abbeel \"Constrained Policy Optimization\" ICML 2017"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:26:42.873146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolACE Winning the Points of LLM Function Calling ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolACE Winning the Points of LLM Function Calling ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:26:42.873271+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Webb \"Reworking Wild Bootstrap-Based Inference for Clustered Errors\" Canadian Journal of Economics 2023"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-26T10:26:42.873413+00:00_

Web search results for query: "Measuring Mathematical Problem Solving With the MATH Dataset Hendrycks NeurIPS 2021"

Links: [{"title":"GitHub - hendrycks/math: The MATH Dataset (NeurIPS 2021) · GitHub","url":"https://github.com/hendrycks/math"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/be83ab3ecd0db773eb2dc1b0a17836a1-Paper-round2.pdf"},{"title":"[2103.03874] Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://arxiv.org/abs/2103.03874"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/be83ab3ecd0db773eb2dc1b0a17836a1-Abstract-round2.html"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset Dan Hendrycks","url":"https://arxiv.org/pdf/2103.03874"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset | OpenReview","url":"https://openreview.net/forum?id=7Bywt2mQsCe"},{"title":"[PDF] Measuring Mathematical Problem Solving With the MATH Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-Mathematical-Problem-Solving-With-the-Hendrycks-Burns/57d1e7ac339e783898f2c3b1af55737cbeee9fc5"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset | Request PDF","url":"https://www.researchgate.net/publication/349880265_Measuring_Mathematical_Problem_Solving_With_the_MATH_Dataset"},{"title":"--- dataset_info: features: - name: problem dtype: string - name: solution","url":"https://huggingface.co/datasets/nlile/hendrycks-MATH-benchmark/raw/main/README.md"},{"title":"Measuring Mathematical Problem Solving With the MATH Dataset - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303874H/abstract"}]

I found the paper and resources for you. Here's what the search revealed:

## Overview

"Measuring Mathematical Problem Solving With the MATH Dataset" is by Dan He
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:26:42.873573+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Moldovan Abbeel \"Safe Exploration in Markov Decision Processes\" ICML 2012"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:26:42.873703+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Graves \"Adaptive Computation Time for Recurrent Neural Networks\" arXiv 1603.08983"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:26:42.873978+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 5",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n37. ruan2024failures\nTitle: Identifying the Risks of LM Agents with an LM-Emulated Sandbox\nAuthors: Ruan, Yangjun and Dong, Honghua and Wang, Andrew and Pitis, Silviu and Zhou, Yongchao and Ba, Jimmy and Dubois, Yann and Maddison, Chris J. and Hashimoto, Tatsunori\nVenue: ICLR 2024\nYear: 2024\n\n38. saferoute-2025\nTitle: SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\nAuthors: Lee, Seanie and others\nVenue: Findings of ACL 2025\nYear: 2025\n\n39. altman1999constrained\nTitle: Constrained Markov Decision Processes\nAuthors: Altman, Eitan\nPublisher: Chapman & Hall/CRC\nYear: 1999\n\n40. mihatsch2002risk\nTitle: Risk-Sensitive Reinforcement Learning\nAuthors: Mihatsch, Oliver and Neuneier, Ralph\nJournal: Machine Learning, vol 49, no 2-3, pp 267-290\nYear: 2002\n\n41. natarajan2013learning\nTitle: Learning with Noisy Labels\nAuthors: Natarajan, Nagarajan and Dhillon, Inderjit S. and Ravikumar, Pradeep and Tewari, Ambuj\nVenue: NeurIPS 2013\nYear: 2013\n\n42. budget-aware-routing-2026\nTitle: Budget-Aware Agentic Routing via Boundary-Guided Training\nAuthors: Zhang, Caiqi and Xia, Menglin and Zhang, Xuchao and Madrigal, Daniel and Mallick, Ankur and Kessler, Samuel and Ruehle, Victor and Rajmohan, Saravan\nJournal: arXiv:2602.21227\nYear: 2026\n\n43. pona2025abstract\nTitle: Abstract Counterfactuals for Language Model Agents\nAuthors: Pona, Edoardo and Kazemi, Milad and Du, Yali and Watson, David and Paoletti, Nicola\nJournal: arXiv:2506.02946\nYear: 2025\n\n44. cso-2026\nTitle: Verified Critical Step Optimization for LLM Agents\nAuthors: Li, Mukai and Zeng, Qingcheng and Fang, Tianqing and Liang, Zhenwen and Song, Linfeng and Liu, Qi and Mi, Haitao and Yu, Dong\nJournal: arXiv:2602.03412\nYear: 2026\n\n45. axis-2026\nTitle: Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\nAuthors: Gyevnár, Bálint and Lucas, Christopher G. and Albrecht, Stefano V. and Cohen, Shay B.\nJournal: arXiv:2505.17801\nYear: 2025\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 5",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n37. ruan2024failures\nTitle: Identifying the Risks of LM Agents with an LM-Emulated Sandbox\nAuthors: Ruan, Yangjun and Dong, Honghua and Wang, Andrew and Pitis, Silviu and Zhou, Yongchao and Ba, Jimmy and Dubois, Yann and Maddison, Chris J. and Hashimoto, Tatsunori\nVenue: ICLR 2024\nYear: 2024\n\n38. saferoute-2025\nTitle: SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\nAuthors: Lee, Seanie and others\nVenue: Findings of ACL 2025\nYear: 2025\n\n39. altman1999constrained\nTitle: Constrained Markov Decision Processes\nAuthors: Altman, Eitan\nPublisher: Chapman & Hall/CRC\nYear: 1999\n\n40. mihatsch2002risk\nTitle: Risk-Sensitive Reinforcement Learning\nAuthors: Mihatsch, Oliver and Neuneier, Ralph\nJournal: Machine Learning, vol 49, no 2-3, pp 267-290\nYear: 2002\n\n41. natarajan2013learning\nTitle: Learning with Noisy Labels\nAuthors: Natarajan, Nagarajan and Dhillon, Inderjit S. and Ravikumar, Pradeep and Tewari, Ambuj\nVenue: NeurIPS 2013\nYear: 2013\n\n42. budget-aware-routing-2026\nTitle: Budget-Aware Agentic Routing via Boundary-Guided Training\nAuthors: Zhang, Caiqi and Xia, Menglin and Zhang, Xuchao and Madrigal, Daniel and Mallick, Ankur and Kessler, Samuel and Ruehle, Victor and Rajmohan, Saravan\nJournal: arXiv:2602.21227\nYear: 2026\n\n43. pona2025abstract\nTitle: Abstract Counterfactuals for Language Model Agents\nAuthors: Pona, Edoardo and Kazemi, Milad and Du, Yali and Watson, David and Paoletti, Nicola\nJournal: arXiv:2506.02946\nYear: 2025\n\n44. cso-2026\nTitle: Verified Critical Step Optimization for LLM Agents\nAuthors: Li, Mukai and Zeng, Qingcheng and Fang, Tianqing and Liang, Zhenwen and Song, Linfeng and Liu, Qi and Mi, Haitao and Yu, Dong\nJournal: arXiv:2602.03412\nYear: 2026\n\n45. axis-2026\nTitle: Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\nAuthors: Gyevnár, Bálint and Lucas, Christopher G. and Albrecht, Stefano V. and Cohen, Shay B.\nJournal: arXiv:2505.17801\nYear: 2025\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:26:42.874237+00:00_

Web search results for query: "Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models NeurIPS 2023 Lu Pan"

Links: [{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/871ed095b734818cfba48db6aeb25a62-Abstract-Conference.html"},{"title":"[2304.09842] Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://arxiv.org/abs/2304.09842"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://lupantech.github.io/papers/neurips23_chameleon.pdf"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"https://chameleon-llm.github.io/"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models","url":"http://web.cs.ucla.edu/~kwchang/bibliography/lu2023chameleon/"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=HtqnVSCj3q&noteId=AkDivMFFzq"},{"title":"GitHub - lupantech/chameleon-llm: Codes for \"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\".","url":"https://github.com/lupantech/chameleon-llm"},{"title":"[PDF] Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chameleon:-Plug-and-Play-Compositional-Reasoning-Lu-Peng/170c97c7215f42edfb20c2248f954879e91ef86e"},{"title":"Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/chameleon-plug-and-play-compositional-reasoning-with-large-language-models/"}]

I found detailed information about the paper. Here's what I found:

## Overview

Chameleon is an AI system that mitigates limitations of LLMs by augmenting them with plug-and-play modules for compositio
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T10:26:42.874421+00:00_

Web search results for query: ""LLM Agents Already Know When to Call Tools" arXiv 2605.09252"

Links: [{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v2"},{"title":"[2605.09252] LLM Agents Already Know When to Call Tools -- Even Without Reasoning","url":"https://arxiv.org/abs/2605.09252"},{"title":"LLM Agents Already Know When to Call Tools","url":"https://lilywenglab.github.io/when2tool/"},{"title":"GitHub - Trustworthy-ML-Lab/when2tool · GitHub","url":"https://github.com/Trustworthy-ML-Lab/when2tool"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737v1"},{"title":"[2605.00737] To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/abs/2605.00737"},{"title":"0.75686 0.33333 0.65882F0.64706 0.35294 0.68627i0.54118 0.37255 0.71765n0.43137 0.39216 0.7451T0.32549 0.41176 0.77647r0.21569 0.43137 0.80392a0.1098 0.45098 0.83529c0 0.47059 0.86275e\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:\\__color_backend_reset:: Holistic Trajectory-Level Evaluation of LLM Tool Calling for Long-Horizon Financial Tasks","url":"https://arxiv.org/html/2604.10015"},{"title":"Tool Calling is Linearly Readable and Steerable in Language Models","url":"https://arxiv.org/html/2605.07990"},{"title":"LLM agents learn to ask under unclear instructions | Let's Data Science","url":"https://letsdatascience.com/news/llm-agents-learn-to-ask-under-unclear-instructions-0840af97"}]

I found the paper! Here's information about "LLM Agents Already Know When to Call Tools" (arXiv 2605.09252):

## Overview

The paper is authored by Chung-En Sun, Linbo Liu, Ge Yan, Zimo Wang, and Tsui-Wei Weng from UC San Diego, with a publication date of May 20, 2026.

## Main Problem

Tool-augmented LLM agents t
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:26:42.874600+00:00_

Web search results for query: "Counterfactual Explanations for Reinforcement Learning Agents Gajcin Jasmina AAMAS 2023"

Links: [{"title":"Counterfactual Explanations for Reinforcement Learning Agents","url":"https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p2925.pdf"},{"title":"Counterfactual Explanations for Reinforcement Learning Agents | Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems","url":"https://dl.acm.org/doi/abs/10.5555/3545946.3599126"},{"title":"Semifactual Explanations for Reinforcement Learning | Proceedings of the 12th International Conference on Human-Agent Interaction","url":"https://dl.acm.org/doi/10.1145/3687272.3688324"},{"title":"[2210.11846] Redefining Counterfactual Explanations for Reinforcement Learning: Overview, Challenges and Opportunities","url":"https://arxiv.org/abs/2210.11846"},{"title":"Counterfactual explanations for reinforcement learning: interview with Jasmina Gajcin - ΑΙhub","url":"https://aihub.org/2022/11/22/counterfactual-explanations-for-reinforcement-learning-interview-with-jasmina-gajcin/"},{"title":"GANterfactual-RL: Understanding Reinforcement Learning Agents' Strategies through Visual Counterfactual Explanations | Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems","url":"https://dl.acm.org/doi/10.5555/3545946.3598751"},{"title":"[PDF] RACCER: Towards Reachable and Certain Counterfactual Explanations for Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RACCER:-Towards-Reachable-and-Certain-Explanations-Gajcin-Dusparic/86148a95c5bd64493d8fc19b4289494c4ab0f0cf"},{"title":"(PDF) Counterfactual Explanations for Reinforcement Learning","url":"https://www.researchgate.net/publication/364658524_Counterfactual_Explanations_for_Reinforcement_Learning"},{"title":"[2303.04475] RACCER: Towards Reachable and Certain Counterfactual Explanations for Reinforcement Learning","url":"https://arxiv.org/abs/2303.0
…[truncated 1338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:26:42.874771+00:00_

Web search results for query: "The Llama 3 Herd of Models arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"}]

Based on the search results, here's what I found about the paper "The Llama 3 Herd of Models" (arXiv 2407.21783):

The paper presents a new set of foundation models, called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

The paper finds that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. The authors publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and their Llama Guard 3 model for input and output safety.

The paper also presents the results of experiments in which they integrate image, video, and speech capabilities into Llama 3 via a compositional approach.

The paper was submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024. You can access it directly at https://arxiv.org/abs/2407.21783.


REMINDER: You MUST include the sou
…[truncated 66 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:26:42.874944+00:00_

Web search results for query: "Achiam Held Tamar Abbeel "Constrained Policy Optimization" ICML 2017"

Links: [{"title":"Constrained Policy Optimization","url":"https://proceedings.mlr.press/v70/achiam17a.html"},{"title":"Constrained policy optimization | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305384"},{"title":"Constrained Policy Optimization | Tejaswi Kasarla","url":"https://tkasarla.github.io/2017/10/19/constrained-policy-optimization/"},{"title":"[1705.10528] Constrained Policy Optimization","url":"https://arxiv.org/abs/1705.10528"},{"title":"[PDF] Constrained Policy Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Constrained-Policy-Optimization-Achiam-Held/7a4193d0b042643a8bb9ec262ed7f9d509bdb12e"},{"title":"Constrained Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/317240991_Constrained_Policy_Optimization"},{"title":"Constrained policy optimization - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/constrained-policy-optimization/"},{"title":"GitHub - jachiam/cpo: Constrained Policy Optimization · GitHub","url":"https://github.com/jachiam/cpo"},{"title":"Constrained Policy Optimization - Robotics Institute Carnegie Mellon University","url":"https://www.ri.cmu.edu/publications/constrained-policy-optimization/"},{"title":"State-wise Constrained Policy Optimization","url":"https://arxiv.org/html/2306.12594v3"}]

Based on the search results, I found comprehensive information about this paper:

The paper "Constrained Policy Optimization" was authored by Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel, and was published in the Proceedings of the 34th International Conference on Machine Learning in 2017 (pages 22-31).

The paper proposes Constrained Policy Optimization (CPO), the first general-purpose policy search algorithm for constrained reinforcement learni
…[truncated 744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:26:42.875142+00:00_

Web search results for query: "Cameron Gelbach Miller "Bootstrap-Based Improvements for Inference with Clustered Errors" Review of Economics and Statistics 2008"

Links: [{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors","url":"https://ideas.repec.org/a/tpr/restat/v90y2008i3p414-427.html"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors | The Review of Economics and Statistics | MIT Press","url":"https://direct.mit.edu/rest/article/90/3/414/57731/Bootstrap-Based-Improvements-for-Inference-with"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors | NBER","url":"https://www.nber.org/papers/t0344"},{"title":"Bootstrap-Based Improvements for Inference with ...","url":"https://www.nber.org/system/files/working_papers/t0344/t0344.pdf"},{"title":"EconPapers: Bootstrap-Based Improvements for Inference with Clustered Errors","url":"https://econpapers.repec.org/RePEc:tpr:restat:v:90:y:2008:i:3:p:414-427"},{"title":"Bootstrap-Based Improvments for Inference With Clustered Errors | Request PDF","url":"https://www.researchgate.net/publication/24096179_Bootstrap-Based_Improvments_for_Inference_With_Clustered_Errors"},{"title":"Sci-Hub | Bootstrap-Based Improvements for Inference with Clustered Errors | 10.1162/rest.90.3.414","url":"https://sci-hub.ee/10.1162/REST.90.3.414"},{"title":"Bootstrap-Based Improvements for Inference with Clustered Errors by A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=956890"},{"title":"(PDF) Bootstrap-Based Improvements for Inference with Clustered Errors (2007) | A. Colin Cameron | 999 Citations","url":"https://scispace.com/papers/bootstrap-based-improvements-for-inference-with-clustered-2rr1liz8yy"}]

I found the paper you're looking for. The paper "Bootstrap-Based Improvements for Inference with Clustered Errors" by A. Colin Cameron, Jonah B. Gelbach, and Douglas L. Miller was published in The Revi
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T10:26:42.875312+00:00_

Web search results for query: "Webb "Reworking Wild Bootstrap-Based Inference for Clustered Errors" Canadian Journal of Economics 2023"

Links: [{"title":"Reworking wild bootstrap‐based inference for clustered errors - Webb - 2023 - Canadian Journal of Economics/Revue canadienne d'économique - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/caje.12661"},{"title":"Reworking Wild Bootstrap Based Inference For Clustered Errors","url":"https://ideas.repec.org/p/qed/wpaper/1315.html"},{"title":"Reworking wild bootstrap‐based inference for clustered errors - No. 56-3, August 2023 - Canadian Journal of Economics - Books and Journals - VLEX 1042749625 - vLex","url":"https://ca.vlex.com/vid/reworking-wild-bootstrapbased-inference-1042749625"},{"title":"Literature on the Wild Bootstrap and Clustered Inference in Regression Models • fwildclusterboot","url":"https://s3alfisc.github.io/fwildclusterboot/articles/Literature.html"},{"title":"Reworking wild bootstrap‐based inference for clustered errors","url":"https://ideas.repec.org/a/wly/canjec/v56y2023i3p839-858.html"},{"title":"Replication Data and Code for: Reworking Wild Bootstrap Based Inference for Clustered Errors - Canadian Journal of Economics (CJE)","url":"https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/BBZFOY"},{"title":"Reworking wild bootstrap‐based inference for clustered errors | Request PDF","url":"https://www.researchgate.net/publication/370920784_Reworking_wild_bootstrap-based_inference_for_clustered_errors"}]

I found the article you're looking for! Here are the details:

**Author:** Matthew D. Webb

**Title:** Reworking wild bootstrap-based inference for clustered errors

**Journal:** Canadian Journal of Economics/Revue canadienne d'économique

**Publication Details:** &lt;cite index="2-4,2-5">Volume 56(3), pages 839-858, August 2023&lt;/cite>

**Summary:** Cluster-robust inference is increasingly common in empirical research. With few clusters, inference is often conducte
…[truncated 455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:26:42.875485+00:00_

Web search results for query: "Graves "Adaptive Computation Time for Recurrent Neural Networks" arXiv 1603.08983"

Links: [{"title":"[1603.08983] Adaptive Computation Time for Recurrent Neural Networks","url":"https://arxiv.org/abs/1603.08983"},{"title":"Adaptive Computation Time for Recurrent Neural Networks","url":"https://www.researchgate.net/publication/301879022_Adaptive_Computation_Time_for_Recurrent_Neural_Networks"},{"title":"Adaptive Computation Time for Recurrent Neural Networks Alex Graves","url":"https://arxiv.org/pdf/1603.08983"},{"title":"Adaptive Computation Time - Hugo Cisneros","url":"https://hugocisneros.com/notes/adaptive_computation_time/"},{"title":"[PDF] Adaptive Computation Time for Recurrent Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adaptive-Computation-Time-for-Recurrent-Neural-Graves/04cca8e341a5da42b29b0bc831cb25a0f784fa01"},{"title":"[1603.08983v1] Adaptive Computation Time for Recurrent Neural Networks","url":"https://arxiv.org/abs/1603.08983v1"},{"title":"Adaptive Computation Time (ACT) in Neural Networks [1/3] | by Grigory Sapunov | Medium","url":"https://moocaholic.medium.com/adaptive-computation-time-act-in-neural-networks-part-1-2a28484b53df"},{"title":"Adaptive Computation Time for Recurrent Neural Networks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1960640a28f3e578a76d374b587717749"}]

I found the paper you're looking for. Here are the key details:

**Title:** Adaptive Computation Time for Recurrent Neural Networks

**Author:** Alex Graves

**arXiv Identifier:** 1603.08983

**Publication Timeline:** Submitted on 29 March 2016 (v1), last revised 21 February 2017 (v6)

**Overview:** The paper introduces Adaptive Computation Time (ACT), an algorithm that allows recurrent neural networks to learn how many computational steps to take between receiving an input and emitting an output. ACT requires minimal changes to the network architecture, is deterministic and differentiable, and does 
…[truncated 576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:26:42.875650+00:00_

Web search results for query: "Qwen2.5 Technical Report arXiv 2412.15115"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Paper page - Qwen2.5 Technical Report","url":"https://huggingface.co/papers/2412.15115"},{"title":"Qwen2.5 Technical Report","url":"https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"[2412.15115v1] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v1"},{"title":"Qwen2.5-Max: Exploring the Intelligence of Large-scale MoE Model | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-max/"},{"title":"[2412.15115v2] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v2"},{"title":"2024-12-20 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115v1"}]

I found the Qwen2.5 Technical Report for you. Here's a summary of the key information:

## Overview

Qwen2.5 is a comprehensive series of large language models (LLMs) designed to meet diverse needs.

## Key Improvements

Compared to previous iterations, Qwen 2.5 has been significantly improved during both the pre-training and post-training stages, with the high-quality pre-training datasets scaled from 7 trillion tokens to 18 trillion tokens.

**Pre-training:** The expanded dataset provides a strong foundation for common sense, expert knowledge, and reasoning capabilities.

**Post-training:** The team implements intricate supervised finetuning with over 1 million samples, as well as multistage reinforcement learning.

## Model Configurations

The open-weight offerings include base models and ins
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:26:42.875824+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 6",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n46. salt-2026\nTitle: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\nAuthors: Li, Jiazheng and Wang, Yawei and Yan, David and Tian, Yijun and Xu, Zhichao and Song, Huan and Xu, Panpan and Cheong, Lin Lee\nVenue: Findings of EACL 2026\nYear: 2026\n\n47. gemma2-2024\nTitle: Gemma 2: Improving Open Language Models at a Practical Size\nAuthors: Gemma Team\nJournal: arXiv:2408.00118\nYear: 2024\n\n48. northcutt2021confident\nTitle: Confident Learning: Estimating Uncertainty in Dataset Labels\nAuthors: Northcutt, Curtis and Jiang, Lu and Chuang, Isaac\nJournal: JAIR, vol 70, pp 1373-1411\nYear: 2021\n\n49. li2020dividemix\nTitle: DivideMix: Learning with Noisy Labels as Semi-supervised Learning\nAuthors: Li, Junnan and Socher, Richard and Hoi, Steven C.H.\nVenue: ICLR 2020\nYear: 2020\n\n50. ng1999policy\nTitle: Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\nAuthors: Ng, Andrew Y. and Harada, Daishi and Russell, Stuart\nVenue: ICML 1999\nYear: 1999\n\n51. agent-safetybench-2024\nTitle: Agent-SafetyBench: Evaluating the Safety of LLM Agents\nAuthors: Zhang, Zhexin and Cui, Shiyao and Lu, Yida and Zhou, Jingzhuo and Yang, Junhao and Liu, Jie and Wang, Renhao and Li, Jiangjie and Huang, Minlie\nJournal: arXiv:2412.14470\nYear: 2024\n\n52. pearl2009causality\nTitle: Causality: Models, Reasoning, and Inference\nAuthors: Pearl, Judea\nPublisher: Cambridge University Press, 2nd edition\nYear: 2009\n\n53. rubin1974estimating\nTitle: Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\nAuthors: Rubin, Donald B.\nJournal: Journal of Educational Psychology, vol 66, no 5, pp 688-701\nYear: 1974\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 6",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n46. salt-2026\nTitle: SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\nAuthors: Li, Jiazheng and Wang, Yawei and Yan, David and Tian, Yijun and Xu, Zhichao and Song, Huan and Xu, Panpan and Cheong, Lin Lee\nVenue: Findings of EACL 2026\nYear: 2026\n\n47. gemma2-2024\nTitle: Gemma 2: Improving Open Language Models at a Practical Size\nAuthors: Gemma Team\nJournal: arXiv:2408.00118\nYear: 2024\n\n48. northcutt2021confident\nTitle: Confident Learning: Estimating Uncertainty in Dataset Labels\nAuthors: Northcutt, Curtis and Jiang, Lu and Chuang, Isaac\nJournal: JAIR, vol 70, pp 1373-1411\nYear: 2021\n\n49. li2020dividemix\nTitle: DivideMix: Learning with Noisy Labels as Semi-supervised Learning\nAuthors: Li, Junnan and Socher, Richard and Hoi, Steven C.H.\nVenue: ICLR 2020\nYear: 2020\n\n50. ng1999policy\nTitle: Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\nAuthors: Ng, Andrew Y. and Harada, Daishi and Russell, Stuart\nVenue: ICML 1999\nYear: 1999\n\n51. agent-safetybench-2024\nTitle: Agent-SafetyBench: Evaluating the Safety of LLM Agents\nAuthors: Zhang, Zhexin and Cui, Shiyao and Lu, Yida and Zhou, Jingzhuo and Yang, Junhao and Liu, Jie and Wang, Renhao and Li, Jiangjie and Huang, Minlie\nJournal: arXiv:2412.14470\nYear: 2024\n\n52. pearl2009causality\nTitle: Causality: Models, Reasoning, and Inference\nAuthors: Pearl, Judea\nPublisher: Cambridge University Press, 2nd edition\nYear: 2009\n\n53. rubin1974estimating\nTitle: Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\nAuthors: Rubin, Donald B.\nJournal: Journal of Educational Psychology, vol 66, no 5, pp 688-701\nYear: 1974\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:26:42.876091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs arXiv 2504.11536"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs arXiv 2504.11536"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:26:42.876273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\" arXiv 2605.00136"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\" arXiv 2605.00136"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:26:42.876417+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson Khanna Neal Li Wong Artificial Intelligence 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson Khanna Neal Li Wong Artificial Intelligence 2021"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T10:26:42.876566+00:00_

Web search results for query: "ToolACE Winning the Points of LLM Function Calling ICLR 2025"

Links: [{"title":"TOOLACE: WINNING THE POINTS OF LLM FUNCTION ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf"},{"title":"ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/pdf/2409.00920"},{"title":"ToolACE: Winning the Points of LLM Function Calling | OpenReview","url":"https://openreview.net/forum?id=8EB8k6DdCU"},{"title":"WINNING THE POINTS OF LLM FUNCTION CALLING","url":"https://openreview.net/pdf?id=8EB8k6DdCU"},{"title":"[2409.00920] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920"},{"title":"ICLR Poster ToolACE: Winning the Points of LLM Function Calling","url":"https://iclr.cc/virtual/2025/poster/30779"},{"title":"ToolACE: Winning the Points of LLM Function Calling | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/toolace-winning-points-llm-function-calling"},{"title":"(PDF) ToolACE: Winning the Points of LLM Function Calling","url":"https://www.researchgate.net/publication/383701460_ToolACE_Winning_the_Points_of_LLM_Function_Calling"},{"title":"[2409.00920v1] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920v1"}]

Based on the search results, here's what I found about ToolACE:

## Overview

ToolACE was published as a conference paper at ICLR 2025. Function calling significantly extends the application boundary of large language models (LLMs), where high-quality and diverse training data is critical for unlocking this capability.

## The ToolACE Approach

ToolACE is an automatic agentic pipeline designed to generate accurate, complex, and diverse tool-learning data, specifically tailored to the capabilities of LLMs. ToolACE leverages a novel self-evolution synthesis process to curate a comprehensive API pool of 26,507 diverse APIs. Dialogs are further gene
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:26:42.876740+00:00_

Web search results for query: "Moldovan Abbeel "Safe Exploration in Markov Decision Processes" ICML 2012"

Links: [{"title":"Safe Exploration in Markov Decision Processes Teodor Mihai Moldovan","url":"https://icml.cc/2012/papers/838.pdf"},{"title":"[1205.4810] Safe Exploration in Markov Decision Processes","url":"https://arxiv.org/abs/1205.4810"},{"title":"Safe Exploration in Finite Markov Decision Processes with Gaussian Processes","url":"https://las.inf.ethz.ch/files/turchetta16safemdp.pdf"},{"title":"[PDF] Safe Exploration in Markov Decision Processes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Safe-Exploration-in-Markov-Decision-Processes-Moldovan-Abbeel/d66ab178e941e3a79954c858d3c1bcdee8e1d17d"},{"title":"Safe exploration in Markov decision processes | Proceedings of the 29th International Coference on International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3042573.3042759"},{"title":"Safe Exploration in Markov Decision Processes | Request PDF","url":"https://www.researchgate.net/publication/225045205_Safe_Exploration_in_Markov_Decision_Processes"},{"title":"Safe Exploration for Optimization with Gaussian Processes","url":"http://proceedings.mlr.press/v37/sui15-supp.pdf"},{"title":"Safe Exploration in Markov Decision Processes Teodor Mihai Moldovan","url":"https://www.cs.ubc.ca/~hutter/nips2011workshop/papers_and_posters/safe_exploration.pdf"}]

I found relevant information about the paper. Here are the search results:

The paper "Safe Exploration in Markov Decision Processes" is authored by Teodor Mihai Moldovan and Pieter Abbeel. It was presented at the International Conference on Machine Learning (ICML) in 2012, pages 1711–1718.

The paper proposes a general formulation of safety through ergodicity, and shows that imposing safety by restricting attention to the resulting set of guaranteed safe policies is NP-hard, and presents an efficient algorithm for guaranteed safe, but potentially suboptimal, exploration.
…[truncated 419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:26:42.876907+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 63 · 2026-05-26T10:26:42.877064+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:26:42.877268+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 65 · 2026-05-26T10:26:42.877451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:26:42.877658+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolACE arXiv 2409.00920 authors list Weiwen Zhang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolACE arXiv 2409.00920 authors list Weiwen Zhang"
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-26T10:26:42.877889+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 7",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n54. switch-transformer-2022\nTitle: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\nAuthors: Fedus, William and Zoph, Barret and Shazeer, Noam\nJournal: JMLR, vol 23, no 120, pp 1-39\nYear: 2022\n\n55. gshard-2021\nTitle: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\nAuthors: Lepikhin, Dmitry and Lee, HyoukJoong and Xu, Yuanzhong and Chen, Dehao and Firat, Orhan and Huang, Yanping and Krikun, Maxim and Shazeer, Noam and Chen, Zhifeng\nVenue: ICLR 2021\nYear: 2021\n\n56. alshiekh2018safe\nTitle: Safe Reinforcement Learning via Shielding\nAuthors: Alshiekh, Mohammed and Bloem, Roderick and Ehlers, Rüdiger and Könighofer, Bettina and Niekum, Scott and Topcu, Ufuk\nVenue: AAAI 2018\nYear: 2018\n\n57. kaushik2020learning\nTitle: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\nAuthors: Kaushik, Divyansh and Hovy, Eduard and Lipton, Zachary C.\nVenue: ICLR 2020\nYear: 2020\n\n58. frugalgpt-2023\nTitle: FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\nAuthors: Chen, Lingjiao and Zaharia, Matei and Zou, James\nJournal: arXiv:2305.05176\nYear: 2023\n\n59. automix-2024\nTitle: AutoMix: Automatically Mixing Language Models\nAuthors: Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket\nVenue: NeurIPS 2024\nYear: 2024\n\n60. mixture-of-depths-2024\nTitle: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\nAuthors: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam\nVenue: ICML 2024\nYear: 2024\n\n61. leviathan2023speculative\nTitle: Fast Inference from Transformers via Speculative Decoding\nAuthors: Leviathan, Yaniv and Kalman, Matan and Matias, Yossi\nVenue: ICML 2023\nYear: 2023\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 7",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n54. switch-transformer-2022\nTitle: Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\nAuthors: Fedus, William and Zoph, Barret and Shazeer, Noam\nJournal: JMLR, vol 23, no 120, pp 1-39\nYear: 2022\n\n55. gshard-2021\nTitle: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\nAuthors: Lepikhin, Dmitry and Lee, HyoukJoong and Xu, Yuanzhong and Chen, Dehao and Firat, Orhan and Huang, Yanping and Krikun, Maxim and Shazeer, Noam and Chen, Zhifeng\nVenue: ICLR 2021\nYear: 2021\n\n56. alshiekh2018safe\nTitle: Safe Reinforcement Learning via Shielding\nAuthors: Alshiekh, Mohammed and Bloem, Roderick and Ehlers, Rüdiger and Könighofer, Bettina and Niekum, Scott and Topcu, Ufuk\nVenue: AAAI 2018\nYear: 2018\n\n57. kaushik2020learning\nTitle: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\nAuthors: Kaushik, Divyansh and Hovy, Eduard and Lipton, Zachary C.\nVenue: ICLR 2020\nYear: 2020\n\n58. frugalgpt-2023\nTitle: FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\nAuthors: Chen, Lingjiao and Zaharia, Matei and Zou, James\nJournal: arXiv:2305.05176\nYear: 2023\n\n59. automix-2024\nTitle: AutoMix: Automatically Mixing Language Models\nAuthors: Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket\nVenue: NeurIPS 2024\nYear: 2024\n\n60. mixture-of-depths-2024\nTitle: Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\nAuthors: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam\nVenue: ICML 2024\nYear: 2024\n\n61. leviathan2023speculative\nTitle: Fast Inference from Transformers via Speculative Decoding\nAuthors: Leviathan, Yaniv and Kalman, Matan and Matias, Yossi\nVenue: ICML 2023\nYear: 2023\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:26:42.878524+00:00_

Web search results for query: "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs arXiv 2504.11536"

Links: [{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/pdf/2504.11536"},{"title":"Paper page - ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://huggingface.co/papers/2504.11536"},{"title":"[2504.11536v1] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536v1"},{"title":"[2504.11536v2] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"http://arxiv.org/abs/2504.11536v2"},{"title":"[PDF] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReTool:-Reinforcement-Learning-for-Strategic-Tool-Feng-Huang/8402e446158252992b6ddf1ff1b0658c39d7604e"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.11536v1?locale=en"}]

I found the paper! Here's what the search revealed about ReTool:

## Overview

ReTool enhances long-form reasoning with tool-integrated learning, including dynamic interleaving of real-time code execution within natural language reasoning processes, and an automated RL paradigm that allows policy rollouts with multi-turn real-time code execution and teaches the model when and how to invoke tools based on outcome feedback.

## Motivation

While reasoning models like DeepSeek R1 trained with reinforcement learning excel in textual reasoning, they struggle in scenarios requiring structured problem-solving, such as geometric reasoning, concise computation, or complex equation solving—areas where computational tools like code interpreters demonstrate distinct advantages.

## Training Approach

ReTool employs a systematic tr
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-26T10:26:42.878801+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\" arXiv 2602.12662"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\" arXiv 2602.12662"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T10:26:42.879057+00:00_

Web search results for query: ""Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents" arXiv 2605.00136"

Links: [{"title":"[2605.00136] Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/abs/2605.00136"},{"title":"Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents","url":"https://arxiv.org/html/2605.00136v1"},{"title":"Artificial Intelligence May 2026","url":"https://arxiv.org/list/cs.AI/current"},{"title":"Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows","url":"https://arxiv.org/html/2604.21816v1"},{"title":"[2605.14038] Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use","url":"https://arxiv.org/abs/2605.14038"},{"title":"[2605.09252] LLM Agents Already Know When to Call Tools -- Even Without Reasoning","url":"https://arxiv.org/abs/2605.09252"},{"title":"UniToolCall: Unifying Tool-Use Representation, Data, and Evaluation for LLM Agents","url":"https://arxiv.org/html/2604.11557"}]

I found the arXiv paper you're looking for! Here's a summary of the research:

**Paper:** "Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents" (arXiv 2605.00136)

**Authors:** Kaituo Zhang, Zhen Xiong, Mingyu Zhong, Zhimeng Jiang, Zhouyuan Yuan, Zhecheng Li, and Ying Lin

**Key Findings:**

While tool-augmented reasoning has become popular for LLM-based agents and is widely assumed to improve reasoning and reliability, this consensus does not always hold when semantic distractors are present, as tool-augmented reasoning does not necessarily outperform native Chain-of-Thought (CoT).

To explain this performance gap, the authors propose a Factorized Intervention Framework that isolates the cost of prompt formatting, the overhead of the tool-calling protocol, and the actual gain from executing tools.

The analysis reveals a critical tradeoff: under semantic noise, the gains from tools often fail to of
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-26T10:26:42.879305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\" arXiv 2605.00737"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\" arXiv 2605.00737"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:26:42.879533+00:00_

Web search results for query: "Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning Olson Khanna Neal Li Wong Artificial Intelligence 2021"

Links: [{"title":"[2101.12446] Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://arxiv.org/abs/2101.12446"},{"title":"Counterfactual state explanations for reinforcement learning agents via generative deep learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370221000060"},{"title":"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210112446O/abstract"},{"title":"Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://www.researchgate.net/publication/348831791_Counterfactual_State_Explanations_for_Reinforcement_Learning_Agents_via_Generative_Deep_Learning"},{"title":"Matthew L. Olson, Roli Khanna, Lawrence Neal, Fuxin Li & Weng-Keen Wong, Counterfactual state explanations for reinforcement learning agents via generative deep learning - PhilPapers","url":"https://philpapers.org/rec/OLSCSE"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Counterfactual+state+explanations+for+reinforcement+learning+agents+via+generative+deep+learning&amp=&author=Matthew+L.+Olson&amp=&author=Roli+Khanna&amp=&author=Lawrence+Neal&amp=&author=Fuxin+Li&amp=&author=Weng-Keen+Wong&amp=&publication_year=2021&amp=&journal=Artificial+Intelligence&amp=&pages=103455&amp=&doi=10.1016/j.artint.2021.103455"},{"title":"(PDF) Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning","url":"https://www.researchgate.net/publication/348928549_Counterfactual_State_Explanations_for_Reinforcement_Learning_Agents_via_Generative_Deep_Learning"},{"title":"Counterfactual Explanations for Reinforcement L
…[truncated 1664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:26:42.879774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 3 Herd of Models authors Grattafiori Dubey arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 3 Herd of Models authors Grattafiori Dubey arXiv 2407.21783"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:26:42.879980+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 technical report authors list Yang An Yang Baosong"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 technical report authors list Yang An Yang Baosong"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:26:42.880233+00:00_

Web search results for query: "ToolACE arXiv 2409.00920 authors list Weiwen Zhang"

Links: [{"title":"ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/pdf/2409.00920"},{"title":"[2409.00920] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920"},{"title":"Paper page - ToolACE: Winning the Points of LLM Function Calling","url":"https://huggingface.co/papers/2409.00920"},{"title":"[2409.00920v1] ToolACE: Winning the Points of LLM Function Calling","url":"https://arxiv.org/abs/2409.00920v1"},{"title":"(PDF) ToolACE: Winning the Points of LLM Function Calling","url":"https://www.researchgate.net/publication/383701460_ToolACE_Winning_the_Points_of_LLM_Function_Calling"},{"title":"(PDF) ToolACE-R: Tool Learning with Adaptive Self-Refinement","url":"https://www.researchgate.net/publication/390439693_ToolACE-R_Tool_Learning_with_Adaptive_Self-Refinement"},{"title":"[PDF] ToolACE: Winning the Points of LLM Function Calling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ToolACE:-Winning-the-Points-of-LLM-Function-Calling-Liu-Huang/0350636522997217df53553ddf3e472338bca97b"}]

Based on the search results, I found the authors list for the ToolACE paper (arXiv 2409.00920). However, I should note that the first author is **Weiwen Liu**, not Weiwen Zhang as mentioned in your query.

The authors of the paper are: Weiwen Liu, Xu Huang, Xingshan Zeng, Xinlong Hao, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Zhengying Liu, Yuanqing Yu, Zezhong Wang, Yuxian Wang, Wu Ning, Yutai Hou, Bin Wang, Chuhan Wu, Xinzhi Wang, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, and Enhong Chen (27 authors total).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:26:42.880470+00:00_

Web search results for query: "Llama 3 Herd of Models authors Grattafiori Dubey arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"}]

I found the paper you're looking for! Here are the results:

The paper "The Llama 3 Herd of Models" presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

**Key Details:**

- **arXiv ID:** 2407.21783
- **Authors:** Aaron Grattafiori and Abhimanyu Dubey are among the lead authors, along with 558 other co-authors
- **Published:** July 31, 2024

**Paper Summary:**

The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

The authors publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:26:42.880713+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Identifying the Risks of LM Agents with an LM-Emulated Sandbox Ruan ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Identifying the Risks of LM Agents with an LM-Emulated Sandbox Ruan ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:26:42.880919+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeRoute Adaptive Model Selection Efficient Accurate Safety Guardrails LLMs Lee Seanie ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeRoute Adaptive Model Selection Efficient Accurate Safety Guardrails LLMs Lee Seanie ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:26:42.881151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Altman \"Constrained Markov Decision Processes\" Chapman Hall 1999 book"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Altman \"Constrained Markov Decision Processes\" Chapman Hall 1999 book"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:26:42.881357+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mihatsch Neuneier \"Risk-Sensitive Reinforcement Learning\" Machine Learning 2002"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-26T10:26:42.881563+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Natarajan Dhillon Ravikumar Tewari \"Learning with Noisy Labels\" NeurIPS 2013"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-26T10:26:42.881748+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Budget-Aware Agentic Routing via Boundary-Guided Training\" arXiv 2602.21227 Zhang 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Budget-Aware Agentic Routing via Boundary-Guided Training\" arXiv 2602.21227 Zhang 2026"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:26:42.881950+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Abstract Counterfactuals for Language Model Agents\" Pona Kazemi arXiv 2506.02946"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:26:42.882170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Verified Critical Step Optimization for LLM Agents\" Li Mukai arXiv 2602.03412"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Verified Critical Step Optimization for LLM Agents\" Li Mukai arXiv 2602.03412"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:26:42.882378+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\" Gyevnár arXiv 2505.17801"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T10:26:42.882620+00:00_

Web search results for query: "Altman "Constrained Markov Decision Processes" Chapman Hall 1999 book"

Links: [{"title":"Constrained Markov Decision Processes - 1st Edition - Shaler Stidham J","url":"https://www.routledge.com/Constrained-Markov-Decision-Processes/Altman/p/book/9780849303821"},{"title":"Amazon.com: Constrained Markov Decision Processes: Stochastic Modeling (Stochastic Modeling Series): 9780849303821: Altman, Eitan: Books","url":"https://www.amazon.com/Constrained-Decision-Processes-Stochastic-Modeling/dp/0849303826"},{"title":"Constrained Markov Decision Processes | BibSonomy","url":"https://www.bibsonomy.org/bibtex/184fb43430ab46ff2336d7e9926a37b45/jleny"},{"title":"Constrained Markov Decision Processes with Total Expected Cost Criteria | Proceedings of the 12th EAI International Conference on Performance Evaluation Methodologies and Tools","url":"https://dl.acm.org/doi/10.1145/3306309.3306342"},{"title":"Constrained Markov decision processes by Eitan Altman | Open Library","url":"https://openlibrary.org/books/OL97592M/Constrained_Markov_decision_processes"},{"title":"[PDF] Constrained Markov Decision Processes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Constrained-Markov-Decision-Processes-Altman/3cc2608fd77b9b65f5bd378e8797b2ab1b8acde7"},{"title":"Constrained Markov Decision Processes: Stochastic Modeling (Stochastic Modeling Series) - Altman, Eitan: 9780849303821 - AbeBooks","url":"https://www.abebooks.com/9780849303821/Constrained-Markov-Decision-Processes-Stochastic-0849303826/plp"},{"title":"Constrained Markov Decision Processes - Eitan Altman - Google Books","url":"https://books.google.com/books/about/Constrained_Markov_Decision_Processes.html?id=3X9S1NM2iOgC"},{"title":"(PDF) Constrained Markov Decision Processes (1999) | Eitan Altman | 1558 Citations","url":"https://typeset.io/papers/constrained-markov-decision-processes-3ndxrfjbtt"}]

I found information about the book you're looking for. The book "Constrained Markov 
…[truncated 791 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T10:26:42.882874+00:00_

Web search results for query: "SafeRoute Adaptive Model Selection Efficient Accurate Safety Guardrails LLMs Lee Seanie ACL 2025"

Links: [{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.105/"},{"title":"[2502.12464] SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/abs/2502.12464"},{"title":"Paper page - SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://huggingface.co/papers/2502.12464"},{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/html/2502.12464"},{"title":"Seanie Lee - Homepage","url":"https://seanie12.github.io/"},{"title":"Seanie Lee DATE OF BiRTH: 1992.04.17, NATiONALiTY: KOREAN","url":"https://seanie12.github.io/assets/cv.pdf"},{"title":"About me - Minki Kang","url":"https://nardien.github.io/"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"No Free Lunch With Guardrails","url":"https://arxiv.org/html/2504.00441v1"}]

Based on the search results, I found information about the SafeRoute paper:

SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models was authored by Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, and Sung Ju Hwang, and was published in the Findings of the Association for Computational Linguistics: ACL 2025 in Vienna, Austria.

The paper addresses an important challenge in LLM safety. While deploying large safety guard models introduces significant computational overhead, smaller safety guard models created through distillation improve efficiency but generally do not perform as well as their larger counterpart
…[truncated 536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:26:42.883182+00:00_

Web search results for query: "Identifying the Risks of LM Agents with an LM-Emulated Sandbox Ruan ICLR 2024"

Links: [{"title":"[2309.15817] Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://arxiv.org/abs/2309.15817"},{"title":"Identifying the Risks of LM Agents with an LM-Emulated Sandbox | OpenReview","url":"https://openreview.net/forum?id=GEcwtMk1uA"},{"title":"Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/7274ed909a312d4d869cc328ad1c5f04-Abstract-Conference.html"},{"title":"GitHub - ryoungj/ToolEmu: [ICLR'24 Spotlight] A language model (LM)-based emulation framework for identifying the risks of LM agents with tool use · GitHub","url":"https://github.com/ryoungj/ToolEmu"},{"title":"ICLR Poster Identifying the Risks of LM Agents with an LM-Emulated Sandbox","url":"https://iclr.cc/virtual/2024/poster/19037"},{"title":"Published as a conference paper at ICLR 2024 IDENTIFYING THE RISKS OF LM AGENTS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2024 IDENTIFYING THE RISKS OF LM AGENTS","url":"https://arxiv.org/pdf/2309.15817"},{"title":"[PDF] Identifying the Risks of LM Agents with an LM-Emulated Sandbox | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Identifying-the-Risks-of-LM-Agents-with-an-Sandbox-Ruan-Dong/0a893657e00fe8ecfadcc65c63bf293e70cb1564"}]

I found the paper you're looking for! Here's what I found:

**Paper Details:**

The paper "Identifying the Risks of LM Agents with an LM-Emulated Sandbox" was published at ICLR 2024 by Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, and Tatsunori Hashimoto from the University of Toronto, Vector Institute, and Stanford University.

**Overview:**

The paper addresses how recent advances in Language Model (LM) 
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:26:42.883431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SALT Step-level Advantage Assignment Long-horizon Agents Trajectory Graph Li Jiazheng 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SALT Step-level Advantage Assignment Long-horizon Agents Trajectory Graph Li Jiazheng 2026"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:26:42.883632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 2 Improving Open Language Models Practical Size arXiv 2408.00118"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 2 Improving Open Language Models Practical Size arXiv 2408.00118"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:26:42.883826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Confident Learning Estimating Uncertainty Dataset Labels Northcutt Jiang Chuang JAIR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Confident Learning Estimating Uncertainty Dataset Labels Northcutt Jiang Chuang JAIR 2021"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:26:42.884031+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DivideMix Learning with Noisy Labels Semi-supervised Learning Li Junnan ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DivideMix Learning with Noisy Labels Semi-supervised Learning Li Junnan ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:26:42.884271+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Policy Invariance Under Reward Transformations Theory Application Reward Shaping Ng Russell ICML 1999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Policy Invariance Under Reward Transformations Theory Application Reward Shaping Ng Russell ICML 1999"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:26:42.884480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-SafetyBench Evaluating Safety LLM Agents Zhang Zhexin arXiv 2412.14470"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-SafetyBench Evaluating Safety LLM Agents Zhang Zhexin arXiv 2412.14470"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:26:42.884671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pearl Judea Causality Models Reasoning Inference Cambridge University Press 2nd edition 2009"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pearl Judea Causality Models Reasoning Inference Cambridge University Press 2nd edition 2009"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:26:42.884864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rubin Donald Estimating Causal Effects Treatments Randomized Nonrandomized Studies Journal Educational Psychology 1974"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rubin Donald Estimating Causal Effects Treatments Randomized Nonrandomized Studies Journal Educational Psychology 1974"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:26:42.885098+00:00_

Web search results for query: "Gemma 2 Improving Open Language Models Practical Size arXiv 2408.00118"

Links: [{"title":"[2408.00118] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v1"},{"title":"2024-06-27 Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/pdf/2408.00118"},{"title":"(PDF) Gemma 2: Improving Open Language Models at a Practical Size","url":"https://www.researchgate.net/publication/382797528_Gemma_2_Improving_Open_Language_Models_at_a_Practical_Size"},{"title":"Paper page - Gemma 2: Improving Open Language Models at a Practical Size","url":"https://huggingface.co/papers/2408.00118"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240800118G/abstract"},{"title":"[PDF] Gemma 2: Improving Open Language Models at a Practical Size | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Gemma-2:-Improving-Open-Language-Models-at-a-Size-Riviere-Pathak/ec2ce4e38af8bc82f1b8928ba51a84911bad0cc6"},{"title":"[2408.00118v1] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v1"},{"title":"[2408.00118v3] Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/abs/2408.00118v3"}]

I found the research paper you're looking for. Here's what the search revealed:

Gemma 2 is a new addition to the Gemma family of lightweight, state-of-the-art open models, ranging in scale from 2 billion to 27 billion parameters. 

The new version applies several known technical modifications to the Transformer architecture, such as interleaving local-global attentions and group-query attention. The 2B and 9B models are trained with knowledge distillation instead of next token prediction.

The resulting models deliver the bes
…[truncated 474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:26:42.885353+00:00_

Web search results for query: "DivideMix Learning with Noisy Labels Semi-supervised Learning Li Junnan ICLR 2020"

Links: [{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning [Quick Review]","url":"https://liner.com/review/dividemix-learning-with-noisy-labels-as-semisupervised-learning"},{"title":"[PDF] DivideMix: Learning with Noisy Labels as Semi-supervised Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivideMix:-Learning-with-Noisy-Labels-as-Learning-Li-Socher/ce435482acc0e195be8d8f002b2655b4c7b08be6"},{"title":"DIVIDEMIX: LEARNING WITH NOISY LABELS AS SEMI- ...","url":"https://openreview.net/pdf?id=HJgExaVtwr"},{"title":"ICLR: DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://iclr.cc/virtual_2020/poster_HJgExaVtwr.html"},{"title":"[2002.07394] DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://arxiv.org/abs/2002.07394"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://papertalk.org/papertalks/3729"},{"title":"GitHub - LiJunnan1992/DivideMix: Code for paper: DivideMix: Learning with Noisy Labels as Semi-supervised Learning","url":"https://github.com/LiJunnan1992/DivideMix"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised ...","url":"https://arxiv.org/pdf/2002.07394"},{"title":"DivideMix: Learning with Noisy Labels as Semi-supervised Learning | Request PDF","url":"https://www.researchgate.net/publication/339350598_DivideMix_Learning_with_Noisy_Labels_as_Semi-supervised_Learning"}]

I've found comprehensive information about the DivideMix paper. Here are the key details:

## Overview

DivideMix is a novel framework for learning with noisy labels by leveraging semi-supervised learning techniques.

## Authors and Publication

The paper was authored by Junnan Li, Richard Socher, and Steven C.H. Hoi, and was published at ICLR 2020.

## Key Methodology

DivideMix models the per-sample loss distri
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:26:42.885605+00:00_

Web search results for query: "SALT Step-level Advantage Assignment Long-horizon Agents Trajectory Graph Li Jiazheng 2026"

Links: [{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.247/"},{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"SALT: Step-level advantage assignment for long-horizon agents via trajectory graph - Amazon Science","url":"https://www.amazon.science/publications/salt-step-level-advantage-assignment-for-long-horizon-agents-via-trajectory-graph"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph | Request PDF","url":"https://www.researchgate.net/publication/403067374_SALT_Step-level_Advantage_Assignment_for_Long-horizon_Agents_via_Trajectory_Graph"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/html/2510.20022v1"},{"title":"Step-level Advantage Assignment for Long-horizon Agents ...","url":"https://aclanthology.org/2026.findings-eacl.247.pdf"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://chatpaper.com/chatpaper/paper/202952"},{"title":"Jiazheng Li","url":"https://lijiazheng0917.github.io/"},{"title":"[Literature Review] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://www.themoonlight.io/en/review/salt-step-level-advantage-assignment-for-long-horizon-agents-via-trajectory-graph"}]

I found comprehensive information about this paper. Here are the search results:

## SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph

SALT is a paper by Jiazheng Li, Yawei Wang, Qiaojing Yan, Yijun Tian, Zhichao Xu, Huan Song, Panpan Xu, and Lin Lee Cheong, published in the Findings of EACL 20
…[truncated 1345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:26:42.885787+00:00_

Web search results for query: "Confident Learning Estimating Uncertainty Dataset Labels Northcutt Jiang Chuang JAIR 2021"

Links: [{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels | Journal of Artificial Intelligence Research","url":"https://jair.org/index.php/jair/article/view/12125"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels | Request PDF","url":"https://www.researchgate.net/publication/350909446_Confident_Learning_Estimating_Uncertainty_in_Dataset_Labels"},{"title":"[1911.00068] Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://arxiv.org/abs/1911.00068"},{"title":"Confident Learning: : Estimating Uncertainty in Dataset Labels: Journal of Artificial Intelligence Research: Vol 70, No null","url":"https://dl.acm.org/doi/10.1613/jair.1.12125"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://www.jair.org/index.php/jair/article/download/12125/26676/26691"},{"title":"dblp: Confident Learning: Estimating Uncertainty in Dataset Labels.","url":"https://dblp.org/rec/journals/jair/NorthcuttJC21.html"},{"title":"An Introduction to Confident Learning: Finding and Learning with Label Errors in Datasets","url":"https://l7.curtisnorthcutt.com/confident-learning"},{"title":"[PDF] Confident Learning: Estimating Uncertainty in Dataset Labels | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confident-Learning:-Estimating-Uncertainty-in-Northcutt-Jiang/cbaaa1154c491f9da2f050d3c22970e15bb7b52b"},{"title":"Estimating Uncertainty in Dataset Labels","url":"https://dspace.mit.edu/bitstream/handle/1721.1/142946/12125-Article%20(PDF)-26691-1-10-20210414.pdf?sequence=2&isAllowed=y"}]

I found the paper you're looking for. Here are the key details:

The paper "Confident Learning: Estimating Uncertainty in Dataset Labels" was published in April 2021 in the Journal of Artificial Intelligence Research by Curtis Northcutt (Massachusetts Institute of Technology), Lu J
…[truncated 1055 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:26:42.885955+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 102 · 2026-05-26T10:26:42.886175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-26T10:26:42.886355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Switch Transformers Scaling to Trillion Parameter Models Simple Efficient Sparsity Fedus Zoph Shazeer JMLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Switch Transformers Scaling to Trillion Parameter Models Simple Efficient Sparsity Fedus Zoph Shazeer JMLR 2022"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:26:42.886508+00:00_

Web search results for query: "Switch Transformers Scaling to Trillion Parameter Models Simple Efficient Sparsity Fedus Zoph Shazeer JMLR 2022"

Links: [{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"[PDF] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Switch-Transformers:-Scaling-to-Trillion-Parameter-Fedus-Zoph/fdacf2a732f55befdc410ea927091cad3b791f13"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://jmlr.org/papers/volume23/21-0998/21-0998.pdf"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/papers/v23/21-0998.html"},{"title":"Journal of Machine Learning Research 23 (2022) 1-40","url":"https://arxiv.org/pdf/2101.03961"},{"title":"Paper page - Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://huggingface.co/papers/2101.03961"},{"title":"Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity","url":"https://alastairreid.github.io/RelatedWork/papers/fedus:arxiv:2021/"},{"title":"[2101.03961v3] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961v3"}]

Great! I found the research paper you're looking for. Here are the details:

## Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**Authors:** William Fedus, Barret Zoph, Noam Shazeer

**Publication:** Journal of Machine Learning Research
…[truncated 1070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:26:42.886689+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

````json
{
  "description": "Verify bib entries batch 8",
  "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n62. bonagiri2025check\nTitle: Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\nAuthors: Bonagiri, Vamshi Krishna and Nguyen, Khanh and Plaut, Benjamin and Kumaraguru, Ponnurangam\nJournal: arXiv:2510.16492\nYear: 2025\n\n63. manakul2023selfcheckgpt\nTitle: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\nAuthors: Potsawee Manakul and Adian Liusie and Mark J. F. Gales\nVenue: EMNLP 2023\nYear: 2023\n\n64. kadavath2022language\nTitle: Language Models (Mostly) Know What They Know\nAuthors: Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Geesaman and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan\nJournal: arXiv:2207.05221\nYear: 2022\n\n65. xin2020deebert\nTitle: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\nAuthors: Ji Xin and Raphael Tang and Jaejun Lee and Yaoliang Yu and Jimmy Lin\nVenue: ACL 2020\nYear: 2020\n\n66. zhou2020bert\nTitle: BERT Loses Patience: Fast and Robust Inference with Early Exit\nAuthors: Wangchunshu Zhou and Canwen Xu and Tao Ge and Julian McAuley and Ke Xu and Furu Wei\nVenue: NeurIPS 2020, vol 33\nYear: 2020\n\n67. chow2015risk\nTitle: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\nAuthors: Yinlam Chow and Aviv Tamar and Shie Mannor and Marco Pavone\nVenue: NeurIPS 2015, vol 28\nYear: 2015\n\n68. tamar2015optimizing\nTitle: Optimizing the CVaR via Sampling\nAuthors: Aviv Tamar and Yonatan Glassner and Shie Mannor\nVenue: AAAI 2015\nYear: 2015\n\nSearch for each paper title individually and report findings."
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries batch 8",
    "prompt": "You are verifying academic paper references for correctness. For each entry below, use WebSearch to search for the paper title and verify: (1) the paper exists, (2) authors are correct, (3) year is correct, (4) title is accurate, (5) venue is correct, (6) arXiv ID if present is correct.\n\nIMPORTANT: It is currently May 2026. Papers dated 2025-2026 are real and expected.\n\nFor each entry, report in this exact format:\n```\n### N. [cite_key] — Title\n- 真实性：✓/✗\n- 作者：✓/✗ (detail if wrong)\n- 年份：✓/✗ (detail if wrong)\n- 标题：✓/✗ (detail if wrong)\n- Venue：✓/✗ (detail if wrong)\n- ID：✓/✗/N/A (detail if wrong)\n```\n\nHere are entries to verify:\n\n62. bonagiri2025check\nTitle: Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\nAuthors: Bonagiri, Vamshi Krishna and Nguyen, Khanh and Plaut, Benjamin and Kumaraguru, Ponnurangam\nJournal: arXiv:2510.16492\nYear: 2025\n\n63. manakul2023selfcheckgpt\nTitle: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\nAuthors: Potsawee Manakul and Adian Liusie and Mark J. F. Gales\nVenue: EMNLP 2023\nYear: 2023\n\n64. kadavath2022language\nTitle: Language Models (Mostly) Know What They Know\nAuthors: Saurav Kadavath and Tom Conerly and Amanda Askell and Tom Henighan and Dawn Drain and Ethan Perez and Nicholas Schiefer and Zac Hatfield-Dodds and Nova DasSarma and Eli Tran-Geesaman and Scott Johnston and Sheer El-Showk and Andy Jones and Nelson Elhage and Tristan Hume and Anna Chen and Yuntao Bai and Sam Bowman and Stanislav Fort and Deep Ganguli and Danny Hernandez and Josh Jacobson and Jackson Kernion and Shauna Kravec and Liane Lovitt and Kamal Ndousse and Catherine Olsson and Sam Ringer and Dario Amodei and Tom Brown and Jack Clark and Nicholas Joseph and Ben Mann and Sam McCandlish and Chris Olah and Jared Kaplan\nJournal: arXiv:2207.05221\nYear: 2022\n\n65. xin2020deebert\nTitle: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\nAuthors: Ji Xin and Raphael Tang and Jaejun Lee and Yaoliang Yu and Jimmy Lin\nVenue: ACL 2020\nYear: 2020\n\n66. zhou2020bert\nTitle: BERT Loses Patience: Fast and Robust Inference with Early Exit\nAuthors: Wangchunshu Zhou and Canwen Xu and Tao Ge and Julian McAuley and Ke Xu and Furu Wei\nVenue: NeurIPS 2020, vol 33\nYear: 2020\n\n67. chow2015risk\nTitle: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\nAuthors: Yinlam Chow and Aviv Tamar and Shie Mannor and Marco Pavone\nVenue: NeurIPS 2015, vol 28\nYear: 2015\n\n68. tamar2015optimizing\nTitle: Optimizing the CVaR via Sampling\nAuthors: Aviv Tamar and Yonatan Glassner and Shie Mannor\nVenue: AAAI 2015\nYear: 2015\n\nSearch for each paper title individually and report findings."
  }
}
````

</details>

---

### Tool result

_source line 106 · 2026-05-26T10:26:42.886913+00:00_

Web search results for query: "Mihatsch Neuneier "Risk-Sensitive Reinforcement Learning" Machine Learning 2002"

Links: [{"title":"Risk-Sensitive Reinforcement Learning | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1023/A:1017940631555"},{"title":"Risk-Sensitive Reinforcement Learning Applied to Control ...","url":"https://arxiv.org/pdf/1109.2147"},{"title":"Risk-Sensitive Reinforcement Learning","url":"https://www.researchgate.net/publication/225256871_Risk-Sensitive_Reinforcement_Learning"},{"title":"[PDF] Risk-Sensitive Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Risk-Sensitive-Reinforcement-Learning-Mihatsch-Neuneier/165f4a4bc8080093c89b8e9916b779aee8b37b81"},{"title":"Risk Sensitive Reinforcement Learning","url":"https://papers.nips.cc/paper/1583-risk-sensitive-reinforcement-learning"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Risk-sensitive+reinforcement+learning&amp=&author=O.+Mihatsch&amp=&author=R.+Neuneier&amp=&publication_year=2002&amp=&journal=Mach.+Learn.&amp=&pages=267-290&amp=&doi=10.1023/A:1017940631555"},{"title":"Risk-sensitive reinforcement learning | Proceedings of the First ACM International Conference on AI in Finance","url":"https://dl.acm.org/doi/10.1145/3383455.3422519"},{"title":"(PDF) Risk-Sensitive Reinforcement Learning","url":"https://www.researchgate.net/publication/261441730_Risk-Sensitive_Reinforcement_Learning"},{"title":"Risk-sensitive reinforcement learning applied to control under constraints | Journal of Artificial Intelligence Research","url":"https://dl.acm.org/doi/10.5555/1622519.1622522"},{"title":"Epistemic Risk-Sensitive Reinforcement Learning","url":"https://arxiv.org/pdf/1906.06273"}]

Based on the search results, I found the paper you're looking for:

**Mihatsch, O., Neuneier, R. "Risk-Sensitive Reinforcement Learning." Machine Learning 49, 267–290 (2002).**

The paper addresses how most reinforcem
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-26T10:26:42.887178+00:00_

Web search results for query: "Natarajan Dhillon Ravikumar Tewari "Learning with Noisy Labels" NeurIPS 2013"

Links: [{"title":"Learning with Noisy Labels Nagarajan Natarajan Inderjit S. Dhillon","url":"https://proceedings.neurips.cc/paper/5073-learning-with-noisy-labels.pdf"},{"title":"Learning with noisy labels | Request PDF","url":"https://www.researchgate.net/publication/285956588_Learning_with_noisy_labels"},{"title":"Learning with noisy labels | Proceedings of the 27th International Conference on Neural Information Processing Systems - Volume 1","url":"https://dl.acm.org/doi/10.5555/2999611.2999745"},{"title":"Learning with Noisy Labels | Center for Big Data Analytics","url":"https://bigdata.oden.utexas.edu/publication/learning-with-noisy-labels-2/"},{"title":"(PDF) Learning from Noisy Labels with Deep Neural Networks: A Survey","url":"https://www.researchgate.net/publication/343005449_Learning_from_Noisy_Labels_with_Deep_Neural_Networks_A_Survey"},{"title":"dblp: Learning with Noisy Labels.","url":"https://dblp.org/rec/conf/nips/NatarajanDRT13.html"},{"title":"Learning from Noisy Labels with No Change to the Training Process","url":"https://proceedings.mlr.press/v139/zhang21k/zhang21k.pdf"},{"title":"Learning with noisy labels — the Research Networking System","url":"https://researchers.dellmed.utexas.edu/en/publications/learning-with-noisy-labels"}]

Based on the search results, I found the paper you're looking for:

"Learning with Noisy Labels" by Nagarajan Natarajan, Inderjit S. Dhillon, Pradeep Ravikumar, and Ambuj Tewari was published in Neural Information Processing Systems (NIPS) in December 2013.

The paper theoretically studies the problem of binary classification in the presence of random classification noise where labels have independently been flipped with some small probability, and the random label noise is class-conditional—the flip probability depends on the class.

The paper is available in PDF format along with a poster and software, and the
…[truncated 155 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-26T10:26:42.887368+00:00_

Web search results for query: ""Budget-Aware Agentic Routing via Boundary-Guided Training" arXiv 2602.21227 Zhang 2026"

Links: [{"title":"[2602.21227] Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/abs/2602.21227"},{"title":"Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/html/2602.21227"},{"title":"Adaptive LLM Routing under Budget Constraints","url":"https://arxiv.org/html/2508.21141v1"},{"title":"Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation","url":"https://arxiv.org/html/2605.05657"},{"title":"xRouter: Training Cost-Aware LLMs Orchestration System via Reinforcement Learning","url":"https://arxiv.org/html/2510.08439v1"},{"title":"Learning Agent Routing From Early Experience","url":"https://arxiv.org/html/2605.07180"},{"title":"Budget-Aware Tool-Use Enables Effective Agent Scaling","url":"https://arxiv.org/html/2511.17006v1"}]

I found the paper! Here are the key details about "Budget-Aware Agentic Routing via Boundary-Guided Training":

**Paper Information:**
- **arXiv ID:** 2602.21227
- **Date:** February 4, 2026
- **Authors:** Caiqi Zhang, Menglin Xia, and others

**Main Contribution:**
The paper addresses the challenge that as large language models evolve into autonomous agents executing long-horizon workflows, invoking a high-capability model at every step becomes economically unsustainable.

**Key Problem:**
Agentic routing is a sequential, path-dependent problem where early mistakes compound, feedback is often at the end of the episode, and deployments often demand strict per-task spending limits.

**Proposed Solution:**
The authors propose Budget-Aware Agentic Routing, which selects between a cheap and an expensive model at each step to optimize the cost-success frontier and to operate under strict per-task budgets.

**Technical Approach:**
They propose Boundary-Guided Training, which leverages two boundary policies (always
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-26T10:26:42.887545+00:00_

Web search results for query: "Pearl Judea Causality Models Reasoning Inference Cambridge University Press 2nd edition 2009"

Links: [{"title":"Amazon.com: Causality: Models, Reasoning and Inference: 9780521895606: Pearl, Judea: Books","url":"https://www.amazon.com/Causality-Reasoning-Inference-Judea-Pearl/dp/052189560X"},{"title":"Causality : models, reasoning, and inference","url":"https://archive.illc.uva.nl/cil/uploaded_files/inlineitem/Pearl_2009_Causality.pdf"},{"title":"Judea Pearl, Causality: Models, Reasoning and Inference - PhilPapers","url":"https://philpapers.org/rec/PEACMR"},{"title":"Causality: Models, Reasoning and Inference (Hardcover) by Judea Pearl - Buy, Rent or Sell - BooksRun","url":"https://booksrun.com/9780521895606-causality-models-reasoning-and-inference-2nd-edition"},{"title":"Cambridge University Press 978-0-521-89560-6 — Causality Judea Pearl","url":"https://assets.cambridge.org/97805218/95606/frontmatter/9780521895606_frontmatter.pdf"},{"title":"CAUSALITY, 2nd Edition, 2009","url":"https://bayes.cs.ucla.edu/BOOK-2K/"},{"title":"Causality (book) - Wikipedia","url":"https://en.wikipedia.org/wiki/Causality_(book)"},{"title":"Causality: Models, Reasoning and Inference - Pearl, Judea: 9780521895606 - AbeBooks","url":"https://www.abebooks.com/9780521895606/Causality-Models-Reasoning-Inference-Pearl-052189560X/plp"},{"title":"Pearl, J. (2009) Causality Models, Reasoning and Inference. 2nd Edition, Cambridge University Press, Cambridge. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3432511"}]

I've found relevant information about this book. Here are the search results:

"Causality: Models, Reasoning and Inference" by Judea Pearl was published by Cambridge University Press in 2009. The ISBN-10 is 052189560X and ISBN-13 is 978-0521895606, and it is the 2nd edition.

This is an updated 2009 version of the original 2000 book. The first edition led to a paradigmatic change in how c
…[truncated 533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:26:42.887717+00:00_

Web search results for query: "Qwen2.5 technical report authors list Yang An Yang Baosong"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"dblp: Qwen2.5 Technical Report.","url":"https://dblp.org/rec/journals/corr/abs-2412-15115.html"},{"title":"Qwen2.5 Technical Report","url":"https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via   Self-Improvement","url":"https://arxiv.org/pdf/2409.12122"},{"title":"Qwen2.5-1M Technical Report","url":"https://arxiv.org/pdf/2501.15383"},{"title":"Qwen2.5-Coder Technical Report | Request PDF","url":"https://www.researchgate.net/publication/384115782_Qwen25-Coder_Technical_Report"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"}]

Based on the search results, I found information about the Qwen2.5 Technical Report authors list.

The Qwen2.5 Technical Report authors include: An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu (with additional authors not shown).

The report introduces Qwen2.5, a comprehensive series of large language models
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 7
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T10:26:42.887891+00:00_

Web search results for query: "Agent-SafetyBench Evaluating Safety LLM Agents Zhang Zhexin arXiv 2412.14470"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/387263688_Agent-SafetyBench_Evaluating_the_Safety_of_LLM_Agents"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"[2412.14470v2] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"http://arxiv.org/abs/2412.14470v2"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241214470Z/abstract"}]

I found comprehensive information about this paper. Here's what the search reveals:

## Overview

Agent-SafetyBench is a comprehensive benchmark designed to evaluate the safety of LLM agents. The paper was authored by Zhexin Zhang and 6 other authors.

## Key Details

Agent-SafetyBench encompasses 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 common failure modes frequently encountered in unsafe interactions.

## Motivation

As large language models are increasingly deployed as agents, their integration into interactive envir
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T10:26:42.888087+00:00_

Web search results for query: ""Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents" arXiv 2602.12662"

Links: [{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662v1"},{"title":"[2602.12662v1] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive"},{"title":"A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law","url":"https://arxiv.org/html/2505.02665v2"},{"title":"Fast, slow, and metacognitive thinking in AI | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-025-00027-5"},{"title":"DSADF: Thinking Fast and Slow for Decision Making","url":"https://arxiv.org/html/2505.08189v2"},{"title":"Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/html/2505.21097v1"},{"title":"Visual Agents as Fast and Slow Thinkers","url":"https://arxiv.org/html/2408.08862v1"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

## "Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents" (arXiv 2602.12662)

The paper introduces CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step.

### Problem Being Addressed

Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horiz
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:26:42.888275+00:00_

Web search results for query: ""Abstract Counterfactuals for Language Model Agents" Pona Kazemi arXiv 2506.02946"

Links: [{"title":"[2506.02946] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946"},{"title":"Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/html/2506.02946v1"},{"title":"[2506.02946v1] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946v1"},{"title":"Abstract Counterfactuals for Language Model Agents | OpenReview","url":"https://openreview.net/forum?id=ifMZw5fm7K"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=325&show=2000"},{"title":"Abstract Counterfactuals for Language Model Agents Edoardo Pona","url":"https://openreview.net/pdf/c39308d32f99302b4eb8a97c6d7eae5b2e2c4466.pdf"}]

I found the paper you're looking for. The paper "Abstract Counterfactuals for Language Model Agents" was submitted on June 3, 2025, and authored by Edoardo Pona, Milad Kazemi, Yali Du, David Watson, and Nicola Paoletti.

The paper addresses counterfactual inference for language model agents and introduces Abstract Counterfactuals, a framework that emphasizes high-level characteristics of actions and interactions within an environment, enabling counterfactual reasoning tailored to user-relevant features. 

The authors argue that existing work on counterfactuals in language models has primarily focused on token-level counterfactuals, which are inadequate for LM agents due to their open-ended action spaces. Unlike traditional agents with fixed action spaces, the actions of LM agents are often implicit in the strings they output, making their action spaces difficult to define and interpret.

The paper is available on arXiv at: https://arxiv.org/abs/2506.02946


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:26:42.888451+00:00_

Web search results for query: ""Verified Critical Step Optimization for LLM Agents" Li Mukai arXiv 2602.03412"

Links: [{"title":"[2602.03412] Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/abs/2602.03412"},{"title":"Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/html/2602.03412v2"},{"title":"Verified Critical Step Optimization for LLM Agents Mukai Li†,1,2","url":"https://arxiv.org/pdf/2602.03412"},{"title":"GitHub - kiaia/CSO: Verified Critical Step Optimization for LLM Agents(CSO) · GitHub","url":"https://github.com/kiaia/CSO"},{"title":"A Survey on the Optimization of Large Language Model-based Agents","url":"https://arxiv.org/html/2503.12434v2"},{"title":"[2602.10226] Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents","url":"https://arxiv.org/abs/2602.10226"},{"title":"STEP-LLM: Fine-Grained LLM Optimization","url":"https://www.emergentmind.com/topics/step-llm"},{"title":"Evolving Excellence: Automated Optimization of LLM-based Agents","url":"https://arxiv.org/html/2512.09108v1"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

**Paper Details:**
"Verified Critical Step Optimization for LLM Agents" proposes Critical Step Optimization (CSO), which focuses preference learning on verified critical steps, decision points where alternate actions demonstrably flip task outcomes from failure to success.

**Main Problem & Approach:**
The paper addresses fundamental challenges in post-training: outcome-only rewards fail to precisely attribute credit to intermediate steps, estimated step-level rewards introduce systematic noise, and Monte Carlo sampling approaches for step reward estimation incur prohibitive computational cost. 

Inspired by findings that only a small fraction of high-entropy tokens drive effective RL for reasoning, the researchers propose CSO, and the method starts from failed policy trajectories 
…[truncated 540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:26:42.888619+00:00_

Web search results for query: ""To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling" arXiv 2605.00737"

Links: [{"title":"[2605.00737] To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/abs/2605.00737"},{"title":"To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://arxiv.org/html/2605.00737v1"},{"title":"(PDF) To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling","url":"https://www.researchgate.net/publication/404397517_To_Call_or_Not_to_Call_A_Framework_to_Assess_and_Optimize_LLM_Tool_Calling"},{"title":"From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents","url":"https://arxiv.org/html/2605.15104"},{"title":"[2605.15104] From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents","url":"https://arxiv.org/abs/2605.15104"}]

I found the paper! Here's what I found about "To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling" (arXiv 2605.00737):

**Overview:**
The paper introduces a principled framework inspired by decision-making theory to evaluate web search tool-use decisions along three key factors: necessity, utility, and affordability.

**Problem Statement:**
Tool use is not always beneficial; some calls may be redundant or even harmful, and effective tool use hinges on a core LLM decision: whether to call or not call a tool, when performing a task. This decision is particularly challenging for web search tools, where the benefits of external information depend on the model's internal knowledge and its ability to integrate potentially noisy tool responses.

**Approach:**
The analysis combines two complementary lenses: a normative perspective that infers true need and utility from an optimal allocation of tool calls, and a descriptive perspective that infers the model's self-perceived need and utility from their observed b
…[truncated 283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:26:42.888798+00:00_

Web search results for query: "Rubin Donald Estimating Causal Effects Treatments Randomized Nonrandomized Studies Journal Educational Psychology 1974"

Links: [{"title":"ERIC - EJ118470 - Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies, Journal of Educational Psychology, 1974","url":"https://eric.ed.gov/?id=EJ118470"},{"title":"[PDF] Estimating causal effects of treatments in randomized and nonrandomized studies. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Estimating-causal-effects-of-treatments-in-and-Rubin/545122e2990590524459ec9b59ccac6ce71e3b6a"},{"title":"Estimating causal effects of treatments in randomized and nonrandomized studies. (1974) | Donald B. Rubin | 9804 Citations","url":"https://scispace.com/papers/estimating-causal-effects-of-treatments-in-randomized-and-48sipamxi0"},{"title":"Rubin, D.B. (1974) Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies. Journal of Educational Psychology, 66, 688-701. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4114686"},{"title":"Estimating causal effects of treatments in randomized and ...","url":"https://psycnet.apa.org/record/1975-06502-001"},{"title":"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies","url":"https://www.ets.org/research/policy_research_reports/publications/article/1974/hrbx.html"},{"title":"Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies","url":"https://dash.harvard.edu/entities/publication/73120378-82c0-6bd4-e053-0100007fdf3b"},{"title":"Rubin, D. (1974) Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies. Journal of Educational Psychology, 66, 688-701. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1362668"},{"title":"Rubin D.B., “Estimating Causal effects of treatments in randomized and non-r
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:26:42.888972+00:00_

Web search results for query: ""Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour" Gyevnár arXiv 2505.17801"

Links: [{"title":"[2505.17801] Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/abs/2505.17801"},{"title":"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/html/2505.17801"},{"title":"Integrating Counterfactual Simulations with Language Models","url":"https://arxiv.org/pdf/2505.17801"},{"title":"GitHub - gyevnarb/axis: Agentic Explanations via Interrogative Simulations · GitHub","url":"https://github.com/gyevnarb/axis"},{"title":"publications | Bálint Gyevnár","url":"https://gbalint.me/publications/"},{"title":"Towards Ethical Multi-Agent Systems of Large Language Models: A Mechanistic Interpretability Perspective","url":"https://www.researchgate.net/publication/398356965_Towards_Ethical_Multi-Agent_Systems_of_Large_Language_Models_A_Mechanistic_Interpretability_Perspective"},{"title":"[2505.13761] Simulation Agent: A Framework for Integrating Simulation and Large Language Models for Enhanced Decision-Making","url":"https://arxiv.org/abs/2505.13761"}]

I found the paper! Here are the key details:

## Paper Overview

The paper proposes AXIS (Agentic eXplanations via Interrogative Simulation), which leverages the counterfactual effect size model and LLMs to generate human-centred action explanations for multi-agent policies by having an LLM interrogate an environment simulator using prompts like 'whatif' and 'remove' to observe and synthesise counterfactual information over multiple rounds.

## Motivation

Autonomous multi-agent systems are useful for automating complex tasks but raise trust concerns due to risks such as miscoordination or goal misalignment. Explainability is vital for users' trust calibration, but explainable MAS face challenges due to complex environ
…[truncated 837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-26T10:26:42.889174+00:00_

Web search results for query: "Policy Invariance Under Reward Transformations Theory Application Reward Shaping Ng Russell ICML 1999"

Links: [{"title":"Publications policy invariance under reward transformations: theory and application to reward shaping","url":"https://www.cs.utexas.edu/~shivaram/readings/b2hd-NgHR1999.html"},{"title":"Policy Invariance Under Reward Transformations | Proceedings of the Sixteenth International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/645528.657613"},{"title":"(Open Access) Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (1999) | Andrew Y. Ng | 2376 Citations","url":"https://scispace.com/papers/policy-invariance-under-reward-transformations-theory-and-41w7bsjxkj"},{"title":"[PDF] Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Policy-Invariance-Under-Reward-Transformations:-and-Ng-Harada/94066dc12fe31e96af7557838159bde598cb4f10"},{"title":"(PDF) Policy Invariance under Reward Transformations for Multi-Objective Reinforcement Learning","url":"https://www.researchgate.net/publication/316839917_Policy_Invariance_under_Reward_Transformations_for_Multi-Objective_Reinforcement_Learning"},{"title":"dblp: Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping.","url":"https://dblp.org/rec/conf/icml/NgHR99.html"},{"title":"Policy Invariance Under Reward Transformations:","url":"https://pdfs.semanticscholar.org/154a/8731d1c4495a82b9a051ad52b0c269559c83.pdf"},{"title":"Improving the Effectiveness of Potential-Based Reward Shaping in Reinforcement Learning","url":"https://arxiv.org/html/2502.01307v1"}]

I found the paper you're looking for. Here are the key details:

"Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping" was authored by Andrew Y. Ng, Daishi Harada, and Stuart J. Russell and published in 
…[truncated 940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:26:42.889355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\" arXiv 2603.07915"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\" arXiv 2603.07915"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:26:42.889550+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GShard Scaling Giant Models Conditional Computation Automatic Sharding Lepikhin ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:26:42.889801+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 122 · 2026-05-26T10:26:42.890035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-26T10:26:42.890264+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\" Ross Gordon Bagnell AISTATS 2011 DAgger"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\" Ross Gordon Bagnell AISTATS 2011 DAgger"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:26:42.890487+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RouteLLM Learning to Route LLMs with Preference Data Ong Almahairi Wu Chiang arXiv 2406.18665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RouteLLM Learning to Route LLMs with Preference Data Ong Almahairi Wu Chiang arXiv 2406.18665"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-26T10:26:42.890700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SafeRoute arXiv 2502.12464 full author list Seanie Lee Dong Bok Lee"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SafeRoute arXiv 2502.12464 full author list Seanie Lee Dong Bok Lee"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:26:42.890909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.21227 full author list Budget-Aware Agentic Routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.21227 full author list Budget-Aware Agentic Routing"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-26T10:26:42.891149+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SALT step-level advantage assignment authors Qiaojing Yan EACL 2026 full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SALT step-level advantage assignment authors Qiaojing Yan EACL 2026 full author list"
  }
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-26T10:26:42.891364+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2506.02946 \"Abstract Counterfactuals\" year 2025 submission date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2506.02946 \"Abstract Counterfactuals\" year 2025 submission date"
  }
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-26T10:26:42.891574+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.03412 \"Verified Critical Step Optimization\" submission date February 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.03412 \"Verified Critical Step Optimization\" submission date February 2026"
  }
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-26T10:26:42.891789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-SafetyBench arXiv 2412.14470 full author list all authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-SafetyBench arXiv 2412.14470 full author list all authors"
  }
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-26T10:26:42.892016+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Confident Learning JAIR 2021 volume pages Northcutt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Confident Learning JAIR 2021 volume pages Northcutt"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:26:42.892252+00:00_

Web search results for query: "GShard Scaling Giant Models Conditional Computation Automatic Sharding Lepikhin ICLR 2021"

Links: [{"title":"ICLR Poster GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://iclr.cc/virtual/2021/poster/3196"},{"title":"dblp: GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding.","url":"https://dblp.org/rec/conf/iclr/LepikhinLXCFHKS21.html"},{"title":"GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | OpenReview","url":"https://openreview.net/forum?id=qrwe7XHTmYb"},{"title":"GShard: Scaling Giant Models With Conditional Computation and Automatic Sharding","url":"https://research.google/pubs/gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding/"},{"title":"GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding - researchr publication","url":"https://researchr.org/publication/LepikhinLXCFHKS21"},{"title":"Brief Review — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding-91393d98f7a4"},{"title":"[2006.16668] GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://arxiv.org/abs/2006.16668"},{"title":"Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, Zhifeng Chen · GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding","url":"https://slideslive.com/38953673/gshard-scaling-giant-models-with-conditional-computation-and-automatic-sharding"},{"title":"GSHARD: SCALING GIANT MODELS WITH CONDI","url":"https://openreview.net/pdf/cdb90e31da8446076492c5aef0c8c6ae35dd472a.pdf"}]

Based on the search results, here's what I found about GShard:

## Overview

GShard is a module composed o
…[truncated 1145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:26:42.892525+00:00_

Web search results for query: "RouteLLM Learning to Route LLMs with Preference Data Ong Almahairi Wu Chiang arXiv 2406.18665"

Links: [{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"Paper page - RouteLLM: Learning to Route LLMs with Preference Data","url":"https://huggingface.co/papers/2406.18665"},{"title":"[2406.18665v2] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v2"},{"title":"[2406.18665v3] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v3"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data Isaac Ong† UC Berkeley","url":"https://arxiv.org/pdf/2406.18665v3"},{"title":"Quick Read :: RouteLLM: Learning to Route LLMs with Preference Data | by QvickRead | Medium","url":"https://readqvick.medium.com/quick-read-routellm-learning-to-route-llms-with-preference-data-88a2b2e94f5e"},{"title":"[2406.18665v1] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v1"},{"title":"RouteLLM Paper – Shekhar Gulati","url":"https://shekhargulati.com/2024/07/09/routellm-paper/"}]

I found the paper you're looking for! Here's what I found:

**RouteLLM: Learning to Route LLMs with Preference Data** (arXiv:2406.18665)

The paper is authored by Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, and others.

**Overview:**

The paper proposes several efficient router models that dynamically select between a stronger and a weaker LLM during inference, aiming to optimize the balance between cost and response quality. The authors develop a training framework for these routers leveraging human preference data and data augmentation techniques to enhance performance.

**Key Results:**

Their evaluation on widely-recognized benchmarks shows that their approach significantly reduces costs—by over 2 times in certain cases—without co
…[truncated 456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:26:42.892791+00:00_

Web search results for query: "SafeRoute arXiv 2502.12464 full author list Seanie Lee Dong Bok Lee"

Links: [{"title":"[2502.12464] SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/abs/2502.12464"},{"title":"Paper page - SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://huggingface.co/papers/2502.12464"},{"title":"SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models","url":"https://arxiv.org/html/2502.12464"},{"title":"[1811.01147] SafeRoute: Learning to Navigate Streets Safely in an Urban Environment","url":"https://arxiv.org/abs/1811.01147"},{"title":"arXiv:2502.12464v2 [cs.CL] 19 May 2025","url":"https://arxiv.org/pdf/2502.12464"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=10650&show=2000"},{"title":"[2204.12464] Monochromatic paths in $2$-edge coloured graphs and hypergraphs","url":"https://arxiv.org/abs/2204.12464"}]

Based on the search results, the full author list for SafeRoute (arXiv:2502.12464) is: Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, and Sung Ju Hwang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:26:42.893028+00:00_

Web search results for query: "arXiv 2602.21227 full author list Budget-Aware Agentic Routing"

Links: [{"title":"[2602.21227] Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/abs/2602.21227"},{"title":"Budget-Aware Agentic Routing via Boundary-Guided Training","url":"https://arxiv.org/pdf/2602.21227"},{"title":"(PDF) Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory","url":"https://www.researchgate.net/publication/400506087_Learning_Query-Aware_Budget-Tier_Routing_for_Runtime_Agent_Memory"},{"title":"Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory","url":"https://viktoraxelsen.github.io/BudgetMem/"},{"title":"[2602.06025] Learning Query-Aware Budget-Tier Routing for Runtime Agent Memory","url":"https://arxiv.org/abs/2602.06025"},{"title":"[2604.03527] Explainable Model Routing for Agentic Workflows","url":"https://arxiv.org/abs/2604.03527"},{"title":"Retrieval-Conditioned Topology Selection with Provable Budget Conservation for Multi-Agent Code Generation","url":"https://arxiv.org/html/2605.05657"},{"title":"[2602.11541v1] Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use","url":"https://arxiv.org/abs/2602.11541v1"}]

Based on the search results, the full author list for arXiv paper 2602.21227 "Budget-Aware Agentic Routing via Boundary-Guided Training" is: Caiqi Zhang, Menglin Xia, Xuchao Zhang, Daniel Madrigal, Ankur Mallick, Samuel Kessler, Victor Ruehle, and Saravan Rajmohan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:26:42.893274+00:00_

Web search results for query: "SALT step-level advantage assignment authors Qiaojing Yan EACL 2026 full author list"

Links: [{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.247/"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph | Request PDF","url":"https://www.researchgate.net/publication/403067374_SALT_Step-level_Advantage_Assignment_for_Long-horizon_Agents_via_Trajectory_Graph"},{"title":"Step-level Advantage Assignment for Long-horizon Agents ...","url":"https://aclanthology.org/2026.findings-eacl.247.pdf"},{"title":"[2510.20022] SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/abs/2510.20022"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon ...","url":"https://www.scilit.com/publications/5e65cea5439fc011c7af1690f6b2ec2a"},{"title":"SALT: Step-level advantage assignment for long-horizon agents via trajectory graph - Amazon Science","url":"https://www.amazon.science/publications/salt-step-level-advantage-assignment-for-long-horizon-agents-via-trajectory-graph"},{"title":"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph","url":"https://arxiv.org/html/2510.20022v1"},{"title":"Jiazheng Li","url":"https://lijiazheng0917.github.io/"}]

Based on the search results, here is the full author list for the paper "SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph" published at EACL 2026:

Jiazheng Li, Yawei Wang, Qiaojing Yan, Yijun Tian, Zhichao Xu, Huan Song, Panpan Xu, and Lin Lee Cheong.

Note: I notice there's a discrepancy in one source where "Qiaojing Yan" from the ACL Anthology citation appears as "David Yan" in the arXiv and other sources. The ACL Anthology official publication lists "Qiaojing Yan" as one of the authors.


REMINDER: You MUST include the sources above i
…[truncated 54 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-26T10:26:42.893541+00:00_

Web search results for query: "Agent-SafetyBench arXiv 2412.14470 full author list all authors"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"},{"title":"\"Agent-SafetyBench: Evaluating the Safety of LLM Agents\"","url":"https://www.rohan-paul.com/p/agent-safetybench-evaluating-the"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/387263688_Agent-SafetyBench_Evaluating_the_Safety_of_LLM_Agents"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"[2412.14470v2] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"http://arxiv.org/abs/2412.14470v2"},{"title":"RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments","url":"https://arxiv.org/html/2506.15253v1"}]

Based on the search results, the full author list for Agent-SafetyBench (arXiv 2412.14470) is: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, and Minlie Huang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-26T10:26:42.893812+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion Language Agents with Verbal Reinforcement Learning Shinn Cassano Gopinath Narasimhan Yao NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion Language Agents with Verbal Reinforcement Learning Shinn Cassano Gopinath Narasimhan Yao NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:26:42.894064+00:00_

Web search results for query: ""A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning" Ross Gordon Bagnell AISTATS 2011 DAgger"

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"},{"title":"[1011.0686] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://arxiv.org/abs/1011.0686"},{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.researchgate.net/publication/47646552_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No-RegretOnline_Learning"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) - HackMD","url":"https://hackmd.io/@XiNyAicATy2jGaBhGc2ZRg/r1a97tfCU"},{"title":"[PDF] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Reduction-of-Imitation-Learning-and-Structured-to-Ross-Gordon/79ab3c49903ec8cb339437ccf5cf998607fc313e"},{"title":"(PDF) A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.academia.edu/24009408/A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No_Regret_Online_Learning"},{"title":"A Reduction of Imitation Learning and Structure Prediction to","url":"https://www.cl.uni-heidelberg.de/courses/ws18/iml/dagger.pdf"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

**Authors:** Stephane Ross, Geoffrey Gordon, and Drew Bagnell

**Publication:** Proceedings of the fourteenth int
…[truncated 1112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T10:26:42.894321+00:00_

Web search results for query: ""Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" arXiv 2603.07915"

Links: [{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.10788"},{"title":"ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping","url":"https://arxiv.org/html/2510.08457v1"},{"title":"e1: Learning Adaptive Control of Reasoning Effort","url":"https://arxiv.org/html/2510.27042v1"},{"title":"[2511.10788] From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/abs/2511.10788"}]

Here are the search results for the paper "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" (arXiv 2603.07915):

## Overview

Ares is a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks. The paper was published on March 9, 2026, by authors Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, and Shiyu Chang.

## Problem Statement

Modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction.

## Key Approach

Ares employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history. To train this router, they develop a data generation pipeline that identifies the minimum reaso
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:26:42.894579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Safe Reinforcement Learning via Shielding Alshiekh Bloem Ehlers Könighofer Niekum Topcu AAAI 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Safe Reinforcement Learning via Shielding Alshiekh Bloem Ehlers Könighofer Niekum Topcu AAAI 2018"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T10:26:42.894798+00:00_

Web search results for query: "Confident Learning JAIR 2021 volume pages Northcutt"

Links: [{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels | Journal of Artificial Intelligence Research","url":"https://jair.org/index.php/jair/article/view/12125"},{"title":"Confident Learning for Machines and Humans by Curtis George Northcutt","url":"https://www.curtisnorthcutt.com/resources/pdf/northcutt-confident-learning-for-machines-and-humans.pdf"},{"title":"Confident Learning: : Estimating Uncertainty in Dataset Labels: Journal of Artificial Intelligence Research: Vol 70, No null","url":"https://dl.acm.org/doi/10.1613/jair.1.12125"},{"title":"Curtis G. Northcutt (MIT) Confident Learning for Machines and Humans","url":"https://www.curtisnorthcutt.com/resources/pdf/northcutt-mit-2021-phd-defense-slides.pdf"},{"title":"Estimating Uncertainty in Dataset Labels","url":"https://dspace.mit.edu/bitstream/handle/1721.1/142946/12125-Article%20(PDF)-26691-1-10-20210414.pdf?sequence=2&isAllowed=y"},{"title":"Confident Learning: Estimating Uncertainty in Dataset Labels","url":"https://www.jair.org/index.php/jair/article/download/12125/26676/26691"},{"title":"dblp: Confident Learning: Estimating Uncertainty in Dataset Labels.","url":"https://dblp.org/rec/journals/jair/NorthcuttJC21.html"},{"title":"[PDF] Confident Learning: Estimating Uncertainty in Dataset Labels | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confident-Learning:-Estimating-Uncertainty-in-Northcutt-Jiang/6482d8c757bce9b0d208d37d4b09e4805faae983"}]

Based on the search results, here is the publication information for the "Confident Learning" paper by Northcutt et al. in JAIR 2021:

Authors: Curtis G. Northcutt, Lu Jiang, and Isaac L. Chuang. Year: 2021. Title: "Confident Learning: Estimating Uncertainty in Dataset Labels." Journal: Journal of Artificial Intelligence Research, Volume 70.

Pages: 1373-1411 (2021)


REMINDER: You MUST include the sources above in your response to the use
…[truncated 28 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:26:42.895064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Check Yourself Before You Wreck Yourself Selectively Quitting Improves LLM Agent Safety arXiv 2510.16492"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Check Yourself Before You Wreck Yourself Selectively Quitting Improves LLM Agent Safety arXiv 2510.16492"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-26T10:26:42.895292+00:00_

Web search results for query: "arXiv 2506.02946 "Abstract Counterfactuals" year 2025 submission date"

Links: [{"title":"[2506.02946] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946"},{"title":"[2506.02946v1] Abstract Counterfactuals for Language Model Agents","url":"https://arxiv.org/abs/2506.02946v1"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=325&show=2000"},{"title":"[2309.04211] Counterfactual Explanations via Locally ... - arXiv","url":"https://arxiv.org/abs/2309.04211"},{"title":"arXiv:2506.05188v1 [cs.CL] 5 Jun 2025 Counterfactual reasoning:","url":"https://www.arxiv.org/pdf/2506.05188v1"},{"title":"[2401.13935] A New Paradigm for Counterfactual Reasoning in Fairness and Recourse","url":"https://arxiv.org/abs/2401.13935"}]

Based on the search results, here is the information about arXiv paper 2506.02946:

**Title:** Abstract Counterfactuals for Language Model Agents

**Authors:** Edoardo Pona, Milad Kazemi, Yali Du, David Watson, Nicola Paoletti

**Submission Date:** Submitted on 3 Jun 2025

**Abstract:** The paper introduces Abstract Counterfactuals, a framework that emphasises high-level characteristics of actions and interactions within an environment, enabling counterfactual reasoning tailored to user-relevant features. Counterfactual inference is a powerful tool for analysing and evaluating autonomous agents, but its application to language model (LM) agents remains challenging. Existing work on counterfactuals in LMs has primarily focused on token-level counterfactuals, which are often inadequate for LM agents due to their open-ended action spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:26:42.895551+00:00_

Web search results for query: "arXiv 2602.03412 "Verified Critical Step Optimization" submission date February 2026"

Links: [{"title":"[2602.03412] Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/abs/2602.03412"},{"title":"Verified Critical Step Optimization for LLM Agents Mukai Li†,1,2","url":"https://arxiv.org/pdf/2602.03412"},{"title":"Verified Critical Step Optimization for LLM Agents","url":"https://arxiv.org/html/2602.03412v1"},{"title":"GitHub - kiaia/CSO: Verified Critical Step Optimization for LLM Agents(CSO) · GitHub","url":"https://github.com/kiaia/CSO"},{"title":"[2602.04449] What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/abs/2602.04449"},{"title":"[2602.17726] Closing Africa's Early Warning Gap: AI Weather Forecasting for Disaster Prevention","url":"https://arxiv.org/abs/2602.17726"},{"title":"1 Introduction","url":"https://arxiv.org/html/2602.13620"},{"title":"Lookahead Path Likelihood Optimization for Diffusion LLMs","url":"https://arxiv.org/html/2602.03496v1"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=6225&show=100"},{"title":"Entropy per Domain-Wall Step and the Structure of Criticality in the 𝑞-State Potts Model","url":"https://arxiv.org/html/2602.00962"}]

Based on the search results, I found the paper you're looking for:

**arXiv:2602.03412** was submitted on **3 February 2026**. 

The paper is titled "Verified Critical Step Optimization for LLM Agents" with authors Mukai Li, Qingcheng Zeng, Tianqing Fang, Zhenwen Liang, Linfeng Song, Qi Liu, Haitao Mi, and Dong Yu.

The paper proposes Critical Step Optimization (CSO), which focuses preference learning on verified critical steps—decision points where alternate actions demonstrably flip task outcomes from failure to success. The method starts from failed policy trajectories rather than expert demonstrations, directly targeting the policy model's weaknesses.


REMINDER: You
…[truncated 87 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-26T10:26:42.895817+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\" arXiv Bae Sangmin 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\" arXiv Bae Sangmin 2025"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:26:42.896070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\" Hao Liu Wang Hu NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\" Hao Liu Wang Hu NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 148 · 2026-05-26T10:26:42.896325+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.17801 AXIS Gyevnar submission date May 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.17801 AXIS Gyevnar submission date May 2025"
  }
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-26T10:26:42.896541+00:00_

Web search results for query: "Reflexion Language Agents with Verbal Reinforcement Learning Shinn Cassano Gopinath Narasimhan Yao NeurIPS 2023"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf"},{"title":"Reflexion: language agents with verbal reinforcement learning | OpenReview","url":"https://openreview.net/forum?id=vAElhFcKW6"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"},{"title":"[Paper Note] Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, NeurIPS'23, 2023.03 · Issue #512 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/512"},{"title":"Reflexion: language agents with verbal reinforcement learning [Quick Review]","url":"https://liner.com/review/reflexion-language-agents-with-verbal-reinforcement-learning"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn, Federi
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-26T10:26:42.896794+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2412.14470 Agent-SafetyBench Zhang Zhexin Cui Shiyao Lu Yida Zhou Jingzhuo Yang Junhao Liu Jie Wang Renhao Li Jiangjie Huang Minlie authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2412.14470 Agent-SafetyBench Zhang Zhexin Cui Shiyao Lu Yida Zhou Jingzhuo Yang Junhao Liu Jie Wang Renhao Li Jiangjie Huang Minlie authors"
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T10:26:42.897064+00:00_

Web search results for query: "Safe Reinforcement Learning via Shielding Alshiekh Bloem Ehlers Könighofer Niekum Topcu AAAI 2018"

Links: [{"title":"Safe Reinforcement Learning via Shielding | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11797"},{"title":"Safe Reinforcement Learning via Shielding - AAAI","url":"https://aaai.org/papers/11797-safe-reinforcement-learning-via-shielding/"},{"title":"Safe Reinforcement Learning via Shielding - Graz University of Technology","url":"https://tugraz.elsevierpure.com/en/publications/safe-reinforcement-learning-via-shielding/"},{"title":"Safe reinforcement learning via shielding under partial observability | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i12.26723"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Alshiekh%2C+M.%2C+Bloem%2C+R.%2C+Ehlers%2C+R.%2C+K%C3%B6nighofer%2C+B.%2C+Niekum%2C+S.%2C+Topcu%2C+U.%3A+Safe+reinforcement+learning+via+shielding.+In%3A+Thirty-Second+AAAI+Conference+on+Artificial+Intelligence+%282018%29"},{"title":"[1708.08611] Safe Reinforcement Learning via Shielding","url":"https://arxiv.org/abs/1708.08611"},{"title":"Safe Reinforcement Learning Using Probabilistic Shields (Invited Paper)","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CONCUR.2020.3"},{"title":"Safe Reinforcement Learning Via Shielding - Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Königshofer, Scott Niekum, Ufuk Topcu - Google Books","url":"https://books.google.com/books/about/Safe_Reinforcement_Learning_Via_Shieldin.html?id=kY65uQEACAAJ"},{"title":"Safe reinforcement learning via shielding | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and T
…[truncated 1605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:26:42.897281+00:00_

Web search results for query: "Check Yourself Before You Wreck Yourself Selectively Quitting Improves LLM Agent Safety arXiv 2510.16492"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492v3"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"(PDF) Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://www.researchgate.net/publication/396714988_Check_Yourself_Before_You_Wreck_Yourself_Selectively_Quitting_Improves_LLM_Agent_Safety"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety | OpenReview","url":"https://openreview.net/forum?id=ALwpW0ygzI"},{"title":"NeurIPS Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://neurips.cc/virtual/2025/125248"},{"title":"Ponnurangam Kumaraguru “PK” on X: \"🎉 New paper accepted to the NeurIPS 2025 “Reliable ML from Unreliable Data” Workshop: “Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety.” 📜 Preprint: https://t.co/bMWbFiER02 https://t.co/vKVz2cmssG\" / X","url":"https://x.com/ponguru/status/1986649704671957348"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/?searchtype=author&query=Benjamin+Plaut"}]

I found the paper! Here are the key details about "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" (arXiv 2510.16492):

**Overview:**
As Large Language Model (LLM) agents increasingly operate in complex environments with real-world consequences, their safety becomes critical.

**Problem A
…[truncated 1152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-26T10:26:42.897524+00:00_

Here are the verification results for all 9 entries:

### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset
- 真实性：✓
- 作者：✓ (Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, Jacob Steinhardt — all confirmed)
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)
- ID：N/A

### 29. [qwen25-2024] — Qwen2.5 Technical Report
- 真实性：✓
- 作者：✓ (An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang et al. — confirmed)
- 年份：✓ (2024, submitted December 19, 2024)
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:2412.15115)

### 30. [llama3-2024] — The Llama 3 Herd of Models
- 真实性：✓
- 作者：✓ (Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri et al. — confirmed, 500+ co-authors)
- 年份：✓ (2024, submitted July 31, 2024)
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:2407.21783)

### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors
- 真实性：✓
- 作者：✓ (A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller — confirmed)
- 年份：✓ (2008)
- 标题：✓
- Venue：✓ (The Review of Economics and Statistics, vol 90, no 3, pp 414-427)
- ID：N/A

### 32. [achiam2017cpo] — Constrained Policy Optimization
- 真实性：✓
- 作者：✓ (Joshua Achiam, David Held, Aviv Tamar, Pieter Abbeel — confirmed)
- 年份：✓ (2017)
- 标题：✓
- Venue：✓ (ICML 2017, pp 22-31)
- ID：N/A

### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling
- 真实性：✓
- 作者：✗ (First author is **Weiwen Liu**, not "Weiwen Zhang" as stated in the bib entry. The full author list has 27 authors led by Weiwen Liu, Xu Huang, Xingshan Zeng, etc.)
- 年份：✓ (2025, ICLR 2025)
- 标题：✓
- Venue：✓ (ICLR 2025)
- ID：N/A

### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors
- 真实性：✓
- 作者：✓ (Matthew D. Webb — confirmed)
- 年份：✓ (2023)
- 标题：✓ (note: the published title uses a lowercase "wild" and an en-dash style: "Reworking wild bootstrap‐based inference for clus
…[truncated 891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T10:26:42.897723+00:00_

Web search results for query: ""ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings" Hao Liu Wang Hu NeurIPS 2023"

Links: [{"title":"GitHub - Ber666/ToolkenGPT: ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings - NeurIPS 2023 (oral)","url":"https://github.com/Ber666/ToolkenGPT"},{"title":"[2305.11554] ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://arxiv.org/abs/2305.11554"},{"title":"NeurIPS Poster ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://neurips.cc/virtual/2023/poster/72492"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://papers.nips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html"},{"title":"NeurIPS 2023 ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings Oral","url":"https://nips.cc/virtual/2023/oral/73868"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings | OpenReview","url":"https://openreview.net/forum?id=BHXsb69bSx"},{"title":"ToolkenGPT: Augmenting Frozen Language Models","url":"https://arxiv.org/pdf/2305.11554"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with ...","url":"https://openreview.net/pdf?id=BHXsb69bSx"},{"title":"Releases · Ber666/ToolkenGPT","url":"https://github.com/Ber666/ToolkenGPT/releases"}]

I found comprehensive information about ToolkenGPT. Here's what I discovered:

## Paper Overview

ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings was published at NeurIPS 2023 as an oral presentation, and it also received the Best Paper Award at SoCalNLP 2023.

## Key Concept

The key idea of ToolkenGPT is to represent each tool as a new token ("toolken") to augment the vocabulary, with each tool associated with an embedding inserted into the L
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-26T10:26:42.897907+00:00_

Web search results for query: "arxiv 2412.14470 Agent-SafetyBench Zhang Zhexin Cui Shiyao Lu Yida Zhou Jingzhuo Yang Junhao Liu Jie Wang Renhao Li Jiangjie Huang Minlie authors"

Links: [{"title":"[2412.14470] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://arxiv.org/abs/2412.14470"},{"title":"Paper page - Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"https://huggingface.co/papers/2412.14470"},{"title":"GitHub - thu-coai/Agent-SafetyBench · GitHub","url":"https://github.com/thu-coai/Agent-SafetyBench"},{"title":"[PDF] Agent-SafetyBench: Evaluating the Safety of LLM Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Agent-SafetyBench:-Evaluating-the-Safety-of-LLM-Zhang-Cui/7d11400eeb317ebee278f49e108226a4f8555dda"},{"title":"AGENT-SAFETYBENCH: Evaluating the Safety of LLM Agents","url":"https://www.arxiv.org/pdf/2412.14470v1"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/papers/2412.14470"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents | Request PDF","url":"https://www.researchgate.net/publication/387263688_Agent-SafetyBench_Evaluating_the_Safety_of_LLM_Agents"},{"title":"[2412.14470v2] Agent-SafetyBench: Evaluating the Safety of LLM Agents","url":"http://arxiv.org/abs/2412.14470v2"},{"title":"\"Agent-SafetyBench: Evaluating the Safety of LLM Agents\"","url":"https://www.rohan-paul.com/p/agent-safetybench-evaluating-the"},{"title":"Agent-SafetyBench: Evaluating the Safety of LLM Agents - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241214470Z/abstract"}]

I found the paper arxiv 2412.14470 "Agent-SafetyBench: Evaluating the Safety of LLM Agents". 

The authors are: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, and Minlie Huang.

Note: Your search query listed slightly different author names than what appears in the paper (for example, you listed "Junhao Yang" while the paper lists "Junxiao Yang"). 
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T10:26:42.898145+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Learning the Difference that Makes a Difference Counterfactually-Augmented Data Kaushik Hovy Lipton ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Learning the Difference that Makes a Difference Counterfactually-Augmented Data Kaushik Hovy Lipton ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-26T10:26:42.898305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Generative Large Language Models Manakul EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Generative Large Language Models Manakul EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T10:26:42.898455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tool Learning with Large Language Models A Survey Qu Dai Wei Cai Wang Yin Xu Wen arXiv 2405.17935"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tool Learning with Large Language Models A Survey Qu Dai Wei Cai Wang Yin Xu Wen arXiv 2405.17935"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T10:26:42.898605+00:00_

Web search results for query: ""Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation" arXiv Bae Sangmin 2025"

Links: [{"title":"[2507.10524] Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/abs/2507.10524"},{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | OpenReview","url":"https://openreview.net/forum?id=QuqsEIVWIG"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiviq.substack.com/p/mixture-of-recursions-learning-dynamic"},{"title":"(PDF) Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://www.researchgate.net/publication/393684588_Mixture-of-Recursions_Learning_Dynamic_Recursive_Depths_for_Adaptive_Token-Level_Computation"},{"title":"Paper page - Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://huggingface.co/papers/2507.10524"},{"title":"ICML Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Thinking","url":"https://icml.cc/virtual/2025/51797"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/html/2507.10524v1"},{"title":"Learning Dynamic Recursive Depths for Adaptive Token- ...","url":"https://arxiv.org/pdf/2507.10524"}]

I found the paper! Here's what I can tell you about it:

The paper "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation" is authored by Sangmin Bae and 10 other authors, with the arXiv identifier 2507.1052
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-26T10:26:42.898780+00:00_

Web search results for query: "arxiv 2505.17801 AXIS Gyevnar submission date May 2025"

Links: [{"title":"[2505.17801] Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/abs/2505.17801"},{"title":"Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour","url":"https://arxiv.org/html/2505.17801"},{"title":"Computer Science May 2025","url":"http://arxiv.org/list/cs/2025-05?skip=8875&show=25"},{"title":"Bálint Gyevnár","url":"https://gbalint.me/"},{"title":"Machine Learning","url":"https://www.arxiv.org/list/cs.LG/recent?skip=501&show=500"},{"title":"[2504.17801] Evolution of Optimization Algorithms for Global Placement via Large Language Models","url":"https://arxiv.org/abs/2504.17801"},{"title":"[2603.14495] Bridging the Gap in the Responsible AI Divides","url":"https://arxiv.org/abs/2603.14495"}]

Based on the search results, I found information about arxiv:2505.17801:

The paper is titled "Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour" by Bálint Gyevnár, Christopher G. Lucas, Stefano V. Albrecht, and Shay B. Cohen.

The paper proposes AXIS (Agentic eXplanations via Interrogative Simulation). AXIS generates human-centred action explanations for multi-agent policies by having an LLM interrogate an environment simulator using prompts like 'whatif' and 'remove' to observe and synthesise counterfactual information over multiple rounds.

The researchers evaluate AXIS on autonomous driving across ten scenarios for five LLMs with a comprehensive methodology combining robustness, subjective preference, correctness, and goal/action prediction with an external LLM as evaluator.

Based on the arxiv identifier "2505.17801", this corresponds to a May 2025 submission, as the first four digits indicate the submission date (25 = 2025, 05 = May).


REMINDER: You MUST include the sources above in your response to the user 
…[truncated 26 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:26:42.898960+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\" Shridhar Yuan Côté Bisk Trischler Hausknecht ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\" Shridhar Yuan Côté Bisk Trischler Hausknecht ICLR 2021"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T10:26:42.899140+00:00_

Web search results for query: "Tool Learning with Large Language Models A Survey Qu Dai Wei Cai Wang Yin Xu Wen arXiv 2405.17935"

Links: [{"title":"[2405.17935] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935"},{"title":"Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/html/2405.17935v1"},{"title":"[2405.17935v3] Tool Learning with Large Language Models: A Survey","url":"https://arxiv.org/abs/2405.17935v3"},{"title":"(PDF) Tool Learning with Large Language Models: A Survey","url":"https://www.researchgate.net/publication/380935103_Tool_Learning_with_Large_Language_Models_A_Survey"},{"title":"Paper page - Tool Learning with Large Language Models: A Survey","url":"https://huggingface.co/papers/2405.17935"},{"title":"[PDF] Tool Learning with Large Language Models: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tool-Learning-with-Large-Language-Models:-A-Survey-Qu-Dai/0479547a69ffa48fe106137eba8358a9d8a2cc48"},{"title":"Tool Learning with Large Language Models: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240517935Q/abstract"},{"title":"From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions","url":"https://arxiv.org/html/2410.08197v2"},{"title":"Tool Learning with Large Language Models: A Survey | PromptLayer","url":"https://www.promptlayer.com/research-papers/tool-learning-with-large-language-models-a-survey"},{"title":"Tool learning with large language models: a survey - ScienceGuardians","url":"https://scienceguardians.com/topic/tool-learning-with-large-language-models-a-survey/"}]

I found the paper! Here are the search results for the paper you requested:

## Paper Information

**Title:** Tool Learning with Large Language Models: A Survey

**Authors:** Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, Ji-Rong Wen

**arXiv ID:** 2405.17935

**Publication Date:** 28 May 2024

## Ov
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T10:26:42.899311+00:00_

Web search results for query: ""ALFWorld: Aligning Text and Embodied Environments for Interactive Learning" Shridhar Yuan Côté Bisk Trischler Hausknecht ICLR 2021"

Links: [{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"ICLR Poster ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://iclr.cc/virtual/2021/poster/2973"},{"title":"[PDF] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ALFWorld:-Aligning-Text-and-Embodied-Environments-Shridhar-Yuan/398a0625e8707a0b41ac58eaec51e8feb87dd7cb"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning | OpenReview","url":"https://openreview.net/forum?id=0IOX0YcCdTn"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://papertalk.org/papertalks/28910"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"alfworld - Overview","url":"https://github.com/alfworld/"},{"title":"ALFWorld: Aligning Text and Embodied Environments for Interactive Learning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/alfworld-aligning-text-and-embodied-environments-for-interactive-learning/"},{"title":"(PDF) ALFWorld: Aligning Text and Embodied Environments for Interactive Learning","url":"https://www.researchgate.net/publication/344551961_ALFWorld_Aligning_Text_and_Embodied_Environments_for_Interactive_Learning"}]

I found extensive information about this paper. Here's what I discovered:

## Paper Overview

The paper "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning" was published at ICLR 2021 by authors Mohit Shridhar, Xingdi Yuan, Marc-Alexand
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-26T10:26:42.899488+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.12662 CogRouter authors Yang Ruihan Ye Fanghua"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.12662 CogRouter authors Yang Ruihan Ye Fanghua"
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-26T10:26:42.899639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Tree of Thoughts Deliberate Problem Solving with Large Language Models Yao Yu Zhao Shafran Griffiths Cao Narasimhan NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Tree of Thoughts Deliberate Problem Solving with Large Language Models Yao Yu Zhao Shafran Griffiths Cao Narasimhan NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-26T10:26:42.899792+00:00_

Web search results for query: "Learning the Difference that Makes a Difference Counterfactually-Augmented Data Kaushik Hovy Lipton ICLR 2020"

Links: [{"title":"[1909.12434] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://arxiv.org/abs/1909.12434"},{"title":"ICLR: Learning The Difference That Makes A Difference With Counterfactually-Augmented Data","url":"https://iclr.cc/virtual_2020/poster_Sklgs0NFvr.html"},{"title":"Learning The Difference That Makes A Difference With Counterfactually-Augmented Data | OpenReview","url":"https://openreview.net/forum?id=Sklgs0NFvr"},{"title":"GitHub - acmi-lab/counterfactually-augmented-data: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data · GitHub","url":"https://github.com/acmi-lab/counterfactually-augmented-data"},{"title":"Papers with Code - Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://paperswithcode.com/paper/learning-the-difference-that-makes-a"},{"title":"[PDF] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Learning-the-Difference-that-Makes-a-Difference-Kaushik-Hovy/47f1eb0dc42189ba7cf21b76598c8217eb1b6e05"},{"title":"ICLR Poster Learning The Difference That Makes A Difference With Counterfactually-Augmented Data","url":"https://iclr.cc/virtual/2020/poster/1891"},{"title":"Learning the Difference that Makes a Difference with Counterfactually-Augmented Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190912434K/abstract"},{"title":"[1909.12434v1] Learning the Difference that Makes a Difference with Counterfactually-Augmented Data","url":"https://arxiv.org/abs/1909.12434v1"},{"title":"Learning the difference that makes a differ","url":"https://openreview.net/pdf?id=Sklgs0NFvr"}]

Great! I found the paper. Here's what the search reveals:

This paper is by Divyansh Kaushi
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-26T10:26:42.899967+00:00_

Web search results for query: "SelfCheckGPT Zero-Resource Black-Box Hallucination Detection Generative Large Language Models Manakul EMNLP 2023"

Links: [{"title":"SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.557/"},{"title":"[2303.08896] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://arxiv.org/abs/2303.08896"},{"title":"GitHub - potsawee/selfcheckgpt: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models · GitHub","url":"https://github.com/potsawee/selfcheckgpt"},{"title":"(PDF) SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://www.researchgate.net/publication/376402462_SelfCheckGPT_Zero-Resource_Black-Box_Hallucination_Detection_for_Generative_Large_Language_Models"},{"title":"Paper page - SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://huggingface.co/papers/2303.08896"},{"title":"[PDF] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelfCheckGPT:-Zero-Resource-Black-Box-Hallucination-Manakul-Liusie/7c1707db9aafd209aa93db3251e7ebd593d55876"},{"title":"EMNLP2023: SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://virtual2023.emnlp.org/paper_349.html"},{"title":"[Quick Review] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models","url":"https://liner.com/review/selfcheckgpt-zeroresource-blackbox-hallucination-detection-for-generative-large-language-models"}]

Based on the search results, here's information about the SelfCheckGPT paper:

## Overview
SelfCheckGPT is a simple sampling-based
…[truncated 1546 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T10:26:42.900172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"A Comprehensive Survey on Safe Reinforcement Learning\" García Fernández JMLR 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"A Comprehensive Survey on Safe Reinforcement Learning\" García Fernández JMLR 2015"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-26T10:26:42.900349+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Language Models Mostly Know What They Know Kadavath arXiv 2207.05221"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Language Models Mostly Know What They Know Kadavath arXiv 2207.05221"
  }
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T10:26:42.900496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "FrugalGPT How to Use Large Language Models Reducing Cost Improving Performance Chen Zaharia Zou arXiv 2305.05176"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "FrugalGPT How to Use Large Language Models Reducing Cost Improving Performance Chen Zaharia Zou arXiv 2305.05176"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-26T10:26:42.900644+00:00_

Web search results for query: "Tree of Thoughts Deliberate Problem Solving with Large Language Models Yao Yu Zhao Shafran Griffiths Cao Narasimhan NeurIPS 2023"

Links: [{"title":"GitHub - princeton-nlp/tree-of-thought-llm: [NeurIPS 2023] Tree of Thoughts: Deliberate Problem Solving with Large Language Models · GitHub","url":"https://github.com/princeton-nlp/tree-of-thought-llm"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models | OpenReview","url":"https://openreview.net/forum?id=5Xc1ecxO1h"},{"title":"[2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://arxiv.org/abs/2305.10601"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html"},{"title":"NeurIPS Poster Tree of Thoughts: Deliberate Problem Solving with Large Language Models","url":"https://neurips.cc/virtual/2023/poster/72797"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models - Princeton University","url":"https://collaborate.princeton.edu/en/publications/tree-of-thoughts-deliberate-problem-solving-with-large-language-m-2/"},{"title":"NeurIPS 2023 Tree of Thoughts: Deliberate Problem Solving with Large Language Models Oral","url":"https://neurips.cc/virtual/2023/oral/73874"},{"title":"Tree of Thoughts: Deliberate Problem Solving with Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10542045-tree-thoughts-deliberate-problem-solving-large-language-models"},{"title":"Tree of Thoughts: A New Way to Unlock Problem-Solving in Large Language Models | by Research Graph | Medium","url":"https://medium.com/@researchgraph/tree-of-thoughts-a-new-way-to-unlock-problem-solving-in-large-language-models-cd50189e59a1"}]

I found information about the paper you're looking for. Here are the key details:

**Paper Title:** Tree of Though
…[truncated 1272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-26T10:26:42.900818+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentBench Evaluating LLMs as Agents Liu Yu Zhang Xu Lei Lai ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentBench Evaluating LLMs as Agents Liu Yu Zhang Xu Lei Lai ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T10:26:42.900971+00:00_

Web search results for query: "arxiv 2602.12662 CogRouter authors Yang Ruihan Ye Fanghua"

Links: [{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=694&show=1000"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/pastweek?skip=11&show=1000"},{"title":"Ruihan Yang - Google 学术搜索","url":"https://scholar.google.com/citations?user=b-o1o7cAAAAJ&hl=zh-CN"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/eess?searchtype=author&query=Yang,+R"},{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=2025&show=1000"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=2025-10-23"},{"title":"Computer Vision and Pattern Recognition","url":"https://web3.arxiv.org/list/cs.CV/recent?skip=145&show=500"}]

Based on the search results, I found the arXiv paper you're looking for:

**Paper:** Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents

**arXiv ID:** 2602.12662

**Authors:** Ruihan Yang, Fanghua Ye, Xiang Wei, Ruoqing Zhao, Kang Luo, Xinbo Xu, Bo Zhao, Ruotian Ma, Shanyi Wang, Zhaopeng Tu, Xiaolong Li, Deqing Yang, and Linus

**Affiliations:** Fudan University and Tencent Hunyuan

**Main Contribution:** CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step

**Key Technical Details:** The framework is grounded in ACT-R theory with four hierarchical cognitive levels, and employs a two-stage training approach including Cognition-aware Supervised Fine
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T10:26:42.901164+00:00_

Web search results for query: ""A Comprehensive Survey on Safe Reinforcement Learning" García Fernández JMLR 2015"

Links: [{"title":"[PDF] A comprehensive survey on safe reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-comprehensive-survey-on-safe-reinforcement-Garc%C3%ADa-Fern%C3%A1ndez/c0f2c4104ef6e36bb67022001179887e6600d24d"},{"title":"(PDF) A comprehensive survey on safe reinforcement learning (2015) | Javier García | 1705 Citations","url":"https://scispace.com/papers/a-comprehensive-survey-on-safe-reinforcement-learning-3p8tg32zci"},{"title":"A comprehensive survey on safe reinforcement learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/2789272.2886795"},{"title":"A comprehensive survey on safe reinforcement learning","url":"https://bibbase.org/network/publication/garcia-fernndez-acomprehensivesurveyonsafereinforcementlearning-2015"},{"title":"A comprehensive survey on safe reinforcement learning","url":"https://www.researchgate.net/publication/301361203_A_comprehensive_survey_on_safe_reinforcement_learning"},{"title":"dblp: A comprehensive survey on safe reinforcement learning.","url":"https://dblp.org/rec/journals/jmlr/GarciaF15.html"},{"title":"A Comprehensive Survey on Safe Reinforcement Learning","url":"https://researchportal.uc3m.es/display/act443125"}]

I found the paper you're looking for! Here are the key details:

"A Comprehensive Survey on Safe Reinforcement Learning" by Javier García and Fernando Fernández was published in the Journal of Machine Learning Research, volume 16, pages 1437-1480 in 2015.

Safe Reinforcement Learning is defined as the process of learning policies that maximize the expectation of the return in problems in which it is important to ensure reasonable system performance and/or respect safety constraints during the learning and/or deployment processes.

The survey categorizes and analyzes two approaches of Safe Reinforcement Learning: the first i
…[truncated 529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:26:42.901339+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-26T10:26:42.901548+00:00_

Now I have enough information to compile the full verification report.

### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph
- 真实性：✓
- 作者：✗ — "David Yan" should be "Qiaojing Yan" per ACL Anthology. All other authors match.
- 年份：✓ (2026)
- 标题：✓
- Venue：✓ (Findings of EACL 2026)
- ID：N/A

### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size
- 真实性：✓
- 作者：✓ (Gemma Team, Google DeepMind)
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:2408.00118)

### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels
- 真实性：✓
- 作者：✓ (Curtis Northcutt, Lu Jiang, Isaac Chuang)
- 年份：✓ (2021)
- 标题：✓
- Venue：✓ (JAIR, vol 70, pp 1373-1411)
- ID：N/A

### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning
- 真实性：✓
- 作者：✓ (Junnan Li, Richard Socher, Steven C.H. Hoi)
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ICLR 2020)
- ID：N/A

### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping
- 真实性：✓
- 作者：✓ (Andrew Y. Ng, Daishi Harada, Stuart Russell)
- 年份：✓ (1999)
- 标题：✓
- Venue：✓ (ICML 1999)
- ID：N/A

### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents
- 真实性：✓
- 作者：✗ — The bib entry lists 9 authors (Zhang, Cui, Lu, Zhou, Yang Junhao, Liu Jie, Wang Renhao, Li Jiangjie, Huang Minlie), but the actual paper has 7 authors: Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang (not "Junhao"), Hongning Wang (not "Renhao"), Minlie Huang. "Liu Jie" and "Li Jiangjie" do not appear as authors. "Yang Junhao" should be "Yang Junxiao". "Wang Renhao" should be "Wang Hongning".
- 年份：✓ (2024)
- 标题：✓
- Venue：✓ (arXiv preprint)
- ID：✓ (arXiv:2412.14470)

### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference
- 真实性：✓
- 作者：✓ (Judea Pearl)
- 年份：✓ (2009, 2nd edition)
- 标题：✓
- Venue：✓ (Cambridge University Press, 2nd edition)
- ID：N/A

### 5
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-26T10:26:42.901734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.23530 MTRouter authors Zhang Yiqun Li Hao"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.23530 MTRouter authors Zhang Yiqun Li Hao"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-26T10:26:42.901888+00:00_

Web search results for query: "FrugalGPT How to Use Large Language Models Reducing Cost Improving Performance Chen Zaharia Zou arXiv 2305.05176"

Links: [{"title":"[2305.05176] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://arxiv.org/abs/2305.05176"},{"title":"FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://www.researchgate.net/publication/370633900_FrugalGPT_How_to_Use_Large_Language_Models_While_Reducing_Cost_and_Improving_Performance"},{"title":"[2305.05176] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://ar5iv.labs.arxiv.org/html/2305.05176"},{"title":"Paper page - FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://huggingface.co/papers/2305.05176"},{"title":"[2305.05176v1] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance","url":"https://arxiv.org/abs/2305.05176v1"},{"title":"FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance - Summary","url":"https://portkey.ai/blog/frugalgpt-how-to-use-large-language-models-while-reducing-cost-and-improving-performance-summary/"},{"title":"[PDF] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FrugalGPT:-How-to-Use-Large-Language-Models-While-Chen-Zaharia/585f8b9725f5f5e5495c3508d39f70d1c053e190"}]

I found the paper you're looking for! Here's what I can tell you about it:

## FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance

**Authors:** Lingjiao Chen, Matei Zaharia, and James Zou from Stanford University

**Publication:** Published on May 9, 2023

**Paper ID:** arXiv 2305.05176

**Overview:**
The paper addresses the expense of using LLMs on large collections of queries, outlin
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T10:26:42.902083+00:00_

Web search results for query: "Language Models Mostly Know What They Know Kadavath arXiv 2207.05221"

Links: [{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"(PDF) Language Models (Mostly) Know What They Know","url":"https://www.researchgate.net/publication/361949621_Language_Models_Mostly_Know_What_They_Know"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know – Papiers","url":"https://papiers.ai/2207.05221"},{"title":"[2207.05221v4] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221v4"}]

I found the paper you're looking for. Here's the information:

**"Language Models (Mostly) Know What They Know"** is a research paper by Saurav Kadavath and 35 co-authors, published on arXiv in 2022 with identifier 2207.05221.

**Summary of the paper:**

The paper studies whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly. 

Key findings include:

1. Larger models are well-calibrated on diverse multiple choice and true/false questions when they are provided in the right format.

2. The researchers can approach s
…[truncated 705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-26T10:26:42.902275+00:00_

Web search results for query: "AgentBench Evaluating LLMs as Agents Liu Yu Zhang Xu Lei Lai ICLR 2024"

Links: [{"title":"[2308.03688] AgentBench: Evaluating LLMs as Agents","url":"https://arxiv.org/abs/2308.03688"},{"title":"AgentBench: Evaluating LLMs as Agents","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html"},{"title":"ICLR Poster AgentBench: Evaluating LLMs as Agents","url":"https://iclr.cc/virtual/2024/poster/17388"},{"title":"AgentBench: Evaluating LLMs as Agents | OpenReview","url":"https://openreview.net/forum?id=zAdUB0aCTQ"},{"title":"GitHub - THUDM/AgentBench: A Comprehensive Benchmark to Evaluate LLMs as Agents (ICLR'24) · GitHub","url":"https://github.com/THUDM/AgentBench"},{"title":"[PDF] AgentBench: Evaluating LLMs as Agents | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AgentBench:-Evaluating-LLMs-as-Agents-Liu-Yu/5dbf93a68b7fda600521f046dea35ea8ba9e884f"},{"title":"(PDF) AgentBench: Evaluating LLMs as Agents","url":"https://www.researchgate.net/publication/372962217_AgentBench_Evaluating_LLMs_as_Agents"},{"title":"AgentBench: Evaluating LLMs as Agents","url":"https://www.emergentmind.com/papers/2308.03688"},{"title":"AgentBench (AgentBench) - Agentic Design | Agentic Design Patterns","url":"https://agentic-design.ai/patterns/evaluation-monitoring/agentbench"},{"title":"AgentBench: Evaluating LLMs as Agents","url":"https://arxiv.org/pdf/2308.03688"}]

I found information about the paper you're searching for. Here are the key details:

**AgentBench: Evaluating LLMs as Agents** was published at the International Conference on Learning Representations 2024 (ICLR 2024). However, I should note that the author names in the search results show **Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai**, and others—the names are slightly different from what you specified (Liu Yu, Zhang Xu, Lei Lai appear to be different name arrangements).

The paper presents 
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-26T10:26:42.902506+00:00_

Now I have all the information needed. Here are the verification results:

---

### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- 真实性：✓
- 作者：✓ (Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori Hashimoto — all match)
- 年份：✓ (ICLR 2024)
- 标题：✓
- Venue：✓ (ICLR 2024, Spotlight paper)
- ID：N/A (no arXiv ID in bib entry; actual arXiv ID is 2309.15817)

---

### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs
- 真实性：✓
- 作者：✗ (bib entry says "Lee, Seanie and others" — actual full author list is Seanie Lee, Dong Bok Lee, Dominik Wagner, Minki Kang, Haebin Seong, Tobias Bocklet, Juho Lee, Sung Ju Hwang. The "and others" is lazy but "Lee, Seanie" as first author is correct)
- 年份：✓ (2025)
- 标题：✓ (full title in the proceedings uses "Large Language Models" instead of "LLMs", but this is a minor abbreviation difference)
- Venue：✓ (Findings of ACL 2025)
- ID：N/A (no arXiv ID in bib entry; actual arXiv ID is 2502.12464)

---

### 39. [altman1999constrained] — Constrained Markov Decision Processes
- 真实性：✓
- 作者：✓ (Eitan Altman)
- 年份：✓ (1999)
- 标题：✓
- Venue：✓ (Chapman & Hall/CRC, book)
- ID：N/A

---

### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning
- 真实性：✓
- 作者：✓ (Oliver Mihatsch, Ralph Neuneier)
- 年份：✓ (2002)
- 标题：✓
- Venue：✓ (Machine Learning, vol 49, no 2-3, pp 267-290)
- ID：N/A

---

### 41. [natarajan2013learning] — Learning with Noisy Labels
- 真实性：✓
- 作者：✓ (Nagarajan Natarajan, Inderjit S. Dhillon, Pradeep Ravikumar, Ambuj Tewari)
- 年份：✓ (2013)
- 标题：✓
- Venue：✓ (NeurIPS 2013, originally called NIPS 2013)
- ID：N/A

---

### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training
- 真实性：✓
- 作者：✓ (Caiqi Zhang, Menglin Xia, Xuchao Zhang, Daniel Madrigal, Ankur Mallick, Samuel Kessler, Victor Ruehle, Saravan Rajmohan — all match)
- 年份：✓ (2026, submitted Fe
…[truncated 1656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 28
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-26T10:26:42.902698+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Ji Xin ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Ji Xin ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-26T10:26:42.902853+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoMix Automatically Mixing Language Models Madaan Aggarwal Anand Potdar Gupta Tandon NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoMix Automatically Mixing Language Models Madaan Aggarwal Anand Potdar Gupta Tandon NeurIPS 2024"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-26T10:26:42.903018+00:00_

Web search results for query: "arxiv 2603.07915 Ares authors full list Jingbo Yang Bairu Hou"

Links: [{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1408&show=2000"},{"title":"[2412.10623] Ares: Approximate Representations via Efficient Sparsification -- A Stateless Approach through Polynomial Homomorphism","url":"https://arxiv.org/abs/2412.10623"},{"title":"GitHub - stanford-futuredata/ARES: Automated Evaluation of RAG Systems · GitHub","url":"https://github.com/stanford-futuredata/ARES"},{"title":"[2601.07915] Subregion algebras in classical and quantum gravity","url":"https://arxiv.org/abs/2601.07915"},{"title":"Author Identifiers - arXiv info","url":"https://info.arxiv.org/help/author_identifiers.html"},{"title":"ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery","url":"https://arxiv.org/html/2603.17623v1"}]

Based on the search results, the full list of authors for arXiv paper 2603.07915 "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" is: Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, and Shiyu Chang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-26T10:26:42.903196+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Language Agent Tree Search Unifies Reasoning Acting Planning Language Models Zhou Yan Shlapentokh-Rothman Wang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Language Agent Tree Search Unifies Reasoning Acting Planning Language Models Zhou Yan Shlapentokh-Rothman Wang ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-26T10:26:42.903344+00:00_

Web search results for query: "arxiv 2604.23530 MTRouter authors Zhang Yiqun Li Hao"

Links: [{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=7065&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1575&show=1000"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=225&show=2000"},{"title":"Computer Science Apr 2024","url":"https://arxiv.org/list/cs/2024-04?skip=2630&show=2000"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings

**arXiv ID:** 2604.23530

**Authors:** Yiqun Zhang, Hao Li, Zihan Wang, Shi Feng, Xiaocui Yang, Daling Wang, Bo Zhang, Lei Bai, and Shuyue Hu

**Affiliations:** The authors are from the School of Computer Science and Engineering at Northeastern University Shenyang, China, and Shanghai Artificial Intelligence Laboratory

**Research Focus:** The paper studies cost-aware multi-turn LLM routing—selecting which model to invoke at each turn from a model pool given a fixed cost budget—and proposes MTRouter, which encodes the interaction history and candidate models into joint history-model embeddings, and learns an outcome estimator from logged trajectories to predict turn-level model utility

The paper was submitted on April 26, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-26T10:26:42.903511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2507.10524 Mixture-of-Recursions full author list Bae Sangmin Kim Yujin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2507.10524 Mixture-of-Recursions full author list Bae Sangmin Kim Yujin"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-26T10:26:42.903663+00:00_

Web search results for query: "DeeBERT Dynamic Early Exiting Accelerating BERT Inference Ji Xin ACL 2020"

Links: [{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.204/"},{"title":"GitHub - castorini/DeeBERT: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference · GitHub","url":"https://github.com/castorini/DeeBERT"},{"title":"[2004.12993] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://arxiv.org/abs/2004.12993"},{"title":"ACL2020: DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://virtual.acl2020.org/paper_main.204.html"},{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://cs.uwaterloo.ca/~jimmylin/publications/Xin_etal_ACL2020.pdf"},{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://papertalk.org/papertalks/6390"},{"title":"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference | Request PDF","url":"https://www.researchgate.net/publication/343302481_DeeBERT_Dynamic_Early_Exiting_for_Accelerating_BERT_Inference"},{"title":"[PDF] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeeBERT:-Dynamic-Early-Exiting-for-Accelerating-Xin-Tang/90a1491ac32e732c93773354e4e665794ed4d490"},{"title":"[Quick Review] DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference","url":"https://liner.com/review/deebert-dynamic-early-exiting-for-accelerating-bert-inference"}]

Based on the search results, here's information about the DeeBERT paper:

## Paper Overview

DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference was published at the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics in July 2020 by Ji Xin, Raphael Tang, Jaejun Lee, Yaoliang Yu, and Jimmy Lin.

## Key Contributions

The paper proposes DeeBERT, a simple 
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-26T10:26:42.903843+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.09252 \"Chung-En Sun\" \"Linbo Liu\" \"Ge Yan\" \"Zimo Wang\" \"Tsui-Wei Weng\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.09252 \"Chung-En Sun\" \"Linbo Liu\" \"Ge Yan\" \"Zimo Wang\" \"Tsui-Wei Weng\" authors"
  }
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T10:26:42.904009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BERT Loses Patience Fast Robust Inference Early Exit Zhou Xu NeurIPS 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BERT Loses Patience Fast Robust Inference Early Exit Zhou Xu NeurIPS 2020"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T10:26:42.904171+00:00_

Web search results for query: "Language Agent Tree Search Unifies Reasoning Acting Planning Language Models Zhou Yan Shlapentokh-Rothman Wang ICML 2024"

Links: [{"title":"GitHub - lapisrocks/LanguageAgentTreeSearch: [ICML 2024] Official repository for \"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models\" · GitHub","url":"https://github.com/lapisrocks/LanguageAgentTreeSearch"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models - Illinois Experts","url":"https://experts.illinois.edu/en/publications/language-agent-tree-search-unifies-reasoning-acting-and-planning-/"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in","url":"https://arxiv.org/pdf/2310.04406"},{"title":"ICML Poster Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://icml.cc/virtual/2024/poster/33107"},{"title":"LanguageAgentTreeSearch | [ICML 2024] Official repository for “Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models”","url":"http://lapisrocks.github.io/LanguageAgentTreeSearch/"},{"title":"[2310.04406] Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models","url":"https://arxiv.org/abs/2310.04406"},{"title":"Language agent tree search unifies reasoning, acting, and planning in language models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694642"},{"title":"Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models","url":"https://arxiv.org/html/2310.04406v3"},{"title":"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | OpenReview","url":"https://openreview.net/forum?id=6LNTSrJjBe"},{"title":"Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/l
…[truncated 1339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-26T10:26:42.904365+00:00_

Web search results for query: "AutoMix Automatically Mixing Language Models Madaan Aggarwal Anand Potdar Gupta Tandon NeurIPS 2024"

Links: [{"title":"[2310.12963] AutoMix: Automatically Mixing Language Models","url":"https://arxiv.org/abs/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://proceedings.neurips.cc//paper_files/paper/2024/hash/ecda225cb187b40ea8edc1f46b03ffda-Abstract-Conference.html"},{"title":"AutoMix: Automatically Mixing Language Models | OpenReview","url":"https://openreview.net/forum?id=e6WrwIvgzX"},{"title":"AutoMix: Automatically Mixing Language Models Pranjal Aggarwal♢∗ Aman Madaan♣∗","url":"https://arxiv.org/pdf/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://automix-llm.github.io/automix/"},{"title":"AutoMix: automatically mixing language models","url":"https://dl.acm.org/doi/10.5555/3737916.3742080"},{"title":"AutoMix: Automatically Mixing Language Models | Request PDF","url":"https://www.researchgate.net/publication/397213626_AutoMix_Automatically_Mixing_Language_Models"},{"title":"[PDF] AutoMix: Automatically Mixing Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AutoMix:-Automatically-Mixing-Language-Models-Madaan-Aggarwal/f0ed191bdcbd56610ab4d95c5a80d5ac31ffc074"}]

Based on the search results, I found detailed information about this paper:

## AutoMix: Automatically Mixing Language Models

The paper was published at NeurIPS 2024 with authors Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam.

**Overview:** AutoMix is an approach that strategically routes queries to larger language models based on the approximate correctness of outputs from a smaller LM.

**Key Technical Contributions:** First, it has a few-shot self-verification mechanism, which estimates the reliability of its 
…[truncated 688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-26T10:26:42.904543+00:00_

Web search results for query: "arxiv 2507.10524 Mixture-of-Recursions full author list Bae Sangmin Kim Yujin"

Links: [{"title":"[2507.10524] Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/abs/2507.10524"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"},{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/html/2507.10524v1"},{"title":"(PDF) Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://www.researchgate.net/publication/393684588_Mixture-of-Recursions_Learning_Dynamic_Recursive_Depths_for_Adaptive_Token-Level_Computation"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiviq.substack.com/p/mixture-of-recursions-learning-dynamic"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | Latest Papers | HyperAI超神经","url":"https://hyper.ai/en/papers/2507.10524"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | alphaXiv","url":"https://www.alphaxiv.org/resources/2507.10524v2"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mixture-recursions-learning-dynamic-recursive-depths-adaptive"}]

Based on the search results, here is the full author list for arxiv paper 2507.10524 "Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation":

The au
…[truncated 641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-26T10:26:42.904717+00:00_

Web search results for query: "arxiv 2605.09252 "Chung-En Sun" "Linbo Liu" "Ge Yan" "Zimo Wang" "Tsui-Wei Weng" authors"

Links: [{"title":"[2605.09252] LLM Agents Already Know When to Call Tools -- Even Without Reasoning","url":"https://arxiv.org/abs/2605.09252"},{"title":"LLM Agents Already Know When to Call Tools - Even Without Reasoning","url":"https://arxiv.org/html/2605.09252v2"},{"title":"LLM Agents Already Know When to Call Tools","url":"https://lilywenglab.github.io/when2tool/"},{"title":"GitHub - Trustworthy-ML-Lab/when2tool · GitHub","url":"https://github.com/Trustworthy-ML-Lab/when2tool"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"},{"title":"Computer Vision and Pattern Recognition Jun 2025","url":"https://www.arxiv.org/list/cs.CV/2025-06?skip=1950&show=1000"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=931&show=1000"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=9875&show=1000"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=2600&show=1000"}]

Based on the search results, I found the paper you were looking for:

The authors of arXiv paper 2605.09252 are Chung-En Sun, Linbo Liu, Ge Yan, Zimo Wang, and Tsui-Wei Weng.

The paper is titled "LLM Agents Already Know When to Call Tools -- Even Without Reasoning" and proposes When2Tool, a benchmark of 18 environments spanning three categories of tool necessity. The authors are affiliated with University of California, San Diego.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-26T10:26:42.904884+00:00_

Web search results for query: "BERT Loses Patience Fast Robust Inference Early Exit Zhou Xu NeurIPS 2020"

Links: [{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://proceedings.neurips.cc/paper/2020/hash/d4dd111a4fd973394238aca5c05bebe3-Abstract.html"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://papers.nips.cc/paper/2020/hash/d4dd111a4fd973394238aca5c05bebe3-Abstract.html"},{"title":"Review for NeurIPS paper: BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://proceedings.neurips.cc/paper_files/paper/2020/file/d4dd111a4fd973394238aca5c05bebe3-MetaReview.html"},{"title":"BERT loses patience: Fast and robust inference with early exit - Beihang University","url":"https://research.buaa.edu.cn/en/publications/bert-loses-patience-fast-and-robust-inference-with-early-exit/"},{"title":"Review for NeurIPS paper: BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://papers.nips.cc/paper/2020/file/d4dd111a4fd973394238aca5c05bebe3-Review.html"},{"title":"GitHub - JetRunner/PABEE: Code for the paper \"BERT Loses Patience: Fast and Robust Inference with Early Exit\". · GitHub","url":"https://github.com/JetRunner/PABEE"},{"title":"BERT Loses Patience: Fast and Robust Inference with Early Exit [Quick Review]","url":"https://liner.com/review/bert-loses-patience-fast-and-robust-inference-with-early-exit"},{"title":"NeurIPS 2020 : BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://nips.cc/virtual/2020/public/poster_d4dd111a4fd973394238aca5c05bebe3.html"},{"title":"[2006.04152] BERT Loses Patience: Fast and Robust Inference with Early Exit","url":"https://arxiv.org/abs/2006.04152"}]

I found the paper you're looking for! Here's what I found:

"BERT Loses Patience: Fast and Robust Inference with Early Exit" was presented at NeurIPS 2020 (Advances in Neural Information Processing Systems 33) and authored by Wangchunshu Zhou, C
…[truncated 976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T10:26:42.905085+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Depths Dynamically Allocating Compute Transformer-Based Language Models Raposo Ritter Richards Lillicrap Humphreys Santoro ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Depths Dynamically Allocating Compute Transformer-Based Language Models Raposo Ritter Richards Lillicrap Humphreys Santoro ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-26T10:26:42.905241+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reflexion arxiv 2303.11366 authors list Noah Shinn Federico Cassano"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reflexion arxiv 2303.11366 authors list Noah Shinn Federico Cassano"
  }
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-26T10:26:42.905388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Risk-Sensitive Robust Decision-Making CVaR Optimization Approach Chow Tamar Mannor Pavone NeurIPS 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Risk-Sensitive Robust Decision-Making CVaR Optimization Approach Chow Tamar Mannor Pavone NeurIPS 2015"
  }
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-26T10:26:42.905534+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2203.07540 ScienceWorld authors Wang Ruoyao Jansen Peter Côté Marc-Alexandre Ammanabrolu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2203.07540 ScienceWorld authors Wang Ruoyao Jansen Peter Côté Marc-Alexandre Ammanabrolu"
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-26T10:26:42.905686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ross Gordon Bagnell DAgger AISTATS 2011 \"Stéphane Ross\" \"Geoffrey J. Gordon\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ross Gordon Bagnell DAgger AISTATS 2011 \"Stéphane Ross\" \"Geoffrey J. Gordon\""
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-26T10:26:42.905890+00:00_

Web search results for query: "Reflexion arxiv 2303.11366 authors list Noah Shinn Federico Cassano"

Links: [{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v4"},{"title":"[2303.11366v1] Reflexion: an autonomous agent with dynamic memory and self-reflection","url":"https://web3.arxiv.org/abs/2303.11366v1"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/html/2303.11366"},{"title":"[2303.11366v3] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v3"},{"title":"reflexion/README.md at main · noahshinn/reflexion","url":"https://github.com/noahshinn/reflexion/blob/main/README.md"},{"title":"Paper page - Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://huggingface.co/papers/2303.11366"}]

Based on the search results, the authors of the paper "Reflexion: Language Agents with Verbal Reinforcement Learning" (arXiv 2303.11366) are Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.

Noah Shinn is from Northeastern University, Federico Cassano is from Northeastern University, Edward Berman is from Northeastern University, Ashwin Gopinath is from Massachusetts Institute of Technology, Karthik Narasimhan is from Princeton University, and Shunyu Yao is from Princeton University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-26T10:26:42.906203+00:00_

Web search results for query: "Mixture-of-Depths Dynamically Allocating Compute Transformer-Based Language Models Raposo Ritter Richards Lillicrap Humphreys Santoro ICML 2024"

Links: [{"title":"[2404.02258] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/abs/2404.02258"},{"title":"[PDF] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mixture-of-Depths:-Dynamically-allocating-compute-Raposo-Ritter/a1f23f04421cdc62e80fe9f04c1ce60f4a6af9f0"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/paper-review-mixture-of-depths-dddf00029026"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models, David Raposo+, N/A, arXiv'24 · Issue #1273 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1273"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language","url":"https://arxiv.org/pdf/2404.02258"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mixture-depths-dynamically-allocating-compute-transformer-based"},{"title":"Paper page - Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://huggingface.co/papers/2404.02258"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69ce3feb84947a5132b622ec"},{"title":"GitHub - sramshetty/mixture-of-depths: An unofficial implementation of \"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-26T10:26:42.906481+00:00_

Web search results for query: "Ross Gordon Bagnell DAgger AISTATS 2011 "Stéphane Ross" "Geoffrey J. Gordon""

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) - HackMD","url":"https://hackmd.io/@XiNyAicATy2jGaBhGc2ZRg/r1a97tfCU"},{"title":"ilpyt.algos.dagger API documentation","url":"https://mitre.github.io/ilpyt/algos/dagger.html"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"dblp: Stéphane Ross","url":"https://dblp.org/pid/93/2963.html"},{"title":"arXiv:1011.0686v3 [cs.LG] 16 Mar 2011","url":"https://arxiv.org/pdf/1011.0686"},{"title":"pre-proceedings Imitation Learning by Coaching∗ He He Hal Daumé III","url":"https://www.cs.jhu.edu/~jason/papers/he+al.nips12.pdf"}]

I found the paper you were searching for. "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning" by Stéphane Ross, Geoffrey J. Gordon, and J. Andrew Bagnell was presented at AISTATS 2011. This paper describes the DAgger (Dataset Aggregation) algorithm.

The paper addresses sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), which violates the common i.i.d. assumptions made in statistical learning.

The paper is available through multiple sources, including the Machine Learning Research Proceedings database (proceedings.mlr.press) and various academic repositories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 204 · 2026-05-26T10:26:42.906710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Yael Septon\" OR \"Guy Septon\" Amitai Amir counterfactual action outcomes AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Yael Septon\" OR \"Guy Septon\" Amitai Amir counterfactual action outcomes AAAI"
  }
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-26T10:26:42.906874+00:00_

Web search results for query: "arxiv 2203.07540 ScienceWorld authors Wang Ruoyao Jansen Peter Côté Marc-Alexandre Ammanabrolu"

Links: [{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5^\"th\" Grader?","url":"https://ar5iv.labs.arxiv.org/html/2203.07540"},{"title":"arXiv:2203.07540v2 [cs.CL] 14 Nov 2022","url":"https://arxiv.org/pdf/2203.07540"},{"title":"[PDF] ScienceWorld: Is your Agent Smarter than a 5th Grader? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ScienceWorld:-Is-your-Agent-Smarter-than-a-5th-Wang-Jansen/0e41fd22d483047bd8fdb1757d90c7702493567e"},{"title":"Paper page - ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://huggingface.co/papers/2203.07540"},{"title":"(PDF) ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://www.researchgate.net/publication/359254600_ScienceWorld_Is_your_Agent_Smarter_than_a_5th_Grader"},{"title":"Computer Science Mar 2022","url":"https://arxiv.org/list/cs/2022-03?skip=2740&show=2000"},{"title":"dblp: Ruoyao Wang","url":"https://dblp.org/pid/212/7581.html"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.775/"}]

I found the paper! Here's the information about arxiv 2203.07540:

**Title:** ScienceWorld: Is your Agent Smarter than a 5th Grader?

**Authors:** Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu

**Affiliations:** University of Arizona (Tucson, AZ), Microsoft Research Montréal, and Allen Institute for AI (Seattle, WA)

**Overview:** The paper presents ScienceWorld, a benchmark to test agents' scientific reasoning abilities in a new interactive text environment at the level of a standard elementary school science curriculum. Current models cannot reason about or explain learned science concepts in novel contexts.

*
…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-26T10:26:42.907108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fast Inference from Transformers via Speculative Decoding Leviathan Kalman Matias ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fast Inference from Transformers via Speculative Decoding Leviathan Kalman Matias ICML 2023"
  }
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-26T10:26:42.907285+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"J. Andrew Bagnell\" OR \"Drew Bagnell\" DAgger AISTATS 2011 imitation learning author name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"J. Andrew Bagnell\" OR \"Drew Bagnell\" DAgger AISTATS 2011 imitation learning author name"
  }
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-26T10:26:42.907440+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2504.11536 ReTool full authors Feng Jiazhan Huang Shijue Qu Xingwei"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2504.11536 ReTool full authors Feng Jiazhan Huang Shijue Qu Xingwei"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-26T10:26:42.907591+00:00_

Web search results for query: "Risk-Sensitive Robust Decision-Making CVaR Optimization Approach Chow Tamar Mannor Pavone NeurIPS 2015"

Links: [{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"https://proceedings.neurips.cc/paper/2015/hash/64223ccf70bbb65a3a4aceac37e21016-Abstract.html"},{"title":"[1506.02188] Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"https://arxiv.org/abs/1506.02188"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach","url":"http://papers.neurips.cc/paper/6014-risk-sensitive-and-robust-decision-making-a-cvar-optimization-approach.pdf"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach | Request PDF","url":"https://www.researchgate.net/publication/277959194_Risk-Sensitive_and_Robust_Decision-Making_a_CVaR_Optimization_Approach"},{"title":"Risk-sensitive and robust decision-making: A CVaR optimization approach - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/risk-sensitive-and-robust-decision-making-a-cvar-optimization-app-2/"},{"title":"dblp: Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach.","url":"https://dblp.org/rec/conf/nips/ChowTMP15.html"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150602188C/abstract"},{"title":"[PDF] Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Risk-Sensitive-and-Robust-Decision-Making:-a-CVaR-Chow-Tamar/f583f9e720c16f6bb50f9d624b61c3bc851be008"},{"title":"Risk-Sensitive and Robust Decision-Makin... - NIPS 2015","url":"https://nips2015.sched.com/event/5QQ5/risk-sensitive-and-robust-decision-making-a-cvar-optimization-approach"},{"title":"Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach. | BibSonomy","url":"h
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-26T10:26:42.907773+00:00_

Web search results for query: ""J. Andrew Bagnell" OR "Drew Bagnell" DAgger AISTATS 2011 imitation learning author name"

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) - HackMD","url":"https://hackmd.io/@XiNyAicATy2jGaBhGc2ZRg/r1a97tfCU"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"ilpyt.algos.dagger API documentation","url":"https://mitre.github.io/ilpyt/algos/dagger.html"},{"title":"J. Andrew Bagnell","url":"https://scholar.google.com/citations?user=7t4jbPQAAAAJ&hl=en"},{"title":"arXiv:1011.0686v3 [cs.LG] 16 Mar 2011","url":"https://arxiv.org/pdf/1011.0686"},{"title":"Introduction to DAgger Shuijing Liu CS 598 SG Paper Presentation 9/26/2019","url":"https://shuijing725.github.io/files/20190926_DAgger.pdf"},{"title":"No-Regret Reductions for Imitation Learning and Structured Prediction","url":"https://www.researchgate.net/publication/220481794_No-Regret_Reductions_for_Imitation_Learning_and_Structured_Prediction"},{"title":"A Reduction of Imitation Learning and Structure Prediction ...","url":"https://www.cl.uni-heidelberg.de/courses/ws18/iml/dagger.pdf"}]

Based on the search results, I can confirm the author information you're looking for:

The DAgger algorithm was described in the paper "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning" by Stéphane Ross, Geoffrey J. Gordon, and J. Andrew Bagnell, and presented at AISTATS 2011.

The researcher's name appears in the literature as both "J. Andrew Bagnell" and "Drew Bagnell" (which is a shortened form of Andrew). The DAgger paper was authored by Stéphane Ross, Geoffrey Gordon, and Drew Bagnell, published in the Proceedings of the fourteenth
…[truncated 179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 211 · 2026-05-26T10:26:42.907951+00:00_

Web search results for query: ""Yael Septon" OR "Guy Septon" Amitai Amir counterfactual action outcomes AAAI"

Links: [{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes","url":"https://ojs.aaai.org/index.php/AAAI/article/download/28863/29640"},{"title":"[2312.11118] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/abs/2312.11118"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/explaining-reinforcement-learning-agents-through-counterfactual-a"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes | Request PDF","url":"https://www.researchgate.net/publication/379288542_Explaining_Reinforcement_Learning_Agents_through_Counterfactual_Action_Outcomes"},{"title":"Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/28863"},{"title":"Yotam Amitai - Publications","url":"https://www.yotamitai.com/publications"},{"title":"dblp: Yotam Amitai","url":"https://dblp.org/pid/284/9338.html"},{"title":"Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes","url":"https://arxiv.org/html/2312.11118v1"},{"title":"[PDF] Explaining Reinforcement Learning Agents Through Counterfactual Action Outcomes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Explaining-Reinforcement-Learning-Agents-Through-Amitai-Septon/66766682c5669964ec6405e0acd9ca228024c5ab"},{"title":"Yotam Amitai's research works","url":"https://www.researchgate.net/scientific-contributions/Yotam-Amitai-2199187157"}]

Based on the search results, I found the research you're looking for. The paper "Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes" was w
…[truncated 592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-26T10:26:42.908206+00:00_

Web search results for query: "arxiv 2504.11536 ReTool full authors Feng Jiazhan Huang Shijue Qu Xingwei"

Links: [{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/pdf/2504.11536"},{"title":"Paper page - ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://huggingface.co/papers/2504.11536"},{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://ar5iv.labs.arxiv.org/html/2504.11536"},{"title":"[2504.11536v1] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536v1"},{"title":"[PDF] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReTool:-Reinforcement-Learning-for-Strategic-Tool-Feng-Huang/8402e446158252992b6ddf1ff1b0658c39d7604e"},{"title":"README.md · JoeYing/ReTool-SFT at main","url":"https://huggingface.co/datasets/JoeYing/ReTool-SFT/blob/main/README.md"},{"title":"[2504.11536v2] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"http://arxiv.org/abs/2504.11536v2"}]

The full list of authors for the paper "ReTool: Reinforcement Learning for Strategic Tool Use in LLMs" (arxiv 2504.11536) is: Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin Chi, and Wanjun Zhong.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-26T10:26:42.908431+00:00_

Web search results for query: "Fast Inference from Transformers via Speculative Decoding Leviathan Kalman Matias ICML 2023"

Links: [{"title":"[2211.17192] Fast Inference from Transformers via Speculative Decoding","url":"https://arxiv.org/abs/2211.17192"},{"title":"Fast inference from transformers via speculative decoding | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3619203"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://proceedings.mlr.press/v202/leviathan23a.html"},{"title":"GitHub - romsto/Speculative-Decoding: Implementation of the paper Fast Inference from Transformers via Speculative Decoding, Leviathan et al. 2023. · GitHub","url":"https://github.com/romsto/Speculative-Decoding"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://openreview.net/pdf?id=C9NEblP8vS"},{"title":"Fast Inference from Transformers via Speculative Decoding - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/fast-inference-from-transformers-via-speculative-decoding/"},{"title":"ICML 2023 Fast Inference from Transformers via Speculative Decoding Oral","url":"https://icml.cc/virtual/2023/oral/25546"},{"title":"Fast Inference from Transformers via Speculative Decoding","url":"https://www.summarizepaper.com/en/arxiv-id/2211.17192v2/"},{"title":"Speculative Decoding Reyna Abhyankar","url":"https://cseweb.ucsd.edu/~yiying/cse291a-fall25/reading/spec-decoding.pdf"},{"title":"(PDF) Fast Inference from Transformers via Speculative Decoding","url":"https://www.researchgate.net/publication/365889265_Fast_Inference_from_Transformers_via_Speculative_Decoding"}]

I found the paper! Here are the key details about "Fast Inference from Transformers via Speculative Decoding":

## Paper Information

The paper was published in the Proceedings of the 40th International Conference on Machine Learning (ICML 2023) with pages 19274-19286, authored by 
…[truncated 851 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-26T10:26:42.908648+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Optimizing the CVaR via Sampling Aviv Tamar Yonatan Glassner Shie Mannor AAAI 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Optimizing the CVaR via Sampling Aviv Tamar Yonatan Glassner Shie Mannor AAAI 2015"
  }
}
```

</details>

---

### Tool call

_source line 215 · 2026-05-26T10:26:42.908805+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 venue accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 venue accepted"
  }
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-26T10:26:42.908955+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoMix Automatically Mixing Language Models full author list arxiv 2310.12963"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoMix Automatically Mixing Language Models full author list arxiv 2310.12963"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-26T10:26:42.909184+00:00_

Web search results for query: "Optimizing the CVaR via Sampling Aviv Tamar Yonatan Glassner Shie Mannor AAAI 2015"

Links: [{"title":"[1404.3862] Optimizing the CVaR via Sampling","url":"https://arxiv.org/abs/1404.3862"},{"title":"Optimizing the CVaR via Sampling | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/9561"},{"title":"Optimizing the CVaR via Sampling | Request PDF","url":"https://www.researchgate.net/publication/361512404_Optimizing_the_CVaR_via_Sampling"},{"title":"CVaR Optimization via Sampling","url":"https://www.emergentmind.com/papers/1404.3862"},{"title":"Optimizing the CVaR via Sampling - AAAI","url":"https://aaai.org/papers/9561-optimizing-the-cvar-via-sampling/"},{"title":"[PDF] Optimizing the CVaR via Sampling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/2e939ed3bb378ea966bf9f710fc1138f4e16ef38"},{"title":"Optimizing the CVaR via Sampling Aviv Tamar, Yonatan Glassner, and Shie Mannor","url":"https://cdn.aaai.org/ojs/9561/9561-13-13089-1-2-20201228.pdf"},{"title":"Optimizing the CVaR via sampling - Fingerprint - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/optimizing-the-cvar-via-sampling-2/fingerprints/"},{"title":"A Model-Based Method for Minimizing CVaR and Beyond","url":"https://axi.lims.ac.uk/paper/2305.17498?page=2"}]

I found the paper you're looking for! Here are the details:

The paper "Optimizing the CVaR via Sampling" by Tamar, Glassner, and Mannor was published in the Proceedings of the AAAI Conference on Artificial Intelligence, Volume 29(1) in 2015.

**Key Contributions:**

The authors develop a new formula for the gradient of CVaR in the form of a conditional expectation and propose a novel sampling-based estimator for the CVaR gradient, in the spirit of the likelihood-ratio method. They analyze the bias of the estimator and prove the convergence of a corresponding stochastic gradient descent a
…[truncated 487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T10:26:42.909460+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org abs 2604.23530 MTRouter full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org abs 2604.23530 MTRouter full author list"
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-26T10:26:42.909690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RouteLLM 2406.18665 authors complete list \"M Waleed Kadous\" \"Ion Stoica\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RouteLLM 2406.18665 authors complete list \"M Waleed Kadous\" \"Ion Stoica\""
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-26T10:26:42.909907+00:00_

Web search results for query: "arxiv.org abs 2604.23530 MTRouter full author list"

Links: [{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"Sciprofiles","url":"https://sciprofiles.com/profile/author/RVZIZXlrSWRiYTdvWlVMcjlKazR3Zz09"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"Computer Science authors/titles Nov 2019","url":"https://arxiv.org/list/cs/1911"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"Alvaro Velasquez","url":"https://sciprofiles.com/profile/author/bkMwQ01EczEybWcrMDZnU1BPM0x0Zz09"},{"title":"arXiv.org e-Print archive","url":"https://arxiv.org/"},{"title":"Computer Science Mar 2024","url":"https://arxiv.org/list/cs/2024-03?skip=4365&show=2000"},{"title":"Machine Learning authors/titles May 2019 (300 skipped)","url":"https://arxiv.org/list/stat.ML/1905?skip=300"}]

Based on the search results, the full author list for the MTRouter paper (arXiv:2604.23530) is: Yiqun Zhang, Hao Li, Zihan Wang, Shi Feng, Xiaocui Yang, Daling Wang, Bo Zhang, Lei Bai, and Shuyue Hu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-26T10:26:42.910165+00:00_

Web search results for query: "RouteLLM 2406.18665 authors complete list "M Waleed Kadous" "Ion Stoica""

Links: [{"title":"[2406.18665] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665"},{"title":"dblp: RouteLLM: Learning to Route LLMs with Preference Data.","url":"https://dblp.org/rec/journals/corr/abs-2406-18665.html"},{"title":"RouteLLM_reportOnReroutingLLM_Toreducecost.pdf","url":"https://www.slideshare.net/slideshow/routellm_reportonreroutingllm_toreducecost-pdf/272325617"},{"title":"[2406.18665v2] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v2"},{"title":"[2406.18665v3] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v3"},{"title":"[2406.18665v1] RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/abs/2406.18665v1"}]

Based on the search results, the complete list of authors for RouteLLM (arXiv:2406.18665) is: Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, M Waleed Kadous, and Ion Stoica.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 222 · 2026-05-26T10:26:42.910407+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"
  }
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T10:26:42.910621+00:00_

Web search results for query: "Mixture-of-Recursions NeurIPS 2025 or ICML 2025 venue accepted"

Links: [{"title":"GitHub - raymin0223/mixture_of_recursions: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation (NeurIPS 2025) · GitHub","url":"https://github.com/raymin0223/mixture_of_recursions"},{"title":"NeurIPS Poster Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118085"},{"title":"ICML Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Thinking","url":"https://icml.cc/virtual/2025/51797"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation | OpenReview","url":"https://openreview.net/forum?id=QuqsEIVWIG"},{"title":"[2507.10524] Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/abs/2507.10524"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive","url":"https://arxiv.org/pdf/2507.10524"}]

Based on the search results, I can confirm that Mixture-of-Recursions was accepted to NeurIPS 2025 as a poster. Additionally, the paper was also accepted to ICML 2025.

The paper introduces Mixture-of-Recursions (MoR), a unified framework that combines parameter efficiency by reusing a shared stack of layers across recursion steps, while lightweight routers enable adaptive token-level thinking by dynamically assigning different recursion depths to individual tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-26T10:26:42.910854+00:00_

Web search results for query: "AutoMix Automatically Mixing Language Models full author list arxiv 2310.12963"

Links: [{"title":"[2310.12963] AutoMix: Automatically Mixing Language Models","url":"https://arxiv.org/abs/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models Pranjal Aggarwal♢∗ Aman Madaan♣∗","url":"https://arxiv.org/pdf/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://automix-llm.github.io/automix/"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://github.com/automix-llm/automix"},{"title":"[PDF] AutoMix: Automatically Mixing Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AutoMix:-Automatically-Mixing-Language-Models-Madaan-Aggarwal/f0ed191bdcbd56610ab4d95c5a80d5ac31ffc074"},{"title":"dblp: AutoMix: Automatically Mixing Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2310-12963.html"},{"title":"AutoMix: Automatically Mixing Language Models Aman Madaan♠∗ Pranjal Aggarwal♢∗","url":"https://arxiv.org/pdf/2310.12963v3"},{"title":"Paper page - AutoMix: Automatically Mixing Language Models","url":"https://huggingface.co/papers/2310.12963"},{"title":"automix/docs/index.html at main · automix-llm/automix","url":"https://github.com/automix-llm/automix/blob/main/docs/index.html"}]

Based on the search results, the full author list for "AutoMix: Automatically Mixing Language Models" (arxiv 2310.12963) is: Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-26T10:26:42.911138+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ToolkenGPT arxiv 2305.11554 authors \"Shibo Hao\" \"Tianyang Liu\" \"Zhen Wang\" \"Zhiting Hu\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ToolkenGPT arxiv 2305.11554 authors \"Shibo Hao\" \"Tianyang Liu\" \"Zhen Wang\" \"Zhiting Hu\""
  }
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-26T10:26:42.911363+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Switch Transformers JMLR volume 23 number 120 pages 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Switch Transformers JMLR volume 23 number 120 pages 2022"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-26T10:26:42.911591+00:00_

Web search results for query: "Switch Transformers JMLR volume 23 number 120 pages 2022"

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/beta/papers/v23/21-0998.html"},{"title":"JMLR Volume 23","url":"https://www.jmlr.org/papers/v23/"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity | BibSonomy","url":"https://www.bibsonomy.org/bibtex/278a9c4fb8cee182f863af53ce1cf41ca/andolab"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"Journal of Machine Learning Research 23 (2022) 1-40","url":"https://arxiv.org/pdf/2101.03961"},{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"Awesome-LLM-papers/06_MOE/2022 (Google) (JMLR) [SwitchTransfomers] Switch Transformers - Scaling to Trillion Parameter Models with Simple and Efficient Sparsity.pdf at main · guyulongcs/Awesome-LLM-papers","url":"https://github.com/guyulongcs/Awesome-LLM-papers/blob/main/06_MOE/2022%20(Google)%20(JMLR)%20%5BSwitchTransfomers%5D%20Switch%20Transformers%20-%20Scaling%20to%20Trillion%20Parameter%20Models%20with%20Simple%20and%20Efficient%20Sparsity.pdf"},{"title":"Scaling to Trillion Parameter Models With Switch Transformers | by Zia Babar | Medium","url":"https://medium.com/@zbabar/scaling-to-trillion-parameter-models-with-switch-transformers-88ca5fb95e5c"}]

I found the information you were looking for. The paper "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity" was published in 2022, Volume 23, Issue 120, Pages 1−39 of the Journal of Machine Learning Research (JMLR).

The paper was authored by William Fedus, Barret Zoph, a
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-26T10:26:42.911843+00:00_

Web search results for query: "ToolkenGPT arxiv 2305.11554 authors "Shibo Hao" "Tianyang Liu" "Zhen Wang" "Zhiting Hu""

Links: [{"title":"[2305.11554] ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://arxiv.org/abs/2305.11554"},{"title":"(PDF) ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://www.researchgate.net/publication/370938521_ToolkenGPT_Augmenting_Frozen_Language_Models_with_Massive_Tools_via_Tool_Embeddings"},{"title":"[2305.11554] ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://ar5iv.labs.arxiv.org/html/2305.11554"},{"title":"Tianyang Liu","url":"https://leolty.github.io/"},{"title":"ToolkenGPT: Augmenting Frozen Language Models","url":"https://arxiv.org/pdf/2305.11554"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html"},{"title":"Computer Science May 2023","url":"https://arxiv.org/list/cs/2023-05?skip=4920&show=2000"},{"title":"ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings","url":"https://papers.nips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html"},{"title":"ToolkenGPT | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668110"},{"title":"Shibo Hao","url":"https://ber666.github.io/"}]

The search results confirm information about ToolkenGPT arxiv 2305.11554. Here's what I found:

**Paper Details:**
The paper "ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings" is authored by Shibo Hao, Tianyang Liu, Zhen Wang, and Zhiting Hu from UC San Diego and Mohamed bin Zayed University of Artificial Intelligence.

**Main Contribution:**
The pape
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-26T10:26:42.912128+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:jmlr.org \"21-0998\" Switch Transformers pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:jmlr.org \"21-0998\" Switch Transformers pages"
  }
}
```

</details>

---

### Tool result

_source line 230 · 2026-05-26T10:26:42.912359+00:00_

Web search results for query: "arxiv 2510.16492 authors Bonagiri Nguyen Plaut Kumaraguru"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/?searchtype=author&query=Benjamin+Plaut"},{"title":"dblp: BibTeX records: Ponnurangam Kumaraguru","url":"https://dblp.org/pid/97/5147.html?view=bibtex"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=1575&show=1000"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1191&show=1000"},{"title":"Computer Science Jun 2024","url":"https://www.arxiv.org/list/cs/2024-06?skip=8925&show=2000"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety"

**Authors:** Vamshi Krishna Bonagiri, Ponnurangam Kumaraguru, Khanh Nguyen, and Benjamin Plaut

**Affiliations:** The authors are from University of California, Berkeley, Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), and International Institute of Information Technology, Hyderabad (IIIT Hyderabad)

**arXiv ID:** 2510.16492

**Key contribution:** The paper proposes using "quitting" as a simple yet effective behavioral mechanism for LLM agents to recognize and withdraw from situations where they lack confidence.

The paper was submitted on October 18, 2025 and last revised on February 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown h
…[truncated 10 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-26T10:26:42.912613+00:00_

Web search results for query: "site:jmlr.org "21-0998" Switch Transformers pages"

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://jmlr.org/papers/volume23/21-0998/21-0998.pdf"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple   and Efficient Sparsity","url":"https://arxiv.org/pdf/2101.03961"},{"title":"SwitchHead: Accelerating Transformers with Mixture-of-Experts Attention","url":"https://arxiv.org/pdf/2312.07987"},{"title":"Transformers in Healthcare: A Survey","url":"https://arxiv.org/pdf/2307.00067"},{"title":"HuggingFace's Transformers: State-of-the-art Natural Language Processing","url":"https://arxiv.org/pdf/1910.03771"}]

Based on the search results, I found the Switch Transformers paper with the identifier "21-0998" on JMLR. The attribution requirements are provided at http://jmlr.org/papers/v23/21-0998.html, and the code for Switch Transformer is available at https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py.

The paper, titled "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity," is published in JMLR Volume 23 and was authored by William Fedus, Barret Zoph, and Noam Shazeer. It advances the current scale of language models by pre-training up to trillion parameter models on the "Colossal Clean Crawled Corpus", and achieves a 4x speedup over the T5-XXL model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-26T10:26:42.912870+00:00_

Now I have all the information needed. Here are my findings:

### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes
- 真实性：✓
- 作者：✗ (第二作者应为 **Yael Septon**，非 "Guy Septon")
- 年份：✓
- 标题：✓
- Venue：✓ (AAAI 2024)
- ID：N/A

### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents
- 真实性：✓ (但属于 AAMAS 2023 Doctoral Consortium 论文，非正式主会议论文)
- 作者：✓
- 年份：✓
- 标题：✓ (完整标题可能为 "Counterfactual Explanations for Reinforcement Learning Agents: Doctoral Consortium")
- Venue：✓ (AAMAS 2023)
- ID：N/A

### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (Artificial Intelligence, vol 295, pp 103455)
- ID：N/A

### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data
- 真实性：✓
- 作者：✓ (Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez, M Waleed Kadous, Ion Stoica 均正确)
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv:2406.18665)
- ID：✓

### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning
- 真实性：✓
- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2023)
- ID：N/A

### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv:2405.17935)
- ID：✓

### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (NeurIPS 2023, oral)
- ID：N/A

### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents
- 真实性：✓
- 作者：✓ (长作者列表与 ICLR 2024 proceedings 一致)
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
- 
…[truncated 345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 43
}
```

</details>

---

### Tool call

_source line 233 · 2026-05-26T10:26:42.913121+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org/abs/2510.16492 \"Bonagiri\" author order"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org/abs/2510.16492 \"Bonagiri\" author order"
  }
}
```

</details>

---

### Tool call

_source line 234 · 2026-05-26T10:26:42.913289+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mixture-of-Depths\" Raposo ICML 2024 proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mixture-of-Depths\" Raposo ICML 2024 proceedings"
  }
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-26T10:26:42.913440+00:00_

Web search results for query: "site:arxiv.org/abs/2510.16492 "Bonagiri" author order"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1283&show=1000"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/pastweek?skip=560&show=2000"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=7575&show=2000"},{"title":"Facile Installation of 2‐Reverse Prenyl Functionality into Indoles ...","url":"https://www.scilit.com/publications/a784feca2366a461b77bd29f35ada2db"},{"title":"[2510.02250] Scaling Agents for Computer Use","url":"https://arxiv.org/abs/2510.02250"},{"title":"Mathematics Feb 2023","url":"https://arxiv.org/list/math/2023-02?skip=1500&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=2650&show=1000"},{"title":"[2511.02864] Mathematical exploration and discovery at scale","url":"https://arxiv.org/abs/2511.02864"},{"title":"[2510.04500] Expand Neurons, Not Parameters","url":"https://arxiv.org/abs/2510.04500"}]

Based on the search results, Vamshi Krishna Bonagiri is the first author of the arXiv paper 2510.16492 titled "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety," and there are 3 other authors on the paper. However, the search result does not provide the complete author list or their full order. To see the complete author list, you would need to visit the full paper on arxiv.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-26T10:26:42.913609+00:00_

Web search results for query: ""Mixture-of-Depths" Raposo ICML 2024 proceedings"

Links: [{"title":"γ−MOD: EXPLORING MIXTURE-OF-DEPTH ADAPTA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf"},{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipedia-mixture-of-depths/"},{"title":"UniMoD: Efficient Unified Multimodal Transformers with Mixture-of-Depths","url":"https://arxiv.org/pdf/2502.06474"},{"title":"Raposo Et Al. - 2024 - Mixture-of-Depths Dynamically Allocating Compute | PDF | Routing | Applied Mathematics","url":"https://www.scribd.com/document/723064609/Raposo-et-al-2024-Mixture-of-Depths-Dynamically-allocating-compute"},{"title":"CNN Mixture-of-Depths Rinor Cakaj 1,2, Jens Mehnert 1, and Bin Yang2","url":"https://openaccess.thecvf.com/content/ACCV2024/papers/Cakaj_CNN_Mixture-of-Depths_ACCV_2024_paper.pdf"},{"title":"[PDF] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mixture-of-Depths:-Dynamically-allocating-compute-Raposo-Ritter/a1f23f04421cdc62e80fe9f04c1ce60f4a6af9f0"},{"title":"VideoLLM-MoD: Efficient Video-Language Streaming with ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language","url":"https://arxiv.org/pdf/2404.02258"}]

Based on the search results, I found information about the "Mixture-of-Depths" paper by Raposo and colleagues. Here are the key findings:

## Publication Status

The Mixture-of-Depths work by Raposo is cited in multiple 2024 papers as "arXiv preprint arXiv:2404.02258, 2024" and appears not to have been formally published at ICML 2024. The paper is titled "Mixture-of-depths: Dynamically allocating compute in transformer-based language mode
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-26T10:26:42.913842+00:00_

I now have all the information needed. Here is the full verification report:

---

### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?
- 真实性：✓
- 作者：✓ (Wang, Ruoyao; Jansen, Peter; Côté, Marc-Alexandre; Ammanabrolu, Prithviraj — all correct)
- 年份：✓ (2022)
- 标题：✓ (exact match)
- Venue：✓ (EMNLP 2022)
- ID：N/A

### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models
- 真实性：✓
- 作者：✓ (Yao, Shunyu; Zhao, Jeffrey; Yu, Dian; Du, Nan; Shafran, Izhak; Narasimhan, Karthik; Cao, Yuan — all correct)
- 年份：✓ (2023)
- 标题：✓ (exact match)
- Venue：✓ (ICLR 2023)
- ID：N/A

### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools
- 真实性：✓
- 作者：✓ (Schick, Timo; Dwivedi-Yu, Jane; Dessì, Roberto; Raileanu, Roberta; Lomeli, Maria; Hambro, Eric; Zettlemoyer, Luke; Cancedda, Nicola; Scialom, Thomas — all correct)
- 年份：✓ (2023)
- 标题：✓ (exact match)
- Venue：✓ (NeurIPS 2023)
- ID：N/A

### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models
- 真实性：✓
- 作者：✓ (Paranjape, Bhargavi; Lundberg, Scott; Singh, Sameer; Hajishirzi, Hannaneh; Zettlemoyer, Luke; Ribeiro, Marco Tulio — all correct)
- 年份：✓ (2023)
- 标题：✗ (arXiv title uses lowercase "multi-step": "ART: Automatic multi-step reasoning and tool-use for large language models". Minor capitalization difference only — not a substantive error, just title casing convention.)
- Venue：✓ (arXiv:2303.09014)
- ID：✓ (2303.09014)

### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models
- 真实性：✓
- 作者：✓ (Lu, Pan; Peng, Baolin; Cheng, Hao; Galley, Michel; Chang, Kai-Wei; Wu, Ying Nian; Zhu, Song-Chun; Gao, Jianfeng — all correct)
- 年份：✓ (2023)
- 标题：✓ (exact match)
- Venue：✓ (NeurIPS 2023)
- ID：N/A

### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs
- 真实性：✓
- 作者：✓ (Feng, Jiazhan; Huang, Shijue; Qu, Xingwei; Zhang, Ge; Qin, Yujia; and others — verified, full list also 
…[truncated 1982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 46
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-26T10:26:42.914080+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mixture-of-Depths\" \"Raposo\" ICML 2024 accepted paper proceedings.mlr.press"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mixture-of-Depths\" \"Raposo\" ICML 2024 accepted paper proceedings.mlr.press"
  }
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:26:42.914255+00:00_

Web search results for query: ""Mixture-of-Depths" "Raposo" ICML 2024 accepted paper proceedings.mlr.press"

Links: [{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipedia-mixture-of-depths/"},{"title":"GitHub - mlresearch/v235: Proceedings of ICML 2024 · GitHub","url":"https://github.com/mlresearch/v235"},{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"Proceedings of Machine Learning Research | Proceedings of the 41st International Conference on Machine Learning Held in Vienna, Austria on 21-27 July 2024 Published as Volume 235 by the Proceedings of Machine Learning Research on 08 July 2024. Volume Edited by: Ruslan Salakhutdinov Zico Kolter Katherine Heller Adrian Weller Nuria Oliver Jonathan Scarlett Felix Berkenkamp Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v235/"},{"title":"ICML 2024 Call for Papers","url":"https://icml.cc/Conferences/2024/CallForPapers"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"Proceedings of Machine Learning Research | Proceedings of the Geometry-grounded Representation Learning and Generative Modeling Workshop (GRaM) Held in Vienna, Asutria on 29 July 2024 Published as Volume 251 by the Proceedings of Machine Learning Research on 12 October 2024. Volume Edited by: Sharvaree Vadgama Erik Bekkers Alison Pouplin Se
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-26T10:26:42.914432+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Check Yourself Before You Wreck Yourself\" \"Khanh Nguyen\" \"Benjamin Plaut\" \"Kumaraguru\" arxiv author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Check Yourself Before You Wreck Yourself\" \"Khanh Nguyen\" \"Benjamin Plaut\" \"Kumaraguru\" arxiv author list"
  }
}
```

</details>

---

### Tool result

_source line 241 · 2026-05-26T10:26:42.914642+00:00_

Now I have all the information. Let me compile the verification report.

Here is the verification report for all 9 entries:

---

### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings
- 真实性：✓
- 作者：✓ (Zhang, Yiqun; Li, Hao; Wang, Zihan; Feng, Shi; Yang, Xiaocui and others — first 5 match, full list is 9 authors including Wang Daling, Zhang Bo, Bai Lei, Hu Shuyue)
- 年份：✓ (2026, arXiv April 2026)
- 标题：✓
- Venue：✓ (ACL 2026 Main Conference)
- ID：N/A (no arXiv ID in entry; actual ID is 2604.23530)

### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?
- 真实性：✓
- 作者：✓ (Zeng, Yirong; You, Shen; Liu, Yufei; Du, Qunyao; Ding, Xiao; Hou, Yutai; Wang, Yuxian; Ning, Wu; Song, Haonan; Tu, Dandan; Cai, Bibo; Liu, Ting — all match)
- 年份：✓ (2026)
- 标题：✓
- Venue：N/A (arXiv preprint, no venue claim)
- ID：✓ (arXiv:2604.19749)

### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning
- 真实性：✓
- 作者：✓ (Sun, Chung-En; Liu, Linbo; Yan, Ge; Wang, Zimo; Weng, Tsui-Wei — all match)
- 年份：✓ (2026, May 2026)
- 标题：✓
- Venue：N/A (arXiv preprint, no venue claim)
- ID：✓ (arXiv:2605.09252)

### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents
- 真实性：✓
- 作者：✓ (Zhang, Kaituo; Xiong, Zhen; Zhong, Mingyu; Jiang, Zhimeng; Yuan, Zhouyuan; Li, Zhecheng; Lin, Ying — all match)
- 年份：✓ (2026, May 2026)
- 标题：✓
- Venue：N/A (arXiv preprint, no venue claim)
- ID：✓ (arXiv:2605.00136)

### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling
- 真实性：✓
- 作者：✓ (Wu, Qinyuan; Das, Soumi; Amani, Mahsa; Nag, Arijit; Lee, Seungeon; Gummadi, Krishna P.; Ravichander, Abhilasha; Zafar, Muhammad Bilal — all match)
- 年份：✓ (2026, May 2026)
- 标题：✓
- Venue：N/A (arXiv preprint, no venue claim)
- ID：✓ (arXiv:2605.00737)

### 15. [dagger-2011] — A Reduction of Imitation Learning and Struc
…[truncated 1626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 46
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-26T10:26:42.914829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:proceedings.mlr.press \"raposo\" \"mixture\" v235"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:proceedings.mlr.press \"raposo\" \"mixture\" v235"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-26T10:26:42.915015+00:00_

Web search results for query: ""Check Yourself Before You Wreck Yourself" "Khanh Nguyen" "Benjamin Plaut" "Kumaraguru" arxiv author list"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492v3"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"(PDF) Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://www.researchgate.net/publication/396714988_Check_Yourself_Before_You_Wreck_Yourself_Selectively_Quitting_Improves_LLM_Agent_Safety"},{"title":"Benjamin Plaut","url":"https://bplaut.github.io/"},{"title":"NeurIPS Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://neurips.cc/virtual/2025/loc/san-diego/125248"},{"title":"Ponnurangam Kumaraguru “PK” on X: \"🎉 New paper accepted to the NeurIPS 2025 “Reliable ML from Unreliable Data” Workshop: “Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety.” 📜 Preprint: https://t.co/bMWbFiER02 https://t.co/vKVz2cmssG\" / X","url":"https://x.com/ponguru/status/1986649704671957348"},{"title":"Check Yourself Before You Wreck Yourself: Selectively","url":"https://openreview.net/pdf/bb9ac95876679983c366254267131d1bf354c8e2.pdf"},{"title":"Benjamin Plaut","url":"https://arxiv.org/search/?searchtype=author&query=Benjamin+Plaut"},{"title":"AI Safety via Generalization and Caution: A Research Agenda — EA Forum","url":"https://forum.effectivealtruism.org/posts/iWKn7BLBeKW9fiPZL/ai-safety-via-generalization-and-caution-a-research-agenda"}]

Based on the search results, I found the paper you're looking for. Here's the autho
…[truncated 696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-26T10:26:42.915205+00:00_

Web search results for query: "site:proceedings.mlr.press "raposo" "mixture" v235"

Links: [{"title":"GitHub - mlresearch/v235: Proceedings of ICML 2024 · GitHub","url":"https://github.com/mlresearch/v235"},{"title":"Scaling Laws for Fine-Grained Mixture of Experts","url":"https://proceedings.mlr.press/v235/ludziejewski24a.html"},{"title":"Convergence of Online Learning Algorithm for a Mixture of Multiple Linear Regressions","url":"https://proceedings.mlr.press/v235/liu24an.html"},{"title":"Merging Multi-Task Models via Weight-Ensembling Mixture of Experts","url":"https://proceedings.mlr.press/v235/tang24e.html"},{"title":"Graph Generation with Diffusion Mixture","url":"https://proceedings.mlr.press/v235/jo24b.html"},{"title":"Theoretical insights for diffusion guidance: A case study for Gaussian mixture models","url":"https://proceedings.mlr.press/v235/wu24b.html"},{"title":"Theoretical Guarantees for Variational Inference with Fixed-Variance Mixture of Gaussians","url":"https://proceedings.mlr.press/v235/huix24a.html"},{"title":"Interpretable Deep Clustering for Tabular Data","url":"https://proceedings.mlr.press/v235/svirsky24a.html"}]

The search results show several papers from Volume 235 of the Proceedings of Machine Learning Research (ICML 2024) that contain the word "mixture," but none of the results specifically mention an author named "raposo." The search did not return papers matching all three criteria (raposo, mixture, and v235) together.

The papers found include works on:
- Scaling Laws for Fine-Grained Mixture of Experts
- Convergence of Online Learning Algorithm for a Mixture of Multiple Linear Regressions
- Merging Multi-Task Models via Weight-Ensembling Mixture of Experts
- Graph Generation with Diffusion Mixture
- Theoretical insights for diffusion guidance: A case study for Gaussian mixture models
- Theoretical Guarantees for Variational Inference with Fixed-Variance Mixture of Gaussians

However, none of these papers appear to have "raposo" as a
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-26T10:26:42.915389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org abs 2510.16492 \"Vamshi Krishna Bonagiri\" \"Ponnurangam Kumaraguru\" \"Khanh Nguyen\" \"Benjamin Plaut\" author order first"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org abs 2510.16492 \"Vamshi Krishna Bonagiri\" \"Ponnurangam Kumaraguru\" \"Khanh Nguyen\" \"Benjamin Plaut\" author order first"
  }
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-26T10:26:42.915543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proceedings.mlr.press raposo24 mixture-of-depths ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proceedings.mlr.press raposo24 mixture-of-depths ICML 2024"
  }
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-26T10:26:42.915705+00:00_

Web search results for query: "proceedings.mlr.press raposo24 mixture-of-depths ICML 2024"

Links: [{"title":"Proceedings of Machine Learning Research | The Proceedings of Machine Learning Research (formerly JMLR Workshop and Conference Proceedings) is a series aimed specifically at publishing machine learning research presented at workshops and conferences. Each volume is separately titled and associated with a particular workshop or conference. Volumes are published online on the PMLR web site. The Series Editors are Neil D. Lawrence and Mark Reid.","url":"https://proceedings.mlr.press/"},{"title":"GitHub - mlresearch/v235: Proceedings of ICML 2024 · GitHub","url":"https://github.com/mlresearch/v235"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"Proceedings of Machine Learning Research | Proceedings of the 41st International Conference on Machine Learning Held in Vienna, Austria on 21-27 July 2024 Published as Volume 235 by the Proceedings of Machine Learning Research on 08 July 2024. Volume Edited by: Ruslan Salakhutdinov Zico Kolter Katherine Heller Adrian Weller Nuria Oliver Jonathan Scarlett Felix Berkenkamp Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v235/"},{"title":"ICLR 2024 TinyPapers | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2024/TinyPapers"},{"title":"Icml","url":"https://icml.cc/media/icml-2024/Slides/35497.pdf"},{"title":"Proceedings of Machine Learning Research vol 247:1–37, 2024","url":"https://proceedings.mlr.press/v247/cohen24c/cohen24c.pdf"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"Downloads 2024","url":"https://icml.cc/Downloads/2024"},{"title":"ICML 2024 Call for Papers","url":"https://icml.cc/Conferences/2024/CallForPapers"}]

The search results show information about ICML 2024 proceedings being published as Volume 235 by the Proceedings of Machine Learning Research, but don't contain specific details about th
…[truncated 3001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-26T10:26:42.915882+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "jmlr.org \"v23/21-0998\" Switch Transformers \"pages 1\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "jmlr.org \"v23/21-0998\" Switch Transformers \"pages 1\""
  }
}
```

</details>

---

### Tool result

_source line 249 · 2026-05-26T10:26:42.916050+00:00_

Web search results for query: "arxiv.org abs 2510.16492 "Vamshi Krishna Bonagiri" "Ponnurangam Kumaraguru" "Khanh Nguyen" "Benjamin Plaut" author order first"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492"},{"title":"Vamshi Krishna Bonagiri","url":"https://scholar.google.com/citations?user=U6p6540AAAAJ&hl=en"},{"title":"dblp: BibTeX records: Ponnurangam Kumaraguru","url":"https://dblp.org/pid/97/5147.html?view=bibtex"},{"title":"Vamshi Krishna Bonagiri","url":"https://victorknox.github.io/"},{"title":"Research, Vamshi Krishna Bonagiri","url":"https://victorknox.github.io/research.html"},{"title":"Vamshi Krishna Bonagiri International Institute of ...","url":"https://www.researchgate.net/profile/Vamshi-Bonagiri"},{"title":"Vamshi Krishna Bonagiri | DeepAI","url":"https://deepai.org/profile/vamshi-krishna-bonagiri"},{"title":"Vamshi Krishna Bonagiri (0000-0002-5537-1664)","url":"https://orcid.org/0000-0002-5537-1664"},{"title":"Vamshi Krishna Bonagiri - - IIIT Blog","url":"https://blogs.iiit.ac.in/monthly_news/vamshi-krishna-bonagiri/"}]

Based on the search results, the author order for arXiv paper 2510.16492 is: Vamshi Krishna Bonagiri, Ponnurangam Kumaraguru, Khanh Nguyen, and Benjamin Plaut.

The paper is titled "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-26T10:26:42.916231+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T10:26:42.916373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-26T10:26:42.916513+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.16492",
  "prompt": "List the exact author names in order as they appear on the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.16492",
    "prompt": "List the exact author names in order as they appear on the paper."
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-26T10:26:42.916666+00:00_

Web search results for query: "jmlr.org "v23/21-0998" Switch Transformers "pages 1""

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/papers/v23/21-0998.html"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://jmlr.org/papers/volume23/21-0998/21-0998.pdf"},{"title":"Journal of Machine Learning Research 23 (2022) 1-40","url":"https://arxiv.org/pdf/2101.03961"},{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"Bluesky","url":"https://bsky.app/intent/compose?text=%22Switch+Transformers%3A+Scaling+to+Trillion+Parameter+Models+with+Simple+and+Efficient+Sparsity.%22+at+#dblphttps://jmlr.org/papers/v23/21-0998.html"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"GitHub - estebancarlin/SwitchTransformer: A Research Implementation of the Switch Transformer Architecture","url":"https://github.com/estebancarlin/SwitchTransformer"},{"title":"Paper page - Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://huggingface.co/papers/2101.03961"},{"title":"ktrain: A Low-Code Library for Augmented Machine Learning","url":"https://jmlr.org/beta/papers/v23/21-1124.html"},{"title":"Review — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-switch-transformers-scaling-to-trillion-parameter-models-with-simple-and-efficient-880edbbf4890"}]

The search successfully found the paper you're looking for. Here are the results:

**Found Document:** The paper "Switch Transformers: Scaling to Trillion Param
…[truncated 792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-26T10:26:42.916828+00:00_

# Author Names

The exact author names in order as they appear on the paper are:

1. Vamshi Krishna Bonagiri
2. Ponnurangam Kumaragurum
3. Khanh Nguyen
4. Benjamin Plaut

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 255 · 2026-05-26T10:26:42.916975+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AutoMix arxiv 2310.12963 authors \"Prakhar Anand\" OR \"Ankit Anand\" \"Srividya\" \"Swaroop\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AutoMix arxiv 2310.12963 authors \"Prakhar Anand\" OR \"Ankit Anand\" \"Srividya\" \"Swaroop\""
  }
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-26T10:26:42.917150+00:00_

Web search results for query: "AutoMix arxiv 2310.12963 authors "Prakhar Anand" OR "Ankit Anand" "Srividya" "Swaroop""

Links: [{"title":"[2310.12963] AutoMix: Automatically Mixing Language Models","url":"https://arxiv.org/abs/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models Pranjal Aggarwal♢∗ Aman Madaan♣∗","url":"https://arxiv.org/pdf/2310.12963"},{"title":"Paper page - AutoMix: Automatically Mixing Language Models","url":"https://huggingface.co/papers/2310.12963"},{"title":"AutoMix: Automatically Mixing Language Models","url":"https://automix-llm.github.io/automix/"},{"title":"automix/docs/index.html at main · automix-llm/automix","url":"https://github.com/automix-llm/automix/blob/main/docs/index.html"},{"title":"[PDF] AutoMix: Automatically Mixing Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AutoMix:-Automatically-Mixing-Language-Models-Madaan-Aggarwal/f0ed191bdcbd56610ab4d95c5a80d5ac31ffc074"},{"title":"Computation and Language authors/titles ... - APS arXiv Mirror","url":"https://aps.arxiv.org/list/cs.CL/recent"},{"title":"AutoMix: Automatically Mixing Language Models Aman Madaan♠∗ Pranjal Aggarwal♢∗","url":"https://arxiv.org/pdf/2310.12963v3"}]

Based on the search results, I found the paper "AutoMix: Automatically Mixing Language Models" with arxiv ID 2310.12963. 

The authors of this paper are: Pranjal Aggarwal, Aman Madaan, Ankit Anand, Srividya Pranavi Potharaju, Swaroop Mishra, Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam.

The paper includes the authors you mentioned:
- **Ankit Anand** ✓ (not "Prakhar Anand")
- **Srividya** (Srividya Pranavi Potharaju) ✓
- **Swaroop** (Swaroop Mishra) ✓

Note that the paper does not have an author named "Prakhar Anand" - it includes "Ankit Anand" instead. AutoMix is an approach that strategically routes queries to larger LMs, based on the approximate correctness of outputs from a smaller LM.
…[truncated 103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-26T10:26:42.917330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Bettina Könighofer\" OR \"Bettina Koenighofer\" safe reinforcement learning shielding AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Bettina Könighofer\" OR \"Bettina Koenighofer\" safe reinforcement learning shielding AAAI"
  }
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-26T10:26:42.917531+00:00_

Now I have all the information needed. The author order on arXiv is: Bonagiri, Kumaraguru, Nguyen, Plaut — but the bib entry lists them as: Bonagiri, Nguyen, Plaut, Kumaraguru. The order is different.

Let me also verify the Semantic Scholar entry for entry 64 to confirm author list completeness.

Here are my findings for all 7 entries:

---

### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety
- 真实性：✓
- 作者：✗ (bib entry 列出顺序为 Bonagiri, Nguyen, Plaut, Kumaraguru，但 arXiv 上的实际作者顺序为 Bonagiri, Kumaraguru, Nguyen, Plaut)
- 年份：✓ (2025)
- 标题：✓
- Venue：✓ (arXiv:2510.16492)
- ID：✓ (2510.16492)

### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models
- 真实性：✓
- 作者：✓ (Potsawee Manakul, Adian Liusie, Mark J. F. Gales)
- 年份：✓ (2023)
- 标题：✓
- Venue：✓ (EMNLP 2023, ACL Anthology确认: 2023.emnlp-main.557)
- ID：N/A

### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know
- 真实性：✓
- 作者：✓ (Saurav Kadavath 等36位共同作者，与 bib entry 一致)
- 年份：✓ (2022)
- 标题：✓
- Venue：✓ (arXiv:2207.05221)
- ID：✓ (2207.05221)

### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference
- 真实性：✓
- 作者：✓ (Ji Xin, Raphael Tang, Jaejun Lee, Yaoliang Yu, Jimmy Lin)
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (ACL 2020, ACL Anthology确认: 2020.acl-main.204)
- ID：N/A

### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit
- 真实性：✓
- 作者：✓ (Wangchunshu Zhou, Canwen Xu, Tao Ge, Julian McAuley, Ke Xu, Furu Wei)
- 年份：✓ (2020)
- 标题：✓
- Venue：✓ (NeurIPS 2020, vol 33)
- ID：N/A

### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach
- 真实性：✓
- 作者：✓ (Yinlam Chow, Aviv Tamar, Shie Mannor, Marco Pavone)
- 年份：✓ (2015)
- 标题：✓
- Venue：✓ (NeurIPS 2015, vol 28)
- ID：N/A

### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling
- 真实性：✓
- 作者：✓ (Aviv Tamar, Yonatan Glassner, Shie Mannor)

…[truncated 414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-26T10:26:42.917716+00:00_

Web search results for query: ""Bettina Könighofer" OR "Bettina Koenighofer" safe reinforcement learning shielding AAAI"

Links: [{"title":"Safe Reinforcement Learning via Shielding | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/11797"},{"title":"Safe Reinforcement Learning via Shielding - AAAI","url":"https://aaai.org/papers/11797-safe-reinforcement-learning-via-shielding/"},{"title":"Safe Reinforcement Learning via Shielding","url":"https://cdn.aaai.org/ojs/11797/11797-13-15325-1-2-20201228.pdf"},{"title":"Safe Reinforcement Learning Using Probabilistic Shields (Invited Paper)","url":"https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CONCUR.2020.3"},{"title":"Safe Reinforcement Learning via Shielding - Graz University of Technology","url":"https://tugraz.elsevierpure.com/en/publications/safe-reinforcement-learning-via-shielding/"},{"title":"Bettina Könighofer – ISEC","url":"https://www.isec.tugraz.at/person/bettina-koenighofer/"},{"title":"Safe Reinforcement Learning via Shielding under Partial Observability","url":"https://repository.ubn.ru.nl/bitstream/handle/2066/294801/294801pre.pdf?sequence=2&isAllowed=y"},{"title":"Synthesizing Efficient and Permissive Programmatic Runtime Shields for Neural Policies | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3773034"},{"title":"Safe reinforcement learning via shielding | Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence and Thirtieth Innovative Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.5555/3504035.3504361"},{"title":"dblp: Safe Reinforcement Learning via Shielding.","url":"https://dblp.org/rec/conf/aaai/AlshiekhBEKNT18.html"}]

I found relevant information about Bettina Könighofer's work on safe reinforcement learning via shielding at AAAI. Her
…[truncated 1165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-26T10:26:42.917950+00:00_

Good - the AAAI proceedings confirm the author name is "Bettina Könighofer" (not "Königshofer" as the Google Books result had listed). Now I have all the information needed to compile the verification report.

Here are the verification results for all 8 entries:

---

### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✗ (pages should be 1-40, not 1-39. The JMLR PDF header explicitly states "Journal of Machine Learning Research 23 (2022) 1-40")
- ID：N/A

### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- ID：N/A

### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- ID：N/A

### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓
- ID：N/A

### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance
- 真实性：✓
- 作者：✓
- 年份：✓
- 标题：✓
- Venue：✓ (arXiv preprint, ID matches)
- ID：✓ (arXiv:2305.05176)

### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models
- 真实性：✓
- 作者：✗ (The bib entry lists only 6 authors: "Madaan, Aman and Aggarwal, Pranjal and Anand, Prakhar and Potdar, Srividya and Gupta, Swaroop and Tandon, Niket". The actual NeurIPS 2024 paper has 13 authors: Pranjal Aggarwal, Aman Madaan, Ankit Anand (not "Prakhar"), Srividya Pranavi Potharaju (not "Potdar"), Swaroop Mishra (not "Gupta"), Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, and Mausam. Multiple author names are wrong and 7 authors are missing entirely.)
- 年份：✓
- 标题：✓
- Venue：✓
- ID：N/A

### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- 真实性：✓
- 作者
…[truncated 1675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Agent",
  "elapsed_ms": 40
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-26T10:26:42.918191+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-26T10:26:42.918365+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 263 · 2026-05-26T10:26:42.918528+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 264 · 2026-05-26T10:26:42.918694+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 265 · 2026-05-26T10:26:42.918859+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-26T10:26:42.919080+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 267 · 2026-05-26T10:26:42.919251+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 268 · 2026-05-26T10:26:42.919495+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-26T10:26:42.919665+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-26T10:26:42.919838+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-26T10:26:42.920024+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-26T10:26:42.920178+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 273 · 2026-05-26T10:26:42.920340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 274 · 2026-05-26T10:26:42.920896+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}  % optional per ACL template; not available in this TeX installation
11	\usepackage{graphicx}
12	\graphicspath{{figures/}}
13	\usepackage{booktabs}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{algorithm}
17	\usepackage{algorithmic}
18	\usepackage{caption}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{listings,breakable}
21	
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 2pt}
23	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
24	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
25	
26	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	Full quantitative validation (DAF, label fractions) is specific to ScienceWorld; MATH and ALFWorld serve as boundary probes, not comprehensive cross-environment validation. DAF depends on a fixed death penalty ($P{=}100$); environments with graded or stochastic failure severity would require extensions (Appendix~\ref{app:penalty}). The internal baseline uses single-pass ReAct~\citep{react-2023}; more aggressive self-correction (e.g., Tree-of-Thought) may further reduce death rates and alter the signal composition. With $K{=}11$ task-type clusters, cluster bootstrap yields wider CIs; wild cluster bootstrap ($p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks provide partial mitigation. Total compute was approximately 200 GPU-hours on consumer and workstation GPUs.
43	
44	\bibliography{references}
45	
46	\appendix
47	
48	\noindent\textbf{Appendix O
…[truncated 61068 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 275 · 2026-05-26T10:26:42.921181+00:00_

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
  "session": "worker_research_ref-audit-B_20260526T101527",
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

_source line 276 · 2026-05-26T10:26:42.921335+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 277 · 2026-05-26T10:26:42.921534+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md",
  "content": "# Reference Audit — Worker B\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：58\n- ✗ 发现问题：10\n\n### 严重问题（作者错误/缺失）\n| # | cite_key | 问题 |\n|---|----------|------|\n| 19 | amitai2024explaining | 第二作者 \"Guy Septon\" 应为 \"Yael Septon\" |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n| 33 | toolace-2025 | 第一作者 \"Zhang, Weiwen\" 应为 \"Liu, Weiwen\" |\n| 46 | salt-2026 | 作者 \"David Yan\" 应为 \"Qiaojing Yan\" |\n| 51 | agent-safetybench-2024 | 多个作者名错误，含两个不存在的作者 |\n| 59 | automix-2024 | 严重作者列表错误：多个名字错误，缺少7位共同作者 |\n\n### 轻微问题\n| # | cite_key | 问题 |\n|---|----------|------|\n| 15 | dagger-2011 | 作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\" |\n| 54 | switch-transformer-2022 | 页码 1-39 应为 1-40 |\n| 62 | bonagiri2025check | 作者顺序错误（bib: Bonagiri/Nguyen/Plaut/Kumaraguru → arXiv: Bonagiri/Kumaraguru/Nguyen/Plaut） |\n\n### Cite Key 不一致\n| # | cite_key | 问题 |\n|---|----------|------|\n| 45 | axis-2026 | cite key 标 2026，但 year 字段和 arXiv 提交日期均为 2025 |\n\n## 正文引用上下文核查\n所有 \\cite{} 引用在正文中的使用均与被引论文的实际内容一致，未发现张冠李戴的引用错误。\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (BibTeX title casing vs arXiv lowercase — 非实质性差异)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✗ (第三作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\"。\"Drew\" 是常用昵称但非 AISTATS 论文集的正式署名)\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✗ (第二作者 \"Guy Septon\" 应为 **\"Yael Septon\"**)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓ (AAMAS 2023 Doctoral Consortium 论文)\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (AAMAS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2406.18665)\n- ID：✓\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（在 Limitations 中提及）\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (Review of Economics and Statistics, vol 90, no 3, pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ (第一作者 \"Zhang, Weiwen\" 应为 **\"Liu, Weiwen\"**（Weiwen Liu）。完整作者列表由 27 位作者组成，以 Weiwen Liu 为首)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56, no 3)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024, Spotlight)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓ (bib 用 \"and others\" 省略，首作者 Lee, Seanie 正确)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2506.02946)\n- ID：✓\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (bib year 字段为 2025，正确；但 cite key \"axis-2026\" 暗示 2026，不一致)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n- 备注：cite key 与实际年份不一致（key 写 2026，实际为 2025）\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ (第三作者 \"David Yan\" 应为 **\"Qiaojing Yan\"**，ACL Anthology 确认)\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 9 位作者，但实际论文仅有 7 位。具体问题：(1) \"Yang Junhao\" 应为 **\"Yang Junxiao\"**；(2) \"Wang Renhao\" 应为 **\"Wang Hongning\"**；(3) \"Liu Jie\" 和 \"Li Jiangjie\" 在实际论文中不存在，为虚构作者。正确的完整作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd edition)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66, no 5)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✗ (页码错误：bib 写 pages={1--39}，JMLR 论文实际为 **1--40**)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 6 位作者，但 NeurIPS 2024 论文实际有 13 位作者。具体问题：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 不在论文作者列表中；(5) 缺少 7 位共同作者：Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✗ (作者顺序错误。bib: Bonagiri, Nguyen, Plaut, Kumaraguru → arXiv 实际顺序: **Bonagiri, Kumaraguru, Nguyen, Plaut**)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md",
    "content": "# Reference Audit — Worker B\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：58\n- ✗ 发现问题：10\n\n### 严重问题（作者错误/缺失）\n| # | cite_key | 问题 |\n|---|----------|------|\n| 19 | amitai2024explaining | 第二作者 \"Guy Septon\" 应为 \"Yael Septon\" |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n| 33 | toolace-2025 | 第一作者 \"Zhang, Weiwen\" 应为 \"Liu, Weiwen\" |\n| 46 | salt-2026 | 作者 \"David Yan\" 应为 \"Qiaojing Yan\" |\n| 51 | agent-safetybench-2024 | 多个作者名错误，含两个不存在的作者 |\n| 59 | automix-2024 | 严重作者列表错误：多个名字错误，缺少7位共同作者 |\n\n### 轻微问题\n| # | cite_key | 问题 |\n|---|----------|------|\n| 15 | dagger-2011 | 作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\" |\n| 54 | switch-transformer-2022 | 页码 1-39 应为 1-40 |\n| 62 | bonagiri2025check | 作者顺序错误（bib: Bonagiri/Nguyen/Plaut/Kumaraguru → arXiv: Bonagiri/Kumaraguru/Nguyen/Plaut） |\n\n### Cite Key 不一致\n| # | cite_key | 问题 |\n|---|----------|------|\n| 45 | axis-2026 | cite key 标 2026，但 year 字段和 arXiv 提交日期均为 2025 |\n\n## 正文引用上下文核查\n所有 \\cite{} 引用在正文中的使用均与被引论文的实际内容一致，未发现张冠李戴的引用错误。\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (BibTeX title casing vs arXiv lowercase — 非实质性差异)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✗ (第三作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\"。\"Drew\" 是常用昵称但非 AISTATS 论文集的正式署名)\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✗ (第二作者 \"Guy Septon\" 应为 **\"Yael Septon\"**)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓ (AAMAS 2023 Doctoral Consortium 论文)\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (AAMAS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2406.18665)\n- ID：✓\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（在 Limitations 中提及）\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (Review of Economics and Statistics, vol 90, no 3, pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ (第一作者 \"Zhang, Weiwen\" 应为 **\"Liu, Weiwen\"**（Weiwen Liu）。完整作者列表由 27 位作者组成，以 Weiwen Liu 为首)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56, no 3)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024, Spotlight)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓ (bib 用 \"and others\" 省略，首作者 Lee, Seanie 正确)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2506.02946)\n- ID：✓\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (bib year 字段为 2025，正确；但 cite key \"axis-2026\" 暗示 2026，不一致)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n- 备注：cite key 与实际年份不一致（key 写 2026，实际为 2025）\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ (第三作者 \"David Yan\" 应为 **\"Qiaojing Yan\"**，ACL Anthology 确认)\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 9 位作者，但实际论文仅有 7 位。具体问题：(1) \"Yang Junhao\" 应为 **\"Yang Junxiao\"**；(2) \"Wang Renhao\" 应为 **\"Wang Hongning\"**；(3) \"Liu Jie\" 和 \"Li Jiangjie\" 在实际论文中不存在，为虚构作者。正确的完整作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd edition)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66, no 5)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✗ (页码错误：bib 写 pages={1--39}，JMLR 论文实际为 **1--40**)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 6 位作者，但 NeurIPS 2024 论文实际有 13 位作者。具体问题：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 不在论文作者列表中；(5) 缺少 7 位共同作者：Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✗ (作者顺序错误。bib: Bonagiri, Nguyen, Plaut, Kumaraguru → arXiv 实际顺序: **Bonagiri, Kumaraguru, Nguyen, Plaut**)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n"
  }
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-26T10:26:42.921940+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-B_20260526T101527",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 279 · 2026-05-26T10:26:42.922166+00:00_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_B.md`。

68 条引用中发现 10 个问题：

**严重（需修复）：**
- `toolace-2025`: 第一作者姓错误 (Zhang → **Liu**)
- `agent-safetybench-2024`: 多个作者名错误 + 2 个虚构作者
- `automix-2024`: 多个作者名错误 + 缺少 7 位共同作者
- `amitai2024explaining`: 第二作者名错误 (Guy → **Yael** Septon)
- `reflexion-2023`: 缺少作者 Edward Berman
- `salt-2026`: 第三作者名错误 (David → **Qiaojing** Yan)

**轻微：**
- `dagger-2011`: 作者昵称 vs 正式名 (Drew → J. Andrew Bagnell)
- `switch-transformer-2022`: 页码 1-39 → 1-40
- `bonagiri2025check`: 作者顺序与 arXiv 不一致
- `axis-2026`: cite key 标 2026 但实际年份为 2025

**无 hallucinated paper**，所有 68 篇论文均真实存在。正文引用上下文全部正确，未发现张冠李戴。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-B_20260526T101527"
}
```

</details>

---
