# research second dataset candidates

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_second_dataset_candidates_20260519T183401_result.json`
- **Structured JSON:** [`3127bc47a4fb99cd25fa.json`](../../sessions/31/3127bc47a4fb99cd25fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/second_dataset_candidates.md`。

核心结论：

**Top-1: ReasoningShield Dataset** — 9.2K 条来自 8 个 LRM 的推理 trace，带句子级安全标注（3 级，κ=0.75），HuggingFace 开源。无需生成 trace，safe→borderline/unsafe 转换可映射为 CP proxy。预计 ~2 小时即可完成数据处理。

**Top-2: AdvBench** — 520 条 harmful prompts，需用 R1-8B 生成 trace + LLM 标注 CP，预计 ~8 小时。规模 10× HarmThoughts，领域差异最大。

**Honorable mention: SORRY-Bench** — 45 个平衡细粒度类别，可做 per-category 层选择分析。

Sources:
- [ReasoningShield Dataset](https://huggingface.co/datasets/ReasoningShield/ReasoningShield-Dataset)
- [ReasoningShield GitHub](https://github.com/CosmosYi/ReasoningShield)
- [XSTest GitHub](https://github.com/paul-rottger/xstest)
- [XSTest Paper (NAACL 2024)](https://aclanthology.org/2024.naacl-long.301/)
- [AdvBench on HuggingFace](https://huggingface.co/datasets/walledai/AdvBench)
- [AdvBench Paper (Zou et al. 2023)](https://arxiv.org/abs/2307.15043)
- [WildGuardMix (NeurIPS 2024)](https://arxiv.org/abs/2406.18495v3)
- [WildJailbreak on HuggingFace](https://huggingface.co/datasets/allenai/wildjailbreak)
- [SORRY-Bench (ICLR 2025)](https://sorry-bench.github.io/)
- [SafeDecoding (ACL 2024)](https://aclanthology.org/2024.acl-long.303/)
- [StrongREJECT](https://huggingface.co/datasets/walledai/StrongREJECT)
- [HEx-PHI](https://huggingface.co/datasets/LLM-Tuning-Safety/HEx-PHI)
- [Annotating the Chain-of-Thought](https://arxiv.org/abs/2510.18154)
- [AISafety-Student Dataset](https://huggingface.co/datasets/AISafety-Student/reasoning-safety-behaviours)
- [SafeRBench](https://arxiv.org/abs/2511.15169)
- [Nvidia Nemotron Safety Dataset](https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset)
- [SafeChain (ACL Findings 2025)](https://aclanthology.org/2025.findings-acl.1197/)
- [Refusal Falls off a Cliff](https://arxiv.org/abs/2510.06036)

---
