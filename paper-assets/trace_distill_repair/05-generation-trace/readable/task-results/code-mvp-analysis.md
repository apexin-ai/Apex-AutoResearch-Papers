# code mvp analysis

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_analysis_20260514T135913_result.json`
- **Structured JSON:** [`66c2f5b0550912a9f731.json`](../../sessions/66/66c2f5b0550912a9f731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器上运行正常。脚本已部署到 `/root/trace_distill_repair/mvp_analysis.py`。

功能总结：
- **Criterion 1**: 从 CSV 统计 trace 收集+结构化解析成功率，阈值 ≥80% pass / <60% kill
- **Criterion 2**: 从 `teacher_scores.json` 或 `teacher_scores/` 目录读取 scored segments，随机抽样计算 precision；支持 ground truth 对比和 confidence proxy 两种模式；数据缺失时标记 DATA_MISSING
- **Criterion 3**: 筛选 >2K token trace 子集，配对比较 structural vs line 的 win rate，exact binomial test 计算 p-value
- **Case study**: 自动选 5 个 structural exclusive win case，按 compression ratio 排序
- **输出**: 格式化判定表 + `mvp_judgment.json` + case study 列表
- **CLI**: `python mvp_analysis.py --results-dir ./mvp_results` 或 `--dry-run` 测试

---
