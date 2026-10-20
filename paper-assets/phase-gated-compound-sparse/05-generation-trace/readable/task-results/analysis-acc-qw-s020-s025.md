# analysis acc qw s020 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s020_s025_20260515T210225_result.json`
- **Structured JSON:** [`7c854e528ca77ba462f2.json`](../../sessions/7c/7c854e528ca77ba462f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Qwen2.5-7B-Instruct MATH-500 (n=50)

| Condition | Accuracy | 备注 |
|-----------|----------|------|
| dense | 32.0% (16/50) | baseline（来自 qw_s015 文件） |
| importance_s015 | 32.0% (16/50) | 几乎无损 |
| **importance_s020** | **24.0% (12/50)** | heads_pruned=140, kv_evict≈20% |
| **importance_s025** | **26.0% (13/50)** | heads_pruned=196, kv_evict≈25% |
| importance_s030 | 14.0% (7/50) | 断崖下跌 |

### 注意事项

- **s025 > s020 是采样噪声**：差异仅 1 题，n=50 下不显著。两者实质都在 24-26% 区间。
- **degradation 拐点**：s015→s020 出现明显下降（32%→24%），s030 断崖（14%）。s020-s025 处于中间过渡区。
- **无 c2_accuracy_eval 对比数据**：服务器上不存在该文件。
- **两个实验均无异常**：EXIT_CODE=0，无错误。

### 结果文件

- JSON: `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s020.json`, `accuracy_eval_qw_s025.json`
- Log: `~/runs/phase-gated-compound-sparse/acc_qw_s020.log`, `acc_qw_s025.log`
- 分析报告已注册: `art_20260515_b7ca16`

---
