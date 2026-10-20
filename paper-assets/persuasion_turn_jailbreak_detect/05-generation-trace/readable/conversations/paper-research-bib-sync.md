# paper research bib sync

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_research_bib_sync_20260518T035730.jsonl`
- **Structured JSON:** [`deb92b87bbf85c2c6f45.json`](../../sessions/de/deb92b87bbf85c2c6f45.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-18T03:59:28.324495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T03:59:28.325207+00:00_

1	# Literature Map — persuasion_turn_jailbreak_detect
2	# Generated: 2026-05-17 by Paper Agent
3	# Target: EMNLP 2026 Main (ARR May cycle)
4	# Total entries: 39 (across 8 categories + technical foundation)
5	# All entries WebSearch-verified
6	
7	metadata:
8	  project: persuasion_turn_jailbreak_detect
9	  target_venue: EMNLP 2026
10	  last_updated: "2026-05-17"
11	  total_papers: 39
12	  categories:
13	    - production_safety_systems
14	    - multi_turn_defenses
15	    - discourse_analysis
16	    - computational_persuasion
17	    - jailbreak_attacks_taxonomies
18	    - red_teaming
19	    - annotation_artifacts
20	    - adaptive_attacks
21	    - technical_foundation
22	
23	papers:
24	
25	  # ============================================================
26	  # Category 1: Production Multi-Turn Safety Systems (5 papers)
27	  # ============================================================
28	
29	  - bibtex_key: inan2023llamaguard
30	    title: "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations"
31	    authors: "Inan et al."
32	    venue: "arXiv preprint"
33	    year: 2023
34	    arxiv: "2312.06674"
35	    category: production_safety_systems
36	    role: background
37	    verified: true
38	    relevance_to_our_work: >
39	      Foundational production safety classifier. Per-turn input/output guard
40	      that lacks multi-turn context modeling. DisPeD addresses this gap by
41	      modeling conversation-level persuasion trajectories.
42	
43	  - bibtex_key: metallamaguard3_2024
44	    title: "Llama Guard 3"
45	    authors: "Meta AI"
46	    venue: "Meta AI (released with Llama 3.1)"
47	    year: 2024
48	    category: production_safety_systems
49	    role: background
50	    verified: true
51	    relevance_to_our_work: >
52	      Latest iteration of Llama Guard with multilingual support and tool-use
53	      safety. Still operates per-turn without multi-turn trajectory modeling.
54	      Baseline comparison target for production safety systems.
55	
56	  -
…[truncated 24580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T03:59:28.325466+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Glob",
  "tool_args": {
    "pattern": "paper/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T03:59:28.325688+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T03:59:28.325844+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T03:59:28.325996+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
registry.lock
registry.yaml
report.md
scripts
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T03:59:28.326141+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T03:59:28.326290+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T03:59:28.326522+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
  "content": "% References for persuasion_turn_jailbreak_detect\n% Auto-generated from literature_map.yaml (2026-05-18)\n% Total entries: 39\n\n% ============================================================\n% Category 1: Production Multi-Turn Safety Systems\n% ============================================================\n\n@article{inan2023llamaguard,\n  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},\n  author={Inan and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2312.06674},\n  archivePrefix={arXiv},\n}\n\n@misc{metallamaguard3_2024,\n  title={Llama Guard 3},\n  author={{Meta AI}},\n  year={2024},\n  howpublished={Meta AI (released with Llama 3.1)},\n}\n\n@article{zeng2024shieldgemma,\n  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},\n  author={Zeng and others},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2407.21772},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{han2024wildguard,\n  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},\n  author={Han and others},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{anthropic2025constitutional,\n  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},\n  author={{Anthropic}},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2501.18837},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 2: Multi-Turn Jailbreak Defenses\n% ============================================================\n\n@article{deepcontext2026,\n  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2602.16935},\n  archivePrefix={arXiv},\n}\n\n@article{tong2025biid,\n  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},\n  author={Tong and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2509.22732},\n  archivePrefix={arXiv},\n}\n\n@article{gguard2025,\n  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.07146},\n  archivePrefix={arXiv},\n}\n\n@article{safedream2026,\n  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2604.16824},\n  archivePrefix={arXiv},\n}\n\n@article{bullwinkel2025repeng,\n  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},\n  author={Bullwinkel and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.02956},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 3: Discourse Analysis in NLP\n% ============================================================\n\n@article{mann1988rst,\n  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},\n  author={Mann, William C. and Thompson, Sandra A.},\n  journal={Text \\& Talk},\n  year={1988},\n  volume={8},\n  number={3},\n  pages={243--281},\n}\n\n@inproceedings{prasad2008pdtb,\n  title={The Penn Discourse TreeBank 2.0},\n  author={Prasad and others},\n  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},\n  year={2008},\n}\n\n@article{stolcke2000dialogueact,\n  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},\n  author={Stolcke and others},\n  journal={Computational Linguistics},\n  year={2000},\n  volume={26},\n  number={3},\n  pages={339--374},\n}\n\n@book{austin1962speechacts,\n  title={How to Do Things with Words},\n  author={Austin, J. L.},\n  publisher={Harvard University Press},\n  year={1962},\n}\n\n@book{searle1969speechacts,\n  title={Speech Acts: An Essay in the Philosophy of Language},\n  author={Searle, J. R.},\n  publisher={Cambridge University Press},\n  year={1969},\n}\n\n% ============================================================\n% Category 4: Computational Persuasion Detection\n% ============================================================\n\n@inproceedings{habernal2016convincingness,\n  title={Which Argument Is More Convincing? Analyzing and Predicting Convincingness of Web Arguments Using Bidirectional LSTM},\n  author={Habernal, Ivan and Gurevych, Iryna},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2016},\n}\n\n@inproceedings{tan2016winningarguments,\n  title={Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-faith Online Discussions},\n  author={Tan and others},\n  booktitle={Proceedings of the International World Wide Web Conference},\n  year={2016},\n}\n\n@article{jaipersaud2025howdollmspersuade,\n  title={How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations},\n  author={Jaipersaud and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2508.05625},\n  archivePrefix={arXiv},\n}\n\n@book{cialdini2001influence,\n  title={Influence: Science and Practice},\n  author={Cialdini, Robert B.},\n  publisher={Allyn \\& Bacon},\n  year={2001},\n  edition={4th},\n}\n\n% ============================================================\n% Category 5: Jailbreak Attacks & Taxonomies\n% ============================================================\n\n@inproceedings{zeng2024pap,\n  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},\n  author={Zeng and others},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2024},\n}\n\n@inproceedings{russinovich2024crescendo,\n  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},\n  author={Russinovich and others},\n  booktitle={USENIX Security Symposium},\n  year={2025},\n  eprint={2404.01833},\n  archivePrefix={arXiv},\n}\n\n@article{chao2023pair,\n  title={Jailbreaking Black Box Large Language Models in Twenty Queries},\n  author={Chao and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2310.08419},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{wei2023jailbroken,\n  title={Jailbroken: How Does LLM Safety Training Fail?},\n  author={Wei and others},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023},\n}\n\n@article{hagendorff2026reasoning,\n  title={Large Reasoning Models Are Autonomous Jailbreak Agents},\n  author={Hagendorff and others},\n  journal={Nature Communications},\n  year={2026},\n}\n\n@article{fitd2024,\n  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2402.15690},\n  archivePrefix={arXiv},\n}\n\n@techreport{deceptivedelight2024,\n  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},\n  author={{Palo Alto Networks Unit 42}},\n  institution={Palo Alto Networks},\n  year={2024},\n}\n\n@inproceedings{ren2024actorattack,\n  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},\n  author={Ren and others},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n@article{zou2023gcg,\n  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},\n  author={Zou and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2307.15043},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 6: Red-Teaming\n% ============================================================\n\n@inproceedings{perez2022redteaming,\n  title={Red Teaming Language Models with Language Models},\n  author={Perez and others},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year={2022},\n}\n\n@article{ganguli2022redteaming,\n  title={Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned},\n  author={Ganguli and others},\n  journal={arXiv preprint},\n  year={2022},\n  eprint={2209.07858},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{mazeika2024harmbench,\n  title={HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal},\n  author={Mazeika and others},\n  booktitle={International Conference on Machine Learning},\n  year={2024},\n}\n\n@article{li2024mhj,\n  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},\n  author={Li and others},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2408.15221},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 7: Annotation Artifacts & Dataset Biases\n% ============================================================\n\n@inproceedings{gururangan2018artifacts,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan and others},\n  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year={2018},\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2019},\n}\n\n@article{poliak2018hypothesis,\n  title={Hypothesis Only Baselines in Natural Language Inference},\n  author={Poliak and others},\n  journal={arXiv preprint},\n  year={2018},\n  eprint={1805.01042},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{schuster2019debiasing,\n  title={Towards Debiasing Fact Verification Models},\n  author={Schuster and others},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year={2019},\n}\n\n% ============================================================\n% Category 8: Adaptive Attacks on Classifiers\n% ============================================================\n\n@article{nasr2025attackermovessecond,\n  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},\n  author={Nasr and Carlini and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2510.09023},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{andriushchenko2024adaptive,\n  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},\n  author={Andriushchenko and others},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n% ============================================================\n% Technical Foundation\n% ============================================================\n\n@inproceedings{he2021deberta,\n  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},\n  author={He and others},\n  booktitle={International Conference on Learning Representations},\n  year={2021},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
    "content": "% References for persuasion_turn_jailbreak_detect\n% Auto-generated from literature_map.yaml (2026-05-18)\n% Total entries: 39\n\n% ============================================================\n% Category 1: Production Multi-Turn Safety Systems\n% ============================================================\n\n@article{inan2023llamaguard,\n  title={Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations},\n  author={Inan and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2312.06674},\n  archivePrefix={arXiv},\n}\n\n@misc{metallamaguard3_2024,\n  title={Llama Guard 3},\n  author={{Meta AI}},\n  year={2024},\n  howpublished={Meta AI (released with Llama 3.1)},\n}\n\n@article{zeng2024shieldgemma,\n  title={ShieldGemma: Generative AI Content Moderation Based on Gemma},\n  author={Zeng and others},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2407.21772},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{han2024wildguard,\n  title={WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs},\n  author={Han and others},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2024},\n}\n\n@article{anthropic2025constitutional,\n  title={Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming},\n  author={{Anthropic}},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2501.18837},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 2: Multi-Turn Jailbreak Defenses\n% ============================================================\n\n@article{deepcontext2026,\n  title={DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2602.16935},\n  archivePrefix={arXiv},\n}\n\n@article{tong2025biid,\n  title={Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks},\n  author={Tong and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2509.22732},\n  archivePrefix={arXiv},\n}\n\n@article{gguard2025,\n  title={An Attention-Aware GNN-Based Input Defender Against Multi-Turn Jailbreak on LLMs},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.07146},\n  archivePrefix={arXiv},\n}\n\n@article{safedream2026,\n  title={SafeDream: Safety World Model for Proactive Early Jailbreak Detection},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2026},\n  eprint={2604.16824},\n  archivePrefix={arXiv},\n}\n\n@article{bullwinkel2025repeng,\n  title={A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks},\n  author={Bullwinkel and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2507.02956},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 3: Discourse Analysis in NLP\n% ============================================================\n\n@article{mann1988rst,\n  title={Rhetorical Structure Theory: Toward a Functional Theory of Text Organization},\n  author={Mann, William C. and Thompson, Sandra A.},\n  journal={Text \\& Talk},\n  year={1988},\n  volume={8},\n  number={3},\n  pages={243--281},\n}\n\n@inproceedings{prasad2008pdtb,\n  title={The Penn Discourse TreeBank 2.0},\n  author={Prasad and others},\n  booktitle={Proceedings of the International Conference on Language Resources and Evaluation},\n  year={2008},\n}\n\n@article{stolcke2000dialogueact,\n  title={Dialogue Act Modeling for Automatic Tagging and Recognition of Conversational Speech},\n  author={Stolcke and others},\n  journal={Computational Linguistics},\n  year={2000},\n  volume={26},\n  number={3},\n  pages={339--374},\n}\n\n@book{austin1962speechacts,\n  title={How to Do Things with Words},\n  author={Austin, J. L.},\n  publisher={Harvard University Press},\n  year={1962},\n}\n\n@book{searle1969speechacts,\n  title={Speech Acts: An Essay in the Philosophy of Language},\n  author={Searle, J. R.},\n  publisher={Cambridge University Press},\n  year={1969},\n}\n\n% ============================================================\n% Category 4: Computational Persuasion Detection\n% ============================================================\n\n@inproceedings{habernal2016convincingness,\n  title={Which Argument Is More Convincing? Analyzing and Predicting Convincingness of Web Arguments Using Bidirectional LSTM},\n  author={Habernal, Ivan and Gurevych, Iryna},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2016},\n}\n\n@inproceedings{tan2016winningarguments,\n  title={Winning Arguments: Interaction Dynamics and Persuasion Strategies in Good-faith Online Discussions},\n  author={Tan and others},\n  booktitle={Proceedings of the International World Wide Web Conference},\n  year={2016},\n}\n\n@article{jaipersaud2025howdollmspersuade,\n  title={How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations},\n  author={Jaipersaud and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2508.05625},\n  archivePrefix={arXiv},\n}\n\n@book{cialdini2001influence,\n  title={Influence: Science and Practice},\n  author={Cialdini, Robert B.},\n  publisher={Allyn \\& Bacon},\n  year={2001},\n  edition={4th},\n}\n\n% ============================================================\n% Category 5: Jailbreak Attacks & Taxonomies\n% ============================================================\n\n@inproceedings{zeng2024pap,\n  title={How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs},\n  author={Zeng and others},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2024},\n}\n\n@inproceedings{russinovich2024crescendo,\n  title={Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack},\n  author={Russinovich and others},\n  booktitle={USENIX Security Symposium},\n  year={2025},\n  eprint={2404.01833},\n  archivePrefix={arXiv},\n}\n\n@article{chao2023pair,\n  title={Jailbreaking Black Box Large Language Models in Twenty Queries},\n  author={Chao and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2310.08419},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{wei2023jailbroken,\n  title={Jailbroken: How Does LLM Safety Training Fail?},\n  author={Wei and others},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023},\n}\n\n@article{hagendorff2026reasoning,\n  title={Large Reasoning Models Are Autonomous Jailbreak Agents},\n  author={Hagendorff and others},\n  journal={Nature Communications},\n  year={2026},\n}\n\n@article{fitd2024,\n  title={Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology},\n  author={Anonymous},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2402.15690},\n  archivePrefix={arXiv},\n}\n\n@techreport{deceptivedelight2024,\n  title={Deceptive Delight: Jailbreak LLMs Through Camouflage and Distraction},\n  author={{Palo Alto Networks Unit 42}},\n  institution={Palo Alto Networks},\n  year={2024},\n}\n\n@inproceedings{ren2024actorattack,\n  title={ActorAttack: Red-Teaming Large Language Models via Multi-Turn Actor Network Theory},\n  author={Ren and others},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n@article{zou2023gcg,\n  title={Universal and Transferable Adversarial Attacks on Aligned Language Models},\n  author={Zou and others},\n  journal={arXiv preprint},\n  year={2023},\n  eprint={2307.15043},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 6: Red-Teaming\n% ============================================================\n\n@inproceedings{perez2022redteaming,\n  title={Red Teaming Language Models with Language Models},\n  author={Perez and others},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year={2022},\n}\n\n@article{ganguli2022redteaming,\n  title={Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned},\n  author={Ganguli and others},\n  journal={arXiv preprint},\n  year={2022},\n  eprint={2209.07858},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{mazeika2024harmbench,\n  title={HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal},\n  author={Mazeika and others},\n  booktitle={International Conference on Machine Learning},\n  year={2024},\n}\n\n@article{li2024mhj,\n  title={LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet},\n  author={Li and others},\n  journal={arXiv preprint},\n  year={2024},\n  eprint={2408.15221},\n  archivePrefix={arXiv},\n}\n\n% ============================================================\n% Category 7: Annotation Artifacts & Dataset Biases\n% ============================================================\n\n@inproceedings{gururangan2018artifacts,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan and others},\n  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics},\n  year={2018},\n}\n\n@inproceedings{niven2019probing,\n  title={Probing Neural Network Comprehension of Natural Language Arguments},\n  author={Niven, Timothy and Kao, Hung-Yu},\n  booktitle={Proceedings of the Association for Computational Linguistics},\n  year={2019},\n}\n\n@article{poliak2018hypothesis,\n  title={Hypothesis Only Baselines in Natural Language Inference},\n  author={Poliak and others},\n  journal={arXiv preprint},\n  year={2018},\n  eprint={1805.01042},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{schuster2019debiasing,\n  title={Towards Debiasing Fact Verification Models},\n  author={Schuster and others},\n  booktitle={Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year={2019},\n}\n\n% ============================================================\n% Category 8: Adaptive Attacks on Classifiers\n% ============================================================\n\n@article{nasr2025attackermovessecond,\n  title={The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections},\n  author={Nasr and Carlini and others},\n  journal={arXiv preprint},\n  year={2025},\n  eprint={2510.09023},\n  archivePrefix={arXiv},\n}\n\n@inproceedings{andriushchenko2024adaptive,\n  title={Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks},\n  author={Andriushchenko and others},\n  booktitle={International Conference on Learning Representations},\n  year={2025},\n}\n\n% ============================================================\n% Technical Foundation\n% ============================================================\n\n@inproceedings{he2021deberta,\n  title={DeBERTa: Decoding-enhanced BERT with Disentangled Attention},\n  author={He and others},\n  booktitle={International Conference on Learning Representations},\n  year={2021},\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T03:59:28.326871+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T03:59:28.327064+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
  "description": "Count BibTeX entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"^@\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
    "description": "Count BibTeX entries"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T03:59:28.327215+00:00_

39

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T03:59:28.327354+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"author={}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
  "description": "Check for empty author fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"author={}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
    "description": "Check for empty author fields"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T03:59:28.327490+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T03:59:28.327648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"title={}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
  "description": "Check for empty title fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"title={}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/references.bib",
    "description": "Check for empty title fields"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T03:59:28.327782+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260518T035730",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-18T03:59:28.327958+00:00_

39 entries, no empty author or title fields。

注意事项：
- `poliak2018hypothesis` 的 venue 原为 "StarSem 2018"，但因无对应会议 arxiv 编号已存在，用了 `@article` + arXiv 格式（与 venue="arXiv preprint" 等效处理）
- `metallamaguard3_2024` 用 `@misc`（无独立论文）
- `deceptivedelight2024` 用 `@techreport`
- `austin1962speechacts`、`searle1969speechacts`、`cialdini2001influence` 用 `@book`
- 多数 "et al." 作者已转为 BibTeX 标准的 "and others" 格式

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_sync_20260518T035730"
}
```

</details>

---
