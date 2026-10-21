# research humaneval para check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_humaneval-para-check_20260516T044347_result.json`
- **Structured JSON:** [`7d2e05118a9874cc9095.json`](../../sessions/7d/7d2e05118a9874cc9095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 结果

### Part 1: Paraphrased HumanEval pass@1 分布
- 26 个模型评测，每个 26 题
- **范围 0%-26.9%**，均值约 11.5%
- 6 个模型得 0 分（完全地板效应）
- **不是全部为零**，但方差极低，仅 1.5B d100 两个模型超过 20%
- 对比原始 HumanEval（164 题）：范围 6.1%-30.5%，方差明显更大

### Part 2: IRT Item Pool 确认
- `run_irt_stan.py:39` 的 `skip_para=True` **已排除 paraphrased 目录**
- Paraphrased HumanEval 不会进入 IRT response matrix

### Part 3: 已添加 Item 方差过滤
- **修改文件**：`artifacts/exp006_irt_calibration/run_irt_stan.py`
- 新增 `filter_low_variance_items()` 函数（lines 113-151）
- 在 `run_real_data()` 循环中调用（line 442），在构建 exposure matrix 之前执行
- 默认阈值 `min_variance=0.01`（对应 p<0.01 或 p>0.99 的 item）
- CLI 新增 `--min-item-variance` 参数
- 过滤后正确对齐 exposure scores（通过 `item_keep_mask`）
- 输出 JSON 包含 `n_items_excluded` 和 `excluded_item_indices` 字段

---
