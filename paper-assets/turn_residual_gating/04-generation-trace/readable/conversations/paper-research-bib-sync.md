# paper research bib sync

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_research_bib_sync_20260519T214929.jsonl`
- **Structured JSON:** [`2b2f58ee4bfe3c401e9d.json`](../../sessions/2b/2b2f58ee4bfe3c401e9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-19T21:52:41.139221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T21:52:41.140259+00:00_

1	categories:
2	  layer_importance:
3	    description: Layer-wise importance analysis, redundancy, and pruning in transformers
4	    papers:
5	    - title: The Unreasonable Ineffectiveness of the Deeper Layers
6	      authors: Gromov et al.
7	      venue: ICLR 2025
8	      year: 2024
9	      url: https://arxiv.org/abs/2403.17887
10	      role: foundation
11	      relevance: 发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要
12	      abstract: Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers
13	        are removed.
14	    - title: 'ShortGPT: Layers in Large Language Models are More Redundant Than You Expect'
15	      authors: Men et al.
16	      venue: arXiv 2024
17	      year: 2024
18	      url: https://arxiv.org/abs/2403.03853
19	      role: foundation
20	      relevance: 提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余
21	      abstract: Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.
22	    - title: The Curse of Depth in Large Language Models
23	      authors: Sun et al.
24	      venue: NeurIPS 2025
25	      year: 2025
26	      url: https://arxiv.org/abs/2502.05795
27	      role: foundation
28	      relevance: Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0
29	      abstract: Pre-Layer Normalization causes output variance to grow exponentially with depth.
30	    - title: 'Reassessing Layer Pruning in LLMs: New Insights and Methods'
31	      authors: Anonymous
32	      venue: arXiv 2024
33	      year: 2024
34	      url: https://arxiv.org/abs/2411.15558
35	      role: context
36	      relevance: 删除最后 25% 层 + 微调即可获得强性能，证实深层冗余
37	      abstract: Simply pruning the final 25% of layers followed by fine-tuning yields strong performance.
38	    - title: Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)
39	      authors: Fan et al.
40	      venue: ICLR 2020
41	      year: 2020
42	      url: https://arxiv.org/abs/1909.11556
43
…[truncated 25424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T21:52:41.140565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
  "offset": "454"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml",
    "offset": "454"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T21:52:41.140878+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (454). The file has 454 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T21:52:41.141245+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if paper directory exists"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T21:52:41.141440+00:00_

acl.sty
acl_natbib.bst

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T21:52:41.141685+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
  "content": "% ============================================================\n% Layer Importance\n% ============================================================\n\n@inproceedings{gromov2024deeper,\n  author    = {Gromov and others},\n  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.17887}\n}\n\n@article{men2024shortgpt,\n  author  = {Men and others},\n  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},\n  journal = {arXiv preprint arXiv:2403.03853},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{sun2025curse,\n  author    = {Sun and others},\n  title     = {{The Curse of Depth in Large Language Models}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.05795}\n}\n\n@article{anonymous2024reassessing,\n  author  = {{Anonymous}},\n  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},\n  journal = {arXiv preprint arXiv:2411.15558},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2411.15558}\n}\n\n@inproceedings{fan2020layerdrop,\n  author    = {Fan and others},\n  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1909.11556}\n}\n\n% ============================================================\n% Multi-Turn Attention\n% ============================================================\n\n@article{dongre2026attention,\n  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},\n  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},\n  journal = {arXiv preprint arXiv:2605.12922},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.12922}\n}\n\n@article{levy2025lost,\n  author  = {Levy and others},\n  title   = {{LLMs Get Lost In Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2505.06120},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.06120}\n}\n\n@article{liu2026intent,\n  author  = {Liu and others},\n  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2602.07338},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.07338}\n}\n\n@article{liu2023lost,\n  author  = {Liu and others},\n  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2307.03172}\n}\n\n@article{anonymous2025style,\n  author  = {{Anonymous}},\n  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},\n  journal = {arXiv preprint arXiv:2512.23578},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2512.23578}\n}\n\n% ============================================================\n% Residual Gating\n% ============================================================\n\n@article{raposo2024mixture,\n  author  = {Raposo and others},\n  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},\n  journal = {arXiv preprint arXiv:2404.02258},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2404.02258}\n}\n\n@inproceedings{schuster2022calm,\n  author    = {Schuster and others},\n  title     = {{Confident Adaptive Language Modeling}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2207.07061}\n}\n\n@inproceedings{qiu2025gated,\n  author    = {Qiu and others},\n  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.06708}\n}\n\n@inproceedings{wang2018skipnet,\n  author    = {Wang and others},\n  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},\n  booktitle = {European Conference on Computer Vision},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.09485}\n}\n\n@article{luo2025flexidepth,\n  author  = {Luo and others},\n  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},\n  journal = {arXiv preprint arXiv:2503.23798},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2503.23798}\n}\n\n@article{lawson2025skip,\n  author  = {Lawson and others},\n  title   = {{Learning to Skip the Middle Layers of Transformers}},\n  journal = {arXiv preprint arXiv:2506.21103},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2506.21103}\n}\n\n% ============================================================\n% Attention Manipulation\n% ============================================================\n\n@inproceedings{press2022alibi,\n  author    = {Press and others},\n  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2108.12409}\n}\n\n@article{chen2023positional,\n  author  = {Chen and others},\n  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},\n  journal = {arXiv preprint arXiv:2306.15595},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2306.15595}\n}\n\n@inproceedings{peng2024yarn,\n  author    = {Peng and others},\n  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.00071}\n}\n\n@inproceedings{xiao2024streaming,\n  author    = {Xiao and others},\n  title     = {{Efficient Streaming Language Models with Attention Sinks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.17453}\n}\n\n@inproceedings{han2024lminfinite,\n  author    = {Han and others},\n  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.16137}\n}\n\n@article{ko2024found,\n  author  = {Ko and others},\n  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},\n  journal = {arXiv preprint arXiv:2406.16008},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.16008}\n}\n\n% ============================================================\n% Theoretical Foundations\n% ============================================================\n\n@article{elhage2021framework,\n  author  = {Elhage and others},\n  title   = {{A Mathematical Framework for Transformer Circuits}},\n  journal = {Anthropic Blog},\n  year    = {2021},\n  url     = {https://transformer-circuits.pub/2021/framework/index.html}\n}\n\n@article{elhage2022superposition,\n  author  = {Elhage and others},\n  title   = {{Toy Models of Superposition}},\n  journal = {arXiv preprint arXiv:2209.10652},\n  year    = {2022},\n  url     = {https://arxiv.org/abs/2209.10652}\n}\n\n@article{belrose2023tuned,\n  author  = {Belrose and others},\n  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},\n  journal = {arXiv preprint arXiv:2303.08112},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2303.08112}\n}\n\n@article{yu2023residual,\n  author  = {Yu and others},\n  title   = {{Exploring the Residual Stream of Transformers}},\n  journal = {arXiv preprint arXiv:2312.12141},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2312.12141}\n}\n\n@inproceedings{makkuva2025markov,\n  author    = {Makkuva and others},\n  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2402.04161}\n}\n\n@inproceedings{ildiz2024markov,\n  author    = {Ildiz and others},\n  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.13512}\n}\n\n% ============================================================\n% Evaluation Benchmarks\n% ============================================================\n\n@inproceedings{zheng2023mtbench,\n  author    = {Zheng and others},\n  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{chiang2024arena,\n  author    = {Chiang and others},\n  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{dubois2024alpacaeval,\n  author    = {Dubois and others},\n  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.04475}\n}\n\n@article{lin2024wildbench,\n  author  = {Lin and others},\n  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},\n  journal = {arXiv preprint arXiv:2406.04770},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.04770}\n}\n\n@inproceedings{bai2024mtbench101,\n  author    = {Bai and others},\n  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14762}\n}\n\n@article{sirdeshmukh2025multichallenge,\n  author  = {Sirdeshmukh and others},\n  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},\n  journal = {arXiv preprint arXiv:2501.17399},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2501.17399}\n}\n\n% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio and Vinyals and Jaitly and Shazeer},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato and Chopra and Auli and Zaremba},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning\n% ============================================================\n\n@inproceedings{yu2020pcgrad,\n  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},\n  title     = {{Gradient Surgery for Multi-Task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2001.06782}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Chen and Badrinarayanan and Lee and Rabinovich},\n  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.02257}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Liu and Liu and Jin and Stone and Liu},\n  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2110.14048}\n}\n\n@inproceedings{navon2022nash,\n  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},\n  title     = {{Multi-Task Learning as a Bargaining Game}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2202.01017}\n}\n\n% ============================================================\n% Residual Scaling\n% ============================================================\n\n@inproceedings{bachlechner2021rezero,\n  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},\n  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},\n  booktitle = {Uncertainty in Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2003.04887}\n}\n\n@inproceedings{zhang2019fixup,\n  author    = {Zhang and Dauphin and Ma},\n  title     = {{Fixup Initialization: Residual Learning Without Normalization}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1901.09321}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
    "content": "% ============================================================\n% Layer Importance\n% ============================================================\n\n@inproceedings{gromov2024deeper,\n  author    = {Gromov and others},\n  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.17887}\n}\n\n@article{men2024shortgpt,\n  author  = {Men and others},\n  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},\n  journal = {arXiv preprint arXiv:2403.03853},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{sun2025curse,\n  author    = {Sun and others},\n  title     = {{The Curse of Depth in Large Language Models}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.05795}\n}\n\n@article{anonymous2024reassessing,\n  author  = {{Anonymous}},\n  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},\n  journal = {arXiv preprint arXiv:2411.15558},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2411.15558}\n}\n\n@inproceedings{fan2020layerdrop,\n  author    = {Fan and others},\n  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1909.11556}\n}\n\n% ============================================================\n% Multi-Turn Attention\n% ============================================================\n\n@article{dongre2026attention,\n  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},\n  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},\n  journal = {arXiv preprint arXiv:2605.12922},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.12922}\n}\n\n@article{levy2025lost,\n  author  = {Levy and others},\n  title   = {{LLMs Get Lost In Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2505.06120},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.06120}\n}\n\n@article{liu2026intent,\n  author  = {Liu and others},\n  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2602.07338},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.07338}\n}\n\n@article{liu2023lost,\n  author  = {Liu and others},\n  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2307.03172}\n}\n\n@article{anonymous2025style,\n  author  = {{Anonymous}},\n  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},\n  journal = {arXiv preprint arXiv:2512.23578},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2512.23578}\n}\n\n% ============================================================\n% Residual Gating\n% ============================================================\n\n@article{raposo2024mixture,\n  author  = {Raposo and others},\n  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},\n  journal = {arXiv preprint arXiv:2404.02258},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2404.02258}\n}\n\n@inproceedings{schuster2022calm,\n  author    = {Schuster and others},\n  title     = {{Confident Adaptive Language Modeling}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2207.07061}\n}\n\n@inproceedings{qiu2025gated,\n  author    = {Qiu and others},\n  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.06708}\n}\n\n@inproceedings{wang2018skipnet,\n  author    = {Wang and others},\n  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},\n  booktitle = {European Conference on Computer Vision},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.09485}\n}\n\n@article{luo2025flexidepth,\n  author  = {Luo and others},\n  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},\n  journal = {arXiv preprint arXiv:2503.23798},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2503.23798}\n}\n\n@article{lawson2025skip,\n  author  = {Lawson and others},\n  title   = {{Learning to Skip the Middle Layers of Transformers}},\n  journal = {arXiv preprint arXiv:2506.21103},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2506.21103}\n}\n\n% ============================================================\n% Attention Manipulation\n% ============================================================\n\n@inproceedings{press2022alibi,\n  author    = {Press and others},\n  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2108.12409}\n}\n\n@article{chen2023positional,\n  author  = {Chen and others},\n  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},\n  journal = {arXiv preprint arXiv:2306.15595},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2306.15595}\n}\n\n@inproceedings{peng2024yarn,\n  author    = {Peng and others},\n  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.00071}\n}\n\n@inproceedings{xiao2024streaming,\n  author    = {Xiao and others},\n  title     = {{Efficient Streaming Language Models with Attention Sinks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.17453}\n}\n\n@inproceedings{han2024lminfinite,\n  author    = {Han and others},\n  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.16137}\n}\n\n@article{ko2024found,\n  author  = {Ko and others},\n  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},\n  journal = {arXiv preprint arXiv:2406.16008},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.16008}\n}\n\n% ============================================================\n% Theoretical Foundations\n% ============================================================\n\n@article{elhage2021framework,\n  author  = {Elhage and others},\n  title   = {{A Mathematical Framework for Transformer Circuits}},\n  journal = {Anthropic Blog},\n  year    = {2021},\n  url     = {https://transformer-circuits.pub/2021/framework/index.html}\n}\n\n@article{elhage2022superposition,\n  author  = {Elhage and others},\n  title   = {{Toy Models of Superposition}},\n  journal = {arXiv preprint arXiv:2209.10652},\n  year    = {2022},\n  url     = {https://arxiv.org/abs/2209.10652}\n}\n\n@article{belrose2023tuned,\n  author  = {Belrose and others},\n  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},\n  journal = {arXiv preprint arXiv:2303.08112},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2303.08112}\n}\n\n@article{yu2023residual,\n  author  = {Yu and others},\n  title   = {{Exploring the Residual Stream of Transformers}},\n  journal = {arXiv preprint arXiv:2312.12141},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2312.12141}\n}\n\n@inproceedings{makkuva2025markov,\n  author    = {Makkuva and others},\n  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2402.04161}\n}\n\n@inproceedings{ildiz2024markov,\n  author    = {Ildiz and others},\n  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.13512}\n}\n\n% ============================================================\n% Evaluation Benchmarks\n% ============================================================\n\n@inproceedings{zheng2023mtbench,\n  author    = {Zheng and others},\n  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{chiang2024arena,\n  author    = {Chiang and others},\n  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{dubois2024alpacaeval,\n  author    = {Dubois and others},\n  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.04475}\n}\n\n@article{lin2024wildbench,\n  author  = {Lin and others},\n  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},\n  journal = {arXiv preprint arXiv:2406.04770},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.04770}\n}\n\n@inproceedings{bai2024mtbench101,\n  author    = {Bai and others},\n  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14762}\n}\n\n@article{sirdeshmukh2025multichallenge,\n  author  = {Sirdeshmukh and others},\n  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},\n  journal = {arXiv preprint arXiv:2501.17399},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2501.17399}\n}\n\n% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio and Vinyals and Jaitly and Shazeer},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato and Chopra and Auli and Zaremba},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning\n% ============================================================\n\n@inproceedings{yu2020pcgrad,\n  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},\n  title     = {{Gradient Surgery for Multi-Task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2001.06782}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Chen and Badrinarayanan and Lee and Rabinovich},\n  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.02257}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Liu and Liu and Jin and Stone and Liu},\n  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2110.14048}\n}\n\n@inproceedings{navon2022nash,\n  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},\n  title     = {{Multi-Task Learning as a Bargaining Game}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2202.01017}\n}\n\n% ============================================================\n% Residual Scaling\n% ============================================================\n\n@inproceedings{bachlechner2021rezero,\n  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},\n  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},\n  booktitle = {Uncertainty in Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2003.04887}\n}\n\n@inproceedings{zhang2019fixup,\n  author    = {Zhang and Dauphin and Ma},\n  title     = {{Fixup Initialization: Residual Learning Without Normalization}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1901.09321}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T21:52:41.142003+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_bib_sync_20260519T214929",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-19T21:52:41.142182+00:00_

共 **45 条** BibTeX entry，覆盖 **9 个** category：

| Category | Count |
|---|---|
| layer_importance | 5 |
| multi_turn_attention | 5 |
| residual_gating | 6 |
| attention_manipulation | 6 |
| theoretical_foundations | 6 |
| evaluation_benchmarks | 6 |
| exposure_bias | 5 |
| gradient_conflict_mtl | 4 |
| residual_scaling | 2 |

文件已写入 `paper/references.bib`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_bib_sync_20260519T214929"
}
```

</details>

---
