# research literature scan pre paper

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan-pre-paper_20260515T024552_result.json`
- **Structured JSON:** [`b303c9fc2920ffd47371.json`](../../sessions/b3/b303c9fc2920ffd47371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新（35 → 39 篇）。总结如下：

## paper_framing 必引论文覆盖检查

9 篇全部已在 map 中，无缺失：
- Guo et al. 2024 (`curious_decline`) ✓
- Padmakumar & He 2024 (`writing_diversity`) ✓
- Holtzman et al. 2020 (`nucleus_sampling`) ✓
- Stamatatos 2009 (`stamatatos_survey`) ✓
- Koppel et al. 2009 (`koppel_authorship`) ✓
- LLM as Broken Telephone ACL 2025 (`broken_telephone`) ✓
- Shi et al. 2024 (`min_k_percent`) ✓
- Kirchenbauer et al. 2023 (`watermark_llm`) ✓
- CCNet / Wenzek et al. 2020 (`ccnet`) ✓

## 新增 4 篇论文

| ID | 论文 | 类型 | 与项目关联 |
|---|---|---|---|
| `diveye` | Basani & Chen, **"Diversity Boosts AI-Generated Text Detection"**, TMLR 2026 (arxiv 2509.18880) | **新发现** | 用 surprisal diversity 做检测，人类文本离散度/尾部更重——与本项目 shape 特征（entropy_std, tail_decay）直接可比，zero-shot 超 SOTA 33.2% |
| `generator_barrier` | Pu et al., **"Breaking the Generator Barrier"**, arXiv 2604.13692 | **新发现** | 解耦表征做跨生成器泛化检测（20 LLM），与本项目 LOGO 评估目标一致，方法论互补（表征学习 vs 特征工程） |
| `feat_aug_transformer` | Mady et al., **"Feature-Augmented Transformers for Robust AI-Text Detection"**, arXiv 2605.03969 | **新发现** | 语言特征增强 Transformer 跨域迁移，验证了语言特征对泛化性的价值，支撑本项目特征工程路线 |
| `chainwash` | Ameen et al., **"Chainwash: Multi-Step Rewriting Attacks on Watermarks"**, arXiv 2605.05503 | **新发现** | 5-hop 重写链将水印检测率从 87.9% 降到 4.86%，直接证明生成链深度影响检测信号，支撑 depth fingerprint 的非水印被动检测定位 |

近 2 周搜索未发现直接做 **generation depth estimation** 的竞争论文——本项目的 ordinal depth estimation 任务仍属独创。

---
