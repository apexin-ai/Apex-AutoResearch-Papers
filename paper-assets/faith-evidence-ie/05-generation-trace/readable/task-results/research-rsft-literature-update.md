# research rsft literature update

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rsft-literature-update_20260515T113125_result.json`
- **Structured JSON:** [`fc0b17d2739152b0d5b4.json`](../../sessions/fc/fc0b17d2739152b0d5b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个产出已生成：

**literature_map.yaml** — 新增 3 个 category（共 11 篇新论文）：
- Category 6: RSFT Methodology & Theory（3 篇）
- Category 7: RL for Information Extraction（5 篇）
- Category 8: Recent LLM-based DocRE Methods（5 篇）

**worker_outputs/rsft_literature_scan.md** — 核心结论：

- **最直接竞争者 R1-RE**（arXiv 2507.04642）用 GRPO 做句子级 RE，与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无
- **无人在 IE/RE 上用过 RSFT**，我们的 novelty 完全成立
- **NLI-based CED reward for RE training** 无先例
- 建议 must-cite 4 篇：R1-RE、"Minimalist Approach"（RSFT 理论）、RelPrior、"RSFT=PPO"（ICML 2025）

---
