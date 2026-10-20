# analysis exp wiki llama8b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_llama8b_20260517T193221_result.json`
- **Structured JSON:** [`ec1a5759fb1299e61bc5.json`](../../sessions/ec/ec1a5759fb1299e61bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**exp_wiki_llama8b 结果：K\* = 1（one-wash），conclusion = negative**

| Pair | AUC | 可区分? |
|------|-----|---------|
| 0v1 | 0.9316 | Yes |
| 1v2 | 0.5954 | No |
| 2v3 | 0.5392 | No |
| 3v4 | 0.5221 | No |
| 4v5 | 0.5212 | No |

LLaMA-3.1-8B 在 Wikipedia 上 K\*=1，与 Pythia-1.4B 和 OLMo-1B 一致，假设 K\*=2 不成立。8B scale 未提升 discrimination boundary，说明 model scale 不是 Wikipedia domain 上 K\* 的决定因素。Qwen-1.5B 的 K\*=2 更可能源于架构或训练数据差异。

已完成：
- 分析报告写入 artifacts 并注册（`art_20260517_09b165`）
- Registry 状态更新为 DONE，conclusion=negative，metrics 含所有关键指标

---
