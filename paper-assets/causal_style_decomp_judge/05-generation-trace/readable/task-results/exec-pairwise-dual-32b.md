# exec pairwise dual 32b

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_pairwise_dual_32b_20260520T175614_result.json`
- **Structured JSON:** [`64575c7b7c0d4fe9c053.json`](../../sessions/64/64575c7b7c0d4fe9c053.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

## 完整报告

### 1. vLLM Kill + GPU 释放
- vLLM 未在运行，无需 kill
- GPU 全部空闲：4×98GB，0 MiB 使用

### 2. 代码同步
- `pairwise_scoring.py` 353 行写入成功
- 关键词 trial1/trial2/dual/consistent 验证通过

### 3. 完整分析 stdout

```
============================================================
  Pairwise Comparison (Position-Controlled)
============================================================
  Total records: 100
  Valid (both trials): 98
  Consistent: 55 (56.1%)
  Ties (inconsistent): 43 (43.9%)

  Position bias:
    Trial 1 chose A: 62/98 (63.3%)
    Trial 2 chose A: 41/98 (41.8%)
    Overall A rate: 103/196 (52.6%)

============================================================
  Overall Results (consistent pairs only)
============================================================
  N = 55
  Formal wins: 38 (69.1%)
  Casual wins: 17 (30.9%)
  Formal win rate: 0.6909
  95% CI (Wilson): [0.5597, 0.7972]
  Sign test p-value: 0.006456

============================================================
  Directional Analysis (consistent only)
============================================================
  formal→casual (n=33)
    Formal wins: 26 (78.8%), p=0.001319
    (formal=original, casual=rewrite → formal win = prefer original)

  casual→formal (n=22)
    Formal wins: 12 (54.5%), p=0.831812
    (casual=original, formal=rewrite → formal win = prefer rewrite)

============================================================
  NLI-Stratified Analysis (consistent only)
============================================================
  NLI≥0.90 (n=46): formal wins 34 (73.9%), p=0.001641
  All (n=55): formal wins 38 (69.1%), p=0.006456
```

### 4. pairwise_summary.csv

| group | n | formal_wins | casual_wins | win_rate | ci_lo | ci_hi | sign_test_p | ties | consistency_rate | position_a_rate |
|---|---|---|---|---|---|---|---|---|---|---|
| overall | 55 | 38 | 17 | 0.6909 | 0.5597 | 0.7972 | 0.006456 | 43 | 0.5612 | 0.5255 |

### 5. pairwise_detailed.csv

| group | n | formal_wins | win_rate | p_value |
|---|---|---|---|---|
| formal→casual | 33 | 26 | 0.7879 | 0.001319 |
| casual→formal | 22 | 12 | 0.5455 | 0.831812 |
| NLI≥0.90 | 46 | 34 | 0.7391 | 0.001641 |
| All | 55 | 38 | 0.6909 | 0.006456 |

### 6. 补充统计

- Total: 100, Valid: 98, Consistent: 55, Ties: 43
- Formal wins: 38, Casual wins: 17
- formal original (n=33): formal_wins=26
- casual original (n=22): formal_wins=12

**注**：去重处理已完成（两个并行进程写入 181 行 → 100 条唯一记录）。产出文件均在 `data/pairwise_results_32b/` 和 `data/pairwise_results_32b.jsonl`。

---
