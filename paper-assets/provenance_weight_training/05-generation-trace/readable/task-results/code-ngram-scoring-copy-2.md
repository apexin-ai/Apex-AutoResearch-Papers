# code ngram scoring

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ngram_scoring_20260518T130533_result.json`
- **Structured JSON:** [`e2a53f41caebd80b25d4.json`](../../sessions/e2/e2a53f41caebd80b25d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。371,499 行输出，每行含 `ngram_ppl` 字段。

## 结果摘要

**N-gram PPL 统计 (trigram, add-k=0.01, 训练于 164,889 real samples)**

| | n | mean | median | std | p5 | p25 | p75 | p95 |
|---|---|---|---|---|---|---|---|---|
| **Real (depth=0)** | 164,889 | 1516.11 | 1135.11 | 1598.48 | 282.62 | 678.60 | 1846.32 | 3905.34 |
| **Synth (depth=1)** | 206,387 | 1506.49 | 473.32 | 5734.81 | 112.72 | 256.98 | 952.85 | 4241.58 |

**关键发现**：
- Synthetic text 的 n-gram PPL **更低**（median 473 vs 1135），说明合成文本的 n-gram 模式更可预测/模板化
- **AUC = 0.7319**（lower PPL = synthetic），作为纯统计基线不错
- **与 q_score 的相关性**：Spearman r = -0.3555，是一个不同的信号源（中等负相关，说明两者提供互补信息）
- 最佳阈值分类准确率：**69.1%**（threshold=720.20）

**产出文件**：`/root/autodl-tmp/provenance_weight_training/data/scored_data_ngram.jsonl`
**脚本**：`/root/autodl-tmp/provenance_weight_training/scoring/score_ngram_ppl.py`

---
