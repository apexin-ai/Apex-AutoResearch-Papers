# analysis token overlap 101

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_token-overlap-101_20260522T005647_result.json`
- **Structured JSON:** [`626f09db07799138afda.json`](../../sessions/62/626f09db07799138afda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

| Model | Jaccard | ∩/EN | ∩/ZH | ZH unique tokens |
|-------|---------|------|------|-----------------|
| **Qwen3-8B** | 10.4% | 16.4% | 22.3% | 10,140 |
| **Llama-3.1-8B** | 15.1% | 18.8% | **43.8%** | 7,020 |

Llama 的 ZH token 有 43.8% 与 EN 重叠（Qwen 仅 22.3%），因为 Llama 缺乏专用中文 token，将中文拆成更多 byte-level/共享 subword。Qwen 有大量专用中文 token，EN-ZH 在 token 层面分离度更高，跨语言探针迁移需更多依赖语义层共享表示。

脚本：`/root/clkc_mech_interp/src/token_overlap.py`
报告：`art_20260522_ec166f`

---
