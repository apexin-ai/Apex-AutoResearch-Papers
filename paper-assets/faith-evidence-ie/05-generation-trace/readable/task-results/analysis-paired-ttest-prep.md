# analysis paired ttest prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paired_ttest_prep_20260516T024727_result.json`
- **Structured JSON:** [`b9d3ba1801702ce28c5e.json`](../../sessions/b9/b9d3ba1801702ce28c5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。

**产出**: `artifacts/paired_ttest_analysis.py`

**当前 eval 结果状态（3 matched pairs 可用，1 缺失）：**

| Seed | CED RSFT | flat-NLI RSFT |
|------|----------|---------------|
| 42 | ✓ `rsft_r2b` (f1=0.4493) | ✓ `rsft_flat_nli` (f1=0.4539) |
| 43 | ✓ `rsft_s43` (f1=0.4683) | ✓ `rsft_flat_nli_s43_reeval` (f1=0.4523) |
| 44 | ✓ `rsft_s44` (f1=0.4655) | ✓ `rsft_flat_nli_s44` (f1=0.4615) |
| 45 | ✗ `rsft_ced_s45` 空 | ✗ `rsft_flat_nli_s45` 空 |

**运行方式**（在服务器上）：
```bash
python paired_ttest_analysis.py --seeds 42 43 44 --per-doc --output /root/autodl-tmp/eval_results/ttest_results.json
```

脚本功能：
- 读取 `metrics_v2.json`（优先）或 `metrics.json`，按 seed 配对
- Seed-level paired t-test + Cohen's d + 95% CI
- Bootstrap CI（10000 resamples）作为非参数替代
- `--per-doc`：加载 `predictions.json` 计算 per-document rel_f1，逐 seed 和 pooled 做 bootstrap paired comparison
- `--output`：JSON 输出完整统计结果

---
