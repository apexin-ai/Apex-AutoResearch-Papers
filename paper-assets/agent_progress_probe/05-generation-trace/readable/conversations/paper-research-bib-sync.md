# paper research bib sync

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_research_bib_sync_20260514T204907.jsonl`
- **Structured JSON:** [`6903689e16fe0d676ad5.json`](../../sessions/69/6903689e16fe0d676ad5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-14T20:52:33.477246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:52:33.477918+00:00_

1	# Literature Map for Agent Progress Probe (EMNLP 2026 ARR)
2	# Generated: 2026-05-14
3	# Paper: Structural Signal Analysis for Progress Stagnation Detection in LLM Agents
4	#
5	# D039 Pivot: Empirical analysis paper. Central finding: stagnation signals are
6	# fundamentally structural (30 features → 0.995 in-domain, 0.967 cross-agent F1),
7	# decisively surpassing NL embeddings (0.906/0.751) and LLM-as-judge (+24.3pp).
8	# TLM is a well-motivated negative finding (3 implementations all fail to beat MV).
9	
10	papers:
11	
12	  # ============================================================
13	  # CATEGORY: direct-competitor
14	  # ============================================================
15	
16	  - id: "xi2025agentprm"
17	    title: "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress"
18	    authors: "Zhiheng Xi, Chenyang Liao, Guanyu Li, Yajie Yang, Wenxiang Chen, Zhihao Zhang, Binghai Wang, Senjie Jin, Yuhao Zhou, Jian Guan, Wei Wu, Tao Ji, Tao Gui, Qi Zhang, Xuanjing Huang"
19	    venue: "arXiv preprint"
20	    year: 2025
21	    arxiv: "2511.08325"
22	    category: "direct-competitor"
23	    role: "主要竞争者：step-level PRM for agent guidance"
24	    key_finding: "用 promise（长期潜力）和 progress（即时进展）两个维度评估 agent 每步决策，实现 8x 计算效率提升"
25	    our_differentiation: "我们是 window-level monitoring（不是 step-level guidance），不需要 outcome labels，目标是 stagnation detection 不是 reward shaping"
26	
27	  - id: "choudhury2025prm"
28	    title: "Process Reward Models for LLM Agents: Practical Framework and Directions"
29	    authors: "Sanjiban Choudhury"
30	    venue: "arXiv preprint"
31	    year: 2025
32	    arxiv: "2502.10325"
33	    category: "direct-competitor"
34	    role: "PRM 框架综述 + InversePRM 方法"
35	    key_finding: "提出 AgentPRM（Monte Carlo rollout actor-critic）和 InversePRM（从 demonstrations 学习 process reward），3B 模型超越 GPT-4o"
36	    our_differentiation: "InversePRM 仍需 demonstration trajectories，我们用 programmatic LFs 替代人工标注；我们关注 monitoring 而非 training signal"

…[truncated 23223 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:52:33.478269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:52:33.478423+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:52:33.478581+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
  "content": "% ==============================================================\n% CATEGORY: direct-competitor\n% ==============================================================\n\n@article{xi2025agentprm,\n  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},\n  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},\n  journal = {arXiv preprint arXiv:2511.08325},\n  year    = {2025},\n}\n\n@article{choudhury2025prm,\n  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author  = {Sanjiban Choudhury},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{li2026toolprmbench,\n  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},\n  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},\n  journal = {arXiv preprint arXiv:2601.12294},\n  year    = {2026},\n}\n\n@article{wang2026planrewardbench,\n  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},\n  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},\n  journal = {arXiv preprint arXiv:2604.08178},\n  year    = {2026},\n}\n\n@inproceedings{chen2025monitoring,\n  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},\n  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},\n  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},\n  year      = {2025},\n}\n\n@article{kale2025weaktostrong,\n  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},\n  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},\n  journal = {arXiv preprint arXiv:2508.19461},\n  year    = {2025},\n}\n\n@article{fan2026agentrm,\n  title   = {Exploring Reasoning Reward Model for Agents},\n  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},\n  journal = {arXiv preprint arXiv:2601.22154},\n  year    = {2026},\n}\n\n@article{qiu2026dataprm,\n  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},\n  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},\n  journal = {arXiv preprint arXiv:2604.24198},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: method-component\n% ==============================================================\n\n@inproceedings{ratner2016dataprogramming,\n  title     = {Data Programming: Creating Large Training Sets, Quickly},\n  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n}\n\n@article{ratner2017snorkel,\n  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},\n  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},\n  journal = {Proceedings of the VLDB Endowment},\n  year    = {2018},\n}\n\n@inproceedings{fu2020flyingsquid,\n  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},\n  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2020},\n}\n\n@inproceedings{zhang2021wrench,\n  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},\n  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n}\n\n@inproceedings{safranchik2020linkedhmm,\n  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},\n  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2020},\n}\n\n@inproceedings{sala2019multiresolution,\n  title     = {Multi-Resolution Weak Supervision for Sequential Data},\n  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{dawid1979em,\n  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},\n  author  = {A. P. Dawid and A. M. Skene},\n  journal = {Journal of the Royal Statistical Society, Series C},\n  year    = {1979},\n}\n\n@inproceedings{nguyen2017hmmcrowd,\n  title     = {Aggregating and Predicting Sequence Labels from Crowd Annotations},\n  author    = {An Thanh Nguyen and Byron C. Wallace and Junyi Jessy Li and Ani Nenkova and Matthew Lease},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2017},\n}\n\n% ==============================================================\n% CATEGORY: evaluation\n% ==============================================================\n\n@article{orlanski2026slopcodebench,\n  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},\n  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},\n  journal = {arXiv preprint arXiv:2603.24755},\n  year    = {2026},\n}\n\n@inproceedings{jimenez2024swebench,\n  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\n  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{yang2024sweagent,\n  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\n  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{wang2025openhands,\n  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\n  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n}\n\n@inproceedings{zhou2024webarena,\n  title     = {WebArena: A Realistic Web Environment for Building Autonomous Agents},\n  author    = {Shuyan Zhou and Frank F. Xu and Hao Zhu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{wang2024mint,\n  title     = {MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback},\n  author    = {Xingyao Wang and Zihan Wang and Jiateng Liu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n% ==============================================================\n% CATEGORY: background\n% ==============================================================\n\n@inproceedings{shinn2023reflexion,\n  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@inproceedings{zhou2024lats,\n  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},\n  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n}\n\n@inproceedings{yao2023tot,\n  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},\n  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@article{cemri2025multiagentfail,\n  title   = {Why Do Multi-Agent LLM Systems Fail?},\n  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},\n  journal = {arXiv preprint arXiv:2503.13657},\n  year    = {2025},\n}\n\n@article{zhu2025agentfail,\n  title   = {Where LLM Agents Fail and How They Can Learn From Failures},\n  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},\n  journal = {arXiv preprint arXiv:2509.25370},\n  year    = {2025},\n}\n\n@article{george2025cycledetection,\n  title   = {Unsupervised Cycle Detection in Agentic Applications},\n  author  = {Felix George and Harshit Kumar and Divya Pathak and others},\n  journal = {arXiv preprint arXiv:2511.10650},\n  year    = {2025},\n}\n\n@article{pipis2025reasoningloop,\n  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},\n  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},\n  journal = {arXiv preprint arXiv:2512.12895},\n  year    = {2025},\n}\n\n@inproceedings{huang2024selfcorrect,\n  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@article{kamoi2024selfcorrection,\n  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},\n  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2024},\n}\n\n@article{liu2026trajad,\n  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},\n  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},\n  journal = {arXiv preprint arXiv:2602.06443},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: technique\n% ==============================================================\n\n@inproceedings{cho2014gru,\n  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},\n  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2014},\n}\n\n@inproceedings{bahdanau2015attention,\n  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},\n  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2015},\n}\n\n@inproceedings{khosla2020supcon,\n  title     = {Supervised Contrastive Learning},\n  author    = {Prannay Khosla and Piotr Teterwak and Chen Wang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n}\n\n@article{zhang2025qwen3embedding,\n  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},\n  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},\n  journal = {arXiv preprint arXiv:2506.05176},\n  year    = {2025},\n}\n\n@article{wang2024e5,\n  title   = {Multilingual E5 Text Embeddings: A Technical Report},\n  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},\n  journal = {arXiv preprint arXiv:2402.05672},\n  year    = {2024},\n}\n\n@article{chen2024bgem3,\n  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},\n  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},\n  journal = {arXiv preprint arXiv:2402.03216},\n  year    = {2024},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
    "content": "% ==============================================================\n% CATEGORY: direct-competitor\n% ==============================================================\n\n@article{xi2025agentprm,\n  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},\n  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},\n  journal = {arXiv preprint arXiv:2511.08325},\n  year    = {2025},\n}\n\n@article{choudhury2025prm,\n  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author  = {Sanjiban Choudhury},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{li2026toolprmbench,\n  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},\n  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},\n  journal = {arXiv preprint arXiv:2601.12294},\n  year    = {2026},\n}\n\n@article{wang2026planrewardbench,\n  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},\n  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},\n  journal = {arXiv preprint arXiv:2604.08178},\n  year    = {2026},\n}\n\n@inproceedings{chen2025monitoring,\n  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},\n  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},\n  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},\n  year      = {2025},\n}\n\n@article{kale2025weaktostrong,\n  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},\n  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},\n  journal = {arXiv preprint arXiv:2508.19461},\n  year    = {2025},\n}\n\n@article{fan2026agentrm,\n  title   = {Exploring Reasoning Reward Model for Agents},\n  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},\n  journal = {arXiv preprint arXiv:2601.22154},\n  year    = {2026},\n}\n\n@article{qiu2026dataprm,\n  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},\n  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},\n  journal = {arXiv preprint arXiv:2604.24198},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: method-component\n% ==============================================================\n\n@inproceedings{ratner2016dataprogramming,\n  title     = {Data Programming: Creating Large Training Sets, Quickly},\n  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n}\n\n@article{ratner2017snorkel,\n  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},\n  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},\n  journal = {Proceedings of the VLDB Endowment},\n  year    = {2018},\n}\n\n@inproceedings{fu2020flyingsquid,\n  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},\n  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2020},\n}\n\n@inproceedings{zhang2021wrench,\n  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},\n  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n}\n\n@inproceedings{safranchik2020linkedhmm,\n  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},\n  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2020},\n}\n\n@inproceedings{sala2019multiresolution,\n  title     = {Multi-Resolution Weak Supervision for Sequential Data},\n  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{dawid1979em,\n  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},\n  author  = {A. P. Dawid and A. M. Skene},\n  journal = {Journal of the Royal Statistical Society, Series C},\n  year    = {1979},\n}\n\n@inproceedings{nguyen2017hmmcrowd,\n  title     = {Aggregating and Predicting Sequence Labels from Crowd Annotations},\n  author    = {An Thanh Nguyen and Byron C. Wallace and Junyi Jessy Li and Ani Nenkova and Matthew Lease},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2017},\n}\n\n% ==============================================================\n% CATEGORY: evaluation\n% ==============================================================\n\n@article{orlanski2026slopcodebench,\n  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},\n  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},\n  journal = {arXiv preprint arXiv:2603.24755},\n  year    = {2026},\n}\n\n@inproceedings{jimenez2024swebench,\n  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\n  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{yang2024sweagent,\n  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\n  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{wang2025openhands,\n  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\n  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n}\n\n@inproceedings{zhou2024webarena,\n  title     = {WebArena: A Realistic Web Environment for Building Autonomous Agents},\n  author    = {Shuyan Zhou and Frank F. Xu and Hao Zhu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{wang2024mint,\n  title     = {MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback},\n  author    = {Xingyao Wang and Zihan Wang and Jiateng Liu and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n% ==============================================================\n% CATEGORY: background\n% ==============================================================\n\n@inproceedings{shinn2023reflexion,\n  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@inproceedings{zhou2024lats,\n  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},\n  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n}\n\n@inproceedings{yao2023tot,\n  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},\n  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@article{cemri2025multiagentfail,\n  title   = {Why Do Multi-Agent LLM Systems Fail?},\n  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},\n  journal = {arXiv preprint arXiv:2503.13657},\n  year    = {2025},\n}\n\n@article{zhu2025agentfail,\n  title   = {Where LLM Agents Fail and How They Can Learn From Failures},\n  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},\n  journal = {arXiv preprint arXiv:2509.25370},\n  year    = {2025},\n}\n\n@article{george2025cycledetection,\n  title   = {Unsupervised Cycle Detection in Agentic Applications},\n  author  = {Felix George and Harshit Kumar and Divya Pathak and others},\n  journal = {arXiv preprint arXiv:2511.10650},\n  year    = {2025},\n}\n\n@article{pipis2025reasoningloop,\n  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},\n  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},\n  journal = {arXiv preprint arXiv:2512.12895},\n  year    = {2025},\n}\n\n@inproceedings{huang2024selfcorrect,\n  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@article{kamoi2024selfcorrection,\n  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},\n  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2024},\n}\n\n@article{liu2026trajad,\n  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},\n  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},\n  journal = {arXiv preprint arXiv:2602.06443},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: technique\n% ==============================================================\n\n@inproceedings{cho2014gru,\n  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},\n  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2014},\n}\n\n@inproceedings{bahdanau2015attention,\n  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},\n  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2015},\n}\n\n@inproceedings{khosla2020supcon,\n  title     = {Supervised Contrastive Learning},\n  author    = {Prannay Khosla and Piotr Teterwak and Chen Wang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n}\n\n@article{zhang2025qwen3embedding,\n  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},\n  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},\n  journal = {arXiv preprint arXiv:2506.05176},\n  year    = {2025},\n}\n\n@article{wang2024e5,\n  title   = {Multilingual E5 Text Embeddings: A Technical Report},\n  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},\n  journal = {arXiv preprint arXiv:2402.05672},\n  year    = {2024},\n}\n\n@article{chen2024bgem3,\n  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},\n  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},\n  journal = {arXiv preprint arXiv:2402.03216},\n  year    = {2024},\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:52:33.478893+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:52:33.479034+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "@",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Grep",
  "tool_args": {
    "pattern": "@",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
    "output_mode": "count"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:52:33.479178+00:00_

38

Found 0 total occurrences across 0 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260514T204907",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T20:52:33.479348+00:00_

38 个 `@` 条目，对应 literature_map.yaml 中全部 38 篇论文。按 5 个 category 分组（direct-competitor 8, method-component 8, evaluation 6, background 10, technique 6），venue 已映射为全称，>5 作者截断为前 3 + others。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_sync_20260514T204907"
}
```

</details>

---
