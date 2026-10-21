# research related work v2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_v2_20260520T203349_result.json`
- **Structured JSON:** [`7255c7a53b391339f1fd.json`](../../sessions/72/7255c7a53b391339f1fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。5 篇重点论文的主要补充：

- **Mesting 2026**：补充了具体 5 个 facets 名称、测试基准（AILuminate/MMLU/Chatbot Arena）、prompt×judge 交互 12.4%、D-study 实用结果（3 judges→38% SE reduction）
- **Yuan 2025**：补充了 9,000-token 回复长度偏移、reasoning models 最受影响、GPU 数量/类型也是变异源
- **Brittlebench 2026**：补充了 63% 排名反转数据、我们参考其扰动协议生成 prompt paraphrase
- **ThinkingMachines 2025**：补充了具体模型（Qwen3-8B）、框架（vLLM）、非确定性逐层定位（RMSNorm→GEMM→attention）、我们使用默认设置反映真实条件
- **Messina 2026**：补充了浮点非结合性作为理论根因、precision × temperature 交互预期

所有条目统一为 4 字段格式（核心发现/方法/与本工作的关系/我们的差异化）。Bui 和 Same Prompt 两篇信息不足处已标注 `[需补充]`。

---
