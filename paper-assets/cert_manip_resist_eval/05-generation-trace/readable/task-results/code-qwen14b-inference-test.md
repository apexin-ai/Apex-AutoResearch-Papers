# code qwen14b inference test

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen14b-inference-test_20260521T194130_result.json`
- **Structured JSON:** [`970595da2f83c32856a3.json`](../../sessions/97/970595da2f83c32856a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试通过。完整结果汇总：

## Qwen2.5-14B-Instruct-AWQ 端到端推理链测试结果

| 指标 | 结果 |
|------|------|
| **模型加载时间** | 56.1s（torch.compile cache hit，实际编译仅 5.25s） |
| **Pairwise 推理时间** | 47.9s（30 pairs） |
| **吞吐量** | 0.6 pairs/sec（峰值 ~200 toks/s input, ~43 toks/s output） |
| **Valid response 比例** | 26/30 (87%)，parse errors = 0 |
| **Winner 分布** | A=5, B=21, tie=0 |
| **Likert 结果** | 5/5 valid — scores: [3, 3, 2, 2, 5] |
| **Unload** | 成功（EngineCore shutdown complete） |
| **总耗时** | 153.9s |
| **判定** | **PASSED** |

**样本输出：**
- `[0]` winner=A, score_a=5, score_b=2 — LIFO/inflation 库存问题，正确判断
- `[1]` winner=A, score_a=5, score_b=2 — 矩阵维度判断正确
- `[2]` winner=B, score_a=2, score_b=5 — 规范性/描述性伦理分类正确

4 个 invalid responses（26/30 = 87%）未报 parse error，说明是 JSON 结构正确但内容不符合预期（如 winner 与 score 不一致等）。整体管道 vLLM load → pairwise → Likert → JSON parse → unload 全链路通过。

---
