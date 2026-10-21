# analysis llama scierc unconstrained

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_scierc_unconstrained_20260514T134815_result.json`
- **Structured JSON:** [`b26097d27d7a7dc62aca.json`](../../sessions/b2/b26097d27d7a7dc62aca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总结果：

## llama_scierc_unconstrained 实验结果

| 指标 | Llama-3.1-8B | Qwen3-8B | 差异 |
|------|-------------|----------|------|
| Entity Type Violation | **0.0%** | 0.4% | Llama 更好 |
| Relation Vocab Violation | **0.5%** | 1.39% | Llama 更好 |
| Domain/Range Violation | **13.3%** | 15.37% | Llama 略好 |
| Entity F1 | 23.56% | **31.01%** | Llama 低 7.5pp |
| Relation F1 | 2.68% | **8.23%** | Llama 低 5.5pp |

**结论**：Llama-3.1-8B 在 unconstrained 设定下 violation rate 全面低于 Qwen3-8B，但 F1 显著更差。原因是 Llama 提取更保守（2451 entities / 1274 relations vs Qwen3 更多的提取量），violation 自然少，但 recall 也随之下降。Qwen3 在 SciERC 上作为 unconstrained baseline 质量优于 Llama，后续 OntoCoDec constrained 实验中 Llama 有更大的 violation 压缩空间（DR 从 13.3% 降至 ~0）但 F1 提升潜力需要验证。

---
