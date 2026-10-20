# recovery check and restart

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_check_and_restart_20260524T111358_result.json`
- **Structured JSON:** [`adfdfbce22760078385d.json`](../../sessions/ad/adfdfbce22760078385d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验恢复完成。汇总：

## 恢复结果

### 1. gemma27b_filtering — 无需重启
实际状态：**9/9 runs 全部完成**（非之前以为的 4/9），所有 eval_results.json 完整。

| Strategy | Seed | MMLU | HellaSwag |
|----------|------|------|-----------|
| no_filter | 42 | 0.5960 | 0.6638 |
| no_filter | 123 | 0.5954 | 0.6636 |
| no_filter | 456 | 0.5953 | 0.6626 |
| binary_ours | 42 | 0.5975 | 0.6775 |
| binary_ours | 123 | 0.5946 | 0.6620 |
| binary_ours | 456 | 0.5953 | 0.6626 |
| graduated_a09 | 42 | 0.5954 | 0.6636 |
| graduated_a09 | 123 | 0.5953 | 0.6626 |
| graduated_a09 | 456 | 0.5953 | 0.6626 |

### 2. code_domain_olmo — 分析步骤修复完成
- 生成 (depth 0-5) + 特征提取 (features.csv, 33000 rows): 重启前已完成
- 分析步骤因 bug 失败：`int(doc_id)` 不兼容字符串 ID `code_py_0`
- 已修复 `run_pipeline.py` 第 453 行，重跑分析成功

**code_olmo 结果：**
- K* = 1（仅 depth 0 vs 1 可区分）
- AUC(0v1) = 0.9996, AUC(1v2) = 0.5567, AUC(2v3+) ≈ 0.50
- JSD(0v1) = 0.334, JSD(1v2+) ≈ 0.003-0.006
- Ordinal MAE = 1.289, Accuracy = 0.346

**GPU 状态：4 张卡全部空闲 (0% utilization, 0 MiB)。**

---
