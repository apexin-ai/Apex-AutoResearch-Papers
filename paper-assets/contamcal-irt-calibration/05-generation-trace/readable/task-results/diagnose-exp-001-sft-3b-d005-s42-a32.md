# diagnose exp 001 sft 3B d005 s42 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_3B_d005_s42_a32_20260516T015151_result.json`
- **Structured JSON:** [`0cfa88c00c3737547a4b.json`](../../sessions/0c/0cfa88c00c3737547a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 失败根因：**非真正失败——训练已完成**

EXIT_CODE=129 (SIGHUP) 发生在训练结束**之后**。日志明确显示：
- 3177/3177 步全部完成 (100%)，epoch=1.0
- `2026-05-16 09:46:39 [INFO] LoRA adapter saved to .../Qwen2.5-3B_d005_s42/lora_adapter`
- `2026-05-16 09:46:39 [INFO] Training complete.`
- 最终 train_loss=1.137，mean_token_accuracy=0.752

SIGHUP 原因：训练完成后进程的父 shell/tmux session 断开，导致 hangup 信号。训练本身无任何错误。

### 训练进度
- **3177/3177 步**，完整 1 epoch，耗时 4h08m33s
- 无 OOM、无 CUDA 错误

### Checkpoint 状态
完整保存，可直接使用：
- `adapter_model.safetensors` (114MB) — 时间戳 09:46
- `adapter_config.json` — 已保存
- `checkpoint-3177/` 目录也存在

### cuda:0 当前状态
- PID 642763 占用 8976MiB（eval 进程仍在运行）
- GPU-Util 0%，温度 27°C，处于空闲/低负载状态

### 非致命警告
日志头部有 bitsandbytes `libnvJitLink.so.13` 加载失败的 warning，但未影响训练。

### 结论
**无需重试。** 训练已成功完成，checkpoint 完整。EXIT_CODE=129 是训练结束后的 SIGHUP，不影响结果。可以直接用 `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter` 进行后续 eval/信号计算。

---
