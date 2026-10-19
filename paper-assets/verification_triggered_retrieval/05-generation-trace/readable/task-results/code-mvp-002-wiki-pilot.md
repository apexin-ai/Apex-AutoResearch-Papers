# code mvp 002 wiki pilot

**verification triggered retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_002_wiki_pilot_20260517T094105_result.json`
- **Structured JSON:** [`5673f60a2705f80305d8.json`](../../sessions/56/5673f60a2705f80305d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验全部完成。以下是 **MVP v2 Wikipedia-Scale Pilot 实验结果汇报**：

---

## 实验配置
- **Corpus**: Tevatron/wikipedia-nq-corpus, 21,015,324 passages (DPR 100-word splits)
- **Index**: Locally built BM25 Lucene index (19GB)
- **Queries**: 复用 mvp_001 前 50 questions (402 claim-query pairs)
- **Pipeline**: BM25 retrieval top-5 → NLI DeBERTa-v3-large evaluation

## 1. NLI Entailment Score

| Metric | Answer-seeking | Verification | Diff |
|--------|---------------|-------------|------|
| Entailment rate (>0.5) | 0.5647 (std=0.314) | 0.5318 (std=0.309) | **-3.28 pp** |
| Mean entailment score | 0.5625 | 0.5321 | **-0.0304** |
| t-statistic | — | — | -2.818 |
| p-value | — | — | **0.00507** |
| Cohen's d | — | — | **-0.141** |

**结论**：Verification queries 显著**更差**（不是更好），差异 -3.28pp，p=0.005，效应量 small (d=-0.14)。

## 2. Top-5 Overlap Rate

| Bucket | Count | Percentage |
|--------|-------|-----------|
| 0-20% | 70 | 17.4% |
| 20-40% | 41 | 10.2% |
| 40-60% | 79 | 19.7% |
| 60-80% | 61 | 15.2% |
| 80-100% | 151 | 37.6% |

- **Mean overlap: 53.0%** (median: 60%)
- 相比 mvp_001（小 corpus）overlap 显著下降，说明在大 corpus 上两种 query 确实检索到不同的文档

## 3. Low-Overlap Sample Cases

Overlap 最低的 cases 全部来自 "Ed Wood" 相关 claims：
- Answer-seeking query "What is Ed Wood's profession?" 检索到相关人物传记（Chris Husbands, Paul Marco）
- Verification query "Evidence supporting Ed Wood was an American filmmaker..." 检索到 Ed Wood 电影相关页面
- 关键发现：**尽管 overlap=0%（完全不同的文档），answer-seeking 的 entailment 反而更高**

## 4. Kill Criteria 判断

**KILL: overlap decreased but entailment diff ≤ 0**

- overlap 从 mvp_001 的 ~90%+ 下降到 53% ✓ （两种 query 确实检索到了不同文档）
- 但 entailment diff = **-3.28pp**（verification 更差，不是更好）✗
- 统计显著（p=0.005）地朝**错误方向**

核心假设被推翻：在大 corpus 上，verification queries 检索到了不同的文档，但这些文档**更不利于验证 claims**，而不是更有利。Answer-seeking queries 反而能找到更相关的 evidence。

---

所有输出已保存到 `/root/verification_triggered_retrieval/mvp_experiment_v2/outputs/`。

---
