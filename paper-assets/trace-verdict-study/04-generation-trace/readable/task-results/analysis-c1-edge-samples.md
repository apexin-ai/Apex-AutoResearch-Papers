# analysis c1 edge samples

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1-edge-samples_20260516T054253_result.json`
- **Structured JSON:** [`0d9d9d69ec9d21a884ef.json`](../../sessions/0d/0d9d9d69ec9d21a884ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C1 边缘样本分析结果

找到 **8 个边缘样本**（ground_truth=pass 但 trace 包含真实异常）：

| idx | problem_id | gt | SFT_pred | B5_pred | exception_type | SFT正确 | B5正确 |
|-----|-----------|-----|----------|---------|----------------|---------|--------|
| 540 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 541 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 542 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 543 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 548 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 549 | MBPP/113 | pass | pass | fail | ValueError | ✓ | ✗ |
| 901 | HumanEval/95 | pass | fail | fail | **GeneratorExit** | ✗ | ✗ |
| 905 | HumanEval/95 | pass | fail | fail | **GeneratorExit** | ✗ | ✗ |

### 统计

- **SFT 正确: 6/8 (75%)**
- **B5 正确: 0/8 (0%)**
- **Delta: +6/8**

### 异常类型分布
- ValueError: 6 (全部来自 MBPP/113，`int('python')` 触发，SFT 全部正确识别为 pass)
- GeneratorExit: 2 (来自 HumanEval/95，**irreducible error**，SFT 和 B5 都错)

### 关键发现

6 个 ValueError 样本：异常是 try/except 结构中被正确捕获的预期行为（检测字符串是否为数字），SFT 学会了区分"被捕获的异常≠测试失败"。

2 个 GeneratorExit 样本：Python generator 被 GC 回收时自动触发，与代码正确性无关，但在 trace 中表现为异常。这是 **irreducible error** —— SFT 也无法正确处理，两种方法都预测为 fail。

结果已保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/c1_edge_samples.json`。

---
