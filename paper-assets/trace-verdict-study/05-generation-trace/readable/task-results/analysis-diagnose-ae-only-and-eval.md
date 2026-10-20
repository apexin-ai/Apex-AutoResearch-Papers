# analysis diagnose ae only and eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnose_ae_only_and_eval_20260519T171858_result.json`
- **Structured JSON:** [`c30d12f9e1df56beddbf.json`](../../sessions/c3/c30d12f9e1df56beddbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 列表为空，无需删除（已被之前的 session 清除或未在当前 session 创建）。

---

## 诊断报告

| 项目 | 结果 |
|------|------|
| **训练状态** | 成功完成。`final/` 目录存在，含 adapter_model.safetensors (239MB)，3 个中间 checkpoint (148/296/444) |
| **Accuracy** | **99.08%** [98.49%, 99.58%] |
| **Pass F1** | 0.9935 |
| **Fail F1** | 0.9840 |
| **Majority baseline** | 0.7151 |
| **Lift** | +27.6pp |
| **Registry** | 已更新 metrics/checkpoint_path/log_path/conclusion=success/status=DONE |
| **Cron** | 当前 session 无活跃 cron，无需清除 |

假设验证：CodeLlama-13B ae_only 达 99.08% accuracy，与 Qwen-7B ae_only (99.92%) 一致，确认 assertion error only ablation 跨 LLaMA 架构泛化成功。

---
