# exp probe cosine sim 117

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_probe-cosine-sim-117_20260523T073547_result.json`
- **Structured JSON:** [`5a9a1d3236a17d5639bc.json`](../../sessions/5a/5a9a1d3236a17d5639bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。同步本地脚本文件也已保存。

## 结果汇报

### Peak Cosine Similarity

| 模型 | 语言 | Peak Layer | Cosine Sim | Random Baseline |
|------|------|-----------|------------|-----------------|
| Llama-3.1-8B | en | 13 | 0.0497 | 0.0003 |
| Llama-3.1-8B | zh | 8 | 0.0462 | 0.0003 |
| Qwen3-8B | en | 4 | 0.0236 | 0.0003 |
| Qwen3-8B | zh | 9 | 0.0407 | 0.0003 |
| Gemma-2-9B | en | 19 | 0.0415 | 0.0010 |
| Gemma-2-9B | zh | 20 | 0.0356 | 0.0010 |

### 结论

**Cosine similarity 极低，接近 0。** Peak 值在 0.02–0.05 之间，虽然略高于随机基线（~0.001），但绝对值非常小。这表明 conflict 探针和 XNLI 探针学到的方向几乎正交——**不支持 "signal piggyback" 假设**。两个任务的信息编码在不同的子空间中。

### 输出文件

- 数据：`data/probe_cosine_similarity.json`
- 图片：`figures/paper/cosine_similarity.pdf` / `.png`

---
