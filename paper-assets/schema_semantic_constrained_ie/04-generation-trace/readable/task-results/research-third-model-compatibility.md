# research third model compatibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_third_model_compatibility_20260516T023439_result.json`
- **Structured JSON:** [`87ea7a68edd36c863364.json`](../../sessions/87/87ea7a68edd36c863364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/_project/report/third_model_compatibility_report.md`。

**结论: 推荐 Mistral-7B-Instruct-v0.3 作为第三模型。**

核心理由：
- **适配成本极低** (~10 行增量改动)，标准 `MistralForCausalLM` 架构无特殊机制
- **XGrammar 完全兼容**，32K 小 vocab 使 FSM 索引构建更快，无 soft-capping 干扰
- **32K context** 覆盖所有 DocRED 文档，无需截断
- **Apache 2.0** 许可证，无需接受协议

Gemma-2-9B-it 的主要问题：必须用 `eager` attention（慢）、不支持 system role（需改 prompt 构建）、constrained decoding 有重复循环风险、8K context 可能不够。适配约需 30-50 行改动且存在未知风险。

---
