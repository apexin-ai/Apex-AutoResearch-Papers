# code exp002 exposure estimation framework

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_exposure_estimation_framework_20260522T090231_result.json`
- **Structured JSON:** [`4c8bf63a679043e93771.json`](../../sessions/4c/4c8bf63a679043e93771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 文件列表

```
exp002/
├── __init__.py
├── run_exp002.py              # 主入口 CLI
├── sources/
│   ├── __init__.py
│   ├── performance_gap.py     # Source 1: 原始 vs rephrased gap + spline校正
│   ├── temporal_signal.py     # Source 2: pre-cutoff vs post-cutoff
│   └── logprober.py           # Source 3: Min-K% memorisation score
├── composite.py               # 加权合成 + 权重调优
├── validation.py              # ConStat delta vs c_n 相关性验证
└── mock_data.py               # Mock 数据生成
```

## Dry-run 结果

| 指标 | 值 |
|------|-----|
| 30 items, 4 models, 2 judges | 420 judgments |
| Source 1 (gap) | 30 items, raw_gap mean=0.797, corrected mean≈0 |
| Source 2 (temporal) | 15/30 items有temporal scores |
| Source 3 (logprob) | 30 items |
| Composite e_i | mean=0.483, std=0.281 |
| Source coverage | 15 items 有2源, 15 items 有3源 |
| ConStat vs c_n | Spearman ρ=1.000, Pearson r=0.995 |

Mock 数据中注入了差异化 contamination 信号 (gpt-4o=1.5, qwen=1.0, llama=0.3, mistral=0.1)，pipeline 成功检出：spline 校正去掉了 difficulty 成分，ConStat delta 与 c_n 完美相关。exp-001 数据到手后替换 `--data-dir` 即可运行。

---
