# research related work gaps w3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_gaps_w3_20260515T144828_result.json`
- **Structured JSON:** [`987bf10d849afac45d41.json`](../../sessions/98/987bf10d849afac45d41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files are written. Here's the summary:

## 完成情况

### literature_map.yaml 更新
所有条目已补充以下信息：
- **R1-RE**: 补充 reward 设计细节（format +1/-3, metric +2/-1.5）、未出现 catastrophic forgetting、句子级 vs 文档级 GRPO 成败分析
- **DAPO**: 补充 entropy collapse 根因（clipping 不对称性）、Dynamic Sampling 与我们 frac_zero_std 的对应关系
- **Dr. GRPO**: 补充 difficulty bias + length bias 两个机制、std→0 时 advantage 爆炸的技术细节
- **"Minimalist Approach"**: 补充 RAFT 与 GRPO 核心区别（负样本处理）、对 RSFT 的理论支持
- **DocRE 方法**全部补充了 F1 数据和 evidence_generation 标记：
  - RelPrior: DocRED test 48.34, Re-DocRED test 54.80
  - AutoRE: DocRED test 45.96, Re-DocRED test 51.97
  - LMRC: DocRED test 60.52, Re-DocRED test 74.63 (hybrid, 非纯 LLM)
  - GLiDRE: Re-DocRED test 77.83 (encoder-based, 非 LLM)
  - Ru-LLM: Springer 付费墙，声称超越 AutoRE 等 baseline
- **Contrastive rewards**: 补充两步机制细节、与 CED 的三点关键差异

### gap_analysis_w3.md
写入 `artifacts/gap_analysis_w3.md`，包含：
- 每篇论文的关键发现和数据
- 与 FREIGE 的关系分析
- 论文引用策略建议（按 related work 子节组织）

**关键发现：所有 LLM-based DocRE 方法均不生成 evidence，FREIGE 是唯一联合抽取 relation+evidence 的方法。**

---
