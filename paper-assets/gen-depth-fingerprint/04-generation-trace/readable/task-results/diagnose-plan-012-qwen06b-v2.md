# diagnose plan 012 qwen06b v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-012-qwen06b-v2_20260516T015306_result.json`
- **Structured JSON:** [`b70d368a3f1d5eca36b6.json`](../../sessions/b7/b70d368a3f1d5eca36b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**结论：实验未失败，已成功完成。Cron 误报。**

### 实际状态

| 项目 | 详情 |
|------|------|
| 状态 | **正常完成** |
| 运行时长 | 116.7 min (~7000s)，5-fold 全部跑完 |
| 结果文件 | `/root/gen-depth-fingerprint/results/plan012_qwen06b_seed123_r32_results.json` (6903B, 09:44 写入) |
| GPU | 4x RTX 5090 全部空闲，进程已正常退出 |
| 错误 | 无 traceback、无 OOM、无 kill 信号 |

### 实验结果

| 指标 | v2 (seed=123, r=32) | 对照 (seed=42, r=16) | XGBoost baseline |
|------|---------------------|----------------------|-----------------|
| 5-class macro F1 | **0.5873 ± 0.0047** | 0.583 | 0.5028 |
| 3-class macro F1 | **0.9054 ± 0.0037** | — | 0.7815 |
| Δ vs XGBoost (5-class) | +0.0845 | — | — |

两组超参数结果高度一致（F1 差异 < 0.005），说明模型对 seed 和 LoRA rank 不敏感。

### 误报原因

脚本没有集成 W&B logging（只存 JSON），Cron 检测到"进程不存在 + 无 W&B metrics"后将正常退出误判为失败。

### 建议

1. 将该实验标记为 **succeeded**，结果有效可用
2. Cron 监控逻辑应增加对 result JSON 文件存在性的检查，避免类似误报

---
