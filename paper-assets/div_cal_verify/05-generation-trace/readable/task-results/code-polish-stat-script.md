# code polish stat script

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_polish_stat_script_20260514T072512_result.json`
- **Structured JSON:** [`99b5641a472d15f3a4c2.json`](../../sessions/99/99b5641a472d15f3a4c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。增强后的 `analyze_355m_3seed.py` 新增了：

1. **`355m_3seed_summary.csv`** — 全量 method×seed×gen 原始数据（与 125M 的 `3seed_summary.csv` 格式一致）
2. **Markdown 表格输出** — Gen7 汇总 + t-test 结果均有 markdown 格式
3. **LaTeX paper-ready 输出** — 可直接粘贴到 `\begin{tabular}`，格式 `$90.25 \pm 3.2$`
4. **Gen7 Ratio 汇总段** — 4 方法的 `selection_rare_ngram_ratio` 均值±SD + LaTeX 格式（D020 鉴别用）
5. **CSV `conclusion` 字段** — 与 125M t-test CSV 字段对齐
6. **Graceful handling** — 部分 seed 缺失时正常降级为 descriptive stats

当前 seed 456 全缺失，t-test 只能出 PARTIAL 结果。seed 456 实验跑完后重新运行即可出完整统计。

---
