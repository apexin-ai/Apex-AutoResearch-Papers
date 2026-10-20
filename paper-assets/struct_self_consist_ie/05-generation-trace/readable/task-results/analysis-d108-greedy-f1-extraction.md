# analysis d108 greedy f1 extraction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d108_greedy_f1_extraction_20260516T072432_result.json`
- **Structured JSON:** [`0278c0611b3b57eb81e5.json`](../../sessions/02/0278c0611b3b57eb81e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已保存到 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/d108_greedy_f1/`，artifact 已注册。

**Canonical Greedy F1 Table (16 rows)**

| Model | Dataset | Task | N | Greedy F1 | Sample F1 (mean) | Oracle F1 |
|-------|---------|------|---|-----------|------------------|-----------|
| LLaMA-3.1-8B | CoNLL | NER | 8 | 0.9266 | 0.9207 | 0.9443 |
| LLaMA-3.1-8B | CoNLL | NER | 16 | 0.9264 | 0.9219 | 0.9494 |
| LLaMA-3.1-8B | SciERC | NER | 8 | 0.6607 | 0.6191 | 0.7781 |
| LLaMA-3.1-8B | SciERC | NER | 16 | 0.6575 | 0.6211 | 0.7986 |
| LLaMA-3.1-8B | SciERC | RE | 8 | 0.4319 | 0.3888 | 0.5775 |
| LLaMA-3.2-3B | SciERC | NER | 8 | 0.6386 | 0.5922 | 0.7620 |
| Qwen2.5-7B | CoNLL | NER | 8 | 0.9074 | 0.8665 | 0.9468 |
| Qwen2.5-7B | CoNLL | NER | 16 | 0.9067 | 0.8669 | 0.9544 |
| Qwen2.5-7B | SciERC | NER | 8 | **0.6633** | 0.6077 | 0.7775 |
| Qwen2.5-7B | SciERC | NER | 16 | 0.6589 | 0.6119 | 0.8167 |
| Qwen2.5-7B | SciERC | RE | 8 | **0.4289** | 0.3544 | 0.5796 |
| Qwen2.5-7B | SciERC | RE | 16 | 0.4189 | 0.3590 | 0.6252 |
| Qwen2.5-7B | WNUT-17 | NER | 16 | 0.5232 | 0.4008 | 0.6637 |
| Qwen3-4B | CoNLL | NER | 8 | 0.9251 | 0.9196 | 0.9408 |
| Qwen3-4B | SciERC | NER | 8 | 0.6612 | 0.5991 | 0.7839 |
| Qwen3-4B | SciERC | RE | 8 | 0.4136 | 0.3350 | 0.5846 |

三个参考值全部匹配。完整 96 行数据在 `results.json`。

---
