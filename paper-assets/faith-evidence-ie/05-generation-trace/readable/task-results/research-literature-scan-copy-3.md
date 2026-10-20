# research literature scan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260516T002439_result.json`
- **Structured JSON:** [`2ed90597d0904ab2d365.json`](../../sessions/2e/2ed90597d0904ab2d365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。以下是 **Top-5 最相关新发现**：

| # | 论文 | 与 FREIGE 的关系 |
|---|------|-----------------|
| 1 | **RIFT** (arXiv:2601.09253) — 用 reward 加权 loss 替代 hard rejection | 可替代 FREIGE 的 binary CED 筛选，用 CED score 作为连续 reward 做 soft reweighting，充分利用所有生成样本 |
| 2 | **Is Best-of-N the Best of Them?** (ICML 2025) — BoN 的 coverage/scaling/optimality 理论分析 | CED reranker 的理论基础，InferenceTimePessimism 算法可指导 CED threshold 设计 |
| 3 | **Inference-Time Reward Hacking** (NeurIPS 2025 Spotlight) — BoN 中 reward hacking 不可避免 | 警示 CED reranker 过度优化风险，HedgeTune 可自动选择最优 N |
| 4 | **Q-BLoRA** (TACL 2025) — 量化 LLM + LoRA 的不平衡导致欠拟合 | 直接解释 QLoRA GRPO 中 evidence-extraction decoupling 的机制：量化精度限制 + rank 限制 = 双重欠拟合下多任务竞争 |
| 5 | **AdaSTaR** (NeurIPS 2025) — 自适应 curriculum 采样优化 rejection sampling | 可优化 FREIGE RSFT 阶段的数据采样策略，先易后难 + diversity sampling |

新增 5 个 category：inference_time_reranking (5篇)、faithfulness_nli (4篇)，以及扩展了 rsft_methodology、evidence_based_docre、lora_qlora_artifacts、llm_docre 等已有类别。

---
