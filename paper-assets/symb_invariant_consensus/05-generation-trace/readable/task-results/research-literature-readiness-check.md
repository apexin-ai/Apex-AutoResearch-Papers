# research literature readiness check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-readiness-check_20260516T044343_result.json`
- **Structured JSON:** [`c74c2e506b9918ad5889.json`](../../sessions/c7/c74c2e506b9918ad5889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文献就绪度评估

**已补全 6 个维度、23 篇论文：**

| 维度 | 状态 | 关键补充 |
|------|------|----------|
| SC 及变体 | ✅ 完备 | Loo 2025 (SC diminishing returns)、CISC、USC、ReASC |
| 符号推理+LLM | ✅ 完备 | Logic-LM、DyLoS (EACL 2026)、FoVer |
| MAX-SAT/约束+NLP | ⚠️ 可用但薄 | LLM Meets CP (IJCAI 2025)、SATBench — SICA 的 WPMS formulation 无直接先例，属新颖贡献 |
| FOLIO/ProofWriter SOTA | ✅ 完备 | LogicAgent、Aristotle (ACL 2025)、Symbolic Provers (ICLR 2025) |
| Reasoning model trace 多样性 | ✅ 关键支撑 | Loo 2025 + Diversity-Aware TTS + DeepSeek-R1 定义 reasoning model 范式 |
| Multi-path aggregation | ✅ 补充 | RC method、CREST |

**仍需注意：**
1. QwQ-32B 3.6% 多候选率是原创实证发现，无直接文献复现——需在论文中清晰 frame 为 empirical observation，引 Loo 2025 作间接支撑
2. WPMS 作为 multi-path consensus 机制在 NLI 中无先例——Related Work 需明确说明 novelty
3. 确认 "CRAFT" 是否为已发表方法还是内部缩写

---
