# ssh ae only investigation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ae_only_investigation_20260515T120816_result.json`
- **Structured JSON:** [`42c98dff72ce95db8137.json`](../../sessions/42/42c98dff72ce95db8137.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查报告：vota_ae_only_seed42

### 结论：训练和评估均已正常完成

**进程状态**：进程已退出，属于正常完成（不是崩溃）。日志显示训练完成后自动进入 eval 阶段，eval 也已跑完并保存结果。

**eval_results.json 完整内容**：

| 指标 | 值 |
|------|-----|
| Accuracy | **99.92%** (CI: [99.75%, 100.0%]) |
| Majority baseline | 71.5% (always predict "pass") |
| Lift over majority | +28.4pp |
| pass P/R/F1 | 1.00 / 0.999 / 0.999 |
| fail P/R/F1 | 0.997 / 1.00 / 0.999 |
| 测试样本数 | 1190 |

**Checkpoint 文件** — 完整存在于 `/root/autodl-tmp/trace-verdict-study-checkpoints/ae_only/final/`：
- `adapter_model.safetensors` — 154MB (LoRA adapter)
- `adapter_config.json`, `tokenizer.json`, `training_args.bin` 等辅助文件齐全
- `eval_results.json` — 1.2KB，已写入

**GPU 状态**：
- GPU 0: 71567/97887 MiB, 100% utilization（被其他任务占用）
- GPU 1: 16765/97887 MiB, 95% utilization（被其他任务占用，**不空闲**）

### 总结

ae_only 实验已正常完成（训练 + eval），accuracy 99.92%。进程消失是因为任务跑完自然退出，不是崩溃。两张 GPU 当前都在被其他任务使用。

---
