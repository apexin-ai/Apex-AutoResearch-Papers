# audit reference

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_audit_reference_20260515T212521.jsonl`
- **Structured JSON:** [`76fded7f5701b67add57.json`](../../sessions/76/76fded7f5701b67add57.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

22 recorded events

### Tool call

_source line 1 · 2026-05-15T21:28:18.514770+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__verify_references",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T21:28:18.515294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T21:28:18.515560+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
  "project": "solver-trace-ablation",
  "skip_online": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper",
    "project": "solver-trace-ablation",
    "skip_online": "False"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T21:28:18.518566+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 30, \"total_citations\": 54, \"unique_cited_keys\": 30, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 18, \"online_not_found\": 7, \"online_mismatch\": 5}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"deepseekmath\", \"type\": \"article\", \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\", \"authors\": \"Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.03300\"}, {\"key\": \"logic-rl\", \"type\": \"article\", \"title\": \"Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning\", \"authors\": \"Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Brya...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2502.14768\"}, {\"key\": \"mellgren-prolog-grpo\", \"type\": \"article\", \"title\": \"Training Language Models to Use Prolog as a Tool\", \"authors\": \"Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2512.07407\"}, {\"key\": \"satlm\", \"type\": \"inproceedings\", \"title\": \"SatLM: Satisfiability-Aided Language Models Using Declarative Prompting\", \"authors\": \"Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems (NeurIPS)\"}, {\"key\": \"lightman-verify-step\", \"type\": \"inproceedings\", \"title\": \"Let's Verify Step by Step\", \"authors\": \"Hunter Lightman and Vineet Kosaraju and Yura Burda and others\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations (ICLR)\"}, {\"key\": \"skalse-reward-hacking\", \"type\": \"inproceedings\", \"title\": \"Defining and Characterizing Reward H
…[truncated 23158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T21:28:18.519057+00:00_

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
  "session": "worker_audit_reference_20260515T212521",
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

_source line 6 · 2026-05-15T21:28:18.519367+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T21:28:18.519606+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeekMath Pushing Limits Mathematical Reasoning arXiv 2402.03300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeekMath Pushing Limits Mathematical Reasoning arXiv 2402.03300"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T21:28:18.521914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T21:28:18.522199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Karwowski \"Goodhart's Law in Reinforcement Learning\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Karwowski \"Goodhart's Law in Reinforcement Learning\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T21:28:18.522417+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Manheim Garrabrant \"Categorizing Variants of Goodhart's Law\" arXiv 1803.04585"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Manheim Garrabrant \"Categorizing Variants of Goodhart's Law\" arXiv 1803.04585"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T21:28:18.522600+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Reinforcement Learning via Symbolic Feedback\" Jha Murty arXiv 2405.16661"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Reinforcement Learning via Symbolic Feedback\" Jha Murty arXiv 2405.16661"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T21:28:18.522826+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rubric-Grounded Reinforcement Learning\" arXiv 2605.08061"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rubric-Grounded Reinforcement Learning\" arXiv 2605.08061"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T21:28:18.523043+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "METR \"Recent Frontier Models Are Reward Hacking\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "tool_args": {
    "query": "METR \"Recent Frontier Models Are Reward Hacking\" 2025"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T21:28:18.523311+00:00_

Web search results for query: "Lightman "Let's Verify Step by Step" ICLR 2024"

Links: [{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"Let's Verify Step by Step","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html"},{"title":"dblp: Let's Verify Step by Step.","url":"https://dblp.org/rec/conf/iclr/LightmanKBEBLLS24.html"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"},{"title":"Figure 2 from Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/2"},{"title":"GitHub - kyegomez/Lets-Verify-Step-by-Step: \"Improving Mathematical Reasoning with Process Supervision\" by OPENAI · GitHub","url":"https://github.com/kyegomez/Lets-Verify-Step-by-Step"},{"title":"Let's Verify Step by Step","url":"https://www.connectedpapers.com/main/be8db99310602d66bba64bcf41a572c45816fbfc/Let's-Verify-Step-by-Step/graph"},{"title":"ICLR Poster Let's Verify Step by Step","url":"https://iclr.cc/virtual/2024/poster/17549"}]

Based on the search results, here's what I found about the paper "Let's Verify Step by Step":

## Paper Overview

"Let's Verify Step by Step" was authored by Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe, and was published at ICLR 2024.

## Key Findings

The paper addresses how large language models have greatly improved in their ability to perform complex multi-ste
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T21:28:18.523613+00:00_

Web search results for query: "DeepSeekMath Pushing Limits Mathematical Reasoning arXiv 2402.03300"

Links: [{"title":"[2402.03300] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/abs/2402.03300"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical","url":"https://arxiv.org/pdf/2402.03300"},{"title":"GitHub - deepseek-ai/DeepSeek-Math: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Math"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/html/2402.03300v3"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/deepseekmath-pushing-the-limits-of-mathematical-reasoning-in-open-language-models-f2665df4019e"},{"title":"Paper page - DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://huggingface.co/papers/2402.03300"},{"title":"[2402.03300v3] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/abs/2402.03300v3"},{"title":"DeepSeekMath: Advancing Math Reasoning","url":"https://www.emergentmind.com/papers/2402.03300"},{"title":"[2402.03300v2] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/abs/2402.03300v2"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models, Zhihong Shao+, arXiv'24 · Issue #1655 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1655"}]

Based on the search results, here's information about the paper "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models" (arXiv 2402.03300):

## Overview
The paper addresses mathematical reasoning, 
…[truncated 1456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T21:28:18.523945+00:00_

Web search results for query: ""Reinforcement Learning via Symbolic Feedback" Jha Murty arXiv 2405.16661"

Links: [{"title":"[2405.16661] RLSF: Fine-tuning LLMs via Symbolic Feedback","url":"https://arxiv.org/abs/2405.16661"},{"title":"[2405.16661v2] RLSF: Reinforcement Learning via Symbolic Feedback","url":"https://arxiv.org/abs/2405.16661v2"},{"title":"RLSF: Reinforcement Learning via Symbolic Feedback","url":"https://arxiv.org/html/2405.16661v1"},{"title":"(PDF) RLSF: Reinforcement Learning via Symbolic Feedback","url":"https://www.researchgate.net/publication/380907103_RLSF_Reinforcement_Learning_via_Symbolic_Feedback"},{"title":"RLSF: Fine-tuning LLMs via Symbolic Feedback - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240516661J/abstract"},{"title":"RLSF: Reinforcement Learning via Symbolic Feedback | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/rlsf-reinforcement-learning-via-symbolic-feedback"},{"title":"RLSF: Fine-tuning LLMs via Symbolic Feedback","url":"https://arxiv.org/html/2405.16661"},{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2508.13678v1"},{"title":"RLSF: Reinforcement Learning via Symbolic Feedback | PromptLayer","url":"https://www.promptlayer.com/research-papers/rlsf-reinforcement-learning-via-symbolic-feedback"},{"title":"RLSF: Reinforcement Learning via Symbolic Feedback | OpenReview","url":"https://openreview.net/forum?id=vf8iou7FNF"}]

I found the paper you were looking for. Here's what I found:

## RLSF: Reinforcement Learning via Symbolic Feedback

The paper introduces Reinforcement Learning via Symbolic Feedback (RLSF), a novel fine-tuning paradigm where symbolic reasoning tools (e.g., solvers, provers, and algebra systems) provide fine-grained feedback to LLMs.

**Key Details:**
- **Authors:** Piyush Jha, Prithwish Jana, Pranavkrishna Suresh, Arnav Arora, and Vijay Ganesh
- **arXiv ID:** 2405.16661
-
…[truncated 870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T21:28:18.524260+00:00_

Web search results for query: "Manheim Garrabrant "Categorizing Variants of Goodhart's Law" arXiv 1803.04585"

Links: [{"title":"[1803.04585] Categorizing Variants of Goodhart's Law","url":"https://arxiv.org/abs/1803.04585"},{"title":"Categorizing Variants of Goodhart's Law","url":"https://arxiv.org/pdf/1803.04585"},{"title":"(PDF) Categorizing Variants of Goodhart's Law","url":"https://www.researchgate.net/publication/323747167_Categorizing_Variants_of_Goodhart's_Law"},{"title":"Categorizing Variants of Goodhart's Law - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv180304585M/abstract"},{"title":"[1803.04585v3] Categorizing Variants of Goodhart's Law","url":"https://arxiv.org/abs/1803.04585v3"},{"title":"[1803.04585v1] Categorizing Variants of Goodhart's Law","url":"https://arxiv.org/abs/1803.04585v1"},{"title":"[PDF] Categorizing Variants of Goodhart's Law | Semantic Scholar","url":"https://www.semanticscholar.org/paper/80939dd8a5cad405053c88ed856c28791bdc0582"},{"title":"David Manheim | IDEAS/RePEc","url":"https://ideas.repec.org/f/pma2620.html"},{"title":"dblp: Categorizing Variants of Goodhart's Law.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-1803-04585.html"},{"title":"Goodhart’s Law and the Death of Honest Metrics | by Claus Rainer Anton Nisslmüller | Medium","url":"https://medium.com/@claus.nisslmueller/goodharts-law-and-the-death-of-honest-metrics-e08cc756f93a"}]

I found the paper for you. "Categorizing Variants of Goodhart's Law" is by David Manheim and Scott Garrabrant.

The paper addresses failure modes that occur when a metric which can be used to improve a system is used to an extent that further optimization is ineffective or harmful, a phenomenon sometimes termed Goodhart's Law. The paper expands on an earlier discussion by Garrabrant which notes there are "(at least) four different mechanisms" that relate to Goodhart's Law, and explores these mechanisms further, specifying more clearly how they occur.

This discussion is inten
…[truncated 429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T21:28:18.524564+00:00_

Web search results for query: "Karwowski "Goodhart's Law in Reinforcement Learning" ICLR 2024"

Links: [{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.lesswrong.com/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"ICLR Poster Goodhart's Law in Reinforcement Learning","url":"https://iclr.cc/virtual/2024/poster/19413"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.semanticscholar.org/paper/Goodhart's-Law-in-Reinforcement-Learning-Karwowski-Hayman/a4bd4da02241eacee990c89ddd748ce37a248fc0"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"Goodhart's Law in Reinforcement Learning - LessWrong 2.0 viewer","url":"https://www.greaterwrong.com/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Rethinking Reward Model Evaluation: Are We Barking up the Wrong Tree?","url":"https://arxiv.org/html/2410.05584v5"}]

I found the paper! Here are the key details about Karwowski's "Goodhart's Law in Reinforcement Learning" at ICLR 2024:

**Paper Information:**
The paper was published as a conference paper at ICLR 2024 by Jacek Karwowski from the University of Oxford, along with co-authors Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, and Joar Skalse.

**Main Contribution:**
The paper addresses the problem that implementing a reward function that perfectly captures a complex task in the real world is impractical, so the reward 
…[truncated 915 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T21:28:18.524896+00:00_

Web search results for query: "METR "Recent Frontier Models Are Reward Hacking" 2025"

Links: [{"title":"Recent Frontier Models Are Reward Hacking - METR","url":"https://metr.org/blog/2025-06-05-recent-reward-hacking/"},{"title":"Recent Frontier Models Are Reward Hacking - METR","url":"https://metr.substack.com/p/2025-06-05-recent-reward-hacking"},{"title":"METR: Recent frontier models are reward hacking","url":"https://www.lesswrong.com/posts/Zu4ai9GFpwezyfB2K/metr-recent-frontier-models-are-reward-hacking"},{"title":"METR: Recent frontier models are reward hacking - LessWrong 2.0 viewer","url":"https://www.greaterwrong.com/posts/Zu4ai9GFpwezyfB2K/metr-recent-frontier-models-are-reward-hacking"},{"title":"Recent Frontier Models are Reward Hacking","url":"https://www.linkedin.com/pulse/recent-frontier-models-reward-hacking-metr-evals-u12qc"},{"title":"METR: Recent frontier models are reward hacking - X","url":"https://x.com/jreuben1/status/1932241852029362200"},{"title":"Reward Hacking: How AI Exploits the Goals We Give It - Americans for Responsible Innovation","url":"https://ari.us/policy-bytes/reward-hacking-how-ai-exploits-the-goals-we-give-it/"},{"title":"Recent Frontier Models Are Reward Hacking | Hacker News","url":"https://news.ycombinator.com/item?id=44237307"}]

I found the METR research paper you were looking for. Here are the key findings:

## Overview

METR recently documented increasingly clear examples of reward hacking where AI systems try to "cheat" and get impossibly high scores. They do this by exploiting bugs in scoring code or subverting the task setup, rather than actually solving the problem.

## Key Findings

In o3 pre-deployment evaluations, the model reward-hacked in 0.7% of runs across HCAST tasks, but on one specific RE-Bench task, o3 eventually reward-hacked in every single trajectory generated. Reward hacking was more than 43× more common on RE-Bench tasks than HCAST tasks.

Similar behaviors have been noticed for other recent models, s
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T21:28:18.525207+00:00_

Web search results for query: ""Rubric-Grounded Reinforcement Learning" arXiv 2605.08061"

Links: [{"title":"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models","url":"https://arxiv.org/html/2605.08061v1"},{"title":"[2605.08061v1] Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning","url":"https://arxiv.org/abs/2605.08061v1"},{"title":"Paper page - Reinforcement Learning with Rubric Anchors","url":"https://huggingface.co/papers/2508.12790"},{"title":"RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards","url":"https://arxiv.org/html/2605.10899v1"},{"title":"Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains","url":"https://arxiv.org/html/2507.17746v2"},{"title":"Reinforcement Learning with Rubric Anchors","url":"https://www.alphaxiv.org/abs/2508.12790"},{"title":"[2605.10899v1] RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards","url":"https://arxiv.org/abs/2605.10899v1"},{"title":"[2508.12790] Reinforcement Learning with Rubric Anchors","url":"https://arxiv.org/abs/2508.12790"},{"title":"Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning","url":"https://arxiv.org/html/2508.16949v3"},{"title":"RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation","url":"https://arxiv.org/html/2601.08430"}]

I found detailed information about the paper "Rubric-Grounded Reinforcement Learning" with arXiv ID 2605.08061. Here's what I found:

## Overview

The paper formalizes rubric-grounded reinforcement learning (RL): a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the policy never sees.

## Key Approach

The framework decomposes reward into weighted, verifiable criteria and uses an LLM judge to score them, 
…[truncated 1360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T21:28:18.525564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T21:28:18.525932+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 11165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_reference_20260515T212521",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---
