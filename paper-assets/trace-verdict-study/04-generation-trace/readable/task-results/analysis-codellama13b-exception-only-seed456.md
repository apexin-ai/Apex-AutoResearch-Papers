# analysis codellama13b exception only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_exception_only_seed456_20260516T224215_result.json`
- **Structured JSON:** [`9c074718bd04b7b17c72.json`](../../sessions/9c/9c074718bd04b7b17c72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B 查询失败（entity 未配置），但 eval 结果和日志都已获取。汇总如下：

## codellama13b_exception_only_seed456 结果

### 核心指标（eval_results.json）

| Metric | Value |
|--------|-------|
| **Accuracy** | 99.83% (CI: 99.58%–100.0%) |
| **Pass F1** | 0.9988 |
| **Fail F1** | 0.9971 |
| Pass Precision | 1.0000 |
| Pass Recall | 0.9976 |
| Fail Precision | 0.9941 |
| Fail Recall | 1.0000 |
| Lift over majority | +28.3pp |
| N (eval samples) | 1190 |

### 训练状态
训练和评估均正常完成（`EXIT_CODE=0`），日志无报错。

### Checkpoint 路径
`/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_exception_only_seed456/final/`

### 3-seed 汇总

seed456 结果与 seed42、seed123 一致（均 ≥99.8% accuracy），**3-seed robustness 验证通过**。exception_only 条件下 CodeLlama-13B 表现极其稳定，跨 seed 方差可忽略不计。

---
