# analysis 14b ced scoring done

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b-ced-scoring-done_20260523T132656_result.json`
- **Structured JSON:** [`1306084064d1cb4a0f0e.json`](../../sessions/13/1306084064d1cb4a0f0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**14B s43 CED scoring 成功完成。**

| 项目 | 值 |
|------|------|
| 状态 | 成功 |
| 输出目录 | `/root/autodl-tmp/rsft_scored_14b_s43/` |
| 全部打分条数 | 24,216 条 |
| top_k=1 筛选后 | **3,017 条**（覆盖 3,017/3,027 个 doc，12.5% 选择率） |
| `rsft_scores.jsonl` | 77.7 MB |
| `rsft_train.jsonl` | 9.4 MB |
| `rsft_report.json` | 4.6 KB |

**筛选后数据质量（selected_stats）：**
- combined_score: mean=0.766, median=0.767
- F1 reward: mean=0.718, median=0.732
- CED reward: mean=0.696, median=0.711
- format reward: 100% 通过

**cuda:1 已释放**（0 MiB 占用）。cuda:2 和 cuda:3 各约 12GB 在用。

---
