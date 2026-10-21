# code exp003 rrf prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003_rrf_prep_20260516T021029_result.json`
- **Structured JSON:** [`fb03692e9a5af7353b35.json`](../../sessions/fb/fb03692e9a5af7353b35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**代码路径**: `/root/contamcal-irt-calibration/exp003/rrf_aggregation.py` (423 行)

### 发现并修复的问题

| # | 问题 | 修复 |
|---|------|------|
| 1 | DEPRECATED 目录未过滤 | 添加 `SKIP_PATTERNS` 黑名单，`aggregate_all_models` 跳过匹配目录 |
| 2 | `DOSAGES` 含不存在的 d050 | 改为 `["d000", "d005", "d025", "d100"]` |
| 3 | 输出缺原始 signal scores | `aggregate_single` 输出增加各 signal 原始值 |
| 4 | 缺 CSV 输出 | 新增 `write_csv()` + `--csv` 标志，列含 item_id/benchmark/model_size/dose/seed/rrf_score/各signal分数和rank |
| 5 | 缺 dry-run 限制 | 新增 `--limit N` 参数贯穿全链路 |
| 6 | 缺目录名解析 | 新增 `parse_model_dir()` 从目录名提取 model_size/dose/seed |

### RRF 公式验证
`score(j) = Σ_s w_s / (k + rank_s(j))`，k=60，等权，rank 含 tie averaging — 正确。

### Dry-run 结果
- 单目录模式 `Qwen2.5-0.5B_d005_s42 --limit 100`: 3 benchmarks × 100 items，正常
- 全模型模式 `--dosage-filter d005 --limit 50 --csv`: 4 目录 × 3 benchmarks × 50 items = 600 行 CSV，DEPRECATED 目录被跳过

### 3B signals 完成度

| 目录 | s1 | s2 | s4 | merged | 状态 |
|------|----|----|----|----|------|
| d005_s123 | 3/3 | 3/3 | 3/3 | 3/3 | 完成 |
| d005_s42 | 3/3 | 3/3 | 1/3 | 1/3 | 进行中 |
| d025_s123 | 3/3 | 3/3 | 2/3 | 2/3 | 进行中(mmlu s4) |
| d025_v3_s42 | 3/3 | 3/3 | 0/3 | 0/3 | 等待 s4 |
| d100_s42 | 3/3 | 3/3 | 2/3 | 2/3 | 进行中(mmlu) |
| d100_a32_s123 | 1/3 | 1/3 | 0/3 | 0/3 | 早期 |
| d000_v2_s42 | 3/3 | 3/3 | 0/3 | 0/3 | 等待 s4 |

3B signals 完成后，执行：
```bash
python3 exp003/rrf_aggregation.py --output-dir /root/autodl-tmp/exp003/results --csv
```

---
