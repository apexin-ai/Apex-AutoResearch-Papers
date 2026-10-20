# code exp 004 fix j6

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-004-fix-j6_20260524T132313_result.json`
- **Structured JSON:** [`f02c77295f2fdaa6b0e4.json`](../../sessions/f0/f02c77295f2fdaa6b0e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模式都跑通。结果汇总：

### 修改摘要

`run_baselines_n17.py` 新增：
- `EXCLUDE_JUDGES = ["mistral-large-2"]` 常量
- `filter_excluded_judges()` 函数 — 加载后过滤观测并重映射 judge 索引
- `--include-mistral` flag — 默认 J=6（排除 Mistral），开启后 J=7
- 输出标注 judge 配置（如 `J=6 (excluding mistral-large-2)`）
- 结果 JSON 增加 `n_judges`、`excluded_judges`、`judge_config` 字段

### J=6 vs J=7 τ 值对比

| 模式 | Judges | Obs | τ | ρ |
|------|--------|-----|------|------|
| J=6（默认） | 6 | 17,899 | 0.8088 | 0.9240 |
| J=7（--include-mistral） | 7 | 17,942 | 0.8088 | 0.9240 |

τ/ρ 无差异 — Mistral 仅贡献 43 条观测（0.2%），对 baseline 排名无影响。这符合预期，也验证了排除决策的合理性。

### 运行命令

```bash
# J=6 正式运行
python exp004/run_baselines_n17.py --judgment-dir exp003/judgment_data_n17 --exposure-csv exp002/results/exposure_scores.csv --output-dir exp004/results_n17_j6

# J=7 sensitivity（Appendix）
python exp004/run_baselines_n17.py --judgment-dir exp003/judgment_data_n17 --exposure-csv exp002/results/exposure_scores.csv --output-dir exp004/results_n17_j7 --include-mistral
```

exp-020 完成后可一键运行，只需替换 `--judgment-dir` 路径。

---
