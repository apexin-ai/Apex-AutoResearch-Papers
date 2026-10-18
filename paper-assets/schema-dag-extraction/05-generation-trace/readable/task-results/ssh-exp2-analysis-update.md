# ssh exp2 analysis update

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp2-analysis-update_20260514T232020_result.json`
- **Structured JSON:** [`403c98751ee44caeb9d9.json`](../../sessions/40/403c98751ee44caeb9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是修改摘要：

### Reviewer 必须修正 (A)
1. **主指标改 relaxed F1** — 原来硬编码 `metrics["exact"]["f1"]`，现在通过 `_get_metrics(metrics, eval_mode)` 统一获取，默认 `eval_mode="relaxed"`
2. **禁用 delta 模式** — 删除了 `use_delta=True` 自动启用逻辑，delta 现在仅作为 `delta_supplementary` 输出，主分析直接做 within-count Pearson r(relaxed_F1, BCS)

### D003 功能扩展 (B)
3. **within-count Pearson r** — 每个 count_key 计算 r, p, 95% CI (Fisher z), n，加偏相关 `partial_corr(F1, BCS | count)` 合并分析
4. **recall-only 分析** — 每个 count 同时计算 `r(recall, BCS)` 及偏相关
5. **per-type confusion rate** — 新增 `analyze_confusion()` 函数，从原始预测+ground truth 统计 (gold_type, pred_type) 错标次数，输出 top-K confused pairs 到 `confusion_analysis.json`
6. **eval_mode 参数** — 支持 `"exact"`, `"relaxed"`, `"text_match"`（text_match 不可用时 fallback 到 relaxed）
7. **可视化** — scatter plots 保存为 `exp2_analysis_f1.png`, `exp2_analysis_recall.png`, `*_combined.png`（per-count 分色 + 回归线）

### 验证
- 语法检查通过
- `--help` 正常输出
- 无 eval 文件时 dry-run 不 crash
- 275 行 → 510 行，未触碰 `run_experiment.py` 或 `evaluate.py`

---
